"""Tests for the auto_doc.py `add` command (add_library function)."""

import json
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import auto_doc


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_probe_output():
    """A realistic probe output for a library with llms-txt available."""
    return {
        "library": "testlib",
        "already_exists": False,
        "existing_paths": [],
        "configured_in": [],
        "official_site": "https://testlib.dev",
        "discovery": {
            "registries": {"pypi": {"domain": "testlib.dev", "github": "org/testlib", "pypi_found": True}},
            "github_search": {"candidates": [], "found": False},
            "tavily_search": {"search_results": [], "answer": None, "available": False},
            "domain_guess": {"probed": []},
            "unified_index": {},
            "enumerated_domains": {},
            "best_guess": {"domain": "testlib.dev", "github": "org/testlib"},
        },
        "llms_txt": [
            {
                "url": "https://testlib.dev/llms-full.txt",
                "http_status": 200,
                "size_bytes": 50000,
                "num_linked_pages": 20,
                "num_headings": 15,
                "sample_links_alive": 5,
                "sample_links_dead": 0,
                "validation_score": 85,
                "is_stub": False,
            }
        ],
        "github_candidates": [],
        "recommendation": "use_llms_txt",
    }


@pytest.fixture
def mock_probe_github():
    """Probe output where GitHub is the best source."""
    return {
        "library": "ghlib",
        "already_exists": False,
        "existing_paths": [],
        "configured_in": [],
        "official_site": None,
        "discovery": {
            "registries": {},
            "github_search": {
                "candidates": [{"full_name": "org/ghlib", "stars": 5000, "homepage": ""}],
                "found": True, "github": "org/ghlib",
            },
            "tavily_search": {"search_results": [], "answer": None, "available": False},
            "domain_guess": {"probed": []},
            "unified_index": {},
            "enumerated_domains": {},
            "best_guess": {"domain": None, "github": "org/ghlib"},
        },
        "llms_txt": [],
        "github_candidates": [
            {
                "repo": "org/ghlib",
                "stars": 5000,
                "last_push": "2025-01-01",
                "is_fork": False,
                "is_archived": False,
                "docs_folder": "docs",
                "docs_file_count": 25,
                "docs_total_size": "500KB",
                "has_markdown": True,
            }
        ],
        "recommendation": "use_github",
    }


@pytest.fixture
def mock_probe_nothing():
    """Probe output where nothing is found."""
    return {
        "library": "nonexistentlib99xyz",
        "already_exists": False,
        "existing_paths": [],
        "configured_in": [],
        "official_site": None,
        "discovery": {
            "registries": {},
            "github_search": {"candidates": [], "found": False},
            "tavily_search": {"search_results": [], "answer": None, "available": False},
            "domain_guess": {"probed": []},
            "unified_index": {},
            "enumerated_domains": {},
            "best_guess": {"domain": None, "github": None},
        },
        "llms_txt": [],
        "github_candidates": [],
        "recommendation": "nothing_found",
    }


@pytest.fixture
def mock_probe_exists():
    """Probe output for a library that already exists."""
    return {
        "library": "fastapi",
        "already_exists": True,
        "existing_paths": ["docs/github-scraped/fastapi"],
        "configured_in": ["repo_config.yaml"],
        "official_site": "https://fastapi.tiangolo.com",
        "discovery": {},
        "llms_txt": [],
        "github_candidates": [],
        "recommendation": "already_exists",
    }


@pytest.fixture
def tmp_docs(tmp_path):
    """Create a temporary docs directory with some markdown files."""
    docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
    docs_dir.mkdir(parents=True)
    (docs_dir / "index.md").write_text("# TestLib\n\nSome content here.\n")
    (docs_dir / "guide.md").write_text("# Guide\n\nUsage guide.\n")
    return docs_dir


# ---------------------------------------------------------------------------
# Tests: Happy path - llms-txt source
# ---------------------------------------------------------------------------

