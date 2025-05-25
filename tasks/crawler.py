# tasks/crawler.py
import requests
from bs4 import BeautifulSoup

def get_google_trends_rss():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=TW"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "xml")
        items = soup.find_all("item")[:4]
        return [f"{i+1}. Google 熱門：{item.title.text.strip()}" for i, item in enumerate(items)]
    except Exception as e:
        return [f"[Google Trends 擷取失敗] {e}"]

def get_hot_topics():
    return get_google_trends_rss()