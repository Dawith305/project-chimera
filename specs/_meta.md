# Project Chimera — Specification Meta

**Version:** 1.0  
**Last Updated:** February 5, 2026  
**Status:** Ratified (Task 2.1)

---

## 1. Vision

Project Chimera is an **Autonomous Influencer Network** — a system of goal-directed digital entities that research trends, generate content, and manage engagement without continuous human intervention.

Chimera is **not** a static scheduling tool. It is a fleet of persistent agents capable of:
- **Perception** — ingesting trends, mentions, and market signals
- **Reasoning** — planning and decomposing goals into executable tasks
- **Creation** — producing multimodal content (text, images, video)
- **Action** — publishing to social platforms and optionally transacting on-chain

The system is designed for scale: a single human Orchestrator can manage thousands of virtual influencers through a **Planner → Worker → Judge** swarm architecture.

---

## 2. Strategic Constraints

### 2.1 Spec-Driven Development (SDD)
- **No implementation code** until the relevant specification is ratified.
- All agents, skills, and integrations must trace back to a spec.
- Ambiguity is the enemy of AI — vague specs lead to hallucination.

### 2.2 MCP-First Integration
- Agents **never** call external APIs directly.
- All external interaction flows through MCP servers (social, vector DB, media, commerce, news).
- MCP is the integration boundary and device-driver layer.

### 2.3 Governance Over Autonomy
- All state-changing actions pass through the Judge.
- Human-in-the-Loop (HITL) is mandatory for low-confidence or sensitive content.
- Optimistic Concurrency Control (OCC) prevents stale commits.

### 2.4 Traceability
- Tenx MCP Sense (or equivalent) must remain connected during development.
- Commit history should tell a story of evolving complexity.
- Every change should be traceable to a requirement or spec.

---

## 3. Architectural Principles

| Principle | Implication |
|-----------|-------------|
| **Hierarchical Swarm** | Planner decomposes goals; Workers execute; Judge validates and commits. |
| **Stateless Workers** | Workers are ephemeral, horizontally scalable, and do not hold governance authority. |
| **Single Gatekeeper** | The Judge is the sole authority for approving, rejecting, or escalating outputs. |
| **Management by Exception** | Humans intervene only when confidence is low or content is sensitive. |
| **Postgres as System of Record** | Transactional data lives in Postgres; Weaviate for semantic memory; Redis for queues. |

---

## 4. Out of Scope (This Specification)

- Implementation of MCP servers (assumed to exist or be provided)
- Full Agentic Commerce / Coinbase AgentKit integration (Phase 3)
- OpenClaw network deployment (planned in `openclaw_integration.md`)
- Multi-tenancy and PaaS licensing model (future phase)

---

## 5. Related Documents

| Document | Purpose |
|----------|---------|
| `functional.md` | User stories and agent-facing requirements |
| `technical.md` | API contracts, database schema, tool definitions |
| `openclaw_integration.md` | Plan for publishing availability/status to OpenClaw |
| `../research/architecture_strategy.md` | Architectural rationale and diagrams |

---

## 6. Approval

This meta specification establishes the high-level vision and constraints for Project Chimera. All downstream specs (`functional.md`, `technical.md`) must align with these principles.
