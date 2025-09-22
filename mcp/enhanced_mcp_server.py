#!/usr/bin/env python3
import asyncio
from mcp_story_server import MCPStoryServer
from mcp.mcp_multimedia_tools import MultimediaMCPTools

class EnhancedMCPServer(MCPStoryServer):
    """集成多媒体功能的增强MCP服务器"""
    
    def __init__(self):
        super().__init__()
        self.multimedia_tools = MultimediaMCPTools()
    
    def list_tools(self):
        """返回所有工具（故事+多媒体）"""
        story_tools = super().list_tools()
        multimedia_tools = self.multimedia_tools.get_multimedia_tools()
        return story_tools + multimedia_tools
    
    async def call_tool(self, name: str, arguments: dict):
        """调用工具（故事或多媒体）"""
        multimedia_tool_names = [
            "generate_character_image",
            "generate_scene_image", 
            "generate_character_voice",
            "generate_background_music",
            "generate_sound_effect"
        ]
        
        if name in multimedia_tool_names:
            return await self.multimedia_tools.call_multimedia_tool(name, arguments)
        else:
            return await super().call_tool(name, arguments)

async def enhanced_demo():
    """增强版演示"""
    server = EnhancedMCPServer()
    
    print("=== AI剧本工坊增强版MCP服务器 ===\n")
    
    # 启动故事会话
    result = await server.call_tool("start_story_session", {})
    print(result["content"][0]["text"])
    
    # 生成角色形象
    print("\n🎨 生成角色形象...")
    result = await server.call_tool("generate_character_image", {
        "character_name": "艾琳",
        "description": "未来科技风格的女性飞行员，短发，专业制服，在星舰驾驶舱",
        "style": "cinematic"
    })
    for content in result["content"]:
        if content["type"] == "text":
            print(content["text"])
    
    # 运行对话并生成配音
    print("\n🎭 生成对话...")
    dialogue_result = await server.call_tool("generate_dialogue", {
        "character_name": "艾琳",
        "phase": "相遇"
    })
    dialogue_text = dialogue_result["content"][0]["text"]
    print(f"艾琳：{dialogue_text}")
    
    # 为对话生成配音
    print("\n🎤 生成配音...")
    voice_result = await server.call_tool("generate_character_voice", {
        "character_name": "艾琳",
        "text": dialogue_text,
        "emotion": "professional"
    })
    for content in voice_result["content"]:
        print(f"  {content['text']}")
    
    # 生成场景插图
    print("\n🖼️ 生成场景插图...")
    scene_result = await server.call_tool("generate_scene_image", {
        "scene_description": "星际飞船远航者号的驾驶舱，充满未来科技感的控制面板",
        "mood": "mysterious",
        "style": "cinematic"
    })
    for content in scene_result["content"]:
        if content["type"] == "text":
            print(content["text"])
    
    # 生成背景音乐
    print("\n🎵 生成背景音乐...")
    music_result = await server.call_tool("generate_background_music", {
        "mood": "tense",
        "genre": "cinematic",
        "duration": 120
    })
    for content in music_result["content"]:
        print(f"  {content['text']}")
    
    # 生成环境音效
    print("\n🔊 生成环境音效...")
    sfx_result = await server.call_tool("generate_sound_effect", {
        "effect_type": "spaceship_ambient",
        "scene_context": "星舰驾驶舱",
        "intensity": "low"
    })
    for content in sfx_result["content"]:
        print(f"  {content['text']}")

if __name__ == "__main__":
    asyncio.run(enhanced_demo())
