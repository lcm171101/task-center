# tasks/crawler.py
import requests
from bs4 import BeautifulSoup

def get_google_trends_html():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily?geo=TW"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        titles = soup.select("div.feed-item div.details-top a.title")
        return [f"Google 熱門：{t.text.strip()}" for t in titles[:4]]
    except Exception as e:
        return [f"[Google Trends 擷取失敗] {e}"]

def get_dcard_hot_html():
    try:
        url = "https://www.dcard.tw/f"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        titles = soup.find_all("h2")
        hot = [t.text.strip() for t in titles if 5 < len(t.text.strip()) < 100]
        return [f"Dcard 熱門：{t}" for t in hot[:3]]
    except Exception as e:
        return [f"[Dcard 擷取失敗] {e}"]

def get_ptt_gossiping():
    try:
        url = "https://www.ptt.cc/bbs/Gossiping/index.html"
        cookies = {"over18": "1"}
        res = requests.get(url, cookies=cookies, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        titles = soup.select("div.title a")
        return [f"PTT 熱門：{a.text.strip()}" for a in titles[:3]]
    except Exception as e:
        return [f"[PTT 擷取失敗] {e}"]

def get_hot_topics():
    result = []
    result.extend(get_ptt_gossiping())
    result.extend(get_dcard_hot_html())
    result.extend(get_google_trends_html())
    return result[:10]