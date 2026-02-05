# Project Chimera — Functional Specification

**Version:** 1.0  
**Traceability:** SRS Sections 4.x, Architecture Strategy

---

## 1. User Stories (Agent Perspective)

User stories are written from the perspective of the **Planner**, **Worker**, or **Judge** agents. These define the executable intent for the system.

---

### 1.1 Perception & Ingestion

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| P-01 | Planner | Fetch trends from configured MCP Resources (e.g. `news://ethiopia/fashion/trends`) | I can detect content opportunities and feed them into the task DAG |
| P-02 | Planner | Poll social mentions via MCP Resources (e.g. `twitter://mentions/recent`) | I can create reply tasks for relevant interactions |
| P-03 | Planner | Pass ingested content through a semantic relevance filter | I only create tasks for content that exceeds the relevance threshold (e.g. 0.75) |
| P-04 | Planner | Receive trend alerts from a background Trend Spotter Worker | I can react to emerging topic clusters and plan content accordingly |

---

### 1.2 Planning & Task Decomposition

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| PL-01 | Planner | Decompose campaign goals into a directed acyclic graph (DAG) of tasks | Workers can execute atomic units of work in parallel |
| PL-02 | Planner | Push tasks to the TaskQueue (Redis) with correct priority and context | Workers know what to do and under what constraints |
| PL-03 | Planner | Replan when a Worker fails or the Judge rejects output | The system recovers from errors without manual intervention |
| PL-04 | Planner | Read GlobalState (campaign goals, budget, persona constraints) before creating tasks | Tasks align with current strategy and policy |

---

### 1.3 Content Generation (Worker)

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| W-01 | Worker | Pull a single task from the TaskQueue | I execute one atomic unit of work with maximum focus |
| W-02 | Worker | Generate text (captions, scripts, replies) using the Cognitive Core | Content is persona-consistent and context-aware |
| W-03 | Worker | Generate images via MCP Tools (e.g. `mcp-server-ideogram`) with `character_reference_id` | Visual content maintains character consistency |
| W-04 | Worker | Generate video via MCP Tools (e.g. `mcp-server-runway`) using tiered strategy (image-to-video vs text-to-video) | We balance quality and cost for daily vs hero content |
| W-05 | Worker | Retrieve relevant memories from Weaviate via MCP before generating | Output is coherent with past interactions and persona |
| W-06 | Worker | Push results to the ReviewQueue with `confidence_score` metadata | The Judge can route based on quality and safety |

---

### 1.4 Validation & Governance (Judge)

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| J-01 | Judge | Pop results from the ReviewQueue | I validate every Worker output before it affects state |
| J-02 | Judge | Compare output against Planner acceptance criteria, persona constraints, and safety guidelines | Only compliant content is committed |
| J-03 | Judge | Route to HITL when `confidence_score` is 0.70–0.90 or content triggers sensitive-topic filters | Humans review borderline or risky content |
| J-04 | Judge | Reject and signal replan when `confidence_score` < 0.70 | Low-quality output is never published |
| J-05 | Judge | Auto-approve when `confidence_score` > 0.90 and no sensitive topics | High-quality output flows without blocking |
| J-06 | Judge | Verify `state_version` before commit (OCC) | Stale updates are rejected to prevent race conditions |
| J-07 | Judge | Validate image consistency (generated vs reference) using a vision-capable model | Character lock is enforced |

---

### 1.5 Publishing & Social Action

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| A-01 | Worker | Execute social actions (post, reply, like) via MCP Tools only | Platform logic is centralized and auditable |
| A-02 | Worker | Include platform-native AI disclosure flags when publishing | We comply with AI transparency requirements |
| A-03 | Judge | Approve social actions only after content validation | No unvetted content reaches public channels |

---

### 1.6 Persona & Memory

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| M-01 | System | Load agent persona from SOUL.md (backstory, voice, directives) | Persona is version-controlled and consistent |
| M-02 | Worker | Query Weaviate for semantically relevant memories before reasoning | Long-term coherence is maintained |
| M-03 | Judge | Trigger background summarization of high-engagement interactions | Persona can evolve based on successful outcomes |

---

### 1.7 Human-in-the-Loop (HITL)

| ID | As a... | I need to... | So that... |
|----|---------|--------------|-------------|
| H-01 | Human Reviewer | Receive escalated tasks in a Review Interface | I can Approve, Reject, or Edit agent-generated content |
| H-02 | Human Reviewer | See `confidence_score`, `reasoning_trace`, and content | I have context to make informed decisions |
| H-03 | System | Not block other tasks while HITL items are pending | Throughput is preserved under management by exception |

---

## 2. Acceptance Criteria Summary

- **P-01 to P-04:** Perception flows through MCP Resources; semantic filter gates task creation.
- **PL-01 to PL-04:** Planner produces valid task DAGs; replanning is reactive.
- **W-01 to W-06:** Workers are stateless, use MCP for all external calls, and push scored results.
- **J-01 to J-07:** Judge is the sole gatekeeper; OCC and HITL routing are enforced.
- **A-01 to A-03:** Social actions are MCP-mediated and disclosure-compliant.
- **M-01 to M-03:** Persona and memory are RAG-augmented and evolvable.
- **H-01 to H-03:** HITL is non-blocking and context-rich.

---

## 3. Traceability

| SRS Section | This Spec |
|-------------|-----------|
| FR 1.0–1.2 (Cognitive Core) | M-01, M-02, M-03; W-05 |
| FR 2.0–2.2 (Perception) | P-01, P-02, P-03, P-04 |
| FR 3.0–3.2 (Creative Engine) | W-02, W-03, W-04; J-07 |
| FR 4.0–4.1 (Action System) | A-01, A-02, A-03 |
| FR 6.0–6.1 (Orchestration) | PL-01 to PL-04; J-01 to J-07 |
| NFR 1.0–1.2 (HITL) | J-03, J-04, J-05; H-01 to H-03 |
