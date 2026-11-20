# The House Playbook: SEO · AEO · GEO
**Oh Betty Jaletti / Maison Betty Jaletti** · ohbettyjaletti.com
Written 2026-11-20 · Review every 8 weeks (next: 2027-01-15)

This is the standing reference. Weekly audits in `audits/` check the store *against this file*.
Confidence is marked on every claim: **[primary]** vendor-independent or platform documentation ·
**[directional]** consistent across several vendor sources, unverified · **[house]** our own decision, not an external rule.

---

## Part 0 — The one-sentence version

> The house already writes beautifully and has built the right assets. What is costing it attention
> is that **the same fact is stated differently in four places**, and that **nothing it writes
> points at anything it sells**. Fix consistency and the bridge, and the existing work starts earning.

---

## Part 1 — Who we are capturing, and in whose voice

Everything below is downstream of this. Get the audience wrong and perfect schema sells nothing.

### 1.1 The reader

Not "women 25–45 who like candles." The house is for **people who do things the long way on purpose**:
who make the coffee themselves because they have the cup for it, highlight in ink without apology,
and buy the bouquet for a Tuesday.

Three things follow from that, and they drive every SEO decision:

| What is true of her | What it means for search |
|---|---|
| She is **researching a feeling**, not a product category | She searches *"how to make a reading nook"*, not *"buy book cover"*. Capture at the feeling stage. |
| She is **suspicious of marketing** and fluent in it | Keyword-stuffed copy reads as cheap and loses her. The voice *is* the conversion mechanism. |
| She **wants permission**, not persuasion | Content that says "this is a legitimate way to live" outperforms content that says "buy this". |

**[house]** She does not arrive ready to buy. She arrives ready to be understood. The commercial
ask comes second, and quietly — but it must actually *come*. See Part 7.

### 1.2 The three search moods

Write for the mood, not the keyword.

1. **The permission search** — *slow living, is slow living just aesthetic, romanticising my life*
   She wants to know the way she wants to live is real. → Essays. Our strongest existing asset.
2. **The making search** — *reading nook ideas small apartment, best lamp for reading at night*
   She is assembling something. → Guides with specifics. **This is where product belongs.**
3. **The verification search** — *what does numbered edition mean, are limited editions worth it, is [brand] legit*
   She is about to spend money and is checking. → Plain, unflinching answers. Trust content.

Our 15 letters map almost exactly onto these three. That was good instinct. The gap is mood 2→purchase.

### 1.3 The voice, as a set of rules

The house voice is an **asset**, not an obstacle to optimisation. Rules:

- **Never** sacrifice a sentence to a keyword. If a phrase cannot be said in the house voice, it is not our phrase.
- The house uses its own words (*your parcel*, *between editions*, *an edition*). Keep them on the
  storefront **and translate them for machines** in `llms.txt` — which it already does, correctly.
- Specifics *are* the voice. "18.89″ long, folds flat to under an inch" is more Betty than "generously sized".
  This matters enormously: specifics are also exactly what AI engines extract. **The voice and AEO want the same thing.**
- Answer-first is not a voice compromise. *"The short answer"* blocks in the letters prove it: the
  direct answer lands first, then the house talks. Keep that pattern.
- One thing the voice must never do: **be vague about money, dates, or availability.** Mystery about an
  edition is charming. Mystery about whether a thing is in stock is a lost sale and a downranked product.

---

## Part 2 — What changed by late 2026

### 2.1 The settled part

**[primary]** Google's own 2026 guidance frames optimising for its generative features as *still SEO* —
it describes "AEO" and "GEO" as terms "you may see used," and says no special markup is required for AI
features. There is no separate AI ranking lever to pull. Clear structure, accurate data, useful content.

**[primary]** Structured data is not an eligibility condition for AI answers, but Product markup still
drives **merchant listing** eligibility and lets Google cross-check the page against a feed.
`shippingDetails` and `hasMerchantReturnPolicy` are *recommended* and act as verification, not gates.
Sources disagree on whether their absence suppresses rich treatment; treat them as worth having, not as emergencies.

**[primary]** Declare the return policy **once**, as `MerchantReturnPolicy` under `Organization`/`OnlineStore`.
Product-level policy markup is for exceptions only (our fragrance rule is a genuine exception). Do not
duplicate identical policy markup across every product.

### 2.2 The real shift: from ranking to being quoted

**[directional]** The unit of visibility is no longer a blue link, it is a **citation inside someone
else's answer**. Practical consequences:

- **Answer the question in the first ~200 words**, and write headers as the questions people actually ask.
  Reported as one of the highest-return changes available. Our letters already do this.
- **Fact density wins.** Citations, figures, named specifics raise the odds of being quoted. One widely
  repeated study claims up to +40% visibility for lower-ranked sites from this alone — **unverified,
  treat as directional**, but the direction is consistent everywhere.
