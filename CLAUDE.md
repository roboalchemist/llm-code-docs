# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

**This is the "librarian" repo - an assistant for [llm-code-docs](~/github/llm-code-docs).**

- **llm-code-docs** (public, GitHub): AI-readable documentation store (245+ frameworks/tools)
- **librarian** (private, Gitea): Discovery, search indexing, format conversion, and automation for managing documentation

Core responsibilities:
1. **Discovery** - Crawl GitHub "awesome lists" to find projects needing documentation
2. **Search** - LanceDB-based semantic search over llm-code-docs
3. **Conversion** - Transform HTML/RFC/SiYuan to clean Markdown
4. **Automation** - Process documentation queues with parallel workers

## Commands

### Discovery (awesome list crawling)

```bash
# Local extraction (fast, preferred) - from cloned seed repos
python3 extract_local.py

# Remote crawling (slower, for discovering new lists)
python3 crawler.py --max-depth 1 --delay 0.3
```

### Search Engine

```bash
# Search documentation
python -m search.cli search "how to use FastAPI middleware"
python -m search.cli search "authentication" --framework django --limit 5

# Build/rebuild index (requires TEI servers running)
USE_GPU_CLUSTER=true python -m search.cli index --rebuild  # Full rebuild
USE_GPU_CLUSTER=true python -m search.cli index --update   # Incremental

# Index statistics and exploration
python -m search.cli stats --verbose
python -m search.cli list-frameworks
python -m search.cli framework fastapi
python -m search.cli show docs/llms-txt/fastapi/llms.txt
```

### Format Conversion

```bash
# HTML/MDX to Markdown (requires ReaderLM server)
python scripts/html_to_markdown.py input.html output.md
python scripts/html_to_markdown.py input.md --inplace

# RFC txt to Markdown
python rfcs/rfc_to_markdown.py rfc793.txt rfc793.md

# SiYuan .sy to Markdown
python tools/siyuan_to_md.py input.sy output.md
python tools/siyuan_to_md.py ./siyuan-data/ ./output-md/  # Directory mode
```

### Automation

```bash
# Process doc-add tickets in a loop (integrates with trckr)
python scripts/docs-loop.py --workers 2 --limit 10

# Process docs queue from CSV
python scripts/process-docs-queue.py --workers 2 --dry-run
```

## Architecture

```
├── extract_local.py       # Fast extraction from local clones
├── crawler.py             # Recursive GitHub crawler with rate limiting
├── search/                # LanceDB semantic search engine
│   ├── cli.py             # Click CLI interface
│   ├── config.py          # LanceDB and embedding config
│   ├── opensearch/
│   │   ├── config.py          # OpenSearch connection settings
│   │   ├── client.py          # OpenSearchClient wrapper
│   │   ├── searcher.py        # HybridSearcher (BM25+SPLADE+dense)
│   │   └── builder.py         # Index builder for documents/folders
│   ├── watcher/
│   │   ├── daemon.py          # DocsWatcher with watchdog
│   │   └── indexer.py         # ChangeQueue and ChangeProcessor
│   ├── embeddings/        # TEI GPU embedding generation
│   ├── indexer/           # Document scanning, chunking, building
│   ├── searcher/          # Query processing, ranking, formatting
│   └── db/                # LanceDB connection and schemas
├── opensearch/            # OpenSearch setup and configuration
│   ├── create_indices.py      # Index creation script
│   ├── create_indices.sh      # Wrapper script
│   ├── mappings/              # Index mapping JSONs (documents, folders)
│   ├── pipelines/             # Search/ingest pipeline configs
│   └── scripts/               # SPLADE model registration
├── scripts/
│   ├── html_to_markdown.py    # ReaderLM-based HTML conversion
│   ├── docs-loop.py           # Automated doc-add ticket processor
│   ├── process-docs-queue.py  # CSV queue processor with worktrees
│   ├── start_opensearch.sh    # Start OpenSearch server
│   ├── start_tei.sh           # Start TEI embedding servers
│   ├── start_readerlm.sh      # Start ReaderLM conversion server
│   ├── start_watcher.sh       # Start file watcher daemon
│   └── stop_*.sh              # Stop scripts for services
├── api/
│   └── main.py                # FastAPI app with /health, /search, /suggest
├── hooks/
│   └── librarian.sh           # Claude Code UserPromptSubmit hook
├── tools/
│   └── siyuan_to_md.py    # SiYuan JSON to Markdown converter
├── rfcs/
│   └── rfc_to_markdown.py # RFC txt to Markdown converter
├── tests/                 # Comprehensive test suite
│   ├── test_opensearch_*.py   # OpenSearch unit/integration tests
│   ├── test_api.py            # REST API tests
│   ├── test_cli.py            # CLI tests
│   ├── test_watcher.py        # File watcher tests
│   └── test_e2e_validation.py # End-to-end validation
└── output/                # Generated results (tracked)
```

