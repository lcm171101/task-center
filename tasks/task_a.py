# tasks/task_a.py
from crawler import get_hot_topics
import json

def run(event):
    try:
        topics = get_hot_topics()
        return "\n".join([f"{i+1}. {t}" for i, t in enumerate(topics)])
    except Exception as e:
        return f"[task_a 錯誤] 無法擷取熱門話題：{e}"