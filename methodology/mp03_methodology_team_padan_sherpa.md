# Methodology: Corporate Facility Event Extraction and Mapping

This document outlines the systematic approach used to identify, extract, analyze, and visualize corporate facility changes (openings, closings, relocations, and expansions) from SEC 8-K filings.

## 1. Data Acquisition
The pipeline begins by querying the **SEC EDGAR Electronic Filing Text Search (EFTS) API**.
- **Source**: SEC EDGAR 8-K filings.
- **Search Parameters**: A 30-day lookback window from the current date.
- **Industry Targeting**: The search is partitioned into two primary sectors using specific keyword phrases:
    - **Financial Services**: Keywords include "new branch", "branch closure", "wealth management office", etc.
    - **Travel & Hospitality**: Keywords include "new property", "hotel opening", "new route", etc.
- **Pagination**: The script retrieves up to 200 hits per phrase to ensure a broad sample size.

## 2. Text Extraction & Cleaning
For every search hit identified:
- The system constructs a direct URL to the SEC filing exhibit.
- **BeautifulSoup4** is utilized to download the HTML content and strip tags, leaving only the primary text.
- To manage computational efficiency and API token limits, the text is truncated to the first 8,000 characters.

## 3. Structured AI Analysis
The raw text is processed by the **Anthropic Claude (Haiku)** LLM to transform unstructured prose into structured data.
- **System Prompting**: Claude is configured as a strict analyst looking for specific facility events while ignoring boilerplate language.
- **Schema Enforcement**: The model returns a JSON object containing:
    - `is_location_event`: Boolean filter.
    - `event_type`: Categorization (opening, closing, relocation, expansion, other).
    - `city/state`: Geographic identifiers.
    - `summary`: A concise (<25 words) description of the event.

## 4. Geocoding
To enable spatial visualization, the extracted city and state names are converted into geographic coordinates.
- **Provider**: OpenStreetMap **Nominatim API**.
- **Rate Limiting**: A 1.1-second pause is implemented between requests to comply with OSM’s usage policy.
- **Fallback**: Events that cannot be successfully geocoded are logged but excluded from the final map.

## 5. Visualization
The final stage uses **Folium** (a Python wrapper for Leaflet.js) to create an interactive map.
- **Color Coding**: 
    - `Green`: Openings
    - `Red`: Closings
    - `Blue`: Expansions
    - `Orange`: Relocations
- **Iconography**: FontAwesome icons differentiate industries (e.g., a "university" icon for banks and a "bed" icon for hospitality).
- **Interactivity**: Each marker includes a popup with a deep link to the original SEC filing, a summary of the event, and company ticker information.
