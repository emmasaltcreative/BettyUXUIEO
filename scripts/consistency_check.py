#!/usr/bin/env python3
"""Cross-surface consistency check for ohbettyjaletti.com.

Catches the failure modes that reach AI shopping agents as fact:
  1. price drift   - agents.md price != live variant price
  2. phantom goods - a product named purchasable in agents.md that 404s
  3. index signals - a page that is noindex but still listed in a sitemap

Usage: python3 scripts/consistency_check.py [--json]
Exit 0 = clean, 1 = findings.
"""
import re, sys, json, html, urllib.request, urllib.error

BASE = "https://ohbettyjaletti.com"
UA = {"User-Agent": "Mozilla/5.0 (compatible; OBJ-weekly-audit)"}

def get(path, timeout=30):
    url = path if path.startswith("http") else BASE + path
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.getcode(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, f"ERR {e}"

def money(s):
    return round(float(str(s).replace("$", "").replace(",", "").strip()), 2)

def main():
    findings = []

    code, agents = get("/agents.md")
    if code != 200:
        print(f"FATAL: /agents.md returned {code}")
        return 1

    # agents.md product lines look like:  **Name** · `/products/handle` · $94.00 · ...
    declared = re.findall(r"\*\*(.+?)\*\*\s*·\s*`(/products/[a-z0-9\-]+)`\s*·\s*\$([0-9][0-9,]*\.?[0-9]*)", agents)
    if not declared:
        findings.append(("parse", "Could not parse any product lines from agents.md - format may have changed"))

    for name, path, price_md in declared:
        handle = path.rsplit("/", 1)[-1]
        unbuyable = bool(re.search(
            r"\*\*(?:drafted|not published)[^*]*\*\*|cannot be bought",
            agents[agents.find(name): agents.find(name) + 600], re.I))
        code, body = get(f"/products/{handle}.json")
        if code != 200:
            if not unbuyable:
                findings.append(("phantom", f"{name}: agents.md presents it as purchasable but /products/{handle} returns {code}"))
            continue
        try:
            variants = json.loads(body)["product"]["variants"]
        except Exception:
            findings.append(("parse", f"{name}: could not read variants JSON"))
            continue
        live = [money(v["price"]) for v in variants]
        if money(price_md) not in live:
            findings.append(("price", f"{name}: agents.md says ${money(price_md):.2f}, live price {' / '.join(f'${p:.2f}' for p in live)}"))

    # walk the sitemap index (loc values are XML-escaped; unescape before fetching)
    code, idx = get("/sitemap.xml")
    sub = [html.unescape(u) for u in re.findall(r"<loc>([^<]+)</loc>", idx)] if code == 200 else []
    urls = []
    for s_url in sub:
        if "agentic" in s_url:
            continue
        c, b = get(s_url)
        if c == 200:
            urls += [html.unescape(u) for u in re.findall(r"<loc>([^<]+)</loc>", b)]

    # products live on the storefront but absent from agents.md
    for h in sorted({m for u in urls for m in re.findall(r"/products/([a-z0-9\-]+)", u)}):
        if h not in agents:
            findings.append(("missing", f"/products/{h} is live and in the sitemap but is not mentioned in agents.md"))

    # noindex pages that are still advertised in a sitemap
    for u in urls[:60]:
        c, b = get(u)
        if c == 200 and re.search(r'<meta name="robots" content="[^"]*noindex', b, re.I):
            findings.append(("index", f"{u} is noindex but is listed in a sitemap"))

    if "--json" in sys.argv:
        print(json.dumps([{"type": t, "detail": d} for t, d in findings], indent=2))
    else:
        if not findings:
            print("CLEAN - no cross-surface inconsistencies found.")
        else:
            print(f"{len(findings)} finding(s):\n")
            for t, d in findings:
                print(f"  [{t:8}] {d}")
    return 1 if findings else 0

sys.exit(main())
