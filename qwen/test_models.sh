#!/usr/bin/env bash
curl -s "${LLM_BASE_URL:-http://127.0.0.1:8000/v1}/models" | python3 -m json.tool
