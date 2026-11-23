# Ready to paste — W47 fixes
Written 2026-11-20 · **decisions of 2026-11-20 applied** (E-1, E-2, E-3, E-5, E-7).
Every fact here was read from live Shopify data or the live storefront on that date.
**Nothing here is applied to the live store.** Each item maps to an approval ID in `review/approvals.md`.

Verified source values used below:
`The Brownstone Tote $91.00 · A Woman Remembered $43.00 · The Out-the-Door Gloves $89.00`
`Market: United States only (single ACTIVE market) · Standard $8.00, free over $70.00 · Express $15.00`
`Returns 30 days from delivery · Virginia, United States · hello@ohbettyjaletti.com`

**Decisions in force:**
- **US only.** Already true at market level — see §8 for the actual cleanup.
- **Nothing is open for preorder.** Drives §1b, the biggest change in this document.
- **Overselling is selling, then fulfilling on demand.** Made-to-order. Drives §5b and §7.
- **Voice-forward homepage copy.**
- **The Advent is parked.**
- **Made-to-order window: 3–5 business days** — matches the existing policy. See §7.

**Still blocked, awaiting a decision:** the scent pyramid (E-4), the social profile URLs (E-6), and what to
do about Express (E-9, §7d — the only thing now holding the A-5/A-7/B-5 batch).

---

## 1a. Homepage title + meta — fixes A-1

Currently promises linen book covers, which are not for sale, and calls the house French.

**Online Store → Preferences**

Title (46 chars):
```
Edition I: What She Carries | Oh Betty Jaletti
```

Meta description (153 chars):
```
What she carries, and what she carries it in. A suede tote cut generously, a travel eau de parfum, leather gloves. An American maison, made the long way.
```

**Also in the same pass:**
- `frontpage` collection SEO title/description — currently empty (B-9). Reuse the above.
- Remove **"French in spirit, American at heart"** wherever it appears. `llms.txt` and the legal notice both
  state Virginia, United States. The meta above carries "An American maison" instead.
- **Add to the launch checklist:** the homepage title changes with every edition.

---

## 1b. The Reading Hour collection is a live open-preorder page — fixes A-6

**This is the most urgent item in this document, and it is a bigger change than an SEO field.**

You said nothing is open for preorder. The live collection page at `/collections/the-reading-hour`
currently says otherwise, five times over, and then shows nothing to buy — because The Chaperone is DRAFT,
so the product grid renders **"Between editions · Nothing here at the moment."**

Verified on the live page (422 rendered words):

| Where | Current live text |
|---|---|
| Eyebrow | `Edition II · Preorder` |
| Hero | `Preorder. Your number in the edition is held the moment you order.` |
| Section heading | `The edition — Open for preorder` |
| SEO title | `The Reading Hour — Edition II, Open for Preorder \| Oh Betty Jaletti` |
| Meta | `… Open for preorder, in considered quantities.` |
| Terms block | `How a preorder works here` → `I. You are charged today` … |
| Product grid | `Between editions · Nothing here at the moment.` |

A visitor is invited to preorder, told they will be charged today, and then given nothing to order.
A crawler reads a page that claims an open preorder with zero offers. Both are worse than silence.

### SEO fields

Title (47 chars):
```
The Reading Hour: Edition II | Oh Betty Jaletti
```
Meta (145 chars):
```
Edition II from Maison Betty Jaletti: objects for the hour you keep for yourself, beginning with The Chaperone. Not yet open — join the waitlist.
```
Collection description:
```html
<p>Edition II. The hour after the dishes and before the sleep, and the few things that make it an occasion rather than a gap in the day. Not yet open. The waitlist holds your number.</p>
```

### Theme / section copy

| Current | Change to |
|---|---|
| `Edition II · Preorder` | `Edition II · Announced` |
| `Preorder. Your number in the edition is held the moment you order.` | `Not yet open. The waitlist holds your number, and earns you one letter when the doors open early.` |
| `The edition — Open for preorder` | `The edition — Not yet open` |
| Primary button → product | Primary button → `/pages/waitlist`, labelled `Join the waitlist` |

### The preorder terms block — keep it, move it to future tense

Do **not** delete it. *"Written down because a preorder is a promise, and promises should be legible"* is
the best trust writing on the site and exactly what AI answers quote. It is only wrong in tense.

| Current | Change to |
|---|---|
| `How a preorder works here` | `How a preorder will work` |
| `Plainly, so there is nothing to discover later.` | keep as is |
| `I. You are charged today` | `I. You will be charged on the day you order` |
| `II. We cut yours when the edition opens` | keep as is |
| `III. It ships by the date on the page` | keep as is |
| `IV. If it cannot be made` | keep as is |

