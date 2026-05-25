# 🌱 The Seed

> *"在刀剑神域的世界里，The Seed 是创世之初的种子，蕴含着无限可能。"*
> 
> 在现实世界中，**The Seed** 是一个面向大众的下一代 AI Agent 开发框架——它继承 OpenClaw Hermes 的核心理念，超越其边界，让每个人都能构建属于自己的 AI Agent。

> ⚡️ **核心理念**：可观测、可拆分溯源、可控、可续执行、能定制、能汇报的 Agent 系统。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

---

## 🎯 Core Philosophy / 核心哲学

### 降本 & 增效的双轮驱动

| 维度 | 策略 | 说明 |
|------|------|------|
| **降本（Cost Reduction）** | 克制的上下文输入 | 只给少量信息，反馈不足则动态补充更多 |
| **降本** | 可定制压缩策略 | 多级压缩：摘要/检索/丢弃，用户可配置 |
| **增效（Efficiency）** | 子任务原子化拆分 | 追求最小可执行单元，场景可定制拆分策略 |
| **增效** | 智能调度 | 子任务并行/串行，优先级调度 |
| **增效** | 提示词优化 | 自适应提示词，根据任务类型选择最佳模板 |

### 生产级可靠性

| 特性 | 说明 |
|------|------|
| **可观测（Observable）** | 每个技能触发、上下文膨胀、token 吞吐全程记录 |
| **可拆分溯源（Traceable）** | 子任务拆分原因可追溯，拆分地图（map）清晰可见 |
| **可控（Controllable）** | 压缩策略、拆分策略、工具选择均可配置 |
| **可续执行（Resumable）** | 细粒度暂停/续训，中间文件详细到支持任意位置恢复 |
| **可定制（Customizable）** | LLM API、工具、压缩策略、拆分策略全部可插拔 |
| **可汇报（Reportable）** | 详尽的 DFX 数据：耗时、费用、瓶颈分析全链路可视化 |

---

## 🏗️ Architecture / 架构设计

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         The Seed Framework                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────────┐  │
│  │    User      │  │  Developer   │  │      Enterprise Admin         │  │
│  │ (Zero Code)  │  │ (Customize)  │  │   (Policy Configuration)      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────────┬───────────────┘  │
│         │                 │                           │                  │
│  ┌──────▼─────────────────▼───────────────────────────▼────────────┐  │
│  │                     Configuration Layer                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  ┌───────────┐ │  │
│  │  │Compression │  │  Decompose  │  │   Tool       │  │    LLM    │ │  │
│  │  │  Policy    │  │  Strategy  │  │  Policy     │  │  Policy   │ │  │
│  │  └─────────────┘  └─────────────┘  └──────────────┘  └───────────┘ │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                  │                                        │
│  ┌───────────────────────────────▼──────────────────────────────────┐  │
│  │                      Core Engine                                     │  │
│  │  ┌─────────────────────────────────────────────────────────────┐    │  │
│  │  │                    Agent Orchestrator                         │    │  │
│  │  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │    │  │
│  │  │  │ Context  │  │  Task     │  │  Tool    │  │   LLM     │  │    │  │
│  │  │  │ Manager  │  │ Splitter  │  │ Executor │  │  Bridge   │  │    │  │
│  │  │  │ (压缩)    │  │ (原子化)  │  │ (可拓展)  │  │ (通用)    │  │    │  │
│  │  │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  │    │  │
│  │  └────────┼─────────────┼─────────────┼───────────────┼────────┘    │  │
│  │           │            │            │            │                  │  │
│  │  ┌─────────▼───────────▼────────────▼────────────▼────────────┐   │  │
│  │  │                    Memory & State                            │   │  │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────────┐ │   │  │
│  │  │  │ Short   │  │  Long   │  │ Check-  │  │  Intermediate   │ │   │  │
│  │  │  │ Term    │  │  Term   │  │ point   │  │    Files        │ │   │  │
│  │  │  │ Memory  │  │ Memory  │  │         │  │  (续训支持)      │ │   │  │
│  │  │  └─────────┘  └─────────┘  └─────────┘  └─────────────────┘ │   │  │
│  │  └───────────────────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                  │                                        │
│  ┌───────────────────────────────▼──────────────────────────────────┐  │
│  │                    Observability Layer                             │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐ │  │
│  │  │   Metrics   │  │   Traces     │  │   Reports & Dashboards   │ │  │
│  │  │ 耗时/吞吐/ │  │ 链路追踪/  │  │ 可视化/瓶颈分析/        │ │  │
│  │  │ 费用/延迟  │  │ 拆分溯源   │  │ E2E耗时占比             │ │  │
│  │  └──────────────┘  └──────────────┘  └──────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    Platform Integration Layer                      │   │
│  │  Telegram | Discord | WeChat | API Server | Custom Webhook        │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Core Modules / 核心模块

