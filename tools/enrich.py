#!/usr/bin/env python3
"""enrich.py - verify every link in data/links.csv and collect metadata into data/enrichment.json.

Per entry id:
  stars, license, pushed_at, archived, gh_description, full_name   (GitHub API via `gh api repos/{owner}/{repo}`;
                                                                    blob/tree URLs use the repo part; renames are
                                                                    followed and recorded in full_name + final_url)
  oembed_title, oembed_author, oembed_text                          (YouTube oEmbed, X oEmbed)
  page_title, page_description                                      (from the HTML of everything else, best effort)
  http_status, final_url, status: ok | redirected | dead | manual_ok, last_checked

status rules: 2xx -> ok (redirected when the final URL is a different page); 404/410/DNS failure/timeout -> dead;
a bot-blocking host (LinkedIn, Instagram, Threads, Reddit, X) answering 401/403/405/429/999 or any host answering
5xx -> manual_ok (recorded with its http_status so check_links.py can list it for a human look).

Requests: HEAD then GET with a browser User-Agent, 20 s timeout, 8 threads. Stdlib only, Python 3.9+.
Run from the repo root: python3 tools/enrich.py
"""
import concurrent.futures
import csv
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKS = os.path.join(ROOT, "data", "links.csv")
OVERRIDES = os.path.join(ROOT, "data", "overrides.json")
OUT = os.path.join(ROOT, "data", "enrichment.json")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0.0.0 Safari/537.36")
TIMEOUT = 20
THREADS = 8
BOT_BLOCKING_HOSTS = ("linkedin.com", "instagram.com", "threads.com", "threads.net", "reddit.com", "x.com",
                      "facebook.com")
TODAY = dt.datetime.now(dt.timezone.utc).date().isoformat()


def log(msg):
    print(msg, file=sys.stderr)


def host_of(url):
    return (urllib.parse.urlsplit(url).hostname or "").lower()


def same_page(a, b):
    """True when two URLs differ only by scheme, www, trailing slash or fragment."""
    def norm(u):
        p = urllib.parse.urlsplit(u)
        h = (p.hostname or "").lower()
        h = h[4:] if h.startswith("www.") else h
        return (h, p.path.rstrip("/").lower(), p.query)
    return norm(a) == norm(b)


# ----------------------------------------------------------------------------- HTTP helpers
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    pass


def http(url, method="GET", max_bytes=400000):
    """Return (status, final_url, body_text or ''). Follows redirects. Raises on network failure."""
    headers = {"User-Agent": UA, "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.9"}
    if "youtube.com" in host_of(url):
        headers["Cookie"] = "SOCS=CAI; CONSENT=YES+cb"  # skip the EU consent interstitial, which hides the watch page
    req = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = ""
            if method == "GET":
                raw = r.read(max_bytes)
                charset = r.headers.get_content_charset() or "utf-8"
                body = raw.decode(charset, "replace")
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read(max_bytes).decode("utf-8", "replace") if method == "GET" else ""
        except Exception:
            pass
        return e.code, e.geturl() if hasattr(e, "geturl") else url, body


def curl(url, method="HEAD"):
    """curl fallback (handles servers that reject urllib): returns (status, final_url, body)."""
    args = ["curl", "-sS", "-L", "--max-time", str(TIMEOUT), "-A", UA, "-o", "/dev/null" if method == "HEAD" else "-",
            "-w", "\n__META__ %{http_code} %{url_effective}"]
    if "youtube.com" in host_of(url):
        args += ["-H", "Cookie: SOCS=CAI; CONSENT=YES+cb"]
    if method == "HEAD":
        args.insert(1, "-I")
    args.append(url)
    r = subprocess.run(args, capture_output=True, text=True, errors="replace")
    out = r.stdout
    m = re.search(r"__META__ (\d{3}) (\S+)\s*$", out)
    if not m:
        raise RuntimeError((r.stderr or "curl failed").strip()[:200])
    body = out[:m.start()] if method == "GET" else ""
    return int(m.group(1)), m.group(2), body


