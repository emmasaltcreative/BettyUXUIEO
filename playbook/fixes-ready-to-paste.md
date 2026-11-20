# Ready to paste — W47 fixes
Written 2026-11-20. Every fact here was read from live Shopify data or the live storefront on that date.
**Nothing here is applied.** Each item maps to an approval ID in `review/approvals.md`.

Verified source values used below:
`The Brownstone Tote $91.00 · A Woman Remembered $43.00 · The Out-the-Door Gloves $89.00`
`Standard $8.00, free over $70.00, arrives 5–10 business days · Express $15.00, arrives 2–4 business days`
`Returns 30 days from delivery · Virginia, United States · hello@ohbettyjaletti.com`

---

## 1. Homepage title + meta — fixes A-1

Currently promises linen book covers, which are not for sale, and calls the house French.

**Recommended — Online Store → Preferences**

Title (53 chars):
```
Suede Totes, Travel Scent & Gloves | Oh Betty Jaletti
```

Meta description (143 chars):
```
Edition I, In Her Purse: an unstructured suede tote, a 10 mL travel eau de parfum, and gloves for cold mornings. Made in considered quantities.
```

**Alternative, voice-forward** — use only if the concrete version feels too plain. It trades some search
clarity for register, and the meta carries the specifics instead.

Title (46 chars):
```
Edition I: What She Carries | Oh Betty Jaletti
```
Meta (153 chars):
```
What she carries, and what she carries it in. A suede tote cut generously, a travel eau de parfum, leather gloves. An American maison, made the long way.
```

**Also change in the same pass:**
- `frontpage` collection SEO title/description — currently empty (B-9). Reuse the above.
- Remove **"French in spirit, American at heart"** wherever it appears. `llms.txt` and the legal notice both
  state Virginia, United States. Pick one story; the honest one is the American one.
- **Add to the launch checklist:** the homepage title changes with every edition.

---

## 2. `llms.txt` / `agents.md` corrections — fixes A-2, B-2, B-3, C-9, C-10

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
Both stated prices are wrong — $94.00 vs the real $91.00, and $71.00 vs the real **$43.00**, a 65% error.

**Then add this line immediately under the `## What is purchasable now` heading:**
```
This file states no prices, stock levels, or ship dates. For all three, read
`/products/{handle}.json` or the UCP/MCP endpoint — they are authoritative and current.
```
**Delete** the paragraph beginning *"Prices above are the current variant prices as of the review date."* —
it is no longer needed and is the source of the error.

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

### 2c. Resolve the contradictions
| In the file | Reality | Fix |
|---|---|---|
| "in-stock orders generally ship within 2–3 business days" | Policy says packed in **3–5** business days | Delete the sentence. Replace with: `Processing and transit windows are stated in the shipping policy; quote that, never this file.` |
| "Express $15.00 on orders of $150.00 or more" | Policy says Express **$15.00**, no threshold | Delete the whole rates list. Replace with: `Rates, thresholds and windows: `/policies/shipping-policy`. Checkout is authoritative.` |
| "the United States only… does not currently sell or ship internationally" | Shopify `shipsToCountries` lists **28 countries** | **Do not edit the file until this is decided** — see B-3. The file and the policy agree with each other and disagree with the store configuration |
| "No piece is open for preorder today" | Reading Hour collection SEO says **"Open for Preorder"** | Decide, then align both. The Chaperone is DRAFT, so today the file is right and the collection is wrong |
| Perfume: "Luminous pear… warm amber… intimate musk… rose and jasmine" | Shopify SEO: "Rose, jasmine, and aged iris over sandalwood and soft musk" | Pick one pyramid and use it on the product page, the SEO field and this file |

### 2d. Update the review date
```
House knowledge below was last reviewed **20 November 2026**.
```

---

## 3. `BlogPosting` schema for the 15 letters — fixes B-4

No letter currently emits any JSON-LD. Add to the article template, inside `<head>`.

**Liquid (recommended — covers all 15 at once):**
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

**Note on `author`:** an `Organization` author is correct here — the letters are signed by the house, not
a named person. If a byline is ever introduced, switch to `"@type": "Person"` and keep it consistent with
the visible byline.

**Also:** all 15 letters are dated July 14, 2026. `dateModified` will stay identical until the letters are
actually revisited. Stagger real revisions rather than back-dating (C-5).

---

## 4. Organization schema — fixes B-5, B-6, B-7

Replace the existing `Organization` block in `theme.liquid`. Additions: `sameAs`, `email`, `address`,
`areaServed`, `hasMerchantReturnPolicy`, `shippingDetails`, and a current `description`.

Declaring the return and shipping policy **once, here** is the documented approach — product-level markup is
for exceptions only.

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
    "returnFees": "https://schema.org/ReturnShippingFees",
    "returnShippingFeesAmount": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": 0
    },
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

**Three things to check before pasting:**
1. **`sameAs` must be filled in** with the real profile URLs. It is the main way an engine confirms
   "Oh Betty Jaletti" and "Maison Betty Jaletti" are one business. Leaving the placeholders in is worse
   than omitting the field.
2. **`returnShippingFeesAmount: 0` is wrong if the buyer pays return postage on a change of mind** — and
   our policy says they do. Either set a real amount or drop `returnFees`/`returnShippingFeesAmount` and
   let the linked policy speak. Do not state free returns we do not offer.
