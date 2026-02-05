# Project Chimera — Standardised Commands
# Traceability: Task 3.2
# Eliminates "It works on my machine" via Docker and consistent tooling

.PHONY: setup test test-local spec-check docker-build docker-test

# Install dependencies (local dev)
setup:
	uv sync

# Run tests in Docker (consistent environment, primary)
test: docker-test

# Run tests locally (when Docker unavailable)
test-local:
	uv run pytest tests/ -v --tb=short

# Verify code aligns with specs
spec-check:
	@chmod +x scripts/spec-check.sh 2>/dev/null || true
	@./scripts/spec-check.sh

# Build Docker image for tests
docker-build:
	docker build -t project-chimera:test .

# Run tests inside Docker container
docker-test: docker-build
	docker run --rm project-chimera:test
