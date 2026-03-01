"""Tests for doc_index.py and source adapters."""

import json
import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add scripts dir to path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from doc_index import get_db, upsert_library, upsert_doc_source, lookup, get_stats, update_platform
from doc_index_sources._base import LibraryDoc, IndexSource
from doc_index_sources.devdocs import DevDocsSource, _normalize_name
from doc_index_sources.dash import DashSource
from doc_index_sources.devhints import DevhintsSource
from doc_index_sources.apisguru import APIsGuruSource
from doc_index_sources.hexdocs import HexDocsSource
from doc_index_sources.pubdev import PubDevSource
from doc_index_sources.hackage import HackageSource
from doc_index_sources.swiftpkg import SwiftPkgSource
from doc_index_sources.golang import GolangSource
from doc_index_sources.readthedocs import ReadTheDocsSource
from doc_index_sources.cljdoc import CljdocSource


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def db():
    """In-memory SQLite database with schema."""
    conn = get_db(Path(":memory:"))
    yield conn
    conn.close()


@pytest.fixture
def tmp_db(tmp_path):
    """File-based SQLite database for CLI tests."""
    db_path = tmp_path / "test_index.db"
    conn = get_db(db_path)
    conn.close()
    return db_path


# ---------------------------------------------------------------------------
# Schema & core operations
# ---------------------------------------------------------------------------

class TestSchema:
    def test_tables_created(self, db):
        tables = {r[0] for r in db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()}
        assert "libraries" in tables
        assert "doc_sources" in tables
        assert "platforms" in tables

    def test_indexes_created(self, db):
        indexes = {r[0] for r in db.execute(
            "SELECT name FROM sqlite_master WHERE type='index'"
        ).fetchall()}
        assert "idx_libraries_name" in indexes
        assert "idx_doc_sources_library" in indexes
        assert "idx_doc_sources_platform" in indexes


class TestUpsert:
    def test_insert_library(self, db):
        lib_id = upsert_library(db, "react", "React", "javascript")
        db.commit()
        assert lib_id > 0
        row = db.execute("SELECT * FROM libraries WHERE id = ?", (lib_id,)).fetchone()
        assert row["name"] == "react"
        assert row["display_name"] == "React"
        assert row["language"] == "javascript"

    def test_upsert_library_updates(self, db):
        id1 = upsert_library(db, "react", "React", None)
        id2 = upsert_library(db, "react", "React.js", "javascript")
        db.commit()
        assert id1 == id2
        row = db.execute("SELECT * FROM libraries WHERE id = ?", (id1,)).fetchone()
        assert row["display_name"] == "React.js"
        assert row["language"] == "javascript"

    def test_upsert_library_preserves_language(self, db):
        """COALESCE keeps existing language if new is NULL."""
        upsert_library(db, "flask", "Flask", "python")
        upsert_library(db, "flask", "Flask", None)
        db.commit()
        row = db.execute("SELECT language FROM libraries WHERE name='flask'").fetchone()
        assert row["language"] == "python"

    def test_insert_doc_source(self, db):
        lib_id = upsert_library(db, "react", "React", "javascript")
        upsert_doc_source(db, lib_id, "devdocs", "https://devdocs.io/react/",
                          "html", {"version": "18"})
        db.commit()
        row = db.execute("SELECT * FROM doc_sources WHERE library_id = ?",
                         (lib_id,)).fetchone()
        assert row["platform"] == "devdocs"
        assert row["doc_url"] == "https://devdocs.io/react/"
        signals = json.loads(row["quality_signals"])
        assert signals["version"] == "18"

    def test_upsert_doc_source_updates(self, db):
        lib_id = upsert_library(db, "react", "React", "javascript")
        upsert_doc_source(db, lib_id, "devdocs", "https://devdocs.io/react~17/",
                          "html", None)
        upsert_doc_source(db, lib_id, "devdocs", "https://devdocs.io/react~18/",
                          "html", {"version": "18"})
        db.commit()
        rows = db.execute("SELECT * FROM doc_sources WHERE library_id = ?",
                          (lib_id,)).fetchall()
        assert len(rows) == 1
        assert rows[0]["doc_url"] == "https://devdocs.io/react~18/"