def fetch(url, methods=("HEAD", "GET")):
    """HEAD then GET (or GET only). Returns (status, final_url, body, error)."""
    err = ""
    for method in methods:
        try:
            status, final, body = http(url, method)
        except Exception as e1:
            try:
                status, final, body = curl(url, method)
            except Exception as e2:
                err = f"{type(e1).__name__}: {str(e1)[:120]} / curl: {str(e2)[:120]}"
                continue
        if status in (301, 302, 303, 307, 308):
            # urllib does not follow 308 and HEAD redirects are not worth trusting: let curl -L resolve it
            try:
                status, final, body = curl(url, "GET")
            except Exception as e3:
                err = str(e3)[:200]
                continue
        if method == "HEAD" and status >= 400:
            continue  # many hosts reject HEAD; confirm with GET
        return status, final, body, ""
    return 0, url, "", err or "no response"


def classify(url, status, final, err=""):
    """Map an HTTP result to (status label, reason)."""
    h = host_of(url)
    blocking = any(h == b or h.endswith("." + b) for b in BOT_BLOCKING_HOSTS)
    if status == 0:
        return "dead", err or "no response"
    if 200 <= status < 300:
        if blocking and re.search(r"(?:/accounts/login|/login\b|/signup|/i/flow/login)", final or ""):
            return "manual_ok", "login wall, the post itself could not be read"
        return ("ok" if same_page(url, final) else "redirected"), ""
    if status in (404, 410):
        return "dead", ""
    if status in (401, 403, 405, 429, 999) and blocking:
        return "manual_ok", f"bot-blocking host answered {status}"
    if status >= 500:
        return "manual_ok", f"server error {status}"
    if status in (401, 403, 429):
        return "manual_ok", f"{status} for an automated client"
    return "dead", f"unexpected status {status}"


TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
META_RE = re.compile(r"<meta\s+[^>]*?(?:name|property)\s*=\s*[\"'](?P<k>og:description|description|og:title)[\"'][^>]*?content\s*=\s*[\"'](?P<v>[^\"']*)[\"']", re.I)
META_RE2 = re.compile(r"<meta\s+[^>]*?content\s*=\s*[\"'](?P<v>[^\"']*)[\"'][^>]*?(?:name|property)\s*=\s*[\"'](?P<k>og:description|description|og:title)[\"']", re.I)
JUNK_TITLES = ("just a moment", "access denied", "attention required", "log in", "login", "sign in", "sign up",
               "page not found", "404", "instagram", "linkedin", "reddit - dive into anything", "x.com")


def clean(s):
    s = html.unescape(s or "")
    s = s.replace(" ", " ").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip()


def page_meta(body):
    title, desc = "", ""
    m = TITLE_RE.search(body or "")
    if m:
        title = clean(m.group(1))[:160]
    metas = {}
    for rx in (META_RE, META_RE2):
        for m in rx.finditer(body or ""):
            metas.setdefault(m.group("k").lower(), clean(m.group("v")))
    desc = metas.get("og:description") or metas.get("description") or ""
    if not title and metas.get("og:title"):
        title = metas["og:title"][:160]
    if title and any(j in title.lower() for j in JUNK_TITLES) and len(title) < 40:
        title = ""
    return title, desc[:300]


# ----------------------------------------------------------------------------- sources
def github_repo(url):
    p = urllib.parse.urlsplit(url)
    segs = [s for s in p.path.split("/") if s]
    if host_of(url) != "github.com" or len(segs) < 2:
        return None
    return segs[0], segs[1], segs[2:]


def gh_api(owner, repo):
    r = subprocess.run(["gh", "api", f"repos/{owner}/{repo}"], capture_output=True, text=True)
    if r.returncode != 0:
        msg = (r.stderr or r.stdout).strip()
        return None, msg[:200]
    try:
        return json.loads(r.stdout), ""
    except ValueError:
        return None, "gh: non-JSON response"


