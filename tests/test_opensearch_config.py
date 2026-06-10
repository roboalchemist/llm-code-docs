"""Tests for OpenSearch configuration module."""

import os
import pytest


class TestOpenSearchConfig:
    """Tests for search.opensearch.config module."""

    def test_default_connection_settings(self):
        """Test that default connection settings are correct."""
        from search.opensearch import config

        assert config.OPENSEARCH_HOST == "localhost"
        assert config.OPENSEARCH_PORT == 9200
        assert "localhost" in config.OPENSEARCH_URL
        assert "9200" in config.OPENSEARCH_URL

    def test_connection_pool_settings(self):
        """Test connection pool default settings."""
        from search.opensearch import config

        assert config.CONNECTION_POOL_SIZE >= 1
        assert config.CONNECTION_TIMEOUT > 0
        assert config.MAX_RETRIES >= 1
        assert config.RETRY_ON_TIMEOUT is True

    def test_bulk_operation_settings(self):
        """Test bulk operation default settings."""
        from search.opensearch import config

        assert config.BULK_CHUNK_SIZE > 0
        assert config.BULK_MAX_RETRIES >= 1
        assert config.BULK_INITIAL_BACKOFF > 0
        assert config.BULK_MAX_BACKOFF > config.BULK_INITIAL_BACKOFF

    def test_index_settings(self):
        """Test index configuration."""
        from search.opensearch import config

        assert config.INDEX_NAME is not None
        assert len(config.INDEX_NAME) > 0
        assert config.INDEX_SETTINGS["number_of_shards"] >= 1
        assert config.INDEX_SETTINGS["knn"] is True

    def test_embedding_settings(self):
        """Test embedding/ML configuration."""
        from search.opensearch import config

        assert config.EMBEDDING_DIMENSION > 0
        assert config.KNN_ENGINE in ["lucene", "nmslib", "faiss"]
        assert config.KNN_SPACE_TYPE in ["l2", "cosinesimil", "innerproduct"]
        assert config.KNN_EF_CONSTRUCTION > 0
        assert config.KNN_M > 0

    def test_search_settings(self):
        """Test search configuration."""
        from search.opensearch import config

        assert config.DEFAULT_SEARCH_SIZE > 0
        assert config.DEFAULT_MIN_SCORE >= 0
        assert config.NEURAL_SEARCH_K > 0

    def test_get_index_mappings(self):
        """Test that index mappings are properly structured."""
        from search.opensearch import config

        mappings = config.get_index_mappings()

        assert "properties" in mappings
        props = mappings["properties"]

        # Check required fields
        assert "content" in props
        assert props["content"]["type"] == "text"

        assert "title" in props
        assert props["title"]["type"] == "text"

        assert "path" in props
        assert props["path"]["type"] == "keyword"

        assert "category" in props
        assert props["category"]["type"] == "keyword"

        assert "folder" in props
        assert props["folder"]["type"] == "keyword"

        assert "embedding" in props
        assert props["embedding"]["type"] == "knn_vector"
        assert props["embedding"]["dimension"] == config.EMBEDDING_DIMENSION

    def test_get_pipeline_config_without_model_id(self):
        """Test that pipeline config raises error without MODEL_ID."""
        from search.opensearch import config

        # Save original value
        original_model_id = config.MODEL_ID

        try:
            # Clear MODEL_ID
            config.MODEL_ID = ""

            with pytest.raises(ValueError) as exc_info:
                config.get_pipeline_config()

            assert "MODEL_ID is not set" in str(exc_info.value)
        finally:
            # Restore original value
            config.MODEL_ID = original_model_id

    def test_get_pipeline_config_with_model_id(self):
        """Test that pipeline config works with MODEL_ID set."""
        from search.opensearch import config

        # Save original value
        original_model_id = config.MODEL_ID

        try:
            # Set a test MODEL_ID
            config.MODEL_ID = "test-model-id"

            pipeline = config.get_pipeline_config()

            assert "description" in pipeline
            assert "processors" in pipeline
            assert len(pipeline["processors"]) > 0

            processor = pipeline["processors"][0]
            assert "text_embedding" in processor
            assert processor["text_embedding"]["model_id"] == "test-model-id"
        finally:
            # Restore original value
            config.MODEL_ID = original_model_id

    def test_environment_variable_override(self, monkeypatch):
        """Test that environment variables override defaults."""
        # Set environment variables
        monkeypatch.setenv("OPENSEARCH_HOST", "custom-host")
        monkeypatch.setenv("OPENSEARCH_PORT", "9201")
        monkeypatch.setenv("OPENSEARCH_INDEX_NAME", "custom_index")

        # Force reimport to pick up new env vars
        import importlib
        from search.opensearch import config
        importlib.reload(config)

        assert config.OPENSEARCH_HOST == "custom-host"
        assert config.OPENSEARCH_PORT == 9201
        assert config.INDEX_NAME == "custom_index"

        # Reload again to restore defaults for other tests
        monkeypatch.delenv("OPENSEARCH_HOST", raising=False)
        monkeypatch.delenv("OPENSEARCH_PORT", raising=False)
        monkeypatch.delenv("OPENSEARCH_INDEX_NAME", raising=False)
        importlib.reload(config)
