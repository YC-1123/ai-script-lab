class StoryState:
    """
    剧情状态机，负责记录当前阶段与推进状态。
    """

    def __init__(self):
        self.phases = ["相遇", "冲突", "理解"]
        self.current_index = 0
        self.flags = {
            "冲突已触发": False,
            "理解已建立": False
        }

    def get_current_phase(self) -> str:
        return self.phases[self.current_index]

    def advance_phase(self):
        if self.current_index < len(self.phases) - 1:
            self.current_index += 1

    def set_flag(self, key: str, value: bool = True):
        self.flags[key] = value

    def get_flag(self, key: str) -> bool:
        return self.flags.get(key, False)

    def reset(self):
        self.current_index = 0
        for key in self.flags:
            self.flags[key] = False