def enrich_github(url, rec):
    owner, repo, rest = github_repo(url)
    data, err = gh_api(owner, repo)
    if data is None:
        if "404" in err or "Not Found" in err:
            rec.update(http_status=404, final_url=url, status="dead", error=err)
            return rec
        # gh unavailable or rate limited: fall back to a plain HTTP check
        rec["error"] = err
        return enrich_http(url, rec)
    full = data.get("full_name") or f"{owner}/{repo}"
    lic = (data.get("license") or {}).get("spdx_id") or ""
    rec.update(stars=data.get("stargazers_count"), license="" if lic == "NOASSERTION" else lic,
               pushed_at=(data.get("pushed_at") or "")[:10], archived=bool(data.get("archived")),
               gh_description=clean(data.get("description") or "")[:300], full_name=full,
               homepage=clean(data.get("homepage") or ""))
    renamed = full.lower() != f"{owner}/{repo}".lower()
    final = "https://github.com/" + full + ("/" + "/".join(rest) if rest else "")
    rec["final_url"] = final
    rec["http_status"] = 200
    rec["status"] = "redirected" if renamed else "ok"
    if rest:
        # a file/tree path inside the repo: confirm the path itself still exists
        status, fin, _, err2 = fetch(final if renamed else url)
        rec["http_status"] = status
        if status in (404, 410):
            rec["status"] = "dead"
            rec["error"] = "path inside the repository no longer exists"
    return rec


def oembed(endpoint, url):
    q = urllib.parse.urlencode({"url": url, "format": "json"})
    status, final, body, err = fetch(endpoint + "?" + q, methods=("GET",))  # HEAD has no body to parse
    if status != 200 or not body:
        return None, status, err
    try:
        return json.loads(body), status, ""
    except ValueError:
        return None, status, "oembed: non-JSON"


def enrich_youtube(url, rec):
    data, status, err = oembed("https://www.youtube.com/oembed", url)
    if data is None:
        rec.update(http_status=status, final_url=url, status="dead" if status in (400, 401, 403, 404) else "manual_ok",
                   error=err or f"oembed {status}")
        return rec
    rec.update(oembed_title=clean(data.get("title", ""))[:160], oembed_author=clean(data.get("author_name", "")),
               http_status=200, final_url=url, status="ok")
    # best effort: the first real sentence of the video's own description (promo lines, links and
    # calls to action are skipped; if nothing is left the entry falls back to 'YouTube video by ...')
    try:
        try:
            s2, _, body = http(url, "GET", max_bytes=3000000)  # the player JSON sits deep in the page
        except Exception:
            s2, _, body = curl(url, "GET")
        m = re.search(r'"shortDescription":"((?:[^"\\]|\\.)*)"', body or "")
        if m:
            text = json.loads('"' + m.group(1) + '"')
            for line in text.split("\n"):
                line = clean(line)
                line = re.sub(r"^\(?\d{1,2}:\d{2}(?::\d{2})?\)?\s*[-:]?\s*", "", line)  # chapter marker: keep the title
                if len(line) < 40 or re.search(r"https?://|www\.|\.com\b|\.ai\b", line):
                    continue
                if re.match(r"^[^\w\"'(]", line):  # emoji / bullet led promo lines
                    continue
                if re.search(r"\b(subscribe|join|sign up|signup|discount|coupon|sponsor|newsletter|follow me|"
                             r"my course|free guide|link in|use code|get my|download my|book a|timestamps?)\b", line, re.I):
                    continue
                rec["page_description"] = line[:300]
                break
    except Exception:
        pass
    return rec


