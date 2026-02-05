# skill_transcribe_audio

**Traceability:** Content pipeline, video processing workflows

## Purpose

Transcribe audio or video to text for content processing, accessibility, and downstream LLM analysis.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `audio_url` | string | Yes | URL or path to audio/video file |
| `language_hint` | string | No | ISO 639-1 code (e.g. `en`, `am`) |
| `format` | string | No | Output format: `text`, `srt`, or `json` (default `text`) |

## Output Contract

| Field | Type | Description |
|-------|------|-------------|
| `transcript` | string | Full transcript text |
| `format` | string | Echo of requested format |
| `duration_seconds` | number | Media duration |
| `language_detected` | string | Detected language code |
| `segments` | array | Optional timed segments `{start, end, text}` |
| `confidence` | number | 0.0–1.0 |

## Implementation Notes

- Will use MCP Tool or local service (e.g. Whisper, cloud ASR)
- Structure ready; logic to be implemented
