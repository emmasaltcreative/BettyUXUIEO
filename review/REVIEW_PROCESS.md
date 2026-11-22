# Human-in-the-loop review process

**Rule: nothing changes the live store, theme, content or Shopify data without an explicit approval from Emma, per item or per category.**

## Flow (weekly)
1. The routine audits the store (live site + Shopify Admin + analytics + fresh research) and writes `audits/<year>-W<nn>-audit.md`.
2. It rewrites `review/approvals.md`: new items as **PENDING**, grouped by category — **Critical**, **Necessary**, **Recommended (AEO/GEO/content)**, **Process**, **Access/Verification**.
3. It sends a push notification: the criticals, anything time-boxed, and how many items await approval.
4. Emma sets each item's Status (on the branch, in GitHub web, or by replying in a session):
   - `APPROVE` · `REJECT` · `DEFER <date>` · `QUESTION: ...`
   - **Or approve a whole category at once** on that category's **Category sign-off** line: `APPROVE ALL`, `APPROVE EXCEPT <ids>`, `REJECT ALL`. A row-level status always overrides the category line.
5. The next run implements **only `APPROVE` items**, one category at a time, on the working branch — never directly to live. Code and content changes go to a branch (PR only if Emma asks). Shopify data changes are listed with exact before/after values and applied only for `APPROVE` items. Each is then marked `DONE <date>`.
6. Items that need Emma's input before any work can start (a price, a date, a decision between options) say so explicitly in the row. The routine does not guess them.

## Carry-forward rules
- `REJECT` items are never re-proposed.
- `DEFER` items return on their date.
- Unanswered `PENDING` items are carried forward. If the store has changed such that an item is resolved or moot, the routine **closes it out itself** and records why in the "Closed out this week" section — rather than carrying dead items indefinitely.
- **Re-raising a deferred item early is allowed only when its premise has changed, and must be stated explicitly** in both the audit and the queue, with the original deferral date, so Emma can push it back.

## Guardrails
- Product publishing, pricing, inventory and anything customer-facing is always Tier 2: approval **plus** a before/after preview.
- No bulk changes without a per-category approval line.
- Every applied change logs: ID, before, after, rollback.
- The routine never sends email/SMS, never publishes a product, and never alters a policy page on its own initiative.

## Release checklist (proposed as H-1, W47)
Before any product goes ACTIVE: price + SKU + inventory policy · 4+ images with alt text · SEO title <60 chars + meta description · "Details" spec block · added to its collection · homepage/collection counts updated · **`agents.md` / `llms.txt` updated and re-dated** · shipping promise matches the published policy · schema spot-checked.

## Research hygiene
- Before citing a source: `python3 scripts/research_db.py check <url>` — skip duplicates. No source is cited twice across weeks.
- Log each new source with `research_db.py add` including a reliability rating (`primary` · `vendor-own-data` · `vendor-directional` · `low-secondary`).
- Findings must be evidenced from the store's own analytics, Admin data or rendered HTML. Vendor statistics are directional context only and never the sole basis for a recommendation.
- Every 2 months (`prune-due` → `prune`): review flagged sources against current best practice, set obsolete ones to `removed`, then `purge`. **Next prune audit due 2026-12-09.**
