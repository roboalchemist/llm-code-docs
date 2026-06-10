"""Tests for OpenSearch index builder module."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch, call
from dataclasses import dataclass


@dataclass
class MockDocumentInfo:
    """Mock DocumentInfo for testing."""
    path: Path
    category: str
    framework: str
    relative_path: str


class TestOpenSearchIndexBuilder:
    """Tests for the OpenSearchIndexBuilder class."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenSearch client."""
        client = MagicMock()
        client.index_name = "test-index"
        client.index_exists.return_value = True
        client.create_index.return_value = True
        client.get_document_count.return_value = 100
        client.refresh_index.return_value = None
        return client

    @pytest.fixture
    def mock_scanner(self):
        """Create a mock document scanner."""
        scanner = MagicMock()
        scanner.scan.return_value = []
        scanner.scan_framework.return_value = []
        return scanner

    @pytest.fixture
    def mock_chunker(self):
        """Create a mock document chunker."""
        chunker = MagicMock()
        chunker.chunk.return_value = ["chunk1", "chunk2"]
        return chunker

    @pytest.fixture
    def mock_generator(self):
        """Create a mock embedding generator."""
        generator = MagicMock()
        generator.generate.return_value = [[0.1] * 768, [0.2] * 768]
        return generator

    @pytest.fixture
    def builder(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Create a builder with mocked dependencies."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )
        return builder

    def test_builder_initialization(self, builder, mock_client, mock_scanner, mock_chunker):
        """Test builder initializes with correct components."""
        assert builder.client == mock_client
        assert builder.scanner == mock_scanner
        assert builder.chunker == mock_chunker
        assert builder.document_batch_size == 500

    def test_builder_lazy_generator(self, mock_client, mock_scanner, mock_chunker, tmp_path):
        """Test generator is lazily initialized."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            checkpoint_dir=tmp_path,
        )
        # Generator not initialized until accessed
        assert builder._generator is None
        assert builder._generator_initialized is False

    def test_get_stats_no_index(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Test get_stats when index doesn't exist."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        mock_client.index_exists.return_value = False

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )

        stats = builder.get_stats()

        assert stats["exists"] is False
        assert stats["document_count"] == 0

    def test_get_stats_with_index(self, builder, mock_client):
        """Test get_stats when index exists."""
        mock_client.index_exists.return_value = True
        mock_client.get_document_count.return_value = 5000
        mock_client.get_index_stats.return_value = {"size": "100mb"}

        stats = builder.get_stats()

        assert stats["exists"] is True
        assert stats["document_count"] == 5000
        assert stats["index_stats"] == {"size": "100mb"}


class TestFullRebuild:
    """Tests for full_rebuild functionality."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenSearch client."""
        client = MagicMock()
        client.index_name = "test-index"
        client.index_exists.return_value = True
        client.create_index.return_value = True
        client.get_document_count.return_value = 0
        client.refresh_index.return_value = None

        # Mock bulk_index to return proper stats
        bulk_stats = MagicMock()
        bulk_stats.success = 2
        bulk_stats.failed = 0
        bulk_stats.errors = []
        client.bulk_index.return_value = bulk_stats
        return client

    @pytest.fixture
    def mock_scanner(self):
        """Create a mock scanner that returns documents."""
        scanner = MagicMock()
        scanner.scan.return_value = [
            MockDocumentInfo(
                path=Path("/docs/test1.md"),
                category="github-scraped",
                framework="fastapi",
                relative_path="test1.md",
            ),
            MockDocumentInfo(
                path=Path("/docs/test2.md"),
                category="github-scraped",
                framework="fastapi",
                relative_path="test2.md",
            ),
        ]
        return scanner

    @pytest.fixture
    def mock_extractor(self):
        """Create a mock metadata extractor."""
        extractor = MagicMock()
        extractor.extract_metadata.return_value = {
            "title": "Test Title",
            "content": "Test content for document",
            "headings": ["Introduction", "Details"],
            "keywords": [],
        }
        return extractor

    @pytest.fixture
    def mock_chunker(self):
        """Create a mock chunker."""
        chunker = MagicMock()
        chunker.chunk.return_value = ["chunk1"]
        return chunker

    @pytest.fixture
    def mock_generator(self):
        """Create a mock generator."""
        generator = MagicMock()
        generator.generate.return_value = [[0.1] * 768]
        return generator

    @pytest.fixture
    def builder(self, mock_client, mock_scanner, mock_chunker, mock_generator, mock_extractor, tmp_path):
        """Create builder with mocked dependencies."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )
        builder.extractor = mock_extractor
        return builder

    def test_full_rebuild_no_checkpoint_fresh_start(self, builder, mock_client, mock_scanner):
        """Test full rebuild starts fresh when no checkpoint exists."""
        # Run non-interactive
        stats = builder.full_rebuild(resume=False, interactive=False)

        # Should have scanned documents
        mock_scanner.scan.assert_called_once()

        # Should have created index
        mock_client.create_index.assert_called_with(recreate=True)

        # Should have refreshed index
        mock_client.refresh_index.assert_called()

    def test_full_rebuild_indexes_documents(self, builder, mock_client, mock_scanner, mock_generator, mock_chunker):
        """Test full rebuild actually indexes documents."""
        stats = builder.full_rebuild(resume=False, interactive=False)

        # Should have generated embeddings
        mock_generator.generate.assert_called()

        # Should have bulk indexed
        mock_client.bulk_index.assert_called()

        # Stats should reflect processed documents
        assert stats["total_documents"] == 2

    def test_full_rebuild_checkpoint_cleared_on_success(self, builder, tmp_path):
        """Test checkpoint is cleared after successful rebuild."""
        builder.full_rebuild(resume=False, interactive=False)

        # Checkpoint should be cleared
        assert not builder.checkpoint.exists()


class TestIncrementalUpdate:
    """Tests for incremental_update functionality."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenSearch client."""
        client = MagicMock()
        client.index_name = "test-index"
        client.index_exists.return_value = True
        client.get_document_count.return_value = 10

        # Mock scroll API responses for getting existing hashes
        client.client = MagicMock()
        client.client.search.return_value = {
            "_scroll_id": "scroll123",
            "hits": {"hits": []},
        }
        client.client.scroll.return_value = {
            "_scroll_id": "scroll123",
            "hits": {"hits": []},
        }
        client.client.clear_scroll.return_value = None

        bulk_stats = MagicMock()
        bulk_stats.success = 0
        bulk_stats.failed = 0
        bulk_stats.errors = []
        client.bulk_index.return_value = bulk_stats
        client.bulk_delete_by_query.return_value = 0

        return client

    @pytest.fixture
    def mock_scanner(self):
        """Create a mock scanner."""
        scanner = MagicMock()
        scanner.scan.return_value = []
        return scanner

    @pytest.fixture
    def mock_chunker(self):
        """Create a mock chunker."""
        chunker = MagicMock()
        chunker.chunk.return_value = ["chunk1"]
        return chunker

    @pytest.fixture
    def mock_generator(self):
        """Create a mock generator."""
        generator = MagicMock()
        generator.generate.return_value = [[0.1] * 768]
        return generator

    @pytest.fixture
    def builder(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Create builder with mocked dependencies."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )
        return builder

    def test_incremental_update_no_changes(self, builder, mock_client, mock_scanner):
        """Test incremental update when no files have changed."""
        mock_scanner.scan.return_value = []

        stats = builder.incremental_update()

        assert stats["new_files"] == 0
        assert stats["modified_files"] == 0
        assert stats["deleted_files"] == 0

    def test_incremental_update_detects_new_files(self, builder, mock_client, mock_scanner, mock_generator, tmp_path):
        """Test incremental update detects new files."""
        # Create a test file
        test_file = tmp_path / "new_doc.md"
        test_file.write_text("# New Document\n\nTest content")

        mock_scanner.scan.return_value = [
            MockDocumentInfo(
                path=test_file,
                category="github-scraped",
                framework="test",
                relative_path="new_doc.md",
            )
        ]

        # Mock extractor
        builder.extractor = MagicMock()
        builder.extractor.extract_metadata.return_value = {
            "title": "New Document",
            "content": "Test content",
            "headings": [],
            "keywords": [],
        }

        stats = builder.incremental_update()

        assert stats["new_files"] == 1


class TestIndexFramework:
    """Tests for index_framework functionality."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenSearch client."""
        client = MagicMock()
        client.index_name = "test-index"
        client.index_exists.return_value = True
        client.get_document_count.return_value = 10

        bulk_stats = MagicMock()
        bulk_stats.success = 2
        bulk_stats.failed = 0
        bulk_stats.errors = []
        client.bulk_index.return_value = bulk_stats
        client.bulk_delete_by_query.return_value = 5

        return client

    @pytest.fixture
    def mock_scanner(self):
        """Create a mock scanner."""
        scanner = MagicMock()
        scanner.scan_framework.return_value = [
            MockDocumentInfo(
                path=Path("/docs/fastapi/intro.md"),
                category="github-scraped",
                framework="fastapi",
                relative_path="intro.md",
            ),
        ]
        return scanner

    @pytest.fixture
    def mock_chunker(self):
        """Create a mock chunker."""
        chunker = MagicMock()
        chunker.chunk.return_value = ["chunk1"]
        return chunker

    @pytest.fixture
    def mock_generator(self):
        """Create a mock generator."""
        generator = MagicMock()
        generator.generate.return_value = [[0.1] * 768]
        return generator

    @pytest.fixture
    def builder(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Create builder with mocked dependencies."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )
        builder.extractor = MagicMock()
        builder.extractor.extract_metadata.return_value = {
            "title": "FastAPI Intro",
            "content": "FastAPI content",
            "headings": [],
            "keywords": [],
        }
        return builder

    def test_index_framework_no_documents(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Test index_framework when no documents found."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        mock_scanner.scan_framework.return_value = []

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )

        stats = builder.index_framework("nonexistent")

        assert stats["chunks"] == 0
        assert stats["documents"] == 0

    def test_index_framework_deletes_existing(self, builder, mock_client, mock_scanner):
        """Test index_framework deletes existing documents first."""
        builder.index_framework("fastapi")

        # Should have called scan_framework
        mock_scanner.scan_framework.assert_called_with("fastapi")

        # Should have deleted existing documents for this framework
        mock_client.bulk_delete_by_query.assert_called_with({"term": {"folder": "fastapi"}})

    def test_index_framework_indexes_documents(self, builder, mock_client, mock_generator):
        """Test index_framework indexes the scanned documents."""
        stats = builder.index_framework("fastapi")

        # Should have generated embeddings
        mock_generator.generate.assert_called()

        # Should have bulk indexed
        mock_client.bulk_index.assert_called()

        # Should have refreshed index
        mock_client.refresh_index.assert_called()

        assert stats["documents"] == 1


class TestGlobalBuilder:
    """Tests for global builder instance management."""

    def test_get_builder_singleton(self):
        """Test get_builder returns singleton instance."""
        from search.opensearch.builder import get_builder, reset_builder

        reset_builder()

        with patch("search.opensearch.builder.OpenSearchIndexBuilder") as MockBuilder:
            builder1 = get_builder()
            builder2 = get_builder()

            # Should be called only once
            MockBuilder.assert_called_once()

        reset_builder()

    def test_reset_builder_clears_singleton(self):
        """Test reset_builder clears the singleton."""
        from search.opensearch.builder import get_builder, reset_builder, _builder

        reset_builder()

        with patch("search.opensearch.builder.OpenSearchIndexBuilder") as MockBuilder:
            MockBuilder.return_value = MagicMock()

            builder1 = get_builder()
            reset_builder()
            builder2 = get_builder()

            # Should be called twice after reset
            assert MockBuilder.call_count == 2

        reset_builder()


class TestDocumentChunking:
    """Tests for document chunking in the builder."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenSearch client."""
        client = MagicMock()
        client.index_name = "test-index"
        return client

    @pytest.fixture
    def mock_scanner(self):
        """Create a mock scanner."""
        return MagicMock()

    @pytest.fixture
    def mock_chunker(self):
        """Create a mock chunker that returns multiple chunks."""
        chunker = MagicMock()
        chunker.chunk.return_value = ["chunk1", "chunk2", "chunk3"]
        return chunker

    @pytest.fixture
    def mock_generator(self):
        """Create a mock generator."""
        generator = MagicMock()
        generator.generate.return_value = [[0.1] * 768, [0.2] * 768, [0.3] * 768]
        return generator

    @pytest.fixture
    def builder(self, mock_client, mock_scanner, mock_chunker, mock_generator, tmp_path):
        """Create builder with mocked dependencies."""
        from search.opensearch.builder import OpenSearchIndexBuilder

        builder = OpenSearchIndexBuilder(
            client=mock_client,
            scanner=mock_scanner,
            chunker=mock_chunker,
            generator=mock_generator,
            checkpoint_dir=tmp_path,
        )
        builder.extractor = MagicMock()
        builder.extractor.extract_metadata.return_value = {
            "title": "Test Doc",
            "content": "Test content",
            "headings": ["H1"],
            "keywords": [],
        }
        return builder

    def test_prepare_document_chunks_creates_multiple_chunks(self, builder, tmp_path):
        """Test that large documents are split into multiple chunks."""
        doc_info = MockDocumentInfo(
            path=tmp_path / "test.md",
            category="github-scraped",
            framework="test",
            relative_path="test.md",
        )

        docs, texts = builder._prepare_document_chunks(doc_info)

        assert len(docs) == 3  # Matches chunker output
        assert len(texts) == 3

        # Check chunk indices
        assert docs[0].chunk_index == 0
        assert docs[1].chunk_index == 1
        assert docs[2].chunk_index == 2

        # Check total_chunks set correctly
        for doc in docs:
            assert doc.total_chunks == 3
