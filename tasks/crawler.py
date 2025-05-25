# tasks/crawler.py
import requests
from bs4 import BeautifulSoup

def get_ptt_hot():
    url = "https://www.ptt.cc/bbs/hotboards.html"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("div.b-ent a.board")
    return [f"PTT 熱門：{item.text.strip()}" for item in items[:3]]

def get_dcard_hot():
    url = "https://www.dcard.tw/f"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.select("h2.sc-1v1d5rx-3")
    return [f"Dcard 熱門：{a.text.strip()}" for a in articles[:3]]

def get_google_trends():
    url = "https://trends.google.com/trends/trendingsearches/daily?geo=TW"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    scripts = soup.find_all("script")
    data = ""
    for script in scripts:
        if "trendingSearchesDays" in script.text:
            data = script.text
            break
    import re
    items = re.findall(r'"title":{"query":"(.*?)"', data)
    return [f"Google 熱門：{t}" for t in items[:4]]

def get_hot_topics():
    result = []
    try:
        result.extend(get_ptt_hot())
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