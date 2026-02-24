from verifiers.wiki_verify import verify_taj_mahal_page

if __name__ == "__main__":
    input_url = input("Enter Wikipedia URL: ").strip()

    if not input_url:
        print("No URL provided.")
    else:
        result = verify_taj_mahal_page(input_url)
        print(result)


