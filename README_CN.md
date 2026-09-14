# 企业 AI 平台 — Qwen + Dify + RAG + ERPNext

本项目将 **Qwen、vLLM、Dify、RAG、BGE-M3 与 ERPNext** 集成为一个本地企业 AI 平台，实现本地大模型推理、企业知识库检索、自然语言 ERP 查询、呆滞库存分析以及 Excel 数据输出。

## 项目概述

```text
用户
  ↓
Dify Chatflow / Workflow
  ├──→ Qwen3.5-9B / vLLM
  ├──→ RAG 知识库 / BGE-M3
  └──→ ERPNext REST API
              ↓
          业务数据
              ↓
          分析与汇总
              ↓
           Excel 输出
```

## 核心功能

- Qwen3.5-9B 本地部署
- vLLM OpenAI-compatible API
- Dify Chatflow 与 Workflow
- 企业 RAG 知识库
- BGE-M3 Embedding 服务
- ERPNext REST API 集成
- 自然语言 ERP 查询
- 呆滞库存识别与分析
- 分析结果输出为 Excel 文件
- Linux / Docker 私有化部署

## 技术栈

| 层级 | 技术 |
|---|---|
| 大模型 | Qwen3.5-9B |
| 推理框架 | vLLM |
| GPU | NVIDIA Tesla V100 32GB |
| 操作系统 | Ubuntu 22.04 LTS |
| 工作流平台 | Dify |
| Embedding | BGE-M3 |
| Embedding 服务 | Xinference |
| ERP | ERPNext |
| 集成方式 | REST API / HTTP |
| 部署 | Docker / Linux |
| 数据输出 | Excel |

## Qwen 本地部署

Qwen3.5-9B 部署于 NVIDIA Tesla V100，通过 vLLM 提供 OpenAI-compatible API。

```text
dtype: float16
max_model_len: 8192
max_num_seqs: 1
gpu_memory_utilization: 0.85
```

## Dify 工作流

Dify 负责 Chatflow、Workflow、本地大模型调用、RAG 检索、HTTP 请求、ERPNext 调用、业务规则处理、结构化结果生成以及文件服务集成。

## 企业 RAG

```text
企业文档
↓
切分
↓
BGE-M3 Embedding
↓
向量检索
↓
相关上下文
↓
Qwen
↓
基于知识库的回答
```

## ERPNext 集成

主要资源：

```text
/api/resource/Item
/api/resource/Bin
/api/resource/Stock Ledger Entry
```

## 自然语言 ERP 查询

```text
用户：查询 SKU001 库存
↓
物料编码提取
↓
ERPNext API
↓
业务数据
↓
自然语言结果
```

## 呆滞库存分析

```json
{
  "item_group": "Raw Material",
  "idle_days": 180,
  "min_stock_value": 50000,
  "analysis_type": "stagnant_inventory"
}
```

```text
开始
↓
结构化条件抽取
↓
ERPNext Bin 查询
↓
库存金额筛选
↓
目标物料迭代
↓
Stock Ledger Entry 查询
↓
呆滞天数计算
↓
呆滞物料汇总
↓
LLM 分析
↓
结构化结果
↓
Excel 输出
```

## 验证范围

- Qwen API
- 企业 RAG
- ERPNext 自然语言查询
- 呆滞库存识别
- Excel 数据输出

## 项目工作内容

- Qwen3.5-9B 本地部署
- NVIDIA Tesla V100 推理配置
- vLLM API 服务
- Dify Workflow / Chatflow 设计
- BGE-M3 Embedding 服务
- 企业 RAG 知识库
- ERPNext REST API 集成
- 呆滞库存分析
- Excel 数据输出
- Linux 与 Docker 部署
- 模型服务、网络、认证和工作流故障排查

## 安全架构

运行时凭证通过环境变量与源代码分离。私有凭证、生产数据库、模型权重和企业机密数据与公开仓库分离。

## License

本项目仅用于个人作品集展示和学术申请用途。
版权所有 © 2026 Xiaoyu。未经授权，不得复制、修改、分发或用于商业用途。
