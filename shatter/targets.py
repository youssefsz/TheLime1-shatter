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
        caches=[
            ".next",
            ".nuxt",
            ".svelte-kit",
            ".swc",
            ".turbo",
            ".parcel-cache",
            ".eslintcache",
            ".angular",
            ".cache",
            ".docusaurus",
            ".vuepress",
            "dist",
            "build",
            "out",
            ".serverless",
            ".netlify",
            ".webpack",
        ],
        deps=["node_modules", "bower_components"],
    ),
    # ── Python ─────────────────────────────────
    Ecosystem(
        name="Python",
        caches=[
            "__pycache__",
            ".pytest_cache",
            ".mypy_cache",
            ".ruff_cache",
            ".pytype",
            ".hypothesis",
            ".pyre",
            ".eggs",
            "eggs",
            "htmlcov",
            "build",
            "dist",
        ],
        deps=[".venv", "venv", "env", "virtualenv", ".tox", ".nox", "__pypackages__"],
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
        caches=[".phpunit.cache"],
        deps=["vendor"],
    ),
    # ── Ruby ───────────────────────────────────
    Ecosystem(
        name="Ruby",
        caches=["tmp/cache", ".yardoc"],
        deps=["vendor/bundle", ".bundle"],
    ),
    # ── Java / Scala / Kotlin ──────────────────
    Ecosystem(
        name="Java / JVM",
        caches=[".gradle", "build", "target", ".bloop", ".metals"],
        deps=[],
    ),
    # ── .NET / C# ──────────────────────────────
    Ecosystem(
        name=".NET",
        caches=["bin", "obj", ".vs", "TestResults", ".ionide"],
        deps=["packages"],
    ),
    # ── Mobile (Expo / React Native) ───────────
    Ecosystem(
        name="Expo",
        caches=[".expo", ".cxx"],
        deps=[],
    ),
    # ── Dart / Flutter ─────────────────────────
    Ecosystem(
        name="Dart",
        caches=[".dart_tool", "build"],
        deps=[".pub-cache"],
    ),
    # ── C / C++ ────────────────────────────────
    Ecosystem(
        name="C/C++",
        caches=[
            "cmake-build-debug",
            "cmake-build-release",
            "out",
            "bin",
            ".cache",
            "CMakeFiles",
            ".ccls-cache",
        ],
        deps=[],
    ),
    # ── Swift / macOS / iOS ────────────────────
    Ecosystem(
        name="Swift",
        caches=["DerivedData", ".build", ".swiftpm"],
        deps=["Pods", "Carthage"],
    ),
    # ── Elixir / Erlang ────────────────────────
    Ecosystem(
        name="Elixir",
        caches=["_build", ".elixir_ls"],
        deps=["deps"],
    ),
    # ── Haskell ────────────────────────────────
    Ecosystem(
        name="Haskell",
        caches=["dist", "dist-newstyle", ".stack-work"],
        deps=[],
    ),
    # ── Clojure ────────────────────────────────
    Ecosystem(
        name="Clojure",
        caches=["target", ".cpcache", ".shadow-cljs"],
        deps=[],
    ),
    # ── OCaml ──────────────────────────────────
    Ecosystem(
        name="OCaml",
        caches=["_build"],
        deps=[],
    ),
    # ── Zig ────────────────────────────────────
    Ecosystem(
        name="Zig",
        caches=["zig-cache", "zig-out"],
        deps=[],
    ),
    # ── Nim ────────────────────────────────────
    Ecosystem(
        name="Nim",
        caches=["nimcache"],
        deps=[],
    ),
    # ── Game Engines (Unity, Godot, Unreal) ────
    Ecosystem(
        name="Unity",
        caches=["Library", "Logs", "obj", "Temp", "MemoryCaptures", "Builds"],
        deps=[],
    ),
    Ecosystem(
        name="Godot",
        caches=[".godot"],
        deps=[],
    ),
    Ecosystem(
        name="Unreal Engine",
        caches=["Binaries", "Build", "DerivedDataCache", "Intermediate", "Saved"],
        deps=[],
    ),
    # ── Data Science / R ───────────────────────
    Ecosystem(
        name="R",
        caches=[".Rproj.user", ".Rhistory"],
        deps=["renv"],
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
