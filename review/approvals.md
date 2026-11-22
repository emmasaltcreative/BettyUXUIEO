# Approval queue

**Status values:** `PENDING` · `APPROVE` · `REJECT` · `DEFER <date>` · `QUESTION: ...` · `DONE <date>`
**How to use:** edit the Status column. Only `APPROVE` items are acted on. You can approve a whole category at once by filling in its **Category sign-off** line instead of every row — `APPROVE ALL`, `APPROVE EXCEPT <ids>`, or `REJECT ALL`.

Last updated: **2026-11-22 (W47)** · Audit: `audits/2026-W47-audit.md`

> ⚠️ **Nothing in the W41 queue was answered.** Every item below marked "carried" has been open for 6 weeks. Where the store has moved on, I have closed the item out myself rather than leaving it to rot — see §6 for what I withdrew and why. No live change has been made to the store by this routine.

---

## 1. CRITICAL — this week
*Four of these are time-boxed. E-4 has a 16-day runway.*

| ID | Change | Risk | Status |
|---|---|---|---|
| E-1 | **Rewrite homepage title + meta description** from "Linen Book Covers & Literary Keepsakes" to the live In Her Purse proposition. Proposed title: `In Her Purse: Bags, Scent & Gloves \| Oh Betty Jaletti` (49 chars). I will draft the meta description for your sign-off before anything changes. | Low — metadata only, reversible | PENDING |
| E-2 | **Correct `agents.md` / `llms.txt`**: tote $94→**$91**, perfume $71→**$43**, add The Out-the-Door Gloves, change "Two pieces are published" → three, re-date "last reviewed". | Low — but it is the file AI agents trust | PENDING |
| E-3 | **Unify the shipping promise.** Three live versions: theme badge "2–3 business days", `agents.md` "2–3", published policy "3–5". **Tell me which number is true** and I will change the other two. | Low — needs your answer first | PENDING |
| E-4 | **The Advent: ship it or drop it.** Currently DRAFT, $0.00, no SKU, no images, DENY at 0 inventory, page unpublished — and its own copy says "order by 8 December". **Decision needed; I cannot guess this one.** | Medium — pricing + publishing a product | PENDING |
| E-5 | **Rework the homepage hero** to lead with A Woman Remembered (12 of 17 orders, 3.76% CVR from social) instead of a collection CTA that has converted 0 of 411 sessions. Includes fixing "Two pieces to begin with" → "Three pieces". | Medium — customer-facing layout + copy | PENDING |
| E-5a | *Sub-item, zero-risk:* fix only the "Two pieces" → "Three pieces" copy bug, even if you reject the wider hero rework. | Low | PENDING |

**Category sign-off (Critical):** `__________`

---

## 2. NECESSARY — high impact, low risk

| ID | Change | Risk | Status |
|---|---|---|---|
| F-1 | **Link the orphaned "At the Worktable" cluster** (15 pages, published 4 Nov, zero internal links from anywhere) into the footer and/or Journal nav. | Low | PENDING |
| F-2 | **Add 4+ photographs per product** (tote 1, gloves 1, perfume 3 today). *Needs your photos* — I can write alt text and set the order. | Low — needs your assets | PENDING |
| F-3 | **Stop showing "In stock · packed in 2–3 days" on gloves with 0 units on hand.** Either stock them or switch to made-to-order wording with a real ship date. | Medium — affects what you promise buyers | PENDING |
| F-4 | **Complete Product schema**: add `hasMerchantReturnPolicy`, `shippingDetails`, all images, and per-variant offers (today only the Small glove SKU is emitted — Medium is invisible). | Low — additive markup | PENDING |
| F-5 | **`/products/the-chaperone` 404s but `agents.md` advertises it** at $169 (its own SEO description says $103). Point agents at `/pages/waitlist` and fix the price contradiction. | Low | PENDING |
| F-6 | **Redirect `/pages/worktable` → `/pages/the-worktable`** (current 404, has recorded traffic). | Low | PENDING |
| F-7 | **Publish a Christmas shipping cutoff** (Standard ≈ 10 Dec, Express ≈ 17 Dec — *you confirm the dates*) in the announcement bar, on PDPs and in the policy. | Low — but the dates must be yours | PENDING |
| F-8 | **Bridge the $70 free-shipping threshold.** AOV is $44; 17 orders produced 17 units — no multi-item orders, and nothing exists between $43 and $89. Options: (a) cart progress nudge, (b) add a sub-$30 item, (c) lower threshold to ~$50. **Pick one.** | Medium — (c) changes margin | PENDING |
| F-9 | **Request reviews from the 17 existing buyers** via Klaviyo (12 bought the same perfume). *This re-raises deferred item C-6 early — see §6.* | Low | PENDING |

