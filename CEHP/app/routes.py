# app/routes.py

from flask import Blueprint, render_template, request, jsonify
from .search_service import perform_search
from .utils import save_table_json
from .ai_service import chat_with_ai_simple
# routes.py 顶部增加：
from .db import get_collection
from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    # 主页面：药品搜索 + 结果表格 + 文心助手入口
    return render_template("index.html")

@main_bp.route("/search", methods=["GET"])
def handle_search():
    # 药品模糊搜索
    query = (request.args.get("query") or "").strip()
    if query:
        results = perform_search(query)
        save_table_json(results)
    # 仍然返回 index.html，前端表格会重新加载 JSON
    return render_template("index.html")


@main_bp.route("/chat_embed")
def chat_embed():
    """
    文心健康助手嵌入页：在主页面的 iframe 里展示。
    对应模板：templates/chat_embed.html
    """
    return render_template("chat_embed.html")


@main_bp.route("/chat", methods=["POST"])
def chat_api():
    """
    给前端 JS 用的聊天接口。
    chat_embed.html 里用 fetch('/chat', {method:'POST', body: JSON.stringify({message: ...})})
    """
    data = request.get_json(force=True) or {}
    msg = (data.get("message") or "").strip()

    if not msg:
        return jsonify({"reply": "请先输入问题"}), 200

    try:
        reply = chat_with_ai_simple(msg)
    except Exception as e:
        # 线上可以改成日志，这里直接返回错误信息方便调试
        reply = f"调用大模型出错：{e}"

    return jsonify({"reply": reply})

@main_bp.route("/drug_detail")
def drug_detail():
    name = (request.args.get("name") or "").strip()
    if not name:
        return jsonify({"status": 400, "message": "缺少药品名称参数 name"}), 400

    collection = get_collection()
    doc = collection.find_one({"药品名称": name}, {"_id": 0})  # 去掉 _id

    if not doc:
        return jsonify({"status": 404, "message": f"未找到药品：{name}"}), 404

    return jsonify({"status": 200, "data": doc})


@main_bp.route("/免责声明")
def disclaimer():
    return render_template("免责声明.html")


@main_bp.route("/官方文档")
def docs():
    return render_template("官方文档.html")
