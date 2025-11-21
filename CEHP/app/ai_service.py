# app/ai_service.py

import os
import yaml
from openai import OpenAI

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INFO_PATH = os.path.join(BASE_DIR, "info.yaml")


def load_config():
    with open(INFO_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def initialize_client() -> OpenAI:
    cfg_all = load_config()
    api_cfg = cfg_all.get("api_config", {})

    client = OpenAI(
        api_key=api_cfg.get("api_key", ""),
        base_url=api_cfg.get("base_url", "")
    )
    return client


def chat_with_ai_simple(message: str) -> str:
    """
    输入用户一句话，返回助手回复（不管上下文，只做单轮，够用就行）。
    你后面要加多轮记忆，可以在这里扩展。
    """
    cfg_all = load_config()
    model_cfg = cfg_all.get("model_config", {})

    system_prompt = model_cfg.get(
        "system_prompt",
        "你是一个智能健康助手，熟悉常见药品与疾病知识，但不能替代医生诊断。"
    )
    model_name = model_cfg.get("model", "gpt-3.5-turbo")
    temperature = model_cfg.get("temperature", 0.7)

    client = initialize_client()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message},
    ]

    # 这里用流式接口，手动拼接内容
    full_resp = ""
    completion = client.chat.completions.create(
        model=model_name,
        temperature=temperature,
        messages=messages,
        stream=True,
    )
    for chunk in completion:
        delta = chunk.choices[0].delta
        if getattr(delta, "content", None):
            full_resp += delta.content

    return full_resp