- **Consistency is a ranking input now.** Models cross-check a claim across sources. When a brand's own
  surfaces disagree about its own price, a model has no reliable fact to quote and tends to use someone
  else's. **This is our single biggest live problem — see Part 3.**
- **Treat each engine as its own environment.** ChatGPT, Google AI Mode and Perplexity use different
  retrieval and different source selection. There is no one ranking to hold.

### 2.3 Where product discovery actually happens now

**[directional]** Google **AI Mode** shopping reads the **Shopping Graph**, fed by Merchant Center with
**free listings enabled** — not by on-page markup alone. Price, stock, shipping and returns should agree
across feed, markup and the visible page; conflicts reportedly cause deprioritisation. Merchant Center has
added *conversational attributes* for AI surfaces via a supplemental feed.
**→ We are on Basic with no Merchant Center feed. This is our largest untapped channel.**

**[directional]** **ChatGPT**: OpenAI stepped back from in-chat Instant Checkout in March 2026 and now
concentrates on **discovery**. Shopify stores reach it through **Shopify Catalog** — no separate feed,
no enrolment; purchases return to our own checkout. The control is in admin under
**Sales channels → Agentic → ChatGPT**. **→ Verify ours is on. Nearly free distribution.**

**[primary]** Our storefront already serves the new agentic layer: `robots.txt` advertises
`/agents.md` and a **UCP** profile at `/.well-known/ucp` with an MCP endpoint at `/api/ucp/mcp`
(UCP versions through 2026-08-25), plus a `sitemap_agentic_discovery.xml`. Shopify gave us this for free.
Our job is only to make sure **what those endpoints say is true**.

### 2.4 Settled questions — stop spending time here

**[primary]** **`llms.txt` does not drive citations.** Adoption is 6–10% of top sites, and **97% of the
files received zero AI-bot requests** in May 2026; one test logged 84 fetches out of 62,100+ AI bot
visits. Google says it will not affect visibility either way. A 10-site test saw 2 sites improve and 8 unchanged.
→ **But keep ours.** Not for citations: it is read by **coding agents and MCP integrations**, and for us
it doubles as `/agents.md`, which Shopify's own `robots.txt` points agents to. It is our agent contract,
not an SEO file. Its value is entirely in **being accurate**.

**[primary]** **FAQ rich results are gone** for most sites. Keep Q&A as *visible content* — it works for
AEO — but do not expect SERP decoration from `FAQPage`.

**[directional]** Rank-tracking an AI answer is not a strategy. Track **citation rate** and **AI referral
traffic**, not AI "position".

---

## Part 3 — The One-Fact Rule (the house's most important rule)

> **Every fact about a piece exists in exactly one authoritative place. Everywhere else points at it.**

A fact about this store currently lives in up to six surfaces:

1. Shopify product/variant fields · 2. Product JSON-LD on the page · 3. Visible page copy
4. Collection & product SEO fields · 5. `llms.txt` / `agents.md` · 6. Policy pages

**[house] The hierarchy, in order of authority:**

| Rank | Surface | Authoritative for |
|---|---|---|
| 1 | Shopify variant data (price, inventory, policy) | price · availability · SKU — **always wins** |
| 2 | Shopify policy pages (`/policies/*`) | shipping rates, windows, returns, destinations |
| 3 | Product metafields (`custom.materials`, `fit_dimensions`, `care`…) | specs, dimensions, care |
| 4 | Visible page copy | the story |
| 5 | `llms.txt` / `agents.md` | brand facts, vocabulary, what exists — **never prices** |

**Rules that follow:**

- **`llms.txt` must not restate a price, a stock state, or a ship window.** It should name the piece and
  point at `/products/{handle}.json`. Every hardcoded number in that file is a future contradiction.
  (It currently hardcodes prices, and two of the three are wrong.)
- **A new published product is not live until it appears in `llms.txt`.** Add it to the publish checklist.
- **Shipping and returns are stated once**, in the policy, and quoted from there.
- **Any number appearing in two places gets a note** saying which one is the source.

**Why this is the top priority:** fancy schema on a product whose price disagrees with the brand's own
agent file is worse than no schema. It teaches every engine that our data is unreliable.

---

## Part 4 — SEO layer

**What it is for us:** being findable for the *making* and *verification* searches, and not wasting
crawl on ourselves.

### Non-negotiables
1. **The homepage title must describe what is actually for sale.** It is the single highest-value string
   on the site. If the catalogue changes edition, the homepage changes with it — same week.
2. **Titles ≤ ~60 characters**, keyword-bearing part first, `| Oh Betty Jaletti` last.
   Em dashes render as `—` and eat width; prefer a comma or a pipe in SEO fields.
