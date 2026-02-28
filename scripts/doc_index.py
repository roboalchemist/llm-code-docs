#!/usr/bin/env python3
"""
doc-index: Pre-computed documentation source index.

Maps library_name → [doc_urls] so auto_doc.py can skip expensive web searches
when we already know where documentation lives.

Usage:
    python3 scripts/doc_index.py build devdocs
    python3 scripts/doc_index.py build all
    python3 scripts/doc_index.py build --list
    python3 scripts/doc_index.py lookup react
    python3 scripts/doc_index.py lookup fastapi --json
    python3 scripts/doc_index.py stats
    python3 scripts/doc_index.py export --format json
"""

import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import typer

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR / "doc_index.db"

app = typer.Typer(help="Documentation source index for auto-doc pipeline.")


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

_SCHEMA = """\
CREATE TABLE IF NOT EXISTS libraries (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    display_name TEXT NOT NULL,
    language TEXT,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS doc_sources (
    id INTEGER PRIMARY KEY,
    library_id INTEGER NOT NULL REFERENCES libraries(id),
    platform TEXT NOT NULL,
    doc_url TEXT NOT NULL,
    doc_type TEXT,
    quality_signals TEXT,
    last_checked TEXT,
    UNIQUE(library_id, platform)
);

CREATE TABLE IF NOT EXISTS platforms (
    name TEXT PRIMARY KEY,
    last_synced TEXT,
    total_entries INTEGER,
    api_url TEXT
);

CREATE INDEX IF NOT EXISTS idx_libraries_name ON libraries(name);
CREATE INDEX IF NOT EXISTS idx_doc_sources_library ON doc_sources(library_id);
CREATE INDEX IF NOT EXISTS idx_doc_sources_platform ON doc_sources(platform);
"""


def get_db(db_path: Path | None = None) -> sqlite3.Connection:
    """Open (or create) the index database and ensure schema exists."""
    path = db_path or DB_PATH
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(_SCHEMA)
    return conn


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def upsert_library(conn: sqlite3.Connection, name: str, display_name: str,
                   language: str | None) -> int:
    """Insert or update a library, return its id."""
    conn.execute(
        "INSERT INTO libraries (name, display_name, language) VALUES (?, ?, ?) "
        "ON CONFLICT(name) DO UPDATE SET display_name=excluded.display_name, "
        "language=COALESCE(excluded.language, libraries.language)",
        (name, display_name, language),
    )
    row = conn.execute("SELECT id FROM libraries WHERE name = ?", (name,)).fetchone()
    return row["id"]


def upsert_doc_source(conn: sqlite3.Connection, library_id: int, platform: str,
                      doc_url: str, doc_type: str | None,
                      quality_signals: dict | None) -> None:
    """Insert or update a doc source for a library."""
    signals_json = json.dumps(quality_signals) if quality_signals else None
    conn.execute(
        "INSERT INTO doc_sources (library_id, platform, doc_url, doc_type, "
        "quality_signals, last_checked) VALUES (?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(library_id, platform) DO UPDATE SET "
        "doc_url=excluded.doc_url, doc_type=excluded.doc_type, "
        "quality_signals=excluded.quality_signals, last_checked=excluded.last_checked",
        (library_id, platform, doc_url, doc_type, signals_json, _now_iso()),
    )


def update_platform(conn: sqlite3.Connection, name: str, total: int,
                    api_url: str) -> None:
    """Record platform sync metadata."""
    conn.execute(
        "INSERT INTO platforms (name, last_synced, total_entries, api_url) "
        "VALUES (?, ?, ?, ?) ON CONFLICT(name) DO UPDATE SET "
        "last_synced=excluded.last_synced, total_entries=excluded.total_entries",
        (name, _now_iso(), total, api_url),
    )


def lookup(conn: sqlite3.Connection, name: str) -> list[dict]:
    """Look up all doc sources for a library by normalized name."""
    rows = conn.execute(
        "SELECT l.name, l.display_name, l.language, "
        "s.platform, s.doc_url, s.doc_type, s.quality_signals, s.last_checked "
        "FROM libraries l JOIN doc_sources s ON l.id = s.library_id "
        "WHERE l.name = ?",
        (name.lower().replace("_", "-").replace(" ", "-"),),
    ).fetchall()
    results = []
    for r in rows:
        entry = dict(r)
        if entry.get("quality_signals"):
            entry["quality_signals"] = json.loads(entry["quality_signals"])
        results.append(entry)
    return results


def get_stats(conn: sqlite3.Connection) -> dict:
    """Get index statistics."""
    total_libs = conn.execute("SELECT COUNT(*) FROM libraries").fetchone()[0]
    total_sources = conn.execute("SELECT COUNT(*) FROM doc_sources").fetchone()[0]

    platform_stats = {}
    for row in conn.execute(
        "SELECT platform, COUNT(*) as cnt FROM doc_sources GROUP BY platform "
        "ORDER BY cnt DESC"
    ):
        platform_stats[row["platform"]] = row["cnt"]

    platform_meta = {}
    for row in conn.execute("SELECT * FROM platforms"):
        platform_meta[row["name"]] = {
            "last_synced": row["last_synced"],
            "total_entries": row["total_entries"],
            "api_url": row["api_url"],
        }

    return {
        "total_libraries": total_libs,
        "total_sources": total_sources,
        "platforms": platform_stats,
        "platform_meta": platform_meta,
    }