**Alternative** if future tense reads oddly on a page with no offers: move the whole block to
`/pages/waitlist`, where a reader is already leaning in, and link to it from the collection. Either works;
the reframe is less work and keeps the collection page substantial.

### Two more places carrying the same claim
- **The Chaperone's SEO description** reads *"Preorder The Chaperone … Charged today"*. It is DRAFT so not
  live, but it must not be published in that state while nothing is open. Flag on the publish checklist.
- **`llms.txt` is already correct** — *"No piece is open for preorder today."* Leave that line alone.

---

## 2. `llms.txt` / `agents.md` corrections — fixes A-2, B-2

The file is well written and should be kept. Three classes of change.

### 2a. Delete every price and stock state
**Find** (in `## What is purchasable now`):
```
**The Brownstone Tote** · `/products/the-brownstone-tote` · $94.00 · No. 1 · in stock, ships now
```
**Replace with:**
```
**The Brownstone Tote** · `/products/the-brownstone-tote` · No. 1
```
Same for **A Woman Remembered** (remove `· $71.00 ·` and `in stock, ships now`).
Both stated prices are wrong — $94.00 vs the real $91.00, and $71.00 vs the real **$43.00**, a 65% overstatement.

**Add immediately under the `## What is purchasable now` heading:**
```
This file states no prices, stock levels, or ship dates. For all three, read
`/products/{handle}.json` or the UCP/MCP endpoint — they are authoritative and current.
```
**Delete** the paragraph beginning *"Prices above are the current variant prices as of the review date."* —
it is the source of the error and is no longer needed.

### 2b. Add the missing published product
The Out-the-Door Gloves was published Nov 16, after the file's Nov 12 review, so it is absent while the
file says "Two pieces are published and buyable."

**Find:** `Two pieces are published and buyable.`
**Replace:** `Three pieces are published and buyable.`

**Add under Edition I, after A Woman Remembered:**
```
**The Out-the-Door Gloves** · `/products/out-the-door-leather-gloves` · No. 3
Chocolate leather gloves for cold mornings and everyday outings, in Small and Medium.
For the buyer who keeps one pair by the door and does not want to think about it again.
```

### 2c. Shipping facts
| In the file | Reality | Fix |
|---|---|---|
| "in-stock orders generally ship within 2–3 business days" | Policy says packed in **3–5** business days | Delete the sentence. Replace with: `Processing and transit windows are stated in the shipping policy; quote that, never this file.` |
| "Express $15.00 on orders of $150.00 or more" | Delivery profile shows Express **$15.00 flat**, no threshold | Delete the rates list. Replace with: `Rates, thresholds and windows: /policies/shipping-policy. Checkout is authoritative.` |
| "the United States only…" | **Correct — leave as is.** Single ACTIVE market is US | No change |
| "No piece is open for preorder today" | **Correct — leave as is** | No change |

### 2d. Made-to-order, and the review date
Add to `## What is purchasable now` (see §7 for why):
```
Pieces are cut to demand. A published piece can be ordered whether or not stock is on the shelf;
the listing states its window. Availability in page markup reads BackOrder for these, which means
orderable and made to order — not unavailable.
```
And update:
```
House knowledge below was last reviewed **20 November 2026**.
```

**Still blocked:** the scent pyramid for A Woman Remembered (E-4). Do not edit that passage until decided.

---

## 3. `BlogPosting` schema for the 15 letters — fixes B-4

