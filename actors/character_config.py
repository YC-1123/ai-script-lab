# actors/character_config.py
from dataclasses import dataclass

@dataclass
class CharacterProfile:
    name: str
    background: str
    personality: str
    speaking_style: str
    emotion: str

# 定义多个角色配置
CHARACTER_CONFIGS = {
    "艾琳": CharacterProfile(
        name="艾琳",
        background="银翼星舰的导航工程师，独立冷静，沉着果断",
        personality="善于分析，情绪不外露，遇事首先推理判断",
        speaking_style="语言简洁明了，常用技术类词汇",
        emotion="平静"
    ),
    "诺亚": CharacterProfile(
        name="诺亚",
        background="星舰安保主管，外表强硬但内心敏感",
        personality="偏执多疑，感情丰富，时常情绪化",
        speaking_style="用词激烈，有时带讽刺语气",
        emotion="戒备"
    )
}