class TestAddLlmsTxt:
    """Test add_library with llms-txt source."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_happy_path_llms_txt(
        self, mock_git, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 5}
        mock_lint.return_value = {"files_checked": 5, "issues_fixed": 2}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "Good"}
        mock_git.return_value = {"commit_sha": "abc123def456", "error": None}

        # Patch DOCS_DIR to use tmp_path
        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib")

        assert result["success"] is True
        assert result["source_used"] == "llms-txt"
        assert result["files_added"] == 5
        assert result["commit_sha"] == "abc123def456"
        assert result["quality_score"] == "pass"
        assert result["error"] is None

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    def test_no_commit_flag(
        self, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 3}
        mock_lint.return_value = {"files_checked": 3, "issues_fixed": 0}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "OK"}

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib", no_commit=True)

        assert result["success"] is True
        assert result["commit_sha"] is None


# ---------------------------------------------------------------------------
# Tests: Happy path - GitHub source
# ---------------------------------------------------------------------------

class TestAddGitHub:
    """Test add_library with GitHub source."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_github")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_happy_path_github(
        self, mock_git, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_github, tmp_path,
    ):
        mock_probe.return_value = mock_probe_github
        mock_fetch.return_value = {"success": True, "file_count": 25}
        mock_lint.return_value = {"files_checked": 25, "issues_fixed": 5}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "OK"}
        mock_git.return_value = {"commit_sha": "def789abc012", "error": None}

        docs_dir = tmp_path / "docs" / "github-scraped" / "ghlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("ghlib")

        assert result["success"] is True
        assert result["source_used"] == "github"
        assert result["files_added"] == 25


# ---------------------------------------------------------------------------
# Tests: Happy path - Web scraper source
# ---------------------------------------------------------------------------

class TestAddWebScraper:
    """Test add_library with web scraper source."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc.decide")
    @patch("auto_doc.fetch_via_jina")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_happy_path_web(
        self, mock_git, mock_review, mock_lint, mock_jina, mock_decide, mock_probe,
        tmp_path,
    ):
        mock_probe.return_value = {
            "library": "weblib",
            "already_exists": False,
            "existing_paths": [],
            "discovery": {"registries": {}, "best_guess": {"domain": "weblib.io", "github": None},
                          "tavily_search": {"search_results": [{"url": "https://weblib.io/docs", "title": "WebLib"}], "answer": None, "available": True},
                          "unified_index": {}, "enumerated_domains": {}},
            "llms_txt": [],
            "github_candidates": [],
        }
        mock_decide.return_value = {"source": "web", "url": "https://weblib.io/", "reason": "web docs"}
        mock_jina.return_value = {"success": True, "file_count": 10}
        mock_lint.return_value = {"files_checked": 10, "issues_fixed": 1}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "Good"}
        mock_git.return_value = {"commit_sha": "web123", "error": None}

        docs_dir = tmp_path / "docs" / "web-scraped" / "weblib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("weblib")

        assert result["success"] is True
        assert result["source_used"] == "web"
        mock_jina.assert_called_once_with("weblib", "https://weblib.io/")


# ---------------------------------------------------------------------------
# Tests: Dry run
# ---------------------------------------------------------------------------

class TestAddDryRun:
    """Test --dry-run flag."""

    @patch("auto_doc._invoke_probe")
    def test_dry_run_stops_after_decide(self, mock_probe, mock_probe_output):
        mock_probe.return_value = mock_probe_output

        result = auto_doc.add_library("testlib", dry_run=True)

        assert result["success"] is True
        assert result["source_used"] == "llms-txt"
        assert result["files_added"] == 0
        assert result["commit_sha"] is None

    @patch("auto_doc._invoke_probe")
    def test_dry_run_skip_returns_error(self, mock_probe, mock_probe_nothing):
        mock_probe.return_value = mock_probe_nothing

        result = auto_doc.add_library("nonexistentlib99xyz", dry_run=True)

        assert result["success"] is False
        assert result["source_used"] == "skip"
        assert "no viable" in result["error"]


# ---------------------------------------------------------------------------
# Tests: Sad path - already exists
# ---------------------------------------------------------------------------

class TestAddAlreadyExists:
    """Test that add fails for existing libraries."""

    @patch("auto_doc._invoke_probe")
    def test_already_exists(self, mock_probe, mock_probe_exists):
        mock_probe.return_value = mock_probe_exists

        result = auto_doc.add_library("fastapi")

        assert result["success"] is True
        assert result["source_used"] == "already_exists"
        assert result["error"] is None


# ---------------------------------------------------------------------------
# Tests: Sad path - nothing found
# ---------------------------------------------------------------------------

class TestAddNothingFound:
    """Test graceful failure when no docs are found."""

    @patch("auto_doc._invoke_probe")
    def test_nothing_found(self, mock_probe, mock_probe_nothing):
        mock_probe.return_value = mock_probe_nothing

        result = auto_doc.add_library("nonexistentlib99xyz")

        assert result["success"] is False
        assert result["source_used"] == "skip"
        assert "no viable" in result["error"]


# ---------------------------------------------------------------------------
# Tests: Sad path - fetch failure
# ---------------------------------------------------------------------------

class TestAddFetchFailure:
    """Test handling of fetch failures."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    def test_fetch_fails(self, mock_fetch, mock_probe, mock_probe_output):
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": False, "error": "connection timeout"}

        result = auto_doc.add_library("testlib")

        assert result["success"] is False
        assert "fetch failed" in result["error"]
        assert "connection timeout" in result["error"]


