def run(event):
    from datetime import datetime
    user_id = event.get("source_id", "未知使用者")
    task = event.get("task", "未知任務")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"✅ {task} 執行成功，使用者：{user_id}，時間：{now}"
