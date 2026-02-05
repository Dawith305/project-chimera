# Project Chimera — OpenClaw Integration Plan

**Version:** 1.0  
**Status:** Optional / Forward-Looking  
**Traceability:** Architecture Strategy §8, SRS Agent Social Protocols

---

## 1. Context

OpenClaw represents an emerging **Agent Social Network** — a protocol layer where AI agents can discover each other, broadcast capabilities, and interoperate. As autonomous influencer agents become first-class participants in digital ecosystems, Chimera must be able to:

- Publish its **availability** and **status** to the network
- Advertise **capabilities** (e.g. content creation, trend analysis)
- Participate in **agent-to-agent** protocols (identity, provenance, negotiation)

This document defines a plan for how Chimera will integrate with OpenClaw-style networks. Implementation is **not** required for Day 2–3 deliverables but establishes the specification for future work.

---

## 2. Integration Objectives

| Objective | Description |
|-----------|-------------|
| **Availability Broadcast** | Chimera agents announce when they are online, idle, or busy |
| **Status Publication** | Current state (Planning, Working, Judging, Sleeping) is discoverable |
| **Capability Advertisement** | Agents declare what they can do (e.g. video generation, trend analysis) |
| **Identity & Provenance** | Cryptographic identity for attribution and trust |
| **Negotiation Readiness** | Structured message formats for future agent-to-agent deals |

---

## 3. Proposed Status Payload

When publishing to OpenClaw, Chimera agents emit a standardized status object:

```json
{
  "agent_id": "chimera-agent-uuid",
  "agent_name": "string",
  "status": "available | busy | sleeping | maintenance",
  "sub_status": "planning | working | judging | idle",
  "capabilities": [
    "content_generation",
    "trend_analysis",
    "social_engagement",
    "video_production"
  ],
  "platforms": ["twitter", "instagram", "tiktok"],
  "timestamp": "ISO8601",
  "signature": "optional-crypto-signature"
}
```

| Field | Purpose |
|-------|---------|
| `agent_id` | Unique Chimera agent identifier |
| `status` | High-level availability |
| `sub_status` | Aligns with Planner/Worker/Judge lifecycle |
| `capabilities` | What the agent can do |
| `platforms` | Where the agent operates |
| `signature` | For future cryptographic provenance |

---

## 4. Publication Mechanisms (Options)

### 4.1 MCP Resource Exposure
- Expose a Chimera MCP Resource: `chimera://agent/{id}/status`
- OpenClaw or other agents poll this resource to discover Chimera status
- Aligns with MCP-first architecture

### 4.2 Push to Registry
- Chimera pushes status to an OpenClaw registry endpoint (when protocol is defined)
- Requires outbound HTTP/SSE from Chimera to registry
- Enables real-time discovery without polling

### 4.3 Event Stream
- Publish status changes to an event stream (e.g. Redis Pub/Sub, Kafka)
- External adapters consume and forward to OpenClaw
- Decouples Chimera core from network specifics

**Recommendation:** Start with **4.1 (MCP Resource)**. It requires no new outbound dependencies and fits the existing MCP topology. Add 4.2 or 4.3 when OpenClaw protocol is stable.

---

## 5. Agent-to-Agent Social Protocols (Planned)

Per Architecture Strategy §8, Chimera should support:

| Protocol | Description | Priority |
|----------|-------------|----------|
| **Identity** | Cryptographic agent identity (e.g. DID) | P2 |
| **Provenance** | Signed content and action claims | P2 |
| **Availability** | Status broadcast (this doc) | P1 |
| **Negotiation** | Structured messages for deals/collaboration | P3 |
| **Reputation** | Verified outcome signals | P3 |
| **Safety Taxonomy** | Shared escalation and sensitivity codes | P2 |

---

## 6. Implementation Phases

| Phase | Scope | Deliverable |
|-------|-------|--------------|
| **Phase 0** | Spec only | This document |
| **Phase 1** | MCP Resource for status | `chimera://agent/{id}/status` returns JSON payload |
| **Phase 2** | Identity & signing | Agent keys; signed status payloads |
| **Phase 3** | Registry integration | Push to OpenClaw when protocol exists |
| **Phase 4** | Full protocol support | Negotiation, reputation, safety taxonomy |

---

## 7. Constraints & Risks

- **Protocol volatility:** OpenClaw and similar networks are evolving. Design for extension.
- **Security:** Status must not leak internal state (task details, credentials).
- **Governance:** Any agent-to-agent interaction must pass through Judge/HITL if it affects Chimera state.

---

## 8. Traceability

| Source | This Spec |
|--------|-----------|
| Challenge: OpenClaw Integration | §3, §4 |
| Architecture Strategy §8 | §5 |
| SRS Agent Social Protocols | §5 |
| REPORT §3 | §5 |
