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
| Tongon, Côte d'Ivoire | Modelled | Matches every Tongon spreadsheet target (table below) |
| Tropicana, Western Australia | Modelled | Year-1 AISC calibrated to FY27 guidance |
| Loulo-Gounkoto, Mali | **Data pending** | Shows event timeline, country premium, dial defaults and evidence; no NPV. See `DATA_GAPS.md` for what's missing. |

## Valuation engine

The engine is a set of pure functions in section 2 of the script: `buildSchedule`, `cutLife`, `shiftSchedule`, `tierOz`, `dialParams`, `runModel`, `transactionMetrics`, `irr`, `breakeven` and `analyse`. It runs annually, in real US$, with flat prices. The valuation date is 1 Jan 2026 and cash flows are discounted from the end of each year: NPV = Σ FCFₜ / (1+r)ᵗ, with t = 1 for 2026.

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
WC           = receivables (days of net revenue) + inventory − payables (days of site costs); opening = year-1 level
FCF          = EBITDA − capex − tax − ΔWC − closure (final production year)
```

Owner's NPV = Σ FCFₜ × owner's shareₜ ÷ (1+r)ᵗ. Transaction NPV and IRR use the owner's FCF less the price paid: the upfront amount at t = 0 and contingent payments as scheduled.

### Tongon reconciliation (Spot, 5% real, no dials, no country premium)

| Target from the spreadsheet | Model | Result |
|---|---|---|
| Asset NPV (100%) ≈ US$322M | US$321.98M | pass |
| Attributable NPV ≈ US$289M | US$288.82M | pass |
| Transaction NPV ≈ US$46M | US$45.53M | pass (the target is stated to the nearest US$1M; this is 1.0% off) |
| Transaction IRR ≈ 16% | 15.67% | pass |
| 2026 payable gold ≈ 126,400 oz | 126,419 oz | pass |
| 2026 FCF ≈ US$107.5M | US$107.45M | pass |
| Gold ±10% → NPV ≈ ±33% | +32.8% / −32.9% | pass |
| Mine life +1 year ≈ +US$57M | +US$56.9M | pass |
| Mine life −1 year ≈ −US$66M | −US$66.2M | pass |

The spreadsheet itself was not supplied, so the engine was rebuilt from the brief. Two readings were needed to match it:

1. **Working-capital days.** The brief gives them as "5 / 45 / 30". Reading that as receivables 5, payables 45 and inventory 30 makes working capital slightly negative, and it reproduces every target. Reading inventory as 45 and payables as 30 gives an NPV of US$325.6M, which is outside the 1% tolerance.
2. **Working-capital release.** The balance unwinds in the year after production ends, but only if that year falls inside the model horizon (2026–2030 for Tongon). With the 2030 extension year switched on, the release would fall in 2031, so it isn't counted. This is what makes the +1 year case come out at +US$57M. It looks like a horizon artifact in the spreadsheet; the app flags it.

Tropicana checks: year-1 production is 420 koz (target 400–430). Year-1 AISC is US$1,939/oz at Spot, 0.7% below the US$1,953 target, because royalties move with price. Reserve life is 4.17 years. Site cost backs out at US$60.40/t.

### Running the checks

- In the app: **Run checks** in the footer. It covers the Tongon targets, the Tropicana calibration, that bridge bars sum to the change (within US$0.1M), 120 model runs with no NaN and no negative production, a test that a dial change updates all four screens, and a horizontal-overflow check at the current width.
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
- Working-capital days are receivables 5 (on net revenue), inventory 30 and payables 45 (on site costs). The balance is released in the year after production ends, if that year is inside the asset's model horizon.
- AISC = (site costs + royalties + sustaining capex + corporate G&A) ÷ payable oz. It excludes exploration, streams, growth capex and closure.
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

**Tongon**
- Recovery of 82% is assumed in the spreadsheet; actual recovery isn't disclosed. Payability is 99.9%.
- The opening tax base is US$150M and closure is US$40M (spreadsheet assumptions). Working-capital days use the reading above.
- The state holds 10% today. This isn't in the source files; it's Côte d'Ivoire's usual free carry, and only the Fiscal dial at High uses it.
- The country risk premium is 3.90%, the Ba2 level in Damodaran's January 2026 table, because Côte d'Ivoire's own row couldn't be read. It is Ba2-rated (Moody's, affirmed Mar 2026).
- The Infrastructure default is Low with no evidence either way, and the Community default is Medium with no public evidence. Both are flagged for diligence.
- The 2030 extension year (4.0 Mt at 1.05 g/t) is off by default. When it's on, the working-capital release falls outside the 2030 horizon.

## Not built in version 1

- From the spec's "Should" list:
  - The undeveloped deposit. The engine already handles deposits: development capex, the capex dial, and delays for permits, ramp-up and the build.
  - Preset scenarios.
  - The one-page PDF. The published page can't open a print dialog.
- From the "Could" list: P10/P50/P90 ranges, CDS survival factors, the structuring view, and other commodities.
