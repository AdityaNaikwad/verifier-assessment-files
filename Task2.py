from playwright.sync_api import sync_playwright
from typing import Dict, Any


def verify_taj_mahal_page(url: str) -> Dict[str, Any]:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=10000)
            try:
                title = page.locator("h1#firstHeading").inner_text()
            except Exception:
                browser.close()
                return {
                    "success": False,
                    "reason": "Title element not found",
                    "evidence": {}
                }

            # Extract Location from infobox
            location_value = None

            rows = page.locator(".infobox tr")
            count = rows.count()

            for i in range(count):
                row = rows.nth(i)
                header = row.locator("th")

                if header.count() > 0:
                    header_text = header.inner_text().strip().lower()
                    if "location" in header_text:
                        location_cell = row.locator("td")
                        if location_cell.count() > 0:
                            location_value = location_cell.inner_text()
                        break

            browser.close()

            # Validate constraints
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
                    "extractedLocation": location_value,
                    "selectors": {
                        "title": "h1#firstHeading",
                        "location": ".infobox tr → th contains 'Location' → td"
                    }
                }
            }

    except Exception as e:
        return {
            "success": False,
            "reason": f"Failed to load page: {str(e)}",
            "evidence": {}
        }


if __name__ == "__main__":
    input_url = input("Enter Wikipedia URL: ").strip()

    if not input_url:
        print("No URL provided.")
    else:
        result = verify_taj_mahal_page(input_url)
        print(result)


