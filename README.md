# LLM Code Documentation Repository

This repository provides comprehensive, AI-readable documentation for various codebases and frameworks. It includes both automated documentation extraction tools and curated documentation collections.

## 🎯 Purpose

This repository serves as a centralized hub for:
- **AI-Optimized Documentation**: Structured for easy parsing by LLMs and AI coding assistants
- **Automated Documentation Sync**: Tools to keep documentation current with source projects
- **Comprehensive Coverage**: Multiple frameworks and libraries in one location

## 📋 Project Status

### Completed
- ✅ CircuitPython documentation extraction
- ✅ Claude Code SDK documentation extraction
- ✅ Textual framework documentation

### In Progress
- ✅ Notion API documentation (93% complete via Crawl4AI - 66/71 files)

### Completed (Recent)
- ✅ Perplexity API documentation extraction (50 files, 476KB)
- ✅ OpenRouter models API extraction (330 models, 53 providers)

See `todo.txt` for detailed task breakdown (21 tasks across 3 phases).

## 📚 Available Documentation

### Current Documentation Sets

- **🌐 Textual Framework** (`textual/`) - Complete TUI framework documentation
- **🔌 CircuitPython** (`circuitpython/`) - MicroPython for microcontrollers
- **🤖 Claude Code SDK** (`claude-code-sdk/`) - Anthropic's Claude Code development tools
- **📝 Notion API** (`notion/`) - Notion API reference documentation
- **🔍 Perplexity API** (`perplexity/`) - Perplexity AI API reference and guides
- **🔀 OpenRouter Models** (`openrouter/`) - Complete model catalog with pricing and capabilities

### Documentation Coverage

- API references and function signatures
- Implementation examples and code samples
- Configuration and setup guides
- Best practices and design patterns
- Troubleshooting and common issues

## 🚀 Quick Start

### Update All Documentation
```bash
# Run all documentation update scripts
./update-scripts/update.sh
```

### Update Specific Documentation
```bash
# Update CircuitPython docs
python3 update-scripts/extract_docs.py

# Update Claude Code SDK docs
python3 update-scripts/claude-code-sdk-docs.py

# Update Notion API docs (71 pages, 93% complete via Crawl4AI)
python3 update-scripts/notion-docs-crawl4ai.py

# Update Perplexity API docs
python3 update-scripts/perplexity-docs.py

# Update OpenRouter models catalog
python3 update-scripts/openrouter-models.py
```

## 🛠️ Update Scripts

The `update-scripts/` directory contains automated tools for maintaining current documentation:

### Available Scripts

| Script | Purpose | Features |
|--------|---------|----------|
| `update.sh` | **Master updater** - runs all documentation scripts | Progress tracking, error handling, summary reporting |
| `extract_docs.py` | **CircuitPython extractor** - clones and extracts docs from git repos | Configurable via YAML, preserves structure, handles updates |
| `claude-code-sdk-docs.py` | **Claude Code SDK downloader** - downloads from official docs | Live sidebar extraction, automatic updates, change detection |
| `notion-docs-crawl4ai.py` | **Notion API reference downloader** - extracts API documentation | Crawl4AI framework, handles JS rendering, complete content capture |
| `perplexity-docs.py` | **Perplexity API extractor** - downloads API documentation | Crawl4AI framework, JavaScript rendering, 50 pages extracted |
| `openrouter-models.py` | **OpenRouter models catalog extractor** - fetches model catalog via API | API-based extraction, dual format output (JSON + Markdown), 330 models |

### Script Features

- **🔄 Automatic Updates**: Scripts detect changes and update only modified files
- **📊 Progress Tracking**: Real-time progress indicators and detailed summaries  
- **⚡ Smart Extraction**: Live sidebar parsing ensures complete documentation capture
- **🛡️ Error Handling**: Robust error handling with informative failure messages
- **📈 Statistics**: File counts, sizes, and timing information for all operations

## 📁 Repository Structure

```
llm-code-docs/
├── README.md                           # This file
├── update-scripts/                     # Documentation maintenance tools
│   ├── update.sh                      # Master update script
│   ├── extract_docs.py                # CircuitPython documentation extractor
│   ├── claude-code-sdk-docs.py        # Claude Code SDK documentation downloader
│   ├── notion-docs.py                 # Notion API reference downloader
│   └── repo_config.yaml               # Configuration for git repository extraction
├── textual/                           # Textual TUI framework documentation
├── circuitpython/                     # CircuitPython microcontroller documentation
├── claude-code-sdk/                   # Claude Code SDK development documentation
├── notion/                            # Notion API reference documentation
├── perplexity/                        # Perplexity API documentation
└── openrouter/                        # OpenRouter models catalog with pricing and capabilities
```

## 🔧 Configuration

### Repository Extraction (CircuitPython)
Edit `update-scripts/repo_config.yaml`:
```yaml
repositories:
  circuitpython:
    url: "https://github.com/adafruit/circuitpython"
    source_folder: "docs"
    target_folder: "circuitpython"
```

### Claude Code SDK Updates
The script automatically extracts the current sidebar structure from https://docs.anthropic.com/en/docs/claude-code/sdk to ensure complete coverage.

