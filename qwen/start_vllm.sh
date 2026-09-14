#!/usr/bin/env bash
set -euo pipefail
MODEL_PATH="${MODEL_PATH:-/models/qwen3.5-9b}"
SERVED_MODEL_NAME="${SERVED_MODEL_NAME:-qwen3.5-9b}"
PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"
VLLM_USE_V1=0 python -m vllm.entrypoints.openai.api_server \
  --model "$MODEL_PATH" \
  --served-model-name "$SERVED_MODEL_NAME" \
  --dtype float16 \
  --max-model-len 8192 \
  --max-num-seqs 1 \
  --gpu-memory-utilization 0.85 \
  --enforce-eager \
  --disable-log-stats \
  --port "$PORT" \
  --host "$HOST" \
  --trust-remote-code \
  --skip-mm-profiling
