# 🌱 The Seed

> *"在刀剑神域的世界里，The Seed 是创世之初的种子，蕴含着无限可能。"*
> 
> 在现实世界中，**The Seed** 是一个面向大众的下一代 AI Agent 开发框架——它继承 OpenClaw Hermes 的核心理念，超越其边界，让每个人都能构建属于自己的 AI Agent。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Chat](https://img.shields.io/badge/Chat-Community-blue.svg)](https://github.com/Kirrito-k423/TheSeed/discussions)

---

## 🎯 Core Philosophy / 核心哲学

The Seed 的设计理念源自 SAO 中的「创世」概念：

1. **The Seed 不只是一个框架，而是一个生态系统**
   - 每个人都可以用 The Seed 构建、发布和分享自己的 Agent
   - 开发者不需要深入理解底层原理，也能创建强大的 AI Agent

2. **超越 OpenClaw Hermes**
   - Hermes 是强大的面向开发者的框架
   - The Seed 在其基础上，增加了面向终端用户的**零代码配置能力**
   - 更大胆的多模型协作、更灵活的工具系统、更开放的生态

3. **Universal LLM API Support / 通用 LLM API 支持**
   - 内置支持 50+ LLM 提供商
   - OpenAI / Anthropic / Google / Azure / 本地模型 / 国产模型（文心/通义/混元/等）
   - 统一接口，一次配置，处处运行

---

## 🏗️ Architecture / 架构设计

```
┌─────────────────────────────────────────────────────────┐
│                    The Seed Framework                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐     │
│  │  User    │   │ Developer│   │   Plugin Author  │     │
│  │ (Zero    │   │ (Custom  │   │   (Extension    │     │
│  │  Code)   │   │  Logic)  │   │    Builder)     │     │
│  └────┬─────┘   └────┬─────┘   └───────┬──────────┘     │
│       │              │                  │                 │
│  ┌────▼───────────────▼─────────────────▼──────────┐    │
│  │           The Seed Core Engine                   │    │
│  │  ┌─────────────────────────────────────────┐     │    │
│  │  │     Agent Orchestration Layer           │     │    │
│  │  │  ┌─────────┐  ┌─────────┐  ┌────────┐  │     │    │
│  │  │  │ Memory  │  │  Tools  │  │  LLM   │  │     │    │
│  │  │  │ Engine  │  │ Registry│  │ Bridge │  │     │    │
│  │  │  └─────────┘  └─────────┘  └────────┘  │     │    │
│  │  └─────────────────────────────────────────┘     │    │
│  │  ┌─────────────────────────────────────────┐     │    │
│  │  │   Platform Integration Layer             │     │    │
│  │  │  Telegram | Discord | WeChat | API | ... │     │    │
│  │  └─────────────────────────────────────────┘     │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Core Components / 核心组件

| Component | Description |
|-----------|-------------|
| **TheSeed.Core** | 核心引擎，处理 Agent 的生命周期管理 |
| **TheSeed.Memory** | 记忆系统，支持短期/长期记忆，跨会话上下文 |
| **TheSeed.Tools** | 工具注册表，动态加载和执行工具 |
| **TheSeed.LLM** | LLM 桥接层，统一接口连接各种模型提供商 |
| **TheSeed.Platform** | 平台集成，支持多端消息网关 |
| **TheSeed.Plugin** | 插件系统，热插拔扩展功能 |
| **TheSeed.Config** | 配置系统，支持 YAML/JSON/ENV 多格式 |
| **TheSeed.UI** | 用户界面，CLI / Web / Desktop 三端可选 |

---

## ✨ Features / 核心特性

### 🚀 Getting Started / 快速上手

```bash
# 安装
pip install the-seed

# 初始化项目
seed init my-agent

# 配置模型
seed config set llm.provider openai
seed config set llm.api_key sk-xxxx

# 启动 Agent
seed run
```

### 🔧 Configuration / 配置示例

```yaml
# seed.yaml
agent:
  name: "MyFirstAgent"
  personality: "helpful"
  model: gpt-4o

llm:
  provider: openai  # or anthropic/google/azure/local/...
  api_key: ${OPENAI_API_KEY}
  # 支持多模型热切换
  models:
    primary: gpt-4o
    fallback: gpt-4o-mini

memory:
  type: sqlite  # or redis/mem0
  session_store: ~/.the-seed/memory.db

tools:
  enabled:
    - web_search
    - calculator
    - file_operations
  custom:
    - ./my-tools/

platforms:
  telegram:
    enabled: true
    bot_token: ${TELEGRAM_BOT_TOKEN}
```

### 🌐 Universal LLM Support / 通用 LLM 支持

```python
from seed import TheSeed

# OpenAI
agent = TheSeed(provider="openai", model="gpt-4o")

# Anthropic
agent = TheSeed(provider="anthropic", model="claude-sonnet-4")

# Google
agent = TheSeed(provider="google", model="gemini-2-flash")

# Azure
agent = TheSeed(provider="azure", endpoint="https://xxx.openai.azure.com")

# 本地模型 / 国产模型
agent = TheSeed(provider="local", model="Qwen/Qwen2.5-72B-Instruct")
agent = TheSeed(provider="qwen", model="qwen-turbo")
agent = TheSeed(provider="wenxin", model="ernie-4.0")

# 自定义 API 端点
agent = TheSeed(
    provider="custom",
    api_base="https://your-custom-endpoint.com/v1",
    api_key="sk-xxxx"
)
```

### 🛠️ Tool System / 工具系统

```python
from seed.tools import register_tool

@register_tool(name="weather", description="查询天气")
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"{city} 今天的天气是晴天，25°C"

# 工具自动被发现并注册
agent = TheSeed()
agent.register_tool(get_weather)
```

### 💬 Multi-Platform / 多平台支持

```bash
# Telegram Bot
seed platform enable telegram --token xxx

# Discord Bot  
seed platform enable discord --token xxx

# WeChat (企业版)
seed platform enable wechat --corpid xxx --corpsecret xxx

# 自定义 API Server
seed platform enable api --port 8080
```

---

## 📁 Project Structure / 项目结构

```
TheSeed/
├── src/
│   └── seed/
│       ├── __init__.py
│       ├── core/                 # 核心引擎
│       │   ├── agent.py          # Agent 主类
│       │   ├── engine.py         # 推理引擎
│       │   └── loop.py          # Agent Loop
│       ├── llm/                  # LLM 桥接
│       │   ├── base.py          # 抽象基类
│       │   ├── openai.py        # OpenAI 适配器
│       │   ├── anthropic.py     # Anthropic 适配器
│       │   └── custom.py        # 自定义适配器
│       ├── memory/              # 记忆系统
│       │   ├── base.py
│       │   ├── short_term.py
│       │   └── long_term.py
│       ├── tools/               # 工具系统
│       │   ├── registry.py
│       │   ├── executor.py
│       │   └── builtins/        # 内置工具
│       ├── platform/            # 平台集成
│       │   ├── base.py
│       │   ├── telegram.py
│       │   ├── discord.py
│       │   └── api.py
│       ├── plugin/             # 插件系统
│       │   ├── loader.py
│       │   └── manager.py
│       ├── config/             # 配置系统
│       │   ├── loader.py
│       │   └── validator.py
│       └── ui/                 # 用户界面
│           ├── cli.py
│           └── web.py
├── tests/
├── docs/
├── examples/
├── pyproject.toml
└── README.md
```

---

## 🔥 Comparison with Hermes / 与 Hermes 对比

| Feature | OpenClaw Hermes | The Seed |
|---------|-----------------|----------|
| **目标用户** | 开发者 | 所有用户 + 开发者 |
| **配置方式** | YAML + 代码 | YAML / JSON / ENV / Web UI |
| **零代码模式** | ❌ | ✅ |
| **多模型支持** | ✅ | ✅ (更广) |
| **工具注册** | 代码级 | 代码 + YAML + 热插拔 |
| **记忆系统** | SQLite | SQLite + Redis + 云端 |
| **平台集成** | 多平台 | 多平台 + 微信小程序 |
| **插件系统** | 基础 | 完整的热插拔生态 |
| **多Agent协作** | 基础 | 原生支持 |
| **学习曲线** | 中高 | 低~中 |

---

## 🚧 Roadmap / 路线图

- [ ] **v0.1.0** - 核心框架搭建完成
- [ ] **v0.2.0** - LLM 适配器支持 OpenAI/Anthropic/本地模型
- [ ] **v0.3.0** - 基础工具系统和记忆系统
- [ ] **v0.4.0** - Telegram/Discord 平台集成
- [ ] **v0.5.0** - 零代码配置模式
- [ ] **v1.0.0** - 正式版发布

---

## 📜 License / 许可证

MIT License - 允许任何人免费使用、修改和分发。

---

## 🙏 Credits / 致谢

- 灵感来源：[Sword Art Online - The Seed](https://swordartonline.fandom.com/wiki/The_Seed)
- 技术参考：[OpenClaw Hermes](https://github.com/nickat坠机/hermes-agent)
- 图标：[Emoji](https://github.com/ikatyang/emoji-cheat-sheet)

---

*"Every great system starts from a single seed."*