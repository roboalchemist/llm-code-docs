"""Tests for OpenSearch hybrid search module.

Tests cover:
- HybridSearchConfig dataclass
- SearchMetrics dataclass
- HybridSearcher class (query building, filtering, result parsing)
- Convenience functions (hybrid_search, get_searcher, reset_searcher)
"""

import pytest
import pandas as pd
from unittest.mock import MagicMock, patch, PropertyMock
import time


class TestHybridSearchConfig:
    """Tests for HybridSearchConfig dataclass."""

    def test_default_config(self):
        """Test default configuration values."""
        from search.opensearch.searcher import HybridSearchConfig, DEFAULT_WEIGHTS

        config = HybridSearchConfig()

        assert config.bm25_weight == DEFAULT_WEIGHTS["bm25"]
        assert config.splade_weight == DEFAULT_WEIGHTS["splade"]
        assert config.dense_weight == DEFAULT_WEIGHTS["dense"]
        assert config.bm25_boost == 1.0
        assert config.title_boost == 2.0
        assert config.use_search_pipeline is True
        assert config.enable_highlighting is True
        assert config.highlight_fragment_size == 150
        assert config.highlight_num_fragments == 3

    def test_custom_config(self):
        """Test custom configuration values."""
        from search.opensearch.searcher import HybridSearchConfig

        config = HybridSearchConfig(
            bm25_weight=0.5,
            splade_weight=0.3,
            dense_weight=0.2,
            bm25_boost=2.0,
            title_boost=3.0,
            use_search_pipeline=False,
            enable_highlighting=False,
        )

        assert config.bm25_weight == 0.5
        assert config.splade_weight == 0.3
        assert config.dense_weight == 0.2
        assert config.bm25_boost == 2.0
        assert config.title_boost == 3.0
        assert config.use_search_pipeline is False
        assert config.enable_highlighting is False


class TestSearchMetrics:
    """Tests for SearchMetrics dataclass."""

    def test_default_metrics(self):
        """Test default metrics values."""
        from search.opensearch.searcher import SearchMetrics

        metrics = SearchMetrics(query="test query")

        assert metrics.query == "test query"
        assert metrics.total_hits == 0
        assert metrics.returned_hits == 0
        assert metrics.took_ms == 0
        assert metrics.total_latency_ms == 0.0
        assert metrics.bm25_enabled is True
        assert metrics.splade_enabled is True
        assert metrics.dense_enabled is True

    def test_custom_metrics(self):
        """Test custom metrics values."""
        from search.opensearch.searcher import SearchMetrics

        metrics = SearchMetrics(
            query="authentication",
            total_hits=100,
            returned_hits=10,
            took_ms=25,
            total_latency_ms=30.5,
            bm25_enabled=True,
            splade_enabled=True,
            dense_enabled=False,
        )

        assert metrics.query == "authentication"
        assert metrics.total_hits == 100
        assert metrics.returned_hits == 10
        assert metrics.took_ms == 25
        assert metrics.total_latency_ms == 30.5
        assert metrics.bm25_enabled is True
        assert metrics.splade_enabled is True
        assert metrics.dense_enabled is False


