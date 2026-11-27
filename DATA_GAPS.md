# Data gaps

These are the gaps hit while building the app, with why each matters and where to look. Tongon and Tropicana are no longer on the page; they stay in the engine as test cases, so their gaps matter only for those checks. Loulo-Gounkoto, which never had enough public data for an NPV, has been removed.

## Deal price and market data

| Gap | Effect in the app | Where to look |
|---|---|---|
| Market data checked page by page | Trading multiples, takeover multiples, share prices and cash came through web-search results in Nov 2026 (`data/research/`): page fetches were blocked by the build environment's network policy. Each value carries the URL and quote the search returned, but not a page read | The filings and quote pages themselves (ASX, SEDAR+, LSE RNS, company sites); widen the environment's network access or upload the PDFs and rerun |
| Gold trading multiples | Five developers (Troilus, Astral, First Mining, Saturn, Turaco), with prices dated late Oct to late Nov 2026 and Saturn's undated; NPV bases differ (Saturn's tax basis and Astral's rate not stated); one takeover (OceanaGold for Ausgold, about 0.75× NPV) | Dated quotes and the studies' NPV statements; Rox, Toubani and Mayfair, which lacked an NPV or a price |
| Thin samples | Lithium trading 5, lithium takeovers 2, lithium deals per t LCE 2, copper trading 5, copper takeovers 3, copper deals per lb 2 | More developers and deals, dated snapshots each quarter |
| Stage multiples | Analytical judgement from *What Drives Mining Project Value*, not a measured sample | A measured P/NAV-by-stage sample from the market data above |
| Funding assumptions | Debt 50% of the funding gap and new shares 10% below the price, when blank | Recent developer financings: debt share, equity discounts, streams and offtake prepayments |
| Exchange rates | A$ (RBA, 26 Nov 2026), C$ (Bank of Canada, 10 Nov 2026), £ (market, 25 Nov 2026) | Update with the deal date |

## Gold and copper

| Gap | Effect in the app | Where to look |
|---|---|---|
| Unit operating costs | Gold: only one study (Diamba Sud) gave mining, processing and G&A; copper: one underground mining cost (Copperwood). Inputs with no typical value say *enter* | The operating-cost tables in the technical reports (NI 43-101 section 21) and ASX study announcements |
| Product terms | No typical value for gold payability and refining, or copper TC/RC, moisture and freight | Offtake and smelter terms in the studies; annual TC/RC benchmarks |
| A$ and C$ figures | Left out of the medians: the studies' exchange rates were not found | The studies' stated FX assumptions |
| Fiscal presets | Gold: WA, NSW, Ghana and Côte d'Ivoire only (Côte d'Ivoire without its free carry); copper: none. Elsewhere tax is Damodaran's rate and you enter the royalty | Royalty acts and revenue offices; the EY mining tax guide; WA and NSW copper rates (WA Mining (Royalties) Regulations 2025, Schedule 1); Queensland's reference prices |
| Profit-based mining taxes | Modelled for Ontario, Quebec, British Columbia and Nevada (README). Not modelled: Ontario's new-mine and remote-mine exemptions, Quebec's minimum mining tax, loss carry-forward for the mining tax. Chile (1% ad valorem plus a margin component of 8–26%, under a 46.5% cap) and Peru (royalty 1–12% and special mining tax 2–8.4%, both by operating margin) have no preset: only the end points of their tables were found | Law 21.591 (Chile); Ley 29788 and 29789 with their margin tables (Peru); Revenu Québec's minimum-tax rates |
| Study examples | No gold or copper study to start from | One complete study per commodity, with its cost tables |

## Lithium calculator

