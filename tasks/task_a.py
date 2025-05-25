# task_a.py
from crawler import get_hot_topics
import json

if __name__ == "__main__":
    try:
        topics = get_hot_topics()
        print(json.dumps(topics, ensure_ascii=False))
    except Exception as e:
        print(json.dumps(["[task_a 錯誤] 無法擷取熱門話題", str(e)]))
