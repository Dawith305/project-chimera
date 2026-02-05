# skill_generate_content

**Traceability:** specs/functional.md W-02, specs/technical.md Worker Result schema

## Purpose

Generate persona-consistent text (captions, scripts, replies, posts) using the Cognitive Core. Output includes confidence score for Judge routing.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content_type` | string | Yes | `caption`, `script`, `reply`, or `post` |
| `context` | object | Yes | `goal_description`, `persona_constraints`, optional `memory_context`, `platform` |
| `max_tokens` | number | No | Max output length (default 500) |

## Output Contract

| Field | Type | Description |
|-------|------|-------------|
| `text_content` | string | Generated text |
| `content_type` | string | Echo of input |
| `confidence_score` | number | 0.0–1.0 for Judge HITL routing |
| `reasoning_trace` | string | Optional LLM reasoning for audit |

## Implementation Notes

- Will call LLM via MCP or direct API
- Must hydrate persona from SOUL.md and Weaviate memory (M-01, M-02)
- `confidence_score` feeds Judge routing (J-03, J-04, J-05)
- Structure ready; logic to be implemented
