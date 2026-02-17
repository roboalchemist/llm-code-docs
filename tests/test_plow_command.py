"""Tests for the auto_doc.py `plow` command (plow_batch function)."""

import json
from pathlib import Path
from unittest.mock import call, patch

import pytest

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import auto_doc


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_ticket(identifier: str, title: str, library: str):
    """Helper: build a ticket dict as returned by trckr_get_next_ticket."""
    return {
        "identifier": identifier,
        "title": title,
        "library_name": library,
    }


def _make_add_result(library: str, success: bool, **kwargs):
    """Helper: build an add_library result dict."""
    base = {
        "library": library,
        "source_used": kwargs.get("source_used", "llms-txt" if success else "skip"),
        "files_added": kwargs.get("files_added", 5 if success else 0),
        "quality_score": kwargs.get("quality_score", "pass" if success else None),
        "commit_sha": kwargs.get("commit_sha", "abc123" if success else None),
        "success": success,
        "error": kwargs.get("error", None if success else "no viable source"),
    }
    return base


# ---------------------------------------------------------------------------
# Tests: Limit respected
# ---------------------------------------------------------------------------

class TestPlowLimit:
    """Test that --limit N stops after N tickets."""

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_limit_3_processes_exactly_3(self, mock_get, mock_update, mock_add):
        """With --limit 3, exactly 3 tickets should be processed."""
        tickets = [
            _make_ticket("DOCS-1", "Add docs for lib-a", "lib-a"),
            _make_ticket("DOCS-2", "Add docs for lib-b", "lib-b"),
            _make_ticket("DOCS-3", "Add docs for lib-c", "lib-c"),
            _make_ticket("DOCS-4", "Add docs for lib-d", "lib-d"),  # should NOT be reached
        ]
        mock_get.side_effect = tickets
        mock_add.return_value = _make_add_result("lib", True)

        summary = auto_doc.plow_batch(limit=3)

        assert summary["processed"] == 3
        assert summary["succeeded"] == 3
        assert mock_add.call_count == 3
        assert summary["stopped_reason"] == "reached --limit 3"

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_limit_1(self, mock_get, mock_update, mock_add):
        """--limit 1 should process exactly 1 ticket."""
        mock_get.return_value = _make_ticket("DOCS-1", "Add docs for fastapi", "fastapi")
        mock_add.return_value = _make_add_result("fastapi", True)

        summary = auto_doc.plow_batch(limit=1)

        assert summary["processed"] == 1
        assert mock_add.call_count == 1

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_limit_0_means_unlimited(self, mock_get, mock_update, mock_add):
        """--limit 0 (default) should process all tickets until queue empty."""
        tickets = [
            _make_ticket("DOCS-1", "lib-a", "lib-a"),
            _make_ticket("DOCS-2", "lib-b", "lib-b"),
            None,  # queue empty
        ]
        mock_get.side_effect = tickets
        mock_add.return_value = _make_add_result("lib", True)

        summary = auto_doc.plow_batch(limit=0)

        assert summary["processed"] == 2
        assert summary["stopped_reason"] == "queue empty"


# ---------------------------------------------------------------------------
# Tests: Successful tickets set to done
# ---------------------------------------------------------------------------

class TestPlowSuccess:
    """Test that successful tickets get status=done with a comment."""

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_success_sets_done(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-10", "Add docs for react", "react"),
            None,
        ]
        mock_add.return_value = _make_add_result("react", True, commit_sha="def456abc")

        summary = auto_doc.plow_batch()

        assert summary["succeeded"] == 1
        assert summary["failed"] == 0

        # Check trckr was called correctly:
        # 1. in-progress, 2. done
        update_calls = mock_update.call_args_list
        assert update_calls[0] == call("DOCS-10", "in-progress", "auto-doc plow: processing 'react'")
        assert update_calls[1][0][0] == "DOCS-10"
        assert update_calls[1][0][1] == "done"
        assert "successfully added" in update_calls[1][0][2]
        assert "react" in update_calls[1][0][2]

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_success_comment_includes_details(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-20", "Add docs for vue", "vue"),
            None,
        ]
        mock_add.return_value = _make_add_result(
            "vue", True, source_used="llms-txt", files_added=12, commit_sha="abc123def",
        )

        auto_doc.plow_batch()

        done_call = mock_update.call_args_list[1]
        comment = done_call[0][2]
        assert "Source: llms-txt" in comment
        assert "Files: 12" in comment
        assert "Commit: abc123def" in comment


