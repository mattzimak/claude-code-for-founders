#!/usr/bin/env python3
"""build.py - render README.md deterministically from data/ + config/sections.json + templates/README.template.md.

Inputs
  data/links.csv          one row per link (from the Notion sync)
  data/notes.json         field notes grouped by section / subsection (from the Notion sync)
  data/enrichment.json    stars, license, last push, titles, link status (from tools/enrich.py; optional)
  data/overrides.json     {"<id>": {"name": ..., "description": ..., "url": ..., "why": ..., "install": ..., "hide": true}}
                          hide: true keeps the row in data/ but out of every rendered file (say why in "_why")
  config/sections.json    section order, blurbs, subsection order, min_entries (global, or per section),
                          optional notes_file + notes_index (see --notes-file below)
  templates/README.template.md   placeholders: {{header_line}} {{toc}} {{start_here}} {{sections}} {{stats}}
  templates/FIELD-NOTES.template.md   placeholders: {{header_line}} {{toc}} {{sections}} (only with a notes file)

Rules
  - name: override > oEmbed/page title when the sync could only name the entry from its URL > sync name
  - description: override > Notion note (a note under 30 chars is completed with the source's own summary)
    > GitHub / oEmbed / page description > a generic label by link kind (never empty)
  - url: override > GitHub rename target (status 'redirected' on github.com) > sync url
  - entry line: - [Name](url) - description. Why: ... (Matt: 8/10) · `install` · 2.5k stars · MIT · updated 2026-08
    missing fields are simply omitted
  - entries sorted by name inside each section; 'Start here' = rating >= 8 or a Why, sorted by rating
  - no timestamps of its own: the only date is the last link check, so two runs give the same file
  - --notes-file FIELD-NOTES.md (or "notes_file" in config/sections.json): every note goes to that file, grouped by
    section and subsection; README.md keeps the link entries, one pointer line per section that has notes, and an
    index of the notes file inside the section named by "notes_index". Off by default: README.md is unchanged.
Stdlib only, Python 3.9+. Run from the repo root: python3 tools/build.py [--notes-file FIELD-NOTES.md]
"""
import argparse
import csv
import json
import os
import re
import unicodedata
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = {
    "links": os.path.join(ROOT, "data", "links.csv"),
    "notes": os.path.join(ROOT, "data", "notes.json"),
    "enrich": os.path.join(ROOT, "data", "enrichment.json"),
    "overrides": os.path.join(ROOT, "data", "overrides.json"),
    "config": os.path.join(ROOT, "config", "sections.json"),
    "template": os.path.join(ROOT, "templates", "README.template.md"),
    "notes_template": os.path.join(ROOT, "templates", "FIELD-NOTES.template.md"),
    "readme": os.path.join(ROOT, "README.md"),
}
MIN_DESC = 30
KIND_LABEL = {"github": "GitHub repository", "youtube": "YouTube video", "x": "Post on X", "instagram": "Instagram post",
              "threads": "Post on Threads", "linkedin": "LinkedIn post", "reddit": "Reddit thread",
              "app-store": "App Store listing", "skill-directory": "Skill directory page", "site": "Web page"}
URL_RE = re.compile(r"https?://\S+")


# ----------------------------------------------------------------------------- text
def norm(s):
    """NFKC (math-bold letters -> plain), long dashes -> hyphen, nbsp -> space, collapse whitespace."""
    s = unicodedata.normalize("NFKC", s or "")
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Cf")  # zero-width and direction marks
    for ch in ("–", "—", "‒", "―", "‑", "−", "‐"):
        s = s.replace(ch, "-")
    s = s.replace(" ", " ").replace("…", "...")
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    return s.strip()


def one_line(s):
    return re.sub(r"\s*\n\s*", " ", norm(s)).strip()


def esc(s):
    """Escape the few markdown characters that would change meaning inside link text and descriptions."""
    return (s.replace("\\", "\\\\").replace("*", "\\*").replace("[", "\\[").replace("]", "\\]")
            .replace("<", "&lt;").replace("`", "'"))


def sentence(s):
    s = one_line(s).rstrip(" -:;,")
    if s and s[-1] not in ".!?\"')":
        s += "."
    return s


