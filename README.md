# Mining Risk Explorer (version 1)

Pick a gold mine, see what it is worth, then turn nine plain-English risk dials to see what each risk takes away.

Everything lives in one file, `index.html`: inline CSS and JavaScript, SVG charts, no libraries and no network calls. Open it in any browser, on a phone or a laptop. It follows the system's light or dark setting.

| Screen | Its one job |
|---|---|
| **Pick** | One card per asset: country, stage, base NPV and risk-adjusted NPV. |
| **Value** | Base and risk-adjusted NPV side by side, transaction IRR where a price was paid, breakeven gold price, the bridge (one bar per dial), the top three risks with their diligence questions, and the annual cash flow. Tap any number to see its formula, inputs and sources. |
| **Dials** | Nine questions, each set to Low, Medium or High. Each starts at an evidence-based default with a one-line reason; evidence and sources are one tap away. Every change updates every screen. |
| **Compare** | Risk-adjusted cost curve. Bar width is year-1 output; height is AISC plus risk cost per ounce. Below it: a side-by-side table and the risk cost per ounce broken down by dial. |

The shared controls in the top bar are the price deck (Spot, Consensus or Downside) and the base real discount rate (default 5%). **Run checks** in the footer reruns the validation suite and prints the results.

## Status of the three assets

| Asset | Status | Reconciliation |
|---|---|---|
| Tongon, Côte d'Ivoire | Modelled | Matches `Tongon_Mining_Model.xlsx` to within US$0.01M: base case, all 14 sensitivity cases, the 20-cell rate × gold grid and FCF year by year |
| Tropicana, Western Australia | Modelled | Year-1 AISC calibrated to FY27 guidance |
| Loulo-Gounkoto, Mali | **Data pending** | Shows event timeline, country premium, dial defaults and evidence; no NPV. See `DATA_GAPS.md` for what's missing. |

`DATA_GAPS.md` lists what's missing today. `COLLECTION_LIST.md` is the prioritised list of what to gather next, and where, to make every number defensible.

## Valuation engine

The engine is a set of pure functions in section 2 of the script: `buildSchedule`, `cutLife`, `shiftSchedule`, `tierOz`, `dialParams`, `runModel`, `transactionMetrics`, `irr`, `breakeven` and `analyse`. It runs annually, in real US$, with flat prices. Cash flows are dated 31 December and discounted from the valuation date, 1 Jan 2026, by actual days ÷ 365, the way Excel's XNPV does in the Tongon spreadsheet: NPV = Σ FCFₜ / (1+r)^tₜ, with t = 364/365 for 2026. IRR uses the same dates, like XIRR.

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

### Tongon reconciliation (Spot, 5% real, no dials, no country premium)

The engine matches `Tongon_Mining_Model.xlsx` exactly. **Run checks** compares it against the spreadsheet's Sensitivity Engine case by case:

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

The app's breakeven is an exact solve. The spreadsheet's is a straight-line estimate from the ±10% cases (US$2,572/oz). The exact figure is higher (US$2,656/oz) because tax floors at zero in loss years. Payback on the purchase price falls in 2028 (year 3), as in the spreadsheet.

Tropicana checks: year-1 production is 420 koz (target 400–430). Year-1 AISC is US$1,939/oz at Spot, 0.7% below the US$1,953 target, because royalties move with price. Reserve life is 4.17 years. Site cost backs out at US$60.40/t.

### Running the checks

- In the app: **Run checks** in the footer. There are 37 checks:
  - the Tongon spreadsheet match: 15 cases, the 20-cell grid, FCF by year and AISC
  - the brief's Tongon targets
  - the Tropicana calibration
  - bridge bars summing to the change (within US$0.1M)
  - 120 model runs with no NaN and no negative production
  - a dial change updating all four screens
  - a horizontal-overflow check at the current width
- Headless: `node tools/run-checks.js`. This needs Playwright and Chromium, and exits non-zero if any check fails.

## How the dials map to the model

Every risk enters the DCF one way: as a range on an input, a delay, an event (yearly probability × impact), or the country premium on the discount rate. Each risk is counted once. **Every level is a starting assumption to calibrate against comparable mines, not an industry statistic.**

