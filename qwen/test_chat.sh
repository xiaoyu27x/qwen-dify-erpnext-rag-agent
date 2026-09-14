#!/usr/bin/env bash
BASE_URL="${LLM_BASE_URL:-http://127.0.0.1:8000/v1}"
MODEL="${LLM_MODEL:-qwen3.5-9b}"
curl -s "${BASE_URL}/chat/completions" -H "Content-Type: application/json" -d "{\"model\":\"${MODEL}\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}]}" | python3 -m json.tool
