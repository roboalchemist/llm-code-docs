"""Integration tests for OpenSearch client.

These tests require a running OpenSearch instance at localhost:9200.
Run with: pytest tests/test_opensearch_integration.py -v

To start OpenSearch: ./scripts/start_opensearch.sh
"""

import os
import pytest
import time

# Skip all tests if OpenSearch is not available
pytestmark = pytest.mark.skipif(
    os.environ.get("RUN_INTEGRATION_TESTS", "").lower() != "true",
    reason="Integration tests require RUN_INTEGRATION_TESTS=true and a running OpenSearch instance"
)


@pytest.fixture(scope="module")
def opensearch_client():
    """Create a real OpenSearch client for integration tests."""
    from search.opensearch.client import OpenSearchClient, reset_client

    reset_client()
    client = OpenSearchClient()

    # Verify connection
    if not client.ping():
        pytest.skip("OpenSearch is not available at localhost:9200")

    yield client

    # Cleanup - delete test index if it exists
    try:
        client.delete_index("test_integration_index")
    except Exception:
        pass

    reset_client()


@pytest.fixture(scope="module")
def test_index_name():
    """Return the test index name."""
    return "test_integration_index"


class TestIntegrationConnection:
    """Integration tests for OpenSearch connection."""

    def test_ping(self, opensearch_client):
        """Test that we can ping OpenSearch."""
        assert opensearch_client.ping() is True

    def test_health_check(self, opensearch_client):
        """Test cluster health check."""
        health = opensearch_client.health_check()

        assert "status" in health
        assert health["status"] in ["green", "yellow", "red"]
        assert "cluster_name" in health

    def test_cluster_info(self, opensearch_client):
        """Test getting cluster info."""
        info = opensearch_client.get_cluster_info()

        assert "name" in info
        assert "version" in info
        assert "number" in info["version"]

    def test_ml_stats(self, opensearch_client):
        """Test ML Commons stats endpoint."""
        try:
            stats = opensearch_client.get_ml_stats()
            assert "ml_node_count" in stats or "nodes" in stats
        except Exception as e:
            # ML Commons may not be fully available
            pytest.skip(f"ML Commons not available: {e}")


class TestIntegrationIndexManagement:
    """Integration tests for index management."""

    def test_create_and_delete_index(self, opensearch_client, test_index_name):
        """Test creating and deleting an index."""
        # Ensure index doesn't exist
        if opensearch_client.index_exists(test_index_name):
            opensearch_client.delete_index(test_index_name)

        # Create index
        result = opensearch_client.create_index(test_index_name)
        assert result is True
        assert opensearch_client.index_exists(test_index_name)

        # Verify settings
        stats = opensearch_client.get_index_stats(test_index_name)
        assert test_index_name in stats["indices"]

        # Delete index
        result = opensearch_client.delete_index(test_index_name)
        assert result is True
        assert not opensearch_client.index_exists(test_index_name)

    def test_recreate_index(self, opensearch_client, test_index_name):
        """Test recreating an existing index."""
        # Create initial index
        opensearch_client.create_index(test_index_name)
        assert opensearch_client.index_exists(test_index_name)

        # Recreate should succeed
        result = opensearch_client.create_index(test_index_name, recreate=True)
        assert result is True

        # Cleanup
        opensearch_client.delete_index(test_index_name)


class TestIntegrationDocumentOperations:
    """Integration tests for document operations."""

    @pytest.fixture(autouse=True)
    def setup_index(self, opensearch_client, test_index_name):
        """Setup test index before each test."""
        opensearch_client.create_index(test_index_name, recreate=True)
        yield
        opensearch_client.delete_index(test_index_name)

    def test_index_and_get_document(self, opensearch_client, test_index_name):
        """Test indexing and retrieving a document."""
        from search.opensearch.client import Document

        doc = Document(
            content="FastAPI is a modern web framework for Python.",
            title="FastAPI Introduction",
            folder="fastapi",
            doc_id="test-doc-1",
        )

        # Index document
        doc_id = opensearch_client.index_document(doc, index_name=test_index_name)
        assert doc_id == "test-doc-1"

        # Refresh to make document searchable
        opensearch_client.refresh_index(test_index_name)

        # Retrieve document
        retrieved = opensearch_client.get_document("test-doc-1", index_name=test_index_name)
        assert retrieved is not None
        assert retrieved["content"] == doc.content
        assert retrieved["title"] == doc.title

    def test_delete_document(self, opensearch_client, test_index_name):
        """Test deleting a document."""
        from search.opensearch.client import Document

        doc = Document(content="Test content", doc_id="delete-me")
        opensearch_client.index_document(doc, index_name=test_index_name)
        opensearch_client.refresh_index(test_index_name)

        # Delete
        result = opensearch_client.delete_document("delete-me", index_name=test_index_name)
        assert result is True

        # Verify deleted
        retrieved = opensearch_client.get_document("delete-me", index_name=test_index_name)
        assert retrieved is None


