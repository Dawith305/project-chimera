# Project Chimera

An **autonomous influencer system** — a fleet of goal-directed digital entities that research trends, generate content, and manage engagement without continuous human intervention. Uses a **Planner → Worker → Judge** swarm architecture, MCP-first integration, and governance-over-autonomy principles.

---

## Quick Start

```bash
make setup      # Install dependencies (uv sync)
make test       # Run full CI pipeline in Docker (lint, security, tests)
make spec-check # Verify code aligns with specs
make verify-mcp # Ensure .cursor/mcp.json exists and references Tenx
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [specs/](specs/) | Functional, technical, and meta specifications |
| [REPORT.md](REPORT.md) | Research summary, architecture, and Day 1 decisions |

---

## Prime Directive (for AI Agents)

**NEVER generate code without checking specs/ first.**

1. Read the relevant spec: `specs/_meta.md`, `specs/functional.md`, `specs/technical.md`
2. Align implementation with API contracts, schemas, and user stories
3. If no spec exists for what you are building, create or extend the spec before coding
4. Ambiguity is the enemy of AI — vague specs lead to hallucination