3. **One URL per idea.** No published draft twins, no two pages answering the same question.
4. **Thin pages are a cluster problem, not a page problem.** Fourteen ~250-word pages behind one hub
   dilute the hub. Either give each real substance or fold them into the hub.
5. **Every published page is in a cluster** with a hub and internal links both ways. Orphans don't rank.
6. **Collections carry SEO fields** — including `frontpage`.

### The cluster map **[house]**
```
/pages/slow-living  (hub: permission)      → 5 letters → In Her Purse
/pages/the-reading-nook  (hub: making)     → 5 letters → The Reading Hour
/pages/numbered-editions  (hub: verify)    → 5 letters → both editions
/pages/the-worktable  (hub: what's coming)  → 14 worktable pages → waitlist
```
Each hub links down to its letters; each letter links up to its hub **and across to one product**. Part 7.

---

## Part 5 — AEO layer

**What it is for us:** being the source that gets read aloud when someone asks a question we have
already answered better than anyone.

### The letter format (keep doing this)
Our letters are genuinely strong. The pattern, made explicit so it is repeatable:

1. **Question-shaped title.** *"What Does a Numbered Edition Mean?"* — matches the spoken query.
2. **`The short answer`** block, first screen, 2–3 sentences, complete enough to be quoted standalone.
3. **H2s that are themselves questions**, in the order a person would ask them.
4. **A "what this does *not* mean" section.** Rare, trusted, highly quotable. We already do it. Keep it.
5. **Specifics with numbers.** `12/200`, `2B pencil`, `18.89″`.
6. **Visible author and date** — and a **last-reviewed date** when we revisit.

### What is missing from it
- **No `Article`/`BlogPosting` JSON-LD on any letter.** The date is visible text only; no machine-readable
  author or `dateModified`. Cheap to add, and it is how a date and a byline become a trust signal.
- **One letter breaks the pattern** (`reading-nook-essentials` opens narratively, no short-answer block).
- **All 15 are dated July 14, 2026.** Four months old and all identical — reads as a content dump.
  Stagger `dateModified` as we genuinely revisit them.

### Rules
- **[house]** Anything a customer emails twice becomes a published answer within two weeks.
- The returns policy is already near-perfect AEO: *"The short version: thirty days from the day it
  arrives."* That is the register to write policy in. **[house]**
- Do not add `FAQPage` markup expecting rich results **[primary]**; write the Q&A visibly instead.

---

## Part 6 — GEO layer

**What it is for us:** when a shopping agent assembles an answer, our pieces are present, correctly
priced, and purchasable.

### 6.1 Product markup — current vs target

Live markup gives us `Product`, `Offer`, `Brand`, `BreadcrumbList`, `sku`, `price`, `priceCurrency`,
`itemCondition`, `availability`. That is a decent base. Target adds:

| Field | Why | Priority |
|---|---|---|
| `hasMerchantReturnPolicy` at **Organization** level | Merchant listing verification; declare once, not per product **[primary]** | High |
| `shippingDetails` | Same. Our rates are flat and simple, so this is easy | High |
| `brand` correctness | **Must be the house on house pieces.** A third-party vendor name in the `vendor` field becomes the `brand` in schema and splits our entity | Critical |
| `gtin`/`mpn` | Feed matching. Use `mpn` = our SKU where there is no barcode | Medium |
| `image` (4+, absolute URLs) | Nothing is eligible without images **[primary]** | Critical |
| `availability` honesty | See 6.2 | Critical |
| `aggregateRating`/`review` | Only once genuinely earned. Never fabricated | Post-launch |

### 6.2 Availability must be true **[house]**

`inventoryPolicy: CONTINUE` on every active variant means we sell past zero. With negative stock,
`availability: InStock` is a claim we cannot keep. Options, in order of preference:

1. Keep real inventory and let `InStock` be true. Best.
2. If selling ahead deliberately, present it as **`BackOrder` or `PreOrder` with a stated ship window**
   on the listing. Honest, and preorder-as-scarcity fits the house perfectly.
3. What we must not do: `InStock` on a piece we cannot ship this week. It is the fastest way to lose
   both a customer and a feed.

### 6.3 Entity consistency
- `Organization` schema should carry `sameAs` (every social profile), `email`, and `address`/`areaServed`.
  We have `name`, `alternateName`, `logo`, `foundingDate`, `description` — **`sameAs` is the notable gap**,
  and it is the main way an engine confirms two names are one business.
- `alternateName: "Maison Betty Jaletti"` is the correct way to carry the dual name. **Keep it.**
  The two-name question is *solved* — as long as `vendor` is never a third party.
- `Organization.description` must list what is currently buyable. It goes stale on every launch.

### 6.4 The agentic layer
- Shopify already serves `/agents.md`, `/.well-known/ucp`, `/api/ucp/mcp`, `sitemap_agentic_discovery.xml`.
  **Do not block them, do not try to improve them.** Just keep the data behind them true.
