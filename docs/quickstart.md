# 快速開始

<<<<<<< HEAD
## 安裝
```bash
# 依專案實際需要
python -m venv .venv
. .venv/Scripts/activate  # Windows
pip install -r requirements.txt  # 若專案有提供
```

## 執行
```bash
python path/to/your_entry.py
```

## 文件本地預覽
```bash
pip install mkdocs mkdocs-material
mkdocs serve  # http://127.0.0.1:8000
```
=======
## 本地預覽文件
```bash
pip install mkdocs mkdocs-material "mkdocstrings[python]"
mkdocs serve  # http://127.0.0.1:8000
```

## 專案安裝（範例，依實際調整）
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows
pip install -r requirements.txt
python -m ats   # 例如有 __main__.py
```

## 撰寫文件
- 在 `docs/` 新增 `.md` 檔即可擴充導覽。
- 在原始碼的 **函式/類別** docstring 填寫說明，API 頁會自動帶入。
>>>>>>> V0.0
