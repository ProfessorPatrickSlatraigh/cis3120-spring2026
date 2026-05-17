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

Reference: docs/MP03_Assignment.docx, Section 3.
"""

# ──────────────────────────────────────────────────────────────────────────
#  Financial Services (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # Money-center banks
    "JPM", "BAC", "WFC", "C",
    # Regional banks
    "PNC", "USB", "TFC",
    # Asset management
    "BLK", "BX",
    # Insurance
    "MET", "PRU",
    # Payments
    "V", "MA", "AXP",
    # Consumer finance
    "COF","DFS",
    # Wealth management
    "SCHW", "EVR",
    # Capital markets banks
    "GS", "MS",
]

FINANCIAL_SERVICES_PHRASES = [
    '"new branch"',
    '"new office"',
    '"branch opening"',
    '"branch closure"',
    '"branch closing"',
    '"branch consolidation"',
    '"regional office"',
    '"office opening"',
    '"new headquarters"',
    '"headquarters relocation"',
    '"office expansion"',
    '"branch relocation"',
    '"office relocation"',
    '"office closure"',
    '"operations center"',
    '"data center"',
    '"new location"',
    '"JPMorgan" "branch"',
    '"Bank of America" "branch"',
    '"Wells Fargo" "branch"',
    '"Citi Bank" "branch"',
    '"Blackstone" "branch"',
    '"Blackrock" "branch"',
    '"Visa" "branch"',
    '"Charles Schwab" "branch"',
    '"Goldman Sachs" "branch"',
     '"Morgan Stanley" "branch"',
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
    "DAL", "UAL", "AAL", "LUV","JBLU"
    # Online travel
    "BKNG", "EXPE", "ABNB", "UBER",
    #Resorts and Casinos
    "WYNN","CZR","BYD","MGM"
    #Hotel REITS
    "PEB","PK","APLE","HST","BHR",
]

TRAVEL_HOSPITALITY_PHRASES = [
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"new route"',
    '"route expansion"'
    '"new service"',
    '"flight route"',
    '"new gateway"',
    '"new terminal"',
    '"grand opening"'
    '"destination opening"',
    '"intinerary expanded"',
    '"now open"',
    '"completed the sale"',
    '"new aquisition"',
    '"completed the aquisition"',
    '"sold its"',
    '"sale of the hotel"',
    '"officially opened"',
    '"soft opening"',
  


]