## GPU Services

All GPU services run on chungus2. **GPU 3 and 5 are RTX 3090s (24GB each).**

### TEI Embedding Server (Qwen3-Embedding-0.6B)

```bash
./scripts/start_tei.sh   # Ports 10001 (GPU 3), 10002 (GPU 5)
./scripts/stop_tei.sh
```
**Performance:** ~475 texts/sec total, 1.5GB VRAM per GPU

### ReaderLM-v2 Server (HTML to Markdown)

```bash
./scripts/start_readerlm.sh  # Port 10010 (GPU 3)
./scripts/stop_readerlm.sh
```
**Note:** Shares GPU 3 with TEI. ~4GB VRAM.

## Search & Embeddings

**Backend: OpenSearch** with hybrid BM25 + SPLADE + dense vector retrieval (migrated from LanceDB).

### OpenSearch Server

OpenSearch 2.17+ with ML Commons and neural search plugins.

```bash
# Start OpenSearch (port 9200)
./scripts/start_opensearch.sh

# Stop OpenSearch
./scripts/stop_opensearch.sh
```

### Hybrid Search Architecture

The search system combines three retrieval methods for optimal results:

1. **BM25**: Traditional keyword matching using TF-IDF scoring
2. **SPLADE**: Neural sparse encoding for semantic expansion (e.g., "auth" → "authentication", "OAuth", "login")
3. **Dense Vectors**: K-NN search on embeddings for semantic similarity

Results are normalized and combined using OpenSearch's search pipeline with configurable weights:
- BM25: 0.3, SPLADE: 0.4, Dense: 0.3

### CLI Usage

```bash
# Search with OpenSearch backend (default)
python -m search.cli search "how to use FastAPI middleware"

# Search with verbose SPLADE info
python -m search.cli search "authentication" --verbose

# Search with scoring breakdown
python -m search.cli search "database ORM" --explain

# Use legacy LanceDB backend
python -m search.cli search "query" --backend lancedb
```

### REST API

Start the API server:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8080
```

Endpoints:
- `GET /health` - Service health including OpenSearch status
- `GET /search?q=...` - Full hybrid search (<200ms latency)
- `GET /suggest?q=...` - Fast framework suggestions (<50ms latency)

### File Watcher Daemon

Monitors llm-code-docs for changes and triggers incremental indexing:

```bash
# Start watcher daemon
./scripts/start_watcher.sh

# Or run directly
python -m search.watcher.daemon --debounce 5 --log-level INFO
```

Features:
- Watches `docs/{llms-txt,github-scraped,web-scraped}/**/*.md`
- 5-second debounce for rapid changes
- Survives OpenSearch restarts (auto-reconnect)
- Graceful shutdown on SIGINT/SIGTERM

### Claude Code Integration

Hook for automatic documentation suggestions in Claude Code:

1. Copy hook script to Claude Code config:
   ```bash
   cp hooks/librarian.sh ~/.claude/hooks/
   ```

2. Add to Claude Code hooks config (`~/.claude/hooks.json`):
   ```json
   {
     "UserPromptSubmit": ["~/.claude/hooks/librarian.sh"]
   }
   ```

3. Configure (optional environment variables):
   ```bash
   export LIBRARIAN_URL="http://localhost:8080"
   export LIBRARIAN_TIMEOUT_MS="50"
   export LIBRARIAN_LIMIT="3"
   ```

### Running Tests

```bash
# Unit tests (no OpenSearch required)
pytest tests/ -v --ignore=tests/test_e2e_validation.py --ignore=tests/test_opensearch_integration.py

# Integration tests (requires running OpenSearch)
RUN_INTEGRATION_TESTS=true pytest tests/test_opensearch_integration.py -v

