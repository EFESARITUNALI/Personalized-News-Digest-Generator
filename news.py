import requests
from datetime import datetime, timedelta
from config import NEWS_API_KEY
from newspaper import Article

def fetch_news(interests):
    base_url = 'https://newsapi.org/v2/everything'
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    params = {
        'q': ' OR '.join(interests),
        'language': 'en',
        'from': from_date,
        'apiKey': NEWS_API_KEY
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print("Failed to fetch news:", response.text)
        return []
    
def get_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text