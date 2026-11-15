# Human-in-the-loop review process

**Core rule: nothing changes the live store, theme, content or `agents.md` without your explicit approval, per item.**

---

## What failed in W41→W46, and what changed

The first queue put 14 items in front of you at equal weight and asked you to adjudicate all of them. Five weeks later, every one was still `PENDING` — and by then the store had pivoted, so most were stale anyway. A queue that asks for 14 decisions gets zero.

Three changes, from W46 on:

1. **A time-boxed section at the top.** Never more than 3 items. These are the ones where waiting has a cost — a deadline, leaking spend, or a wrong price in front of customers. If you read nothing else, read those three.
2. **Approve by category, not line by line.** You can write `APPROVE ALL` against a whole section heading and I'll treat every item in it as approved. Per-item approval stays available when you want it.
3. **Stale items expire.** Anything `PENDING` for 3+ weeks gets re-derived against the current store at the next run rather than carried forward blindly. The store moves faster than the queue.

---

## Weekly flow

1. **I read `review/approvals.md` first**, before any research, and action every `APPROVE`.
2. **I run `scripts/consistency_check.py`** — automated cross-surface checks (price drift between `agents.md` and live variants, products named as purchasable that 404, live products missing from `agents.md`, noindex pages listed in sitemaps). Any finding goes straight into the critical section.
3. **I audit the live site** — rendered HTML, structured data, Core Web Vitals, mobile rendering, Shopify Admin state, agent-facing files.
4. **I research**, deduping every URL against `research/research-db.json` so no source is cited twice across weeks.
5. **I write `audits/<year>-W<nn>-audit.md`** and rebuild `review/approvals.md`.
6. **I push a notification** with the criticals and the count awaiting you.
7. **You edit the Status column** — in the repo, on GitHub, or by replying in a session.
8. **Next run I implement only `APPROVE` items**, on the branch, never direct to live, and mark them `DONE <date>`.

---

## Tiers

| Tier | What | Needs |
|---|---|---|
| 1 | Read-only checks, research, drafting copy for your review | No approval |
| 2 | Anything customer-facing: SEO fields, theme/CSS, content, nav, `agents.md` | Per-item or per-category approval |
| 3 | Publishing products, prices, inventory, anything that takes money | Explicit approval **plus** a before/after preview |

Every applied change logs: ID · before · after · rollback.

**`agents.md` is Tier 2 and treated as customer-facing.** AI agents quote it to buyers as fact, so an error there reaches customers exactly like wrong on-site copy does.

---

## Research hygiene

- Before citing: `python3 scripts/research_db.py check <url>` — skip anything already in the DB.
- Add with `research_db.py add <id> <url> <title> <publisher> <category> <reliability> <takeaway>`.
- Reliability is recorded honestly (`primary` / `platform` / `vendor`). Most SEO/GEO writing is vendor marketing; stats from those sources are labelled directional in the audit, and site measurements are always preferred over cited benchmarks.

## Two-month research prune

- `python3 scripts/research_db.py prune-due` → is it due?
- When due: `prune` (flags sources unconfirmed >120 days as `review`) → check each flagged source against current practice → set obsolete ones to `removed` → `purge` (moves them to `research/pruned-log.json`).
- **Next prune audit due: 2026-12-09.**
