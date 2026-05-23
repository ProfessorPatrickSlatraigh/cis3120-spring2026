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
    # Mid-cap regionals
    "FITB", "RF", "KEY", "ZION", "CFG", "HBAN", "MTB", "FHN",
    # Smaller regionals with active branch activity
    "BOKF", "WTFC", "CVBF", "IBCP", "UCBI", "SFNC", "FFIN",
    "NBTB", "CTBI", "FULT", "WSBC", "RNST", "HOPE", "BPOP",
    # Capital markets / investment banks
    "GS", "MS", "LAZ", "EVR", "PJT", "HLI",
    # Asset management
    "BLK", "BX", "KKR", "APO", "ARES", "OWL", "CG", "BAM",
    # Custody / trust banks
    "BK", "STT", "NTRS",
    # Exchanges
    "ICE", "CME", "NDAQ", "CBOE", "MKTX",
    # Brokerage and consumer finance
    "SCHW", "ALLY", "RJF", "AMTD", "LPL",
    # Payments and fintech
    "V", "MA", "AXP", "FIS", "FISV", "GPN", "PYPL", "SQ", "WEX",
    # Insurance
    "MET", "PRU", "AIG", "AFL", "CB", "HIG", "TRV", "ALL", "LNC",
    # Specialty finance
    "SLM", "OMF", "CACC", "ELVT", "WRLD",
    # Large regionals with active real estate filings
    "WAL", "EWBC", "COLB", "UMBF", "SNV", "NYCB", "ABCB",
    "HOMB", "IBTX", "TCBI", "GBCI", "FFBC", "IBOC", "CATY",
    # Smaller community banks — frequent branch 8-K filers
    "LKFN", "GABC", "SRCE", "BUSE", "SBCF", "FBNC", "TRST",
    "CHCO", "BSVN", "CFFI", "MOFG", "PPBI", "WABC", "TFSL",
    # Specialty/consumer finance
    "NAVI", "ENVA",
    "NKSH", "UNTY", "FMCB", "AROW", "AMTB", "FSEA", "FUNC",
    "CZWI", "EFSC", "FNWB", "HBT", "SBSI", "SFBC", "CNOB",
    "AUB", "SSB", "KRNY", "FRST", "BANR", "RM",
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
    # Corporate real estate
    '"headquarters relocation"',
    '"relocate its headquarters"',
    '"new headquarters"',
    '"lease termination"',
    '"office relocation"',
    # Capital-markets infrastructure
    '"trading floor"',
    '"matching engine"',
    '"exchange floor"',
    # Consolidation
    '"footprint reduction"',
    '"consolidate operations"',
    '"office consolidation"',
    # Expansion
    '"expanded presence"',
    '"new office"',
    # Facility types
    '"technology center"',
    '"innovation center"',
    '"service center"',
    '"processing center"',
    '"financial center"',
    '"new facility"',
    # Lease and real estate actions
    '"entered into a lease"',
    '"signed a lease"',
    '"office space"',
    '"square feet"',
    '"corporate campus"',
    '"relocated its office"',
    '"new corporate headquarters"',
    '"principal offices"',
    '"executive offices"',
    '"change of address"',
    # Branch network language
    '"branch network"',
    '"retail banking"',
    '"banking center"',
    '"financial center opening"',
    '"de novo branch"',
    '"branch acquisition"',
    '"branch sale"',
    '"banking locations"',
    '"branch locations"',
    '"banking offices"',
    # Workforce / facility consolidation
    '"reduce its real estate"',
    '"office space reduction"',
    '"facility consolidation"',
    '"workforce consolidation"',
    '"shared services center"',
    '"captive center"',
    '"back office"',
    '"middle office"',
    # Announcement-style phrases — signal actual events, not boilerplate
    '"proud to announce"',
    '"pleased to announce"',
    '"officially opened"',
    '"grand opening"',
    '"ribbon cutting"',
    '"will relocate"',
    '"has relocated"',
    '"is relocating"',
    '"will open"',
    '"has opened"',
    '"will close"',
    '"has closed"',
    '"new location at"',
    '"moving to"',
    '"moved to"',
    '"new branch opening"',
    '"branch grand opening"',
    '"opened its doors"',
    '"open for business"',
]

# ──────────────────────────────────────────────────────────────────────────
#  Travel and Hospitality (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────
TRAVEL_HOSPITALITY_TICKERS = [
    # Hotel brands
    "MAR", "HLT", "H", "CHH", "WH", "IHG",
    "PK", "HST", "RHP", "SHO", "PEB", "APLE", "DRH",
    "XHR", "CLDT","VAC", "TNL", "HGV", "PLYA", "SOND",
    # Cruise
    "CCL", "RCL", "NCLH",
    "VIK", "ACEL",
    # Airlines
    "DAL", "UAL", "AAL", "LUV", "JBLU", "ALK", "ULCC",
    "SKYW", "SNCY", "HA", "MESA", "ATSG", "JOBY",  "ACHR", "BBY", "RJET",
    # Online travel / booking
    "BKNG", "EXPE", "TRIP", "ABNB", "VACQ", "TRVG", "MMYT",
    # Casino / Resorts
    "MGM", "LVS", "WYNN", "CZR", "PENN", "FUN",
    "BYD", "MLCO", "AGS", "SGMS", "CHDN", "DKNG",
    "RSI", "GDEN", "FULL",
    # Theme parks / attractions 
    "DIS", "SIX", "SEAS", "PLBY", "EPR", "CNK",  
    # Car rental / ground transportation 
    "HTZ", "CAR", "UBER", "LYFT",
    "BLDE", "WKHS", 
]

