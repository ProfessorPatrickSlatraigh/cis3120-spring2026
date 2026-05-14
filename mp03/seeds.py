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
# Financial Services (Modified to include Investment Banking & Wealth Mgmt)
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
    # Added: Investment Banking & Capital Markets
    "GS", "MS", "RJF"
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
    # Added: Corporate & Capital Markets infrastructure
    '"trading floor"',
    '"wealth management office"',
    '"private banking center"'
]

# ──────────────────────────────────────────────────────────────────────────
# Travel and Hospitality (Modified to include expanded Aviation/Leisure)
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
    # Added: Vacation Ownership & Additional Aviation
    "VAC", "ALK"
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
    # Added: Specific infrastructure & service expansions
    '"hangar opening"',
    '"maintenance base"',
    '"flight path launch"'
]
