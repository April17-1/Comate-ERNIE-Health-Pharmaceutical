# app/db.py

import pymongo
from flask import current_app

client = None
collection = None


def init_db(app):
    global client, collection
    host = app.config["MONGO_HOST"]
    port = app.config["MONGO_PORT"]
    db_name = app.config["MONGO_DB_NAME"]
    col_name = app.config["MONGO_COLLECTION_NAME"]

    client = pymongo.MongoClient(host=host, port=port)
    db = client[db_name]
    collection = db[col_name]


def get_collection():
    """在业务代码中统一通过这个函数拿 collection。"""
    global collection
    if collection is None:
        # 保险起见
        raise RuntimeError("Mongo collection not initialized")
    return collection
