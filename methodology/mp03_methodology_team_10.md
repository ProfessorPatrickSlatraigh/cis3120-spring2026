## 6. Methodology


### 6.1 Ticker-list rationale

Financial Services

The seeded 14 tickers cover money-center banks, three regionals, two asset managers, two insurers, and the card networks, but Section 3 of the assignment explicitly flags the seed as biased toward retail-banking events and lacking capital-markets coverage. To close this gap, eleven tickers were added across four under-represented segments. Mid-cap regionals FITB, RF, and KEY were added because branch consolidation activity is most concentrated at this tier — the money-center banks have largely completed theirs, but mid-caps are still rationalizing post-2008 acquisitions. Capital markets names GS and MS were added because the seed had zero pure investment banks; without them the map would skew toward retail geography and miss the financial centers where IB capacity actually sits. Custody banks BK, STT, and NTRS were added because they operate the largest operations centers in the industry and are unusually frequent filers of ops-center relocation 8-Ks. Exchanges ICE, CME, and NDAQ were added because they file 8-Ks for data-center and matching-engine relocations, which represent a class of location event that no bank produces. SCHW, ALLY, and KKR were added to round out brokerage, consumer finance, and alternative asset management. No original tickers were removed.

Travel and Hospitality

The seeded 14 tickers were expanded to 75 across several segments. Casino-resort operators MGM, LVS, WYNN, CZR, PENN, BYD, and DKNG were added because they regularly file location-related 8-Ks for property openings and sportsbook launches not represented in the seed. Hotel REITs (PK, HST, APLE, RHP) were added because they file 8-Ks for individual lodging properties frequently. IHG and JBLU were added for broader hotel brand and Northeast airline coverage respectively. TRIP and ABNB were added to represent other common online travel booking agencies. Theme park operators DIS, SEAS, and EPR were added for attraction and entertainment coverage. Ground transportation tickers HTZ, CAR, UBER, and LYFT were added for rental and mobility events. I considered adding MAA but removed it as it is a residential REIT not hospitality. No original seed tickers were removed.

Retail

The retail list has around 87 publicly-traded U.S. retailers across 15+ sub-segments: big-box (WMT, TGT, COST), home improvement (HD, LOW), off-price and dollar (TJX, ROST, DG, DLTR, BURL), drug stores (WBA, CVS, RAD), specialty (BBY, GPS), grocery (KR, SFM, ACI, WMK, GO), department stores (M, KSS, JWN), beauty (ULTA, ELF, COTY, SBH), discount specialty (FIVE, OLLI, BIG, PSMT), auto (AAP, ORLY, AZO), apparel (AEO, URBN, ANF, LULU, PLCE, RL, VFC, TPR, LEVI, and others), pet retail (CHWY, PETQ, WOOF), furniture and home (W, RH, WSM, ETD, LZB), e-commerce (AMZN, EBAY, ETSY), sporting (DKS, ASO, HIBB), mattress (TPX, SNBR, PRPL), jewelry (SIG, TIF), and convenience and fuel retail (CASY, BJ, MUSA). I extended the original 14-ticker seed in three rounds. First to 20 by adding department stores, beauty, discount specialty, and auto retail, then up to around 87 to maximize event coverage at the 30-day window. Sub-segment breadth matters because drug stores trend toward net-closing while dollar stores trend toward net-opening, so a list weighted toward one sub-segment would have produced a one-sided view of expansion versus consolidation.  


### 6.2 Search-phrase rationale

Financial Services

All 10 seed phrases were retained. For corporate real estate, "headquarters relocation", "relocate its headquarters", "new headquarters", "lease termination", and "office relocation" were added to catch HQ moves and lease decisions that the retail-branch vocabulary misses. For capital markets specifically, "trading floor", "matching engine", and "exchange floor" were added because these phrases essentially only appear in IB and exchange filings, giving high precision for the segment the seed undercounted. For consolidation activity, "footprint reduction", "consolidate operations", and "office consolidation" were added to pick up cost-rationalization filings that don't actually use the word "branch" — important because some of the most relevant white-collar consolidation 8-Ks avoid retail-branch language. Finally, "expanded presence" and "new office" were added on the expansion side so the corpus would not be structurally biased toward consolidation alone. "Office" alone and "closing" alone were considered but dropped because they generate too many false positives — every governance section mentions "office", and "closing" matches every loan-closing event in bank 8-Ks.