### 1. Context Manager（上下文管理器）

**职责**：克制的上下文输入 + 可定制压缩策略

```
输入信息 ──→ [少给原则] ──→ [反馈不足?] ──→ [动态补充更多]
                                    │
                          ┌─────────▼─────────┐
                          │  压缩策略选择器    │
                          │  - Summary (摘要)   │
                          │  - Retrieval (检索) │
                          │  - Drop (丢弃)      │
                          │  - Keep (保留)      │
                          └─────────────────────┘
```

### 2. Task Splitter（任务拆分器）

**职责**：极致简单的子任务拆分，追求原子化

| 策略 | 适用场景 |
|------|----------|
| `atomic` | 通用场景，每个动作一个子任务 |
| `scene-aware` | 业务场景，保留领域知识边界 |
| `streaming` | 流式场景，支持增量处理 |
| `rollback` | 关键决策场景，保留回滚点 |

**拆分输出**：
```json
{
  "task_id": "t001",
  "decomposition_reason": "用户问题涉及多步骤，需要拆分以确保可追溯",
  "subtasks": [
    {
      "id": "s001",
      "action": "search_web",
      "input": "最新AI Agent框架对比",
      "output_file": ".seed/checkpoint/s001.json"
    },
    {
      "id": "s002", 
      "action": "analyze",
      "depends_on": ["s001"],
      "input_file": ".seed/checkpoint/s001.json",
      "output_file": ".seed/checkpoint/s002.json"
    }
  ]
}
```

### 3. Tool Executor（工具执行器）

**职责**：易拓展的工具接口，支持网络搜索、文本处理、命令行执行

```python
@register_tool(name="web_search", description="网络搜索")
def web_search(query: str, max_results: int = 5) -> str:
    """支持多种搜索后端：SerpAPI/Tavily/Bing/Google"""
    ...

@register_tool(name="cli_execute", description="命令行执行")
def cli_execute(command: str, timeout: int = 30) -> str:
    """安全执行本地命令，超时保护"""
    ...

@register_tool(name="text_process", description="文本处理")
def text_process(text: str, operation: str) -> str:
    """文本分析、摘要、翻译等操作"""
    ...
```

### 4. LLM Bridge（LLM 桥接层）

**职责**：统一接口，连接各种 LLM 提供商

```python
# 支持的提供商
providers = [
    "openai",      # GPT-4o / GPT-4o-mini
    "anthropic",   # Claude 3.5 / Claude 3 Opus
    "google",      # Gemini 2.0 / Gemini Flash
    "qwen",        # 通义千问
    "wenxin",      # 文心一言
    "混元",        # 腾讯混元
    "local",       # vLLM / Ollama / LocalAI
    "custom",      # 自定义端点
]
```

---

## 📊 Observability / 可观测性

### 详尽的 DFX 数据

| 指标类别 | 具体指标 | 说明 |
|----------|----------|------|
| **Skills 触发** | 触发时刻、上下文膨胀率 | 记录每个 skill 何时被触发，输入输出大小 |
| **Token 吞吐** | 输入/输出 token 数、首 token 延迟、总费用 | 按子任务/工具/全链路统计 |
| **工具调用** | 调用次数、成功率、耗时、错误类型 | 每个工具的独立 metrics |
| **E2E 分析** | 总耗时、瓶颈占比、拆分 map 图 | 端到端任务追踪和瓶颈定位 |
| **子任务溯源** | 拆分原因、子任务依赖图、中间文件 | 任意位置可恢复 |