# ---------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------

@app.command()
def build(
    platform: str = typer.Argument(
        ..., help="Platform to build from (e.g. 'devdocs', 'all')"
    ),
    list_platforms: bool = typer.Option(
        False, "--list", help="List available platforms and exit"
    ),
    db_path: Optional[str] = typer.Option(None, "--db", help="Custom DB path"),
):
    """Build/update the index from a platform's API."""
    from doc_index_sources import SOURCES

    if list_platforms or platform == "list":
        typer.echo("Available platforms:")
        for name, cls in SOURCES.items():
            src = cls()
            typer.echo(f"  {name:15s} {src.description}")
        raise typer.Exit()

    db = db_path or None
    if platform == "all":
        targets = list(SOURCES.keys())
    elif platform in SOURCES:
        targets = [platform]
    else:
        typer.echo(f"Unknown platform: {platform}", err=True)
        typer.echo(f"Available: {', '.join(SOURCES.keys())}", err=True)
        raise typer.Exit(1)

    conn = get_db(Path(db) if db else None)
    try:
        for target in targets:
            _build_one(conn, target, SOURCES[target])
    finally:
        conn.close()


def _build_one(conn: sqlite3.Connection, platform_name: str, source_cls: type) -> None:
    """Build index entries for one platform."""
    source = source_cls()
    typer.echo(f"Building {platform_name} ({source.description})...")
    t0 = time.monotonic()
    count = 0
    errors = 0

    for entry in source.fetch():
        try:
            lib_id = upsert_library(conn, entry.name, entry.display_name,
                                    entry.language)
            upsert_doc_source(conn, lib_id, platform_name, entry.doc_url,
                              entry.doc_type, entry.quality_signals)
            count += 1
            if count % 500 == 0:
                conn.commit()
                typer.echo(f"  ... {count} entries")
        except Exception as e:
            errors += 1
            if errors <= 5:
                typer.echo(f"  error on {entry.name}: {e}", err=True)

    conn.commit()
    update_platform(conn, platform_name, count, source.api_url)
    conn.commit()

    elapsed = time.monotonic() - t0
    typer.echo(f"  Done: {count} entries in {elapsed:.1f}s"
               + (f" ({errors} errors)" if errors else ""))


@app.command()
def lookup_cmd(
    name: str = typer.Argument(..., help="Library name to look up"),
    as_json: bool = typer.Option(False, "--json", help="Output as JSON"),
    db_path: Optional[str] = typer.Option(None, "--db", help="Custom DB path"),
):
    """Look up documentation sources for a library."""
    conn = get_db(Path(db_path) if db_path else None)
    try:
        results = lookup(conn, name)
    finally:
        conn.close()

    if not results:
        typer.echo(f"No entries found for '{name}'")
        raise typer.Exit(1)

    if as_json:
        typer.echo(json.dumps(results, indent=2))
    else:
        typer.echo(f"Documentation sources for '{name}':")
        for r in results:
            typer.echo(f"  [{r['platform']}] {r['doc_url']}")
            if r.get("doc_type"):
                typer.echo(f"    type: {r['doc_type']}")
            if r.get("language"):
                typer.echo(f"    language: {r['language']}")


@app.command()
def stats(
    platform: Optional[str] = typer.Option(None, "--platform",
                                           help="Filter by platform"),
    as_json: bool = typer.Option(False, "--json", help="Output as JSON"),
    db_path: Optional[str] = typer.Option(None, "--db", help="Custom DB path"),
):
    """Show index statistics."""
    conn = get_db(Path(db_path) if db_path else None)
    try:
        s = get_stats(conn)
    finally:
        conn.close()

    if platform:
        count = s["platforms"].get(platform, 0)
        meta = s["platform_meta"].get(platform, {})
        if as_json:
            typer.echo(json.dumps({"platform": platform, "entries": count, **meta},
                                  indent=2))
        else:
            typer.echo(f"{platform}: {count} entries")
            if meta.get("last_synced"):
                typer.echo(f"  Last synced: {meta['last_synced']}")
        return

    if as_json:
        typer.echo(json.dumps(s, indent=2))
    else:
        typer.echo(f"Total libraries: {s['total_libraries']}")
        typer.echo(f"Total sources:   {s['total_sources']}")
        typer.echo("\nPer platform:")
        for p, cnt in s["platforms"].items():
            meta = s["platform_meta"].get(p, {})
            synced = meta.get("last_synced", "never")
            typer.echo(f"  {p:15s} {cnt:>6d}  (synced: {synced})")


@app.command()
def export(
    format: str = typer.Option("json", help="Export format: json"),
    db_path: Optional[str] = typer.Option(None, "--db", help="Custom DB path"),
):
    """Export the full index."""
    conn = get_db(Path(db_path) if db_path else None)
    try:
        rows = conn.execute(
            "SELECT l.name, l.display_name, l.language, "
            "s.platform, s.doc_url, s.doc_type, s.quality_signals "
            "FROM libraries l JOIN doc_sources s ON l.id = s.library_id "
            "ORDER BY l.name, s.platform"
        ).fetchall()
    finally:
        conn.close()

    entries = []
    for r in rows:
        entry = dict(r)
        if entry.get("quality_signals"):
            entry["quality_signals"] = json.loads(entry["quality_signals"])
        entries.append(entry)

    typer.echo(json.dumps(entries, indent=2))


if __name__ == "__main__":
    app()
