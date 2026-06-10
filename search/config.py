"""Configuration for LanceDB Search Engine."""

from pathlib import Path
import os

# Base directories
PROJECT_ROOT = Path(__file__).parent.parent
LANCEDB_DIR = PROJECT_ROOT / "lancedb"

# Support Docker environment (repo mounted at /llm-code-docs)
# Check at import time for Docker paths
_docker_docs = Path("/llm-code-docs/docs")
_docker_index = Path("/llm-code-docs/index.yaml")

if _docker_docs.exists() and _docker_index.exists():
    DOCS_ROOT = _docker_docs
    INDEX_YAML = _docker_index
else:
    DOCS_ROOT = Path.home() / "github" / "llm-code-docs" / "docs"
    INDEX_YAML = Path.home() / "github" / "llm-code-docs" / "index.yaml"

# Ensure directories exist
LANCEDB_DIR.mkdir(exist_ok=True)

# Embedding model configuration
EMBEDDING_MODEL = "small"  # qwen3-embeddings-mlx model
EMBEDDING_DIMENSION = 1024  # Small model (0.6B) uses 1024d
EMBEDDING_BATCH_SIZE = 128

# GPU Server Configuration
# Set USE_GPU_CLUSTER=True to use multi-GPU chungus2 servers (6.2x faster)
USE_GPU_CLUSTER = os.environ.get("USE_GPU_CLUSTER", "false").lower() == "true"

if USE_GPU_CLUSTER:
    # 2x RTX 3090 cluster on chungus2 (M40s excluded due to OOM)
    GPU_SERVERS = [
        "http://chungus2:10001",  # RTX 3090 #0
        "http://chungus2:10002",  # RTX 3090 #1
    ]
else:
    # Single local MLX server
    EMBEDDING_API_URL = "http://localhost:10001"

# LanceDB index configuration
DOCUMENTS_INDEX_CONFIG = {
    "metric": "cosine",
    "index_type": "IVF_PQ",
    "num_partitions": 256,
    "num_sub_vectors": 64,  # 1024/16, must divide embedding dimension
}

FOLDERS_INDEX_CONFIG = {
    "metric": "cosine",
    "index_type": "FLAT",  # Small table, use exact search
}

# Chunking configuration
MAX_CHUNK_TOKENS = 1000  # Target ~750-1000 tokens per chunk
MIN_CHUNK_TOKENS = 100   # Minimum viable chunk size
CHUNK_OVERLAP_TOKENS = 50  # Overlap between chunks

# Search configuration
DEFAULT_SEARCH_LIMIT = 10
DEFAULT_FOLDER_LIMIT = 5

# Hybrid ranking weights
RANKING_WEIGHTS = {
    "semantic": 0.7,
    "keyword": 0.2,
    "recency": 0.1,
}

# Categories
CATEGORIES = ["llms-txt", "github-scraped", "web-scraped"]
