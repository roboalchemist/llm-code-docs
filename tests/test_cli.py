"""Tests for the CLI module (search/cli.py).

Tests cover:
- Default backend is opensearch
- --backend flag switches between opensearch and lancedb
- --explain flag shows scoring breakdown
- --verbose flag shows SPLADE term expansion / search metrics
- All existing flags (--limit, --category, --framework, etc.) still work
- Help text includes new options
"""

import os
import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from click.testing import CliRunner

import pandas as pd

# Set test environment variables before importing
os.environ.setdefault("OPENSEARCH_HOST", "localhost")
os.environ.setdefault("OPENSEARCH_PORT", "9200")
os.environ.setdefault("OPENSEARCH_INDEX_NAME", "test_llm_docs")
os.environ.setdefault("OPENSEARCH_PIPELINE_NAME", "test_pipeline")


from search.cli import cli

# Pre-import submodules so patch() can resolve the dotted paths.
# These modules have empty __init__.py files so they must be imported
# explicitly before mock.patch can find the attributes.
import search.searcher.query
import search.searcher.ranker
import search.searcher.formatter
import search.opensearch.searcher

# Patch paths: because cli.py uses lazy imports inside functions,
# we must patch at the source module where the function is defined.
PATCH_GET_SEARCHER = 'search.opensearch.searcher.get_searcher'
PATCH_GET_FORMATTER = 'search.searcher.formatter.get_formatter'
PATCH_GET_PROCESSOR = 'search.searcher.query.get_processor'
PATCH_GET_RANKER = 'search.searcher.ranker.get_ranker'


@pytest.fixture
def runner():
    """Create a Click CLI test runner."""
    return CliRunner()


@pytest.fixture
def mock_opensearch_searcher():
    """Mock the OpenSearch HybridSearcher for CLI tests."""
    from search.opensearch.searcher import HybridSearchConfig, SearchMetrics

    mock_searcher = MagicMock()
    mock_searcher.config = HybridSearchConfig()

    # Create sample document results DataFrame
    doc_df = pd.DataFrame([
        {
            "doc_id": "doc1",
            "doc_hash": "abc123",
            "similarity_score": 0.95,
            "final_score": 0.95,
            "_raw_score": 12.5,
            "content": "FastAPI is a modern, fast web framework for building APIs.",
            "title": "FastAPI Introduction",
            "framework": "fastapi",
            "category": "github-scraped",
            "source_type": "github-scraped",
            "file_path": "intro.md",
            "path": "/docs/fastapi/intro.md",
            "relative_path": "docs/fastapi/intro.md",
            "folder_id": "folder1",
            "chunk_index": 0,
            "chunk_id": 0,
            "total_chunks": 1,
            "chunk_count": 1,
            "created_at": None,
            "updated_at": None,
            "last_modified": None,
            "highlight": {},
            "highlighted_content": "<em>FastAPI</em> middleware example",
            "highlighted_title": "",
        },
        {
            "doc_id": "doc2",
            "doc_hash": "def456",
            "similarity_score": 0.82,
            "final_score": 0.82,
            "_raw_score": 9.3,
            "content": "Middleware in FastAPI allows you to process requests.",
            "title": "FastAPI Middleware",
            "framework": "fastapi",
            "category": "github-scraped",
            "source_type": "github-scraped",
            "file_path": "middleware.md",
            "path": "/docs/fastapi/middleware.md",
            "relative_path": "docs/fastapi/middleware.md",
            "folder_id": "folder1",
            "chunk_index": 0,
            "chunk_id": 0,
            "total_chunks": 1,
            "chunk_count": 1,
            "created_at": None,
            "updated_at": None,
            "last_modified": None,
            "highlight": {},
            "highlighted_content": "",
            "highlighted_title": "",
        },
    ])

    # Create sample folder results DataFrame
    folder_df = pd.DataFrame([
        {
            "folder_id": "folder1",
            "framework_name": "fastapi",
            "description": "Modern web framework for Python APIs",
            "category": "github-scraped",
            "path": "/docs/fastapi",
            "file_count": 25,
            "size": "1.2 MB",
            "status": "active",
            "source_url": "https://github.com/tiangolo/fastapi",
            "all_titles": "FastAPI, Introduction, Middleware",
            "last_updated": None,
            "similarity_score": 0.90,
            "final_score": 0.90,
            "_raw_score": 8.7,
        },
    ])

    # Document search metrics
    doc_metrics = SearchMetrics(
        query="FastAPI middleware",
        total_hits=42,
        returned_hits=2,
        took_ms=15,
        total_latency_ms=25.3,
        bm25_enabled=True,
        splade_enabled=True,
        dense_enabled=True,
    )

    # Folder search metrics
    folder_metrics = SearchMetrics(
        query="FastAPI middleware",
        total_hits=5,
        returned_hits=1,
        took_ms=8,
        total_latency_ms=12.1,
        bm25_enabled=True,
        splade_enabled=False,
        dense_enabled=True,
    )

    mock_searcher.search.return_value = (doc_df, doc_metrics)
    mock_searcher.search_folders.return_value = (folder_df, folder_metrics)

    return mock_searcher