# ---------------------------------------------------------------------------
# Tests: Failed tickets set to in-review
# ---------------------------------------------------------------------------

class TestPlowFailure:
    """Test that failed tickets get status=in-review with error comment."""

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_failure_sets_in_review(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-30", "Add docs for obscurelib", "obscurelib"),
            None,
        ]
        mock_add.return_value = _make_add_result("obscurelib", False, error="no viable source found")

        summary = auto_doc.plow_batch()

        assert summary["failed"] == 1
        assert summary["succeeded"] == 0

        update_calls = mock_update.call_args_list
        # in-progress call
        assert update_calls[0][0][1] == "in-progress"
        # in-review call with error
        assert update_calls[1][0][0] == "DOCS-30"
        assert update_calls[1][0][1] == "in-review"
        assert "failed" in update_calls[1][0][2]
        assert "no viable source" in update_calls[1][0][2]

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_add_library_exception_sets_in_review(self, mock_get, mock_update, mock_add):
        """If add_library raises an exception, ticket should go to in-review."""
        mock_get.side_effect = [
            _make_ticket("DOCS-31", "Add docs for crashlib", "crashlib"),
            None,
        ]
        mock_add.side_effect = RuntimeError("unexpected network error")

        summary = auto_doc.plow_batch()

        assert summary["failed"] == 1
        update_calls = mock_update.call_args_list
        assert update_calls[1][0][1] == "in-review"
        assert "unexpected network error" in update_calls[1][0][2]


# ---------------------------------------------------------------------------
# Tests: Empty queue handling
# ---------------------------------------------------------------------------

class TestPlowEmptyQueue:
    """Test behavior when the queue is empty."""

    @patch("auto_doc.trckr_get_next_ticket")
    def test_empty_queue_returns_immediately(self, mock_get):
        mock_get.return_value = None

        summary = auto_doc.plow_batch()

        assert summary["processed"] == 0
        assert summary["succeeded"] == 0
        assert summary["failed"] == 0
        assert summary["stopped_reason"] == "queue empty"
        assert summary["tickets"] == []

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_queue_exhausted_mid_run(self, mock_get, mock_update, mock_add):
        """Queue runs out before --limit is reached."""
        mock_get.side_effect = [
            _make_ticket("DOCS-40", "lib-x", "lib-x"),
            None,  # queue empty after 1 ticket
        ]
        mock_add.return_value = _make_add_result("lib-x", True)

        summary = auto_doc.plow_batch(limit=5)

        assert summary["processed"] == 1
        assert summary["stopped_reason"] == "queue empty"


# ---------------------------------------------------------------------------
# Tests: Dry run mode
# ---------------------------------------------------------------------------

class TestPlowDryRun:
    """Test --dry-run passes through to add_library."""

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_dry_run_passed_to_add_library(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-50", "Add docs for drylib", "drylib"),
            None,
        ]
        mock_add.return_value = _make_add_result("drylib", True, files_added=0, commit_sha=None)

        auto_doc.plow_batch(dry_run=True)

        mock_add.assert_called_once_with("drylib", dry_run=True)

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_dry_run_success_comment_notes_dry_run(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-51", "Add docs for drylib", "drylib"),
            None,
        ]
        mock_add.return_value = _make_add_result("drylib", True, files_added=0, commit_sha=None)

        auto_doc.plow_batch(dry_run=True)

        done_call = mock_update.call_args_list[1]
        assert "dry run" in done_call[0][2]


# ---------------------------------------------------------------------------
# Tests: Mixed success/failure
# ---------------------------------------------------------------------------

