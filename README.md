# Mining Risk Explorer

A calculator for pricing a new spodumene (lithium) mine. Enter what you know about the deposit. Every input you leave blank takes a typical value from published studies, and ten standard risk settings take their share of the value. Then move the drivers (price, capex, operating cost, recovery, grade, delay, discount rate) and watch the value change.

The engine is tested against three published feasibility studies, and it reconciles to the Tongon gold mine's spreadsheet to the cent. Those tests run under **Checks** at the foot of the page.

Everything lives in one file, `index.html`: inline CSS and JavaScript, SVG charts, no libraries and no network calls. Open it in any browser, on a phone or a laptop. It follows the system's light or dark setting. Inputs apply as you type. Your inputs, risk settings, what-ifs, deck and rate are saved in this browser only (`localStorage`), and nothing leaves the page.

## The page

One page, no tabs.

| Part | What it does |
|---|---|
| **Value bar** (stays at the top) | Owner's NPV after risks, NPV before risks, IRR, capex and first production. NPV after risks is the most you could pay at your rate, country risk included. With a what-if on, the bar shows the change against your inputs. |
| **Start from** | Loads a published study (Manna DFS, Ewoyaa DFS or Finniss DFS) or a blank new deposit. A message then offers **Undo** for ten seconds. |
| **Inputs** (left on a laptop, first on a phone) | Seven folding groups: Deposit, Mine plan, Processing, Haulage, Fiscal, Capital, Price and rate. Each shows a one-line summary when folded. A blank field uses the value shown in grey. |
| **Risks** | Ten standard risks, each a Low–Medium–High slider (left Low, middle Medium, right High), with what it costs. The amounts add up to the gap between value before and after risks. |
| **What if** | Seven sliders that each move one driver on top of your inputs. The value bar updates while a slider moves. |
| **Sensitivities** | A tornado (each driver moved on its own), a price × capex grid, and value against the whole price deck with breakeven marked. All are centred on the what-if case. |
| **Annual cash flow** | The year-by-year model, after or before risks. |
| **Data** and **Checks** (footer) | The typical values with their ranges and study pages, the other data sources and the assumptions; and the checks that test the engine. |

Explanations sit behind the small **i** buttons rather than on the page. An input's **i** gives what it means, its typical value and range, and a **Sources** link to the study pages behind it. A risk's **i** gives its plain question, what each level does and why it starts where it does.

