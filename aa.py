import requests

def fetch_data_from_api():
    url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None

def identify_citations(data):
    citations = []
    for item in data:
        response = item.get("response", "")
        sources = item.get("sources", [])
        for source in sources:
            if source["context"] in response:
                citations.append({"id": source["id"], "link": source.get("link", "")})
    return citations

def main():
    data = fetch_data_from_api()
    if data:
        citations = identify_citations(data)
        print("Citations:", citations)

if __name__ == "__main__":
    main()
