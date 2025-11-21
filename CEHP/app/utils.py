# app/utils.py

import json
from typing import List
from flask import current_app


import json
import os

def save_table_json(table_data, filename="demo3.json"):
    """
    table_data: List[List[str]]
    每一行形如：
    [药品名称, 处方类型, 用法用量, 适应症, 副作用, 禁忌, 储藏方法, detail_json]
    """
    items = []
    for row in table_data:
        # 不足 8 个字段时用空串补齐，防止下标越界
        row = (row + [""] * 8)[:8]
        name, rx_type, dosage, indication, side, contra, store, detail_json = row

        items.append({
            "药品名称":   name,
            "处方类型":   rx_type,
            "用法用量":   dosage,
            "适应症":     indication,
            "副作用":     side,
            "禁忌":       contra,
            "储藏方法":   store,
            "detail_json": detail_json,   # ✅ 给前端弹窗用
        })

    data = {
        "status": 200,
        "message": "",
        "total": len(items),
        "rows": {
            "item": items
        }
    }

    out_path = os.path.join("static", "json", "2", "table", filename)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



def init_empty_table_json(total: int = 8) -> None:
    """启动时写一个空的表格 JSON。"""
    from flask import current_app

    data = {
        "status": 200,
        "message": "",
        "total": total,
        "rows": {
            "item": [{} for _ in range(total)]
        }
    }
    json_path = current_app.config["TABLE_JSON_PATH"]
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