| Dial (plain question) | Low | Medium | High | DCF line |
|---|---|---|---|---|
| Resource and grade: how sure are we about the ounces? | none | grade −5%, life −10% | grade −10%, life −25% | head grade; tonnes (the last tonnes of the schedule are removed, pro rata in the final year) |
| Recovery: will the plant get the gold out? | −1 pt | −4 pts | −12 pts | recovery |
| Ground and mining: how hard is it to mine? | none | mining cost +5% | +15%, plus a 5%/yr chance of a 2-month stoppage | mining cost; downtime |
| Infrastructure: power, water, supplies? | none | processing and site G&A +5% | +10%, plus a 2%/yr chance of a 1-month outage | processing and G&A; downtime |
| People and operator: have they done this before? | none | site costs +5% | +10% (deposits also ramp up 6 months slower) | all site costs |
| Capex and schedule (deposits only) | none | capex +15%, 6 months late | +35%, 12 months late | development capex; timing |
| Fiscal and legal: will the rules change? | none | 25% chance of +2 pt royalty within 3 years | 50% chance of +2 pts and the state stake going to 30% | royalties; owner's share |
| Community and environment | none | 3%/yr chance of a 1-month blockade | 10%/yr chance of a 3-month blockade (deposits also get a 1-year permit delay) | downtime |
| Political and security | 0.5 × CRP | 1.0 × CRP | 1.5 × CRP | discount rate only, with no stoppage event as well |

