## 🧪 Web Verifier Take-Home Assessment
 A structured verification system that:
- 🔎 Validates GitHub issue search URLs
- 🌐 Verifies live DOM state from Wikipedia
- 📄 Validates static HTML snapshots (no network)
- 📊 Returns structured evidence (not just pass/fail)

## 🧰 Tech Stack:-
- Python 3.10+
- urllib.parse
- playwright
- beautifulsoup4

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/web-verifier-takehome.git
cd web-verifier-takehome
```
---
### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
---
### 3. Install Requirements

```bash
pip install -r requirements.txt
```
---
### 4. Install Playwright Browser
```bash
playwright install
```
---

## 🔎 Task 1 — URL Verifier
- File: `verifiers/url_verifier.py`
Runner: `Task1.py`
- Goal
   Verify that a GitHub issue search URL satisfies:
    - repo = microsoft/playwright
    - type = issues
    - state = open
    - label = bug

# How to Use
Call the function:
-   `verify_github_issue_search(url, constraints)`


Returns:
```bash
{
  "success": true,
  "reason": "All constraints satisfied",
  "evidence": {
    "repo": "microsoft/playwright",
    "is": ["issue", "open"],
    "label": "bug"
  }
```
---

## 🌐 Task 2 — DOM Verifier (Live Page)

- Logic File: `verifiers/wikipedia_verifier.py`
- Runner: `task2.py`
# Goal
From:
`https://en.wikipedia.org/wiki/Taj_Mahal`

- Verify:
  Page title contains "Taj Mahal"
  Infobox location contains "Agra"

# ▶ Run
```bash
python task2.py
Enter URL when prompted.
```
---

## 📄 Task 3 — Snapshot DOM Verifier (No Network)

- Logic File: `verifiers/snapshot_verifier.py`
- Runner: `task3.py`

- Goal
  From snapshot HTML:
  - Price ≤ 3000
  - City = "Pune"
  - Bedrooms = 2
# ▶ Run
```bash
python task3.py
Enter snapshot file path when prompted.
```
# Failures return:
```bash
{
  "success": false,
  "reason": "Clear explanation",
  "evidence": {}
}
```
---

```bash
📂 Project Structure
web-verifier-takehome/
│
├── verifiers/
│   ├── url_verifier.py
│   ├── wikipedia_verifier.py
│   └── snapshot_verifier.py
│
├── task2.py
├── task3.py
├── requirements.txt
└── README.md
```