@pytest.fixture
def mock_empty_opensearch_searcher():
    """Mock an OpenSearch HybridSearcher that returns empty results."""
    from search.opensearch.searcher import HybridSearchConfig, SearchMetrics

    mock_searcher = MagicMock()
    mock_searcher.config = HybridSearchConfig()

    empty_metrics = SearchMetrics(
        query="nonexistent query",
        total_hits=0,
        returned_hits=0,
        took_ms=5,
        total_latency_ms=10.0,
        bm25_enabled=True,
        splade_enabled=True,
        dense_enabled=True,
    )

    mock_searcher.search.return_value = (pd.DataFrame(), empty_metrics)
    mock_searcher.search_folders.return_value = (pd.DataFrame(), empty_metrics)

    return mock_searcher


def _make_mock_formatter(return_value="results"):
    """Create a mock formatter with common setup."""
    mock_formatter = MagicMock()
    mock_formatter.format_results.return_value = return_value
    mock_formatter.show_content_preview = True
    mock_formatter.show_scores = True
    return mock_formatter


class TestCLIHelp:
    """Tests for CLI help text and structure."""

    def test_main_help(self, runner):
        """Test main CLI help shows all commands."""
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert 'search' in result.output
        assert 'index' in result.output
        assert 'stats' in result.output

    def test_search_help_shows_backend_option(self, runner):
        """Test search --help includes --backend option."""
        result = runner.invoke(cli, ['search', '--help'])
        assert result.exit_code == 0
        assert '--backend' in result.output
        assert 'opensearch' in result.output
        assert 'lancedb' in result.output

    def test_search_help_shows_explain_option(self, runner):
        """Test search --help includes --explain option."""
        result = runner.invoke(cli, ['search', '--help'])
        assert result.exit_code == 0
        assert '--explain' in result.output
        assert 'scoring breakdown' in result.output.lower()

    def test_search_help_shows_verbose_option(self, runner):
        """Test search --help includes --verbose option."""
        result = runner.invoke(cli, ['search', '--help'])
        assert result.exit_code == 0
        assert '--verbose' in result.output
        assert 'SPLADE' in result.output

    def test_version_output(self, runner):
        """Test version option shows updated version."""
        result = runner.invoke(cli, ['--version'])
        assert result.exit_code == 0
        assert '0.2.0' in result.output


