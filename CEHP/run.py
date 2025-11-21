# run.py
from app import create_app
from app.utils import init_empty_table_json

app = create_app()

if __name__ == "__main__":
    # 初始化空表格 JSON，保证第一次打开页面不会报错
    with app.app_context():
        init_empty_table_json(total=8)

    app.run(host="0.0.0.0", port=5000)
