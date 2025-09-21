def build_character_prompt(name: str, background: str, personality: str, style: str, emotion: str, story_phase: str, history: str) -> str:
    """
    构建角色生成Prompt文本，融合剧情阶段、人物设定、当前情绪与上下文摘要。
    """
    return (
        f"【角色：{name}】\n"
        f"背景：{background}\n"
        f"性格：{personality}\n"
        f"语言风格：{style}\n"
        f"当前情绪：{emotion}\n"
        f"剧情阶段：{story_phase}\n"
        f"上下文摘要：{history}\n"
        f"{name}："
    )