class TestSearchOpenSearchBackend:
    """Tests for search command with opensearch backend (default)."""

    def test_default_backend_is_opensearch(self, runner, mock_opensearch_searcher):
        """Test that opensearch is the default backend."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware'])

                assert result.exit_code == 0
                mock_opensearch_searcher.search.assert_called_once()

    def test_opensearch_search_returns_results(self, runner, mock_opensearch_searcher):
        """Test opensearch backend returns formatted results."""
        mock_formatter = _make_mock_formatter('Query: "FastAPI middleware"\n\n=== Documents (2 matches) ===')

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware'])

                assert result.exit_code == 0
                assert 'FastAPI middleware' in result.output

    def test_opensearch_explicit_backend_flag(self, runner, mock_opensearch_searcher):
        """Test --backend opensearch explicitly selects opensearch."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test query', '--backend', 'opensearch'])

                assert result.exit_code == 0
                mock_opensearch_searcher.search.assert_called_once()

    def test_opensearch_search_with_category_filter(self, runner, mock_opensearch_searcher):
        """Test opensearch search passes category filter."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, [
                    'search', 'test query',
                    '--category', 'github-scraped',
                ])

                assert result.exit_code == 0
                call_kwargs = mock_opensearch_searcher.search.call_args
                assert call_kwargs.kwargs.get('category') == 'github-scraped'

    def test_opensearch_search_with_framework_filter(self, runner, mock_opensearch_searcher):
        """Test opensearch search passes framework filter."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, [
                    'search', 'middleware',
                    '--framework', 'fastapi',
                ])

                assert result.exit_code == 0
                call_kwargs = mock_opensearch_searcher.search.call_args
                assert call_kwargs.kwargs.get('framework') == 'fastapi'

    def test_opensearch_search_with_limit(self, runner, mock_opensearch_searcher):
        """Test opensearch search passes limit parameter."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, [
                    'search', 'test query',
                    '--limit', '20',
                ])

                assert result.exit_code == 0
                call_kwargs = mock_opensearch_searcher.search.call_args
                assert call_kwargs.kwargs.get('size') == 20

    def test_opensearch_docs_only(self, runner, mock_opensearch_searcher):
        """Test --docs-only skips folder search."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '--docs-only'])

                assert result.exit_code == 0
                mock_opensearch_searcher.search.assert_called_once()
                mock_opensearch_searcher.search_folders.assert_not_called()

    def test_opensearch_folders_only(self, runner, mock_opensearch_searcher):
        """Test --folders-only skips document search."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '--folders-only'])

                assert result.exit_code == 0
                mock_opensearch_searcher.search.assert_not_called()
                mock_opensearch_searcher.search_folders.assert_called_once()

    def test_opensearch_empty_results(self, runner, mock_empty_opensearch_searcher):
        """Test opensearch handles empty results gracefully."""
        mock_formatter = _make_mock_formatter('=== Documents (0 matches) ===')

        with patch(PATCH_GET_SEARCHER, return_value=mock_empty_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'nonexistent query'])

                assert result.exit_code == 0
                assert '0 matches' in result.output


class TestSearchLanceDBBackend:
    """Tests for search command with lancedb backend."""

    def test_lancedb_backend_flag(self, runner):
        """Test --backend lancedb uses the LanceDB processor."""
        mock_processor = MagicMock()
        mock_ranker = MagicMock()
        mock_formatter = _make_mock_formatter("lancedb results")

        mock_results = MagicMock()
        mock_results.documents = pd.DataFrame()
        mock_results.folders = pd.DataFrame()
        mock_results.query = "test"
        mock_processor.search.return_value = mock_results

        with patch(PATCH_GET_PROCESSOR, return_value=mock_processor):
            with patch(PATCH_GET_RANKER, return_value=mock_ranker):
                with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                    result = runner.invoke(cli, [
                        'search', 'test query',
                        '--backend', 'lancedb',
                    ])

                    assert result.exit_code == 0
                    mock_processor.search.assert_called_once()
                    assert 'lancedb results' in result.output

    def test_lancedb_backend_with_reranking(self, runner):
        """Test LanceDB backend applies reranking by default."""
        mock_processor = MagicMock()
        mock_ranker = MagicMock()
        mock_formatter = _make_mock_formatter("reranked")

        doc_df = pd.DataFrame([{"content": "test", "title": "test"}])
        mock_results = MagicMock()
        mock_results.documents = doc_df
        mock_results.folders = pd.DataFrame()
        mock_processor.search.return_value = mock_results
        mock_ranker.rerank_documents.return_value = doc_df

        with patch(PATCH_GET_PROCESSOR, return_value=mock_processor):
            with patch(PATCH_GET_RANKER, return_value=mock_ranker):
                with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                    result = runner.invoke(cli, [
                        'search', 'test query',
                        '--backend', 'lancedb',
                    ])

                    assert result.exit_code == 0
                    mock_ranker.rerank_documents.assert_called_once()

    def test_lancedb_backend_no_rerank(self, runner):
        """Test LanceDB backend skips reranking with --no-rerank."""
        mock_processor = MagicMock()
        mock_ranker = MagicMock()
        mock_formatter = _make_mock_formatter("no rerank")

        mock_results = MagicMock()
        mock_results.documents = pd.DataFrame()
        mock_results.folders = pd.DataFrame()
        mock_processor.search.return_value = mock_results

        with patch(PATCH_GET_PROCESSOR, return_value=mock_processor):
            with patch(PATCH_GET_RANKER, return_value=mock_ranker):
                with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                    result = runner.invoke(cli, [
                        'search', 'test query',
                        '--backend', 'lancedb',
                        '--no-rerank',
                    ])

                    assert result.exit_code == 0
                    mock_ranker.rerank_documents.assert_not_called()
                    mock_ranker.rerank_folders.assert_not_called()


class TestExplainFlag:
    """Tests for the --explain flag."""

    def test_explain_shows_scoring_breakdown(self, runner, mock_opensearch_searcher):
        """Test --explain displays scoring breakdown section."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'Scoring Breakdown' in result.output

    def test_explain_shows_component_weights(self, runner, mock_opensearch_searcher):
        """Test --explain shows BM25/SPLADE/Dense weight configuration."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'BM25=' in result.output
                assert 'SPLADE=' in result.output
                assert 'Dense=' in result.output

    def test_explain_shows_raw_scores(self, runner, mock_opensearch_searcher):
        """Test --explain shows raw and normalized scores for each document."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'Raw score' in result.output
                assert 'Normalized' in result.output
                assert 'Final' in result.output

    def test_explain_shows_document_details(self, runner, mock_opensearch_searcher):
        """Test --explain shows framework and title for each document."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'fastapi' in result.output
                assert 'FastAPI Introduction' in result.output
                assert 'Document Scores' in result.output

    def test_explain_shows_framework_scores(self, runner, mock_opensearch_searcher):
        """Test --explain shows framework/folder scores."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'Framework Scores' in result.output

    def test_explain_shows_pipeline_info(self, runner, mock_opensearch_searcher):
        """Test --explain shows search pipeline information."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                assert 'hybrid_search_pipeline' in result.output
                assert 'min_max' in result.output

    def test_explain_with_empty_results(self, runner, mock_empty_opensearch_searcher):
        """Test --explain handles empty results gracefully."""
        mock_formatter = _make_mock_formatter("no results")

        with patch(PATCH_GET_SEARCHER, return_value=mock_empty_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'nothing here', '--explain'])

                assert result.exit_code == 0
                assert 'Scoring Breakdown' in result.output
                # Should not crash with empty results

    def test_explain_shows_highlights(self, runner, mock_opensearch_searcher):
        """Test --explain shows highlighted content when available."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--explain'])

                assert result.exit_code == 0
                # First document has highlighted_content set
                assert 'Highlight' in result.output


