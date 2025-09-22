# AI剧本工坊 - 多媒体MCP服务器

## 🎭 项目概述

AI剧本工坊是一个基于MCP（Model Context Protocol）标准的多媒体内容生成平台，专注于AI驱动的剧本创作和多媒体内容生成。

## ✨ 核心特性

### 📝 智能剧本生成
- 多角色对话系统
- 动态剧情推进
- 情绪状态管理
- 上下文记忆机制

### 🎨 多媒体内容生成
- **角色形象生成** - DALL-E集成，支持多种艺术风格
- **场景插图生成** - 动态场景可视化
- **角色配音生成** - ElevenLabs语音合成
- **背景音乐生成** - AI音乐创作
- **环境音效生成** - Freesound API集成

### 🔧 MCP标准化架构
- 标准化工具接口
- 可扩展模块设计
- 第三方服务集成
- 跨平台兼容性

## 🚀 快速开始

### 基础剧本生成
```bash
python3 main.py
```

### 多媒体内容演示
```bash
python3 multimedia_demo.py
```

## 🛠️ MCP工具列表

### 故事生成工具
- `start_story_session` - 启动剧本会话
- `initialize_character` - 初始化角色
- `generate_dialogue` - 生成对话
- `advance_story_phase` - 推进剧情
- `run_story_round` - 运行完整轮次

### 多媒体生成工具
- `generate_character_image` - 角色形象生成
- `generate_scene_image` - 场景插图生成
- `generate_character_voice` - 角色配音生成
- `generate_background_music` - 背景音乐生成
- `generate_sound_effect` - 环境音效生成

## 📊 使用示例

### 生成角色形象
```python
await server.call_tool("generate_character_image", {
    "character_name": "艾琳",
    "description": "未来科技风格女性飞行员",
    "style": "realistic"
})
```

### 生成角色配音
```python
await server.call_tool("generate_character_voice", {
    "character_name": "艾琳",
    "text": "航线参数已校准",
    "emotion": "professional"
})
```

## 🎯 应用场景

### 内容创作
- 快速剧本原型制作
- 多媒体素材生成
- 创意灵感激发

### 教育培训
- 互动式故事教学
- 语言学习辅助
- 创意写作训练

### 娱乐应用
- 个性化故事体验
- 角色扮演游戏
- 社交互动平台

## 🔮 技术架构

```
AI剧本工坊
├── 核心剧本引擎
│   ├── 角色管理系统
│   ├── 剧情状态机
│   └── 对话生成器
├── MCP标准化层
│   ├── 工具定义
│   ├── 请求处理
│   └── 响应格式化
└── 多媒体集成层
    ├── 图像生成 (DALL-E)
    ├── 语音合成 (ElevenLabs)
    └── 音效库 (Freesound)
```

## 📈 项目演进

1. **第一阶段** - 基础剧本生成系统
2. **第二阶段** - MCP标准化重构
3. **第三阶段** - 多媒体内容集成 ✅
4. **未来规划** - VR/AR沉浸式体验

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License

---

**AI剧本工坊** - 让AI创作更加生动多彩 🎨🎭🎵
