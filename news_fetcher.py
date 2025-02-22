import requests
from config import NEWS_API_KEY

def get_news():
    """Fetches the latest AI market news from NewsAPI."""
    URL = f"https://newsapi.org/v2/everything?q=AI&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(URL)
    data = response.json()
    
    if data.get("status") != "ok":
        print("Error fetching news:", data)
        return []
    
    return [{"title": article["title"], "url": article["url"], "source": article["source"]["name"]}
            for article in data.get("articles", [])]
