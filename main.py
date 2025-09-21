import asyncio
from director import StoryDirector

async def main():
    # 初始化导演控制器
    director = StoryDirector()
    await director.initialize_characters()
    await director.run_story_loop()

if __name__ == '__main__':
    asyncio.run(main())