class TestIntegrationBulkOperations:
    """Integration tests for bulk operations."""

    @pytest.fixture(autouse=True)
    def setup_index(self, opensearch_client, test_index_name):
        """Setup test index before each test."""
        opensearch_client.create_index(test_index_name, recreate=True)
        yield
        opensearch_client.delete_index(test_index_name)

    def test_bulk_index_small_batch(self, opensearch_client, test_index_name):
        """Test bulk indexing a small batch of documents."""
        from search.opensearch.client import Document

        docs = [
            Document(
                content=f"Document {i} content",
                title=f"Doc {i}",
                folder="test",
            )
            for i in range(10)
        ]

        stats = opensearch_client.bulk_index(
            docs,
            index_name=test_index_name,
            show_progress=False,
        )

        assert stats.success == 10
        assert stats.failed == 0

        # Verify count
        opensearch_client.refresh_index(test_index_name)
        count = opensearch_client.get_document_count(test_index_name)
        assert count == 10

    def test_bulk_index_large_batch(self, opensearch_client, test_index_name):
        """Test bulk indexing 1000+ documents (QA criteria)."""
        from search.opensearch.client import Document

        docs = [
            Document(
                content=f"Document {i} with content for bulk testing",
                title=f"Bulk Doc {i}",
                folder="bulk-test",
            )
            for i in range(1100)  # More than 1000
        ]

        stats = opensearch_client.bulk_index(
            docs,
            index_name=test_index_name,
            chunk_size=200,
            show_progress=False,
        )

        assert stats.success == 1100
        assert stats.failed == 0
        assert stats.success >= 1000  # QA criteria

        # Verify count
        opensearch_client.refresh_index(test_index_name)
        count = opensearch_client.get_document_count(test_index_name)
        assert count == 1100

    def test_bulk_delete_by_query(self, opensearch_client, test_index_name):
        """Test bulk delete by query."""
        from search.opensearch.client import Document

        # Index some documents
        docs = [
            Document(content="Keep this", folder="keep"),
            Document(content="Delete this 1", folder="delete"),
            Document(content="Delete this 2", folder="delete"),
            Document(content="Keep this too", folder="keep"),
        ]
        opensearch_client.bulk_index(docs, index_name=test_index_name, show_progress=False)
        opensearch_client.refresh_index(test_index_name)

        # Delete by query
        deleted = opensearch_client.bulk_delete_by_query(
            {"match": {"folder": "delete"}},
            index_name=test_index_name,
        )

        assert deleted == 2

        # Verify remaining
        opensearch_client.refresh_index(test_index_name)
        count = opensearch_client.get_document_count(test_index_name)
        assert count == 2


class TestIntegrationSearch:
    """Integration tests for search operations."""

    @pytest.fixture(autouse=True)
    def setup_searchable_index(self, opensearch_client, test_index_name):
        """Setup index with searchable documents."""
        from search.opensearch.client import Document

        opensearch_client.create_index(test_index_name, recreate=True)

        docs = [
            Document(
                content="FastAPI is a modern, fast web framework for building APIs with Python.",
                title="FastAPI Introduction",
                folder="fastapi",
                category="github-scraped",
            ),
            Document(
                content="Pytest is a testing framework that makes it easy to write tests.",
                title="Pytest Overview",
                folder="pytest",
                category="github-scraped",
            ),
            Document(
                content="OpenSearch is a distributed search and analytics engine.",
                title="OpenSearch Guide",
                folder="opensearch",
                category="web-scraped",
            ),
        ]

        opensearch_client.bulk_index(docs, index_name=test_index_name, show_progress=False)
        opensearch_client.refresh_index(test_index_name)

        yield

        opensearch_client.delete_index(test_index_name)

    def test_text_search(self, opensearch_client, test_index_name):
        """Test basic text search."""
        results = opensearch_client.search(
            "FastAPI web framework",
            index_name=test_index_name,
            min_score=0.1,
        )

        assert len(results) >= 1
        assert results[0].folder == "fastapi"
        assert "FastAPI" in results[0].content

    def test_search_with_filter(self, opensearch_client, test_index_name):
        """Test search with category filter."""
        results = opensearch_client.search(
            "search",
            index_name=test_index_name,
            filters={"category": "web-scraped"},
            min_score=0.1,
        )

        # Should only return OpenSearch doc (web-scraped category)
        for result in results:
            assert result.category == "web-scraped"

    def test_search_no_results(self, opensearch_client, test_index_name):
        """Test search with no matching results."""
        results = opensearch_client.search(
            "nonexistent query that matches nothing xyz123",
            index_name=test_index_name,
            min_score=0.5,
        )

        assert len(results) == 0
