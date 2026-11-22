# Lithium benchmarks: what to fetch

These documents set the typical values in the lithium deposit screener. The screener covers hard-rock spodumene: ore mined, concentrated on site to about 6% Li₂O (SC6), trucked or railed to port, and shipped. Every typical value in the app will cite one of these documents.

Upload what you find to the chat, or open the network so I can fetch them myself (see the end).

**Tip:** for each study, get the **results announcement**: the 20–40 page "DFS/PFS/PEA results" release, usually with a key-metrics table. It has almost everything, and the 400-page technical report is only needed for gaps.

## 1. Data that applies everywhere

- [ ] **Damodaran country risk premiums, January 2026.** Download `ctryprem.xlsx`, or save `ctryprem.html` as PDF, from pages.stern.nyu.edu/~adamodar. One file covers every country we'll need. If his July 2026 update is also available, grab that too.
- [ ] **Spodumene price forecast.** Get the Australian Government's *Resources and Energy Quarterly*, latest edition, lithium chapter: SC6 price history and forecast. It's free from industry.gov.au.
- [ ] **Current realised spodumene price.** Get the latest quarterly reports (Sep quarter 2026) from **PLS** (formerly Pilbara Minerals) and **Liontown**. They show realised US$/t and the grade it was sold at.
- [ ] **Fiscal terms.** Get the latest **EY Global Mining & Metals Tax Guide** (free PDF) for royalty, income tax and state participation by country. The studies below also state their own royalty and tax.

## 2. Studies: the benchmark set

These span three stages (scoping/PEA, PFS, DFS), several countries, and the whole range of haulage: a short truck run to port, a long road haul across borders, and remote North American logistics. Fetch them in this order; the first six would already give useful typical values.

| # | Company and project | Country | Why it's in the set |
|---|---|---|---|
| 1 | Liontown, **Kathleen Valley** (DFS and later updates) | Western Australia | Tier-one Australian benchmark; truck to port; now producing, so the study can be checked against actual results |
| 2 | Atlantic Lithium, **Ewoyaa** (DFS) | Ghana | West Africa; short haul to Takoradi port; negotiated royalty and state stake |
| 3 | Kodal Minerals, **Bougouni** (feasibility study) | Mali | Very long road haul to a port in another country; Mali fiscal and export risk |
| 4 | Leo Lithium / Ganfeng, **Goulamina** (DFS) | Mali | Large Malian deposit; the 2023–24 dispute over the state's stake is a real risk case |
| 5 | Patriot Battery Metals, **Shaakichiuwaanaan** (PEA) | Quebec, Canada | Remote, large and early stage; long road and rail logistics |
| 6 | Core Lithium, **Finniss** (DFS and the restart study) | Northern Territory, Australia | Short haul to Darwin; a mine that was paused when prices fell |
| 7 | Critical Elements, **Rose** (feasibility study) | Quebec, Canada | Second Canadian data point at feasibility stage |
| 8 | Sigma Lithium, **Grota do Cirilo** (latest technical report) | Brazil | Low cost, producing; road haul to a Brazilian port |
| 9 | AVZ Minerals, **Manono** (DFS) | DR Congo | Extreme logistics (about 2,000 km to the Indian Ocean) and a licence dispute with the state |
| 10 | Savannah Resources, **Barroso** (latest study) | Portugal | European permitting and a European cost base |
| 11 | Global Lithium, **Manna**, or Delta Lithium, **Mt Ida** (latest study) | Western Australia | Junior Australian deposits at earlier stages |

## 3. What I'll extract from each study

You don't need to fill this in; upload the PDF and I'll extract it. Listed so you know what matters.

| Area | Values |
|---|---|
| Study | Stage (scoping/PEA, PFS, DFS), date, owner, ownership share |
| Deposit | Resource and reserve tonnes and % Li₂O by category; strip ratio; open pit or underground |
| Mining | Mining rate, dilution and recovery; mining cost (US$/t moved or per t ore) |
| Processing | Throughput (Mtpa), head grade, recovery, concentrate grade (SC5.5 or SC6), concentrate output (ktpa), processing cost (US$/t ore) |
| Overheads | Site G&A (US$M/yr), power source and cost, camp and fly-in/fly-out costs |
| Haulage and logistics | Mode (truck, rail), distance (km), haulage cost (US$/t concentrate), port charges (US$/t), shipping (US$/t), sale basis (FOB or CIF) |
| Fiscal | Royalty (rate and base), income tax, state stake, other levies |
| Capital | Initial capex split (plant, infrastructure, pre-strip, owner's costs, contingency %), sustaining capex, closure |
| Economics | Price deck (US$/t SC6), discount rate, NPV, IRR, payback, AISC or C1 cost |

Each study then gives the app one row of evidence, and the typical value for any input is the median across studies, with the range shown. Haulage rates come out in US$ per tonne-km, by mode, from the studies' own distances and costs.

## Or open the network so I can fetch them

The session's network policy currently blocks these sites. To let me fetch the documents directly, change **Network access** in the environment's settings: the cloud environment menu in the session's title bar, then Edit. The steps are at https://code.claude.com/docs/en/cloud-environments#network-access.

Either choose a broader access level while we compile, or add the hosts below under Allowed domains, leaving "Allow package managers" ticked:

- `announcements.asx.com.au`, `www.asx.com.au` (most Australian and some African studies)
- `www.sedarplus.ca`, `www.sec.gov` (Canadian and US technical reports)
- `pages.stern.nyu.edu` (Damodaran)
- `www.industry.gov.au` (Resources and Energy Quarterly)
- `www.ey.com` (tax guide)
- `minedocs.com` (hosts many technical reports)
- the company sites, as needed

If the change doesn't reach this running session, uploading works just as well.
