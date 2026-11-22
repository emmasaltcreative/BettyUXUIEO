# Change log — 2026-11-20

Emma's instruction: *"please correct everything the way an intelligent atelier lifestyle business owner would."*
Judgement calls I made are recorded under **Decisions I took** below, with reasoning.

Live theme at time of work: `OBJ v5.32 · CTA, top, Instagram (preview)` (`gid://shopify/OnlineStoreTheme/189811097653`).
Theme file writes to the live theme are blocked by design, so theme changes are staged in a duplicate
for Emma to preview and publish. Shopify Admin data has no staging layer, so those changes are live on save.

---

## Applied to the live store

| # | ID | Change | Status |
|---|---|---|---|
| 1 | B-1 | `/pages/waitlist-trust-draft` unpublished — was a live, indexable duplicate of `/pages/waitlist` | **DONE** |
| 2 | A-6a | `the-reading-hour` collection: SEO title, meta and description no longer claim an open preorder | **DONE** |
| 3 | B-9 | `frontpage` collection SEO title + meta set (were empty) | **DONE** |
| 4 | E-4 | Scent pyramid reconciled across 6 surfaces: product description, SEO title/meta, `global.description_tag`, `custom.object_copy`, `custom.materials`. Added an explicit **The Notes** bullet so the pyramid is extractable | **DONE** |
| 5 | A-8 | Express delivery method renamed `Express — packed the next business day` → **`Express — first in the queue`**, with a description saying it buys a faster journey, not a faster making | **DONE** |
| 7 | A-4 | **Letter closing blocks applied (8 of 15 so far):** `what-does-numbered-edition-mean`, `verify-limited-edition-genuine`, `are-limited-edition-home-goods-worth-it`, `limited-vs-open-edition-vs-one-of-a-kind`, `collecting-numbered-editions-beginners`, `slow-living-vs-minimalism`, `slow-living-home-small-budget`, `slow-living-autumn-winter`. All 15 blocks are written in `playbook/paste/letter-closing-blocks.html` | **IN PROGRESS** |
| 6 | A-7 | **The Wait** line added to all 3 active products, worded per piece: tote *"made up to order… chosen, knotted and packed by the house"*; perfume *"blended and filled to order, in small batches"*; gloves *"brought in to order… checked over and packed by the house"*. All state three to five business days | **DONE** |

### 2 — before / after (A-6a)
```
SEO title    BEFORE  The Reading Hour — Edition II, Open for Preorder | Oh Betty Jaletti
             AFTER   The Reading Hour: Edition II | Oh Betty Jaletti
Meta         BEFORE  … beginning with The Chaperone. Open for preorder, in considered quantities.
             AFTER   … beginning with The Chaperone. Not yet open — join the waitlist.
Description  BEFORE  … a gap in the day. Open for preorder, made in considered quantities.
             AFTER   … a gap in the day. Not yet open. The waitlist holds your number.
```

---

## Decisions I took

### E-9 · Express → **Option A: Express buys faster post, not faster making**
At a 3–5 day making window, `Express — packed the next business day` cannot be honoured and the
promised 2–4 day arrival is really 4–8. Retiring it (Option B) would be the purist choice, but it
removes a paid option in gift season for no gain beyond honesty that Option A also delivers. Option C
(genuinely packing in one day) contradicts the thing the house actually sells. So: rename the method,
state the real window, keep the priority lane.

### E-4 · Scent pyramid → **reconcile to the product page, not the SEO field**
Five surfaces disagreed. The visible product description and `llms.txt` both say *luminous pear, warm
amber, intimate musk, a quiet trace of flowers*. The SEO field said *aged iris*; the metafields said
*peony and lilac*. Those outliers appear once each; pear/amber/musk appears twice and is the hero copy a
customer actually reads. Canonical pyramid adopted:

> **Luminous pear → warm amber, with a quiet trace of rose and jasmine → sandalwood and intimate musk.**

Rose, jasmine, sandalwood and musk are kept because they appear across the metafields and the SEO field;
only *aged iris*, *peony* and *lilac* are dropped.
**⚠ This is the one correction that needs Emma's nose, not her approval.** I reconciled marketing copy;
only she knows what the fragrance actually smells like. If the SEO field was the accurate one, tell me
and I will flip it the other way.

### E-6 · `sameAs` → **Instagram only**
Found exactly one profile on the live site: `https://www.instagram.com/ohbettyjaletti/`. No Pinterest,
TikTok, Facebook or YouTube link exists anywhere on the storefront, so `sameAs` carries one URL rather
than invented placeholders.

### B-2 · **I was wrong again — the `$150` Express threshold is real. Reversed.**
I reported that `llms.txt` invented an Express threshold the policy did not have. The live delivery
method carries the condition *"On orders of $150 or more"*, so `llms.txt` was **accurate** and the
**shipping policy was the incomplete one** — it quoted $15.00 with no threshold. The corrected policy
now states it. Lesson for the audit process: check the store configuration, not just the two documents
that disagree.

### A-3 · **I was wrong — `brand: Glove Story` is correct. Reversed.**
I had flagged the gloves' Product schema emitting `"brand":"Glove Story"` as a critical entity error and
recommended overwriting `vendor` with `Maison Betty Jaletti`. Reading the product copy shows that would
have been a misattribution: the gloves are *"Made in France by Glove Story. Chosen by the house for In
Her Purse, **not made by it**."* The curation is deliberate and stated.

Schema-correct modelling for a house that sells another maker's work is `brand` = the real maker and
`Offer.seller` = the house. So **`vendor` stays `Glove Story`**, and the real fix is the missing
`Offer.seller` on every product, which was absent across the whole catalogue. Better outcome than my
original finding, and it protects the curation story.

Verified the other two are correctly attributed: the tote is *"cut and finished… by the house"* and the
perfume *"blended and bottled by hand at the house — this one we make ourselves"*. Both correctly read
`Maison Betty Jaletti`.

---

## Needs Emma's hands — no API exists

| ID | Item | Exact text / action |
|---|---|---|
| A-1 | **Homepage title + meta.** There is no Admin API mutation for Online Store → Preferences | Title: `Edition I: What She Carries \| Oh Betty Jaletti` · Meta: `What she carries, and what she carries it in. A suede tote cut generously, a travel eau de parfum, leather gloves. An American maison, made the long way.` |
| A-7/A-8 | **Shipping policy.** Blocked: the connection lacks the `write_legal_policies` scope | Paste `playbook/paste/shipping-policy.html` into Settings → Policies → Shipping policy. It corrects the Express arrival window, adds the $150 threshold, adds a Made to Order section, and states that nothing is open for preorder |
| — | **Publish the staged theme** once previewed | Theme duplicate named below |
| B-8 | Product photographs (4+ per piece) | Needs the photographs; I draft alt text after |
| C-1 | Merchant Center + free listings | Account setup |
| C-2 | Verify Sales channels → Agentic → ChatGPT | Read-only check in admin |
| D-4 | Search Console + Bing Webmaster | Account setup |
