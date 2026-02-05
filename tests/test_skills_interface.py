"""test_skills_interface — Asserts skills accept correct parameters.

Traceability: specs/technical.md; skills/README.md §3
Challenge: Task 3.1 — These tests SHOULD fail. Defines the empty slot the AI must fill.
"""

from __future__ import annotations

import inspect

import pytest

from skills.skill_download_youtube import download_youtube
from skills.skill_fetch_trends import fetch_trends
from skills.skill_generate_content import generate_content
from skills.skill_transcribe_audio import transcribe_audio


@pytest.mark.parametrize(
    ("func", "expected_params"),
    [
        (
            fetch_trends,
            ["resource_uri", "time_window_hours", "max_items"],
        ),
        (
            transcribe_audio,
            ["audio_url", "language_hint", "format"],
        ),
        (
            download_youtube,
            ["video_url", "format", "quality"],
        ),
        (
            generate_content,
            ["content_type", "context", "max_tokens"],
        ),
    ],
)
def test_skill_accepts_required_parameters(
    func: object, expected_params: list[str]
) -> None:
    """Each skill must accept the parameters defined in skills/README.md."""
    sig = inspect.signature(func)
    actual_params = list(sig.parameters.keys())
    for param in expected_params:
        assert param in actual_params, f"{func.__name__} must accept '{param}'"


def test_fetch_trends_returns_contract_shape() -> None:
    """skill_fetch_trends must return structure per skills/README.md §3.1."""
    result = fetch_trends("news://ethiopia/fashion/trends", max_items=1)
    assert "trends" in result and "fetched_at" in result and "resource_uri" in result
    if result["trends"]:
        trend = result["trends"][0]
        assert "relevance_score" in trend and 0.0 <= trend["relevance_score"] <= 1.0


def test_transcribe_audio_returns_contract_shape() -> None:
    """skill_transcribe_audio must return structure per skills/README.md §3.2."""
    result = transcribe_audio("https://example.com/audio.mp3")
    assert "transcript" in result and "confidence" in result
    assert 0.0 <= result["confidence"] <= 1.0


def test_download_youtube_returns_contract_shape() -> None:
    """skill_download_youtube must return structure per skills/README.md §3.3."""
    result = download_youtube("https://youtube.com/watch?v=test")
    assert "local_path" in result and "metadata" in result
    assert "title" in result["metadata"]


def test_generate_content_returns_contract_shape() -> None:
    """skill_generate_content must return structure per skills/README.md §3.4."""
    context = {"goal_description": "Test", "persona_constraints": []}
    result = generate_content("caption", context)
    assert "text_content" in result and "confidence_score" in result
    assert 0.0 <= result["confidence_score"] <= 1.0
