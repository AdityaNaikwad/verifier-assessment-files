from playwright.sync_api import sync_playwright
from typing import Dict, Any


def verify_taj_mahal_page(url: str) -> Dict[str, Any]:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=10000)

            title = page.locator("h1#firstHeading").inner_text()

            location_value = None
            rows = page.locator(".infobox tr")
            count = rows.count()

            for i in range(count):
                row = rows.nth(i)
                header = row.locator("th")

                if header.count() > 0:
                    header_text = header.inner_text().strip().lower()
                    if "location" in header_text:
                        td = row.locator("td")
                        if td.count() > 0:
                            location_value = td.inner_text()
                        break

            browser.close()

            violations = []

            if "taj mahal" not in title.lower():
                violations.append("title")

            if not location_value or "agra" not in location_value.lower():
                violations.append("location")

            if violations:
                return {
                    "success": False,
                    "reason": f"Constraint violations: {violations}",
                    "evidence": {
                        "pageTitle": title,
                        "extractedLocation": location_value
                    }
                }

            return {
                "success": True,
                "reason": "Page title and location satisfy constraints",
                "evidence": {
                    "pageTitle": title,
                    "extractedLocation": location_value
                }
            }

    except Exception as e:
        return {
            "success": False,
            "reason": f"Failed to load page: {str(e)}",
            "evidence": {}
        }