3. **`areaServed` assumes US-only.** Blocked on B-3 — Shopify is configured for 28 countries.
4. `@type: OnlineStore` is a subtype of `Organization` and is the better fit; if the theme depends on
   `Organization` elsewhere, keep `Organization` — both work.

**Fragrance exception** — the one place product-level policy markup is justified. On A Woman Remembered only:
```json
"hasMerchantReturnPolicy": {
  "@type": "MerchantReturnPolicy",
  "applicableCountry": "US",
  "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
  "merchantReturnDays": 30,
  "returnPolicySeasonalOverride": [],
  "customerRemorseReturnFees": "https://schema.org/ReturnShippingFees",
  "merchantReturnLink": "https://ohbettyjaletti.com/policies/refund-policy",
  "additionalProperty": {
    "@type": "PropertyValue",
    "name": "Return condition",
    "value": "Unopened bottles only. Once opened, fragrance cannot be returned."
  }
}
```

---

## 5. Product schema additions — fixes A-3, A-5, B-5

### 5a. `brand` must be the house — A-3, critical
`/products/out-the-door-leather-gloves` currently emits `"brand":"Glove Story"`, taken from Shopify `vendor`.

**Fix in Shopify, not in the theme:** set `vendor` to `Maison Betty Jaletti` on The Out-the-Door Gloves
and on every house piece. To keep supplier records, use a metafield (`custom.supplier`) or a tag — never
`vendor`, because `vendor` becomes `brand` in schema.

Then audit all ten: nine read `Maison Betty Jaletti`; the gloves are the only exception.

### 5b. Honest availability — A-5
All three active variants are `inventoryPolicy: CONTINUE` with quantities **−5**, **−12**, **0/0**, and all
three pages claim `InStock`.

Preferred, if selling ahead is deliberate:
```json
"availability": "https://schema.org/BackOrder"
```
with a visible ship window on the listing. In Liquid:
```liquid
"availability": "https://schema.org/{% if variant.available and variant.inventory_quantity > 0 %}InStock{% elsif variant.available %}BackOrder{% else %}OutOfStock{% endif %}"
```
This keeps the page honest automatically and matches the house's preorder model, which is a selling point
rather than an apology.

### 5c. `mpn` for feed matching — B-5
No `gtin` or `mpn` anywhere. With no barcodes, use the SKU:
```liquid
"mpn": {{ variant.sku | json }}
```
Keep `sku` as well; they serve different purposes.

### 5d. Images — B-8
`mediaCount`: tote **1**, perfume **3**, gloves **1**, four Edition II pieces **0**. Target 4+ per published
piece: hero on white, in-hand for scale, a detail, the parcel. Nothing is eligible for merchant listings
or AI shopping surfaces without images. Alt text can be drafted once the photographs exist.

---

## 6. The attention bridge — fixes A-4, the highest-value item here

Zero product links across every letter checked. Add one closing block per letter. **One object, named,
with the sentence that earns it** — not a product grid.

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

| Letters | The one object | Link while unpublished |
|---|---|---|
| `reading-nook-essentials`, `reading-corner-small-apartment`, `best-lighting-reading-at-night`, `reading-side-table-essentials` | The Chaperone | `/pages/waitlist` — say plainly it is coming |
| `evening-reading-habit`, `slow-living-rituals-under-an-hour`, `slow-living-evening-routine` | One More Chapter | `/pages/waitlist` |
| `slow-living-vs-minimalism`, `slow-living-home-small-budget` | A Woman Remembered | live — `/products/a-woman-remembered` |
| `slow-living-autumn-winter` | The Out-the-Door Gloves | live — `/products/out-the-door-leather-gloves` |
| `what-does-numbered-edition-mean`, `are-limited-edition-home-goods-worth-it`, `verify-limited-edition-genuine`, `limited-vs-open-edition-vs-one-of-a-kind`, `collecting-numbered-editions-beginners` | Edition I collection | live — `/collections/in-her-purse` |

**Two more links per letter, same pass:**
- **Up to its hub** — `/pages/slow-living`, `/pages/the-reading-nook`, or `/pages/numbered-editions`.
- **Across to one sibling letter**, in a sentence rather than a related-posts widget.

**And on the three hubs:** link down to each of their five letters. The hubs currently do not, so the
clusters are not yet clusters.

**Klaviyo capture** — the end of a 1,000-word letter is the warmest moment on the site. One line, house
voice, no discount:
```
Letters from the maison, when there is something worth saying. Nothing else.
```

---

## 7. Quick wins — no copy needed

| Fix | Where | ID |
|---|---|---|
| Unpublish `/pages/waitlist-trust-draft` | Admin → Pages | B-1 |
| Set `frontpage` collection SEO fields | Admin → Collections | B-9 |
| Verify **Sales channels → Agentic → ChatGPT** is enabled | Admin → Sales channels | C-2 |
| Decide The Advent: build or park | Admin → Products | B-10 |
| Add `The short answer` block to `reading-nook-essentials` | Admin → Blog posts | C-4 |
| Keep `robots.txt` permissive — no change, decision only | n/a | C-6 |