Travel and Hospitality

All 10 seed phrases were kept and the list was expanded to 71 phrases across seven sub-segments. For hotels, "hotel acquisition" and "property acquisition" were added for REIT filings, and "all-inclusive resort", "vacation club", and "new timeshare" were added for VAC and HGV coverage. For airlines, "new concourse", "new crew base", and "new training center" were added for facility events beyond route launches. For cruise, "private island" and "new itinerary" were added as well as "private island" where there is high precision, appearing almost exclusively in CCL and RCL destination opening filings. For gaming, "new sportsbook" and "retail sportsbook" were added for DKNG and PENN physical location openings. For theme parks, "new ride" and "new land" were added as it shows higher accuracy in Disney themed land announcements. I changed "homeport" to "home port" as cruise lines commonly write it as one word in actual filings.

Retail

The retail phrase list has around 76 phrases across three categories. For expansion: "new store," "store opening," "grand opening," "flagship store," "new location," "new format," "opened a new," "announced the opening," "plans to open," "first store," "expanding," "expansion," "new market," "market entry," "international expansion," and others. For consolidation: "store closure," "store closing," "store closures," "store consolidation," "plans to close," "to close," "will close," "announced the closure," "closing stores," "closure of," "footprint reduction," and others. For supply-chain and real estate: "distribution center," "fulfillment center," "warehouse opening," "distribution facility," "store relocation," "omnichannel hub," "facility opening," "facility closure," "sale-leaseback," "property acquisition," "lease termination," "real estate," and others. I extended the original 10-phrase seed to 16 in round 2 to cover supply-chain language, then to around 76 in round 3 to include the corporate 8-K language that smaller phrase lists miss. The broader phrases trade precision for recall, which matches the Module 15 pipeline design where Stage 1 retrieves widely and Stage 3 filters strictly.


### 6.3 Window-experiment results

| | industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---|---|---|---|---|
| 0 | Financial Services | 30 | 21 | 3 | 0.008127 |
| 1 | Financial Services | 60 | 24 | 5 | 0.013549 |
| 2 | Financial Services | 90 | 25 | 5 | 0.013574 |
| 3 | Financial Services | 180 | 48 | 7 | 0.019493 |
| 4 | Financial Services | 360 | 88 | 9 | 0.024986 |
| 5 | Travel and Hospitality | 30 | 17 | 3 | 0.008320 |
| 6 | Travel and Hospitality | 60 | 21 | 3 | 0.008320 |
| 7 | Travel and Hospitality | 90 | 29 | 5 | 0.014298 |
| 8 | Travel and Hospitality | 180 | 9 | 3 | 0.008780 |
| 9 | Travel and Hospitality | 360 | 17 | 5 | 0.015829 |
| 10 | Retail | 30 | 20 | 1 | 0.002636 |
| 11 | Retail | 60 | 29 | 3 | 0.006982 |
| 12 | Retail | 90 | 55 | 4 | 0.009874 |
| 13 | Retail | 180 | 80 | 2 | 0.004674 |
| 14 | Retail | 360 | 92 | 2 | 0.005395 |

360 is the appropriate window because the Travel and Hospitality and Retail industries do not get the required 8 events. Additionally, the total cost for all trials is ~$0.16 which is under the $3 limit.

### 6.4 Stage 3 classification quality per industry

Financial Services

