# Project Chimera — Test & Dev Environment
# Traceability: Task 3.2, specs/_meta.md
# Ensures consistent output regardless of host ("It works on my machine" → eliminated)

FROM python:3.11-slim

# Install uv for fast, reproducible dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

# Dependencies first (better layer caching)
COPY pyproject.toml uv.lock ./
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
RUN uv sync --frozen

# Application source
COPY skills/ skills/
COPY tests/ tests/
COPY specs/ specs/

# Ensure Python can find project modules
ENV PYTHONPATH=/app

# Default: run tests
CMD ["uv", "run", "pytest", "tests/", "-v", "--tb=short"]
