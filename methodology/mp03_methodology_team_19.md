
# MP03 Methodology — Team 19

## Ticker-list rationale

The Financial Services ticker list began with the instructor seed list and was extended with GS, MS, and COF. These additions help include investment banking, capital-markets activity, and consumer finance, so the Financial Services pipeline is not limited only to retail banking branches.

The Travel and Hospitality ticker list keeps the instructor seed list because it already covers hotels, cruise lines, airlines, and online travel companies.

## Search-phrase rationale

The Financial Services phrase list was extended with "office relocation" and "financial center" because financial companies often describe physical location changes as offices, centers, or regional operations rather than only branch openings and closings.

The Travel and Hospitality phrase list was extended with "new destination", "route expansion", and "resort expansion" because airlines and hotel companies often describe physical growth through routes, destinations, resorts, and property openings.

## Window-tuning results

| industry               |   window_days |   candidate_count |   event_count |   estimated_cost_usd |
|:-----------------------|--------------:|------------------:|--------------:|---------------------:|
| Financial Services     |            30 |                 0 |             0 |                    0 |
| Travel and Hospitality |            30 |                 0 |             0 |                    0 |
| Financial Services     |            60 |                 0 |             0 |                    0 |
| Travel and Hospitality |            60 |                 0 |             0 |                    0 |
| Financial Services     |            90 |                 0 |             0 |                    0 |
| Travel and Hospitality |            90 |                 0 |             0 |                    0 |
| Financial Services     |           180 |                 0 |             0 |                    0 |
| Travel and Hospitality |           180 |                 0 |             0 |                    0 |
| Financial Services     |           360 |                 0 |             0 |                    0 |
| Travel and Hospitality |           360 |                 0 |             0 |                    0 |

## Stage 3 classification quality

Stage 3 was checked by reviewing whether Claude's event_type matched the summary and whether city and state were populated when is_location_event was true. Records without usable geocoding information were not added to the final map.

## Limitations

The pipeline depends on 8-K filings, EDGAR keyword search, and the selected search phrases. Some location events may be missed if companies used different wording or reported location activity outside of 8-K exhibits. The geocoder may also miss ambiguous or international locations.

Chosen window: 360 days.

Total final mapped events: 0.
