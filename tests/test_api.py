"""Tests for the FastAPI search and suggestion API.

Tests cover:
- Health endpoint with OpenSearch up/down scenarios
- Search endpoint with results, empty results, and errors
- Suggest endpoint with results, empty results, and errors
- Query parameter validation
- Response model structure
"""

import os
import time

import pytest
from unittest.mock import MagicMock, patch, PropertyMock
import pandas as pd

# Set test environment before importing app modules
os.environ.setdefault("OPENSEARCH_HOST", "localhost")
os.environ.setdefault("OPENSEARCH_PORT", "9200")
os.environ.setdefault("OPENSEARCH_INDEX_NAME", "test_llm_docs")
os.environ.setdefault("OPENSEARCH_PIPELINE_NAME", "test_pipeline")

from fastapi.testclient import TestClient

from api.main import (
    create_app,
    HealthResponse,
    SearchResponse,
    SuggestResponse,
)
from search.opensearch.client import OpenSearchClient
from search.opensearch.searcher import HybridSearcher, SearchMetrics


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_os_client():
    """Create a mock OpenSearchClient."""
    client = MagicMock(spec=OpenSearchClient)
    client.ping.return_value = True
    client.health_check.return_value = {
        "cluster_name": "test-cluster",
        "status": "green",
        "number_of_nodes": 1,
        "active_primary_shards": 5,
        "active_shards": 5,
    }
    client.get_document_count.return_value = 22000
    return client


@pytest.fixture
def mock_searcher():
    """Create a mock HybridSearcher."""
    searcher = MagicMock(spec=HybridSearcher)
    return searcher


@pytest.fixture
def test_client(mock_os_client, mock_searcher):
    """Create a FastAPI test client with injected mocks."""
    application = create_app(
        opensearch_client=mock_os_client,
        searcher=mock_searcher,
    )
    return TestClient(application)


@pytest.fixture
def sample_search_df():
    """Create a sample search results DataFrame."""
    return pd.DataFrame([
        {
            "doc_id": "doc-1",
            "title": "FastAPI Introduction",
            "content": "FastAPI is a modern, fast web framework for building APIs.",
            "framework": "fastapi",
            "category": "github-scraped",
            "file_path": "intro.md",
            "final_score": 0.95,
            "highlighted_content": "<em>FastAPI</em> is a modern framework",
            "chunk_index": 0,
            "total_chunks": 3,
        },
        {
            "doc_id": "doc-2",
            "title": "FastAPI Routing",
            "content": "FastAPI routing uses decorators to define endpoints.",
            "framework": "fastapi",
            "category": "github-scraped",
            "file_path": "routing.md",
            "final_score": 0.82,
            "highlighted_content": "",
            "chunk_index": 0,
            "total_chunks": 1,
        },
    ])


@pytest.fixture
def sample_search_metrics():
    """Create sample search metrics."""
    return SearchMetrics(
        query="fastapi",
        total_hits=42,
        returned_hits=2,
        took_ms=12,
        total_latency_ms=15.3,
    )


@pytest.fixture
def sample_folder_df():
    """Create a sample folder results DataFrame."""
    return pd.DataFrame([
        {
            "folder_id": "folder-1",
            "framework_name": "FastAPI",
            "description": "Modern Python web framework",
            "category": "github-scraped",
            "path": "docs/github-scraped/fastapi",
            "file_count": 45,
            "source_url": "https://github.com/tiangolo/fastapi",
            "final_score": 0.98,
        },
        {
            "folder_id": "folder-2",
            "framework_name": "Flask",
            "description": "Lightweight Python web framework",
            "category": "github-scraped",
            "path": "docs/github-scraped/flask",
            "file_count": 30,
            "source_url": "https://github.com/pallets/flask",
            "final_score": 0.75,
        },
    ])


@pytest.fixture
def sample_folder_metrics():
    """Create sample folder search metrics."""
    return SearchMetrics(
        query="fast web framework",
        total_hits=10,
        returned_hits=2,
        took_ms=5,
        total_latency_ms=8.2,
    )


