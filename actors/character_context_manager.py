import random
from actors.character_config import CHARACTER_CONFIGS
from prompts.story_templates import get_story_intro
from typing import List
from engine.generator import generate_response
from prompts.emotion_to_tone import emotion_tone_hint
from openai import OpenAI

client = OpenAI(api_key="sk-f8bc4b9248224d7c9a8de15db033ab53", base_url="https://api.deepseek.com")

class CharacterContextManager:
    def __init__(self, character_name: str):
        self.profile = CHARACTER_CONFIGS[character_name]
        self.name = character_name
        self.history: List[str] = []

    def initialize_context(self):
        self.history.clear()
        self.history.append(f"角色设定：{self.profile.background}，性格：{self.profile.personality}，语气风格：{self.profile.speaking_style}，当前情绪：{self.profile.emotion}")

    def build_prompt(self, phase: str, all_responses: list = None, character_names: list = None, current_round_responses: list = None, current_round_speakers: list = None) -> str:
        context = "\n".join(self.history[-3:])  # 取最近3轮上下文
        tone_style = emotion_tone_hint(self.profile.emotion)
        
        # 使用AI检查上一轮是否有问题需要回答
        question_guide = ""
        if all_responses and character_names:
            for i, response in enumerate(all_responses):
                speaker = character_names[i]
                if speaker != self.name:
                    try:
                        check_response = client.chat.completions.create(
                            model="deepseek-chat",
                            messages=[{"role": "user", "content": f"判断这句话是否包含问题或需要回应：{response}，回答是或否"}]
                        )
                        if "是" in check_response.choices[0].message.content:
                            question_guide = f"请回答{speaker}的问题：{response}"
                            break
                    except:
                        pass
        
        # 本轮已有对话内容
        current_dialogue = ""
        if current_round_responses and current_round_speakers and phase != "相遇":
            dialogue_parts = []
            for speaker, response in zip(current_round_speakers, current_round_responses):
                dialogue_parts.append(f"{speaker}：{response}")
            if dialogue_parts:
                current_dialogue = f"本轮对话：\n" + "\n".join(dialogue_parts) + "\n请基于本轮对话内容继续对话。"
        
        prompt = (
            # f"故事背景：{get_story_intro()}\n"
            f"当前剧情阶段：{phase}。\n"
            f"{self.name}，请根据设定继续对话。\n"
            f"人物背景：{self.profile.background}。\n"
            f"性格特点：{self.profile.personality}。\n"
            f"当前情绪：{self.profile.emotion}。\n"
            f"语气风格：{tone_style}。\n"
            f"历史对话摘要：{context}\n"
            f"{current_dialogue}"
            f"{question_guide}"
            f"{self.name}："
        )
        return prompt

    async def generate_response(self, prompt: str) -> str:
        # 模拟异步调用语言模型（此处使用固定返回）
        # 实际应调用 deepseek-chat 接口
        return await generate_response(self.name, prompt)

    def update_context(self, response: str):
        self.history.append(f"{self.name}：{response}")