TRAVEL_HOSPITALITY_PHRASES = [
    # Hotels 
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"hotel franchise"',
    '"resort expansion"',
    '"new resort"',
    '"hotel acquisition"',
    '"property acquisition"',
    '"new full-service"',
    '"new select-service"',
    '"new boutique"',           
    '"all-inclusive resort"',   
    '"vacation club"',          
    '"new timeshare"',          
    '"luxury hotel"',           
    '"new inn"',                
    '"extended stay"',         
    # Airlines
    '"new route"',
    '"new gateway"',
    '"new terminal"',
    '"new nonstop"',
    '"new lounge"',
    '"new service"',
    '"new flight"',
    '"new hub"',
    '"new concourse"',          
    '"new maintenance"',        
    '"new crew base"',          
    '"new training center"',    
    # Cruise
    '"new ship"',
    '"port of call"',
    '"new cruise terminal"',
    '"homeport"',
    '"inaugural sailing"',
    '"new itinerary"',
    '"new deployment"',         
    '"new embarkation"',        
    '"private island"',         
    '"new destination"',
    # Casino / gaming
    '"casino opening"',
    '"grand opening"',
]
# ─────────────────────────────────────────────────────────────────────────────
# Retail (added by Jenna: 20 companies across nine sub-segments)
# ─────────────────────────────────────────────────────────────────────────────

RETAIL_TICKERS = [
    # Big-box / general merchandise
    "WMT", "TGT", "COST",
    # Home improvement
    "HD", "LOW",
    # Off-price / discount / dollar
    "TJX", "ROST", "DG", "DLTR",
    # Drug stores
    "WBA", "CVS",
    # Specialty
    "BBY", "GPS",
    # Grocery
    "KR",
    # Additional sub-segments (extended by Jenna)
    # Department stores
    "M", "KSS",
    # Off-price extension
    "BURL",
    # Beauty specialty
    "ULTA",
    # Discount specialty
    "FIVE",
    # Auto retail
    "AAP",
    # Round 3 additions
    # Apparel / fashion
    "AEO", "URBN", "ANF", "LULU", "PLCE", "CRI", "GES", "EXPR", "BKE",
    "ZUMZ", "CAL", "FL", "GCO", "DBI", "JWN", "PVH", "RL", "VFC",
    "TPR", "CPRI", "LEVI", "FIGS",
    # Pet retail
    "CHWY", "PETQ", "WOOF",
    # Office / business supplies
    "ODP",
    # Furniture / home
    "W", "RH", "WSM", "ETD", "LZB", "ARHS", "HVT",
    # E-commerce / online
    "AMZN", "EBAY", "ETSY", "OSTK",
    # Sporting / outdoor / hobby
    "DKS", "ASO", "HIBB", "BOOT", "VSTO",
    # Convenience / wholesale
    "CASY", "BJ",
    # Auto parts
    "ORLY", "AZO",
    # Beauty / personal care
    "SBH", "ELF", "COTY",
    # Discount / closeout
    "OLLI", "BIG", "PSMT",
    # Mattress / specialty home
    "TPX", "SNBR", "PRPL",
    # Crafts / hobby
    "MIK",
    # Vitamins / health
    "GNC", "VSI",
    # Jewelry
    "SIG", "TIF",
    # Toys
    "FNKO",
    # Grocery extension
    "SFM", "ACI", "WMK", "GO",
    # Drug store extension
    "RAD",
    # Convenience / fuel retail
    "MUSA",
]

RETAIL_PHRASES = [
    # Store openings
    '"new store"',
    '"store opening"',
    '"grand opening"',
    '"flagship store"',
    # Store closings / consolidation
    '"store closure"',
    '"store closing"',
    '"store closures"',
    '"store consolidation"',
    # Distribution / supply chain real estate
    '"distribution center"',
    '"fulfillment center"',
    # Additional phrases (extended by Jenna)
    '"new location"',
    '"warehouse opening"',
    '"distribution facility"',
    '"store relocation"',
    '"new format"',
    '"omnichannel hub"',
    # Round 3 additions
    '"opened a new"',
    '"announced the opening"',
    '"plans to open"',
    '"plans to close"',
    '"to close"',
    '"will close"',
    '"announced the closure"',
    '"closing stores"',
    '"closure of"',
    '"new outlet"',
    '"new market"',
    '"market entry"',
    '"market expansion"',
    '"first store"',
    '"open its first"',
    '"opening of"',
    '"expanding"',
    '"expansion"',
    '"closing"',
    '"opening"',
    '"new facility"',
    '"facility opening"',
    '"facility closure"',
    '"new corporate office"',
    '"new headquarters"',
    '"headquarters relocation"',
    '"office relocation"',
    '"branch"',
    '"new branch"',
    '"showroom"',
    '"new showroom"',
    '"new club"',
    '"club opening"',
    '"prototype store"',
    '"concept store"',
    '"pilot store"',
    '"pop-up store"',
    '"pop-up shop"',
    '"store remodel"',
    '"remodeled store"',
    '"new market launch"',
    '"launch"',
    '"opened"',
    '"closed"',
    '"acquisition of"',
    '"divestiture"',
    '"sale-leaseback"',
    '"real estate"',
    '"property acquisition"',
    '"lease termination"',
    '"facility consolidation"',
    '"network optimization"',
    '"footprint reduction"',
    '"footprint expansion"',
    '"new region"',
    '"regional expansion"',
    '"international expansion"',
    '"new country"',
    '"new state"',
    '"new city"',
]