- `robots.txt` is Shopify's default and permissive: `User-agent: *  Allow: /` with no AI-crawler blocks.
  GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot and Google-Extended are all **allowed**.
  **[house] Decision: keep it that way.** A house that wants to be found by people taking the long way
  cannot afford to be invisible to the tool they ask. Revisit only if scraping becomes a real cost.
- **Merchant Center with free listings** is the one genuinely missing channel **[directional]**. It is
  the entry to Google AI Mode shopping and it is free. Biggest single unlock available to us.
- **Verify Sales channels → Agentic → ChatGPT is enabled.** Zero-effort distribution **[directional]**.

---

## Part 7 — The attention bridge (how capture becomes a sale)

**This is the part that is currently missing entirely, and it is the one the audience question turns on.**

Fifteen letters, three guide hubs, strong voice, answer-first structure — and **zero links to a product
across every letter checked.** The house is capturing exactly the attention it set out to capture and then
letting it leave. All the SEO and GEO work in this document is worth less than fixing this.

### The rule **[house]**
> Every letter ends with **one** object. Not a grid, not a "shop all" — one piece, named, with a sentence
> about why *that* piece belongs to *that* idea, and a link.

One, because a grid is a catalogue and reads as an ad; one object, chosen, reads as a recommendation —
which is the house voice, and converts better from this audience.

### The mapping
| Letter cluster | The one object | The sentence it earns |
|---|---|---|
| Reading nook / lighting / side table | The Chaperone *(when published)* | the thing the nook is *for* |
| Evening reading habit / rituals under an hour | One More Chapter *(when published)* | the hour, made an occasion |
| Slow living / vs minimalism / small budget | A Woman Remembered | the small thing that marks a day |
| Numbered editions / verifying / collecting | In Her Purse collection | the house's own numbering, shown |
| Autumn & winter slow living | The Out-the-Door Gloves | cold mornings, named |

Where the honest match is an unpublished piece, **link the waitlist instead** and say plainly what is
coming. That is the house's whole model, and a waitlist signup from a letter is a better outcome than a bounce.

### Also missing
- **Hub pages do not link down to their letters**, so the clusters are not clusters yet.
- **The letters do not link to each other.** Five slow-living letters that never mention one another.
- **No email capture inside the letters** — a reader at the end of a 1,000-word essay is the warmest
  reader on the site, and Klaviyo is already connected.

---

## Part 8 — Measuring it

Track these; ignore everything else.

| Metric | Where | Target |
|---|---|---|
| **AI referral sessions** (chatgpt.com, perplexity.ai, gemini, copilot) | Shopify analytics / GA referrers | Establish baseline, then grow |
| **Citation presence** — ask the 15 letter questions in ChatGPT / AI Mode / Perplexity monthly, log whether we are cited | Manual, 20 min/month | Up quarterly |
| **Letter → product click-through** | Shopify analytics on letter pages | >3% once Part 7 ships |
| **Impressions & position** for the three clusters | Search Console | Up quarterly |
| Merchant listing / feed errors | Merchant Center, once live | Zero |
| Consistency check — the W47 contradiction list | Weekly audit | Zero |

**[directional]** Do not track "AI rank". Track whether we are quoted, and whether being quoted sends anyone.

---

## Part 9 — What not to chase

- **`llms.txt` as an SEO tactic.** Settled: it does not move citations **[primary]**. Keep ours as the agent
  contract, keep it accurate, spend no optimisation effort on it.
- **`FAQPage` markup for rich results.** Deprecated for most sites **[primary]**.
- **Vendor stat quoting.** "AI traffic +393%", "+40% from fact density" — directional at best. Measure ours.
- **Keyword density, meta keywords, exact-match stuffing.** Actively harmful to this voice.
- **AI-written letters.** The voice is the moat. It is the reason this audience stays.
- **Blocking AI crawlers** while asking to be found in AI answers.
- **Chasing head terms** like "tote bag". We lose those. We win *"what does a numbered edition mean"*.

---

## Part 10 — The weekly ten minutes

Run before anything else. Any **no** is a finding.

1. Does the homepage title name something actually for sale?
2. Do Shopify price, page price, and `llms.txt` agree on every published piece? *(`llms.txt` should state no prices at all.)*
3. Is every published product in `llms.txt` / `agents.md`?
4. Does `availability` in schema match what we can actually ship?
5. Is `brand` in every Product schema the house?
6. Do shipping rates, windows and destinations match the policy page everywhere they appear?
7. Any published duplicate or draft-twin pages?
8. Does every letter published this week link to one object and one hub?
9. Does `Organization.description` list what is buyable today?
10. Any new empty or thin published page?

---

## Appendix — Sources

See `research/research-db.json` (r001–r012). Confidence marks in this document follow that file's
`reliability` field. Where sources conflict, both positions are stated rather than resolved.
