# Human-in-the-loop review process

**Rule: nothing changes the live store, theme, or content without an explicit approval from Emma, per item.**

## Flow (weekly)
1. Routine writes `audits/<year>-W<nn>-audit.md` and appends new items to `review/approvals.md` as **PENDING**, grouped by category (UX/UI, SEO, AEO, GEO, Content, Technical, Access).
2. Routine sends a push notification summarizing criticals and how many items await approval.
3. Emma edits `review/approvals.md` (on the branch, GitHub web, or by replying in a session) and changes each item's status:
   - `APPROVE` (go ahead), `REJECT` (don't, and don't re-raise), `DEFER <date>` (re-surface later), `QUESTION: ...`.
4. Next run, the routine implements **only APPROVE items**, one category at a time, on a branch (never directly to live): code/content changes go to a PR; Shopify data changes are listed with exact before/after values and applied only for APPROVE items. It marks them `DONE` with date + link.
5. REJECT items are never re-proposed. DEFER items return on their date. Unanswered PENDING items are carried forward and reminded only if Critical.

## Guardrails
- Product publishing, pricing, inventory and anything customer-facing is always Tier 2 (approval + a before/after preview).
- No bulk changes without a per-category approval line.
- Every change logs: ID, before, after, rollback.

## Research hygiene
- Before citing a source: `python3 scripts/research_db.py check <url>`; skip duplicates.
- Every 2 months (`prune-due`): run `prune`, review flagged sources against current best practice, set obsolete ones to `removed`, then `purge`.
