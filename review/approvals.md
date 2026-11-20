# Approval queue
Status values: PENDING | APPROVE | REJECT | DEFER <date> | QUESTION: ... | DONE <date>
Edit the Status column. Only APPROVE items are acted on.

Ready-to-paste copy and markup for everything below: `playbook/fixes-ready-to-paste.md` (section noted per row).
Standing reference: `playbook/SEO-AEO-GEO-PLAYBOOK.md`.

---

## Decisions only you can make — these block other items

| ID | Decision | Status |
|---|---|---|
| **E-1** | **Shipping destinations: US-only, or international?** Shopify is configured for **28 countries**; the shipping policy and `llms.txt` both say United States only. Blocks B-3, the Organization schema `areaServed`, and the `llms.txt` rewrite. Has legal exposure beyond SEO (fragrance is stated ground-only, no international) | PENDING |
| **E-2** | **Is anything open for preorder right now?** Reading Hour collection SEO says "Open for Preorder"; `llms.txt` says nothing is; The Chaperone is DRAFT with a preorder tag. **Tell me which is true** and I align all three | PENDING |
| **E-3** | **Selling past zero: deliberate?** All 3 active variants are `CONTINUE` with stock **−5 / −12 / 0**, all claiming `InStock`. Options: (a) hold real stock, (b) present as backorder/preorder with a ship window, (c) stop overselling. (b) fits the house model | PENDING |
| **E-4** | **A Woman Remembered — which scent pyramid is correct?** Shopify SEO says "rose, jasmine, aged iris over sandalwood and soft musk"; `llms.txt` says "luminous pear, warm amber, intimate musk, a trace of rose and jasmine" | PENDING |
| **E-5** | **Homepage copy: concrete or voice-forward?** Two options in §1. Recommended is the concrete one ("Suede Totes, Travel Scent & Gloves") | PENDING |
| **E-6** | **Social profile URLs for `sameAs`** (Instagram / Pinterest / TikTok / anything else). Needed for B-6; it is the main signal that "Oh Betty Jaletti" and "Maison Betty Jaletti" are one business | PENDING |
| **E-7** | **The Advent — build this week or park it?** Draft, $0.00, no SKU, media, SEO or metafields; `/pages/advent` unpublished. It is Nov 20 | PENDING |

## Critical

| ID | Change | Fix | Status |
|---|---|---|---|
| A-1 | Rewrite homepage title + meta — they advertise linen book covers, which are not for sale, and call the house French | §1 | PENDING |
| A-2 | Strip all prices/stock from `llms.txt` + add the missing gloves. Two of three prices are wrong; the perfume is off by **65%** ($71 stated vs $43 actual) | §2 | PENDING |
| A-3 | Set `vendor` to `Maison Betty Jaletti` on The Out-the-Door Gloves — its Product schema currently emits `"brand":"Glove Story"` | §5a | PENDING |
| A-4 | **Add one named object + hub link + sibling link to each of the 15 letters.** Zero product links exist today. Highest-value item in this queue | §6 | PENDING |
| A-5 | Make `availability` honest in Product schema (blocked on E-3) | §5b | PENDING |

## SEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-1 | Unpublish `/pages/waitlist-trust-draft` — live, indexable duplicate of `/pages/waitlist` | §7 | PENDING |
| B-9 | Set `frontpage` collection SEO title/description (currently empty) | §7 | PENDING |
| C-3 | Worktable cluster: 14 pages at 250–290 words each diluting their hub. Give substance or fold into the hub | — | PENDING |
| C-5 | Stagger letter `dateModified` as letters are genuinely revisited (all 15 read July 14, 2026) | §3 | PENDING |

## Content / AEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-4 | Add `BlogPosting` schema to the article template — no letter emits any JSON-LD today | §3 | PENDING |
| B-2 | Fix shipping facts in `llms.txt`: it says 2–3 day processing (policy says 3–5) and an Express $150 threshold that does not exist | §2c | PENDING |
| B-3 | Align shipping destinations across store config, policy and `llms.txt` (blocked on E-1) | §2c | PENDING |
| C-4 | Add a `The short answer` block to `reading-nook-essentials` — the only letter breaking the pattern | §7 | PENDING |
| C-9 | Align preorder status across collection SEO, `llms.txt` and the product (blocked on E-2) | §2c | PENDING |
| C-10 | Pick one scent pyramid and use it everywhere (blocked on E-4) | §2c | PENDING |
| — | Add Klaviyo capture at the end of each letter, house voice, no discount | §6 | PENDING |

## GEO

| ID | Change | Fix | Status |
|---|---|---|---|
| B-5 | Declare `hasMerchantReturnPolicy` + `shippingDetails` **once** at Organization level; add `mpn` = SKU to products | §4, §5c | PENDING |
| B-6 | Add `sameAs`, `email`, `address`, `areaServed` to Organization schema (blocked on E-6, E-1) | §4 | PENDING |
| B-7 | Rewrite stale `Organization.description` — omits the gloves and Edition II | §4 | PENDING |
| C-1 | Set up Merchant Center with free listings — entry to Google AI Mode shopping, free. Needs B-8 + A-5 first | — | PENDING |
| C-2 | Verify **Sales channels → Agentic → ChatGPT** is enabled (read-only check) | §7 | PENDING |
| C-6 | **Confirm AI crawler policy: keep `robots.txt` permissive.** Recommended. No change needed, decision only | §7 | PENDING |
| C-7 | Keep `llms.txt`, but as the agent contract only — not an SEO asset. Accuracy is its whole value | §2 | PENDING |

## Store / Content

| ID | Change | Fix | Status |
|---|---|---|---|
| B-8 | Product images: 4+ per published piece. `mediaCount` is tote **1**, perfume **3**, gloves **1**, four Edition II pieces **0**. Needs your photographs; I draft alt text | §5d | PENDING |
| B-10 | The Advent: build or park (blocked on E-7) | §7 | PENDING |
| A-3-old | Map the edition lifecycle (waitlist / open / sealed / closed) and which page is linked when | — | PENDING |
| C-5-old | Verified: policies are published and the returns policy is excellent. **Closed** — use it as the voice template for the shipping rewrite | — | DONE 2026-11-20 |

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
| B-1-old | Collection SEO title whitespace / "Linen Covers" mismatch | DONE — both edition collections now have clean, accurate SEO fields |
| B-2-old | Product SEO titles too long | DONE — titles are now in range |
| C-4-old | Brand name split (Oh Betty / Maison Betty) | DONE — solved via `alternateName` in Organization schema. **Keep it**; only `vendor` leaks remain (A-3) |
| B-3-old | Products lacked extractable facts | DONE — `custom.materials`, `fit_dimensions`, `care`, `suitability`, `making_note` metafields on newer pieces |
| C-1-old | Answer-first guide pages | DONE — 3 hubs + 15 letters with `The short answer` blocks. Schema and product links still missing (B-4, A-4) |

## UX/UI

| ID | Change | Status |
|---|---|---|
| C-6-old | Reviews near add-to-cart post-launch | DEFER 2027-01-15 |
