import asyncio
from actors.character_context_manager import CharacterContextManager
from prompts.story_templates import get_story_intro
from story.story_state import StoryState
from story.emotion_trigger import check_phase_trigger
from engine.response_coordinator import ResponseCoordinator
from story.trigger_rules import should_trigger_conflict, should_trigger_understanding
from user_input.input_router import InputRouter

class StoryDirector:
    def __init__(self):
        # 定义角色名称与剧情阶段
        self.character_names = ["莉亚", "凯德"]
        self.contexts = {}
        self.story_state = StoryState()
        self.coordinator = ResponseCoordinator(self.character_names)
        self.phase_index = 0
        self.watch_mode = False  # 默认导演模式
        self.input_router = InputRouter()

    async def initialize_characters(self):
        print("【系统】剧本角色初始化中...\n")
        for name in self.character_names:
            self.contexts[name] = CharacterContextManager(name)
            self.contexts[name].initialize_context()
        print("【系统】初始化完成，当前参与角色：", "、".join(self.character_names))
        print(f"\n【背景】{get_story_intro()}")

    def handle_user_input(self):
        """处理用户输入，支持情绪切换和剧情注入"""
        if self.watch_mode:
            return  # 观看模式跳过用户输入
            
        print("\n【用户输入】输入指令（直接回车跳过）：")
        print("- 切换情绪 [情绪名称]")
        print("- 注入剧情 [剧情内容]")
        print("- 查看状态")
        
        user_input = input(">>> ").strip()
        if not user_input:
            return
            
        if " " in user_input:
            command, content = user_input.split(" ", 1)
        else:
            command, content = user_input, ""
            
        result = self.input_router.route(command, content)
        print(result)

    def build_enhanced_prompt(self, base_prompt):
        """将情绪和注入剧情结合到prompt中"""
        enhancements = []
        # 处理情绪注入
        emotion_context = self.input_router.get_emotion_context()
        if emotion_context:
            enhancements.append(emotion_context)
        # 处理剧情注入    
        plot_context = self.input_router.get_plot_context()
        if plot_context:
            enhancements.append(plot_context)
            self.input_router.clear_injected_plot()  # 使用后清除
            
        if enhancements:
            return base_prompt + "\n\n" + "\n".join(enhancements)
        return base_prompt

    async def run_story_loop(self):
        print("\n【系统】剧情演化开始\n")
        round_count = 1
        previous_responses = []
        previous_speakers = []
        phase_round_count = 1  # 当前阶段的轮数计数
        
        while self.story_state.current_index < len(self.story_state.phases):
            phase = self.story_state.get_current_phase()
                        
            # 每轮剧情前处理用户输入
            self.handle_user_input()

            print(f"\n—— 第{round_count}轮 · 剧情阶段【{phase}】(阶段第{phase_round_count}轮) ——")
            
            all_responses = []
            current_speakers = []
            current_responses = []
            
            for _ in range(len(self.character_names)):
                name = self.coordinator.next_character()
                ctx = self.contexts[name]
                base_prompt = ctx.build_prompt(phase, previous_responses, previous_speakers, current_responses, current_speakers)
                enhanced_prompt = self.build_enhanced_prompt(base_prompt)
                response = await ctx.generate_response(enhanced_prompt)
                ctx.update_context(response)
                print(f"\n{name}：{response}")
                all_responses.append(response)
                current_speakers.append(name)
                current_responses.append(response)
            
            previous_responses = all_responses
            previous_speakers = current_speakers
            
            # 检查是否触发下一阶段
            combined_dialogue = " ".join(all_responses)
            phase_advanced = False
            
            if check_phase_trigger(combined_dialogue, phase):
                print(f"\n【系统】检测到阶段触发条件，推进到下一阶段")
                self.story_state.advance_phase()
                phase_advanced = True
                phase_round_count = 1  # 重置阶段轮数
            else:
                phase_round_count += 1
            
            # 特殊处理：确保理解阶段至少运行2轮
            if phase == "理解" and phase_round_count >= 3 and not phase_advanced:
                print(f"\n【系统】理解阶段完成，故事达到圆满结局")
                break
            
            round_count += 1
            if round_count > 10:  # 防止无限循环，增加限制
                print(f"\n【系统】达到最大轮数限制，故事结束")
                break

        print("\n【系统】剧情推进结束")

