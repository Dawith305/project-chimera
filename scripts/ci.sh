#!/usr/bin/env bash
# CI — Linting, Security, Testing
# Traceability: Governance Pipeline (rubric)
# Runs in Docker for consistent output

set -e
cd "$(dirname "$0")/.."

echo "=== Lint (ruff) ==="
uv run ruff check . --output-format=concise

echo ""
echo "=== Format (ruff) ==="
uv run ruff format --check .

echo ""
echo "=== Security (pip-audit) ==="
uv run pip-audit

echo ""
echo "=== Test (pytest) ==="
uv run pytest tests/ -v --tb=short
