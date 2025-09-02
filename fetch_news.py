import requests
from config import get_mongo_connection

def fetch_finance_news():
    print("📰 Fetching finance news headlines...")

    # Example free API endpoint (replace with real API key if needed)
    url = "https://newsapi.org/v2/top-headlines?category=business&apiKey=demo"  # Replace demo with your key
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch news.")
        return

    articles = response.json().get("articles", [])
    if not articles:
        print("No news articles found.")
        return

    db = get_mongo_connection()
    if db is None:
        return


    collection = db["news"]

    for article in articles:
        doc = {
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "publishedAt": article.get("publishedAt"),
            "url": article.get("url")
        }
        collection.update_one(
            {"url": doc["url"]}, {"$set": doc}, upsert=True
        )
    print("News headlines inserted/updated.")