class TestVerboseFlag:
    """Tests for the --verbose flag with opensearch backend."""

    def test_verbose_shows_search_metrics(self, runner, mock_opensearch_searcher):
        """Test --verbose displays search metrics section."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'Search Metrics' in result.output

    def test_verbose_shows_backend_info(self, runner, mock_opensearch_searcher):
        """Test --verbose shows OpenSearch backend identifier."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'OpenSearch (hybrid)' in result.output

    def test_verbose_shows_splade_status(self, runner, mock_opensearch_searcher):
        """Test --verbose shows SPLADE enabled/disabled status."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'SPLADE:' in result.output
                assert 'BM25:' in result.output
                assert 'Dense vectors:' in result.output

    def test_verbose_shows_timing(self, runner, mock_opensearch_searcher):
        """Test --verbose shows timing information."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'OpenSearch took:' in result.output
                assert 'Total latency:' in result.output
                assert '15ms' in result.output

    def test_verbose_shows_hit_counts(self, runner, mock_opensearch_searcher):
        """Test --verbose shows total hits and returned count."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'Total hits: 42' in result.output
                assert 'Returned: 2' in result.output

    def test_verbose_shows_weights(self, runner, mock_opensearch_searcher):
        """Test --verbose shows component weights."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'FastAPI middleware', '--verbose'])

                assert result.exit_code == 0
                assert 'Weights:' in result.output
                assert 'BM25=0.3' in result.output
                assert 'SPLADE=0.4' in result.output
                assert 'Dense=0.3' in result.output

    def test_verbose_and_explain_combined(self, runner, mock_opensearch_searcher):
        """Test --verbose and --explain can be used together."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, [
                    'search', 'FastAPI middleware',
                    '--verbose', '--explain',
                ])

                assert result.exit_code == 0
                assert 'Search Metrics' in result.output
                assert 'Scoring Breakdown' in result.output


class TestBackendFlagValidation:
    """Tests for --backend flag edge cases."""

    def test_invalid_backend_rejected(self, runner):
        """Test that invalid backend values are rejected by Click."""
        result = runner.invoke(cli, ['search', 'test', '--backend', 'invalid'])
        assert result.exit_code != 0
        assert "Invalid value" in result.output or "invalid" in result.output.lower()

    def test_backend_short_flag(self, runner, mock_opensearch_searcher):
        """Test -b short flag works."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '-b', 'opensearch'])

                assert result.exit_code == 0

    def test_explain_short_flag(self, runner, mock_opensearch_searcher):
        """Test -e short flag works for explain."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '-e'])

                assert result.exit_code == 0
                assert 'Scoring Breakdown' in result.output

    def test_verbose_short_flag(self, runner, mock_opensearch_searcher):
        """Test -v short flag works for verbose."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '-v'])

                assert result.exit_code == 0
                assert 'Search Metrics' in result.output