- **Events.** A p%/yr chance of an n-month stoppage cuts milled tonnes, and with them production and variable costs, by p × n/12 each year. 40% of site costs are fixed and continue.
- **Bridge.** Dials are applied cumulatively in the order Resource, Recovery, Ground, Infrastructure, People, Capex, Fiscal, Community, Political. Each bar is the NPV change from adding that dial, so the bars sum exactly to risk-adjusted minus base.
- **Risk cost per ounce** on the cost curve = (base − risk-adjusted owner's NPV) ÷ the owner's share of base-case life-of-mine payable ounces.

## How to add an asset

Assets live in `const ASSETS = [...]` in section 1 of the script. Copy the Tongon object (fixed schedule) or the Tropicana object (schedule built from reserves), then:

1. **Identity.** Set `id`, `name`, `country`, `region`, `stage` (`'operating'` or `'deposit'`), `metal`, `method`, `owners`, `ownerShare` (the NPV basis), `ownerLabel` and `stateStake`.
2. **Schedule.** Use either
   - `{ kind: 'fixed', rows: [{year, ore (Mt), grade (g/t)}], extension? }`, or
   - `{ kind: 'sources', startYear, millRate, groupCaps, sources: [{id, tonnes, grade, group?, priority}], extension? }`. The scheduler fills the mill in priority order each year, within the caps for each group (for example underground and open pit), and stops when the sources run out.
3. **Processing.** Set `{ recovery, payability }`.
4. **Costs.** Either give unit costs directly as `{ split: {mining, processing, transport, ga} (US$/t milled), corporatePerOz, explorationPerOz, sustainingPerT, growthCapex: {year: US$}, devCapex: {year: US$} }`, or use `calibrate: {...}` to back out site cost per tonne from guided AISC, as Tropicana does. For a deposit, put the build cost in `devCapex`; the Capex dial scales it, and the delay dials shift production.
5. **Fiscal.** Set `{ royalties: [{name, rate}], taxRate, taxBase, closure, wc: {receivableDays, inventoryDays, payableDays}, wcReleaseHorizon }`. Set `wcReleaseHorizon` to `null` to always release working capital.
6. **Optional.** Add a `stream` (`{holderPayment, tiers: [{upTo, rate}]}`) and a `transaction` (`{upfront, contingentTotal, contingentPaidShare, contingentYears}`).
7. **Country premium.** Set `crp: { value, label, source, url, flag, note }`.
8. **Dial defaults.** Set `dialDefaults`: for each of the nine dial ids, `{ level, reason, sources: [keys of S], question }`. The `question` is the diligence question shown in the top-three risks.
9. **Evidence and events.** Fill `evidence: [{label, value, unit, source, url, flag, note?, input?, dial?}]`. Use `input: true` for model inputs (these appear in the traces) and `dial: 'id'` for evidence shown under that dial. Fill `events: [{date, text, source, url}]` for the timeline. Add new source records to `S` and spread them in with `...S.KEY`.
10. **Missing data.** If key inputs are missing, set `dataStatus: 'pending'`, add a `pendingNote` and a `gaps` list, and leave out `schedule`, `costs` and `fiscal`. The asset then shows its timeline, premium and dial defaults, with no NPV.

Flags: `sourced` means taken directly from a document, `derived` means computed from sourced figures (say how in `note`), and `assumption` means judgement (say why).

Then open the app and press **Run checks**. The NaN and negative-production sweep covers every modelled asset automatically.

## Full assumptions list

These also appear in the app under **Assumptions list**.

**Model-wide**
- 40% of site costs are fixed during a stoppage.
- Stoppage events are expected values: p × months ÷ 12, and events from different dials add.
- A fiscal change "within three years" is equally likely in each of years 1–3, so the expected rise ramps in at min(1, t/3). The state-stake rise uses the same timing.
- A state-stake rise is uncompensated. The owner's share falls pro rata: share × (1 − new stake) ÷ (1 − current stake).
- Sustaining capex scales with tonnes milled, so it falls during stoppages.
- Tax depreciation is units of production on scheduled tonnes, and the remainder is deducted in the final year.
- Cash flows are dated 31 December and discounted by actual days ÷ 365 from 1 Jan 2026 (the XNPV convention).
- Working-capital days are receivables 5 (on revenue after the stream), inventory 30 and payables 45 (on site costs). The balance is released in the year after production ends, if that year is inside the asset's model horizon.
- AISC = (site costs + royalties + sustaining capex + corporate G&A + exploration) ÷ payable oz. It excludes streams, growth capex and closure.
- Risk cost per ounce is the owner's NPV change ÷ the owner's base-case life-of-mine ounces.
- The Consensus deck is flat at US$4,500/oz from 2028 onwards (Goldman Sachs gives 2026 and 2027). The Downside deck of US$3,000 flat is set in the brief.
- Every dial level is a starting assumption to calibrate.

**Tropicana**
- Mill rate is 9.3 Mtpa (FY26 actual, rounded). Payability is 99.9%.
- FX is 0.70 US$/A$. Regis uses 0.72; the reserve price implies 0.66.
- The site cost split (mining / processing / transport / G&A) uses Tongon's proportions, because Tropicana's unit costs aren't public. The split only matters for the Ground and Infrastructure dials.
- Corporate G&A and exploration are zero, as they sit inside the calibrated site cost.
- Tax is 30% (the standard federal rate). The opening tax base is US$500M, closure is US$100M, and working-capital days are as above.
- Calendar 2026 is calibrated to FY27 guidance (Jul 2026–Jun 2027), and Havana growth capex (about US$47M) is placed in 2026.
- The schedule mines underground at up to 2.0 Mtpa and open pit at up to 4.3 Mtpa, with stockpiles filling the mill. Both mining rates are FY26 actuals grossed up to 100%.
- The life-extension stepper (off by default) adds years of 2.0 Mt of underground resource at 2.4 g/t, with the rest of the mill fed at 0.5 g/t. This is resource conversion, not reserve.
- The country risk premium is 0%, as for any Aaa country. The data pack asks for Australia's row to be confirmed.

**Tongon** (the spreadsheet calls itself "best guesses from public information, not Tongon's actual mine plan")
- Throughput of 4.0 Mtpa, the grade path from 1.20 to 1.10 g/t and recovery of 82% are estimates; none is disclosed. Throughput is set so the model matches 2025 output of about 125,600 oz. Payability is 99.9%.
- Site cost of US$59.50/t is back-solved from 2025 EBITDA (US$164M on US$445M revenue, per Empress Royalty). The split between mining, processing, transport and G&A is an estimate.
- Corporate G&A is US$15/oz, exploration US$25/oz, sustaining capex US$7.50/t, and tax 25% (the standard rate). All are assumptions.
- The opening tax base is US$150M and closure is US$40M. Closure wasn't found in public sources.
- Half the US$113M contingent consideration is assumed paid, evenly over 2026–2028.
- The stream agreement counts tiers from 31 Jan 2026; the model counts from 1 Jan 2026.
- The state holds at least 10%, free-carried (per Legal 500); it's modelled as 10%, and only the Fiscal dial at High uses it.
- The country risk premium is 3.90%, the Ba2 level in Damodaran's January 2026 table, because Côte d'Ivoire's own row couldn't be read. It is Ba2-rated (Moody's, affirmed Mar 2026).
- The Infrastructure default is Low with no evidence either way, and the Community default is Medium with no public evidence. Both are flagged for diligence.
- The 2030 extension year (4.0 Mt at 1.05 g/t) is off by default. When it's on, the working-capital release falls outside the 2030 horizon.

## Not built in version 1

- From the spec's "Should" list:
  - The undeveloped deposit. The engine already handles deposits: development capex, the capex dial, and delays for permits, ramp-up and the build.
  - Preset scenarios.
  - The one-page PDF. The published page can't open a print dialog.
- From the "Could" list: P10/P50/P90 ranges, CDS survival factors, the structuring view, and other commodities.
