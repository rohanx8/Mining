# Data gaps

These are the gaps hit while building the app, with why each matters and where to look. Anything listed here is either flagged in the app as an assumption or keeps an asset at "data pending".

## Lithium deposit screener

| Gap | Effect in the app | Where to look |
|---|---|---|
| Rail, conveyor and barge rates per tonne-km | No benchmark. A leg without a rate counts as zero, and the app says so. Only road haulage has a typical value (US$0.137/t-km, 4 studies). | Shaakichiuwaanaan feasibility studies (road to Matagami, then rail; CA$217–302/t combined); published rail tariffs in WA and Quebec; iron-ore and coal haulage studies |
| Port charges separate from haulage | Studies often fold them into the haul rate (Manna: US$58/t for haulage and port combined), so the port field has no typical value | Port tariff schedules: Port Hedland, Esperance, Geraldton, Darwin East Arm, Takoradi, Quebec ports |
| Infrastructure capex per km of road, rail or power line | Must be entered by hand in the Haulage step | Studies that build access roads or power lines (Rose, Shaakichiuwaanaan, Ewoyaa); public road-building cost benchmarks |
| Fiscal terms beyond the five presets | Presets cover WA, NT, Ghana, Mali (pre-2023 terms) and Quebec. Elsewhere, tax is Damodaran's corporate rate and you enter the royalty. | EY *Global Mining and Metals Tax Guide*, country chapters (use the extraction prompt; the full guide is 2,147 pages) |
| Quebec mining tax | Not modelled. Rose reports a 41.7% effective tax rate including it; the preset uses the 26.14% corporate rate, so Quebec values are too high. | Quebec Mining Tax Act; Rose FS tax section; EY guide, Canada chapter |
| Mali's 2023 mining code | The Mali preset uses the 2020 Bougouni terms (3% + 0.5% royalties, 3% ISCP, 25% tax), which the 2023 code replaced with higher royalties and state stakes | The 2023 code and decrees; recent Goulamina or Bougouni filings; EY guide, Mali chapter |
| Grade and cost profiles by year | The screener uses one grade and one cost set for every year, which explains most of the ±20% gap against studies (Manna −16%: its study mines 0.93% Li₂O early against a 0.88% average) | Year-by-year schedules in DFS appendices |
| Ewoyaa's product mix | Entered as SC6 at 62.1% recovery; the study sells SC6 and SC5.5 (67.2% recovery to SC5.5) | Ewoyaa DFS product split by year |
| Thin typical values | Several medians rest on few points: underground mining (2), flotation processing (2), ocean freight (2), existing-plant capex ratio (1) | More studies: Goulamina (Mali), Mt Holland, Bald Hill, Grota do Cirilo (Brazil), Whabouchi (Quebec), Arcadia (Zimbabwe). Kathleen Valley (`data/studies/S01.json`) is filed but not yet in the medians. |
| Deposit dial calibration | The dial rules (Inferred share, testwork, strip ratio, haul distance, operator, capex basis, country premium, permits) are judgement | Study-to-outcome comparisons: Shaakichiuwaanaan PEA to FS (in the app), Finniss 2021 DFS to 2025 restart (in the app), Kathleen Valley ramp-up recovery (in the app); add Mt Cattlin, Bald Hill and Pilgangoora stage 1 |
| Price decks | The forecast is one source (*Resources and Energy Quarterly*, Australian Department of Industry, Science and Resources, Sep 2026) and spot is a single print | Long-term price assumptions in recent studies; company guidance; public bank forecasts |
| Capex phasing, ramp-up and years to construction | Assumptions (`BUILD_PHASING`, 50%/75% slow ramp-up, 0/1/2 years from permit status) | Construction schedules and ramp-up curves in the studies and in quarterly reports of recent starts |

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

Closed: Australia's row in Damodaran's January 2026 table is confirmed at 0% (Moody's Aaa; `data/country_risk_2026.json`).

## Model-wide

| Gap | Note |
|---|---|
| Dial calibration | Every dial level is a starting assumption. The honest calibration is base rates from comparable mines (grade reconciliation, recovery shortfalls, stoppage frequency, capex overruns), and those are slow to gather. |
| Country premium vintage | The app uses Damodaran's January 2026 table, as the brief fixed. The July 2026 update is in `data/country_risk_2026.json` too; switching deposits to it is a one-line change (`cr[2]` to `cr[3]` in `depositDerived`). |
| Consensus gold deck after 2027 | Flat at US$4,500/oz is an assumption |
| Funding risk for deposits | No dial yet for whether the owner can raise the capex, or at what dilution |
