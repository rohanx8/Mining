# Mining Risk Explorer

A calculator for a rough deal price on a mining project: lithium (spodumene), gold or copper concentrate. It is built for small-cap funds, private equity and investment banks. Enter what you know about the deposit and the company. Blank inputs take a typical value from published studies where the studies give one; ten standard risk settings take their share of the value. A football field then sets the DCF beside what listed peers trade at, what takeovers paid and what deals paid per unit of resource. Move the drivers (price, capex, operating cost, recovery, grade, delay, discount rate) and watch the value change.

The engine is tested against three published feasibility studies, and it reconciles to the Tongon gold mine's spreadsheet to the cent. Those tests run under **Checks** at the foot of the page.

Everything lives in one file, `index.html`: inline CSS and JavaScript, SVG charts, no libraries and no network calls. Open it in any browser, on a phone or a laptop. It follows the system's light or dark setting. Inputs apply as you type. Your inputs, risk settings, what-ifs, deck and rate are saved in this browser only (`localStorage`), and nothing leaves the page.

## The page

One page, no tabs.

| Part | What it does |
|---|---|
| **Value bar** (stays at the top) | Owner's NPV after risks, NPV before risks, IRR and the breakeven price after risks. NPV after risks is the most you could pay at your rate, country risk included. With a scenario on, the bar shows the change against your inputs. |
| **Start from** | Loads a published study (Manna DFS, Ewoyaa DFS or Finniss DFS) or a blank new deposit, priced today: a study dated 2024 or earlier comes with its costs at November 2025 prices, and Ewoyaa takes Ghana's current royalty and free carry. A message says so and offers **Undo** for ten seconds. |
| **Inputs** (left on a laptop, first on a phone) | Eight folding groups: Deposit (with the commodity), Mine plan, Processing, Haulage and sales, Fiscal, Capital, Price and rate, Company and deal. Each shows a one-line summary when folded. A blank field uses the value shown in grey; a box that says *enter* has no typical value and needs your figure. |
| **Key numbers** | Output, mine life, C1 (gold: cash cost) and AISC, breakeven price after risks, payback year, value ÷ capex, and the resource with value per unit of it, in each commodity's units (lithium: kt and LCE, US$/t; gold: koz, US$/oz, Moz; copper: kt of payable copper, US$/lb, Mt Cu). **Download** saves an Excel workbook with live formulas, a one-page PDF memo or a CSV. |
| **Deal price** | Equity value after and before risks, the funding gap and a fully funded value per share, market cap, price ÷ value, EV per unit of resource, and a football field of methods with the market cap marked. |
| **Risks** | Ten standard risks, each a slider from Low (left) through Medium to High (right) in quarter steps, nine positions in all. In bold next to each title: the figure it gives this project now (for example capex US$368M, 9 mo late). At the slider ends: the figure at Low and at High. On the right: what it takes. The amounts add up to the gap between value before and after risks. |
| **Scenarios** | Seven sliders that each move one driver on top of your inputs. In bold next to each title: the figure the model uses now (the long-term price, the capex, and so on). At the slider ends: the figure at each end of its range. On the right: what that move is worth. The value bar updates while a slider moves. |
| **Sensitivities** | The eight inputs that move value most when each moves ±10% on its own, as a tornado, centred on the scenario case. **Full view** opens every input, any one sensitivity across its range, and price × capex, each with a table. Every risk and scenario row has a chart button that opens its own chart and table. |
| **Annual cash flow** | The year-by-year model, after or before risks. |
| **Data** and **Checks** (footer) | The typical values with their ranges and study pages, the other data sources and the assumptions; and the checks that test the engine. |

Explanations sit behind the small **i** buttons rather than on the page. An input's **i** gives what it means, its typical value and range, and a **Sources** link to the study pages behind it. A risk's **i** gives its plain question, what each level does and why it starts where it does.

Gold decks: **Forecast** (REQ Sep 2026, Table 9.1, real: US$4,613/oz in 2026 falling to US$3,760 from 2031), **Spot** (US$3,700), **Consensus** and **Downside** (US$3,000). Copper decks: **Forecast** (REQ Sep 2026, Table 11.1, p106, real LME: US$6.11/lb in 2026 falling to US$5.26 from 2031), **Long term** (US$5.26) and **Downside** (US$4.58, the 2025 average). Default discount rates follow industry norms: 8% real for lithium and base metals, 5% for gold (KPMG, 2014, as cited in *What Drives Mining Project Value*); the lithium studies' median is also 8%.

