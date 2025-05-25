# tasks/task_a.py
from tasks.crawler import get_hot_topics

def run(event):
    try:
        topics = get_hot_topics()
        if not topics:
            return "[⚠️ 無熱門話題] 抓取結果為空"
        return "\n".join([f"{i+1}. {t}" for i, t in enumerate(topics)])
    except Exception as e:
        return f"[task_a 錯誤] {e}"