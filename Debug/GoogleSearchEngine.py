import requests
def func(query):
    API_KEY = "AIzaSyDIFRgKoflTcq2u7lCR06DE2lKsxbvjA84"

    SEARCH_ENGINE_ID = "0bd6f53696ce27097"


    page = 1

    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    data = requests.get(url).json()

    search_items = data.get("items")

    for i, search_item in enumerate(search_items, start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        
        # alternatively, you can get the HTML snippet (bolded keywords)
        html_snippet = search_item.get("htmlSnippet")
        link = search_item.get("link")
        
        # result = "="*10, f"Result #{i+start-1}", "="*10)
        # title ="Title:", title
        description = "Description:", snippet
        # url = "URL:", link, "\n"
        
        return description