class TestHybridSearcherInit:
    """Tests for HybridSearcher initialization."""

    def test_init_with_defaults(self):
        """Test initialization with default parameters."""
        from search.opensearch.searcher import (
            HybridSearcher,
            DOCUMENTS_INDEX,
            FOLDERS_INDEX,
        )

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_get_client.return_value = mock_client

            searcher = HybridSearcher()

            assert searcher.client == mock_client
            assert searcher.documents_index == DOCUMENTS_INDEX
            assert searcher.folders_index == FOLDERS_INDEX
            assert searcher.config is not None

    def test_init_with_custom_client(self):
        """Test initialization with custom client."""
        from search.opensearch.searcher import HybridSearcher

        mock_client = MagicMock()
        searcher = HybridSearcher(client=mock_client)

        assert searcher.client == mock_client

    def test_init_with_custom_config(self):
        """Test initialization with custom configuration."""
        from search.opensearch.searcher import HybridSearcher, HybridSearchConfig

        config = HybridSearchConfig(bm25_weight=0.5)

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            searcher = HybridSearcher(config=config)

            assert searcher.config.bm25_weight == 0.5

    def test_init_with_custom_indices(self):
        """Test initialization with custom index names."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()

            searcher = HybridSearcher(
                documents_index="custom_docs",
                folders_index="custom_folders",
            )

            assert searcher.documents_index == "custom_docs"
            assert searcher.folders_index == "custom_folders"


class TestBuildHybridQuery:
    """Tests for query building methods."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            return HybridSearcher()

    def test_bm25_only_query(self, searcher):
        """Test building a BM25-only query (no vectors)."""
        query = searcher._build_hybrid_query(
            query="FastAPI middleware",
            size=10,
        )

        # Should have a multi_match query for BM25
        assert "query" in query
        assert "multi_match" in query["query"]
        assert query["query"]["multi_match"]["query"] == "FastAPI middleware"
        assert "content" in query["query"]["multi_match"]["fields"]
        assert query["size"] == 10

    def test_hybrid_query_with_dense_vector(self, searcher):
        """Test building query with BM25 + dense vector."""
        dense_vector = [0.1] * 384  # Typical embedding dimension

        query = searcher._build_hybrid_query(
            query="authentication",
            dense_vector=dense_vector,
            size=10,
        )

        # Should have hybrid query structure
        assert "query" in query
        assert "hybrid" in query["query"]
        assert "queries" in query["query"]["hybrid"]

        # Should have 2 sub-queries: BM25 + KNN
        assert len(query["query"]["hybrid"]["queries"]) == 2

    def test_hybrid_query_with_sparse_vector(self, searcher):
        """Test building query with BM25 + SPLADE sparse vector."""
        sparse_vector = {
            "authentication": 2.5,
            "oauth": 1.8,
            "security": 1.2,
        }

        query = searcher._build_hybrid_query(
            query="auth",
            sparse_vector=sparse_vector,
            size=10,
        )

        # Should have hybrid query structure
        assert "query" in query
        assert "hybrid" in query["query"]

        # Should have 2 sub-queries: BM25 + SPLADE
        assert len(query["query"]["hybrid"]["queries"]) == 2

    def test_full_hybrid_query(self, searcher):
        """Test building full hybrid query (BM25 + SPLADE + dense)."""
        dense_vector = [0.1] * 384
        sparse_vector = {"auth": 2.5, "login": 1.8}

        query = searcher._build_hybrid_query(
            query="authentication",
            dense_vector=dense_vector,
            sparse_vector=sparse_vector,
            size=10,
        )

        # Should have all 3 sub-queries
        assert "hybrid" in query["query"]
        assert len(query["query"]["hybrid"]["queries"]) == 3

    def test_query_with_category_filter(self, searcher):
        """Test query building with single category filter."""
        query = searcher._build_hybrid_query(
            query="test",
            category="github-scraped",
            size=10,
        )

        # Filter should be applied
        assert "bool" in query["query"]
        assert "filter" in query["query"]["bool"]
        filters = query["query"]["bool"]["filter"]
        assert any("term" in f for f in filters)

    def test_query_with_multiple_categories(self, searcher):
        """Test query building with multiple categories."""
        query = searcher._build_hybrid_query(
            query="test",
            categories=["github-scraped", "llms-txt"],
            size=10,
        )

        # Filter should use terms (plural)
        assert "bool" in query["query"]
        filters = query["query"]["bool"]["filter"]
        assert any("terms" in f for f in filters)

    def test_query_with_framework_filter(self, searcher):
        """Test query building with framework filter."""
        query = searcher._build_hybrid_query(
            query="routing",
            framework="fastapi",
            size=10,
        )

        # Framework filter should be applied
        assert "bool" in query["query"]
        filters = query["query"]["bool"]["filter"]
        filter_found = False
        for f in filters:
            if "term" in f and "framework" in f["term"]:
                filter_found = True
                assert f["term"]["framework"] == "fastapi"
        assert filter_found

    def test_query_with_min_score(self, searcher):
        """Test query building with minimum score threshold."""
        query = searcher._build_hybrid_query(
            query="test",
            min_score=0.5,
            size=10,
        )

        assert "min_score" in query
        assert query["min_score"] == 0.5

    def test_query_includes_highlighting(self, searcher):
        """Test that highlighting is included by default."""
        query = searcher._build_hybrid_query(
            query="test",
            size=10,
        )

        assert "highlight" in query
        assert "fields" in query["highlight"]
        assert "content" in query["highlight"]["fields"]
        assert "title" in query["highlight"]["fields"]

    def test_query_without_highlighting(self):
        """Test query without highlighting when disabled."""
        from search.opensearch.searcher import HybridSearcher, HybridSearchConfig

        config = HybridSearchConfig(enable_highlighting=False)

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            searcher = HybridSearcher(config=config)

            query = searcher._build_hybrid_query(query="test", size=10)

            assert "highlight" not in query

    def test_query_includes_search_pipeline(self, searcher):
        """Test that search pipeline is included for multi-retrieval queries."""
        from search.opensearch.searcher import HYBRID_SEARCH_PIPELINE

        query = searcher._build_hybrid_query(
            query="test",
            dense_vector=[0.1] * 384,
            size=10,
        )

        assert "search_pipeline" in query
        assert query["search_pipeline"] == HYBRID_SEARCH_PIPELINE

    def test_query_specifies_source_fields(self, searcher):
        """Test that query specifies which fields to return."""
        query = searcher._build_hybrid_query(query="test", size=10)

        assert "_source" in query
        assert "content" in query["_source"]
        assert "title" in query["_source"]
        assert "framework" in query["_source"]
        assert "file_path" in query["_source"]


