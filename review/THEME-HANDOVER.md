# Theme handover — staged in `OBJ v5.35 · SEO-AEO-GEO corrections`
Written 2026-11-23 · theme id `gid://shopify/OnlineStoreTheme/189964484661`

**Forked from `OBJ v5.34 · Velvet Christmas bow`**, which was live at the time, so publishing it keeps
your bow work. Nothing is live until you publish it.

---

## ⚠ Delete this one first

**`OBJ v5.33 · SEO/AEO/GEO corrections`** — my earlier attempt, forked from **v5.32**.
**Publishing it would revert the Velvet Christmas bow.** I cannot delete a theme (the mutation is
blocked), so please delete it in Online Store → Themes so it can't be published by mistake.

It also contains a stray `snippets/obj-write-test.liquid` I used to test write access. It dies with the theme.

---

## Staged and ready (6 files)

| File | Change | Fixes |
|---|---|---|
| `templates/collection.the-reading-hour.json` | Eyebrow `Edition II · Preorder` → `· Announced`; hero note → *"Not yet open. The waitlist holds your number…"*; button → **Join the waitlist** → `/pages/waitlist`; grid heading `Open for preorder` → `Not yet open`; terms retitled *"How a preorder will work"*; note I → *"You **will be** charged on the day you order"* | **A-6b** |
| `sections/main-article.liquid` | Adds `BlogPosting` JSON-LD: headline, description, `datePublished`, `dateModified`, author, publisher, `isPartOf`, image. Visible layout untouched | **B-4** |
| `snippets/obj-organization-schema.liquid` | **New.** Full `OnlineStore` schema: `sameAs`, `email`, `address`, `areaServed`, `hasMerchantReturnPolicy` (30 days, remorse vs defect fees split correctly), `shippingDetails` (3–5 handling, 2–5 transit). Reads its two volatile facts from shop metafields with safe fallbacks | **B-5, B-6, B-7** |
| `snippets/obj-product-schema.liquid` | **New.** Corrected Product schema: honest `availability`, all photographs, `mpn`, `Offer.seller`. **Not yet wired in — see below** | **A-5, B-5** |
| `layout/theme.liquid` | Renders the Organization snippet in place of the old inline block; homepage meta fallback now describes Edition I accurately | **B-6, B-7** |
| `templates/agents.md.liquid` | **Prices removed entirely.** The piece list is now **generated from the live catalogue**, assembled from product metafields, so it cannot go stale again. Also: three pieces not two, gloves credited to Glove Story, processing 2–3 → 3–5 days, Express described honestly, made-to-order section added, `BackOrder` explained to agents, review date bumped | **A-2, B-2, C-7** |

### Data layer (already live, survives every fork)
Created two shop metafields the Organization snippet reads:
- `custom.org_description` — edit this per edition instead of the theme
- `custom.org_same_as` — currently the one Instagram URL

---

## One line left, and I'd rather you did it than me

`sections/main-product.liquid` still emits its own Product schema with
`availability: InStock` regardless of stock. The corrected logic is already staged as
`snippets/obj-product-schema.liquid`; it just needs calling.

**In Online Store → Themes → `OBJ v5.35` → Edit code → `sections/main-product.liquid`**, find the
first `<script type="application/ld+json">` block near the bottom — the one starting
`"@context": "https://schema.org/"` and `"@type": "Product"` — and replace that whole block
(down to and including its `</script>`) with this single line:

```liquid
{% render 'obj-product-schema', product: product, variant: variant, preproduction: preproduction, object_copy: object_copy %}
```

Leave the `BreadcrumbList` block below it alone.

**Why I stopped here:** that file is 37,610 bytes and there is no patch API — I would have had to
retype the whole thing, and with `theme_bash` and `theme_screenshot` both blocked I had no way to
verify it rendered afterwards. Retyping your most important template blind is a worse risk than a
one-line edit you can see. The hard part (the logic) is done and staged.

What it changes once wired:
- `InStock` only with real stock · `BackOrder` when orderable but unstocked · `OutOfStock` otherwise
  (replacing `Discontinued`, which means retired). Untracked inventory reads as `InStock`, not backorder.
- Every photograph listed, not just the first
- `mpn` = SKU, and `Offer.seller` = the house

---

## Still needs you, outside the theme

| Item | Where |
|---|---|
| **Homepage title + meta** — no Admin API for Online Store → Preferences | Title `Edition I: What She Carries \| Oh Betty Jaletti`; meta in `playbook/fixes-ready-to-paste.md` §1a |
| **Shipping policy** — my connection lacks `write_legal_policies` | Paste `playbook/paste/shipping-policy.html` |
| Product photographs, 4+ per piece | I draft alt text once they exist |
| Merchant Center + free listings; Search Console / Bing | Account setup |

---

## Theme hygiene, so this stops happening

While I worked, the live theme changed under me and my first fork went stale. Per Playbook 3.1:
1. Always fork from the **current live** theme. Never from an older `v5.x`.
2. Keep one or two dev themes. Delete the rest.
3. Prefer Shopify's **GitHub integration** so theme code merges instead of overwriting.
