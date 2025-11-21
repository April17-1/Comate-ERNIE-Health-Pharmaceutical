# app/__init__.py

import os
from flask import Flask
from config import Config
from .db import init_db
from .routes import main_bp

# 项目根目录，例如：C:/.../FM
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app(config_class=Config) -> Flask:
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    app.config.from_object(config_class)

    # 初始化 Mongo
    init_db(app)

    # 注册路由蓝图
    app.register_blueprint(main_bp)

    return app
