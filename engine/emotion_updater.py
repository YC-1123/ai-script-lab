from collections import defaultdict

EMOTION_TRIGGERS = {
    "愤怒": ["愤怒", "欺骗", "不公", "威胁", "不安"],
    "喜悦": ["开心", "惊喜", "美好", "希望", "信任"],
    "悲伤": ["难过", "孤独", "后悔", "失落"],
    "戒备": ["隐藏", "怀疑", "防备"],
    "理解": ["共鸣", "原谅", "宽容", "认同"]
}

def update_emotion_from_text(current_emotion: str, response_text: str) -> str:
    """
    根据响应文本中的关键词推测情绪变化
    """
    emotion_score = defaultdict(int)
    for emotion, keywords in EMOTION_TRIGGERS.items():
        for keyword in keywords:
            if keyword in response_text:
                emotion_score[emotion] += 1

    if emotion_score:
        new_emotion = max(emotion_score.items(), key=lambda x: x[1])[0]
        return new_emotion if new_emotion != current_emotion else current_emotion

    return current_emotion  # 保持原有情绪