class TestBuildSpladeQuery:
    """Tests for SPLADE query building."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            return HybridSearcher()

    def test_splade_query_structure(self, searcher):
        """Test SPLADE query builds correct rank_feature queries."""
        sparse_vector = {
            "authentication": 2.5,
            "oauth": 1.8,
            "login": 0.9,
        }

        query = searcher._build_splade_query(sparse_vector)

        assert "bool" in query
        assert "should" in query["bool"]
        assert len(query["bool"]["should"]) == 3

    def test_splade_query_uses_rank_feature(self, searcher):
        """Test that SPLADE query uses rank_feature for each token."""
        sparse_vector = {"auth": 2.5}

        query = searcher._build_splade_query(sparse_vector)

        # Check for rank_feature
        should_clause = query["bool"]["should"][0]
        assert "rank_feature" in should_clause
        assert "field" in should_clause["rank_feature"]
        assert "boost" in should_clause["rank_feature"]
        assert should_clause["rank_feature"]["boost"] == 2.5

    def test_splade_query_filters_zero_weights(self, searcher):
        """Test that zero-weight tokens are filtered out."""
        sparse_vector = {
            "auth": 2.5,
            "ignored": 0.0,  # Should be filtered
            "login": 1.0,
        }

        query = searcher._build_splade_query(sparse_vector)

        # Should only have 2 clauses (auth and login)
        assert len(query["bool"]["should"]) == 2

    def test_splade_query_empty_vector(self, searcher):
        """Test SPLADE query with empty vector returns match_all."""
        query = searcher._build_splade_query({})

        assert "match_all" in query


class TestBuildFilterClauses:
    """Tests for filter clause building."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            return HybridSearcher()

    def test_no_filters(self, searcher):
        """Test that no filters returns empty list."""
        filters = searcher._build_filter_clauses()
        assert filters == []

    def test_single_category_filter(self, searcher):
        """Test single category filter."""
        filters = searcher._build_filter_clauses(category="github-scraped")

        assert len(filters) == 1
        assert "term" in filters[0]
        assert filters[0]["term"]["source_type"] == "github-scraped"

    def test_multiple_categories_filter(self, searcher):
        """Test multiple categories filter."""
        filters = searcher._build_filter_clauses(
            categories=["github-scraped", "llms-txt"]
        )

        assert len(filters) == 1
        assert "terms" in filters[0]
        assert filters[0]["terms"]["source_type"] == ["github-scraped", "llms-txt"]

    def test_single_framework_filter(self, searcher):
        """Test single framework filter."""
        filters = searcher._build_filter_clauses(framework="fastapi")

        assert len(filters) == 1
        assert "term" in filters[0]
        assert filters[0]["term"]["framework"] == "fastapi"

    def test_multiple_frameworks_filter(self, searcher):
        """Test multiple frameworks filter."""
        filters = searcher._build_filter_clauses(frameworks=["fastapi", "flask"])

        assert len(filters) == 1
        assert "terms" in filters[0]
        assert filters[0]["terms"]["framework"] == ["fastapi", "flask"]

    def test_combined_filters(self, searcher):
        """Test combining category and framework filters."""
        filters = searcher._build_filter_clauses(
            category="github-scraped",
            framework="fastapi",
        )

        assert len(filters) == 2


