# skill_download_youtube

**Traceability:** Content ingestion, remixing, transcription pipeline

## Purpose

Download video or audio from YouTube for content ingestion, remixing, or transcription.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `video_url` | string | Yes | YouTube URL |
| `format` | string | No | `video` (mp4) or `audio` (m4a/mp3), default `video` |
| `quality` | string | No | `high`, `medium`, or `low`, default `medium` |

## Output Contract

| Field | Type | Description |
|-------|------|-------------|
| `local_path` | string | Path to downloaded file |
| `format` | string | Echo of requested format |
| `duration_seconds` | number | Video/audio duration |
| `resolution` | string | e.g. `1920x1080` (video only) |
| `file_size_bytes` | number | File size |
| `checksum` | string | Integrity hash |
| `metadata` | object | `title`, `channel`, `published_at` |

## Implementation Notes

- Will use yt-dlp or equivalent
- Must respect platform ToS and rate limits
- Structure ready; logic to be implemented
