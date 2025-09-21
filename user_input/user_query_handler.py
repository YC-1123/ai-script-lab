from user_input.input_router import InputRouter

class UserQueryHandler:
    """
    用户输入的处理协调器，结合输入路由模块
    """

    def __init__(self):
        self.router = InputRouter()

    def handle_user_input(self, raw_input: str) -> str:
        """
        基本指令格式：命令: 内容
        例如：切换情绪: 愤怒
        """
        if ":" not in raw_input:
            return "【系统】指令格式错误，应为 '命令: 内容'"
        command, content = raw_input.split(":", 1)
        return self.router.route(command.strip(), content.strip())