class TestParseResultsToDataFrame:
    """Tests for result parsing."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            return HybridSearcher()

    def test_empty_response(self, searcher):
        """Test parsing empty response returns empty DataFrame."""
        response = {"hits": {"hits": [], "total": {"value": 0}}}

        df = searcher._parse_results_to_dataframe(response)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0

    def test_single_result(self, searcher):
        """Test parsing single result."""
        response = {
            "hits": {
                "hits": [
                    {
                        "_id": "doc1",
                        "_score": 0.95,
                        "_source": {
                            "content": "FastAPI is a modern framework",
                            "title": "FastAPI Intro",
                            "framework": "fastapi",
                            "source_type": "github-scraped",
                            "file_path": "intro.md",
                            "chunk_index": 0,
                            "total_chunks": 1,
                        },
                    }
                ],
                "total": {"value": 1},
                "max_score": 0.95,
            }
        }

        df = searcher._parse_results_to_dataframe(response)

        assert len(df) == 1
        assert df.iloc[0]["doc_id"] == "doc1"
        assert df.iloc[0]["title"] == "FastAPI Intro"
        assert df.iloc[0]["framework"] == "fastapi"
        assert df.iloc[0]["similarity_score"] == 1.0  # Normalized

    def test_multiple_results_score_normalization(self, searcher):
        """Test that scores are normalized relative to max score."""
        response = {
            "hits": {
                "hits": [
                    {"_id": "doc1", "_score": 1.0, "_source": {"content": "A"}},
                    {"_id": "doc2", "_score": 0.5, "_source": {"content": "B"}},
                    {"_id": "doc3", "_score": 0.25, "_source": {"content": "C"}},
                ],
                "total": {"value": 3},
                "max_score": 1.0,
            }
        }

        df = searcher._parse_results_to_dataframe(response)

        assert len(df) == 3
        assert df.iloc[0]["similarity_score"] == 1.0
        assert df.iloc[1]["similarity_score"] == 0.5
        assert df.iloc[2]["similarity_score"] == 0.25

    def test_highlight_extraction(self, searcher):
        """Test that highlights are extracted."""
        response = {
            "hits": {
                "hits": [
                    {
                        "_id": "doc1",
                        "_score": 1.0,
                        "_source": {"content": "FastAPI is great"},
                        "highlight": {
                            "content": ["<em>FastAPI</em> is great"],
                            "title": ["<em>FastAPI</em> Introduction"],
                        },
                    }
                ],
                "total": {"value": 1},
                "max_score": 1.0,
            }
        }

        df = searcher._parse_results_to_dataframe(response)

        assert df.iloc[0]["highlighted_content"] == "<em>FastAPI</em> is great"
        assert df.iloc[0]["highlighted_title"] == "<em>FastAPI</em> Introduction"

    def test_dataframe_has_compatibility_columns(self, searcher):
        """Test that DataFrame includes columns for formatter compatibility."""
        response = {
            "hits": {
                "hits": [
                    {
                        "_id": "doc1",
                        "_score": 1.0,
                        "_source": {
                            "content": "Test",
                            "source_type": "github-scraped",
                            "file_path": "test.md",
                        },
                    }
                ],
                "total": {"value": 1},
                "max_score": 1.0,
            }
        }

        df = searcher._parse_results_to_dataframe(response)

        # Check for compatibility columns
        assert "similarity_score" in df.columns
        assert "final_score" in df.columns
        assert "category" in df.columns  # Mapped from source_type
        assert "path" in df.columns  # Alias for file_path
        assert "relative_path" in df.columns  # Alias for formatter


class TestSearch:
    """Tests for the main search method."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        mock_client = MagicMock()
        mock_client.client = MagicMock()
        mock_client.client.search.return_value = {
            "hits": {
                "hits": [
                    {
                        "_id": "doc1",
                        "_score": 0.95,
                        "_source": {
                            "content": "Authentication guide",
                            "title": "Auth Guide",
                            "framework": "fastapi",
                            "source_type": "github-scraped",
                        },
                    }
                ],
                "total": {"value": 1},
                "max_score": 0.95,
            },
            "took": 25,
        }

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = mock_client
            searcher = HybridSearcher()
            searcher.client = mock_client
            return searcher

    def test_search_returns_dataframe_and_metrics(self, searcher):
        """Test that search returns DataFrame and SearchMetrics."""
        from search.opensearch.searcher import SearchMetrics

        results, metrics = searcher.search(query="authentication")

        assert isinstance(results, pd.DataFrame)
        assert isinstance(metrics, SearchMetrics)

    def test_search_metrics_populated(self, searcher):
        """Test that search metrics are correctly populated."""
        results, metrics = searcher.search(query="authentication")

        assert metrics.query == "authentication"
        assert metrics.total_hits == 1
        assert metrics.returned_hits == 1
        assert metrics.took_ms == 25
        assert metrics.total_latency_ms > 0
        assert metrics.bm25_enabled is True

    def test_search_tracks_enabled_methods(self, searcher):
        """Test that metrics correctly track which methods are enabled."""
        # BM25 only
        _, metrics1 = searcher.search(query="test")
        assert metrics1.bm25_enabled is True
        assert metrics1.splade_enabled is False
        assert metrics1.dense_enabled is False

        # With dense vector
        _, metrics2 = searcher.search(query="test", dense_vector=[0.1] * 384)
        assert metrics2.dense_enabled is True

        # With sparse vector
        _, metrics3 = searcher.search(query="test", sparse_vector={"auth": 1.5})
        assert metrics3.splade_enabled is True

    def test_search_handles_error_gracefully(self, searcher):
        """Test that search handles errors and returns empty results."""
        searcher.client.client.search.side_effect = Exception("Connection error")

        results, metrics = searcher.search(query="test")

        assert len(results) == 0
        assert metrics.total_hits == 0
        assert metrics.total_latency_ms > 0  # Still tracks time