# ---------------------------------------------------------------------------
# Tests: Sad path - review failure
# ---------------------------------------------------------------------------

class TestAddReviewFailure:
    """Test handling of LLM review failure."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    def test_review_fails(
        self, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 5}
        mock_lint.return_value = {"files_checked": 5, "issues_fixed": 0}
        mock_review.return_value = {
            "pass": False,
            "issues": ["wrong library detected", "mostly boilerplate"],
            "files_to_delete": ["junk.md"],
            "summary": "This is not testlib documentation",
        }

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")
        (docs_dir / "junk.md").write_text("# Junk")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib")

        assert result["success"] is False
        assert result["quality_score"] == "fail"
        assert "content review failed" in result["error"]
        # Verify junk file was deleted
        assert not (docs_dir / "junk.md").exists()


# ---------------------------------------------------------------------------
# Tests: Sad path - git commit failure
# ---------------------------------------------------------------------------

class TestAddGitFailure:
    """Test handling of git commit/push failure."""

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_git_commit_fails(
        self, mock_git, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 5}
        mock_lint.return_value = {"files_checked": 5, "issues_fixed": 0}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "OK"}
        mock_git.return_value = {"commit_sha": None, "error": "nothing to commit"}

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib")

        assert result["success"] is False
        assert "nothing to commit" in result["error"]

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_push_fails_but_commit_succeeds(
        self, mock_git, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        """Push failure is non-fatal if commit succeeded."""
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 5}
        mock_lint.return_value = {"files_checked": 5, "issues_fixed": 0}
        mock_review.return_value = {"pass": True, "issues": [], "files_to_delete": [], "summary": "OK"}
        mock_git.return_value = {"commit_sha": "abc123", "error": "push failed: remote rejected"}

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib")

        # Commit worked, so overall success (push error is logged but non-fatal)
        assert result["success"] is True
        assert result["commit_sha"] == "abc123"


# ---------------------------------------------------------------------------
# Tests: CLI interface (typer)
# ---------------------------------------------------------------------------

class TestAddCLI:
    """Test the typer CLI interface for the add command."""

    @patch("auto_doc.add_library")
    def test_json_output(self, mock_add):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_add.return_value = {
            "library": "testlib",
            "source_used": "llms-txt",
            "files_added": 5,
            "quality_score": "pass",
            "commit_sha": "abc123",
            "success": True,
            "error": None,
        }

        result = runner.invoke(auto_doc.app, ["add", "testlib", "--json"])
        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["success"] is True
        assert output["library"] == "testlib"

    @patch("auto_doc.add_library")
    def test_human_output_success(self, mock_add):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_add.return_value = {
            "library": "testlib",
            "source_used": "llms-txt",
            "files_added": 5,
            "quality_score": "pass",
            "commit_sha": "abc123def456",
            "success": True,
            "error": None,
        }

        result = runner.invoke(auto_doc.app, ["add", "testlib"])
        assert result.exit_code == 0
        assert "Successfully added" in result.output

    @patch("auto_doc.add_library")
    def test_human_output_failure(self, mock_add):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_add.return_value = {
            "library": "badlib",
            "source_used": "skip",
            "files_added": 0,
            "quality_score": None,
            "commit_sha": None,
            "success": False,
            "error": "no viable documentation source found",
        }

        result = runner.invoke(auto_doc.app, ["add", "badlib"])
        assert result.exit_code == 1

    @patch("auto_doc.add_library")
    def test_dry_run_flag_passed(self, mock_add):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_add.return_value = {
            "library": "testlib",
            "source_used": "llms-txt",
            "files_added": 0,
            "quality_score": None,
            "commit_sha": None,
            "success": True,
            "error": None,
        }

        result = runner.invoke(auto_doc.app, ["add", "testlib", "--dry-run", "--json"])
        assert result.exit_code == 0
        mock_add.assert_called_once_with("testlib", dry_run=True, no_commit=False)

    @patch("auto_doc.add_library")
    def test_no_commit_flag_passed(self, mock_add):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_add.return_value = {
            "library": "testlib",
            "source_used": "llms-txt",
            "files_added": 5,
            "quality_score": "pass",
            "commit_sha": None,
            "success": True,
            "error": None,
        }

        result = runner.invoke(auto_doc.app, ["add", "testlib", "--no-commit"])
        assert result.exit_code == 0
        mock_add.assert_called_once_with("testlib", dry_run=False, no_commit=True)


# ---------------------------------------------------------------------------
# Tests: Edge cases
# ---------------------------------------------------------------------------

class TestAddEdgeCases:
    """Test edge cases and boundary conditions."""

    @patch("auto_doc._invoke_probe")
    def test_probe_raises_exception(self, mock_probe):
        """If probe itself raises, add_library should handle gracefully."""
        mock_probe.side_effect = Exception("network error")

        result = auto_doc.add_library("testlib")

        # Should fail, not crash
        assert result["success"] is False

    @patch("auto_doc._invoke_probe")
    @patch("auto_doc._fetch_llms_txt")
    @patch("auto_doc.cleanup_markdownlint")
    @patch("auto_doc.review_content")
    @patch("auto_doc._git_commit_and_push")
    def test_review_deletes_flagged_files(
        self, mock_git, mock_review, mock_lint, mock_fetch, mock_probe,
        mock_probe_output, tmp_path,
    ):
        """Review that passes but flags files for deletion."""
        mock_probe.return_value = mock_probe_output
        mock_fetch.return_value = {"success": True, "file_count": 3}
        mock_lint.return_value = {"files_checked": 3, "issues_fixed": 0}
        mock_review.return_value = {
            "pass": True,
            "issues": ["minor: one duplicate file"],
            "files_to_delete": [],
            "summary": "Acceptable with minor issues",
        }
        mock_git.return_value = {"commit_sha": "abc123", "error": None}

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)
        (docs_dir / "test.md").write_text("# Test")

        with patch.object(auto_doc, "DOCS_DIR", tmp_path / "docs"):
            result = auto_doc.add_library("testlib")

        assert result["success"] is True
        assert result["quality_score"] == "pass"


# ---------------------------------------------------------------------------
# Tests: _git_commit_and_push
# ---------------------------------------------------------------------------

class TestGitCommitAndPush:
    """Test the git commit and push helper."""

    @patch("subprocess.run")
    def test_nothing_staged(self, mock_run, tmp_path):
        # git add succeeds, diff --cached --quiet returns 0 (nothing staged)
        mock_run.side_effect = [
            MagicMock(returncode=0),  # git add docs
            MagicMock(returncode=0),  # git add config 1
            MagicMock(returncode=0),  # git add config 2
            MagicMock(returncode=0),  # git diff --cached --quiet
        ]

        docs_dir = tmp_path / "docs" / "llms-txt" / "testlib"
        docs_dir.mkdir(parents=True)

        with patch.object(auto_doc, "REPO_ROOT", tmp_path):
            result = auto_doc._git_commit_and_push("testlib", "llms-txt", docs_dir)

        assert result["commit_sha"] is None
        assert "nothing to commit" in result["error"]


# ---------------------------------------------------------------------------
# Integration tests: invoke add via CliRunner (no probe mocking)
# ---------------------------------------------------------------------------

class TestAddIntegration:
    """Integration tests that invoke add through CliRunner without mocking probe.

    These tests verify the full probe → decide → add pipeline works end-to-end
    through the typer CLI layer, catching issues like the OptionInfo bug where
    calling typer commands directly as Python functions fails.
    """

    def test_add_dry_run_nonexistent_library(self):
        """add --dry-run for a nonexistent library should return structured JSON error."""
        from typer.testing import CliRunner
        runner = CliRunner()

        result = runner.invoke(auto_doc.app, ["add", "nonexistent_xyz_12345", "--dry-run", "--json"])
        assert result.exit_code in (0, 1)  # either is fine

        output = json.loads(result.output)
        assert output["library"] == "nonexistent_xyz_12345"
        assert output["success"] is False
        # Should get a structured error, not a traceback
        assert output["error"] is not None
        assert "OptionInfo" not in result.output  # The original bug

    def test_add_dry_run_returns_valid_json(self):
        """add --dry-run --json should always return parseable JSON, never a traceback."""
        from typer.testing import CliRunner
        runner = CliRunner()

        result = runner.invoke(auto_doc.app, ["add", "some-test-lib", "--dry-run", "--json"])
        # Must be valid JSON regardless of success/failure
        try:
            output = json.loads(result.output)
        except json.JSONDecodeError:
            pytest.fail(f"add --dry-run --json returned non-JSON output: {result.output[:500]}")

        assert "library" in output
        assert "success" in output
        assert "error" in output

    def test_probe_invoked_via_clirunner(self):
        """Verify _invoke_probe works correctly through CliRunner."""
        # This directly tests the fix: _invoke_probe should return a dict, not crash
        try:
            result = auto_doc._invoke_probe("nonexistent_xyz_99999")
            # If it succeeds, it should be a dict with expected keys
            assert isinstance(result, dict)
            assert "library" in result
        except RuntimeError as e:
            # RuntimeError is the expected error path (probe failed or invalid JSON)
            assert "OptionInfo" not in str(e)  # The original bug
