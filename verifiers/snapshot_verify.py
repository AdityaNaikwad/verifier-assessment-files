from bs4 import BeautifulSoup
from typing import Dict, Any


def verify_from_html(html_string: str, constraints: Dict[str, Any]) -> Dict[str, Any]:
    try:
        soup = BeautifulSoup(html_string, "html.parser")

        price_element = soup.select_one("[data-price]")
        city_element = soup.select_one("[data-city]")
        bedrooms_element = soup.select_one("[data-bedrooms]")

        if not price_element or not city_element or not bedrooms_element:
            return {
                "success": False,
                "reason": "Missing required elements in HTML",
                "evidence": {}
            }

        price = int(price_element["data-price"])
        city = city_element["data-city"]
        bedrooms = int(bedrooms_element["data-bedrooms"])

        violations = []

        if price > constraints["max_price"]:
            violations.append("price")

        if city.lower() != constraints["city"].lower():
            violations.append("city")

        if bedrooms != constraints["bedrooms"]:
            violations.append("bedrooms")

        if violations:
            return {
                "success": False,
                "reason": f"Constraint violations: {violations}",
                "evidence": {
                    "price": price,
                    "city": city,
                    "bedrooms": bedrooms,
                    "violations": violations
                }
            }

        return {
            "success": True,
            "reason": "All constraints satisfied",
            "evidence": {
                "price": price,
                "city": city,
                "bedrooms": bedrooms
            }
        }

    except Exception as e:
        return {
            "success": False,
            "reason": f"Failed to parse HTML: {str(e)}",
            "evidence": {}
        }
