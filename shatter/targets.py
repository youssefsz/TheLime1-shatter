"""
targets.py — Ecosystem target registry.

To add a new ecosystem, simply append a new entry to ECOSYSTEMS.
The core engine reads from this registry — no other files need to change.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Ecosystem:
    """Represents a language / framework ecosystem and the directories it generates."""

    name: str
    caches: list[str] = field(default_factory=list)
    deps: list[str] = field(default_factory=list)


# ──────────────────────────────────────────────
#  REGISTRY — add new ecosystems here
# ──────────────────────────────────────────────

ECOSYSTEMS: list[Ecosystem] = [
    # ── JavaScript / TypeScript ────────────────
    Ecosystem(
        name="JavaScript",
        caches=[".next", ".nuxt", ".svelte-kit", ".swc", ".turbo", ".parcel-cache"],
        deps=["node_modules"],
    ),
    # ── Python ─────────────────────────────────
    Ecosystem(
        name="Python",
        caches=["__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".pytype"],
        deps=[".venv", "venv", ".tox", ".nox"],
    ),
    # ── Rust ───────────────────────────────────
    Ecosystem(
        name="Rust",
        caches=[],
        deps=["target"],
    ),
    # ── Go ─────────────────────────────────────
    Ecosystem(
        name="Go",
        caches=[],
        deps=["vendor"],
    ),
    # ── PHP ────────────────────────────────────
    Ecosystem(
        name="PHP",
        caches=[],
        deps=["vendor"],
    ),
    # ── Ruby ───────────────────────────────────
    Ecosystem(
        name="Ruby",
        caches=[],
        deps=["vendor/bundle"],
    ),
    # ── Java / Kotlin ──────────────────────────
    Ecosystem(
        name="Java",
        caches=[".gradle", "build"],
        deps=[],
    ),
    # ── .NET / C# ──────────────────────────────
    Ecosystem(
        name=".NET",
        caches=["bin", "obj"],
        deps=[],
    ),
    # ── Expo / React Native ────────────────────
    Ecosystem(
        name="Expo",
        caches=[".expo"],
        deps=[],
    ),
    # ── Dart / Flutter ─────────────────────────
    Ecosystem(
        name="Dart",
        caches=[".dart_tool", "build"],
        deps=[],
    ),
]


def _collect(attr: str) -> set[str]:
    """Gather all unique directory names for a given attribute across ecosystems."""
    names: set[str] = set()
    for eco in ECOSYSTEMS:
        names.update(getattr(eco, attr))
    return names


ALL_CACHE_DIRS: set[str] = _collect("caches")
ALL_DEP_DIRS: set[str] = _collect("deps")
ALL_TARGET_DIRS: set[str] = ALL_CACHE_DIRS | ALL_DEP_DIRS