Lithium price decks: **Forecast** (*Resources and Energy Quarterly*, Australian Department of Industry, Science and Resources, Sep 2026, real: US$2,411/t SC6 in 2026 falling to US$1,498 from 2031), **Spot** (US$2,105), **Study LT** (US$1,620, the long-term price in PLS's P2000 feasibility study) and **Downside** (US$817). A long-term price you enter replaces the deck's long-run price. The default discount rate is 8% real, the median across the studies.

## Pricing a deposit

### Inputs

| Group | Inputs | Used when you leave it blank |
|---|---|---|
| Deposit | Name; resource by category (Measured, Indicated, Inferred: Mt and % Li₂O); whether Inferred counts; mining method; underground share; strip ratio | Strip ratio 7.3 (median of 5); underground share 30% |
| Mine plan | Plan tonnes, grade and Inferred share from a study, or the share of the resource mined and dilution; ore per year; mining costs | Plan share 48% (4 studies); dilution 5.75% (4); ore per year from Taylor's rule (life ≈ 0.2 × tonnes^0.25); open pit US$3.38 per tonne moved (4); underground US$51.77 per tonne of ore (2) |
| Processing | Route (DMS only, or DMS + flotation); recovery; concentrate grade; processing cost; site G&A; by-product credit | Recovery 72.3% DMS (6) or 74.7% with flotation (3); processing US$19.85/t (4) or US$21.28/t (2); G&A US$6.25/t (4) |
| Haulage | Own plant, or truck ore to an existing plant; up to two legs to port (truck, rail, conveyor or barge: km × rate); port and loading; ocean freight; other per-tonne costs; infrastructure capex | Road US$0.137 per t-km (4); ocean freight US$25/t (2); an existing plant costs 41% of building your own (1 case) |
| Fiscal | Country or state; royalty and what it's charged on (gross revenue or FOB value); income tax; state free carry; private royalty; dividend withholding tax | Presets for Western Australia, Northern Territory, Ghana (the 2025 royalty that slides with the SC6 price, and the 13% free carry in the ratified Ewoyaa lease), Mali (pre-2023 terms) and Quebec (41.7% effective income and mining tax, from the Rose study). Private royalties and withholding tax are zero unless entered. Any other country: Damodaran's corporate tax rate, and you enter the royalty. The country risk premium comes from Damodaran (Jan 2026) for all 178 countries in his table. |
| Capital | Initial capex; sustaining capex; closure; head office; receivables; years to construction; build time; ramp-up | Capex US$95.0 per tonne of annual ore capacity (6 own-plant studies, November 2025 prices); sustaining US$33.9 per t of concentrate (6); closure US$17.8M (5); head office US$14.9M a year (1: Liontown); receivables 30 days of revenue (an assumption); one year to construction |
| Price and rate | Price deck; long-term price; discount to the benchmark; discount rate; ownership | Forecast deck; 8% real; price received 4.0% below SC6 (2: Liontown 6.6%, PLS 1.3%, September quarter 2026) |

Each typical value is the median of the study points in `data/lithium_typicals.json`, converted to US$ at each study's own FX assumption. Costs from studies dated 2024 or earlier are brought to November 2025 prices, just before the 1 January 2026 valuation date, with US CPI-U: each study year's BLS annual average to the November 2025 index, 324.122 (2020 ×1.252, 2021 ×1.196, 2023 ×1.064, 2024 ×1.033). Studies from 2025 on stay in their own dollars. A study loaded as your project gets the same factors; prices, ocean freight, by-product credits and tax losses are not escalated. CPI is a floor for mining costs, which rose faster. The own-plant capex median leaves out the Manna–Nova case, which has its own existing-plant ratio. The studies: Ewoyaa DFS (Jun 2023), Bougouni FS (Jan 2020), Shaakichiuwaanaan PEA (Aug 2024) and feasibility studies (Oct 2025, Nov 2026), Finniss Stage 1 DFS (Jul 2021) and restart study (May 2025), Rose FS (Aug 2023), Manna DFS (Dec 2025) and Manna–Nova integration study (Sep 2026), plus PLS and Liontown September 2026 quarterly actuals.

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

Between the three stated settings, each slider has three more steps. A step blends the two settings either side in a straight line: Capex halfway from Medium to High is +25% and 9 months late. For a chance of an event, the chance blends and the size of the event stays (Fiscal halfway from Medium to High is a 37.5% chance of a two-point royalty rise), so the expected effect is a straight line too. Nothing beyond the stated Low, Medium and High settings is invented; to go further, use the what-if sliders.

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

In bold next to each title is the figure the model uses now: the long-term SC6 price, the capex, opex per tonne of ore, the recovery, the grade, the year construction starts and the discount rate. The slider ends show the figure at each end of its range, and the right-hand column what that one move is worth. The value bar updates while a slider moves and shows the change against your inputs. **Reset** clears them.

**Sensitivities** are centred on the what-if case. The panel shows the eight inputs that move value after risks most when each moves 10% down and up on its own (one more year to construction counts as one), biggest first.

**A chart and a table for every sensitivity.** The chart button on each risk and what-if row, and the **Full view** button on the Sensitivities panel, open a full-size view (full screen on a phone) with three tabs:

- **Every input:** each of about 20 inputs moved down and up by 10%, 20% or 50% on its own, from the current case, plus one more year to construction. A tornado ranks them, and a table gives each input's figure now and after the move, the value after risks at each, and the swing. Inputs that are zero for this project are left out. Click an input's name for its own chart.
- **One at a time:** pick any of the seven what-ifs, the inputs or the ten risks. A chart shows value after risks (and before risks, where it differs) across that driver's whole range, with the current setting and the breakeven marked, and the x-axis in the driver's own figures. The table gives each step's setting, its figure, the value before and after risks and the change from now.
- **Price × capex:** a 7 × 7 grid, with the long-term price and the capex under each move.

### Key numbers and the download

Output and unit costs are as planned, before risks; breakeven, payback and value per tonne are after risks.

| Number | How it is worked out |
|---|---|
| Output | Concentrate a year at full rate, and its lithium carbonate equivalent: Li₂O × 2.473 (molar masses) |
| Mine life | Plan tonnes ÷ ore per year |
| C1 | Mining, processing, site G&A, haulage to the ship and other per-tonne costs, less by-product credits, per tonne of concentrate over the life of mine, free on board |
| AISC | C1 plus royalties, sustaining capex and head office |
| Breakeven price | The flat SC6 price (real) at which value after risks is zero, found by bisection on the engine |
| Payback | The first production year in which the owner's cumulative cash after risks, undiscounted, turns positive |
| Value ÷ capex | NPV after risks ÷ initial capex, both at the owner's share |
| Resource | Resource tonnes × grade × 2.473, in Mt LCE (100%), and NPV after risks per tonne of the owner's share |

**Download CSV** saves one file: the results, the key numbers, the price deck and rates, each risk's setting, figure and value taken, the what-ifs, the inputs used (with the what-ifs) and the annual cash flow, after or before risks as the table shows. Inside claude.ai the viewer confirms the save; a copy opened on its own downloads directly.

## Deal price, for funds, private equity and banks

The **Deal price** panel turns the project value into a company value and a rough price.

- **Equity value** = NPV (owner's share, after head office and capex) + cash − debt + other assets, all from **Company and deal** (share price, shares, cash, debt and other assets in A$, C$, £ or US$; exchange rates from the RBA, 26 Nov 2026, the Bank of Canada, 10 Nov 2026, and the market, 25 Nov 2026).
- **Fully funded value per share**: the funding gap (capex less cash) is raised as debt (50% when blank, an assumption) and new shares issued 10% below the price (an assumption); the value spreads over the new share count.
- **Price ÷ value** before and after risks, and **EV per unit of resource** (t LCE, oz, lb Cu).

The football field shows each method's low, mid and high:

| Method | How |
|---|---|
| DCF after risks | Your settings; price ±10% and the discount rate ±1 point |
| DCF, funded buyer | The same with People and Funding at Low: a buyer that runs and pays for the build |
| Trading peers | Listed developers' EV ÷ attributable study NPV (25th to 75th percentile), applied to the published study NPV |
| Takeovers | Prices paid ÷ the target's study NPV, applied the same way |
| Stage multiple | *What Drives Mining Project Value*, section 1.1 note 5: scoping 0.10–0.25×, PFS 0.25–0.50×, FS 0.50–0.85×, in construction 0.80–1.0× study NPV (analytical judgement, not a measured sample) |
| Deals per resource | Prices paid per unit of resource, times your resource |

The shaded band runs from the median low to the median high of the methods. Multiples apply to the **published study NPV** (an input; without it, to value before risks).

**Market data** (`data/research/`, curated in the app's `MARKET` table): five DFS/FS lithium developers traded at 0.01–0.15× study NPV in late November 2026 (median 0.03×); the two lithium takeovers agreed in 2026 paid 0.32× and 0.34× (Titan for Global Lithium, Huayou for Atlantic Lithium); five copper developers traded at 0.05–0.30× (median 0.11×) and three copper takeovers paid 0.04–0.38×; five gold developers traded at 0.12–0.39× (median 0.22×), and one gold takeover offer paid about 0.75× (OceanaGold for Ausgold). These came through web-search results, because page fetches were blocked in the build environment; they have not been checked page by page against the filings.

### Calibration: who owns the project

The risk settings were tested against these prices. As the listed owner stands (a team that has not built a mine, no funding yet), the Manna DFS keeps 8% of its value after risks, close to where lithium developers trade (median 0.03–0.06× study NPV). For a funded, experienced buyer (People and Funding at Low) it keeps 63%, close to the roughly 70% that Titan's offer for Global Lithium implies against the same value before risks. So the settings stand, and **Valued for** (Company and deal) switches between the two views. Ewoyaa as a buyer keeps 31%, below what Huayou's offer implies (about 66%): Ghana's 9.7% country risk premium in full, plus a High Fiscal start, is harsher than that buyer was; with Political at Low and Fiscal at Medium it keeps 52%.

## Gold and copper

The same engine values gold (payable ounces from grade, recovery and payability, less refining and transport per ounce) and copper concentrate (payable pounds priced net of the treatment charge per dry tonne and the refining charge per pound; haulage and freight per wet tonne). Key numbers, the deal price, the exports and the sensitivities follow the commodity's units.

Typical values are thin. They come from public study announcements, gathered through web search (`data/research/`, compiled by `tools/compile_typicals_au_cu.py` into `data/gold_typicals.json` and `data/copper_typicals.json`): gold recovery 90.9% (4 studies), mill processing US$13.4/t (2), site G&A US$5.6/t (2), capex US$138 per tonne of yearly capacity (2), strip 2.4 (3); copper recovery 86% (3), concentrate grade 25% Cu (3), payability 96.5% (1), capex US$61 per tonne of yearly capacity (3). Figures stated only in A$ or C$ were left out, because the studies' exchange rates were not found.

Gold fiscal presets: Western Australia (2.5% of royalty value, tax 30%), New South Wales (4% of ex-mine value, tax 30%), Ghana (L.I. 2517: 5% up to US$1,900/oz rising to 12% above US$4,500, the 1% Growth and Sustainability Levy, tax 35%, state free carry 10%) and Côte d'Ivoire (ad valorem 5–8% by gold price, 0.5% local development contribution; tax is Damodaran's rate and the free carry must be entered). **Mining taxes on profit.** The engine also charges taxes on mining profit (EBITDA less tax depreciation), each year, deducted for income tax: flat, in slices of the profit margin, or British Columbia's two-stage tax. Presets for gold and copper: Ontario (10% of mining profit, income tax 26.5%), Quebec (16% of profit up to a 35% margin, 22% to 50%, 28% above; income tax 26.5%), British Columbia (2% of net current proceeds until capital is recovered, then 13% of net revenue, with the 2% credited; income tax 27%) and Nevada (net proceeds tax 5% once net proceeds pass US$4M a year, NRS 362.140, plus the 1.1% gold and silver excise tax on gold; federal tax 21%). Exemptions, minimum taxes and loss carry-forward for the mining tax are not modelled. Anywhere else, enter a flat rate under Fiscal. Chile and Peru (margin-banded royalties) and WA and NSW copper wait for the official rate tables. All of these came through web search and have not been checked against the legislation. Inputs with no typical value (gold: mining costs, payability, refining, sustaining; copper: mining and processing costs, G&A, moisture, TC/RC, freight, closure) say *enter*, and the page lists them until you do.

## Data behind this round

- `data/research/`: the raw research, one JSON file per question (lithium, gold and copper developers' market data; gold and copper studies and unit costs; fiscal terms; discount-rate norms, deals and decks). Every value carries the URL and quote a web search returned, marked `"via": "search"`.
- `data/gold_typicals.json`, `data/copper_typicals.json`: built from it by `tools/compile_typicals_au_cu.py` and embedded in the page by `tools/embed_typicals_au_cu.py`.

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

- In the app: **Checks** in the footer. The two gold mines are test cases only: the engine must rebuild their spreadsheet and published figures before it values a project. There are 72 checks:
  - the Tongon spreadsheet match: 15 cases, the 20-cell grid, FCF by year and AISC
  - the brief's Tongon targets
  - the three lithium studies, each within ±20% of its published NPV
  - the Tropicana calibration
  - your project: value after risks uses the rate that includes country risk; Funding takes value from deposits only; a loss-making mine closes rather than mining at a loss; value after risks is no more than before; value rises with the price; each year of delay costs value; each what-if moves value the right way; the price what-if matches the engine's own price lever; each risk takes more value as its slider moves from Low to High; a whole step gives exactly the stated setting; a step between settings blends them in a straight line; every input in the full-size view moves value the right way; typical capex excludes the existing-plant case and is escalated to the valuation date
  - gold ounces and copper pounds from tonnes, grade, recovery and payability; copper priced net of TC/RC; a funded buyer's DCF at least the DCF as set; the quartiles behind the market multiples; Quebec's margin slices; a mining tax on profit lowering value and income tax; British Columbia's 2% until capital is recovered
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

Every risk enters the DCF one way: as a range on an input, a delay, an event (yearly probability × impact), or the country premium on the discount rate. Each risk is counted once. The table gives the three stated settings; the slider steps between them blend the two settings either side (see Where the risks start). **Every level is a starting assumption to calibrate against comparable mines, not an industry statistic.**

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
- Capex, when not given, is the median intensity across six own-plant studies at November 2025 prices (US$95.0 per tonne of annual ore capacity). The range is wide (US$73–311), and remote greenfield sites sit at the top.
- Costs from studies dated 2024 or earlier are escalated to November 2025 prices with US CPI-U; 2025–2026 studies stay in their own dollars. A study loaded as your project is escalated the same way.
- Price received is 4.0% below the SC6 benchmark (median of Liontown and PLS, September quarter 2026). Studies loaded as examples keep their own pricing.
- Head-office overhead is US$14.9M a year from 2026 until the mine stops (Liontown's administration and corporate costs, one figure). Examples exclude it, as their studies do.
- Working capital: receivables 30 days of revenue (an assumption); inventory 30 and payables 45 days of site costs (Tongon spreadsheet). Examples exclude it.
- The Funding risk's financing costs (10% and 20% of capex) and delays (6 and 12 months) are starting assumptions.
- A risk the inputs say nothing about starts at Medium; a blank capex (the typical value) starts the Capex risk at High.
- A mine that loses cash closes, or pauses if prices recover; care and maintenance costs the fixed 40% of site costs.
- Private royalties, withholding tax on dividends, and carbon and other per-tonne costs are zero unless entered. Stamp duty, deal costs and the price of buying the project are not modelled: the value is before them.
- Using an existing plant costs 41% of building your own: one case (Manna–Nova against the Manna DFS), and that study also buys the plant at an undisclosed price.
- Capex phasing (`BUILD_PHASING`), the slow ramp-up (50% then 75%) and one year to construction when the field is blank are assumptions.
- Rail, conveyor and barge have no benchmark rate yet; a leg without a rate counts as zero, and the app says so.
- Royalty presets come from the studies: WA 5% of FOB value; NT at its 2.5% of gross floor; Ghana's government royalty slides with the SC6 price under the Minerals and Mining (Royalty) Regulations, 2025 (5% up to US$1,500/t, 7% above, 12% above US$3,200/t; the band from US$2,501 to 3,200 is not confirmed, so 7% is used), plus the 1% Growth and Sustainability levy, 35% tax and the 13% free carry in the Ewoyaa lease ratified in March 2026. The Ewoyaa example keeps its study's 5%, third-party 1%, levy and 10% carry, so it can be checked against the DFS; loaded as your project it takes today's terms; Mali at pre-2023 terms; Quebec 2% with a 41.7% effective income and mining tax rate (Rose feasibility study, p3).
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
- Calibration against outcomes (grade reconciliation, recovery shortfalls, overruns), beyond the market check above.
- Market data checked against the filings, more of it (gold trading multiples especially), and dated snapshots.
- Gold and copper unit costs from the technical reports, and fiscal presets for the main gold and copper jurisdictions.
- Grade and cost profiles by year.
- Other commodities (iron ore is the natural next one: haulage already takes rail legs).
- P10/P50/P90 ranges, several projects side by side, and a one-page PDF.