At the 30-day window, Stage 3 processed 2 candidates and classified 0 as location events. Both were quarterly earnings releases that mentioned branch-related language in boilerplate sections, not actual location announcements. At the 360-day window, the pipeline identified multiple true location events including branch openings by National Bankshares (Roanoke, VA), Unity Bancorp (Madison, NJ), Farmers & Merchants Bancorp (Livingston, CA), First United (Boonsboro, MD), and Amerant Bank (Miami Beach, FL), plus one closing by First Northwest Bank (Bellevue, WA). The main false positive pattern was investor presentations referencing branch counts statistically rather than announcing a specific new event.


Travel and Hospitality 

Stage 3 has classified 7 of 17 filtered candidates as location events at the 360-day window, yielding 4 openings and 3 expansions with clean, complete field extraction. The 10 false positives were relatively precise in correctly filtering out 4 Caesars quarterly earnings releases, 3 credit/debt facility amendments (Travel & Leisure, Park Hotels), and a Hyatt Hotels Corp agreement as generic corporate disclosures. However, potential false negatives remain unverified for a Six Flags news release and a DiamondRock exhibit. Two key error patterns emerged: two different phrases must have matched filings that describe the same event in the candidates list which got classified twice by Stage 3, leading to dual records for both the Hollywood Casino Joliet and Royal Palm South Beach Miami events. A misclassification occurred on a Phoenix record, where an acquisition (change of ownership) was flagged as a new facility "opening".

Retail

At the 30-day window, Stage 3 processed 19 candidates and classified 1 as a confirmed location event. With only one event, a true precision rate isn't statistically meaningful, but the 19-to-1 funnel itself is informative. It reflects the recall-over-precision choice in 6.2, where the 76-phrase seed casts wide on purpose. The filtered candidates appeared to fall into three patterns: earnings releases using "expansion" in a financial sense, routine business overviews mentioning past store counts, and lease or real-estate disclosures that weren't tied to a specific new opening or closing. The most plausible false-negative risk is small-format moves that retailers disclose informally rather than in an 8-K, which the pipeline can't recover. The low conversion is also consistent with retail filing behavior at a short window. Most 30-day 8-K activity is earnings, executive changes, and dividends, not store-level real estate, so a longer window is likely necessary for retail to produce a comparable event count. 


### 6.5 Limitations

Financial Services 
The primary limitation was phrase mismatch — terms like "data center" and "executive offices" generated high false positive volumes from earnings releases rather than location announcements. A second limitation was that large banks like JPMorgan rarely file dedicated 8-Ks for individual branch decisions, so the pipeline undercounts events for the largest institutions while overcounting false positives from smaller community banks whose investor presentations happen to contain branch-related language.
Travel and Hospitality  

The pipeline’s primary limitation was that it failed to find the target of 8 events even after searching a full year of data, because travel and hospitality companies usually announce new locations in press releases or investor meetings rather than official SEC 8-K filings. Second, because the system looks for each search phrase separately and doesn't remove duplicate results, the exact same real-world events (like the Joliet and Miami locations) were counted and mapped multiple times, making the map look more crowded than it actually is. Third of all, searching for a longer timeframe didn’t always bring back more data; for example, the 180-day window trial brought back fewer results than the 90-day trial because of system lag and temporary website errors on the SEC database.

Retail

Four limitations shape how retail can be read in the comparative reflection. First, sub-segment selection is itself an analytical choice. The 87-ticker list leans toward big-box, dollar, drug, off-price, and supply-chain real estate, and a list weighted toward apparel or grocery would produce a different map. The retail pattern should be read as one defensible slice of public retail, not the full industry. Second, the 8-K disclosure threshold makes small and independent retailers invisible, which undercuts coverage of a meaningful share of U.S. store-level activity. Third, the recall-over-precision phrase choice lowers expected Stage 3 precision relative to a tighter list. Verifying it tightly would require manual review of the full candidate set. Fourth, the 30-day window produced only one confirmed retail event, which limits how much the reflection can claim about retail's geography at this window. Longer windows are likely needed for retail to support meaningful comparison with Financial Services and Travel & Hospitality. 