"""test_trend_fetcher — Asserts trend data structure matches API contract.

Traceability: specs/functional.md P-01, P-04; specs/technical.md; skills/README.md §3.1
Challenge: Task 3.1 — These tests SHOULD fail. Defines the empty slot the AI must fill.
"""

from __future__ import annotations

from skills.skill_fetch_trends import fetch_trends

REQUIRED_TOP_LEVEL_KEYS = ("trends", "fetched_at", "resource_uri")
REQUIRED_TREND_KEYS = ("id", "title", "summary", "source", "published_at", "relevance_score")


def test_trend_fetcher_returns_valid_structure() -> None:
    """P-01: Trend data structure matches API contract per specs/technical.md."""
    result = fetch_trends("news://test/trends", max_items=5)

    assert "trends" in result, "Result must contain 'trends' key"
    assert "fetched_at" in result, "Result must contain 'fetched_at' key"
    assert "resource_uri" in result, "Result must contain 'resource_uri' key"

    assert result["resource_uri"] == "news://test/trends"

    trends = result["trends"]
    assert isinstance(trends, list), "trends must be a list"

    for trend in trends:
        for key in REQUIRED_TREND_KEYS:
            assert key in trend, f"Each trend must have '{key}'"
        assert 0.0 <= trend["relevance_score"] <= 1.0, "relevance_score must be 0.0-1.0"


def test_trend_fetcher_respects_max_items() -> None:
    """P-01: Result respects max_items parameter."""
    result = fetch_trends("news://test/trends", max_items=3)
    assert len(result["trends"]) <= 3, "Must not exceed max_items"
