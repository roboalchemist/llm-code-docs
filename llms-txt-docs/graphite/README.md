# Graphite Documentation

This directory contains LLM-optimized documentation for [Graphite](https://graphite.dev/), a modern developer workflow tool for stacked pull requests and Git workflows.

## What is Graphite?

Graphite is a suite of tools that helps developers:
- Create and manage stacked pull requests
- Streamline Git workflows with the `gt` CLI
- Collaborate on code changes more efficiently
- Use AI-powered code review features

Graphite provides both a CLI tool and web dashboard for managing pull request stacks.

## Documentation Format

The documentation here is extracted from Graphite's official LLM-friendly documentation files following the [llms.txt](https://llmstxt.org/) standard. We download both formats:

### 1. Individual Files (91 files)
Individual markdown files for each documentation page, ideal for:
- Efficient context management (load only what you need)
- Targeted documentation lookup
- Reduced token usage in LLM contexts

### 2. Comprehensive File
- `graphite-full.md` - Complete Graphite documentation in a single file (~600KB)
- Useful for full-context searches and comprehensive reference

## Contents

The documentation covers:

### Core Topics
- **Getting Started**: Installation, authentication, basic workflows
- **Stacked PRs**: Creating, managing, and collaborating on stacked pull requests
- **CLI Commands**: Complete reference for all `gt` commands
- **AI Features**: AI-powered code review, privacy, customization
- **Integrations**: GitHub, VS Code, Linear, Slack, Jira
- **Web Dashboard**: Managing PRs through the web interface
- **Merge Queues**: Automated PR merging and testing

### Advanced Features
- Multi-trunk support
- Branch reordering and rebasing
- Team collaboration workflows
- Custom review rules
- CI optimizations for stacks
- Billing and plan management

## Updating This Documentation

To update the Graphite documentation to the latest version:

```bash
# From repository root - downloads both formats by default
python3 update-scripts/graphite-docs.py

# Or use the master update script
./update-scripts/update.sh
```

### Script Options

The `graphite-docs.py` script supports three modes:

```bash
# Download both formats (default)
python3 update-scripts/graphite-docs.py --mode both

# Download only individual files
python3 update-scripts/graphite-docs.py --mode individual

# Download only the comprehensive file
python3 update-scripts/graphite-docs.py --mode full
```

## File Statistics

- **Individual Files**: 91 markdown files
- **Total Size**: ~1.4 MB
- **Comprehensive File**: graphite-full.md (~600 KB)
- **Coverage**: Complete Graphite documentation

## Source

All documentation is sourced from:
- **Index**: https://graphite.com/docs/llms.txt (list of all pages)
- **Full**: https://graphite.com/docs/llms-full.txt (comprehensive file)
- **Human-readable**: https://graphite.com/docs/

## Use Cases

This documentation is ideal for:
- Training AI models on Graphite workflows
- Building AI assistants that understand Graphite commands
- Creating context for LLM-powered development tools
- Offline reference for Graphite features
- Automated documentation analysis and search
- Efficient context loading (use individual files instead of full file)

## Related Links

- [Graphite Website](https://graphite.dev/)
- [Graphite CLI GitHub](https://github.com/withgraphite/graphite-cli)
- [llms.txt Standard](https://llmstxt.org/)
- [Graphite Agent (AI Reviews)](https://graphite.dev/docs/ai-reviews)

---

**Last Updated**: 2025-11-18
**Update Script**: `update-scripts/graphite-docs.py`
**Upstream Source**: https://graphite.com/docs/