def host_of(url):
    h = (urllib.parse.urlsplit(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def url_key(url):
    p = urllib.parse.urlsplit(url.strip())
    return (host_of(url), p.path.rstrip("/").lower(), p.query)


def anchor(text):
    """GitHub heading anchor (without the duplicate suffix - see anchors_for)."""
    a = norm(text).lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def anchors_for(headings):
    """Assign GitHub-style anchors to headings in document order (duplicates get -1, -2, ...)."""
    seen, out = {}, []
    for h in headings:
        a = anchor(h)
        n = seen.get(a, 0)
        seen[a] = n + 1
        out.append(a if n == 0 else "%s-%d" % (a, n))
    return out


def fmt_stars(n):
    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""
    if n < 1000:
        return "%d stars" % n
    if n < 10000:
        s = "%.1f" % (n / 1000.0)
        return (s[:-2] if s.endswith(".0") else s) + "k stars"
    return "%dk stars" % (n // 1000)


def trim(s, limit=220):
    s = one_line(URL_RE.sub("", s or ""))
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    if len(s) <= limit:
        return s
    cut = s[:limit]
    m = re.search(r"^(.+[.!?])\s", cut)
    if m and len(m.group(1)) >= 40:
        return m.group(1)
    return cut[:cut.rfind(" ")] + "..."


# ----------------------------------------------------------------------------- data
def load_all():
    with open(P["links"], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with open(P["notes"], encoding="utf-8") as f:
        notes = json.load(f).get("sections", {})
    enrich = {}
    if os.path.exists(P["enrich"]):
        with open(P["enrich"], encoding="utf-8") as f:
            enrich = json.load(f)
    overrides = {}
    if os.path.exists(P["overrides"]):
        with open(P["overrides"], encoding="utf-8") as f:
            overrides = json.load(f)
    with open(P["config"], encoding="utf-8") as f:
        config = json.load(f)
    with open(P["template"], encoding="utf-8") as f:
        template = f.read()
    return rows, notes, enrich, overrides, config, template


def site_stars(notes_field):
    for tok in (notes_field or "").split(";"):
        tok = tok.strip()
        if tok.startswith("site_stars:"):
            try:
                return int(tok.split(":", 1)[1])
            except ValueError:
                return None
    return None


def source_description(row, enr):
    for key in ("gh_description", "oembed_text", "page_description"):
        v = trim(enr.get(key, ""))
        if v and len(v) >= 12:
            return v
    return ""


def resolve_name(row, enr, ov):
    if ov.get("name"):
        return one_line(ov["name"])
    if "name-from-url" in (row.get("notes") or ""):
        for key in ("oembed_title", "page_title"):
            t = one_line(enr.get(key, ""))
            t = re.sub(r"\s*[|\-]\s*(YouTube|GitHub|Medium|Substack|App Store|Mac App Store)\s*$", "", t)
            if t and 3 <= len(t) <= 90 and not URL_RE.search(t):
                return t
    return one_line(row["name"])


def resolve_description(row, enr, ov):
    if ov.get("description"):
        return one_line(ov["description"])
    own = trim(row.get("description", ""), 400)
    src = source_description(row, enr)
    if len(own) >= MIN_DESC:
        return own
    if own and src and src.lower() != own.lower():
        return own.rstrip(".") + " - " + src
    if own:
        return own
    if src:
        return src
    label = KIND_LABEL.get(row.get("kind", ""), "Web page")
    author = one_line(enr.get("oembed_author", ""))
    return label + (" by " + author if author else "")


def resolve(rows, enrich, overrides):
    out = []
    for row in rows:
        enr = enrich.get(row["id"]) or {}
        ov = overrides.get(row["id"]) or {}
        if ov.get("hide"):
            continue  # hidden by hand (data/overrides.json "hide": true) - stays in data/ for the record
        url = ov.get("url") or row["url"]
        if not ov.get("url") and enr.get("status") == "redirected" and host_of(url) == "github.com" \
                and enr.get("final_url") and host_of(enr["final_url"]) == "github.com":
            url = enr["final_url"]  # the repository was renamed: follow it
        stars = enr.get("stars")
        if stars is None:
            stars = site_stars(row.get("notes"))
        e = {
            "id": row["id"], "section": row["section"], "subsection": row["subsection"], "kind": row["kind"],
            "url": url, "name": resolve_name(row, enr, ov), "description": resolve_description(row, enr, ov),
            "why": one_line(ov.get("why", row.get("why", ""))), "rating": row.get("rating", ""),
            "install": one_line(ov.get("install", row.get("install", ""))),
            "also_urls": [u for u in (row.get("also_urls") or "").split() if u],
            "stars": stars, "license": enr.get("license", ""), "pushed_at": enr.get("pushed_at", ""),
            "archived": bool(enr.get("archived")), "status": enr.get("status", ""),
        }
        out.append(e)
    primaries = {url_key(e["url"]) for e in out}
    for e in out:
        ov = overrides.get(e["id"]) or {}
        if isinstance(ov.get("also_urls"), list):
            e["also_urls"] = [u for u in ov["also_urls"] if u]
        also_status = (enrich.get(e["id"]) or {}).get("also") or {}
        keep = []
        for u in e["also_urls"]:
            rec = also_status.get(u) or {}
            final = rec.get("final_url") or u
            if url_key(u) in primaries or url_key(final) in primaries:
                continue  # already listed as an entry of its own
            if url_key(u) == url_key(e["url"]) or e["url"].lower().startswith(final.rstrip("/").lower() + "/"):
                continue  # the entry's own repository root (e.g. a renamed repo)
            if rec.get("status") == "dead":
                continue  # checked and gone (an unchecked secondary link is kept)
            keep.append(u)
        e["also_urls"] = keep[:3]
    return out


# ----------------------------------------------------------------------------- rendering
def entry_line(e, with_section=False):
    parts = ["- [%s](%s) - %s" % (esc(e["name"]), e["url"], esc(sentence(e["description"])))]
    if e["why"]:
        parts[0] += " Why: " + esc(sentence(e["why"]))
    if e["rating"]:
        parts[0] += " (Matt: %s/10)" % e["rating"]
    meta = []
    if e["install"]:
        meta.append("`%s`" % e["install"].replace("`", ""))
    if e["stars"] is not None and fmt_stars(e["stars"]):
        meta.append(fmt_stars(e["stars"]))
    if e["license"]:
        meta.append(e["license"])
    if e["pushed_at"]:
        meta.append("updated " + e["pushed_at"][:7])
    if e["archived"]:
        meta.append("archived")
    for u in e["also_urls"]:
        meta.append("also: [%s](%s)" % (host_of(u), u))
    if with_section:
        meta.append(e["section"] + (" / " + e["subsection"] if e["subsection"] else ""))
    line = parts[0]
    if meta:
        line += " · " + " · ".join(meta)
    return line


def code_fence(text, lang, indent):
    fence = "````" if "```" in text else "```"
    lang = {"plain text": "text", "shell": "bash", "plain": "text"}.get((lang or "").lower(), (lang or "").lower())
    pad = " " * indent
    body = unicodedata.normalize("NFKC", text).replace(" ", " ").rstrip("\n")
    lines = [pad + fence + lang]
    lines += [(pad + l) if l.strip() else "" for l in body.split("\n")]
    lines.append(pad + fence)
    return lines


NOTE_OVERRIDES = {}  # {"<block_id>": {"text": "..."}} from data/overrides.json["_notes"], set by build()
ENTRY_INDEX = {}     # id -> resolved entry, set by build(); lets notes point at an entry listed in another section
LABEL_RE = re.compile(r"\((?:\s*(?:Link|Source|Post|Site|Article|Video|Thread|Docs|GitHub|Repo|Website|Homepage"
                      r"|Tutorial|Guide|Readme)\s*(?:[·/,|+&]|and)?\s*)+\)", re.I)


def note_text(n):
    """A note's text after overrides and light cleanup (unfinished trailing parenthetical, dangling separators)."""
    ov = NOTE_OVERRIDES.get(n.get("block_id", ""))
    text = ov["text"] if ov and ov.get("text") else n["text"]
    text = one_line(text)
    text = LABEL_RE.sub(" ", text)                    # "(Link)" whose link was a private redirect and got dropped
    text = re.sub(r"\s*\([^)]*$", "", text)          # "(settings - claude code -" left unfinished in Notion
    text = re.sub(r"(?:\s*[-,;|]\s*)+$", "", text)     # dangling separators
    return text.strip()


def render_notes(items, base_indent, skip_root=True):
    """Render note blocks as a nested bullet list. Returns (lines, count)."""
    lines, count = [], 0
    items = [n for n in items if not (skip_root and n["type"] == "toggle" and n["depth"] == 0)]
    if not items:
        return lines, 0
    min_depth = min(n["depth"] for n in items)
    prev_bullet_indent = None
    prev_type = None
    for n in items:
        indent = base_indent + 2 * (n["depth"] - min_depth)
        pad = " " * indent
        t = n["type"]
        if t == "code":
            ci = (prev_bullet_indent + 2) if prev_bullet_indent is not None else indent
            lines += code_fence(n["text"], n.get("language", ""), ci)
            count += 1
            prev_type = t
            continue
        if t == "table_row":
            cells = [esc(one_line(c)) or "(none)" for c in n.get("cells", [])]
            cells = ["(none)" if c in ("-", "n/a", "N/A") else c for c in cells]
            text = " | ".join(cells)
            if prev_type != "table_row":
                text = "**" + text + "**"
        else:
            text = esc(note_text(n))
        if not text:
            continue
        if t in ("heading", "toggle"):
            text = "**" + text.rstrip(":") + "**"
        elif t == "quote":
            text = "> " + text
        lines.append(pad + "- " + text)
        prev_bullet_indent = indent
        prev_type = t
        count += 1
    return lines, count


def render_group(entries, notes, base_indent=0, split=False):
    """Entries (sorted by name) with their attached notes, then the free-standing notes.
    Returns (lines, note_lines, n_entries, n_notes). With split=True every note goes to note_lines (the notes file);
    lines then carries the entry lines only."""
    lines, note_lines, n_notes = [], [], 0
    by_entry = {}
    free = []
    for n in notes:
        if n.get("entry_id"):
            by_entry.setdefault(n["entry_id"], []).append(n)
        else:
            free.append(n)
    ids = {e["id"] for e in entries}
    pointers = []  # notes attached to an entry that is listed in another section (first section wins)
    for eid, ns in list(by_entry.items()):
        if eid not in ids:
            if eid in ENTRY_INDEX:
                pointers.append((ENTRY_INDEX[eid], ns))
            else:
                free.extend(ns)
            del by_entry[eid]
    target = note_lines if split else lines
    for e in sorted(entries, key=lambda x: (x["name"].casefold(), x["url"])):
        lines.append(" " * base_indent + entry_line(e))
        if e["id"] in by_entry:
            if split:
                target.append(" " * base_indent + "- [%s](%s):" % (esc(e["name"]), e["url"]))
            sub, c = render_notes(by_entry[e["id"]], base_indent + 2, skip_root=False)
            target += sub
            n_notes += c
    for ref, ns in sorted(pointers, key=lambda p: p[0]["name"].casefold()):
        where = ref["section"] + (" / " + ref["subsection"] if ref["subsection"] else "")
        target.append(" " * base_indent + "- [%s](%s) - my notes on it; the entry itself is under %s:" % (esc(ref["name"]), ref["url"], where))
        sub, c = render_notes(ns, base_indent + 2, skip_root=False)
        target += sub
        n_notes += c + 1
    free_lines, c = render_notes(free, base_indent)
    target += free_lines
    n_notes += c
    return lines, note_lines, len(entries), n_notes


def build(notes_file=None):
    """Render README.md (and the notes file when one is configured). Returns (readme, notes_doc, stats, entries);
    notes_doc is "" when no notes file is in use."""
    rows, notes, enrich, overrides, config, template = load_all()
    if notes_file is None:
        notes_file = config.get("notes_file") or ""
    split = bool(notes_file)
    notes_index = config.get("notes_index", "") if split else ""
    NOTE_OVERRIDES.clear()
    NOTE_OVERRIDES.update(overrides.get("_notes") or {})
    entries = resolve(rows, enrich, overrides)
    ENTRY_INDEX.clear()
    ENTRY_INDEX.update({e["id"]: e for e in entries})
    cfg_sections = config["sections"]
    stats = {"entries": len(entries), "sections": {}, "notes": 0, "unlisted_sections": []}
    headings = []       # in document order, for anchors
    body = []

    # Start here
    start = [e for e in entries if e["why"] or (e["rating"] and e["rating"].isdigit() and int(e["rating"]) >= 8)]
    start.sort(key=lambda e: (-(int(e["rating"]) if e["rating"].isdigit() else 0), e["name"].casefold()))
    # config/sections.json "start_here_max": keep the section short; 0 or missing = no cap
    start_max = int(config.get("start_here_max", 0) or 0)
    if start_max > 0 and len(start) > start_max:
        start = start[:start_max]
    start_lines = []
    if start:
        headings.append("Start here")
        start_lines = ["## Start here", "", "What I would send a founder who has one evening: my highest-rated picks and the first entries I wrote a reason for. The full list follows.", ""]
        start_lines += [entry_line(e, with_section=True) for e in start]

    known = {s["name"] for s in cfg_sections}
    per = []  # one record per section: rendered README lines, notes-file lines, the subsections shown in each
    for sec in cfg_sections:
        name = sec["name"]
        sec_entries = [e for e in entries if e["section"] == name]
        sec_notes = notes.get(name, {})
        subs_present = sorted({e["subsection"] for e in sec_entries if e["subsection"]} | {k for k in sec_notes if k})
        order = [s for s in sec.get("subsections", []) if s in subs_present] + \
                [s for s in subs_present if s not in sec.get("subsections", [])]
        rec = {"name": name, "blurb": sec.get("blurb", "").strip(), "readme": [], "notes": [],
               "subs_readme": [], "subs_notes": [], "n_e": 0, "n_n": 0}
        # ungrouped content first (subsection "")
        lines, nlines, a, b = render_group([e for e in sec_entries if not e["subsection"]], sec_notes.get("", []), split=split)
        rec["readme"] += lines
        if lines:
            rec["readme"].append("")
        rec["notes"] += nlines
        if nlines:
            rec["notes"].append("")
        rec["n_e"] += a
        rec["n_n"] += b
        for sub in order:
            lines, nlines, a, b = render_group([e for e in sec_entries if e["subsection"] == sub], sec_notes.get(sub, []), split=split)
            if lines or not split:  # with a notes file, a subsection made of notes only lives in that file
                rec["subs_readme"].append(sub)
                rec["readme"] += ["### " + sub, ""] + lines + [""]
            if nlines:
                rec["subs_notes"].append(sub)
                rec["notes"] += ["### " + sub, ""] + nlines + [""]
            rec["n_e"] += a
            rec["n_n"] += b
        per.append(rec)
        stats["sections"][name] = {"entries": rec["n_e"], "notes": rec["n_n"], "items": rec["n_e"] + rec["n_n"]}
        stats["notes"] += rec["n_n"]

    # the notes file: sections in README order, only those that have notes
    notes_doc = ""
    notes_anchor = {}
    if split:
        with open(P["notes_template"], encoding="utf-8") as f:
            notes_template = f.read()
        nheadings = ["Contents"]
        nbody = []
        for rec in per:
            if not rec["notes"]:
                continue
            nheadings.append(rec["name"])
            nheadings += rec["subs_notes"]
            nbody += ["## " + rec["name"], "",
                      "Links for this section are in [README.md](README.md#%s)." % anchor(rec["name"]), ""] + rec["notes"]
        nanchors = anchors_for(nheadings)
        pos = 1
        ntoc = []
        for rec in per:
            if not rec["notes"]:
                continue
            notes_anchor[rec["name"]] = nanchors[pos]
            ntoc.append("- [%s](#%s) (%d notes)" % (rec["name"], nanchors[pos], rec["n_n"]))
            pos += 1
            for sub in rec["subs_notes"]:
                ntoc.append("  - [%s](#%s)" % (sub, nanchors[pos]))
                pos += 1
        n_secs = len(notes_anchor)
        notes_header = "%d notes in %d sections · built from the same data as README.md" % (stats["notes"], n_secs)
        notes_doc = notes_template
        notes_doc = notes_doc.replace("{{header_line}}", notes_header)
        notes_doc = notes_doc.replace("{{toc}}", "\n".join(ntoc))
        notes_doc = notes_doc.replace("{{sections}}", "\n".join(nbody).rstrip())
        notes_doc = re.sub(r"\n{3,}", "\n\n", notes_doc).rstrip() + "\n"
        stats["notes_sections"] = n_secs

    for rec in per:
        name = rec["name"]
        headings.append(name)
        body += ["## " + name, "", rec["blurb"], ""]
        if split and name == notes_index and notes_anchor:
            body.append("Everything I wrote down, grouped by section, lives in [%s](%s):" % (notes_file, notes_file))
            body.append("")
            for r2 in per:
                if r2["notes"]:
                    body.append("- [%s](%s#%s) - %d notes" % (r2["name"], notes_file, notes_anchor[r2["name"]], r2["n_n"]))
            body.append("")
        body += rec["readme"]
        headings += rec["subs_readme"]
        if split and rec["notes"] and name != notes_index:
            body.append("My notes on this section: [%s](%s#%s) (%d notes)." % (name, notes_file, notes_anchor[name], rec["n_n"]))
            body.append("")
        if body and body[-1] != "":
            body.append("")
    for e in entries:
        if e["section"] not in known and e["section"] not in stats["unlisted_sections"]:
            stats["unlisted_sections"].append(e["section"])
    for name in notes:
        if name not in known and name not in stats["unlisted_sections"]:
            stats["unlisted_sections"].append(name)

    headings += ["How this list is built", "License"]
    anchors = dict(zip(headings, anchors_for(headings)))  # duplicate names get their first anchor; see toc below
    ordered_anchors = anchors_for(headings)
    toc = []
    pos = 0
    if start:
        toc.append("- [Start here](#%s)" % ordered_anchors[pos])
        pos += 1
    for rec in per:
        toc.append("- [%s](#%s)" % (rec["name"], ordered_anchors[pos]))
        pos += 1
        for sub in rec["subs_readme"]:
            toc.append("  - [%s](#%s)" % (sub, ordered_anchors[pos]))
            pos += 1
    toc.append("- [How this list is built](#%s)" % ordered_anchors[pos])
    toc.append("- [License](#%s)" % ordered_anchors[pos + 1])

    checked = [enrich[e["id"]] for e in entries if e["id"] in enrich and enrich[e["id"]].get("http_status") is not None]
    dead = sum(1 for r in checked if r.get("status") == "dead")
    last = max((r.get("last_checked", "") for r in checked), default="")
    if checked and last:
        header = "%d entries · last verified %s · %d links checked · %d dead" % (len(entries), last, len(checked), dead)
    else:
        header = "%d entries · links not verified yet (run tools/enrich.py)" % len(entries)
    stats_line = "Current build: %d entries in %d sections, %d field notes. Links checked: %d, dead: %d, last check: %s. What the sync excluded and why is in `data/_report.md`." % (
        len(entries), len(cfg_sections), stats["notes"], len(checked), dead, last or "never")
    if split:
        stats_line += " The field notes are rendered into `%s` by the same build." % notes_file
    stats.update(header=header, checked=len(checked), dead=dead, last_checked=last, notes_file=notes_file)

    out = template
    out = out.replace("{{header_line}}", header)
    out = out.replace("{{toc}}", "\n".join(toc))
    out = out.replace("{{start_here}}", "\n".join(start_lines).rstrip())
    out = out.replace("{{sections}}", "\n".join(body).rstrip())
    out = out.replace("{{stats}}", stats_line)
    out = re.sub(r"\n{3,}", "\n\n", out).rstrip() + "\n"
    return out, notes_doc, stats, entries


def main():
    ap = argparse.ArgumentParser(description="Render README.md from data/ (see the module docstring).")
    ap.add_argument("--notes-file", default=None, metavar="FILE",
                    help="write every note to FILE (relative to the repo root) and keep only pointers in README.md; "
                         "default: 'notes_file' from config/sections.json, else off")
    args = ap.parse_args()
    text, notes_doc, stats, _ = build(args.notes_file)
    with open(P["readme"], "w", encoding="utf-8") as f:
        f.write(text)
    if stats.get("notes_file"):
        with open(os.path.join(ROOT, stats["notes_file"]), "w", encoding="utf-8") as f:
            f.write(notes_doc)
    print("build: %s -> README.md" % stats["header"])
    if stats.get("notes_file"):
        print("  notes -> %s (%d notes in %d sections)" % (stats["notes_file"], stats["notes"], stats.get("notes_sections", 0)))
    for name, s in stats["sections"].items():
        print("  %-28s entries=%-3d notes=%d" % (name, s["entries"], s["notes"]))
    if stats["unlisted_sections"]:
        print("  WARNING sections in data but not in config/sections.json (not rendered): " + ", ".join(stats["unlisted_sections"]))


if __name__ == "__main__":
    main()
