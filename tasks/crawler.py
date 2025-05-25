# tasks/crawler.py
import requests
from bs4 import BeautifulSoup
from pytrends.request import TrendReq

def get_google_trends():
    pytrends = TrendReq(hl='zh-TW', tz=540)
    pytrends.build_payload(kw_list=["新聞"])
    trending = pytrends.trending_searches(pn='taiwan')
    topics = trending[0].tolist()[:4]
    return [f"Google 熱門：{t}" for t in topics]

def get_dcard_hot():
    url = "https://www.dcard.tw/service/api/v2/posts?popular=true&limit=10"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = res.json()
    return [f"Dcard 熱門：{item['title']}" for item in data[:3]]

def get_ptt_gossiping():
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"
    cookies = {"over18": "1"}
    res = requests.get(url, cookies=cookies, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.select("div.title a")
    return [f"PTT 熱門：{a.text.strip()}" for a in titles[:3]]

def get_hot_topics():
    result = []
    try:
        result.extend(get_ptt_gossiping())
    except Exception as e:
        result.append(f"[PTT 擷取失敗] {e}")
    try:
        result.extend(get_dcard_hot())
    except Exception as e:
        result.append(f"[Dcard 擷取失敗] {e}")
    try:
        result.extend(get_google_trends())
    except Exception as e:
        result.append(f"[Google Trends 擷取失敗] {e}")
    return result[:10]