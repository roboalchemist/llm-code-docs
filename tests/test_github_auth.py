"""Tests for GitHub API authentication in auto_doc.py (AUTO-36)."""

import json
import os
import subprocess
import sys
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))


class TestEnsureGithubToken:
    """Test _ensure_github_token() token loading priority."""

    def test_gh_token_env_already_set(self):
        """GH_TOKEN already in env — should be left as-is."""
        with patch.dict(os.environ, {"GH_TOKEN": "existing-token"}, clear=False):
            from auto_doc import _ensure_github_token
            _ensure_github_token()
            assert os.environ["GH_TOKEN"] == "existing-token"

    def test_github_token_env_copied(self):
        """GITHUB_TOKEN env should be copied to GH_TOKEN."""
        env = {"GITHUB_TOKEN": "from-github-token"}
        # Remove GH_TOKEN if present
        with patch.dict(os.environ, env, clear=False):
            os.environ.pop("GH_TOKEN", None)
            from auto_doc import _ensure_github_token
            _ensure_github_token()
            assert os.environ["GH_TOKEN"] == "from-github-token"

    @patch("subprocess.run")
    def test_gh_auth_token_fallback(self, mock_run):
        """Falls back to `gh auth token` CLI when no env vars set."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="ghp_test_cli_token\n",
        )
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GH_TOKEN", None)
            os.environ.pop("GITHUB_TOKEN", None)
            from auto_doc import _ensure_github_token
            _ensure_github_token()
            assert os.environ.get("GH_TOKEN") == "ghp_test_cli_token"

    @patch("subprocess.run")
    def test_gh_auth_token_failure_no_crash(self, mock_run):
        """If `gh auth token` fails, should not crash."""
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GH_TOKEN", None)
            os.environ.pop("GITHUB_TOKEN", None)
            from auto_doc import _ensure_github_token
            _ensure_github_token()
            # GH_TOKEN should NOT be set
            assert os.environ.get("GH_TOKEN") in (None, "")


class TestGithubApiGetAuth:
    """Test that _github_api_get uses auth token in HTTP fallback."""

    @patch("auto_doc._run_cmd", return_value=None)  # gh CLI fails
    @patch("auto_doc.SESSION")
    def test_fallback_uses_auth_header(self, mock_session, mock_run_cmd):
        """When gh CLI fails, HTTP fallback should include Authorization header."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"test": True}
        mock_session.get.return_value = mock_response

        with patch.dict(os.environ, {"GH_TOKEN": "ghp_test_token"}, clear=False):
            from auto_doc import _github_api_get
            result = _github_api_get("repos/test/test")

        assert result == {"test": True}
        # Verify the Authorization header was passed
        call_kwargs = mock_session.get.call_args
        headers = call_kwargs.kwargs.get("headers") or call_kwargs[1].get("headers", {})
        assert headers.get("Authorization") == "token ghp_test_token"

    @patch("auto_doc._run_cmd", return_value=None)  # gh CLI fails
    @patch("auto_doc.SESSION")
    def test_fallback_without_token(self, mock_session, mock_run_cmd):
        """When no token available, should still work (unauthenticated)."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"test": True}
        mock_session.get.return_value = mock_response

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GH_TOKEN", None)
            from auto_doc import _github_api_get
            result = _github_api_get("repos/test/test")

        assert result == {"test": True}
        call_kwargs = mock_session.get.call_args
        headers = call_kwargs.kwargs.get("headers") or call_kwargs[1].get("headers", {})
        assert "Authorization" not in headers


class TestGithubAuthLive:
    """Live integration tests — require gh auth to be configured."""

    @pytest.fixture(autouse=True)
    def check_gh_auth(self):
        """Skip if gh is not authenticated."""
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            pytest.skip("gh not authenticated")

    def test_rate_limit_is_5000(self):
        """Verify authenticated rate limit is 5000."""
        from auto_doc import _github_api_get
        result = _github_api_get("rate_limit")
        assert result is not None
        core_limit = result["resources"]["core"]["limit"]
        assert core_limit == 5000, f"Expected 5000 (authenticated), got {core_limit}"

    def test_gh_auth_status_succeeds(self):
        """QA criterion: gh auth status succeeds."""
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode == 0
