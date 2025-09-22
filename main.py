import asyncio
from director import StoryDirector

async def main():
    print("=== AI剧本工坊 ===")
    print("请选择模式：")
    print("1. 观看模式 - 自动演绎完整剧情")
    print("2. 导演模式 - 可交互控制剧情")
    
    while True:
        choice = input("请输入选择 (1/2): ").strip()
        if choice in ['1', '2']:
            break
        print("请输入有效选择 (1 或 2)")
    
    # 初始化导演控制器
    director = StoryDirector()
    await director.initialize_characters()
    
    if choice == '1':
        print("\n【观看模式】开始自动演绎...")
        director.watch_mode = True
    else:
        print("\n【导演模式】开始交互式剧情...")
        director.watch_mode = False
    
    await director.run_story_loop()

if __name__ == '__main__':
    asyncio.run(main())