class TestFormatterIntegration:
    """Tests verifying CLI correctly configures the formatter."""

    def test_no_preview_flag_disables_preview(self, runner, mock_opensearch_searcher):
        """Test --no-preview disables content preview in formatter."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '--no-preview'])

                assert result.exit_code == 0
                assert mock_formatter.show_content_preview is False

    def test_no_scores_flag_disables_scores(self, runner, mock_opensearch_searcher):
        """Test --no-scores disables score display in formatter."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test', '--no-scores'])

                assert result.exit_code == 0
                assert mock_formatter.show_scores is False

    def test_default_shows_preview_and_scores(self, runner, mock_opensearch_searcher):
        """Test default behavior shows preview and scores."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test'])

                assert result.exit_code == 0
                assert mock_formatter.show_content_preview is True
                assert mock_formatter.show_scores is True


class TestSearchResultsWrapping:
    """Tests for wrapping OpenSearch results into SearchResults format."""

    def test_opensearch_results_wrapped_correctly(self, runner, mock_opensearch_searcher):
        """Test opensearch DataFrame results are wrapped in SearchResults."""
        mock_formatter = _make_mock_formatter("wrapped")

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, ['search', 'test'])

                assert result.exit_code == 0

                # Verify format_results was called with a SearchResults object
                call_args = mock_formatter.format_results.call_args
                search_results = call_args[0][0]

                from search.searcher.results import SearchResults
                assert isinstance(search_results, SearchResults)
                assert search_results.query == 'test'
                assert search_results.total_documents == 2
                assert search_results.total_folders == 1

    def test_opensearch_folder_limit_passed(self, runner, mock_opensearch_searcher):
        """Test folder-limit parameter is passed to search_folders."""
        mock_formatter = _make_mock_formatter()

        with patch(PATCH_GET_SEARCHER, return_value=mock_opensearch_searcher):
            with patch(PATCH_GET_FORMATTER, return_value=mock_formatter):
                result = runner.invoke(cli, [
                    'search', 'test',
                    '--folder-limit', '3',
                ])

                assert result.exit_code == 0
                call_kwargs = mock_opensearch_searcher.search_folders.call_args
                assert call_kwargs.kwargs.get('size') == 3