# End-to-end validation (requires running OpenSearch with indexed data)
RUN_E2E_TESTS=true pytest tests/test_e2e_validation.py -v
```

### Performance Targets

| Operation | Target | Measured |
|-----------|--------|----------|
| Suggest (folders) | <50ms | ~15-30ms |
| Search (documents) | <200ms | ~50-100ms |
| Bulk indexing | >100 docs/sec | ~200 docs/sec |

## Search Engine Details (LanceDB Legacy)

LanceDB-based semantic search with hybrid ranking (semantic 70%, keyword 20%, recency 10%).

**Key configuration** (`search/config.py`):
- `USE_GPU_CLUSTER=true` - Use multi-GPU TEI servers (required for indexing)
- `EMBEDDING_DIMENSION=1024` - Qwen3-Embedding-0.6B output dimension
- `MAX_CHUNK_TOKENS=1000` - Target chunk size for document splitting
- `DOCS_ROOT` - Auto-detects Docker (`/llm-code-docs/docs`) vs local (`~/github/llm-code-docs/docs`)

## Format Converters

### HTML to Markdown (ReaderLM-v2)
Converts HTML/MDX to clean Markdown via local LLM. Used for:
- Pure HTML files saved as .md (scraped Notion docs)
- MDX/JSX files with embedded HTML (Weaviate, etc.)

API endpoint: `http://localhost:10010/v1/chat/completions` (OpenAI-compatible)

**Specs:** 1.54B params, bfloat16, 512K context, ~4GB VRAM

**Usage:**
```bash
# Convert a single file
python scripts/html_to_markdown.py input.html output.md

# Convert in-place (overwrite)
python scripts/html_to_markdown.py input.md --inplace

# Dry run to check what would be converted
python scripts/html_to_markdown.py file.md --dry-run
```

**Use Cases:**
1. **Pure HTML files** saved as .md (e.g., scraped Notion docs at `llm-code-docs/docs/llms-txt/notion/`)
2. **MDX/JSX files** with embedded HTML (e.g., Weaviate docs at `llm-code-docs/docs/github-scraped/weaviate/`)
3. **Any HTML-heavy markdown** that needs cleanup

**API Usage:**
```bash
curl http://localhost:10010/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "jinaai/ReaderLM-v2",
    "messages": [{"role": "user", "content": "Convert to markdown:\n```html\n<h1>Hello</h1>\n```"}]
  }'
```

### RFC to Markdown
Converts IETF RFC txt files to structured Markdown with:
- YAML frontmatter (RFC number, title, date, category)
- Clickable table of contents
- Code block detection
- Page break removal

### SiYuan to Markdown
Converts SiYuan's JSON-based `.sy` files to clean Markdown. Handles:
- Headings, paragraphs, lists (nested), tables
- Code blocks, blockquotes, math blocks
- Inline formatting (bold, italic, code, links, marks)

## Automation Scripts

### docs-loop.py
Continuously processes `doc-add` labeled trckr tickets by invoking `/docs:WTFM-next`.

```bash
python scripts/docs-loop.py --workers 2 --limit 10 --max-stale 3
```
- `--workers N` - Parallel Claude instances (staggered start)
- `--max-stale N` - Stop if no progress for N iterations
- Logs to `output/docs-loop.log`

### process-docs-queue.py
Processes tickets from `output/docs_tickets.csv` using git worktrees.

```bash
python scripts/process-docs-queue.py --workers 2 --status triage,todo
```
- Creates worktree per ticket in `/tmp/llm-code-docs-<branch>`
- Runs `/WTFM <topic>` then merges to master
- Thread-safe CSV locking for parallel workers

## Key Patterns

**Discovery pipeline:** `sindresorhus/awesome` + `bayandin/awesome-awesomeness` → 846 unique awesome lists → extract project URLs → check for llms.txt or good docs → add to llm-code-docs

**Search index:** Documents are chunked (~1000 tokens), embedded via TEI, stored in LanceDB. Hybrid ranking combines semantic similarity (70%), keyword matching (20%), and recency (10%).

**Ticket workflow:** trckr issues with `doc-add` label → triage → todo → in-progress (via automation) → in-review → done

## Discovery Implementation Details

**crawler.py:**
- `AwesomeRepo` - Dataclass representing a discovered repo (owner, name, url, depth, parent)
- `AwesomeCrawler` - Recursive crawler with rate limiting, deduplication, and depth control
  - `is_likely_awesome_list()` - Heuristic detection (looks for "awesome", "curated", "list", etc.)
  - `fetch_readme()` - Fetches README via raw.githubusercontent.com with fallbacks

**extract_local.py:**
- `extract_from_file()` - Regex-based GitHub link extraction from markdown
- `is_awesome_name()` - Simple name-based awesome list detection