def enrich_x(url, rec):
    data, status, err = oembed("https://publish.twitter.com/oembed", url)
    if data is None and host_of(url) == "x.com":
        alt = url.replace("https://x.com/", "https://twitter.com/", 1)
        data, status, err = oembed("https://publish.twitter.com/oembed", alt)
    if data is None:
        rec.update(http_status=status, final_url=url, status="dead" if status == 404 else "manual_ok",
                   error=err or f"oembed {status}")
        return rec
    text = re.sub(r"<[^>]+>", " ", data.get("html", ""))
    text = clean(text)
    text = re.sub(r"\s*(?:pic\.twitter\.com/\S+)", "", text)
    text = re.sub(r"\s*-\s*[^-]+\(@\w+\)\s+\w+ \d{1,2}, \d{4}\s*$", "", text)  # drop the trailing attribution line
    rec.update(oembed_author=clean(data.get("author_name", "")), oembed_text=text[:300],
               oembed_title=clean(data.get("author_name", "")) + " on X" if data.get("author_name") else "",
               http_status=200, final_url=url, status="ok")
    return rec


def enrich_http(url, rec):
    status, final, body, err = fetch(url)
    if 200 <= status < 300 and not body:
        # HEAD answered: fetch the page once more for its title and description
        s2, f2, body, _ = fetch(url, methods=("GET",))
        if s2:
            status, final = s2, f2
    rec["http_status"] = status
    rec["final_url"] = final or url
    if body:
        title, desc = page_meta(body)
        if title:
            rec["page_title"] = title
        if desc:
            rec["page_description"] = desc
    rec["status"], reason = classify(url, status, final, err)
    if reason:
        rec["error"] = reason
    return rec


def check_also(urls):
    """Status of the secondary URLs of an entry (rendered as 'also:' links only when they answer)."""
    out = {}
    for u in urls:
        try:
            status, final, _, err = fetch(u)
            label, reason = classify(u, status, final, err)
        except Exception as e:
            status, label, reason = 0, "dead", str(e)[:120]
        out[u] = {"http_status": status, "status": label, "final_url": final or u}
        if reason:
            out[u]["error"] = reason
    return out


def enrich_one(row, url_override):
    url = url_override or row["url"]
    rec = {"url": url, "stars": None, "license": "", "pushed_at": "", "archived": False, "gh_description": "",
           "full_name": "", "oembed_title": "", "http_status": 0, "final_url": url, "status": "dead",
           "last_checked": TODAY}
    h = host_of(url)
    try:
        if h == "github.com" and github_repo(url):
            enrich_github(url, rec)
        elif "youtube.com" in h and "v=" in url:
            enrich_youtube(url, rec)
        elif h == "x.com" and "/status/" in url:
            enrich_x(url, rec)
        else:
            enrich_http(url, rec)
    except Exception as e:  # never let one link kill the run
        rec["status"] = "dead"
        rec["error"] = f"{type(e).__name__}: {str(e)[:160]}"
    also = [u for u in (row.get("also_urls") or "").split() if u]
    if also:
        rec["also"] = check_also(also)
    return row["id"], rec


def main():
    if not os.path.exists(LINKS):
        sys.exit(f"missing {LINKS} - run the Notion sync first")
    with open(LINKS, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    overrides = {}
    if os.path.exists(OVERRIDES):
        with open(OVERRIDES, encoding="utf-8") as f:
            overrides = json.load(f)
    previous = {}
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            previous = json.load(f)
    log(f"enrich: {len(rows)} links, {THREADS} threads")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as ex:
        futs = [ex.submit(enrich_one, r, (overrides.get(r["id"]) or {}).get("url", "")) for r in rows]
        for fut in concurrent.futures.as_completed(futs):
            eid, rec = fut.result()
            old = previous.get(eid) or {}
            if rec["status"] == "dead" and rec.get("http_status", 0) == 0 and old.get("status") in ("ok", "redirected"):
                # network failure this run: keep last known good metadata, flag it for a human
                rec = dict(old, status="manual_ok", error="unreachable this run: " + rec.get("error", ""),
                           last_checked=TODAY)
            results[eid] = rec
    counts = {}
    for rec in results.values():
        counts[rec["status"]] = counts.get(rec["status"], 0) + 1
    ordered = {k: results[k] for k in sorted(results)}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(ordered, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    print("enrich: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + f" -> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
