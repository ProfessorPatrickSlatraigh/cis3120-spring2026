"""
Seeded data for Mini-Project MP03 — Press Release to Plot: Industry Comparison.

These lists are starting points provided by the instructor. Teams are expected
to modify both the ticker lists and the phrase lists during the project.
Modifications must be justified in the methodology section.

The seeds were chosen to give each industry a working starting point, not to
be optimal. The Financial Services seed is biased toward retail-banking events
and undercounts capital-markets activity; the Travel and Hospitality seed
mixes hotel-style and airline-style location events that may warrant separate
treatment in your map. Identifying these limitations and proposing fixes is
the methodology section's purpose.

Reference: docs/MP03_Assignment.docx, Section 3..
"""

# ──────────────────────────────────────────────────────────────────────────
#  Financial Services (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # Money-center banks
    "JPM", "BAC", "WFC", "C",

    # Regional banks
    "PNC", "USB", "TFC", "RF", "FNB", "HBAN", "AUB",

    # Asset management
    "BLK", "BX", "GS", "MS", "SCHW",

    # Insurance
    "MET", "PRU", "ALL", "TRV",

    # Payments
    "V", "MA", "AXP", "COF", "DFS",
]

FINANCIAL_SERVICES_PHRASES = [
    '"new branch"',
    '"branch opening"',
    '"branch closure"',
    '"branch closing"',
    '"branch consolidation"',
    '"regional office"',
    '"office closure"',
    '"operations center"',
    '"data center"',
    '"new location"',
    # Added phrases
    '"branch network"',
    '"financial center"',
    '"banking center"',
    '"new financial center"',
    '"new banking center"',
    '"office relocation"',
    '"new office"',
    '"regional headquarters"',
    '"operations hub"',
    '"service center"',
    '"customer service center"',
    '"call center"',
    '"corporate office"',
    '"office opening"',
    '"office expansion"',
    '"branch relocation"',
    '"relocated branch"',
    '"new headquarters"',
    '"headquarters relocation"',
    '"technology center"',
    '"processing center"',
    '"loan production office"',
    
]

# ──────────────────────────────────────────────────────────────────────────
#  Travel and Hospitality (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

TRAVEL_HOSPITALITY_TICKERS = [
    # Hotels
    "MAR", "HLT", "H", "CHH", "WH",
    # Cruise
    "CCL", "RCL", "NCLH",
    # Airlines
    "DAL", "UAL", "AAL", "LUV",
    # Online travel
    "BKNG", "EXPE",
    # Casinos / Resorts
    "MGM", "WYNN", "LVS",

    # Alternative lodging
    "ABNB",

    # Travel tech
    "TCOM",
]

TRAVEL_HOSPITALITY_PHRASES = [
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"new route"',
    '"new gateway"',
    '"new terminal"',
    '"grand opening"',
     # Added phrases
    '"new resort"',
    '"hotel expansion"',
    '"destination opening"',
    '"new service route"',
    '"airport lounge"',
    '"new flights"',
    '"tourism expansion"',
    '"hospitality expansion"',
    
    '"Marriott" "opening"',
    '"Hilton" "opening"',
    '"Hyatt" "opening"',
    '"Wyndham" "opening"',
    '"Delta" "new route"',
    '"United Airlines" "new route"',
    '"American Airlines" "new route"',
    '"Southwest" "new route"',
    '"Carnival" "new port"',
    '"Royal Caribbean" "new itinerary"',
    '"MGM" "new resort"',
    '"Wynn" "new resort"',

    
]
