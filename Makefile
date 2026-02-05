# Project Chimera — Standardised Commands
# Traceability: Task 3.2, Governance Pipeline
# Eliminates "It works on my machine" via Docker and consistent tooling

.PHONY: setup test test-local lint security spec-check verify-mcp ci docker-build docker-test

# Install dependencies (local dev)
setup:
	uv sync --extra dev

# Full CI pipeline in Docker (lint + security + test)
test: docker-test
ci: docker-test

# Run tests locally (when Docker unavailable)
test-local:
	uv run pytest tests/ -v --tb=short

# Lint (local)
lint:
	uv run ruff check . --output-format=concise
	uv run ruff format --check .

# Security audit (local)
security:
	uv run pip-audit

# Verify code aligns with specs
spec-check:
	@chmod +x scripts/spec-check.sh 2>/dev/null || true
	@./scripts/spec-check.sh

# Ensure MCP config exists and references Tenx/10academy
verify-mcp:
	@test -f .cursor/mcp.json || (echo "Error: .cursor/mcp.json not found"; exit 1)
	@grep -qE 'tenx|10academy' .cursor/mcp.json || (echo "Error: .cursor/mcp.json must reference tenx or 10academy"; exit 1)
	@echo "MCP config OK"

# Build Docker image
docker-build:
	docker build -t project-chimera:test .

# Run full pipeline in Docker (lint, security, test)
docker-test: docker-build
	docker run --rm project-chimera:test
