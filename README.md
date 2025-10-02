# LLM Code Documentation Repository

This repository provides comprehensive, AI-readable documentation for various codebases and frameworks. It includes both automated documentation extraction tools and curated documentation collections.

## 🎯 Purpose

This repository serves as a centralized hub for:
- **AI-Optimized Documentation**: Structured for easy parsing by LLMs and AI coding assistants
- **Automated Documentation Sync**: Tools to keep documentation current with source projects
- **Comprehensive Coverage**: Multiple frameworks and libraries in one location

## 📚 Available Documentation

### Current Documentation Sets

- **🌐 Textual Framework** (`textual/`) - Complete TUI framework documentation
- **🔌 CircuitPython** (`circuitpython/`) - MicroPython for microcontrollers
- **🤖 Claude Code SDK** (`claude-code-sdk/`) - Anthropic's Claude Code development tools
- **📝 Notion API** (`notion/`) - Notion API reference documentation

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

# Update Notion API docs (63 pages, skips 8 JS-rendered pages)
python3 update-scripts/notion-docs.py --cached
```

## 🛠️ Update Scripts

The `update-scripts/` directory contains automated tools for maintaining current documentation:

### Available Scripts

| Script | Purpose | Features |
|--------|---------|----------|
| `update.sh` | **Master updater** - runs all documentation scripts | Progress tracking, error handling, summary reporting |
| `extract_docs.py` | **CircuitPython extractor** - clones and extracts docs from git repos | Configurable via YAML, preserves structure, handles updates |
| `claude-code-sdk-docs.py` | **Claude Code SDK downloader** - downloads from official docs | Live sidebar extraction, automatic updates, change detection |
| `notion-docs.py` | **Notion API reference downloader** - extracts API documentation | Skips JS-rendered pages, prevents corruption, detailed warnings |

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
└── notion/                            # Notion API reference documentation
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
The Notion API documentation extractor has special handling for JavaScript-rendered pages:

**Known Limitation**: 8 pages require JavaScript rendering and are automatically skipped to prevent file corruption:
- `revoke-token.md`
- `introspect-token.md`
- `list-file-uploads.md`
- `complete-a-file-upload.md`
- `retrieve-a-file-upload.md`
- `refresh-a-token.md`
- `create-a-data-source.md`
- `create-a-file-upload.md`

These pages must be manually extracted using browser automation tools (e.g., Playwright). The script will skip them and display warnings to prevent overwriting existing manually-extracted content.

## 📊 Statistics

The repository currently contains:
- **71 documentation files** for Notion API (63 fully extracted, 8 require manual extraction)
- **37+ documentation files** for Claude Code SDK
- **Complete CircuitPython docs** extracted from official repositories
- **Comprehensive Textual framework** documentation
- **750KB+ total documentation** optimized for AI consumption

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