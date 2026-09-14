#!/usr/bin/env bash
set -euo pipefail
python3 scripts/test_qwen.py
python3 scripts/test_erpnext.py
