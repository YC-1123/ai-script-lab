from openai import OpenAI

client = OpenAI(api_key="sk-f8bc4b9248224d7c9a8de15db033ab53", base_url="https://api.deepseek.com")

def check_phase_trigger(dialogue: str, current_phase: str) -> bool:
    """检查对话是否触发下一阶段"""
    trigger_prompts = {
        "相遇": "判断对话是否出现冲突、争执、分歧等情况，回答是或否",
        "冲突": "判断对话是否出现理解、和解、共鸣等情况，回答是或否",
        "理解": "判断对话是否已达到深度理解，回答是或否"
    }
    
    if current_phase not in trigger_prompts:
        return False
        
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{
                "role": "user", 
                "content": f"{trigger_prompts[current_phase]}：{dialogue}"
            }]
        )
        return "是" in response.choices[0].message.content
    except:
        return False
