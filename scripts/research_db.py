#!/usr/bin/env python3
"""Research DB helper.
  check <url>...   exit 1 if any URL already in DB (dedupe before citing)
  add              add a source from args: id url title publisher category reliability takeaway
  prune-due        print whether the 2-month prune audit is due
  prune            mark stale candidates (last_confirmed > 120d) as 'review'; human/agent then sets 'removed'
  purge            delete sources with status 'removed' (moves them to research/pruned-log.json)
"""
import json, sys, datetime as dt, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "research"
DB = P / "research-db.json"
load = lambda: json.loads(DB.read_text())
save = lambda d: DB.write_text(json.dumps(d, indent=2) + "\n")
norm = lambda u: u.split("#")[0].rstrip("/").lower()
today = dt.date.today()

def main(a):
    d = load(); cmd = a[0] if a else ""
    if cmd == "check":
        seen = {norm(s["url"]) for s in d["sources"]}
        dup = [u for u in a[1:] if norm(u) in seen]
        for u in dup: print("DUPLICATE:", u)
        sys.exit(1 if dup else 0)
    if cmd == "add":
        id_, url, title, pub, cat, rel, take = a[1:8]
        if norm(url) in {norm(s["url"]) for s in d["sources"]}: sys.exit("already present")
        d["sources"].append(dict(id=id_, url=url, title=title, publisher=pub, category=cat, reliability=rel,
            first_used=today.isoformat(), last_confirmed=today.isoformat(), status="active", takeaway=take))
        save(d)
    elif cmd == "prune-due":
        due = dt.date.fromisoformat(d["next_prune_audit_due"])
        print("DUE" if today >= due else f"not due until {due}")
    elif cmd == "prune":
        n = 0
        for s in d["sources"]:
            if s["status"] == "active" and (today - dt.date.fromisoformat(s["last_confirmed"])).days > 120:
                s["status"] = "review"; n += 1
        d["last_prune_audit"] = today.isoformat()
        d["next_prune_audit_due"] = (today + dt.timedelta(days=61)).isoformat()
        save(d); print(f"{n} flagged for review")
    elif cmd == "purge":
        gone = [s for s in d["sources"] if s["status"] == "removed"]
        d["sources"] = [s for s in d["sources"] if s["status"] != "removed"]
        lp = P / "pruned-log.json"
        log = json.loads(lp.read_text()) if lp.exists() else []
        log += [{"url": s["url"], "removed": today.isoformat()} for s in gone]
        lp.write_text(json.dumps(log, indent=2) + "\n"); save(d); print(f"purged {len(gone)}")
    else: print(__doc__)
main(sys.argv[1:])