class TestLookup:
    def test_lookup_found(self, db):
        lib_id = upsert_library(db, "fastapi", "FastAPI", "python")
        upsert_doc_source(db, lib_id, "devdocs",
                          "https://devdocs.io/fastapi/", "html", {"v": "0.100"})
        db.commit()
        results = lookup(db, "fastapi")
        assert len(results) == 1
        assert results[0]["platform"] == "devdocs"
        assert results[0]["quality_signals"] == {"v": "0.100"}

    def test_lookup_not_found(self, db):
        results = lookup(db, "nonexistent-lib")
        assert results == []

    def test_lookup_normalizes_input(self, db):
        lib_id = upsert_library(db, "my-lib", "MyLib", "python")
        upsert_doc_source(db, lib_id, "devdocs", "https://devdocs.io/my-lib/",
                          "html", None)
        db.commit()
        # Underscore and space variants should find the same lib
        assert len(lookup(db, "my_lib")) == 1
        assert len(lookup(db, "my lib")) == 1
        assert len(lookup(db, "My-Lib")) == 1

    def test_lookup_multiple_sources(self, db):
        lib_id = upsert_library(db, "react", "React", "javascript")
        upsert_doc_source(db, lib_id, "devdocs", "https://devdocs.io/react/",
                          "html", None)
        upsert_doc_source(db, lib_id, "dash", "https://kapeli.com/dash/react",
                          "html", None)
        db.commit()
        results = lookup(db, "react")
        assert len(results) == 2
        platforms = {r["platform"] for r in results}
        assert platforms == {"devdocs", "dash"}


class TestStats:
    def test_empty_stats(self, db):
        s = get_stats(db)
        assert s["total_libraries"] == 0
        assert s["total_sources"] == 0
        assert s["platforms"] == {}

    def test_stats_with_data(self, db):
        lib1 = upsert_library(db, "react", "React", "javascript")
        lib2 = upsert_library(db, "flask", "Flask", "python")
        upsert_doc_source(db, lib1, "devdocs", "https://devdocs.io/react/",
                          "html", None)
        upsert_doc_source(db, lib2, "devdocs", "https://devdocs.io/flask/",
                          "html", None)
        upsert_doc_source(db, lib1, "dash", "https://dash/react", "html", None)
        update_platform(db, "devdocs", 2, "https://devdocs.io/docs.json")
        db.commit()
        s = get_stats(db)
        assert s["total_libraries"] == 2
        assert s["total_sources"] == 3
        assert s["platforms"]["devdocs"] == 2
        assert s["platforms"]["dash"] == 1
        assert "devdocs" in s["platform_meta"]


# ---------------------------------------------------------------------------
# Adapter parsing tests (mock HTTP)
# ---------------------------------------------------------------------------

DEVDOCS_RESPONSE = [
    {"slug": "react~18", "name": "React", "type": "javascript",
     "version": "18.2.0", "release": "18.2.0", "mtime": 1700000000},
    {"slug": "python~3.12", "name": "Python", "type": "python",
     "version": "3.12", "release": "3.12.1", "mtime": 1700000001},
    {"slug": "css", "name": "CSS", "type": "css"},
]

DASH_RESPONSE = [
    {"name": "React.xml", "type": "file", "path": "React.xml"},
    {"name": "Flask.xml", "type": "file", "path": "Flask.xml"},
    {"name": "README.md", "type": "file", "path": "README.md"},
]

