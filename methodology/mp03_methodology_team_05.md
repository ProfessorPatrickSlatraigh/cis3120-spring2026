MP03 Methodology — Team 05
Industry Comparison: Financial Services and Travel and Hospitality

6.1 Ticker-List Rationale
Financial Services: We started with the seed list and added GS, MS, SCHW, PYPL, and SQ to cover capital markets, brokerage, and fintech firms that weren't in the original list. These companies have physical offices and branches that could show up in location-related 8-K filings.
Travel and Hospitality: We kept the seed list and added lodging REITs (HST, PK, APLE, etc.), resort/casino operators (MGM, LVS, WYNN), additional airlines (ALK, JBLU, SAVE), and vacation ownership firms (VAC, TNL, HGV). Stage 1 testing showed that a lot of hotel and property-related EDGAR hits came from property owners and operators rather than the big brand names like Marriott or Hilton, so expanding the list improved how many relevant filings we found.

6.2 Search-Phrase Rationale
Financial Services: We kept all the seed phrases and added "new office", "office opening", "trading floor", and "advisory office" to catch capital markets and wealth management announcements. We also added company-name phrases like "JPMorgan" "branch" and "Goldman Sachs" "office" to target specific firms directly. Even with these additions, EDGAR returned very few candidates because big banks usually don't file standalone 8-Ks for branch changes — they report that kind of thing in earnings releases instead.
Travel and Hospitality: We extended the seed phrases with terms like "new resort", "resort expansion", "hotel conversion", "route expansion", and "new destination" to catch more types of location events beyond just hotel openings. We also added some unquoted terms like hotel opening and new hotel to improve recall since EDGAR's search can miss things when phrases are too specific.

6.3 Window-Experiment Results
The results showed: [industry, window_days, candidate_count, event_count, estimated_cost_usd]
[Financial Services, 30, 0, 0, 0.000000]
[Financial Services, 60, 0, 0, 0.000000]
[Financial Services, 90, 0, 0, 0.000000]
[Financial Services, 180, 0, 0, 0.000000]
[Financial Services, 360, 1, 1, 0.002928]
[Travel and Hospitality, 30, 42, 8, 0.106696]
Travel and Hospitality hit the 8-event target at 30 days and stopped there. Financial Services never reached the target, it returned zero candidates through 180 days and only 1 at 360 days. The chosen window is 360 days because that's the ceiling and Financial Services fell short at every window tested. The shortfall is acknowledged in the limitations section. Total API cost across all trials was about $0.11, which is well under the $3.00 ceiling.


6.4 Stage 3 Classification Quality
Travel and Hospitality: Out of 42 candidates at 30 days, Claude classified 8 as real location events and rejected the other 34. Of the 8, 7 were successfully geocoded. The positive classifications looked very legitimate, they included hotel tower openings, property announcements, and filings relating to resorts with specific cities and states. One event failed geocoding because the city Claude extracted didn't resolve in Nominatim.
Financial Services: Only one candidate came through across all windows, and it was classified as a true event but failed geocoding. With only one result there's not much to evaluate.

6.5 Limitations
The biggest limitation is that Financial Services barely showed up in EDGAR at all. Large banks don't usually file standalone 8-Ks for branch openings or closures, they report that in earnings calls or 10-Ks, which our pipeline doesn't search. The ticker filter may also have cut out some valid hits if EDGAR didn't attach ticker metadata to the filing. On the Travel side, one event was lost at geocoding because the city Claude extracted didn't resolve in Nominatim. The 30-day window for Travel also means we're only seeing very recent filings, which might not represent typical patterns over a longer period.
