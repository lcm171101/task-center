# 專案 B：任務 API 中心 + Web UI 管理系統

本專案負責處理所有任務邏輯，供外部如 LINE Bot Proxy 呼叫任務 API。  
同時提供 Web 管理介面供人工操作與設定。

---

## 🧠 功能總覽

- ✅ 提供 `/api/execute_task` 任務執行 API
- ✅ 可透過 `tasks/task_x.py` 模組擴充任務
- ✅ 支援 Firestore 日誌紀錄與過期自動清除
- ✅ 提供完整任務管理 Web UI

---

## 📁 專案資料夾結構

```
專案資料夾/
├── app_ui.py                    # 主程式
├── firestore_utils_lazy_env.py # Firestore 工具
├── /tasks                       # 任務模組（如 task_b.py）
├── /templates                   # 管理 UI 頁面
│   ├── index.html
│   ├── task_registry.html
│   ├── add_keyword.html
│   ├── edit_description.html
│   ├── manage.html
│   └── task_table.html
├── requirements.txt             # 套件需求
```

---

## 🔐 環境變數設定

| 名稱 | 說明 |
|------|------|
| `FIREBASE_KEY` | base64 編碼的 Firebase Admin SDK JSON 金鑰 |

---

## 🔧 主要 API 路由

| 路徑 | 方法 | 說明 |
|------|------|------|
| `/api/execute_task` | POST | 接收任務名稱並執行對應模組，如 `tasks/task_b.py` |
| `/delete_expired_logs` | GET | 手動清除 Firestore 中已過期（超過 60 天）的紀錄 |

---

## 🌐 管理頁面路由

| 路徑 | 功能 |
|------|------|
| `/` | 導覽首頁 |
| `/task_registry` | 查詢所有任務與關鍵字說明 |
| `/add_keyword` | 新增任務與模組 |
| `/edit_description` | 編輯任務說明 |
| `/manage` | 刪除任務 / 匯出記錄 |
| `/tasks` | 保護內部路由，禁止存取 |
| `/export_logs` | 匯出 logs CSV |
| `/delete_expired_logs` | 清除 60 天前的 logs |

---

## 📬 API 呼叫範例（for 專案 A）

```json
POST /api/execute_task
{
  "task": "任務B",
  "source_id": "U12345678",
  "source_type": "user",
  "original_text": "#任務B"
}
```

---

## 📝 Firestore 紀錄格式

每次任務成功或失敗都會記錄至 `logs` 集合：

```json
{
  "timestamp": "2025-05-24 21:50:00",
  "task": "任務B",
  "source_id": "Uxxxx",
  "source_type": "user",
  "message": "#任務B",
  "result": "✅ 任務B 執行成功",
  "expiry": "2025-07-23"
}
```

---

## 🧱 任務模組說明

所有任務對應的模組放在 `tasks/` 目錄下，命名為 `task_x.py`  
每個模組需包含以下函式：

```python
def run(event):
    return "任務執行結果"
```

---

## 🔧 套件需求

- `flask`
- `firebase-admin`
- `gunicorn`

---

## ✅ 可擴充方向

- [ ] 加入登入驗證系統
- [ ] 支援任務分類與狀態標籤
- [ ] 圖表統計與每日分析報表
