"""skill_download_youtube — Download video/audio from YouTube.

Traceability: skills/README.md §3.3
"""

from __future__ import annotations


def download_youtube(
    video_url: str,
    format: str = "video",
    quality: str = "medium",
) -> dict:
    """Download video or audio from YouTube.

    Args:
        video_url: YouTube URL.
        format: video (mp4) or audio (m4a/mp3).
        quality: high, medium, or low.

    Returns:
        Dict with: local_path, format, duration_seconds, resolution,
        file_size_bytes, checksum, metadata.

    Raises:
        NotImplementedError: Implementation pending (TDD empty slot).
    """
    raise NotImplementedError("skill_download_youtube: implementation pending")