| Gap | Effect in the app | Where to look |
|---|---|---|
| Rail, conveyor and barge rates per tonne-km | No benchmark. A leg without a rate counts as zero, and the app says so. Only road haulage has a typical value (US$0.137/t-km, 4 studies). | Shaakichiuwaanaan feasibility studies (road to Matagami, then rail; CA$217–302/t combined); published rail tariffs in WA and Quebec; iron-ore and coal haulage studies |
| Port charges separate from haulage | Studies often fold them into the haul rate (Manna: US$58/t for haulage and port combined), so the port field has no typical value | Port tariff schedules: Port Hedland, Esperance, Geraldton, Darwin East Arm, Takoradi, Quebec ports |
| Infrastructure capex per km of road, rail or power line | Must be entered by hand in the Haulage step | Studies that build access roads or power lines (Rose, Shaakichiuwaanaan, Ewoyaa); public road-building cost benchmarks |
| Fiscal terms beyond the five presets | Presets cover WA, NT, Ghana, Mali (pre-2023 terms) and Quebec. Elsewhere, tax is Damodaran's corporate rate and you enter the royalty. | EY *Global Mining and Metals Tax Guide*, country chapters (use the extraction prompt; the full guide is 2,147 pages) |
| Quebec mining tax | Modelled as an effective rate: the Quebec preset uses the 41.7% income-and-mining-tax rate Rose reports (p3), not the progressive mining tax itself | Quebec Mining Tax Act; the Rose FS tax section; EY guide, Canada chapter |
| Ghana's 2025 royalty bands | The preset uses L.I. 2517 as WTS Global and TaxLawGH summarise it: 5% to US$1,500/t SC6, 7% to US$2,500, 10% to US$3,000, 12% above. Reports of the ratified Ewoyaa lease put the 12% band above US$3,200. From search results, not the gazetted text | The Minerals and Mining (Royalty) Regulations, 2025 as gazetted; the ratified Ewoyaa lease; Atlantic Lithium's ASX releases |
| Mali's 2023 mining code | The Mali preset uses the 2020 Bougouni terms (3% + 0.5% royalties, 3% ISCP, 25% tax), which the 2023 code replaced with higher royalties and state stakes | The 2023 code and decrees; recent Goulamina or Bougouni filings; EY guide, Mali chapter |
| Grade and cost profiles by year | The screener uses one grade and one cost set for every year, which explains most of the ±20% gap against studies (Manna −16%: its study mines 0.93% Li₂O early against a 0.88% average) | Year-by-year schedules in DFS appendices |
| Ewoyaa's product mix | Entered as SC6 at 62.1% recovery; the study sells SC6 and SC5.5 (67.2% recovery to SC5.5) | Ewoyaa DFS product split by year |
| Thin typical values | Several medians rest on few points: underground mining (2), flotation processing (2), ocean freight (2), existing-plant capex ratio (1) | More studies: Goulamina (Mali), Mt Holland, Bald Hill, Grota do Cirilo (Brazil), Whabouchi (Quebec), Arcadia (Zimbabwe). Kathleen Valley (`data/studies/S01.json`) is filed but not yet in the medians. |
| Deposit dial calibration | The dial rules (Inferred share, testwork, strip ratio, haul distance, operator, capex basis, country premium, permits) are judgement | Study-to-outcome comparisons: Shaakichiuwaanaan PEA to FS (in the app), Finniss 2021 DFS to 2025 restart (in the app), Kathleen Valley ramp-up recovery (in the app); add Mt Cattlin, Bald Hill and Pilgangoora stage 1 |
| Price decks | The forecast is one source (*Resources and Energy Quarterly*, Australian Department of Industry, Science and Resources, Sep 2026) and spot is a single print | Long-term price assumptions in recent studies; company guidance; public bank forecasts |
| Capex phasing, ramp-up and years to construction | Assumptions (`BUILD_PHASING`, 50%/75% slow ramp-up, 0/1/2 years from permit status) | Construction schedules and ramp-up curves in the studies and in quarterly reports of recent starts |
| Head-office overhead | One figure (Liontown, US$14.9M a year); a junior holding one project spends less, a multi-asset producer more. It costs a small deposit a lot of value | Appendix 5B item 1.2(e) for five to ten ASX lithium developers and producers |
| Price received below the benchmark | Two points (Liontown 6.6%, PLS 1.3%, one quarter each); partly timing | Realised against benchmark prices for more producers and more quarters (Mineral Resources, IGO, Sigma, Rio Tinto's lithium unit) |
| Working-capital days | Receivables of 30 days are an assumption; inventory and payables come from the Tongon spreadsheet | Payment terms in offtake agreements; working-capital lines in study cash flows |
| Cost escalation | US CPI-U from each study year's annual average to the November 2025 index (324.122), the last before the valuation date; studies loaded as your project get the same factors. CPI understates mining-cost inflation: Finniss capex doubled from 2021 to 2025 | A mining or construction cost index (for example a mine-cost or EPC index) to replace CPI for capex and opex |
| Funding dial | Financing costs of 10% and 20% of capex and delays of 6 and 12 months are judgement | Financing terms of recent lithium builds: debt fees and rates, cost-overrun facilities, equity raised and its discount |
| Withholding tax, stamp duty, private royalties | Withholding tax and private royalties are zero unless entered; stamp duty and deal costs are not modelled at all, so the value is before them | EY guide country chapters; state duty schedules (for example WA landholder duty); tenement royalty registers |
| C1 and AISC against the studies | The key numbers come from the model's flat cost set and are not yet checked against the C1 or AISC each study reports | The cost summary tables of the Manna, Ewoyaa and Finniss studies |
| State actions on lithium | From news reports; primary sources not yet attached | Government gazettes and statements: Zimbabwe (Dec 2022), Namibia (Jun 2023), Mexico (Apr 2022), Chile (Apr 2023), Mali (Aug 2023) |
| Care-and-maintenance cost | Uses the 40% fixed share of site costs as a proxy | Care-and-maintenance costs reported by paused lithium operations (Finniss and others, 2024) |
| Dials against market multiples | Tested (README, Calibration): as the listed owner stands, values sit near where developers trade; for a funded buyer, near what 2026 takeovers paid. Country risk in full looks harsher than a strategic buyer in Ghana was | More takeovers with their targets' NPVs, especially in high-risk countries |

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
