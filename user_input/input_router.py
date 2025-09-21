class InputRouter:
    """
    将用户输入指令映射为具体分支行为
    """

    def __init__(self):
        self.valid_commands = {
            "切换情绪": self.route_emotion_switch,
            "注入剧情": self.route_story_injection,
            "查看状态": self.route_status_view,
        }

    def route(self, command: str, content: str) -> str:
        for keyword, handler in self.valid_commands.items():
            if command.startswith(keyword):
                return handler(content)
        return "【系统】未知指令，请重新输入"

    def route_emotion_switch(self, emotion: str) -> str:
        # 实际逻辑应通过上下文接口更新角色情绪
        return f"【系统】角色情绪已设定为：{emotion}"

    def route_story_injection(self, plot: str) -> str:
        # 将 plot 内容注入到剧情上下文中
        return f"【系统】已注入新剧情片段：{plot}"

    def route_status_view(self, _: str) -> str:
        return "【系统】当前状态：阶段-相遇，情绪-平静，角色-艾琳/诺亚"