class TestPlowMixed:
    """Test a batch with both successes and failures."""

    @patch("auto_doc.add_library")
    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_mixed_batch(self, mock_get, mock_update, mock_add):
        mock_get.side_effect = [
            _make_ticket("DOCS-60", "lib-ok", "lib-ok"),
            _make_ticket("DOCS-61", "lib-fail", "lib-fail"),
            _make_ticket("DOCS-62", "lib-ok2", "lib-ok2"),
            None,
        ]
        mock_add.side_effect = [
            _make_add_result("lib-ok", True),
            _make_add_result("lib-fail", False, error="fetch timeout"),
            _make_add_result("lib-ok2", True),
        ]

        summary = auto_doc.plow_batch()

        assert summary["processed"] == 3
        assert summary["succeeded"] == 2
        assert summary["failed"] == 1
        assert len(summary["tickets"]) == 3

        # Verify per-ticket results
        assert summary["tickets"][0]["success"] is True
        assert summary["tickets"][1]["success"] is False
        assert summary["tickets"][1]["error"] == "fetch timeout"
        assert summary["tickets"][2]["success"] is True


# ---------------------------------------------------------------------------
# Tests: Bad library name extraction
# ---------------------------------------------------------------------------

class TestPlowBadTitle:
    """Test ticket with unextractable library name."""

    @patch("auto_doc.trckr_update_ticket")
    @patch("auto_doc.trckr_get_next_ticket")
    def test_empty_library_name_skipped(self, mock_get, mock_update):
        mock_get.side_effect = [
            _make_ticket("DOCS-70", "", ""),  # empty title → empty library
            None,
        ]

        summary = auto_doc.plow_batch(limit=1)

        assert summary["processed"] == 1
        assert summary["skipped"] == 1
        assert summary["succeeded"] == 0

        # Should set in-review, not done
        update_calls = mock_update.call_args_list
        assert update_calls[0][0][1] == "in-review"
        assert "could not extract" in update_calls[0][0][2]


# ---------------------------------------------------------------------------
# Tests: CLI interface (typer)
# ---------------------------------------------------------------------------

class TestPlowCLI:
    """Test the typer CLI interface for the plow command."""

    @patch("auto_doc.plow_batch")
    def test_json_output(self, mock_batch):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_batch.return_value = {
            "processed": 2,
            "succeeded": 1,
            "failed": 1,
            "skipped": 0,
            "tickets": [],
            "stopped_reason": "queue empty",
        }

        result = runner.invoke(auto_doc.app, ["plow", "--json", "--limit", "2"])
        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["processed"] == 2
        mock_batch.assert_called_once_with(limit=2, dry_run=False, project_id=auto_doc.DOCS_PROJECT_ID)

    @patch("auto_doc.plow_batch")
    def test_human_output(self, mock_batch):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_batch.return_value = {
            "processed": 3,
            "succeeded": 2,
            "failed": 1,
            "skipped": 0,
            "tickets": [
                {"identifier": "DOCS-1", "library": "react", "success": True,
                 "source_used": "llms-txt", "error": None, "files_added": 5},
                {"identifier": "DOCS-2", "library": "badlib", "success": False,
                 "source_used": None, "error": "no source", "files_added": 0},
                {"identifier": "DOCS-3", "library": "vue", "success": True,
                 "source_used": "github", "error": None, "files_added": 10},
            ],
            "stopped_reason": "queue empty",
        }

        result = runner.invoke(auto_doc.app, ["plow", "--limit", "3"])
        assert result.exit_code == 0
        assert "3 processed" in result.output
        assert "2 succeeded" in result.output
        assert "1 failed" in result.output

    @patch("auto_doc.plow_batch")
    def test_dry_run_flag_passed(self, mock_batch):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_batch.return_value = {
            "processed": 0, "succeeded": 0, "failed": 0, "skipped": 0,
            "tickets": [], "stopped_reason": "queue empty",
        }

        runner.invoke(auto_doc.app, ["plow", "--dry-run", "--limit", "5"])
        mock_batch.assert_called_once_with(limit=5, dry_run=True, project_id=auto_doc.DOCS_PROJECT_ID)

    @patch("auto_doc.plow_batch")
    def test_custom_project_id(self, mock_batch):
        from typer.testing import CliRunner
        runner = CliRunner()

        mock_batch.return_value = {
            "processed": 0, "succeeded": 0, "failed": 0, "skipped": 0,
            "tickets": [], "stopped_reason": "queue empty",
        }

        runner.invoke(auto_doc.app, ["plow", "--project-id", "custom-uuid-123"])
        mock_batch.assert_called_once_with(limit=0, dry_run=False, project_id="custom-uuid-123")