DEVHINTS_RESPONSE = {
    "tree": [
        {"path": "react.md", "size": 5000, "type": "blob"},
        {"path": "bash.md", "size": 3000, "type": "blob"},
        {"path": "_data/whatever.md", "size": 100, "type": "blob"},  # has /
        {"path": "_sidebar.md", "size": 200, "type": "blob"},  # starts with _
        {"path": "README.md", "size": 1000, "type": "blob"},  # filtered out (no _ but valid)
    ]
}

APISGURU_RESPONSE = {
    "stripe.com": {
        "versions": {
            "2023-08-16": {
                "info": {
                    "title": "Stripe API",
                    "externalDocs": {"url": "https://stripe.com/docs/api"},
                    "x-apisguru-categories": ["payment"],
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/stripe.com/2023-08-16/openapi.json",
            }
        }
    },
    "github.com": {
        "versions": {
            "v3": {
                "info": {
                    "title": "GitHub REST API",
                },
                "swaggerUrl": "https://api.apis.guru/v2/specs/github.com/v3/openapi.json",
            }
        }
    },
}


class TestDevDocsAdapter:
    @patch("doc_index_sources.devdocs.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = DevDocsSource()
        entries = list(source.fetch())
        assert len(entries) == 3

        react = entries[0]
        assert react.name == "react"
        assert react.display_name == "React"
        assert react.doc_url == "https://devdocs.io/react~18/"
        assert react.language == "javascript"
        assert react.quality_signals["version"] == "18.2.0"

        python = entries[1]
        assert python.name == "python"
        assert python.language == "python"


class TestDashAdapter:
    @patch("doc_index_sources.dash.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DASH_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = DashSource()
        entries = list(source.fetch())
        # Only .xml files
        assert len(entries) == 2
        assert entries[0].name == "react"
        assert entries[1].name == "flask"


class TestDevhintsAdapter:
    @patch("doc_index_sources.devhints.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVHINTS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = DevhintsSource()
        entries = list(source.fetch())
        # react.md, bash.md, README.md (not _data/ or _sidebar)
        assert len(entries) == 3
        names = {e.name for e in entries}
        assert "react" in names
        assert "bash" in names
        assert "readme" in names
        assert entries[0].doc_type == "cheatsheet"


class TestAPIsGuruAdapter:
    @patch("doc_index_sources.apisguru.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: APISGURU_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = APIsGuruSource()
        entries = list(source.fetch())
        assert len(entries) == 2

        stripe = next(e for e in entries if "stripe" in e.name)
        assert stripe.doc_url == "https://stripe.com/docs/api"
        assert stripe.doc_type == "api-spec"
        assert stripe.quality_signals["has_external_docs"] is True

        github = next(e for e in entries if "github" in e.name)
        # No externalDocs, falls back to swaggerUrl
        assert "apis.guru" in github.doc_url or "github" in github.doc_url


class TestNormalizeName:
    def test_basic(self):
        assert _normalize_name("React") == "react"
        assert _normalize_name("My Library") == "my-library"
        assert _normalize_name("some_thing") == "some-thing"
        assert _normalize_name("  spaces  ") == "spaces"


# ---------------------------------------------------------------------------
# CLI integration tests (via typer.testing)
# ---------------------------------------------------------------------------

from typer.testing import CliRunner
from doc_index import app

runner = CliRunner()


class TestCLI:
    def test_build_list(self):
        result = runner.invoke(app, ["build", "list"])
        assert result.exit_code == 0
        assert "devdocs" in result.output
        assert "apisguru" in result.output

    @patch("doc_index_sources.devdocs.requests.get")
    def test_build_devdocs(self, mock_get, tmp_db):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        result = runner.invoke(app, ["build", "devdocs", "--db", str(tmp_db)])
        assert result.exit_code == 0
        assert "Done:" in result.output

    @patch("doc_index_sources.devdocs.requests.get")
    def test_lookup_found(self, mock_get, tmp_db):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        runner.invoke(app, ["build", "devdocs", "--db", str(tmp_db)])
        result = runner.invoke(app, ["lookup-cmd", "react", "--db", str(tmp_db)])
        assert result.exit_code == 0
        assert "devdocs" in result.output
        assert "devdocs.io" in result.output

    @patch("doc_index_sources.devdocs.requests.get")
    def test_lookup_json(self, mock_get, tmp_db):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        runner.invoke(app, ["build", "devdocs", "--db", str(tmp_db)])
        result = runner.invoke(app, ["lookup-cmd", "react", "--json",
                                     "--db", str(tmp_db)])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert len(data) >= 1
        assert data[0]["platform"] == "devdocs"

    def test_lookup_not_found(self, tmp_db):
        result = runner.invoke(app, ["lookup-cmd", "nonexistent",
                                     "--db", str(tmp_db)])
        assert result.exit_code == 1

    @patch("doc_index_sources.devdocs.requests.get")
    def test_stats(self, mock_get, tmp_db):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        runner.invoke(app, ["build", "devdocs", "--db", str(tmp_db)])
        result = runner.invoke(app, ["stats", "--db", str(tmp_db)])
        assert result.exit_code == 0
        assert "Total libraries:" in result.output

    @patch("doc_index_sources.devdocs.requests.get")
    def test_stats_json(self, mock_get, tmp_db):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: DEVDOCS_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        runner.invoke(app, ["build", "devdocs", "--db", str(tmp_db)])
        result = runner.invoke(app, ["stats", "--json", "--db", str(tmp_db)])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["total_libraries"] == 3

    def test_build_unknown_platform(self, tmp_db):
        result = runner.invoke(app, ["build", "unknown_platform",
                                     "--db", str(tmp_db)])
        assert result.exit_code == 1


# ---------------------------------------------------------------------------
# Base class tests
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Tier B adapter test data
# ---------------------------------------------------------------------------

HEXDOCS_PAGE1 = [
    {"name": "phoenix", "downloads": {"all": 50000000}, "updated_at": "2026-01-01T00:00:00Z"},
    {"name": "ecto", "downloads": {"all": 40000000}, "updated_at": "2026-01-01T00:00:00Z"},
]

PUBDEV_RESPONSE = {
    "packages": [
        {"name": "flutter_bloc"},
        {"name": "provider"},
    ],
    "next_url": None,
}

HACKAGE_RESPONSE = [
    {"packageName": "aeson"},
    {"packageName": "lens"},
]

SWIFTPKG_RESPONSE = [
    "https://github.com/Alamofire/Alamofire.git",
    "https://github.com/onevcat/Kingfisher",
]

GOLANG_NDJSON = (
    '{"Path":"github.com/gin-gonic/gin","Version":"v1.9.1","Timestamp":"2026-01-01T00:00:00Z"}\n'
    '{"Path":"golang.org/x/net","Version":"v0.20.0","Timestamp":"2026-01-01T00:00:00Z"}\n'
)

RTD_RESPONSE = {
    "results": [
        {
            "slug": "requests",
            "name": "Requests",
            "programming_language": {"code": "python"},
            "urls": {"documentation": "https://requests.readthedocs.io/"},
        },
    ],
    "next": None,
}

CLJDOC_SITEMAP = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://cljdoc.org/d/ring/ring-core/1.9.0</loc></url>
  <url><loc>https://cljdoc.org/d/ring/ring-core/1.8.0</loc></url>
  <url><loc>https://cljdoc.org/d/metosin/reitit/0.7.0</loc></url>
</urlset>
"""


# ---------------------------------------------------------------------------
# Tier B adapter parsing tests
# ---------------------------------------------------------------------------

class TestHexDocsAdapter:
    @patch("doc_index_sources.hexdocs.requests.get")
    @patch("doc_index_sources.hexdocs.time.sleep")
    def test_parse(self, mock_sleep, mock_get):
        # First call returns data, second returns empty list (end pagination)
        resp1 = MagicMock(status_code=200, json=lambda: HEXDOCS_PAGE1)
        resp1.raise_for_status = MagicMock()
        resp2 = MagicMock(status_code=200, json=lambda: [])
        resp2.raise_for_status = MagicMock()
        mock_get.side_effect = [resp1, resp2]

        source = HexDocsSource()
        entries = list(source.fetch())
        assert len(entries) == 2
        assert entries[0].name == "phoenix"
        assert entries[0].language == "elixir"
        assert entries[0].doc_url == "https://hexdocs.pm/phoenix/"
        assert entries[0].quality_signals["downloads"] == 50000000


class TestPubDevAdapter:
    @patch("doc_index_sources.pubdev.requests.get")
    @patch("doc_index_sources.pubdev.time.sleep")
    def test_parse(self, mock_sleep, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: PUBDEV_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = PubDevSource()
        entries = list(source.fetch())
        assert len(entries) == 2
        assert entries[0].name == "flutter-bloc"
        assert entries[0].language == "dart"
        assert "pub.dev/documentation" in entries[0].doc_url


class TestHackageAdapter:
    @patch("doc_index_sources.hackage.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: HACKAGE_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = HackageSource()
        entries = list(source.fetch())
        assert len(entries) == 2
        assert entries[0].name == "aeson"
        assert entries[0].language == "haskell"
        assert "hackage.haskell.org" in entries[0].doc_url


class TestSwiftPkgAdapter:
    @patch("doc_index_sources.swiftpkg.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: SWIFTPKG_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = SwiftPkgSource()
        entries = list(source.fetch())
        assert len(entries) == 2
        assert entries[0].name == "alamofire"
        assert entries[0].language == "swift"
        assert "swiftpackageindex.com" in entries[0].doc_url
        assert entries[1].name == "kingfisher"


class TestGolangAdapter:
    @patch("doc_index_sources.golang.requests.get")
    def test_parse(self, mock_get):
        mock_resp = MagicMock(status_code=200)
        mock_resp.raise_for_status = MagicMock()
        mock_resp.iter_lines = MagicMock(return_value=GOLANG_NDJSON.strip().split("\n"))
        mock_get.return_value = mock_resp

        source = GolangSource()
        entries = list(source.fetch())
        assert len(entries) == 2
        assert entries[0].name == "gin"
        assert entries[0].language == "go"
        assert "pkg.go.dev/github.com/gin-gonic/gin" in entries[0].doc_url
        assert entries[1].name == "net"


class TestReadTheDocsAdapter:
    @patch("doc_index_sources.readthedocs.requests.get")
    @patch("doc_index_sources.readthedocs.time.sleep")
    def test_parse(self, mock_sleep, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: RTD_RESPONSE
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = ReadTheDocsSource()
        entries = list(source.fetch())
        assert len(entries) == 1
        assert entries[0].name == "requests"
        assert entries[0].language == "python"
        assert entries[0].doc_url == "https://requests.readthedocs.io/"


class TestCljdocAdapter:
    @patch("doc_index_sources.cljdoc.requests.get")
    def test_parse(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200, content=CLJDOC_SITEMAP.encode()
        )
        mock_get.return_value.raise_for_status = MagicMock()

        source = CljdocSource()
        entries = list(source.fetch())
        # ring/ring-core appears twice (two versions) but deduped
        assert len(entries) == 2
        names = {e.name for e in entries}
        assert "ring-core" in names
        assert "reitit" in names
        assert entries[0].language == "clojure"
        assert "cljdoc.org/d/ring/ring-core" in entries[0].doc_url


# ---------------------------------------------------------------------------
# Base class tests
# ---------------------------------------------------------------------------

class TestBaseClass:
    def test_index_source_not_implemented(self):
        source = IndexSource()
        with pytest.raises(NotImplementedError):
            list(source.fetch())

    def test_library_doc_defaults(self):
        doc = LibraryDoc(name="test", display_name="Test", doc_url="https://test.com")
        assert doc.language is None
        assert doc.doc_type == "html"
        assert doc.quality_signals == {}