### Notion API Updates

Uses Crawl4AI for content extraction with JavaScript rendering:
```bash
# Extract all 71 Notion API pages
python3 update-scripts/notion-docs-crawl4ai.py
```

Crawl4AI successfully extracted 71 pages with 66 files containing complete content including examples, object schemas, and code samples. 5 OAuth endpoint files (revoke-token, introspect-token, complete-a-file-upload, retrieve-a-file-upload, list-file-uploads) have partial content due to complex page structure and may require manual extraction.

### Perplexity API Updates

Uses Crawl4AI for comprehensive documentation extraction:
```bash
# Extract all Perplexity API documentation
python3 update-scripts/perplexity-docs.py
```

Successfully extracted 50 documentation pages covering API Reference, Getting Started, Guides, Cookbook, and Help sections with 100% success rate.

### OpenRouter Models Catalog

Uses the OpenRouter API to fetch the complete model catalog:
```bash
# Set your API key (required)
export OPENROUTER_API_KEY="your-api-key-here"

# Extract all OpenRouter models
python3 update-scripts/openrouter-models.py
```

Successfully extracted 330 models from 53 providers with dual format output:
- **JSON catalog** (587KB): Complete model data with enhanced metadata including pricing stats, context window ranges, capability distribution, and provider information
- **Markdown table** (34KB): Human-readable comparison with model names, context lengths, and pricing

Model catalog includes 54 free models (16% of catalog), with top providers being qwen (42 models), openai (42 models), and mistralai (35 models).

## 📊 Statistics

The repository currently contains:
- **71 documentation files** for Notion API (~596KB total via Crawl4AI, 93% complete)
- **50 documentation files** for Perplexity API (~476KB total via Crawl4AI)
- **330 models** in OpenRouter catalog (~587KB JSON + 34KB Markdown, 53 providers)
- **37+ documentation files** for Claude Code SDK
- **Complete CircuitPython docs** extracted from official repositories
- **Comprehensive Textual framework** documentation
- **7MB+ total documentation** optimized for AI consumption

## 🗂️ Task Management

The project uses a comprehensive task list in `todo.txt` with **21 detailed tasks** organized in **3 phases**:

### Phase 0: Current State Validation
- Task 0: Validate existing Notion extraction and determine starting point

### Phase 1: Notion API Documentation (Tasks 1-8) - ✅ SUBSTANTIALLY COMPLETE
- ✅ Complete extraction using Crawl4AI framework (Tasks 1-3)
- ✅ JavaScript-rendered content handling
- ✅ Comprehensive QA and verification (Task 4)
- ✅ Documentation updates (Task 6)
- Note: 66/71 files successfully extracted; 5 OAuth endpoint files require manual extraction

### Phase 2: Perplexity Documentation (Tasks 9-15) - ✅ COMPLETE
- ✅ Research and implement Perplexity docs extraction
- ✅ Crawl4AI-based extraction script
- ✅ Full extraction and verification (50 files, 476KB, 100% success rate)

### Phase 3: OpenRouter Models API (Tasks 16-20) - ✅ COMPLETE
- ✅ API-based extraction of model catalog (330 models, 53 providers)
- ✅ Dual format output: JSON (587KB) + Markdown (34KB)
- ✅ Comprehensive metadata with pricing, capabilities, and provider stats
- ✅ Documentation and final project verification

Each task is self-contained with complete instructions, verification steps, and success criteria for independent agent execution.

## 🎯 Usage with AI Systems

This documentation is optimized for:
- **Code generation assistance**: Detailed API references and examples
- **Implementation guidance**: Step-by-step guides and best practices  
- **Troubleshooting support**: Common issues and solutions
- **Architecture understanding**: Project structures and design patterns

## 🔄 Keeping Documentation Current

### Automated Updates
```bash
# Update all documentation sets
./update-scripts/update.sh

# This will:
# 1. Extract fresh CircuitPython docs from GitHub
# 2. Download latest Claude Code SDK documentation  
# 3. Report on changes and statistics
# 4. Handle errors gracefully with detailed logging
```

### Manual Updates
Individual scripts can be run for targeted updates:
```bash
# Force fresh sidebar extraction for Claude Code SDK
python3 update-scripts/claude-code-sdk-docs.py

# Use cached links for faster updates
python3 update-scripts/claude-code-sdk-docs.py --cached
```

## 🏗️ Adding New Documentation

To add documentation for a new project:

1. **Add extraction script** to `update-scripts/`
2. **Update `repo_config.yaml`** if using git extraction
3. **Run master update script** to verify integration
4. **Update this README** to document the new addition

## 📝 Documentation Quality

All documentation in this repository is:
- ✅ **Regularly updated** via automated scripts
- ✅ **Comprehensive** with full API coverage  
- ✅ **Structured** for optimal AI parsing
- ✅ **Verified** through automated testing and validation
- ✅ **Version-controlled** with clear change tracking

---

This repository is maintained to provide the most current and comprehensive documentation for AI-assisted development across multiple frameworks and tools.