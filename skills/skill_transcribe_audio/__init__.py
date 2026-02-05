"""skill_transcribe_audio — Transcribe audio/video to text.

Traceability: skills/README.md §3.2
"""

from __future__ import annotations


def transcribe_audio(
    audio_url: str,
    language_hint: str | None = None,
    format: str = "text",
) -> dict:
    """Transcribe audio or video to text.

    Args:
        audio_url: URL or path to audio/video file.
        language_hint: ISO 639-1 code (e.g. en, am).
        format: Output format: text, srt, or json.

    Returns:
        Dict with: transcript, format, duration_seconds, language_detected,
        segments (optional), confidence.

    Raises:
        NotImplementedError: Implementation pending (TDD empty slot).
    """
    raise NotImplementedError("skill_transcribe_audio: implementation pending")
