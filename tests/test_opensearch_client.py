"""Tests for OpenSearch client module."""

import pytest
from unittest.mock import MagicMock, patch, call
from datetime import datetime, timezone


class TestDocument:
    """Tests for the Document dataclass."""

    def test_document_creation(self):
        """Test basic document creation."""
        from search.opensearch.client import Document

        doc = Document(
            content="Test content",
            title="Test Title",
            path="/test/path.md",
        )

        assert doc.content == "Test content"
        assert doc.title == "Test Title"
        assert doc.path == "/test/path.md"
        assert doc.chunk_index == 0
        assert doc.total_chunks == 1
        assert doc.embedding is None

    def test_document_to_dict(self):
        """Test document serialization to dictionary."""
        from search.opensearch.client import Document

        doc = Document(
            content="Test content",
            title="Test Title",
            path="/test/path.md",
            category="test",
            folder="test_folder",
            file_path="path.md",
            chunk_index=1,
            total_chunks=3,
            content_hash="abc123",
        )

        result = doc.to_dict()

        assert result["content"] == "Test content"
        assert result["title"] == "Test Title"
        assert result["path"] == "/test/path.md"
        assert result["category"] == "test"
        assert result["folder"] == "test_folder"
        assert result["file_path"] == "path.md"
        assert result["chunk_index"] == 1
        assert result["total_chunks"] == 3
        assert result["content_hash"] == "abc123"
        assert "indexed_at" in result
        assert "embedding" not in result  # None embeddings excluded

    def test_document_to_dict_with_embedding(self):
        """Test document serialization includes embedding when present."""
        from search.opensearch.client import Document

        embedding = [0.1, 0.2, 0.3]
        doc = Document(
            content="Test content",
            embedding=embedding,
        )

        result = doc.to_dict()

        assert "embedding" in result
        assert result["embedding"] == embedding


class TestSearchResult:
    """Tests for the SearchResult dataclass."""

    def test_search_result_creation(self):
        """Test search result creation."""
        from search.opensearch.client import SearchResult

        result = SearchResult(
            doc_id="doc123",
            score=0.95,
            content="Test content",
            title="Test Title",
        )

        assert result.doc_id == "doc123"
        assert result.score == 0.95
        assert result.content == "Test content"
        assert result.title == "Test Title"
        assert result.highlight is None


class TestBulkStats:
    """Tests for the BulkStats dataclass."""

    def test_bulk_stats_defaults(self):
        """Test bulk stats default values."""
        from search.opensearch.client import BulkStats

        stats = BulkStats()

        assert stats.success == 0
        assert stats.failed == 0
        assert stats.errors == []
        assert stats.duration_seconds == 0.0


