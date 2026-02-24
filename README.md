Web Verifier Take-Home Assessment

This repository implements three independent verifiers as required:

Task 1 — URL Verifier

Task 2 — DOM Verifier (Live Page)

Task 3 — Snapshot DOM Verifier (No Network)

Each verifier returns structured output:

{
  "success": true | false,
  "reason": "Explanation of result",
  "evidence": { extracted_data }
}


The output always includes extracted evidence — not just true/false.

Project Structure:-
VERIFIER-ASSESSMENT-FILES/
│
├── verifiers/
│     ├── url_verifier.py
│     ├── wikipedia_verifier.py
│     ├── snapshot_verifier.py
│
├── task2.py
├── task3.py
├── requirements.txt
├── README.md

Installation

Install dependencies:

pip install -r requirements.txt
playwright install

Task 1 — URL Verifier

File:
verifiers/url_verifier.py

Goal

Verify a GitHub issue search URL satisfies:

repo = microsoft/playwright

type = issues

state = open

label = bug

Implementation Details

Uses urllib.parse

Decodes URL encoding

Normalizes tokens (case-insensitive)

Parses search query into structured dictionary

Performs semantic validation (not raw string matching)

Order of tokens does not matter

Extra parameters allowed

Output Includes

Extracted repo

Extracted state tokens

Extracted label

Clear reason for failure if constraints missing

Task 2 — DOM Verifier (Live Wikipedia Page)

Logic File:
verifiers/wikipedia_verifier.py

Runner:
task2.py

Goal

From:

https://en.wikipedia.org/wiki/Taj_Mahal


Verify:

Page title contains "Taj Mahal"

Infobox location contains "Agra" (case-insensitive, partial match allowed)

Implementation Details

Uses Playwright (headless Chromium)

Extracts:

h1#firstHeading for title

Iterates .infobox tr

Matches th containing "Location"

Extracts corresponding td

Avoids brittle nth-child selectors

Defensive handling if elements missing

Graceful network failure handling

Run
python task2.py


Enter the Wikipedia URL when prompted.

Task 3 — Snapshot DOM Verifier (No Network)

Logic File:
verifiers/snapshot_verifier.py

Runner:
task3.py

Goal

From provided snapshot HTML:

Price ≤ 3000

City = "Pune" (case-insensitive)

Bedrooms = 2

Implementation Details

Uses BeautifulSoup

Extracts via data attributes:

[data-price]

[data-city]

[data-bedrooms]

Converts values to correct types

Collects violations explicitly

No network calls

Run
python task3.py


Enter snapshot file path when prompted.

Assumptions Made

URL token order does not matter.

URL encoding variations are normalized.

Extra URL parameters are allowed if required constraints are present.

Wikipedia page structure follows standard infobox layout.

Snapshot HTML uses stable data attributes.

Case-insensitive matching is acceptable for text validation.

Error Handling

All verifiers handle:

Missing elements

Malformed HTML

Network failure

Timeout

File read errors

Failures return:

{
  "success": false,
  "reason": "Clear explanation",
  "evidence": {}
}

Design Decisions

Separation of logic and runner files

Semantic constraint validation

Structured evidence reporting

Defensive DOM traversal

Minimal and relevant dependencies only

Dependencies
playwright
beautifulsoup4

Result

All provided test cases pass/fail as expected.

The implementation prioritizes:

Correctness

Robustness

Clean architecture

Clear evidence extraction