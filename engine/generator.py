# engine/generator.py

import os
import asyncio

from openai import OpenAI

OPENAI_API_KEY = "sk-f8bc4b9248224d7c9a8de15db033ab53"
# 使用deepseek接口构建模型客户端

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.deepseek.com"
)

async def generate_response(name:str, prompt:str) -> str:
    """
    调用 Deepseekchat生成指定角色的对话内容
    """
    try:
        response = await asyncio.to_thread(client.chat.completions.create,
            model="deepseek-chat",
            messages=[
                {"role":"system","content": f"你是剧本角色 {name}，需要以该身份进行回应"},
                {"role":"user","content": prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] 生成失败：{str(e)}"
        