class TestOpenSearchClient:
    """Tests for the OpenSearchClient class."""

    def test_client_initialization(self, mock_opensearch_client):
        """Test client initializes with correct settings."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            client = OpenSearchClient()

            assert client.host == "localhost"
            assert client.port == 9200
            assert client.pool_size > 0
            assert client.timeout > 0

    def test_client_initialization_with_url(self, mock_opensearch_client):
        """Test client can parse URL parameter."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            client = OpenSearchClient(url="http://custom-host:9201")

            assert client.host == "custom-host"
            assert client.port == 9201

    def test_ping_success(self, mock_opensearch_client):
        """Test ping returns True when OpenSearch responds."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.ping.return_value = True

            client = OpenSearchClient()
            assert client.ping() is True

    def test_ping_failure(self, mock_opensearch_client):
        """Test ping returns False when OpenSearch is unavailable."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.ping.side_effect = Exception("Connection refused")

            client = OpenSearchClient()
            assert client.ping() is False

    def test_health_check(self, mock_opensearch_client):
        """Test health check returns cluster health."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            client = OpenSearchClient()
            health = client.health_check()

            assert health["status"] == "green"
            assert health["cluster_name"] == "test-cluster"
            assert health["number_of_nodes"] == 1

    def test_health_check_connection_error(self, mock_opensearch_client):
        """Test health check raises ConnectionError on failure."""
        from search.opensearch.client import OpenSearchClient
        from opensearchpy.exceptions import ConnectionError as OSConnectionError

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            # OSConnectionError expects (status_code, error_message, extra_info)
            mock_opensearch_client.cluster.health.side_effect = OSConnectionError(
                "N/A", "Connection refused", {}
            )

            client = OpenSearchClient()

            with pytest.raises(ConnectionError):
                client.health_check()

    def test_get_cluster_info(self, mock_opensearch_client):
        """Test get_cluster_info returns cluster information."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            client = OpenSearchClient()
            info = client.get_cluster_info()

            assert info["cluster_name"] == "test-cluster"
            assert "version" in info

    def test_index_exists_false(self, mock_opensearch_client):
        """Test index_exists returns False for non-existent index."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = False

            client = OpenSearchClient()
            assert client.index_exists("test_index") is False

    def test_index_exists_true(self, mock_opensearch_client):
        """Test index_exists returns True for existing index."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = True

            client = OpenSearchClient()
            assert client.index_exists("test_index") is True

    def test_create_index(self, mock_opensearch_client):
        """Test create_index creates a new index."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = False

            client = OpenSearchClient()
            result = client.create_index("new_index")

            assert result is True
            mock_opensearch_client.indices.create.assert_called_once()

    def test_create_index_already_exists(self, mock_opensearch_client):
        """Test create_index returns False if index exists."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = True

            client = OpenSearchClient()
            result = client.create_index("existing_index")

            assert result is False
            mock_opensearch_client.indices.create.assert_not_called()

    def test_create_index_recreate(self, mock_opensearch_client):
        """Test create_index with recreate=True deletes existing index."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = True

            client = OpenSearchClient()
            result = client.create_index("existing_index", recreate=True)

            assert result is True
            mock_opensearch_client.indices.delete.assert_called_once()
            mock_opensearch_client.indices.create.assert_called_once()

    def test_delete_index(self, mock_opensearch_client):
        """Test delete_index removes an index."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = True

            client = OpenSearchClient()
            result = client.delete_index("test_index")

            assert result is True
            mock_opensearch_client.indices.delete.assert_called_once()

    def test_delete_index_not_exists(self, mock_opensearch_client):
        """Test delete_index returns False if index doesn't exist."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.indices.exists.return_value = False

            client = OpenSearchClient()
            result = client.delete_index("nonexistent_index")

            assert result is False

    def test_get_document_count(self, mock_opensearch_client):
        """Test get_document_count returns correct count."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.count.return_value = {"count": 500}

            client = OpenSearchClient()
            count = client.get_document_count()

            assert count == 500

    def test_index_document(self, mock_opensearch_client, sample_documents):
        """Test indexing a single document."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.index.return_value = {"_id": "doc123"}

            client = OpenSearchClient()
            doc_id = client.index_document(sample_documents[0])

            assert doc_id == "doc123"
            mock_opensearch_client.index.assert_called_once()

    def test_get_document(self, mock_opensearch_client):
        """Test retrieving a document by ID."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.get.return_value = {
                "_id": "doc123",
                "_source": {"content": "Test content", "title": "Test"},
            }

            client = OpenSearchClient()
            doc = client.get_document("doc123")

            assert doc["content"] == "Test content"
            assert doc["title"] == "Test"

    def test_get_document_not_found(self, mock_opensearch_client):
        """Test get_document returns None for non-existent document."""
        from search.opensearch.client import OpenSearchClient
        from opensearchpy.exceptions import NotFoundError

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.get.side_effect = NotFoundError()

            client = OpenSearchClient()
            doc = client.get_document("nonexistent")

            assert doc is None

    def test_delete_document(self, mock_opensearch_client):
        """Test deleting a document by ID."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.delete.return_value = {"result": "deleted"}

            client = OpenSearchClient()
            result = client.delete_document("doc123")

            assert result is True

    def test_delete_document_not_found(self, mock_opensearch_client):
        """Test delete_document returns False for non-existent document."""
        from search.opensearch.client import OpenSearchClient
        from opensearchpy.exceptions import NotFoundError

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.delete.side_effect = NotFoundError()

            client = OpenSearchClient()
            result = client.delete_document("nonexistent")

            assert result is False

    def test_search(self, mock_opensearch_client):
        """Test text search."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.search.return_value = {
                "hits": {
                    "hits": [
                        {
                            "_id": "doc1",
                            "_score": 0.95,
                            "_source": {
                                "content": "FastAPI web framework",
                                "title": "FastAPI",
                                "folder": "fastapi",
                            },
                            "highlight": {"content": ["<em>FastAPI</em> web framework"]},
                        }
                    ]
                }
            }

            client = OpenSearchClient()
            results = client.search("FastAPI")

            assert len(results) == 1
            assert results[0].doc_id == "doc1"
            assert results[0].score == 0.95
            assert "FastAPI" in results[0].content

    def test_search_with_filters(self, mock_opensearch_client):
        """Test search with filters."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.search.return_value = {"hits": {"hits": []}}

            client = OpenSearchClient()
            client.search("test", filters={"category": "github-scraped"})

            # Verify filter was included in query
            call_args = mock_opensearch_client.search.call_args
            body = call_args.kwargs["body"]
            assert "filter" in body["query"]["bool"]

    def test_neural_search(self, mock_opensearch_client):
        """Test neural (vector) search."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.search.return_value = {
                "hits": {
                    "hits": [
                        {
                            "_id": "doc1",
                            "_score": 0.92,
                            "_source": {
                                "content": "Test content",
                                "title": "Test",
                            },
                        }
                    ]
                }
            }

            client = OpenSearchClient()
            query_vector = [0.1] * 384  # Mock embedding
            results = client.neural_search(query_vector)

            assert len(results) == 1
            assert results[0].score == 0.92

    def test_hybrid_search(self, mock_opensearch_client):
        """Test hybrid search combining text and vector."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.search.return_value = {
                "hits": {
                    "hits": [
                        {
                            "_id": "doc1",
                            "_score": 0.90,
                            "_source": {
                                "content": "Hybrid result",
                                "title": "Hybrid",
                            },
                        }
                    ]
                }
            }

            client = OpenSearchClient()
            query_vector = [0.1] * 384
            results = client.hybrid_search("test query", query_vector)

            assert len(results) == 1

            # Verify query contains both text and knn
            call_args = mock_opensearch_client.search.call_args
            body = call_args.kwargs["body"]
            should = body["query"]["bool"]["should"]
            assert len(should) == 2  # text query and knn query


class TestBulkIndex:
    """Tests for bulk indexing operations."""

    def test_bulk_index_success(self, mock_opensearch_client, sample_documents):
        """Test successful bulk indexing."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            with patch("search.opensearch.client.streaming_bulk") as mock_bulk:
                # Simulate successful indexing
                mock_bulk.return_value = iter([
                    (True, {"index": {"_id": "doc1"}}),
                    (True, {"index": {"_id": "doc2"}}),
                    (True, {"index": {"_id": "doc3"}}),
                ])

                client = OpenSearchClient()
                stats = client.bulk_index(sample_documents, show_progress=False)

                assert stats.success == 3
                assert stats.failed == 0
                assert len(stats.errors) == 0
                assert stats.duration_seconds >= 0

    def test_bulk_index_partial_failure(self, mock_opensearch_client, sample_documents):
        """Test bulk indexing with some failures."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            with patch("search.opensearch.client.streaming_bulk") as mock_bulk:
                # Simulate partial failure
                mock_bulk.return_value = iter([
                    (True, {"index": {"_id": "doc1"}}),
                    (False, {"error": "mapping error"}),
                    (True, {"index": {"_id": "doc3"}}),
                ])

                client = OpenSearchClient()
                stats = client.bulk_index(sample_documents, show_progress=False)

                assert stats.success == 2
                assert stats.failed == 1
                assert len(stats.errors) == 1

    def test_bulk_index_large_set(self, mock_opensearch_client, large_document_set):
        """Test bulk indexing with 1000+ documents."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            with patch("search.opensearch.client.streaming_bulk") as mock_bulk:
                # Simulate successful indexing of all documents
                mock_bulk.return_value = iter([
                    (True, {"index": {"_id": f"doc{i}"}})
                    for i in range(len(large_document_set))
                ])

                client = OpenSearchClient()
                stats = client.bulk_index(large_document_set, show_progress=False)

                assert stats.success == len(large_document_set)
                assert stats.success >= 1000  # QA criteria
                assert stats.failed == 0

    def test_bulk_delete_by_query(self, mock_opensearch_client):
        """Test bulk delete by query."""
        from search.opensearch.client import OpenSearchClient

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client
            mock_opensearch_client.delete_by_query.return_value = {"deleted": 50}

            client = OpenSearchClient()
            deleted = client.bulk_delete_by_query({"match": {"folder": "test"}})

            assert deleted == 50


class TestGlobalClient:
    """Tests for global client instance management."""

    def test_get_client_singleton(self, mock_opensearch_client):
        """Test that get_client returns the same instance."""
        from search.opensearch.client import get_client, reset_client

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            reset_client()  # Clear any existing instance

            client1 = get_client()
            client2 = get_client()

            assert client1 is client2

    def test_reset_client(self, mock_opensearch_client):
        """Test that reset_client clears the global instance."""
        from search.opensearch.client import get_client, reset_client

        with patch("search.opensearch.client.OpenSearch") as mock_os:
            mock_os.return_value = mock_opensearch_client

            client1 = get_client()
            reset_client()
            client2 = get_client()

            assert client1 is not client2
