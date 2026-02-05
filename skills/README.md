# Chimera Agent Skills

**Version:** 1.0  
**Traceability:** Task 2.3 Sub-Task B, specs/functional.md, specs/technical.md

---

## 1. Overview

A **Skill** is a specific capability package that Chimera agents (Planner, Worker, Judge) invoke to perform atomic tasks. Skills are reusable functions or scripts — distinct from **MCP Servers**, which are external bridges (e.g. database connector, social platform API).

| Concept | Definition | Example |
|---------|------------|---------|
| **Skill** | Reusable capability package the agent calls | `skill_fetch_trends`, `skill_transcribe_audio` |
| **MCP Server** | External bridge exposing Tools/Resources | mcp-server-twitter, mcp-server-weaviate |

Skills may *use* MCP Tools internally but expose a clean, typed interface to the agent.

---

## 2. Skill Inventory

| Skill | Purpose | Used By | Spec Reference |
|-------|---------|---------|-----------------|
| `skill_fetch_trends` | Fetch trends from news/resources | Planner | P-01, P-04 |
| `skill_transcribe_audio` | Transcribe audio/video to text | Worker | Content pipeline |
| `skill_download_youtube` | Download video/audio from YouTube | Worker | Content ingestion |
| `skill_generate_content` | Generate persona-consistent text | Worker | W-02 |

---

## 3. Skill Definitions (Input/Output Contracts)

### 3.1 skill_fetch_trends

**Purpose:** Fetch trend data from configured MCP Resources (e.g. `news://ethiopia/fashion/trends`) for the Planner to detect content opportunities.

**Input Contract:**

```json
{
  "resource_uri": "string (required)",
  "time_window_hours": "number (optional, default 24)",
  "max_items": "number (optional, default 20)"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `resource_uri` | string | Yes | MCP Resource URI (e.g. `news://ethiopia/fashion/trends`) |
| `time_window_hours` | number | No | How far back to look (default 24) |
| `max_items` | number | No | Max items to return (default 20) |

**Output Contract:**

```json
{
  "trends": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "source": "string",
      "published_at": "ISO8601",
      "relevance_score": "number (0.0-1.0)"
    }
  ],
  "fetched_at": "ISO8601",
  "resource_uri": "string"
}
```

**Implementation:** Calls MCP Resource via `mcp://` scheme. No implementation required yet; structure only.

---

### 3.2 skill_transcribe_audio

**Purpose:** Transcribe audio or video to text. Used for content processing, accessibility, and downstream LLM analysis.

**Input Contract:**

```json
{
  "audio_url": "string (required)",
  "language_hint": "string (optional, e.g. 'en', 'am')",
  "format": "string (optional: 'text' | 'srt' | 'json', default 'text')"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `audio_url` | string | Yes | URL or path to audio/video file |
| `language_hint` | string | No | ISO 639-1 code for better accuracy |
| `format` | string | No | Output format: `text`, `srt`, or `json` |

**Output Contract:**

```json
{
  "transcript": "string",
  "format": "string",
  "duration_seconds": "number",
  "language_detected": "string",
  "segments": [
    {
      "start": "number",
      "end": "number",
      "text": "string"
    }
  ],
  "confidence": "number (0.0-1.0)"
}
```

**Implementation:** Will use MCP Tool or local transcription service (e.g. Whisper). Structure only for now.

---

### 3.3 skill_download_youtube

**Purpose:** Download video or audio from YouTube for content ingestion, remixing, or transcription.

**Input Contract:**

```json
{
  "video_url": "string (required)",
  "format": "string (optional: 'video' | 'audio', default 'video')",
  "quality": "string (optional: 'high' | 'medium' | 'low', default 'medium')"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `video_url` | string | Yes | YouTube URL (e.g. `https://youtube.com/watch?v=...`) |
| `format` | string | No | `video` (mp4) or `audio` (m4a/mp3) |
| `quality` | string | No | Resolution/bitrate tier |

**Output Contract:**

```json
{
  "local_path": "string",
  "format": "string",
  "duration_seconds": "number",
  "resolution": "string (e.g. '1920x1080')",
  "file_size_bytes": "number",
  "checksum": "string",
  "metadata": {
    "title": "string",
    "channel": "string",
    "published_at": "string"
  }
}
```

**Implementation:** Will use yt-dlp or equivalent. Structure only for now.

---

### 3.4 skill_generate_content

**Purpose:** Generate persona-consistent text (captions, scripts, replies) using the Cognitive Core. Aligns with W-02.

**Input Contract:**

```json
{
  "content_type": "string (required: 'caption' | 'script' | 'reply' | 'post')",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "memory_context": "string (optional)",
    "platform": "string (optional)"
  },
  "max_tokens": "number (optional, default 500)"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content_type` | string | Yes | `caption`, `script`, `reply`, or `post` |
| `context` | object | Yes | Goal, persona, optional memory, platform |
| `max_tokens` | number | No | Max output length |

**Output Contract:**

```json
{
  "text_content": "string",
  "content_type": "string",
  "confidence_score": "number (0.0-1.0)",
  "reasoning_trace": "string (optional)"
}
```

**Implementation:** Will call LLM via MCP or direct API. Structure only for now.

---

## 4. Directory Structure

```
skills/
├── README.md                 # This file
├── skill_fetch_trends/
│   └── README.md             # Detailed I/O, dependencies
├── skill_transcribe_audio/
│   └── README.md
├── skill_download_youtube/
│   └── README.md
└── skill_generate_content/
    └── README.md
```

Each subdirectory contains a README with full contract details and future implementation notes.

---

## 5. Traceability

| Functional Spec | Skill |
|-----------------|-------|
| P-01, P-04 | skill_fetch_trends |
| W-02 | skill_generate_content |
| Content pipeline | skill_transcribe_audio, skill_download_youtube |

| Technical Spec | Mapping |
|----------------|--------|
| MCP Resource URIs | skill_fetch_trends consumes these |
| Worker Result schema | skill_generate_content outputs `confidence_score` |
