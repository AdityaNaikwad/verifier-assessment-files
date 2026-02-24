
from verifiers.snapshot_verify import verify_from_html

if __name__ == "__main__":
    file_path = input("Enter snapshot HTML file path: ").strip()

    constraints = {
        "max_price": 3000,
        "city": "Pune",
        "bedrooms": 2
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        result = verify_from_html(html_content, constraints)
        print(result)

    except Exception as e:
        print({
            "success": False,
            "reason": f"Failed to read file: {str(e)}",
            "evidence": {}
        })
