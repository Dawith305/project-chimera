#!/usr/bin/env bash
# spec-check — Verifies code aligns with specs
# Traceability: Task 3.2, specs/_meta.md §2.4
# Exit 0: pass, Exit 1: fail

set -e
cd "$(dirname "$0")/.."

ERRORS=0

# 1. Required spec files exist
for f in specs/_meta.md specs/functional.md specs/technical.md; do
  if [[ ! -f "$f" ]]; then
    echo "FAIL: Missing required spec: $f"
    ERRORS=$((ERRORS + 1))
  fi
done

# 2. Test files reference specs
for f in tests/*.py; do
  [[ -f "$f" ]] || continue
  if ! grep -q "specs/" "$f" 2>/dev/null; then
    echo "FAIL: $f has no spec traceability (add specs/ reference in docstring)"
    ERRORS=$((ERRORS + 1))
  fi
done

# 3. Skill modules have traceability
for f in skills/skill_*/*.py; do
  [[ -f "$f" ]] || continue
  if ! grep -q "Traceability\|specs/" "$f" 2>/dev/null; then
    echo "FAIL: $f has no spec traceability"
    ERRORS=$((ERRORS + 1))
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  echo "spec-check: $ERRORS failure(s)"
  exit 1
fi

echo "spec-check: OK (specs present, traceability verified)"
exit 0
