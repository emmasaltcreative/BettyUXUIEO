# Approval queue
Status values: PENDING | APPROVE | REJECT | DEFER <date> | QUESTION: ... | DONE <date>
Edit the Status column. Only APPROVE items are acted on.

Ready-to-paste copy and markup for everything below: `playbook/fixes-ready-to-paste.md` (section per row).
Standing reference: `playbook/SEO-AEO-GEO-PLAYBOOK.md`.

**Decisions of 2026-11-20 are applied to the fixes doc.** The rows below now carry exact before/after values
and are ready to action on approval. Per `REVIEW_PROCESS.md`, anything customer-facing still needs an
explicit APPROVE per item — a decision answered an open question, it did not authorise the change.

---

## Still open — blocking other items

| ID | Decision needed | Blocks | Status |
|---|---|---|---|
| **E-9** | **Express: what do we do?** With a 3–5 day making window, `Express — packed the next business day` at $15.00 cannot be honoured, and the policy's "arrives in 2–4 business days" would really be 4–8. **(A)** rename to "first in the queue" and state 4–8 *(recommended, copy-only)* · **(B)** retire Express until stock exists · **(C)** genuinely pack Express in one business day. **Last item blocking the A-5 / A-7 / B-5 batch** | A-5, A-7, B-5 | PENDING |
| **E-4** | **A Woman Remembered — which scent pyramid is correct?** Shopify SEO says "rose, jasmine, aged iris over sandalwood and soft musk"; `llms.txt` says "luminous pear, warm amber, intimate musk, a trace of rose and jasmine" | C-10, part of A-2 | PENDING |
| **E-6** | **Social profile URLs for `sameAs`** (Instagram / Pinterest / TikTok / other). Main signal that "Oh Betty Jaletti" and "Maison Betty Jaletti" are one business | B-6 | PENDING |

## Decisions received 2026-11-20

| ID | Decision | Status |
|---|---|---|
| E-1 | **United States only** | ANSWERED 2026-11-20 — already true at market level; B-3 downgraded to housekeeping |
| E-2 | **Nothing is open for preorder** | ANSWERED 2026-11-20 — escalated to A-6 |
| E-3 | **Overselling is selling, then fulfilling on demand** (made to order) | ANSWERED 2026-11-20 — A-5 → `BackOrder`; raises A-7 and E-8 |
| E-5 | **Voice-forward homepage copy** | ANSWERED 2026-11-20 — A-1 copy finalised |
| E-7 | **The Advent is parked** | ANSWERED 2026-11-20 — B-10 closed |
| E-8 | **Made-to-order window: 3–5 business days** | ANSWERED 2026-11-20 — matches the existing policy, so Standard needs no rewrite and schema `handlingTime` is confirmed. Raises E-9 for Express |

## Critical

| ID | Change | Before → After | Fix | Status |
|---|---|---|---|---|
| **A-6** | **Reading Hour collection claims an open preorder in 6 places and shows no products.** Live payment promise the house is not keeping. **Most urgent item in this queue** | SEO title `The Reading Hour — Edition II, Open for Preorder \| Oh Betty Jaletti` → `The Reading Hour: Edition II \| Oh Betty Jaletti`; eyebrow `Edition II · Preorder` → `Edition II · Announced`; heading `Open for preorder` → `Not yet open`; CTA → `/pages/waitlist`; terms block kept, moved to future tense | §1b | PENDING |
| A-1 | Homepage title + meta advertise linen book covers, which are not for sale, and call the house French | `Linen Book Covers & Literary Keepsakes \| Oh Betty Jaletti` → `Edition I: What She Carries \| Oh Betty Jaletti` (46 chars) + new 153-char meta | §1a | PENDING |
| A-2 | Strip all prices/stock from `llms.txt`; add the missing gloves | `$94.00` → removed (real: $91.00); `$71.00` → removed (real: **$43.00**, a 65% overstatement); `Two pieces` → `Three pieces`; gloves entry added | §2 | PENDING |
| A-3 | Product schema emits a third-party brand on a house piece | `vendor: Glove Story` → `vendor: Maison Betty Jaletti` on The Out-the-Door Gloves | §5a | PENDING |
| A-4 | **Add one named object + hub link + sibling link to each of the 15 letters.** Zero product links today. Highest commercial value in this queue | 0 product links → 1 named object per letter; 9 of 15 point to `/pages/waitlist`, 6 to live products | §6 | PENDING |
| A-5 | Make `availability` honest — decided: made to order | `InStock` on stock of −5 / −12 / 0 → `BackOrder` via Liquid, flipping automatically | §5b | PENDING *(ready; Express copy needs E-9)* |
| **A-7** | **Made-to-order window — decided: 3–5 business days** | Add listing line *"Cut to order. Yours is made when you order it, and leaves the house in three to five business days."* + a `Made to order` clause in the shipping policy. Standard needs no change; `handlingTime` 3–5 confirmed | §7a–c | PENDING |
| **A-8** | **Express cannot be honoured at a 3–5 day making window** | `Express — packed the next business day`, "arrives in 2–4 business days", $15.00 → really 4–8 business days. Three options in §7d | §7d | PENDING *(needs E-9)* |

## SEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-1 | Unpublish `/pages/waitlist-trust-draft` — live, indexable duplicate of `/pages/waitlist` | §9 | PENDING |
| B-9 | Set `frontpage` collection SEO title/description (currently empty) | §9 | PENDING |
| C-3 | Worktable cluster: 14 pages at 250–290 words each diluting their hub. Give substance or fold into the hub | — | PENDING |
| C-5 | Stagger letter `dateModified` as letters are genuinely revisited (all 15 read July 14, 2026) | §3 | PENDING |

## Content / AEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-4 | Add `BlogPosting` schema to the article template — no letter emits any JSON-LD today | §3 | PENDING |
| B-2 | Fix shipping facts in `llms.txt`: says 2–3 day processing (policy says 3–5) and an Express $150 threshold that does not exist (it is $15.00 flat) | §2c | PENDING |
| C-4 | Add a `The short answer` block to `reading-nook-essentials` — the only letter breaking the pattern | §9 | PENDING |
| C-10 | Pick one scent pyramid and use it everywhere | §2c | PENDING *(needs E-4)* |
| — | Add Klaviyo capture at the end of each letter, house voice, no discount | §6 | PENDING |
| C-9 | Preorder status alignment | DONE 2026-11-20 — folded into A-6 once E-2 was answered |

## GEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-5 | Declare `hasMerchantReturnPolicy` + `shippingDetails` **once** at Organization level; add `mpn` = SKU. Return fees split to match policy: buyer pays on remorse, house pays on defect. `handlingTime` 3–5 confirmed | §4, §5c | PENDING |
| B-6 | Add `sameAs`, `email`, `address`, `areaServed: United States` to Organization schema | §4 | PENDING *(needs E-6)* |
| B-7 | Rewrite stale `Organization.description` — omits the gloves and Edition II | §4 | PENDING |
| C-1 | Set up Merchant Center with free listings — entry to Google AI Mode shopping, free. Needs B-8 + A-5 first | — | PENDING |
| C-2 | Verify **Sales channels → Agentic → ChatGPT** is enabled (read-only check) | §9 | PENDING |
| C-6 | **Confirm AI crawler policy: keep `robots.txt` permissive.** Recommended. Decision only, no change | §9 | PENDING |
| C-7 | Keep `llms.txt` as the agent contract, not an SEO asset. Accuracy is its whole value | §2 | PENDING |

## Store / Content

| ID | Change | Fix | Status |
|---|---|---|---|
| B-8 | Product images: 4+ per published piece. `mediaCount` is tote **1**, perfume **3**, gloves **1**, four Edition II pieces **0**. Needs your photographs; I draft alt text | §5d | PENDING |
| B-3 | Retire the dead International delivery zone, narrow the Samples profile to US, drop the unused Codigle profile. **No urgency** — checkout is already US-gated | §8 | PENDING |
| A-3-old | Map the edition lifecycle (waitlist / open / sealed / closed) and which page is linked when. A-6 is the first instance of this going wrong | — | PENDING |
| B-10 | The Advent | DONE 2026-11-20 — parked per E-7, no action |
| C-5-old | Policies verified published; returns policy is excellent | DONE 2026-11-20 — use it as the voice template for the shipping rewrite |

## Access / Technical

| ID | Change | Status |
|---|---|---|
| D-1 | Live-site access | DONE 2026-11-20 — session moved to the `BETTY` environment (allows `ohbettyjaletti.com`, `cdn.shopify.com`). Use it for all future audits |
| D-2 | Verify checkout settings (guest checkout, Shop Pay/Apple Pay, shipping shown early): read-only check | PENDING |
| D-3 | Core Web Vitals. PageSpeed host not in the allowlist; homepage HTML is 211KB, product pages ~170KB before assets | PENDING |
| D-4 | Search Console + Bing Webmaster verified, sitemap submitted? | PENDING |
| D-5 | Does a Merchant Center account exist? | PENDING |

## Resolved since W41

| ID | Item | Status |
|---|---|---|
| B-1-old | Collection SEO title whitespace / "Linen Covers" mismatch | DONE — both edition collections now have clean SEO fields *(though A-6 makes Reading Hour's inaccurate again, for a different reason)* |
| B-2-old | Product SEO titles too long | DONE — titles are now in range |
| C-4-old | Brand name split (Oh Betty / Maison Betty) | DONE — solved via `alternateName`. **Keep it**; only the `vendor` leak remains (A-3) |
| B-3-old | Products lacked extractable facts | DONE — `custom.materials`, `fit_dimensions`, `care`, `suitability`, `making_note` metafields on newer pieces |
| C-1-old | Answer-first guide pages | DONE — 3 hubs + 15 letters with `The short answer` blocks. Schema and product links still missing (B-4, A-4) |

## UX/UI

| ID | Change | Status |
|---|---|---|
| C-6-old | Reviews near add-to-cart post-launch | DEFER 2027-01-15 |
