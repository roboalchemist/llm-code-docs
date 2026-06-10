# LanceDB Search Engine for llm-code-docs

Semantic search engine for the llm-code-docs repository, built with LanceDB and sentence-transformers.

## Features

- **Dual search mode**: Returns both specific markdown documents AND general documentation folders
- **Semantic search**: Uses sentence-transformers embeddings for intelligent matching
- **Hybrid ranking**: Combines semantic similarity, keyword matching, and recency
- **Incremental updates**: Fast updates when documentation changes
- **CLI interface**: Easy-to-use command-line tool

## Installation

### Option 1: Docker (Recommended)

```bash
# Build Docker image
docker build -t llm-docs-search .

# Or use docker-compose
docker-compose build
```

### Option 2: Local Install

```bash
# Install dependencies
pip install -r requirements-search.txt
```

**Note**: On macOS, there may be PyTorch/PyArrow mutex lock issues. Docker is recommended for reliable operation.

## Usage

### Docker Usage (Recommended)

```bash
# Set up alias for convenience
alias llmdocs='docker run --rm -v ~/github/llm-code-docs:/llm-code-docs:ro -v $(pwd)/lancedb:/app/lancedb llm-docs-search'

# Full rebuild (initial indexing, ~30-60 minutes)
llmdocs python search.py index --rebuild

# Incremental update (after doc changes)
llmdocs python search.py index --update

# Index single framework for testing
llmdocs python search.py index --framework click

# Search documentation
llmdocs python search.py search "gitea repo limit 50 change config"

# Limit results
llmdocs python search.py search "fastapi async database" --limit 5

# Show statistics
llmdocs python search.py stats

# List all frameworks
llmdocs python search.py list-frameworks

# Show framework details
llmdocs python search.py framework gitea
```

### Local Usage

```bash
# Full rebuild (initial indexing)
python search.py index --rebuild

# Incremental update (after doc changes)
python search.py index --update

# Index single framework for testing
python search.py index --framework click

# Search documentation
python search.py search "gitea repo limit 50 change config"

# Limit results
python search.py search "fastapi async database" --limit 5

# Show statistics
python search.py stats

# List all frameworks
python search.py list-frameworks

# Show framework details
python search.py framework gitea
```

## Architecture

### Components

- **config.py** - Configuration (paths, model settings)
- **db/** - LanceDB connection and schema management
  - `schema.py` - Table definitions (documents, folders)
  - `connection.py` - Database connection handling
- **embeddings/** - Embedding generation
  - `generator.py` - sentence-transformers wrapper
- **indexer/** - Indexing pipeline
  - `scanner.py` - File tree walker
  - `extractor.py` - Metadata extraction
  - `chunker.py` - Smart document chunking
  - `builder.py` - Main orchestrator
- **searcher/** - Search functionality
  - `query.py` - Dual search (documents + folders)
  - `ranker.py` - Hybrid ranking algorithm
  - `formatter.py` - Result display
- **utils/** - Utilities
  - `yaml_parser.py` - index.yaml parser
  - `hashing.py` - Content hashing for incremental updates
- **cli.py** - Click CLI interface
- **search.py** - Entry point

### Database Schema

**Documents Table** (~21K+ rows):
- Document metadata (path, title, headings, keywords)
- Content chunks with embeddings (384-dim vectors)
- Categorization (framework, category)
- Timestamps for incremental updates

**Folders Table** (~290 rows):
- Framework/tool metadata from index.yaml
- Aggregated content embeddings
- File counts, sizes, descriptions

### Embedding Model

**sentence-transformers/all-MiniLM-L6-v2**:
- 384-dimensional embeddings
- Fast local inference (~0.1ms per sentence)
- No API costs, works offline
- Good semantic understanding for technical docs

### Indexing Performance

- **Full index**: ~30-60 minutes for 21,846 files
- **Incremental update**: 1-5 minutes (only changed files)
- **Search latency**: <100ms per query
- **Storage**: ~500MB (embeddings + content)

## Example Queries

```bash
# Configuration documentation
python search.py search "gitea repository limit configuration"
# Returns: config-cheat-sheet.md + gitea folder

# Framework features
python search.py search "fastapi async database connection"
# Returns: FastAPI DB docs + fastapi folder

# Testing guidance
python search.py search "pytest fixtures"
# Returns: pytest documentation + pytest folder

# General topics
python search.py search "git hosting"
# Returns: gitea, gitlab folders + relevant docs
```

## Troubleshooting

### Known Issues

**macOS PyTorch/PyArrow mutex lock issue:**

If indexing hangs with "[mutex.cc : 452] RAW: Lock blocking" error:

1. Try on Linux (works reliably)
2. Use Docker container
3. Or try these workarounds:

```bash
# Force CPU-only mode
export PYTORCH_ENABLE_MPS_FALLBACK=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

python search.py index --rebuild
```

### Performance Tips

1. **Initial indexing**: Run overnight, model download takes time on first run
2. **Batch size**: Adjust `config.EMBEDDING_BATCH_SIZE` based on RAM
3. **GPU**: CUDA/MPS acceleration automatic if available
4. **Incremental updates**: Much faster than full rebuild

## Development

### Project Structure

```
llm-code-docs-meta/
├── search/               # Search engine package
│   ├── config.py
│   ├── db/
│   ├── embeddings/
│   ├── indexer/
│   ├── searcher/
│   └── utils/
├── search.py             # CLI entry point
├── requirements-search.txt
├── lancedb/              # Database (gitignored)
└── SEARCH_README.md      # This file
```

### Adding Features

1. **Custom ranking**: Modify `search/searcher/ranker.py`
2. **Different embeddings**: Change model in `search/config.py`
3. **Additional metadata**: Update schemas in `search/db/schema.py`
4. **New commands**: Add to `search/cli.py`

## Integration

### With Claude Code Agents

The search engine is designed for Claude Code agent integration:

```python
from search.searcher.query import get_searcher

searcher = get_searcher()
results = searcher.search("gitea config")

for doc in results.documents:
    print(f"- {doc.title} ({doc.path})")

for folder in results.folders:
    print(f"- {folder.framework_name}: {folder.description}")
```

### With Existing Tools

Complements existing llm-code-docs discovery tools:
- `extract_local.py` - Discovers awesome lists
- `crawler.py` - Crawls for new projects
- **search engine** - Finds specific documentation quickly

## Future Enhancements

- [ ] Web UI (FastAPI + React)
- [ ] Advanced filters (by category, date range)
- [ ] Query expansion and synonyms
- [ ] "Find similar" functionality
- [ ] Search analytics
- [ ] GPU optimization for large-scale indexing

## Credits

Built with:
- [LanceDB](https://lancedb.com/) - Vector database
- [sentence-transformers](https://www.sbert.net/) - Embeddings
- [Click](https://click.palletsprojects.com/) - CLI framework
- [tqdm](https://tqdm.github.io/) - Progress bars
