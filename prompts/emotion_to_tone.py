from openai import OpenAI

client = OpenAI(api_key="sk-f8bc4b9248224d7c9a8de15db033ab53", base_url="https://api.deepseek.com")

def emotion_tone_hint(emotion: str) -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": f"根据'{emotion}'情绪生成语言风格提示词，15字内"}]
        )
        return response.choices[0].message.content.strip()
    except:
        return "中性语气"