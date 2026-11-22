# Data gaps

These are the gaps hit while building version 1, grouped by asset, with why each matters and where to look. Anything listed here is either flagged in the app as an assumption or keeps the asset at "data pending".

## Loulo-Gounkoto (Mali): why it has no NPV yet

The public sources reached so far are enough for the event timeline, the country premium, plant capacity, historic grade and recovery, and the old fiscal terms. They aren't enough to build a schedule or costs. This environment can't reach barrick.com, s25.q4cdn.com (Barrick's document host) or sec.gov, so the Loulo-Gounkoto figures in the app come from search-result excerpts. Check them against the documents before relying on them.

| Missing | Why it matters | Where to look |
|---|---|---|
| Ore Reserves by mine and source at 31 Dec 2025 (Yalea, Gara, Gounkoto open pit and underground, stockpiles) | Sets the schedule and mine life. Secondary sources disagree on the whole-complex reserve: 6.9 Moz @ 4.16 g/t vs 7.3 Moz @ 4.02 g/t. | Barrick 2025 reserves table; Barrick 2025 Annual Information Form |
| Ore milled, head grade and recovery, 2023–2026 | Calibrates the schedule and the Recovery dial (we have only 2022: 5.1 Mt @ 4.59 g/t, 91.2%) | Barrick quarterly "Mine Stats" PDFs |
| Site AISC for 2024 (actual) and 2026; sustaining capex by year | Lets site cost per tonne be calibrated the way Tropicana's is. We have only 2023 AISC (US$1,166/oz, secondary). | Barrick Q4 2024 MD&A; 2026 quarterly MD&A segment tables |
| Unit costs (US$/t mined, milled; G&A) | Lets the Ground, Infrastructure and People dials act on real cost lines | Loulo-Gounkoto technical report |
| Royalty, income tax and state stake after the Nov 2025 settlement | The settlement accepted the 2023 code, but its terms aren't published. The code's sliding royalty gives about 9.5% at US$4,500/oz; other outlets say 10% or 10.5%. The US$1,000–1,600 band wasn't found. | Settlement and convention texts; Decree 2024-0396; law-firm guides |
| Priority dividend on the state's free-carried 10% | Affects cash to the owner | 2023 code implementing decree; Barrick filings |
| Closure provision | Closure line | Provisions note in Barrick's 2025 financial statements; technical report |
| Settlement amount | Context only. Bloomberg/Reuters report about US$430M (244bn CFA). Ecofin reports US$253M, which matches the 144bn CFA cash tranche. | Barrick 24 Nov 2025 release; Q4 2025 MD&A (US$559M of related adjustments) |

## Tongon (Côte d'Ivoire)

| Gap | Effect in the app | Where to look |
|---|---|---|
| Throughput, head grade and recovery (the spreadsheet's estimates: 4.0 Mtpa, 1.20 → 1.10 g/t, 82%) | Drive every ounce; the Recovery default is Medium because 82% is assumed | Barrick quarterly Mine Stats and MD&As, 2019–Q3 2025, Tongon rows |
| Basis of the 620 koz reserve (100% or 89.7%) | Resource dial evidence (the plan is 1.27× the reserves left) | Barrick reserves table, 31 Dec 2024 |
| Contingent consideration terms | Half of US$113M assumed paid, evenly over 2026–2028 | Barrick 2 Dec 2025 release and 2025 annual report: price thresholds and conversion milestones |
| Stream terms | 0.5%-of-spot ongoing payment is unusually low; tiers start 31 Jan 2026 (modelled from 1 Jan) | Empress Royalty MD&A and material change report |
| Opening tax base, closure cost, sustaining capex, corporate G&A, exploration | US$150M, US$40M, US$7.50/t, US$15/oz, US$25/oz (spreadsheet assumptions) | EITI Côte d'Ivoire payment data; Tongon closure plan; Barrick Tongon sustaining capex history |
| Infrastructure and community evidence | Infrastructure default Low, Community default Medium, both without public evidence | Site visit; grid reliability data; local press; ESIA |
| Reserves beyond 2029 | Drives the Resource dial and the +1 year case | Updated reserve statement under Atlantic Group |

## Tropicana (Western Australia)

These come from the data pack's own Data gaps sheet, plus gaps the model hit.

| Gap | Effect in the app | Where to look |
|---|---|---|
| Site unit costs (mining A$/t moved, processing A$/t milled, G&A) | Site cost is back-solved from guided AISC (US$60.40/t) and split in Tongon's proportions | AngloGold 20-F or annual report cost tables; Regis annual report segment note |
| Life-of-mine plan beyond reserves | Reserve life is 4.2 years; the extension stepper is a flagged resource-conversion case | AngloGold Mineral Resource and Ore Reserve Report 2025 |
| Closure provision amount | US$100M assumed | Regis annual report rehabilitation provision (30% share) |
| Tax base of Tropicana assets | US$500M assumed | Regis annual report (30% share of PP&E) |
| Tailings facility design and capacity; water source and permits | Community and Infrastructure dial evidence only | WA DEMIRS approvals; Global Tailings Portal; AngloGold sustainability report |
| Havana Underground capex at 100% | Growth capex taken as FY27 guidance midpoint ÷ 30% (about US$47M) | Regis 9 Sep 2024 release (full table) |
| Tropicana 2025 AISC in US$ (AngloGold basis) | No cross-check on the A$ calibration; 2024 was US$1,297/oz | AngloGold 2025 Form 20-F |
| FX | 0.70 US$/A$ assumed (Regis uses 0.72; the reserve price implies 0.66) | House view |
| Cost by ore source | Average cost per tonne milled overstates costs in stockpile-only years (no mining cost there). This matters little within reserves but more for the extension case. | Unit costs by source from the operator |
| Australia's row in Damodaran's table | 0% assumed, as for any Aaa country | Damodaran Jan 2026 table |

## Model-wide

| Gap | Note |
|---|---|
| Dial calibration | Every dial level is a starting assumption. The honest calibration is base rates from comparable mines (grade reconciliation, recovery shortfalls, stoppage frequency), and those are slow to gather. |
| Country premium vintage | The brief fixes Damodaran's January 2026 table. He published a July 2026 update; switching vintages is a one-line change per asset. |
| Consensus deck after 2027 | Flat at US$4,500/oz is an assumption |
| Undeveloped deposit | Not included yet. The spec suggests Assafou, using public feasibility data only. |