No letter currently emits any JSON-LD. Add to the article template, inside `<head>`.

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": {{ request.origin | append: article.url | json }}
  },
  "headline": {{ article.title | json }},
  "description": {{ article.excerpt_or_content | strip_html | truncatewords: 40 | json }},
  "datePublished": {{ article.published_at | date: "%Y-%m-%d" | json }},
  "dateModified": {{ article.updated_at | date: "%Y-%m-%d" | json }},
  "author": {
    "@type": "Organization",
    "name": "Oh Betty Jaletti",
    "url": "https://ohbettyjaletti.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Oh Betty Jaletti",
    "logo": {
      "@type": "ImageObject",
      "url": "https://ohbettyjaletti.com/cdn/shop/t/53/assets/obj-floral-mark.svg"
    }
  }{% if article.image %},
  "image": {{ article.image | image_url: width: 1200 | prepend: "https:" | json }}{% endif %}
}
</script>
```

**On `author`:** an `Organization` author is correct — the letters are signed by the house, not a person.
If a byline is ever introduced, switch to `"@type": "Person"` and match the visible byline.

**Note:** all 15 letters are dated July 14, 2026, so `dateModified` stays identical until they are actually
revisited. Stagger real revisions rather than back-dating (C-5).

---

## 4. Organization schema — fixes B-5, B-6, B-7

Replace the existing `Organization` block in `theme.liquid`. `areaServed` is **United States**, per the
US-only decision. Declaring the return and shipping policy **once here** is the documented approach;
product-level markup is for exceptions only.

```json
{
  "@context": "https://schema.org",
  "@type": "OnlineStore",
  "name": "Oh Betty Jaletti",
  "alternateName": "Maison Betty Jaletti",
  "url": "https://ohbettyjaletti.com",
  "logo": "https://ohbettyjaletti.com/cdn/shop/t/53/assets/obj-floral-mark.svg",
  "foundingDate": "2026",
  "email": "hello@ohbettyjaletti.com",
  "slogan": "Little things, kept close.",
  "description": "Oh Betty Jaletti is an American maison for the ones who take the slow way: small, useful, unreasonably pretty things, made with intention and released in considered quantities. Edition I, In Her Purse, holds the Brownstone Tote, A Woman Remembered and the Out-the-Door Gloves.",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "VA",
    "addressCountry": "US"
  },
  "areaServed": { "@type": "Country", "name": "United States" },
  "sameAs": [
    "FILL: https://www.instagram.com/...",
    "FILL: https://www.pinterest.com/...",
    "FILL: https://www.tiktok.com/@..."
  ],
  "hasMerchantReturnPolicy": {
    "@type": "MerchantReturnPolicy",
    "applicableCountry": "US",
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
    "merchantReturnDays": 30,
    "returnMethod": "https://schema.org/ReturnByMail",
    "customerRemorseReturnFees": "https://schema.org/ReturnShippingFees",
    "itemDefectReturnFees": "https://schema.org/FreeReturn",
    "merchantReturnLink": "https://ohbettyjaletti.com/policies/refund-policy"
  },
  "shippingDetails": {
    "@type": "OfferShippingDetails",
    "shippingRate": {
      "@type": "MonetaryAmount",
      "value": 8.00,
      "currency": "USD"
    },
    "shippingDestination": {
      "@type": "DefinedRegion",
      "addressCountry": "US"
    },
    "deliveryTime": {
      "@type": "ShippingDeliveryTime",
      "handlingTime": {
        "@type": "QuantitativeValue",
        "minValue": 3, "maxValue": 5,
        "unitCode": "DAY"
      },
      "transitTime": {
        "@type": "QuantitativeValue",
        "minValue": 2, "maxValue": 5,
        "unitCode": "DAY"
      }
    }
  }
}
```

**Before pasting:**
1. **`sameAs` must be filled in** with real profile URLs (E-6). It is the main way an engine confirms
   "Oh Betty Jaletti" and "Maison Betty Jaletti" are one business. Leaving placeholders in is worse than
   omitting the field — so either fill it or delete the key.
2. The return fees are split correctly to match your policy: **buyer pays on a change of mind**
   (`customerRemorseReturnFees`), **house pays when the fault is ours** (`itemDefectReturnFees`). Do not
   collapse these into a single `returnFees: FreeReturn` — that would promise free returns you do not offer.
3. `handlingTime` of 3–5 days is **confirmed correct** — the made-to-order window was set to 3–5, which is
   what the policy already claimed. No change needed here. Express is a separate problem; see §7d.
4. `@type: OnlineStore` is a subtype of `Organization`. If the theme depends on `Organization` elsewhere,
   keep `Organization`; both work.

**Fragrance exception** — the one place product-level policy markup is justified. On A Woman Remembered only:
```json
"hasMerchantReturnPolicy": {
  "@type": "MerchantReturnPolicy",
  "applicableCountry": "US",
  "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
  "merchantReturnDays": 30,
  "merchantReturnLink": "https://ohbettyjaletti.com/policies/refund-policy",
  "additionalProperty": {
    "@type": "PropertyValue",
    "name": "Return condition",
    "value": "Unopened bottles only. Once opened, fragrance cannot be returned."
  }
}
```

---

## 5. Product schema — fixes A-3, A-5, B-5

### 5a. `brand` must be the house — A-3, critical
`/products/out-the-door-leather-gloves` emits `"brand":"Glove Story"`, taken from Shopify `vendor`.

**Fix in Shopify, not the theme:** set `vendor` to `Maison Betty Jaletti` on The Out-the-Door Gloves.
To keep supplier records, use a metafield (`custom.supplier`) or a tag — never `vendor`, because `vendor`
becomes `brand` in schema. Nine of ten products are already correct; the gloves are the only exception.

### 5b. Availability — A-5, decided: made to order
All three active variants are `inventoryPolicy: CONTINUE` with quantities **−5**, **−12**, **0/0**, and all
three pages claim `InStock`. Since selling ahead is deliberate, the honest value is **`BackOrder`** —
which in schema means *orderable, not yet in hand*, exactly the model described.

```liquid
"availability": "https://schema.org/{% if variant.available and variant.inventory_quantity > 0 %}InStock{% elsif variant.available %}BackOrder{% else %}OutOfStock{% endif %}"
```

This flips automatically as stock comes and goes, so it stays true without anyone remembering to update it.

**`BackOrder` is not a downgrade.** It is how a made-to-order house is supposed to describe itself, and it
protects against the Merchant Center disapprovals that follow from claiming stock you do not hold.
It does require a visible window on the listing, now set at **3–5 business days** — see §7a.

### 5c. `mpn` for feed matching — B-5
No `gtin` or `mpn` anywhere. With no barcodes, use the SKU:
```liquid
"mpn": {{ variant.sku | json }}
```
Keep `sku` as well; they serve different purposes.

### 5d. Images — B-8
`mediaCount`: tote **1**, perfume **3**, gloves **1**, four Edition II pieces **0**. Target 4+ per published
piece: hero on white, in-hand for scale, a detail, the parcel. Nothing is eligible for merchant listings or
AI shopping surfaces without images. Alt text can be drafted once the photographs exist.

---

## 6. The attention bridge — fixes A-4, the highest-value item here

Zero product links across every letter checked. Add one closing block per letter. **One object, named, with
the sentence that earns it** — not a product grid.

**The block, in house voice** (example, for `what-does-numbered-edition-mean`):
```html
<aside class="letter-object">
  <p class="letter-object__eyebrow">The house keeps its own numbers</p>
  <p>
    Edition I is called <em>In Her Purse</em>, and every piece in it is marked with its place —
    No. 1 the tote, No. 2 the scent, No. 3 the gloves. Not a serial number. A position, in a run
    the house declared before it opened.
  </p>
  <p><a href="/collections/in-her-purse">See Edition I, In Her Purse &rarr;</a></p>
