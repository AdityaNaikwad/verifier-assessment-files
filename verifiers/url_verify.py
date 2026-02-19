from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any


def parse_search_tokens(url: str) -> Dict[str, Any]:
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    raw_q = query_params.get("q", [])
    if not raw_q:
        return {}

    tokens = unquote(raw_q[0]).lower().split()

    structured = {}

    for token in tokens:
        token = token.strip()
        if ":" not in token:
            continue

        key, value = token.split(":", 1)

        # Handle multiple 'is:' tokens (issue + open)
        if key == "is":
            structured.setdefault("is", []).append(value)
        else:
            structured[key] = value

    return structured


def verify_search(url: str, constraints: Dict[str, str]) -> Dict[str, Any]:
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)

        # Validate type parameter
        actual_type = query_params.get("type", [""])[0].lower()
        required_type = constraints["type"].lower()

        if actual_type != required_type:
            return {
                "success": False,
                "reason": f"type mismatch: expected '{required_type}', got '{actual_type}'",
                "evidence": {"actualType": actual_type}
            }

        structured = parse_search_tokens(url)

        violations = []

        # Repo check
        if structured.get("repo") != constraints["repo"].lower():
            violations.append("repo")

        # is:issue check
        if "is" not in structured or "issue" not in structured["is"]:
            violations.append("is:issue")

        # state check (is:open)
        if "is" not in structured or constraints["state"].lower() not in structured["is"]:
            violations.append(f"is:{constraints['state']}")

        # label check
        if structured.get("label") != constraints["label"].lower():
            violations.append("label")

        if violations:
            return {
                "success": False,
                "reason": f"Missing or incorrect constraints: {violations}",
                "evidence": structured
            }

        return {
            "success": True,
            "reason": "All constraints satisfied",
            "evidence": structured
        }

    except Exception as e:
        return {
            "success": False,
            "reason": f"Failed to parse URL: {str(e)}",
            "evidence": {}
        }
