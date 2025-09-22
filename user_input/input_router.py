class InputRouter:
    """
    将用户输入指令映射为具体分支行为
    """

    def __init__(self):
        self.current_emotion = None
        self.injected_plot = None
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
        self.current_emotion = emotion
        return f"【系统】角色情绪已设定为：{emotion}"

    def route_story_injection(self, plot: str) -> str:
        self.injected_plot = plot
        return f"【系统】已注入新剧情片段：{plot}"

    def route_status_view(self, _: str) -> str:
        return f"【系统】当前情绪：{self.current_emotion or '默认'}，注入剧情：{self.injected_plot or '无'}"

    def get_emotion_context(self) -> str:
        return f"当前情绪状态：{self.current_emotion}" if self.current_emotion else ""

    def get_plot_context(self) -> str:
        return f"注入剧情：{self.injected_plot}" if self.injected_plot else ""

    def clear_injected_plot(self):
        self.injected_plot = None