### 报告示例

```
┌─────────────────────────────────────────────────────────────┐
│  The Seed - 任务执行报告                                    │
├─────────────────────────────────────────────────────────────┤
│  任务ID: task_20250601_001                                   │
│  开始时间: 2026-06-01 10:00:00                               │
│  总耗时: 45.2s                                               │
├─────────────────────────────────────────────────────────────┤
│  拆分原因: 用户问题涉及多步骤网络搜索+分析，原子化拆分        │
│  子任务数: 4                                                  │
├─────────────────────────────────────────────────────────────┤
│  子任务   │ 耗时   │ Token  │ 费用    │ 状态                │
│  ──────── │ ─────  │ ─────  │ ──────  │ ─────────────────── │
│  s001 搜索│ 12.3s  │ 1,200  │ $0.002  │ ✅ 完成              │
│  s002 分析│ 8.7s   │ 3,400  │ $0.014  │ ✅ 完成              │
│  s003 汇总│ 5.1s   │ 800    │ $0.003  │ ✅ 完成              │
├─────────────────────────────────────────────────────────────┤
│  工具调用 │ 次数   │ 成功率 │ 耗时均  │                     │
│  ──────── │ ─────  │ ─────  │ ─────   │                     │
│  web_search│ 2     │ 100%   │ 5.2s    │                     │
├─────────────────────────────────────────────────────────────┤
│  瓶颈分析: s002 分析阶段占总耗时 19.2%，为主要瓶颈           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start / 快速开始

```bash
# 安装
pip install the-seed

# 初始化
seed init my-agent --scenario e-commerce

# 配置
seed config set llm.provider openai
seed config set llm.model gpt-4o
seed config set llm.api_key ${OPENAI_API_KEY}

# 启用可观测性
seed config set observability.enabled true
seed config set observability.export_format html

# 运行
seed run --task "分析竞品价格并给出建议"
```

---

## ⚙️ Configuration / 配置示例

```yaml
# seed.yaml
agent:
  name: "MyAgent"
  scenario: custom  # e-commerce / customer-service / data-analysis / custom
  model: gpt-4o

llm:
  provider: openai
  api_key: ${OPENAI_API_KEY}
  # 多模型热切换
  models:
    primary: gpt-4o
    analysis: gpt-4o-mini
    fallback: claude-sonnet-4

# 压缩策略
compression:
  strategy: adaptive  # none / summary / retrieval / adaptive
  max_context_tokens: 128000
  trigger_threshold: 0.7  # 上下文利用率 > 70% 时触发压缩

# 拆分策略
decompose:
  strategy: atomic  # atomic / scene-aware / streaming / rollback
  max_subtasks: 20
  parallel_threshold: 3  # 超过3个子任务时尝试并行

# 工具配置
tools:
  enabled:
    - web_search
    - cli_execute
    - text_process
  custom_path: ./my-tools/

# 可观测性
observability:
  enabled: true
  export:
    - format: json
      path: .seed/reports/
    - format: html
      path: .seed/reports/
  metrics:
    - token_usage
    - latency
    - cost
    - error_rate

# 平台配置
platforms:
  api:
    enabled: true
    port: 8080
```

---

## 🔥 Comparison / 与 Hermes 对比

| Feature | OpenClaw Hermes | The Seed |
|---------|-----------------|----------|
| **目标用户** | 开发者 | 所有用户 + 开发者 |
| **配置方式** | YAML + 代码 | YAML / JSON / ENV / Web UI |
| **零代码模式** | ❌ | ✅ |
| **上下文压缩** | 基础 | 可定制多级压缩策略 |
| **任务拆分** | 基础 | 原子化 + 场景定制 |
| **细粒度续训** | ❌ | ✅ Checkpoint 中间文件 |
| **可观测性** | 基础日志 | DFX 全链路 metrics + 报告 |
| **多模型支持** | ✅ | ✅ (更广+热切换) |
| **工具系统** | 代码级 | 代码 + YAML + 热插拔 |
| **E2E 报告** | 基础 | 详尽瓶颈分析 + 可视化 |

---

## 📜 License

MIT License

---

*"Every great system starts from a single seed."*