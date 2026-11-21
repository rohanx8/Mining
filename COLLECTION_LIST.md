# What to collect next

These are things to gather from the internet (and Stanford's library) to make Mining Risk Explorer more robust and easier to defend. They are grouped by what each one unblocks, most important first. Every item says **where** to find it, **what** to capture, and **which number in the app it defends**.

Everything here is free or available through Stanford's library. Skip anything that needs a paid subscription you don't have; the app should never depend on paywalled data.

## How to capture each data point

Use one row per number, with the same fields the app stores. That way each row drops straight into `ASSETS` as an evidence item.

| Field | Example |
|---|---|
| Asset | Tongon |
| Label | Ore processed, 2024 |
| Value and unit | 4.1 Mt |
| Basis | 100% or attributable (say which share) |
| As at or period | FY2024 |
| Source name | Barrick, Q4 2024 Mine Stats |
| URL, page and table | link; p. 12, table "Tongon" |
| Flag | sourced / derived (show the working) / assumption (say why) |

Two habits make the platform much harder to attack:

- **Save the PDF and archive the link.** Company pages move. Save each document, and paste each URL into the Wayback Machine (web.archive.org/save) so the citation still resolves later.
- **Record the page and table.** "Barrick 2025 AIF, p. 87, table 3" survives scrutiny; "Barrick website" does not.

Send me the filled rows or the PDFs and I'll load them, flag them, and add checks.

---

## Priority 1: Finish version 1

### A. Loulo-Gounkoto (Mali): give it an NPV

Barrick's site and SEC filings are blocked from my environment, but you can download them directly. This group unlocks the definition-of-done item: showing why Loulo-Gounkoto sits higher on the risk-adjusted cost curve than Tropicana.

- [ ] **Barrick Mineral Reserves and Resources at 31 Dec 2025.**
  - Where: barrick.com, Operations, Mineral Reserves and Resources; also in the 2025 Annual Information Form (AIF) on SEDAR+ (sedarplus.ca) or EDGAR (Form 40-F).
  - Collect: tonnes, grade and ounces for each Loulo-Gounkoto source (Yalea underground, Gara underground, Gounkoto open pit and underground, Loulo open pits, stockpiles), at 100% and attributable, plus the reserve gold price.
  - Defends: the schedule and mine life. Today, secondary sources disagree (6.9 vs 7.3 Moz).
- [ ] **Barrick 2025 AIF, Loulo-Gounkoto section.**
  - Where: SEDAR+ or EDGAR (exhibit to the 40-F).
  - Collect: life-of-mine plan summary; royalties, tax and state interest under the conventions and the 2023 code; the "tested under the 2023 code" statement; any priority dividend.
  - Defends: the royalty, tax and owner's share lines.
- [ ] **Barrick Q4 2024 MD&A and the 2024 and 2026 quarterly "Mine Stats".**
  - Where: barrick.com, Investors, Quarterly results.
  - Collect, by year: tonnes processed, head grade, recovery, production, cash cost, AISC and sustaining capex for Loulo-Gounkoto (2023, 2024, and Q1–Q3 2026).
  - Defends: calibrating site cost per tonne, the same way Tropicana is calibrated to AISC.
- [ ] **Loulo-Gounkoto NI 43-101 technical report** (latest; one effective 31 Dec 2022 exists).
  - Where: SEDAR+ or EDGAR exhibits.
  - Collect: the year-by-year life-of-mine schedule; unit costs (mining US$/t, processing US$/t, G&A); recovery by ore type; sustaining and expansion capex (the 6.2 Mtpa plant); closure cost estimate.
  - Defends: every cost line, and the split the Ground, Infrastructure and People dials act on.
- [ ] **Closure provision for Loulo-Gounkoto.**
  - Where: the provisions note in Barrick's 2025 audited financial statements.
  - Defends: the closure line.
- [ ] **Settlement and new convention terms (24 Nov 2025).**
  - Where: Barrick's 24 Nov 2025 release and Q4 2025 MD&A (US$559M of related adjustments); Mali government communiqués; law-firm notes (search "Mali mining code 2023 decree 2024-0396").
  - Collect: royalty rate, state stake after settlement, tax rate, stability period, and how the US$430M (or US$253M cash tranche) splits.
  - Defends: the Fiscal dial default and the base fiscal terms.
- [ ] **Mali 2023 Mining Code and Decree 2024-0396 (full text).**
  - Collect: the full royalty schedule by gold-price band (the US$1,000–1,600 band is still missing), income tax, state participation tiers, and the priority dividend mechanics.
  - Defends: the royalty line at every price deck, not just today's.

### B. Tongon (Côte d'Ivoire): replace the spreadsheet's own assumptions

The spreadsheet says it is "best guesses from public information, not Tongon's actual mine plan". Barrick disclosed Tongon operating data every quarter until the sale, so most of the guesses can be replaced.

- [ ] **Barrick quarterly Mine Stats and MD&As, 2019 to Q3 2025, Tongon rows.**
  - Collect: tonnes processed, head grade, recovery, production, cash cost, AISC and sustaining capex, by quarter.
  - Defends: three inputs the spreadsheet flags as undisclosed (4.0 Mtpa throughput, 82% recovery, the 1.20 g/t grade path), and the Recovery dial default.
- [ ] **Barrick reserves table, 31 Dec 2024, Tongon row.**
  - Collect: tonnes, grade and ounces, and whether the figure is 100% or 89.7%.
  - Defends: the 620 koz reserve behind the Resource dial; the spreadsheet notes the basis is unclear.
- [ ] **Contingent consideration terms.**
  - Where: Barrick's 2 Dec 2025 release and 2025 annual report; any Atlantic Group disclosure.
  - Collect: the gold-price thresholds and averaging window (2.5 years), and the resource-conversion milestones (5 years).
  - Defends: replaces "50% paid evenly 2026–2028" with an amount and timing tied to the price deck.
- [ ] **Empress Royalty stream documents.**
  - Where: the 17 Sep 2026 release, Empress MD&A and the material change report on SEDAR+.
  - Collect: the tier start date (31 Jan 2026), the ongoing payment, the upfront deposit and the term.
  - Defends: the stream line. A 0.5%-of-spot ongoing payment is unusually low, so confirm it.
- [ ] **EITI Côte d'Ivoire reconciliation reports, Tongon SA rows.**
  - Where: eiti.org/countries/cote-divoire (national reports).
  - Collect: royalties, income tax and dividends Tongon actually paid, by year.
  - Defends: royalty, tax and the 25% rate with actual payments; may hint at the tax base.
- [ ] **Côte d'Ivoire 2025 Finance Law gold royalty schedule.**
  - Collect: every price band (5–8%).
  - Defends: the royalty at the Downside deck and in breakeven solves.
- [ ] **Tongon closure plan or ESIA; Atlantic Group's operator team and mining contractor.**
  - Where: ANDE (Côte d'Ivoire environment agency) notices, Atlantic Group releases, local press.
  - Defends: US$40M closure, the People dial (Medium because the owner hasn't run a mine), and the Community and Infrastructure dials, which have no public evidence yet.

### C. Tropicana (Western Australia): replace back-solved costs

- [ ] **AngloGold Ashanti 2025 Form 20-F, Tropicana section.**
  - Where: reports.anglogoldashanti.com/25/download/AGA-20F25.pdf.
  - Collect: per-mine AISC and total cash cost in US$, tonnes, recovery, and capex by type.
  - Defends: a direct cross-check on the A$ AISC calibration and the 0.70 FX assumption.
- [ ] **AngloGold Mineral Resource and Ore Reserve Report 2025.**
  - Collect: life-of-mine plan beyond reserves, underground conversion history, and unit costs if given.
  - Defends: the life-extension stepper, which is today a flagged resource-conversion case.
- [ ] **Regis FY26 annual report (to 30 Jun 2026), Tropicana segment and notes.**
  - Collect: the rehabilitation provision (30% share), PP&E (30%), D&A and segment costs.
  - Defends: the US$100M closure and US$500M tax base assumptions.
- [ ] **Havana Underground release (9 Sep 2024), full table.**
  - Collect: capex at 100%.
  - Defends: growth capex (now the FY27 guidance midpoint ÷ 30%).
- [ ] **Tailings and water.**
  - Where: Global Tailings Portal (tailing.grida.no), WA DEMIRS approvals, DWER water licences.
  - Collect: TSF capacity and consequence class, and water source and licence limits.
  - Defends: the Infrastructure and Community dial evidence.

---

## Priority 2: Calibrate the dials

Every dial level is a starting assumption today. Base rates from comparable mines are what make each level defensible. Build one comparables table (suggested columns at the end) and fill it from the sources below.

- [ ] **Resource and grade (grade −5/−10%, life −10/−25%).**
  - Where: company reserve reconciliation tables (Newmont, Barrick and AngloGold publish additions, depletion and revisions each year); mill-to-model reconciliation statements in JORC Table 1 and annual reports; S&P Capital IQ Pro reserve histories (Stanford library).
  - Collect, for 20–30 comparable gold mines: planned versus actual head grade in the first 3–5 years, reserve revisions, and Inferred-to-Indicated conversion rates.
- [ ] **Recovery (−1/−4/−12 points).**
  - Where: feasibility studies versus later annual reports for the same mines; academic work on study accuracy (search the library for McCarthy, "Why feasibility studies fail").
  - Collect: planned versus achieved recovery, split by plant history (years of data) and ore type (oxide versus fresh, refractory).
- [ ] **Ramp-up and schedule (People, Capex and Community delays).**
  - Where: McNulty's ramp-up curves (Mining Engineering, 1998, via the library); company releases on first gold versus plan.
  - Collect: months from first gold to nameplate, and months late versus study.
- [ ] **Capex overruns (+15/+35%).**
  - Where: Bertisen and Davis (2008), "Bias and error in mine project capital cost estimation" (The Engineering Economist, via the library); company releases on final versus study capex.
  - Collect: overrun distribution by study stage (PFS versus DFS) and region.
- [ ] **Ground and mining stoppages (5% a year × 2 months at High).**
  - Where: company releases; WA DEMIRS incident reports; news archives.
  - Collect: an event table of mine, year, cause (wall failure, flooding, collapse), months lost and output lost, covering roughly 2005–2025. Include Santa Rita 2021, which the spec cites.
- [ ] **Infrastructure outages (2% a year × 1 month at High).**
  - Where: World Bank Enterprise Surveys (enterprisesurveys.org) for outages per month by country; GlobalPetrolPrices (globalpetrolprices.com) for diesel; Mali fuel-blockade reporting.
  - Collect: outage frequency and duration for Mali, Côte d'Ivoire and Australia, and the diesel price history.
- [ ] **Labour (People dial).**
  - Where: ILOSTAT strikes and lockouts (ilostat.ilo.org); Fraser survey sub-indices for labour regulation and skills availability; company releases.
  - Collect: strike days per year in mining by country, and contractor changes at comparable mines.
- [ ] **Fiscal changes (25% or 50% chance of +2 points within three years).**
  - Where: EY, PwC and KPMG mining tax guides (free PDFs, one per year); the IMF's fiscal regime notes; NRGI Resource Governance Index (resourcegovernance.org).
  - Collect: a dated list of gold royalty, tax and state-stake changes for about 15 African and Australian jurisdictions, 2005–2026. The frequency of rises per country per three years is the probability the dial needs.
- [ ] **Expropriation and disputes (Political and Fiscal at High).**
  - Where: the ICSID case database (icsid.worldbank.org/cases/case-database); UNCTAD's investment dispute navigator; news.
  - Collect: mining disputes by country and outcome, including Barrick v. Mali, and asset seizures or forced renegotiations since 2010.
- [ ] **Community and environment (blockade probabilities).**
  - Where: EJAtlas (ejatlas.org); the Business and Human Rights Resource Centre; national press.
  - Collect: blockades or protests at gold mines by country, with duration.
- [ ] **Climate (drought and flood downtime).**
  - Where: World Bank Climate Change Knowledge Portal (climateknowledgeportal.worldbank.org); ND-GAIN (gain.nd.edu).
  - Collect: drought and flood frequency for each mine's region, and any weather stoppages (for example, Regis's Duketon rain in September 2026).

**Suggested comparables table:** mine; country; years; study type; planned vs actual grade, recovery, throughput, capex and first gold; stoppage events (cause, months); fiscal changes (date, size); source per cell.

---

## Priority 3: Cross-check country risk and value

- [ ] **Damodaran country risk premiums: January 2026 file and the July 2026 update.**
  - Where: pages.stern.nyu.edu/~adamodar, the current data page and the "archived data" page.
  - Collect: rows for Côte d'Ivoire (replaces the 3.90% Ba2 fallback), Mali and Australia; also the 2015–2026 history for each.
  - Defends: the Political dial, and shows how stable the premium is.
- [ ] **Sovereign CDS and Eurobond spreads** (the spec's "Could": a second country-risk method).
  - Where: Bloomberg via Stanford library.
  - Collect: 5-year CDS for Côte d'Ivoire if it trades; Eurobond yields for Côte d'Ivoire; Mali has no liquid market, so note that.
  - Defends: a market-implied survival factor to set against Damodaran.
- [ ] **Governance and security indices.**
  - Where: World Bank Worldwide Governance Indicators; the Fraser survey 2020–2025 series (investment attractiveness and policy perception); ACLED event data (acleddata.com, free research registration); Global Peace Index.
  - Collect: country scores over time, and ACLED events within 50 km of each mine (Kéniéba in Kayes region; Tongon's area of northern Côte d'Ivoire).
  - Defends: the Political and Community dial evidence with numbers rather than anecdotes.
- [ ] **Gold price consensus from more than one bank.**
  - Where: the LBMA annual forecast survey (lbma.org.uk); the World Bank Commodity Markets Outlook (April and October); published bank forecasts; Reuters' quarterly gold poll summaries.
  - Collect: forecasts by year, deflated to real terms with US CPI (FRED series CPIAUCSL), since the model is real.
  - Defends: the Consensus deck, which today rests on one bank plus a flat assumption.
- [ ] **Peer cost curve.**
  - Where: S&P Capital IQ Pro (Stanford library) for global gold AISC by mine; peer company reports.
  - Collect: AISC and output for about 30 peer mines.
  - Defends: puts the three assets on a real industry cost curve rather than one built only from themselves.
- [ ] **Real discount rate convention.**
  - Where: VALMIN and CIMVAL valuation code guidance; company reserve statements stating their discount rates; published broker NAV notes.
  - Defends: the 5% real default.
- [ ] **Transaction and stream comparables.**
  - Where: company releases and deal coverage on MINING.COM, Reuters and Kitco.
  - Collect: price per reserve ounce and P/NAV for recent gold deals (including Tongon, at US$192–305M for 89.7%), plus stream terms (rates, ongoing payments, deposits).
  - Defends: a market sanity check on the app's values, and data for the future structuring view.

---

## Priority 4: Extend scope

- [ ] **Undeveloped deposit with a public feasibility study** (the spec's "Should").
  - The spec suggests Assafou, using only public data.
  - Collect: capex, construction schedule, life-of-mine production, AISC, recovery, permitting status and study date.
  - Defends: exercises the Capex and schedule dial, which the engine already supports.
- [ ] **A second operating mine in a mid-risk jurisdiction** (for example Ghana or Burkina Faso).
  - Defends: fills out the cost curve between Australia and Mali.

---

## Fastest wins

If you only have an afternoon, these four remove the most flagged assumptions:

1. Barrick's 31 Dec 2025 reserves table and the Q4 2025 MD&A, which together nearly unblock Loulo-Gounkoto.
2. Barrick Tongon quarterly Mine Stats for 2019–2025, which replace Tongon's throughput, grade and recovery guesses.
3. Damodaran's January 2026 archived file, which replaces the Côte d'Ivoire fallback.
4. AngloGold's 2025 Form 20-F, Tropicana section, which cross-checks the Tropicana cost calibration.
