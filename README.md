# BettyUXUIEO
Weekly UX/UI + SEO/AEO/GEO audit system for Oh Betty Jaletti (ohbettyjaletti.com).

## Start here
- **`playbook/SEO-AEO-GEO-PLAYBOOK.md`** — the standing reference: the target audience and house voice,
  what changed in 2026, the One-Fact Rule, the SEO/AEO/GEO layers, the content→product bridge,
  what to measure and what to ignore. Weekly audits check the store *against this file*.
  Review every 8 weeks (next: 2027-01-15).
- **`playbook/fixes-ready-to-paste.md`** — the current copy, schema and Liquid, ready to apply.
- **`review/approvals.md`** — human approval queue. **Nothing ships without an APPROVE per item.**
  `E-*` rows are decisions only Emma can make; they block other items.

## Layout
- `audits/` — weekly reports (`<year>-W<nn>-audit.md`)
- `review/REVIEW_PROCESS.md` — the human-in-the-loop flow and guardrails
- `research/research-db.json` — source dedupe DB with reliability grades, 2-month prune cycle
- `scripts/research_db.py` — `check <url>` before citing · `add` · `prune-due` · `prune` · `purge`

## Auditing the live site
Run audits on the **`BETTY`** cloud environment, which allows `ohbettyjaletti.com` and `cdn.shopify.com`.
From a session on the Default environment: `switch_environment` to `env_01P5HQanYUBEYn6keXiBGT7t`
(mode `network_only`). Without it the storefront is unreachable and schema/robots/sitemap checks are blind.
PageSpeed Insights is still not reachable, so Core Web Vitals remain unverified.

## Conventions
- Confidence is marked on every external claim: **[primary]** platform/vendor-independent ·
  **[directional]** vendor-sourced, unverified · **[house]** our own decision.
- Where sources conflict, state both positions rather than resolving them.