**Category sign-off (Necessary):** `__________`

---

## 3. RECOMMENDED — AEO / GEO / content

| ID | Change | Risk | Status |
|---|---|---|---|
| G-1 | Add answer-first opening, visible byline, last-updated date and `Article` schema to the 3 guide pages; link each to products. *(carried from W41 C-1 — still open)* | Low | PENDING |
| G-2 | Write SEO titles + meta descriptions for the 15 Worktable pages (all currently on the default theme pattern, no meta description, no schema). | Low | PENDING |
| G-3 | Add `sameAs` (Instagram) and `ContactPoint` to Organization schema. | Low | PENDING |
| G-4 | Add a referrer/UTM segment for ChatGPT / Perplexity / Claude so AI referrals are measured rather than assumed. | Low | PENDING |
| G-5 | Add the `\| Oh Betty Jaletti` brand suffix to the tote and perfume SEO titles. | Low | PENDING |
| G-6 | Pick one canonical returns page — `/pages/returns` and `/policies/refund-policy` are duplicates that will drift. | Low | PENDING |
| G-7 | Add the shipping policy to the footer (currently reachable only at checkout). | Low | PENDING |
| G-8 | Remove the duplicate "Your Privacy Choices" footer link. | Low | PENDING |

**Category sign-off (Recommended):** `__________`

---

## 4. PROCESS

| ID | Change | Risk | Status |
|---|---|---|---|
| H-1 | **Adopt a 9-point release checklist** that must clear before any product goes ACTIVE (price/SKU/inventory, 4+ images, SEO fields, Details block, collection, homepage counts, `agents.md` re-dated, shipping promise, schema). Every Critical item this week except E-5 traces to its absence; W41 found the same class of defect. | Low — process only | PENDING |
| H-2 | Should I keep carrying unanswered items forward indefinitely, or auto-close anything unanswered after 4 weeks and re-raise only if it worsens? | — | QUESTION: awaiting your preference |

**Category sign-off (Process):** `__________`

---

## 5. ACCESS / VERIFICATION
*Read-only checks I cannot complete without you.*

| ID | Item | Status |
|---|---|---|
| D-2 | Confirm guest checkout is enabled and shipping cost appears before the final checkout step. Shop Pay is confirmed active. *(carried from W41)* | PENDING |
| D-4 | Confirm Search Console + Bing Webmaster are verified and the sitemap is submitted — no verification meta tag is in the HTML, so it may be DNS-verified. *(carried from W41)* | PENDING |
| D-5 | Was archiving **The Scented Letter** (free sample, 244 units in stock, 6 claimed) deliberate? It is the cheapest list-builder you have. | PENDING |

**Category sign-off (Access):** `__________`

---

## 6. Closed out this week — no action needed from you

Withdrawn because the store moved on and I verified it live (detail in `audits/2026-W47-audit.md` §5):

| W41 ID | Outcome |
|---|---|
| D-1 | **Resolved** — live site is now reachable; this week's audit used rendered HTML, schema, robots and measured Core Web Vitals. |
| D-3 | **Resolved, passing** — mobile LCP 0.76–1.26s, CLS 0 across homepage, PDP and collection. No action. |
| A-1, A-3 | **Superseded** — Edition II is now coherently "not yet open" and `noindex`; the draft products are deliberate. |
| B-1, B-2 | **Resolved** — collection title rewritten and clean; all live SEO titles are 43–57 chars. |
| B-3, B-4 | **Resolved for live products** — tote and gloves carry full "Details" spec blocks; No. 1/2/3 numbering is in use and explained in `agents.md`. |
| C-2 | **Verified** — Product + BreadcrumbList schema is valid; the remaining gaps are now itemised as F-4. |
| C-3 | **Resolved** — `robots.txt` is permissive to AI crawlers; UCP, `/api/ucp/mcp`, `agents.md`, `llms.txt` all live. |
| C-4 | **Resolved** — Organization schema carries `name: Oh Betty Jaletti` + `alternateName: Maison Betty Jaletti`. |
| C-5 | **Resolved** — shipping, refund and returns policies all published; remaining nits are G-6 / G-7. |
| A-2 | **Re-raised as F-2** (still one image per product). |
| C-6 | **Re-raised early as F-9.** It was deferred to 2027-01-15 *because there were no buyers.* There are now 17. Flagging the early re-raise explicitly rather than quietly overriding your deferral — if you would rather keep it parked until January, reject F-9 and it goes back to `DEFER 2027-01-15`. |

Also recorded so it is not re-flagged: the 57 sessions to `/password` with 100% bounce were from the pre-launch lock; `/password` now redirects to `/`. No action.
