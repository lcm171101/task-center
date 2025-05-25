# tasks/crawler.py
import requests
from bs4 import BeautifulSoup
from pytrends.request import TrendReq

def get_google_trends():
    try:
        pytrends = TrendReq(hl='zh-TW', tz=540)
        trending = pytrends.trending_searches(pn='taiwan')  # 修正為 'taiwan'
        topics = trending[0].tolist()[:4]
        return [f"Google 熱門：{t}" for t in topics]
    except Exception as e:
        return [f"[Google Trends 擷取失敗] {e}"]

def get_dcard_hot():
    try:
        url = "https://www.dcard.tw/service/api/v2/posts?popular=true&limit=10"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if res.status_code != 200:
            return [f"[Dcard 擷取失敗] 狀態碼 {res.status_code}"]
        data = res.json()
        return [f"Dcard 熱門：{item['title']}" for item in data[:3]]
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
    result.extend(get_dcard_hot())
    result.extend(get_google_trends())
    return result[:10]