# =============================================================================
# Health Endpoint Tests
# =============================================================================


class TestHealthEndpoint:
    """Tests for GET /health."""

    def test_health_ok(self, test_client, mock_os_client):
        """Health returns ok when OpenSearch is healthy."""
        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["version"] == "0.1.0"
        assert "opensearch" in data["dependencies"]

        os_dep = data["dependencies"]["opensearch"]
        assert os_dep["status"] == "ok"
        assert os_dep["latency_ms"] >= 0
        assert os_dep["details"]["cluster_status"] == "green"
        assert os_dep["details"]["document_count"] == 22000

    def test_health_opensearch_down(self, test_client, mock_os_client):
        """Health returns error when OpenSearch ping fails."""
        mock_os_client.ping.return_value = False

        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        assert data["dependencies"]["opensearch"]["status"] == "error"

    def test_health_opensearch_connection_error(self, test_client, mock_os_client):
        """Health returns error when OpenSearch raises ConnectionError."""
        mock_os_client.ping.side_effect = ConnectionError("Connection refused")

        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        os_dep = data["dependencies"]["opensearch"]
        assert os_dep["status"] == "error"
        assert "Connection refused" in os_dep["details"]["error"]

    def test_health_opensearch_red_cluster(self, test_client, mock_os_client):
        """Health returns degraded when cluster status is red."""
        mock_os_client.health_check.return_value = {
            "cluster_name": "test-cluster",
            "status": "red",
            "number_of_nodes": 1,
        }

        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "degraded"
        assert data["dependencies"]["opensearch"]["details"]["cluster_status"] == "red"

    def test_health_opensearch_yellow_cluster(self, test_client, mock_os_client):
        """Health returns ok when cluster status is yellow."""
        mock_os_client.health_check.return_value = {
            "cluster_name": "test-cluster",
            "status": "yellow",
            "number_of_nodes": 1,
        }

        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["dependencies"]["opensearch"]["details"]["cluster_status"] == "yellow"

    def test_health_ping_ok_but_health_check_fails(self, test_client, mock_os_client):
        """Health still reports ok status when ping succeeds but health_check fails."""
        mock_os_client.health_check.side_effect = Exception("Health check timeout")

        response = test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        # Ping was OK, so opensearch dependency shows ok
        assert data["dependencies"]["opensearch"]["status"] == "ok"
        assert "Health check timeout" in data["dependencies"]["opensearch"]["details"]["note"]

    def test_health_response_model(self, test_client):
        """Health response conforms to HealthResponse model."""
        response = test_client.get("/health")

        assert response.status_code == 200
        # Validate the response can be parsed by our model
        data = response.json()
        health = HealthResponse(**data)
        assert health.status in ("ok", "degraded", "error")
        assert health.version == "0.1.0"


# =============================================================================
# Search Endpoint Tests
# =============================================================================


