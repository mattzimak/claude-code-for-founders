#!/usr/bin/env python3
"""lint.py - quality gate for README.md and the data behind it. Exit 1 on any failure.

Fails on
  - README.md stale (differs from a fresh tools/build.py render) or missing
  - data/enrichment.json missing, or any link with status dead
  - a rendered description shorter than 30 characters
  - duplicate URLs or duplicate names across entries
  - http:// anywhere in the README
  - tracking parameters in a URL (utm_*, fbclid, gclid, mcp_token, igsh)
  - links to private hosts (notion.so, app.notion.com, notion.site, drive.google.com, docs.google.com, skool.com)
  - U+2013 / U+2014 / U+00A0 anywhere in the README
  - the placeholder "TBD", or a line that ends with a dangling " - "
  - a section with fewer rendered items than config/sections.json min_entries
  - a table-of-contents anchor that does not resolve to a heading
Stdlib only, Python 3.9+. Run from the repo root: python3 tools/lint.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402

TRACKING_RE = re.compile(r"[?&](utm_[a-z]*|fbclid|gclid|mcp_token|igsh)=", re.I)
PRIVATE_HOST_RE = re.compile(r"https?://(?:[\w.-]+\.)?(notion\.so|app\.notion\.com|notion\.site|drive\.google\.com|docs\.google\.com|skool\.com)\b", re.I)
URL_RE = re.compile(r"\((https?://[^)\s]+)\)")


def main():
    fails = []
    warn = []
    if not os.path.exists(build.P["readme"]):
        fails.append("README.md is missing - run tools/build.py")
        report(fails, warn)
    with open(build.P["readme"], encoding="utf-8") as f:
        readme = f.read()
    fresh, stats, entries = build.build()
    if fresh != readme:
        fails.append("README.md is stale - run tools/build.py and commit the result")

    # links
    rows, notes, enrich, overrides, config, _ = build.load_all()
    if not enrich:
        fails.append("data/enrichment.json missing - run tools/enrich.py before lint")
    else:
        for e in entries:
            rec = enrich.get(e["id"])
            if rec is None:
                warn.append("not checked: %s (%s) - run tools/enrich.py" % (e["name"], e["url"]))
            elif rec.get("status") == "dead":
                fails.append("dead link: %s -> %s (http %s%s) [id %s]" % (
                    e["name"], e["url"], rec.get("http_status"), ", " + str(rec.get("error", ""))[:80] if rec.get("error") else "", e["id"]))

    # descriptions
    for e in entries:
        if len(e["description"]) < build.MIN_DESC:
            fails.append("short description (%d chars): %s -> %r [id %s]" % (len(e["description"]), e["name"], e["description"], e["id"]))

    # duplicates
    seen_url, seen_name = {}, {}
    for e in entries:
        k = build.url_key(e["url"])
        if k in seen_url:
            fails.append("duplicate url: %s used by %r and %r" % (e["url"], seen_url[k], e["name"]))
        seen_url[k] = e["name"]
        n = e["name"].casefold()
        if n in seen_name:
            fails.append("duplicate name: %r (%s and %s)" % (e["name"], seen_name[n], e["url"]))
        seen_name[n] = e["url"]

    # README text
    lines = readme.split("\n")
    for i, line in enumerate(lines, 1):
        if "http://" in line:
            fails.append("line %d: http:// link" % i)
        for m in URL_RE.finditer(line):
            u = m.group(1)
            if TRACKING_RE.search(u):
                fails.append("line %d: tracking parameter in %s" % (i, u))
            if PRIVATE_HOST_RE.search(u):
                fails.append("line %d: private host in %s" % (i, u))
        for ch, label in (("–", "U+2013 en dash"), ("—", "U+2014 em dash"), (" ", "U+00A0 nbsp")):
            if ch in line:
                fails.append("line %d: %s" % (i, label))
        if re.search(r"\bTBD\b", line):
            fails.append("line %d: TBD placeholder" % i)
        if re.search(r"\S - *$", line) or line.strip() == "-":
            fails.append("line %d: dangling ' - '" % i)

    # thin sections
    min_entries = int(config.get("min_entries", 3))
    for sec in config["sections"]:
        s = stats["sections"].get(sec["name"], {"items": 0, "entries": 0, "notes": 0})
        if s["items"] < min_entries:
            fails.append("section %r has %d items (entries %d + notes %d), minimum is %d" % (
                sec["name"], s["items"], s["entries"], s["notes"], min_entries))
    for name in stats.get("unlisted_sections", []):
        fails.append("section %r exists in data/ but not in config/sections.json (not rendered)" % name)

    # TOC anchors
    headings = [re.sub(r"^#{2,3}\s+", "", l).strip() for l in lines if re.match(r"^#{2,3}\s+\S", l)]
    anchors = set(build.anchors_for(headings))
    toc_start = readme.find("## Contents")
    toc_end = readme.find("\n## ", toc_start + 5) if toc_start >= 0 else -1
    toc = readme[toc_start:toc_end] if toc_start >= 0 and toc_end > toc_start else ""
    if not toc:
        fails.append("no '## Contents' block found")
    for m in re.finditer(r"\]\(#([^)]+)\)", toc):
        if m.group(1) not in anchors:
            fails.append("TOC anchor #%s does not resolve to a heading" % m.group(1))

    report(fails, warn, stats)


OPEN_MARK = "## Open decisions (from tools/lint.py)"


def write_open_decisions(fails, warn):
    """Keep the tail of data/_report.md in sync with what lint cannot fix on its own."""
    path = os.path.join(build.ROOT, "data", "_report.md")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        text = f.read()
    cut = text.find(OPEN_MARK)
    if cut >= 0:
        text = text[:cut].rstrip() + "\n"
    L = ["", OPEN_MARK, "",
         "Refreshed by every `python3 tools/lint.py` run. Each line needs a human decision: fix it in "
         "`data/overrides.json` (name, description, url) or change the source in Notion, then re-sync.", ""]
    L += ["- " + f for f in fails] if fails else ["- none, lint passes"]
    if warn:
        L += ["", "Warnings:", ""] + ["- " + w for w in warn]
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n" + "\n".join(L) + "\n")


def report(fails, warn, stats=None):
    if stats:
        print("lint: %d entries, %d notes, %d links checked, %d dead" % (
            stats["entries"], stats["notes"], stats.get("checked", 0), stats.get("dead", 0)))
    for w in warn:
        print("WARN " + w)
    for f in fails:
        print("FAIL " + f)
    write_open_decisions(fails, warn)
    if fails:
        print("lint: %d failure(s) - listed under '%s' in data/_report.md" % (len(fails), OPEN_MARK))
        sys.exit(1)
    print("lint: ok")
    sys.exit(0)


if __name__ == "__main__":
    main()
