# Approval queue — rewritten 2026-11-15 (W46)

**Status values:** `PENDING` · `APPROVE` · `REJECT` · `DEFER <date>` · `QUESTION: ...` · `DONE <date>`
**How to use:** edit only the Status column, then tell me (or just leave it — I read this file at the start of every run). Only `APPROVE` items are acted on. `REJECT` is permanent; I won't raise it again.

> **Note on the W41 queue:** all 14 items sat `PENDING` for 5 weeks. The store pivoted in that time, so re-approving stale items would have been wrong. The queue below is rebuilt against the store as it is today. W41 items that the pivot resolved (live-site access, brand-name split, policy pages) are closed in the audit's §0 and are not repeated here.

---

## ⚡ Decide this week (time-boxed)

| ID | Change | Why now | Status |
|---|---|---|---|
| A-2 | **The Advent: launch or drop?** If launching I need a price, images, and a go-ahead to write SEO fields + publish the page. | Its own copy says order by **8 Dec**; that is 23 days out and it is currently draft, $0.00, no images, page 404. | PENDING |
| A-3 | **Edition II preorder: which state?** (a) publish The Chaperone and lift the noindex, or (b) relabel nav to "Coming soon" and soften the collection copy to waitlist language. | Nav promises a preorder; the product 404s. Every day this runs, intent leaks. (b) takes ~20 min and stops it today. | PENDING |
| A-4 | **Confirm The Chaperone's real price.** Variant says **$169.00**; its own SEO description says **"$103"**. Which is right? | Must be settled before it is ever published, or the SERP snippet undercuts checkout by 39%. | PENDING |

---

## Critical — SEO

| ID | Change | Status |
|---|---|---|
| A-1 | Rewrite homepage title + meta, which currently advertise "linen book covers, journals & candles" (none of which exist). Proposed title: `In Her Purse: Suede Totes & Travel Perfume \| Oh Betty Jaletti`. I'll draft the meta for your approval. | PENDING |
| A-5 | Unpublish `/pages/waitlist-trust-draft` (public, indexable, titled "The Waitlist (trust draft)", duplicates `/pages/waitlist`) — or redirect it to `/pages/waitlist`. | PENDING |

---

## Critical — agent-facing accuracy (`agents.md`)

| ID | Change | Status |
|---|---|---|
| A-4a | Correct tote price in `agents.md`: **$94.00 → $91.00**. | PENDING |
| A-4b | Correct perfume price in `agents.md`: **$71.00 → $59.00** (a 20% overstatement AI agents are quoting as fact). | PENDING |
| B-1 | Add **The Scented Letter** to `agents.md` — it is live, free, 245 in stock, and the file currently says only two pieces are buyable. | PENDING |
| B-2 | Align preorder language: `agents.md` says "No piece is open for preorder today"; the storefront says "Open for preorder". Follows whatever you decide in A-3. | PENDING |

---

## SEO / technical

| ID | Change | Status |
|---|---|---|
| B-3 | Add `Article` schema to 15 journal articles + 3 guide pages (currently zero structured data on any of them). Theme edit. | PENDING |
| B-7 | Extend Product schema: `hasMerchantReturnPolicy`, `shippingDetails`, `color`, `material`, `weight`. The facts already exist in your policies — this just makes them machine-readable. | PENDING |
| B-8 | Assign GTINs/barcodes to variants (prerequisite for Merchant Center + agentic catalogue). Needs your product data. | PENDING |
| B-9 | 15 `worktable-*` pages have no meta descriptions and ~100–150 words each. **Choose:** (a) I write meta descriptions + thicken them, or (b) `noindex` the set until the concepts are real. | PENDING |
| B-10 | Write SEO title + description for The Scented Letter (currently empty). Keeping the `the-scented-card` handle. | PENDING |
| B-11 | Add an `<h1>` to `/pages/waitlist` and fix meta still reading "The doors open September 29". | PENDING |
| B-13 | Set SEO fields on the `frontpage` collection. | PENDING |
| D-1 | Add `sameAs` (social profiles) + `contactPoint` to Organization schema. **Send me your social URLs.** | PENDING |
| D-2 | Add visible "Last updated" dates to guides and articles. | PENDING |

---

## Content / AEO

| ID | Change | Status |
|---|---|---|
| B-4 | Commission 3–4 articles supporting **Edition I** (tote packing, travel fragrance, faux suede care, silk scarf styling). Today all 18 content pieces support the edition nobody can buy. I draft, you approve each. | PENDING |
| B-5 | Add 1–2 contextual in-body product links per article (currently only footer boilerplate). | PENDING |
| B-6 | Add 4+ images per product. **Needs your photography**; I'll write alt text and shot-list it. | PENDING |

---

## UX/UI

| ID | Change | Status |
|---|---|---|
| C-1 | Raise mobile tap targets to ≥44px (18 of 27 are currently under 40px). Theme CSS. | PENDING |
| C-2 | Fix double arrow on hero CTA ("SEE THE COLLECTION → →"). One character. | PENDING |
| C-3 | Add the free Scented Letter to main nav + offer it in cart/post-purchase. | PENDING |
| C-4 | Start review requests to the ~15 existing buyers via Klaviyo (feeds `aggregateRating`). | PENDING |

---

## Operations

| ID | Change | Status |
|---|---|---|
| B-12 | Turn on inventory tracking and set real edition sizes. Stock is currently untracked and has gone negative (−4 tote, −11 perfume), which sits badly against a "considered quantities / numbered editions" promise. | PENDING |
| D-4 | Agree a monthly `agents.md` review, triggered by any price or catalogue change (not just a calendar date). | PENDING |
| E-1 | Confirm Search Console + Bing Webmaster are verified and the sitemap is submitted. Read-only check — **I just need to know, or access.** | PENDING |

---

## Carried forward / deferred

| ID | Change | Status |
|---|---|---|
| W41 C-6 | Reviews near add-to-cart | DEFER 2027-01-15 |
| E-2 | Merchant Center feed (blocked on B-8 GTINs) | DEFER until B-8 done |
| E-3 | Closed-edition URL strategy — finish the drafted `/pages/edition-closed` + `/pages/ledger` before Edition I sells through | DEFER 2026-12-15 |
