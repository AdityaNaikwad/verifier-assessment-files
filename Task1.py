from verifiers.url_verify import verify_search
if __name__ == "__main__":
    constraints = {
        "repo": "microsoft/playwright",
        "type": "issues",
        "state": "open",
        "label": "bug"
    }

    test_url = "https://github.com/search?q=repo%3Amicrosoft%2Fplaywright+is%3Aissue+is%3Aopen+label%3Abug&type=issues"

    result = verify_search(test_url, constraints)
    print(result)
