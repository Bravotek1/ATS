"""ATS 範例套件。

此模組僅用於展示 mkdocstrings 會如何擷取 docstring。請在實際專案中移除此檔案。
"""

def run_test(config: dict) -> bool:
    """執行一次自動測試流程。

    Args:
        config (dict): 測試設定，例如儀器連線、測項清單。

    Returns:
        bool: 成功回傳 True，失敗回傳 False。
    """
    return True
