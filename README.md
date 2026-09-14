# Enterprise AI Platform — Qwen + Dify + RAG + ERPNext

A local enterprise AI platform integrating **Qwen**, **vLLM**, **Dify**, **RAG**, **BGE-M3**, and **ERPNext** for private LLM inference, enterprise knowledge retrieval, natural-language ERP querying, stagnant-inventory analysis, and Excel data export.

## Project Overview

```text
User
  ↓
Dify Chatflow / Workflow
  ├──→ Qwen3.5-9B via vLLM
  ├──→ RAG Knowledge Base via BGE-M3
  └──→ ERPNext REST API
              ↓
        Business Data
              ↓
      Analysis / Summary
              ↓
        Excel Export
```

## Key Features

- Local deployment of Qwen3.5-9B
- OpenAI-compatible inference API using vLLM
- Dify Chatflow and Workflow orchestration
- Enterprise RAG knowledge base
- BGE-M3 embedding service
- ERPNext REST API integration
- Natural-language ERP querying
- Stagnant-inventory identification and analysis
- Structured result export to Excel
- Linux / Docker private deployment

## Technology Stack

| Layer | Technology |
|---|---|
| LLM | Qwen3.5-9B |
| Inference | vLLM |
| GPU | NVIDIA Tesla V100 32GB |
| OS | Ubuntu 22.04 LTS |
| Workflow | Dify |
| Embedding | BGE-M3 |
| Embedding Service | Xinference |
| ERP | ERPNext |
| Integration | REST API / HTTP |
| Deployment | Docker / Linux |
| Export | Excel |

## Repository Structure

```text
qwen-dify-erpnext/
├── README.md
├── README_CN.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── qwen/
├── dify/
│   ├── workflows/
│   └── prompts/
├── erpnext/
│   ├── api/
│   ├── filters/
│   └── sample-data/
├── rag/
│   ├── sample_documents/
│   └── retrieval-tests/
├── scripts/
├── screenshots/
└── diagrams/
```

## Local Qwen Deployment

Qwen3.5-9B is deployed locally on NVIDIA Tesla V100 through vLLM and exposed through OpenAI-compatible API endpoints.

```text
dtype: float16
max_model_len: 8192
max_num_seqs: 1
gpu_memory_utilization: 0.85
```

Main endpoints:

```text
/v1/models
/v1/chat/completions
```

## Dify Orchestration

Dify provides Chatflow and Workflow orchestration, local LLM invocation, RAG retrieval, HTTP requests, ERPNext access, business-rule processing, structured result generation, and file-service integration.

## Enterprise RAG

```text
Enterprise Document
↓
Chunking
↓
BGE-M3 Embedding
↓
Vector Retrieval
↓
Relevant Context
↓
Qwen
↓
Grounded Answer
```

## ERPNext Integration

Main resources:

```text
/api/resource/Item
/api/resource/Bin
/api/resource/Stock Ledger Entry
```

## Natural-Language ERP Query

```text
User: Query the inventory of SKU001.
↓
Item-Code Extraction
↓
ERPNext API
↓
Business Data
↓
Natural-Language Result
```

## Stagnant-Inventory Analysis

```json
{
  "item_group": "Raw Material",
  "idle_days": 180,
  "min_stock_value": 50000,
  "analysis_type": "stagnant_inventory"
}
```

```text
Start
↓
Structured Condition Extraction
↓
ERPNext Bin Query
↓
Stock-Value Filtering
↓
Target-Item Iteration
↓
Stock Ledger Entry Query
↓
Idle-Day Calculation
↓
Stagnant-Item Aggregation
↓
LLM Analysis
↓
Structured Result
↓
Excel Export
```

## Validation

- Qwen API: `/v1/models`, `/v1/chat/completions`
- RAG: Document → Retrieval → Context → Qwen Answer
- ERP: Natural-Language Request → Structured Condition → ERPNext API → Result
- Stagnant Inventory: Inventory + Stock Ledger Entry + Idle-Day Calculation
- Data Export: Analysis Result → Excel File

## Technical Contribution

- Qwen3.5-9B local deployment
- NVIDIA Tesla V100 inference configuration
- vLLM API service
- Dify Workflow and Chatflow design
- BGE-M3 embedding service
- Enterprise RAG knowledge base
- ERPNext REST API integration
- Stagnant-inventory analysis
- Excel data export
- Linux and Docker deployment
- Model-serving, networking, authentication, and workflow troubleshooting

## Security Architecture

Runtime credentials are separated from source files and supplied through environment variables. Private credentials, production databases, model weights, and enterprise-confidential datasets remain outside the repository.

## License

This project is for portfolio and academic application purposes only.
Copyright © 2026 Xiaoyu. All rights reserved.
