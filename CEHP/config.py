# config.py

class Config:
    # Mongo 配置
    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DB_NAME = "medicine"
    MONGO_COLLECTION_NAME = "data"

    # JSON 文件路径（相对项目根目录）
    TABLE_JSON_PATH = r"static/json/2/table/demo3.json"
