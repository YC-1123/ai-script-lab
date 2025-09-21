import asyncio
from actors.character_context_manager import CharacterContextManager
from prompts.story_templates import get_story_intro
from story.story_state import StoryState
from story.emotion_trigger import check_phase_trigger
from engine.response_coordinator import ResponseCoordinator
from story.trigger_rules import should_trigger_conflict, should_trigger_understanding

class StoryDirector:
    def __init__(self):
        # 定义角色名称与剧情阶段
        self.character_names = ["艾琳", "诺亚"]
        self.contexts = {}
        self.story_state = StoryState()
        self.coordinator = ResponseCoordinator(self.character_names)
        self.phase_index = 0

    async def initialize_characters(self):
        print("【系统】剧本角色初始化中...\n")
        for name in self.character_names:
            self.contexts[name] = CharacterContextManager(name)
            self.contexts[name].initialize_context()
        print("【系统】初始化完成，当前参与角色：", "、".join(self.character_names))
        print(f"\n【背景】{get_story_intro()}")

    async def run_story_loop(self):
        print("\n【系统】剧情演化开始\n")
        round_count = 1
        previous_responses = []
        previous_speakers = []
        
        while self.story_state.current_index < len(self.story_state.phases) - 1:
            phase = self.story_state.get_current_phase()
            print(f"\n—— 第{round_count}轮 · 剧情阶段【{phase}】——")
            
            all_responses = []
            current_speakers = []
            current_responses = []
            
            for _ in range(len(self.character_names)):
                name = self.coordinator.next_character()
                ctx = self.contexts[name]
                prompt = ctx.build_prompt(phase, previous_responses, previous_speakers, current_responses, current_speakers)
                response = await ctx.generate_response(prompt)
                ctx.update_context(response)
                print(f"\n{name}：{response}")
                all_responses.append(response)
                current_speakers.append(name)
                current_responses.append(response)
            
            previous_responses = all_responses
            previous_speakers = current_speakers
            
            # 检查是否触发下一阶段
            combined_dialogue = " ".join(all_responses)
            if check_phase_trigger(combined_dialogue, phase):
                print(f"\n【系统】检测到阶段触发条件，推进到下一阶段")
                self.story_state.advance_phase()
            
            round_count += 1
            if round_count > 10:  # 防止无限循环
                break

        print("\n【系统】剧情推进结束")