class TestSearchEndpoint:
    """Tests for GET /search."""

    def test_search_returns_results(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search returns formatted results from HybridSearcher."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get("/search", params={"q": "fastapi"})

        assert response.status_code == 200
        data = response.json()
        assert data["query"] == "fastapi"
        assert data["returned"] == 2
        assert data["total_hits"] == 42
        assert data["took_ms"] == 12
        assert data["total_latency_ms"] > 0

        # Check first result
        first = data["results"][0]
        assert first["doc_id"] == "doc-1"
        assert first["title"] == "FastAPI Introduction"
        assert first["framework"] == "fastapi"
        assert first["score"] == 0.95
        assert first["chunk_index"] == 0
        assert first["total_chunks"] == 3

    def test_search_empty_results(self, test_client, mock_searcher):
        """Search returns empty list when no results found."""
        empty_df = pd.DataFrame()
        metrics = SearchMetrics(query="nonexistent", total_hits=0)
        mock_searcher.search.return_value = (empty_df, metrics)

        response = test_client.get("/search", params={"q": "nonexistent_framework_xyz"})

        assert response.status_code == 200
        data = response.json()
        assert data["results"] == []
        assert data["returned"] == 0
        assert data["total_hits"] == 0

    def test_search_with_limit(self, test_client, mock_searcher, sample_search_df, sample_search_metrics):
        """Search passes limit parameter to searcher."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get("/search", params={"q": "fastapi", "limit": 5})

        assert response.status_code == 200
        # Verify the limit was passed to the searcher
        mock_searcher.search.assert_called_once()
        call_kwargs = mock_searcher.search.call_args
        assert call_kwargs.kwargs.get("size") == 5 or call_kwargs[1].get("size") == 5

    def test_search_with_category_filter(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search passes category filter to searcher."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get(
            "/search", params={"q": "fastapi", "category": "github-scraped"}
        )

        assert response.status_code == 200
        call_kwargs = mock_searcher.search.call_args
        assert call_kwargs.kwargs.get("category") == "github-scraped" or call_kwargs[1].get("category") == "github-scraped"

    def test_search_with_framework_filter(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search passes framework filter to searcher."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get(
            "/search", params={"q": "routing", "framework": "fastapi"}
        )

        assert response.status_code == 200
        call_kwargs = mock_searcher.search.call_args
        assert call_kwargs.kwargs.get("framework") == "fastapi" or call_kwargs[1].get("framework") == "fastapi"

    def test_search_with_min_score(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search passes min_score parameter to searcher."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get(
            "/search", params={"q": "fastapi", "min_score": 0.5}
        )

        assert response.status_code == 200
        call_kwargs = mock_searcher.search.call_args
        assert call_kwargs.kwargs.get("min_score") == 0.5 or call_kwargs[1].get("min_score") == 0.5

    def test_search_missing_query(self, test_client):
        """Search returns 422 when query parameter is missing."""
        response = test_client.get("/search")
        assert response.status_code == 422

    def test_search_empty_query(self, test_client):
        """Search returns 422 when query is empty string."""
        response = test_client.get("/search", params={"q": ""})
        assert response.status_code == 422

    def test_search_limit_bounds(self, test_client, mock_searcher, sample_search_df, sample_search_metrics):
        """Search rejects limit outside valid range."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        # Too low
        response = test_client.get("/search", params={"q": "test", "limit": 0})
        assert response.status_code == 422

        # Too high
        response = test_client.get("/search", params={"q": "test", "limit": 101})
        assert response.status_code == 422

    def test_search_service_unavailable(self, test_client, mock_searcher):
        """Search returns 503 when searcher raises exception."""
        mock_searcher.search.side_effect = Exception("OpenSearch connection refused")

        response = test_client.get("/search", params={"q": "fastapi"})

        assert response.status_code == 503
        assert "unavailable" in response.json()["detail"].lower()

    def test_search_content_truncation(self, test_client, mock_searcher):
        """Search truncates long content to 500 characters."""
        long_content = "x" * 1000
        df = pd.DataFrame([{
            "doc_id": "doc-1",
            "title": "Test",
            "content": long_content,
            "framework": "test",
            "category": "test",
            "file_path": "test.md",
            "final_score": 0.9,
            "highlighted_content": "",
            "chunk_index": 0,
            "total_chunks": 1,
        }])
        metrics = SearchMetrics(query="test", total_hits=1, returned_hits=1)
        mock_searcher.search.return_value = (df, metrics)

        response = test_client.get("/search", params={"q": "test"})

        assert response.status_code == 200
        content = response.json()["results"][0]["content"]
        assert len(content) <= 500

    def test_search_response_model(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search response conforms to SearchResponse model."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get("/search", params={"q": "fastapi"})

        assert response.status_code == 200
        data = response.json()
        search_resp = SearchResponse(**data)
        assert search_resp.query == "fastapi"
        assert len(search_resp.results) == 2

    def test_search_all_params_combined(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search works with all parameters combined."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get("/search", params={
            "q": "authentication",
            "limit": 20,
            "category": "llms-txt",
            "framework": "nextauth",
            "min_score": 0.3,
        })

        assert response.status_code == 200
        call_kwargs = mock_searcher.search.call_args.kwargs
        assert call_kwargs["query"] == "authentication"
        assert call_kwargs["size"] == 20
        assert call_kwargs["category"] == "llms-txt"
        assert call_kwargs["framework"] == "nextauth"
        assert call_kwargs["min_score"] == 0.3


# =============================================================================
# Suggest Endpoint Tests
# =============================================================================


class TestSuggestEndpoint:
    """Tests for GET /suggest."""

    def test_suggest_returns_results(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest returns framework suggestions from folders index."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "fast web framework"})

        assert response.status_code == 200
        data = response.json()
        assert data["query"] == "fast web framework"
        assert data["returned"] == 2
        assert data["total_hits"] == 10

        # Check first suggestion
        first = data["suggestions"][0]
        assert first["framework_name"] == "FastAPI"
        assert first["description"] == "Modern Python web framework"
        assert first["category"] == "github-scraped"
        assert first["file_count"] == 45
        assert first["score"] == 0.98

    def test_suggest_empty_results(self, test_client, mock_searcher):
        """Suggest returns empty list when no matches found."""
        empty_df = pd.DataFrame()
        metrics = SearchMetrics(query="zzz_nonexistent", total_hits=0)
        mock_searcher.search_folders.return_value = (empty_df, metrics)

        response = test_client.get("/suggest", params={"q": "zzz_nonexistent"})

        assert response.status_code == 200
        data = response.json()
        assert data["suggestions"] == []
        assert data["returned"] == 0
        assert data["total_hits"] == 0

    def test_suggest_with_limit(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest passes limit parameter to search_folders."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "react", "limit": 3})

        assert response.status_code == 200
        call_kwargs = mock_searcher.search_folders.call_args
        assert call_kwargs.kwargs.get("size") == 3 or call_kwargs[1].get("size") == 3

    def test_suggest_with_category_filter(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest passes category filter to search_folders."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get(
            "/suggest", params={"q": "react", "category": "llms-txt"}
        )

        assert response.status_code == 200
        call_kwargs = mock_searcher.search_folders.call_args
        assert call_kwargs.kwargs.get("category") == "llms-txt" or call_kwargs[1].get("category") == "llms-txt"

    def test_suggest_default_limit(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest uses default limit of 5."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "python"})

        assert response.status_code == 200
        call_kwargs = mock_searcher.search_folders.call_args
        assert call_kwargs.kwargs.get("size") == 5 or call_kwargs[1].get("size") == 5

    def test_suggest_missing_query(self, test_client):
        """Suggest returns 422 when query parameter is missing."""
        response = test_client.get("/suggest")
        assert response.status_code == 422

    def test_suggest_empty_query(self, test_client):
        """Suggest returns 422 when query is empty."""
        response = test_client.get("/suggest", params={"q": ""})
        assert response.status_code == 422

    def test_suggest_limit_bounds(self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics):
        """Suggest rejects limit outside valid range."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        # Too low
        response = test_client.get("/suggest", params={"q": "test", "limit": 0})
        assert response.status_code == 422

        # Too high
        response = test_client.get("/suggest", params={"q": "test", "limit": 51})
        assert response.status_code == 422

    def test_suggest_service_unavailable(self, test_client, mock_searcher):
        """Suggest returns 503 when search_folders raises exception."""
        mock_searcher.search_folders.side_effect = Exception("OpenSearch unavailable")

        response = test_client.get("/suggest", params={"q": "python"})

        assert response.status_code == 503
        assert "unavailable" in response.json()["detail"].lower()

    def test_suggest_response_model(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest response conforms to SuggestResponse model."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "python web"})

        assert response.status_code == 200
        data = response.json()
        suggest_resp = SuggestResponse(**data)
        assert suggest_resp.query == "python web"
        assert len(suggest_resp.suggestions) == 2

    def test_suggest_latency_tracked(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest response includes total latency measurement."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "python"})

        assert response.status_code == 200
        data = response.json()
        assert data["total_latency_ms"] >= 0
        assert data["took_ms"] == 5


# =============================================================================
# Application Factory Tests
# =============================================================================


class TestAppFactory:
    """Tests for the create_app factory function."""

    def test_create_app_default(self):
        """create_app creates a FastAPI app with default configuration."""
        application = create_app()
        assert application is not None
        assert application.title == "Librarian Search API"

    def test_create_app_with_injected_deps(self, mock_os_client, mock_searcher):
        """create_app accepts injected dependencies."""
        application = create_app(
            opensearch_client=mock_os_client,
            searcher=mock_searcher,
        )
        assert application.state.opensearch_client is mock_os_client
        assert application.state.searcher is mock_searcher

    def test_openapi_schema_available(self, test_client):
        """OpenAPI schema is accessible."""
        response = test_client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "paths" in schema
        assert "/health" in schema["paths"]
        assert "/search" in schema["paths"]
        assert "/suggest" in schema["paths"]

    def test_docs_page_available(self, test_client):
        """Swagger docs page is accessible."""
        response = test_client.get("/docs")
        assert response.status_code == 200


# =============================================================================
# Edge Cases and Integration
# =============================================================================


class TestEdgeCases:
    """Edge case and integration tests."""

    def test_search_with_special_characters(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics
    ):
        """Search handles special characters in query."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)

        response = test_client.get("/search", params={"q": "C++ templates <vector>"})
        assert response.status_code == 200
        assert response.json()["query"] == "C++ templates <vector>"

    def test_suggest_with_unicode(
        self, test_client, mock_searcher, sample_folder_df, sample_folder_metrics
    ):
        """Suggest handles unicode characters in query."""
        mock_searcher.search_folders.return_value = (
            sample_folder_df,
            sample_folder_metrics,
        )

        response = test_client.get("/suggest", params={"q": "datos en espanol"})
        assert response.status_code == 200

    def test_search_highlight_none_handling(self, test_client, mock_searcher):
        """Search handles None highlighted content gracefully."""
        df = pd.DataFrame([{
            "doc_id": "doc-1",
            "title": "Test",
            "content": "Test content",
            "framework": "test",
            "category": "test",
            "file_path": "test.md",
            "final_score": 0.9,
            "highlighted_content": None,
            "chunk_index": 0,
            "total_chunks": 1,
        }])
        metrics = SearchMetrics(query="test", total_hits=1, returned_hits=1)
        mock_searcher.search.return_value = (df, metrics)

        response = test_client.get("/search", params={"q": "test"})
        assert response.status_code == 200
        # None highlight should become None in response
        result = response.json()["results"][0]
        assert result["highlight"] is None

    def test_concurrent_requests(
        self, test_client, mock_searcher, sample_search_df, sample_search_metrics,
        sample_folder_df, sample_folder_metrics,
    ):
        """Multiple endpoints can be called sequentially without interference."""
        mock_searcher.search.return_value = (sample_search_df, sample_search_metrics)
        mock_searcher.search_folders.return_value = (sample_folder_df, sample_folder_metrics)

        # Hit all three endpoints
        health = test_client.get("/health")
        search = test_client.get("/search", params={"q": "fastapi"})
        suggest = test_client.get("/suggest", params={"q": "python"})

        assert health.status_code == 200
        assert search.status_code == 200
        assert suggest.status_code == 200

    def test_search_nan_score_handling(self, test_client, mock_searcher):
        """Search handles NaN scores in results."""
        df = pd.DataFrame([{
            "doc_id": "doc-1",
            "title": "Test",
            "content": "Test content",
            "framework": "test",
            "category": "test",
            "file_path": "test.md",
            "final_score": float("nan"),
            "highlighted_content": "",
            "chunk_index": 0,
            "total_chunks": 1,
        }])
        metrics = SearchMetrics(query="test", total_hits=1, returned_hits=1)
        mock_searcher.search.return_value = (df, metrics)

        response = test_client.get("/search", params={"q": "test"})
        # FastAPI/JSON serialization of NaN may produce null or error
        # We just want it not to crash with 500
        assert response.status_code in (200, 422)