Lithium price decks: **Forecast** (*Resources and Energy Quarterly*, Australian Department of Industry, Science and Resources, Sep 2026, real: US$2,411/t SC6 in 2026 falling to US$1,498 from 2031), **Spot** (US$2,105), **Study LT** (US$1,620, the long-term price in PLS's P2000 feasibility study) and **Downside** (US$817). A long-term price you enter replaces the deck's long-run price. The default discount rate is 8% real, the median across the studies.

## Pricing a deposit

### Inputs

| Group | Inputs | Used when you leave it blank |
|---|---|---|
| Deposit | Name; resource by category (Measured, Indicated, Inferred: Mt and % Li₂O); whether Inferred counts; mining method; underground share; strip ratio | Strip ratio 7.3 (median of 5); underground share 30% |
| Mine plan | Plan tonnes, grade and Inferred share from a study, or the share of the resource mined and dilution; ore per year; mining costs | Plan share 48% (4 studies); dilution 5.75% (4); ore per year from Taylor's rule (life ≈ 0.2 × tonnes^0.25); open pit US$3.27 per tonne moved (4); underground US$51.77 per tonne of ore (2) |
| Processing | Route (DMS only, or DMS + flotation); recovery; concentrate grade; processing cost; site G&A; by-product credit | Recovery 72.3% DMS (6) or 74.7% with flotation (3); processing US$19.85/t (4) or US$20.60/t (2); G&A US$6.16/t (4) |
| Haulage | Own plant, or truck ore to an existing plant; up to two legs to port (truck, rail, conveyor or barge: km × rate); port and loading; ocean freight; other per-tonne costs; infrastructure capex | Road US$0.137 per t-km (4); ocean freight US$25/t (2); an existing plant costs 41% of building your own (1 case) |
| Fiscal | Country or state; royalty and what it's charged on (gross revenue or FOB value); income tax; state free carry; private royalty; dividend withholding tax | Presets for Western Australia, Northern Territory, Ghana, Mali (pre-2023 terms) and Quebec (41.7% effective income and mining tax, from the Rose study), from the studies. Private royalties and withholding tax are zero unless entered. Any other country: Damodaran's corporate tax rate, and you enter the royalty. The country risk premium comes from Damodaran (Jan 2026) for all 178 countries in his table. |
| Capital | Initial capex; sustaining capex; closure; head office; receivables; years to construction; build time; ramp-up | Capex US$93.7 per tonne of annual ore capacity (6 own-plant studies, 2024 prices); sustaining US$32.9 per t of concentrate (6); closure US$17.2M (5); head office US$14.9M a year (1: Liontown); receivables 30 days of revenue (an assumption); one year to construction |
| Price and rate | Price deck; long-term price; discount to the benchmark; discount rate; ownership | Forecast deck; 8% real; price received 4.0% below SC6 (2: Liontown 6.6%, PLS 1.3%, September quarter 2026) |

Each typical value is the median of the study points in `data/lithium_typicals.json`, converted to US$ at each study's own FX assumption. Costs from studies dated before 2024 are brought to 2024 prices with US CPI-U annual averages (BLS: 2020 ×1.212, 2021 ×1.158, 2023 ×1.029); studies from 2024 on stay in their own year's dollars. CPI is a floor for mining costs, which rose faster. The own-plant capex median leaves out the Manna–Nova case, which has its own existing-plant ratio. The studies: Ewoyaa DFS (Jun 2023), Bougouni FS (Jan 2020), Shaakichiuwaanaan PEA (Aug 2024) and feasibility studies (Oct 2025, Nov 2026), Finniss Stage 1 DFS (Jul 2021) and restart study (May 2025), Rose FS (Aug 2023), Manna DFS (Dec 2025) and Manna–Nova integration study (Sep 2026), plus PLS and Liontown September 2026 quarterly actuals.

### What the calculator calculates

```
mine plan        = resource × plan share × (1 + dilution), at resource grade ÷ (1 + dilution)   [or the study's plan]
concentrate t    = ore × grade % × recovery ÷ concentrate grade %
price            = SC6 price × concentrate grade ÷ 6 × (1 − price received below the benchmark)
revenue          = concentrate × price + by-product credit
royalties        = Σ rate × (gross revenue, or FOB value = revenue − ocean freight)
mining per t ore = (1 − UG share) × open-pit cost per t moved × (1 + strip) + UG share × UG cost
site costs       = (mining + processing + G&A) per t ore, 40% fixed during a stoppage
logistics        = Σ legs (km × rate) + port, per t concentrate; ocean freight per t concentrate; other costs per t
head office      = overhead per year, from 2026 until the mine stops
working capital  = receivables (days of revenue) + inventory 30 − payables 45 (days of site costs), released at the end
capex            = input, or typical intensity × ore per year (× 41% for an existing plant), + infrastructure you must build;
                   the Funding risk adds financing costs
tax              = max(0, taxable income after losses carried forward) × rate; capex depreciated by units of production
owner's FCF      = FCF × ownership × (1 − free carry) × (1 − withholding tax) when positive; FCF × ownership when negative
pause or close   = if the cash margin (EBITDA − sustaining capex) turns negative and the price never recovers, the mine
                   closes and the rest of the ore stays in the ground; if it recovers, loss years are paused (care and
                   maintenance at the fixed 40% of site costs) and that ore is mined later. The owner takes the better path.
```

The build is spread over calendar years (`BUILD_PHASING`: 1 year 100%; 1.5 years 67/33; 2 years 40/60; 2.5 years 40/40/20; 3 years 25/45/30). Production starts when the build ends; a half-year build starts production mid-year. A slow ramp-up runs at 50% then 75% of nameplate.

Outputs: owner's NPV before and after risks, IRR, capex, first production and the annual cash flow. **NPV after risks** is the most you could pay for the project at your rate: the cash flows you expect with the risks applied, discounted at your real rate plus the country premium. It is not combined with a hurdle rate, which would count the risks twice.

### The calculator against published studies

Each study runs with its own price deck and discount rate, no risks, at 100%:

| Study | Calculator | Study | Gap | IRR: calculator vs study |
|---|---|---|---|---|
| Ewoyaa DFS (Jun 2023), Ghana | US$1,540M | US$1,498M (p4) | +2.8% | 124% vs 105% |
| Finniss DFS (Jul 2021), Northern Territory | US$133M | US$119M (A$170M × 0.70, p2) | +11.6% | 61% vs 47% |
| Manna DFS (Dec 2025), Western Australia | US$265M | US$317M (A$472.4M × 0.67, p84) | −16.2% | 22% vs 26% |

**Checks** passes each study within ±20%. The band is deliberate. The calculator uses one grade and one set of unit costs for every year. Real studies schedule higher grade early and costlier mining late (Manna mines 0.93% Li₂O early against a 0.88% average and leaves its underground ore until later), and that timing moves NPV. IRR is more sensitive still to how capex is phased. Treat the calculator as a first pass to decide whether a deposit deserves a study, not a substitute for one.

Loading a study under **Start from** makes it your project: it is priced on the deck you choose rather than the study's own, the owner-level costs its NPV leaves out (head office, working capital, price received below the benchmark) return to their typical values, and the risks apply. That is why a loaded study shows a different value from its published NPV.

### Where the risks start

| Risk | Rule (a starting assumption to calibrate) |
|---|---|
| Resource and grade | Inferred share of the plan: under 5% Low, 5–20% Medium, over 20% High |
| Recovery | Testwork: pilot plant or variability Low, bench-scale Medium, none High |
| Ground and mining | Open pit with strip ratio up to 12:1 Low; steeper, or any underground, Medium |
| Infrastructure | Concentrate travels over 800 km to port High; diesel power Medium; grid, gas or hybrid power Low |
| People and operator | Has built and run a similar mine Low; has built a mine, but not spodumene, Medium; has not built a mine High |
| Capex and schedule | Capex from a feasibility study Low, PFS Medium, scoping study High. A blank capex (the typical value) High; your own number Medium |
| Funding | Committed or in hand Low; not yet known Medium; no funding route yet High |
| Fiscal and legal | Country risk premium under 3% Low, 3–8% Medium, over 8% High (a proxy for fiscal instability). Countries with a recent state action on lithium or mining terms start at High: Zimbabwe and Namibia (export bans on raw or unprocessed ore, 2022 and 2023), Mexico (nationalisation, 2022), Chile (state control of strategic projects, 2023) and Mali (new mining code, 2023). Export bans are bigger than this risk's royalty event, so treat High as a floor. |
| Community and environment | Permits granted Low, in progress Medium, not applied for High |
| Political and security | Medium: the country premium applied once in full |

The study presets carry their testwork, power, permits, operator, capex basis and funding status. A new deposit doesn't, so a risk the inputs say nothing about starts at Medium. Move any slider to your own view; **Reset** puts them back.

Calibration evidence: Shaakichiuwaanaan's total development capex rose 44% from PEA to feasibility study (CA$1,374M to CA$1,978M) even as contingency fell from 24% to 11%, more than the Capex risk's High setting of +35%. Finniss's capex doubled and its haulage cost per tonne nearly tripled between its 2021 DFS and its 2025 restart study. Kathleen Valley recovered 60–63% during ramp-up against a 72% median in studies.

### What-ifs and sensitivities

**What if** moves one driver at a time on top of your inputs, which stay as entered:

| Slider | Range | What it moves |
|---|---|---|
| Price | −40% to +40% | Every year of the price deck |
| Capex | −50% to +50% | Initial capex, including infrastructure |
| Opex | −30% to +30% | Operating cost: mining, processing and site G&A per tonne |
| Recovery | −10 to +10 points | Lithia recovery |
| Grade | −20% to +20% | Head grade of the ore sent to the plant |
| Start delay | 0 to 4 years | Years before construction starts |
| Discount rate | −5 to +5 points | The real discount rate |

The value bar updates while a slider moves and shows the change against your inputs. **Reset what-ifs** clears them.

**Sensitivities** are centred on the what-if case:

- **Tornado:** value after risks with price ±20%, capex ±20%, opex ±20%, recovery ±5 points, grade ±10%, discount rate ±2 points and one year's delay, each on its own, longest bar first. The labels match the sliders.
- **Price × capex:** value after risks, in US$M, for price −30% to +30% and capex −20% to +50%.
- **Price curve:** value before and after risks as the whole price deck moves from −50% to +50%, with breakeven after risks marked.

## Valuation engine

The engine is a set of pure functions in section 2 of the script: `buildSchedule`, `cutLife`, `shiftSchedule`, `tierOz`, `dialParams`, `runModel`, `transactionMetrics`, `irr` and `analyse`. A product adapter (`COMMODITY`) handles gold (payable ounces) and spodumene (tonnes of concentrate), so the same engine and risks serve both. It runs annually, in real US$. Cash flows are dated 31 December and discounted from the valuation date, 1 Jan 2026, by actual days ÷ 365, the way Excel's XNPV does in the Tongon spreadsheet: NPV = Σ FCFₜ / (1+r)^tₜ, with t = 364/365 for 2026. IRR uses the same dates, like XIRR.

The deposit layer (`depositDerived`, `depositDialDefaults`, `depositEvidence`, `depositAsset`) turns the inputs, plus any what-ifs, into an asset object the engine runs like any other. Gold is no longer on the page, but the gold assets stay in the engine as references the checks run against.

For gold:

```
payable oz   = ore milled × grade ÷ 31.1034768 × recovery × payability
revenue      = payable oz × gold price
stream       = streamed oz (cumulative-ounce tiers) × price × (1 − holder's ongoing payment)
royalties    = revenue × royalty rate(s)
site costs   = unit site cost × (40% × scheduled t + 60% × milled t)      [fixed share only matters in a stoppage]
EBITDA       = revenue − stream − royalties − site costs − corporate G&A − exploration
capex        = sustaining (per t milled) + growth + development
depreciation = (opening tax base + capex) × this year's t ÷ remaining scheduled t
tax          = max(0, (EBITDA − depreciation) × tax rate)
WC           = receivables (days of revenue after stream) + inventory − payables (days of site costs); opening = year-1 level
FCF          = EBITDA − capex − tax − ΔWC − closure (final production year)
```

Owner's NPV = Σ FCFₜ × owner's shareₜ ÷ (1+r)ᵗ. Transaction NPV and IRR use the owner's FCF less the price paid: the upfront amount at t = 0 and contingent payments as scheduled.

### Tongon reconciliation (Spot, 5% real, no risks, no country premium)

The engine matches `Tongon_Mining_Model.xlsx` exactly. **Checks** compares it against the spreadsheet's Sensitivity Engine case by case:

| Case | Asset NPV (100%) | Transaction NPV | Transaction IRR |
|---|---|---|---|
| Base | US$322.44M | US$45.93M | 15.75% |
| Gold −10% / +10% | US$216.49M / US$428.08M | −US$49.10M / US$140.70M | −8.15% / 35.51% |
| Gold −20% / +20% | US$102.43M / US$533.72M | −US$151.41M / US$235.46M | n/a / 53.46% |
| Grade −10% / +10% | US$217.09M / US$427.38M | −US$48.56M / US$140.07M | −8.04% / 35.35% |
| Mine life −1 / +1 year | US$256.22M / US$379.00M | −US$13.46M / US$96.67M | 0.69% / 22.94% |
| Site cost −10% / +10% | US$386.50M / US$258.37M | US$103.40M / −US$11.53M | 27.90% / 2.08% |
| Longer hauls +US$3/t | US$290.14M | US$16.96M | 9.11% |
| Royalty +2 points | US$298.55M | US$24.51M | 10.87% |
| Stream removed | US$363.92M | US$83.14M | 23.87% |
| Closure +50% | US$305.98M | US$31.18M | 12.79% |

- Every case matches to within US$0.01M, and each IRR to within 0.01 points.
- The 20-cell grid of NPV by discount rate (5–10%) and gold case (−20% to +20%) also matches.
- So does free cash flow for each year from 2026 to 2030 (US$107.45M, 102.49M, 96.14M, 57.46M, −4.09M), and 2026 AISC of US$2,474/oz.

The brief's rounded targets (NPV ≈ US$322M, attributable ≈ US$289M, transaction NPV ≈ US$46M, IRR ≈ 16%, 2026 payable gold ≈ 126,400 oz, gold ±10% ≈ ±33%, life +1 ≈ +US$57M, life −1 ≈ −US$66M) are checked too, and all pass.

Three spreadsheet conventions the engine follows:

1. **Working-capital days** are receivables 5, payables 45 and inventory 30. Receivables use revenue after the stream; inventory and payables use site costs. Working capital comes out slightly negative and unwinds in the year after production stops.
2. **That unwind only counts inside the 2026–2030 columns.** With the 2030 extension year on, it would fall in 2031, so it isn't counted. This is part of why +1 year is worth +US$56.6M.
3. **Discounting uses XNPV and XIRR with 31 December dates.** AISC includes exploration (stream cost is a memo line).


Tropicana checks: year-1 production is 420 koz (target 400–430). Year-1 AISC is US$1,939/oz at Spot, 0.7% below the US$1,953 target, because royalties move with price. Reserve life is 4.17 years. Site cost backs out at US$60.40/t.

### Running the checks

- In the app: **Checks** in the footer. There are 60 checks:
  - the Tongon spreadsheet match: 15 cases, the 20-cell grid, FCF by year and AISC
  - the brief's Tongon targets
  - the three lithium studies, each within ±20% of its published NPV
  - the Tropicana calibration
  - your project: value after risks uses the rate that includes country risk; Funding takes value from deposits only; a loss-making mine closes rather than mining at a loss; value after risks is no more than before; value rises with the price; each year of delay costs value; each what-if moves value the right way; the price what-if matches the engine's own price lever; typical capex excludes the existing-plant case and is in 2024 prices
  - risk amounts summing to the change (within US$0.1M) for every asset
  - each asset's value ladder adding up from in-situ value to risk-adjusted value
  - 312 model runs with no NaN and no negative production
  - a risk change and a what-if move each updating the value and the sensitivities
  - a horizontal-overflow check at the current width
- Headless: `node tools/run-checks.js 375` (or `1280`). This needs Playwright and Chromium, and exits non-zero if any check fails.

## Ideas adapted from the posters

Two posters supplied ideas: *From In-Situ Value to Equity Value* and *What Drives Mining Project Value* (Ren and Patel, Nov 2026).

- **One input at a time** (poster 3.1): the tornado under Sensitivities.
- **The value bridge from in-situ value to equity value:** the engine's value ladder, from metal in the mine plan at spot through recovery, costs, capex, tax, discounting and the partners' share to value after risks. A check confirms it adds up for every asset.
- **Screening questions** (framework 1.2): the plain question behind each risk, in its **i** note.
- **Failure modes and interactions** (framework 2.2, 2.4): the slow ramp-up option (interaction 8) and the free carry that funds nothing (interaction 12).

Not brought in: the copper worked example (a different metal), the metal-flow ribbon, the full linkage matrix, stage P/NAV multiples and the in-situ yardsticks for base-metal resources.

## How the risks map to the model

Every risk enters the DCF one way: as a range on an input, a delay, an event (yearly probability × impact), or the country premium on the discount rate. Each risk is counted once. **Every level is a starting assumption to calibrate against comparable mines, not an industry statistic.**

| Risk (plain question) | Low | Medium | High | DCF line |
|---|---|---|---|---|
| Resource and grade: how sure are we about the tonnes and grade? | none | grade −5%, life −10% | grade −10%, life −25% | head grade; tonnes (the last tonnes of the schedule are removed, pro rata in the final year) |
| Recovery: will the plant get the metal out? | −1 pt | −4 pts | −12 pts | recovery |
| Ground and mining: how hard is it to mine? | none | mining cost +5% | +15%, plus a 5%/yr chance of a 2-month stoppage | mining cost; downtime |
| Infrastructure: power, water, supplies? | none | processing and site G&A +5% | +10%, plus a 2%/yr chance of a 1-month outage | processing and G&A; downtime |
| People and operator: have they done this before? | none | site costs +5% | +10% (deposits also ramp up 6 months slower) | all site costs |
| Capex and schedule (deposits only) | none | capex +15%, 6 months late | +35%, 12 months late | development capex; timing |
| Funding (deposits only): can the owner pay for the build? | none | financing costs of 10% of capex, 6 months late | 20%, 12 months late | development capex; timing |
| Fiscal and legal: will the rules change? | none | 25% chance of +2 pt royalty within 3 years | 50% chance of +2 pts and the state stake going to 30% | royalties; owner's share |
| Community and environment | none | 3%/yr chance of a 1-month blockade | 10%/yr chance of a 3-month blockade (deposits also get a 1-year permit delay) | downtime |
| Political and security | 0.5 × CRP | 1.0 × CRP | 1.5 × CRP | discount rate only, with no stoppage event as well |

- **Events.** A p%/yr chance of an n-month stoppage cuts milled tonnes, and with them production and variable costs, by p × n/12 each year. 40% of site costs are fixed and continue.
- **Amounts.** Risks are applied cumulatively in the order Resource, Recovery, Ground, Infrastructure, People, Capex, Funding, Fiscal, Community, Political. Each amount is the NPV change from adding that risk, so the amounts sum exactly to the gap between value before and after risks.

## How to add a lithium study as an example

Examples live in `const LI_EXAMPLES = [...]` in the lithium block of the script. Copy one entry, then:

1. **`d`**: the study's inputs in the same fields as the inputs on the page (`juris`, `mea`/`ind`/`inf`, `method`, `planMt`, `planGrade`, `inferredShare`, `rate`, unit costs, `recovery`, `concGrade`, `legs`, `port`, `freight`, `royalty`, `tax`, `freeCarry`, `capex`, `sustaining`, `closure`, `buildYears`, `ramp` and so on). Convert to US$ at the study's own FX.
2. **`deckOverride`**: the study's price deck, either `flat` or `byProdYear` (one price per production year).
3. **`study`**: its published post-tax NPV in US$ at 100%, IRR, discount rate and a one-line `npvText` with the page.

Add it to `PRESETS` so it appears under **Start from**. Open **Checks**: the new study joins the ±20% reconciliation automatically. If it misses, look first at grade and cost profiles by year, capex phasing and ramp-up, which the screener flattens.

To add a jurisdiction preset, add a row to `LI_JURIS` with its royalties (rate and base: `gross` or `fob`), tax rate, free carry, and the study and page it came from.

To refresh the typical values: add or edit a study file in `data/studies/`, add its points in `tools/compile_typicals.py`, run `python3 tools/compile_typicals.py` to rebuild `data/lithium_typicals.json`, then paste its `typicals` object into `const LI_TYPICALS` in `index.html`. The app makes no network calls, so it can't read the JSON at runtime.

## How to add a gold asset

Gold assets don't appear on the page. They stay in the engine as references the checks run against.

Assets live in `const ASSETS = [...]` in section 1 of the script. Copy the Tongon object (fixed schedule) or the Tropicana object (schedule built from reserves), then:

1. **Identity.** Set `id`, `name`, `stage` (`'operating'` or `'deposit'`), `ownerShare` (the NPV basis) and `stateStake`.
2. **Schedule.** Use either
   - `{ kind: 'fixed', rows: [{year, ore (Mt), grade (g/t)}], extension? }`, or
   - `{ kind: 'sources', startYear, millRate, groupCaps, sources: [{id, tonnes, grade, group?, priority}], extension? }`. The scheduler fills the mill in priority order each year, within the caps for each group (for example underground and open pit), and stops when the sources run out.
3. **Processing.** Set `{ recovery, payability }`.
4. **Costs.** Either give unit costs directly as `{ split: {mining, processing, transport, ga} (US$/t milled), corporatePerOz, explorationPerOz, sustainingPerT, growthCapex: {year: US$}, devCapex: {year: US$} }`, or use `calibrate: {...}` to back out site cost per tonne from guided AISC, as Tropicana does.
5. **Fiscal.** Set `{ royalties: [{name, rate}], taxRate, taxBase, closure, wc: {receivableDays, inventoryDays, payableDays}, wcReleaseHorizon }`. Set `wcReleaseHorizon` to `null` to always release working capital.
6. **Optional.** Add a `stream` (`{holderPayment, tiers: [{upTo, rate}]}`) and a `transaction` (`{upfront, contingentTotal, contingentPaidShare, contingentYears}`).
7. **Country premium.** Set `crp: { value }`, the premium as a fraction (Damodaran's table).
8. **Starting risk levels.** Set `dialDefaults: startAt({ resource: 'L', recovery: 'M', ... })` with a level for each risk (Funding gets Low automatically for an operating mine).
9. **Sources.** Record where each input came from in the README's assumptions list, as for Tongon and Tropicana.

## Data files

| File | What it holds |
|---|---|
| `data/studies/*.json` | One file per study, with page-cited extracts. `S05_progression.json` tracks Shaakichiuwaanaan from PEA to its two feasibility studies. |
| `data/lithium_typicals.json` | The typical values: median, range, count and every point with its study and page. Built by `tools/compile_typicals.py`. |
| `data/lithium_benchmarks.json` | PLS and Liontown September 2026 quarterly actuals, the P2000 and Kathleen Valley expansion studies, and the REQ price forecast. |
| `data/country_risk_2026.json` | Damodaran's country risk premiums (Jan and Jul 2026) and corporate tax rates for 178 countries. |

`LITHIUM_SOURCES.md` lists the documents and where each came from. `DATA_GAPS.md` lists what's missing today. `COLLECTION_LIST.md` is the prioritised list of what to gather next.

## Full assumptions list

The lithium ones also appear in the app under **Data**.

**Model-wide**
- 40% of site costs are fixed during a stoppage.
- Stoppage events are expected values: p × months ÷ 12, and events from different risks add.
- A fiscal change "within three years" is equally likely in each of years 1–3, so the expected rise ramps in at min(1, t/3). The state-stake rise uses the same timing.
- A state-stake rise is uncompensated. The owner's share falls pro rata: share × (1 − new stake) ÷ (1 − current stake).
- Sustaining capex scales with tonnes milled, so it falls during stoppages.
- Tax depreciation is units of production on scheduled tonnes, and the remainder is deducted in the final year.
- Cash flows are dated 31 December and discounted by actual days ÷ 365 from 1 Jan 2026 (the XNPV convention).
- Risk cost per unit is the owner's NPV change ÷ the owner's base-case life-of-mine output.
- Every risk level and every starting rule is an assumption to calibrate.

**Lithium deposit screener**
- One grade and one set of unit costs for every year of the plan (flat profiles). Studies schedule grade and cost by year, so expect results within about ±20% of a detailed study.
- Concentrate is priced pro rata to SC6 by its grade (SC5.5 earns 5.5/6 of the SC6 price). Studies that sell a mix of grades (Ewoyaa: SC6 and SC5.5) are entered at one grade.
- The mine plan, when not given, is the resource × the typical plan share, plus dilution at zero grade.
- Ore per year, when not given, comes from Taylor's rule: life ≈ 0.2 × (plan tonnes)^0.25.
- Capex, when not given, is the median intensity across six own-plant studies in 2024 prices (US$93.7 per tonne of annual ore capacity). The range is wide (US$71–301), and remote greenfield sites sit at the top.
- Costs from studies before 2024 are escalated to 2024 prices with US CPI-U; 2025–2026 studies stay in their own dollars.
- Price received is 4.0% below the SC6 benchmark (median of Liontown and PLS, September quarter 2026). Studies loaded as examples keep their own pricing.
- Head-office overhead is US$14.9M a year from 2026 until the mine stops (Liontown's administration and corporate costs, one figure). Examples exclude it, as their studies do.
- Working capital: receivables 30 days of revenue (an assumption); inventory 30 and payables 45 days of site costs (Tongon spreadsheet). Examples exclude it.
- The Funding risk's financing costs (10% and 20% of capex) and delays (6 and 12 months) are starting assumptions.
- A risk the inputs say nothing about starts at Medium; a blank capex (the typical value) starts the Capex risk at High.
- A mine that loses cash closes, or pauses if prices recover; care and maintenance costs the fixed 40% of site costs.
- Private royalties, withholding tax on dividends, carbon and other per-tonne costs, and stamp duty are zero unless entered.
- Using an existing plant costs 41% of building your own: one case (Manna–Nova against the Manna DFS), and that study also buys the plant at an undisclosed price.
- Capex phasing (`BUILD_PHASING`), the slow ramp-up (50% then 75%) and one year to construction when the field is blank are assumptions.
- Rail, conveyor and barge have no benchmark rate yet; a leg without a rate counts as zero, and the app says so.
- Royalty presets come from the studies: WA 5% of FOB value; NT at its 2.5% of gross floor; Ghana 5% plus a 1% levy, 35% tax and a 10% free carry; Mali at pre-2023 terms; Quebec 2% with a 41.7% effective income and mining tax rate (Rose feasibility study, p3).
- A free carry takes its share of positive cash flows and funds nothing.
- Studies are converted to US$ at their own FX assumption (Manna 0.67, Finniss 2021 0.70, Shaakichiuwaanaan 0.76 US$/CA$).
- Tax losses carry forward without limit; a study's stated opening losses are used where given (Finniss 2021: US$52.7M).

**Tropicana**
- Mill rate is 9.3 Mtpa (FY26 actual, rounded). Payability is 99.9%.
- FX is 0.70 US$/A$. Regis uses 0.72; the reserve price implies 0.66.
- The site cost split (mining / processing / transport / G&A) uses Tongon's proportions, because Tropicana's unit costs aren't public. The split only matters for the Ground and Infrastructure risks.
- Corporate G&A and exploration are zero, as they sit inside the calibrated site cost.
- Tax is 30% (the standard federal rate). The opening tax base is US$500M, closure is US$100M, and working-capital days are as for Tongon.
- Calendar 2026 is calibrated to FY27 guidance (Jul 2026–Jun 2027), and Havana growth capex (about US$47M) is placed in 2026.
- The schedule mines underground at up to 2.0 Mtpa and open pit at up to 4.3 Mtpa, with stockpiles filling the mill.
- The life-extension stepper (off by default) adds years of 2.0 Mt of underground resource at 2.4 g/t, with the rest of the mill fed at 0.5 g/t. This is resource conversion, not reserve.
- The country risk premium is 0%, as for any Aaa country.

**Tongon** (the spreadsheet calls itself "best guesses from public information, not Tongon's actual mine plan")
- Throughput of 4.0 Mtpa, the grade path from 1.20 to 1.10 g/t and recovery of 82% are estimates; none is disclosed. Payability is 99.9%.
- Site cost of US$59.50/t is back-solved from 2025 EBITDA (US$164M on US$445M revenue, per Empress Royalty).
- Corporate G&A is US$15/oz, exploration US$25/oz, sustaining capex US$7.50/t, and tax 25%. All are assumptions.
- The opening tax base is US$150M and closure is US$40M.
- Half the US$113M contingent consideration is assumed paid, evenly over 2026–2028.
- The stream agreement counts tiers from 31 Jan 2026; the model counts from 1 Jan 2026.
- The state holds at least 10%, free-carried (per Legal 500); only the Fiscal risk at High uses it.
- The country risk premium is 3.895%, Côte d'Ivoire's row in Damodaran's January 2026 file (Moody's Ba2).
- The 2030 extension year (4.0 Mt at 1.05 g/t) is off by default.

## Not built yet

- The data pack behind the typical values: more studies per input, and benchmarks for rail, conveyor and barge rates, separate port charges and infrastructure capex per kilometre.
- Calibration of the risk settings against outcomes. For a junior, the settings can take more value than market multiples imply.
- Grade and cost profiles by year.
- Other commodities (iron ore is the natural next one: haulage already takes rail legs).
- P10/P50/P90 ranges, several projects side by side, and a one-page PDF.