</aside>
```

**The mapping** — one object per letter cluster:

| Letters | The one object | Link |
|---|---|---|
| `reading-nook-essentials`, `reading-corner-small-apartment`, `best-lighting-reading-at-night`, `reading-side-table-essentials` | The Chaperone | `/pages/waitlist` — not yet open, say so plainly |
| `evening-reading-habit`, `slow-living-rituals-under-an-hour`, `slow-living-evening-routine` | One More Chapter | `/pages/waitlist` |
| `slow-living-vs-minimalism`, `slow-living-home-small-budget` | A Woman Remembered | live — `/products/a-woman-remembered` |
| `slow-living-autumn-winter` | The Out-the-Door Gloves | live — `/products/out-the-door-leather-gloves` |
| `what-does-numbered-edition-mean`, `are-limited-edition-home-goods-worth-it`, `verify-limited-edition-genuine`, `limited-vs-open-edition-vs-one-of-a-kind`, `collecting-numbered-editions-beginners` | Edition I collection | live — `/collections/in-her-purse` |

Nine of the fifteen letters point at the waitlist rather than a product. That is the correct outcome while
Edition II is unopened, and it is a far better one than a bounce.

**Two more links per letter, same pass:**
- **Up to its hub** — `/pages/slow-living`, `/pages/the-reading-nook`, or `/pages/numbered-editions`.
- **Across to one sibling letter**, in a sentence rather than a related-posts widget.

**And on the three hubs:** link down to each of their five letters. The hubs do not currently, so the
clusters are not yet clusters.

**Klaviyo capture** — the end of a 1,000-word letter is the warmest moment on the site. One line, house
voice, no discount:
```
Letters from the maison, when there is something worth saying. Nothing else.
```

---

## 7. Made-to-order window — **decided: 3–5 business days** — fixes A-7

The window is **three to five business days to pack**, which is exactly what the shipping policy already
claims. So Standard needs no rewrite, and the `handlingTime` of 3–5 in §4 was already correct.

### 7a. The listing line — add to each made-to-order piece

House voice, and it reframes the wait as the point rather than the delay:
```
Cut to order. Yours is made when you order it, and leaves the house in three to five business days.
```

### 7b. The policy clause — add to the shipping policy under "Order Processing"

```
Made to order. Most pieces are cut when you order them rather than held on a shelf. That is the three
to five business days above; it is not a delay, it is the making. If a piece will take materially
longer, we write to you with a new date, and you may cancel for a full refund.
```

### 7c. Schema — confirmed, no change from §4
```json
"handlingTime": { "@type": "QuantitativeValue", "minValue": 3, "maxValue": 5, "unitCode": "DAY" }
```

### 7d. Express is now the one remaining conflict — **E-9**

Standard reconciles cleanly. Express does not, and the arithmetic is worth seeing plainly.

**The policy currently promises:**
> *Express — arrives in 2–4 business days. **Packed first, within one business day**, then 1–3 business
> days in the post. $15.00.*

The delivery method itself is named **"Express — packed the next business day"**.

**With a 3–5 day making window, both claims are false:**

| | Packing | Post | Stated arrival | Actual arrival |
|---|---|---|---|---|
| Standard $8.00 | 3–5 | 2–5 | 5–10 business days | **5–10** ✓ |
| Express $15.00 | 3–5 *(not 1)* | 1–3 | 2–4 business days | **4–8** ✗ |

So Express would cost $15 to save roughly one to two business days, while advertising that it saves six.
That is the part worth your judgement, not just a copy fix.

**Option A — Express buys faster post, not faster making** *(recommended if Express stays bookable)*
Copy-only change, honest, keeps the revenue.
- Rename the method: `Express — packed the next business day` → `Express — first in the queue`
- Policy: *"Express — arrives in 4–8 business days. Packed in three to five business days, then 1–3 in the post. $15.00."*

**Option B — retire Express until stock exists**
Cleanest. Nothing is promised that the house does not control. Costs a little revenue on a method that
currently cannot deliver what it says.

**Option C — keep next-business-day packing and genuinely honour it for Express orders**
Only if a single piece really can be cut, numbered, packed and signed off in one business day. If it can,
this is the best outcome and the policy stays as written. If it cannot, it is the worst, because it is the
promise most likely to be tested by the buyer who paid extra.

**My recommendation: A.** It is a copy change, it is true, and it keeps a priority lane for the buyer who
wants one — without claiming the making can be rushed, which is the opposite of what the house sells.

## 8. Shipping zones: the "28 countries" correction — fixes B-3

**Correction to the W47 audit.** I reported that Shopify was configured to ship to 28 countries while the
policy said US-only, and flagged legal exposure. That was overstated. The accurate position:

- **Markets:** exactly one — `United States`, `ACTIVE`, region `US`. **Checkout is already gated to the US.**
  Non-US customers cannot buy. The policy and `llms.txt` are correct, and no customer-facing promise is broken.
- `shop.shipsToCountries` returns 28 countries because it unions **delivery zones**, not markets. The zones:

| Profile | Zone | Countries | Methods |
|---|---|---|---|
| General profile *(default)* | Domestic | US | Standard $8.00 · Standard $0.00 *(the free-over-$70 tier)* · Express $15.00 |
| General profile *(default)* | **International** | 27 | `usps`, `dhl_express` — **both active** |
| Samples — posted free | Everywhere the house writes | 28 | Posted — free $0.00 |
| Codigle Combine Shipping | Combine Shipping | Rest of World | Combine Shipping $0.00 |

**So the real finding is dead configuration, not a broken promise.** It still matters:
1. The **International zone has active carrier rates.** If a second market is ever added, international
   shipping switches on silently, with no policy to match it.
2. `shipsToCountries` is what feeds, API consumers and shopping agents read. It says 28; the truth is 1.
3. The **Samples** profile covers 28 countries for The Scented Letter — which is `ARCHIVED`, so moot today,
   but it is how a free sample would end up posted to Singapore.
4. **Codigle Combine Shipping** is an app-created profile covering Rest of World. If that app is no longer
   in use, the profile should go with it.

**Recommended:** delete the International zone from the General profile, narrow the Samples profile to US,
and remove the Codigle profile if the app is gone. Low risk, and it makes `shipsToCountries` agree with
reality. **No urgency** — nothing is mis-sold today.

---

## 9. Quick wins — no copy needed

| Fix | Where | ID |
|---|---|---|
| Unpublish `/pages/waitlist-trust-draft` | Admin → Pages | B-1 |
| Set `frontpage` collection SEO fields | Admin → Collections | B-9 |
| Verify **Sales channels → Agentic → ChatGPT** is enabled | Admin → Sales channels | C-2 |
| Add `The short answer` block to `reading-nook-essentials` | Admin → Blog posts | C-4 |
| Keep `robots.txt` permissive — decision only, no change | n/a | C-6 |
| The Advent — **parked**, no action | n/a | B-10 |
