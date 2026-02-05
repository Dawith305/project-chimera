# skill_fetch_trends

**Traceability:** specs/functional.md P-01, P-04

## Purpose

Fetch trend data from configured MCP Resources for the Planner to detect content opportunities and feed the task DAG.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `resource_uri` | string | Yes | MCP Resource URI (e.g. `news://ethiopia/fashion/trends`) |
| `time_window_hours` | number | No | How far back to look (default 24) |
| `max_items` | number | No | Max items to return (default 20) |

## Output Contract

| Field | Type | Description |
|-------|------|-------------|
| `trends` | array | List of trend objects with `id`, `title`, `summary`, `source`, `published_at`, `relevance_score` |
| `fetched_at` | string | ISO8601 timestamp |
| `resource_uri` | string | Echo of input |

## Implementation Notes

- Consumes MCP Resources via `news://`, `mcp://` schemes
- Semantic relevance filter (P-03) may be applied downstream
- Structure ready; logic to be implemented per specs/technical.md
