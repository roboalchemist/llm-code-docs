"""Pytest configuration and fixtures for OpenSearch tests."""

import os
import pytest
from unittest.mock import MagicMock, patch

# Set test environment variables before importing config
os.environ.setdefault("OPENSEARCH_HOST", "localhost")
os.environ.setdefault("OPENSEARCH_PORT", "9200")
os.environ.setdefault("OPENSEARCH_INDEX_NAME", "test_llm_docs")
os.environ.setdefault("OPENSEARCH_PIPELINE_NAME", "test_pipeline")


@pytest.fixture
def mock_opensearch_client():
    """Create a mock OpenSearch client for unit testing."""
    with patch("opensearchpy.OpenSearch") as mock_class:
        mock_instance = MagicMock()
        mock_class.return_value = mock_instance

        # Setup common mock responses
        mock_instance.ping.return_value = True
        mock_instance.cluster.health.return_value = {
            "cluster_name": "test-cluster",
            "status": "green",
            "number_of_nodes": 1,
            "active_primary_shards": 5,
            "active_shards": 5,
        }
        mock_instance.info.return_value = {
            "name": "test-node",
            "cluster_name": "test-cluster",
            "version": {"number": "2.17.1"},
        }
        mock_instance.indices.exists.return_value = False
        mock_instance.indices.create.return_value = {"acknowledged": True}
        mock_instance.indices.delete.return_value = {"acknowledged": True}
        mock_instance.indices.stats.return_value = {"_all": {"total": {"docs": {"count": 100}}}}
        mock_instance.count.return_value = {"count": 100}
        mock_instance.ingest.get_pipeline.side_effect = Exception("Not found")
        mock_instance.ingest.put_pipeline.return_value = {"acknowledged": True}

        yield mock_instance


@pytest.fixture
def sample_documents():
    """Create sample documents for testing."""
    from search.opensearch.client import Document

    return [
        Document(
            content="FastAPI is a modern, fast web framework for building APIs with Python.",
            title="FastAPI Introduction",
            path="/docs/fastapi/intro.md",
            category="github-scraped",
            folder="fastapi",
            file_path="intro.md",
            chunk_index=0,
            total_chunks=1,
            content_hash="abc123",
        ),
        Document(
            content="Pytest is a testing framework that makes it easy to write small tests.",
            title="Pytest Overview",
            path="/docs/pytest/overview.md",
            category="github-scraped",
            folder="pytest",
            file_path="overview.md",
            chunk_index=0,
            total_chunks=1,
            content_hash="def456",
        ),
        Document(
            content="OpenSearch is a distributed search and analytics engine.",
            title="OpenSearch Guide",
            path="/docs/opensearch/guide.md",
            category="web-scraped",
            folder="opensearch",
            file_path="guide.md",
            chunk_index=0,
            total_chunks=1,
            content_hash="ghi789",
        ),
    ]


@pytest.fixture
def large_document_set():
    """Create a large set of documents for bulk testing."""
    from search.opensearch.client import Document

    return [
        Document(
            content=f"Document number {i} with some test content for bulk indexing.",
            title=f"Test Doc {i}",
            path=f"/docs/test/doc{i}.md",
            category="test",
            folder="test",
            file_path=f"doc{i}.md",
            chunk_index=0,
            total_chunks=1,
            content_hash=f"hash{i}",
        )
        for i in range(1500)  # More than 1000 to test bulk handling
    ]