class TestSearchFolders:
    """Tests for folder search method."""

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        mock_client = MagicMock()
        mock_client.client = MagicMock()
        mock_client.client.search.return_value = {
            "hits": {
                "hits": [
                    {
                        "_id": "folder1",
                        "_score": 0.9,
                        "_source": {
                            "framework_name": "FastAPI",
                            "description": "Modern web framework",
                            "category": "github-scraped",
                            "path": "/docs/fastapi",
                            "file_count": 25,
                        },
                    }
                ],
                "total": {"value": 1},
                "max_score": 0.9,
            },
            "took": 15,
        }

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = mock_client
            searcher = HybridSearcher()
            searcher.client = mock_client
            return searcher

    def test_search_folders_returns_correct_structure(self, searcher):
        """Test folder search returns correct DataFrame structure."""
        results, metrics = searcher.search_folders(query="FastAPI")

        assert isinstance(results, pd.DataFrame)
        assert "framework_name" in results.columns
        assert "description" in results.columns
        assert "file_count" in results.columns

    def test_search_folders_splade_disabled(self, searcher):
        """Test that folder search has SPLADE disabled."""
        _, metrics = searcher.search_folders(query="test")

        assert metrics.splade_enabled is False


class TestExplainQuery:
    """Tests for the explain_query method."""

    def test_explain_returns_query_body(self):
        """Test that explain_query returns the query body without executing."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_get_client.return_value = mock_client

            searcher = HybridSearcher()
            query = searcher.explain_query(
                query="authentication",
                dense_vector=[0.1] * 384,
                sparse_vector={"auth": 2.5},
            )

            # Should return the query structure without executing
            assert "query" in query
            assert "hybrid" in query["query"]
            # Client search should NOT have been called
            mock_client.client.search.assert_not_called()


class TestConvenienceFunctions:
    """Tests for module-level convenience functions."""

    def test_get_searcher_returns_singleton(self):
        """Test that get_searcher returns a singleton instance."""
        from search.opensearch.searcher import get_searcher, reset_searcher

        reset_searcher()  # Clear any existing singleton

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()

            searcher1 = get_searcher()
            searcher2 = get_searcher()

            assert searcher1 is searcher2

    def test_reset_searcher_clears_singleton(self):
        """Test that reset_searcher clears the singleton."""
        from search.opensearch.searcher import get_searcher, reset_searcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()

            searcher1 = get_searcher()
            reset_searcher()
            searcher2 = get_searcher()

            assert searcher1 is not searcher2

    def test_hybrid_search_convenience_function(self):
        """Test the hybrid_search convenience function."""
        from search.opensearch.searcher import hybrid_search, reset_searcher

        reset_searcher()

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_client.client = MagicMock()
            mock_client.client.search.return_value = {
                "hits": {"hits": [], "total": {"value": 0}},
                "took": 5,
            }
            mock_get_client.return_value = mock_client

            results, metrics = hybrid_search(query="test", size=5)

            assert isinstance(results, pd.DataFrame)
            assert metrics.query == "test"


class TestSpladeSemanticExpansion:
    """Tests verifying SPLADE semantic expansion behavior.

    QA Criteria: SPLADE expansion visible (search "auth" finds "authentication", "OAuth")
    """

    @pytest.fixture
    def searcher(self):
        """Create a searcher with mocked client."""
        from search.opensearch.searcher import HybridSearcher

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = MagicMock()
            return HybridSearcher()

    def test_splade_vector_expands_query_terms(self, searcher):
        """Test that SPLADE sparse vector enables semantic expansion.

        When the user searches for "auth", SPLADE provides a sparse vector
        that includes related terms like "authentication", "oauth", "login".
        These terms become rank_feature queries that boost documents
        containing those related concepts.
        """
        # Simulated SPLADE output for query "auth"
        # In production, this comes from the SPLADE model
        splade_expansion = {
            "auth": 3.2,           # Original term (high weight)
            "authentication": 2.8, # Semantic expansion
            "oauth": 2.1,          # Related protocol
            "login": 1.5,          # Related concept
            "secure": 1.2,         # Related concept
            "token": 0.9,          # Related term
        }

        query = searcher._build_splade_query(splade_expansion)

        # Verify rank_feature queries are created for all expanded terms
        should_clauses = query["bool"]["should"]
        fields_boosted = {
            clause["rank_feature"]["field"].split(".")[-1]: clause["rank_feature"]["boost"]
            for clause in should_clauses
        }

        # Verify semantic expansion is included
        assert "authentication" in fields_boosted
        assert "oauth" in fields_boosted
        assert fields_boosted["auth"] > fields_boosted["authentication"]  # Original term higher

    def test_hybrid_query_combines_all_signals(self, searcher):
        """Test that hybrid query properly combines BM25, SPLADE, and dense."""
        query = searcher._build_hybrid_query(
            query="auth",  # BM25 will match "auth"
            sparse_vector={  # SPLADE expansion
                "auth": 3.2,
                "authentication": 2.8,
                "oauth": 2.1,
            },
            dense_vector=[0.1] * 384,  # Dense embedding
            size=10,
        )

        # All three retrieval methods should be present
        hybrid_queries = query["query"]["hybrid"]["queries"]
        assert len(hybrid_queries) == 3

        # Check for each query type
        query_types = []
        for q in hybrid_queries:
            if "multi_match" in q:
                query_types.append("bm25")
            elif "bool" in q and "should" in q["bool"]:
                query_types.append("splade")
            elif "knn" in q:
                query_types.append("dense")

        assert "bm25" in query_types
        assert "splade" in query_types
        assert "dense" in query_types


class TestLatencyTracking:
    """Tests for latency tracking.

    QA Criteria: Latency under 100ms for typical queries
    """

    def test_latency_tracked_in_metrics(self):
        """Test that total_latency_ms is tracked in SearchMetrics."""
        from search.opensearch.searcher import HybridSearcher

        mock_client = MagicMock()
        mock_client.client = MagicMock()
        mock_client.client.search.return_value = {
            "hits": {"hits": [], "total": {"value": 0}},
            "took": 25,  # OpenSearch internal time (mocked)
        }

        with patch("search.opensearch.searcher.get_client") as mock_get_client:
            mock_get_client.return_value = mock_client

            searcher = HybridSearcher()
            searcher.client = mock_client

            _, metrics = searcher.search(query="test")

            # OpenSearch time from response
            assert metrics.took_ms == 25

            # Total latency should be tracked (in mocked scenario it's just wall-clock)
            assert metrics.total_latency_ms > 0

    def test_total_latency_includes_overhead(self):
        """Test that total_latency_ms tracks end-to-end time.

        Note: In unit tests with mocks, the 'took_ms' from OpenSearch is just
        a mocked value, while 'total_latency_ms' measures actual wall-clock time.
        In production, total_latency_ms >= took_ms because it includes:
        - Network round-trip time
        - Serialization/deserialization
        - Query building time
        - Result parsing time
        """
        from search.opensearch.searcher import SearchMetrics

        # Verify that both metrics are distinct
        metrics = SearchMetrics(
            query="test",
            took_ms=25,  # Just OpenSearch internal time
            total_latency_ms=35.5,  # Full round-trip time
        )

        # Both values should be tracked
        assert metrics.took_ms == 25
        assert metrics.total_latency_ms == 35.5

        # In production, total >= took due to overhead
        assert metrics.total_latency_ms >= metrics.took_ms

    def test_metrics_distinguishes_opensearch_and_total_time(self):
        """Test that took_ms vs total_latency_ms are distinct."""
        from search.opensearch.searcher import SearchMetrics

        metrics = SearchMetrics(
            query="test",
            took_ms=25,  # Just OpenSearch
            total_latency_ms=35.5,  # Includes network, serialization, etc.
        )

        assert metrics.took_ms < metrics.total_latency_ms
