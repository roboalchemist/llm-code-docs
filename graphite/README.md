# Graphite Documentation

This directory contains LLM-optimized documentation for [Graphite](https://graphite.dev/), a modern developer workflow tool for stacked pull requests and Git workflows.

## What is Graphite?

Graphite is a suite of tools that helps developers:
- Create and manage stacked pull requests
- Streamline Git workflows
- Collaborate on code changes more efficiently
- Use AI-powered code review features

Graphite provides both a CLI tool and web dashboard for managing pull request stacks.

## Documentation Format

The documentation here is extracted from Graphite's official LLM-friendly documentation files:

- **llms-full.txt**: A comprehensive single-file export of all Graphite documentation, optimized for AI/LLM consumption
- **llms.txt**: An index file listing all individual documentation pages (similar to a sitemap)

These files follow the [llms.txt](https://llmstxt.org/) standard for AI-readable documentation.

## Contents

- `graphite-full.md` - Complete Graphite documentation in a single markdown file (~600KB)
  - Basic and advanced CLI tutorials
  - AI code review features and configuration
  - GitHub authentication and integration
  - Billing and plan information
  - CLI command reference
  - Troubleshooting guides
  - API documentation

## Updating This Documentation

To update the Graphite documentation to the latest version:

```bash
# From repository root
python3 update-scripts/graphite-docs.py

# Or use the master update script
./update-scripts/update.sh
```

### Script Options

The `graphite-docs.py` script supports three modes:

```bash
# Download just the full comprehensive file (default)
python3 update-scripts/graphite-docs.py --mode full

# Download individual markdown files
python3 update-scripts/graphite-docs.py --mode individual

# Download both formats
python3 update-scripts/graphite-docs.py --mode both
```

## Documentation Coverage

The full documentation includes:

### Core Topics
- **Getting Started**: Installation, authentication, basic workflows
- **Stacked PRs**: Creating, managing, and collaborating on stacked pull requests
- **CLI Commands**: Complete reference for all `gt` commands
- **AI Features**: AI-powered code review, privacy, customization
- **Integrations**: GitHub, VS Code, Linear, Slack
- **Web Dashboard**: Managing PRs through the web interface
- **Merge Queues**: Automated PR merging and testing

### Advanced Features
- Multi-trunk support
- Branch reordering and rebasing
- Team collaboration workflows
- Custom review rules
- Billing and plan management

## Source

All documentation is sourced from:
- **Primary**: https://graphite.com/docs/llms-full.txt
- **Index**: https://graphite.com/docs/llms.txt
- **Human-readable**: https://graphite.com/docs/

## Statistics

- **File Size**: ~600KB
- **Lines**: ~9,800
- **Code Blocks**: ~270
- **Sections**: ~780+

## Use Cases

This documentation is ideal for:
- Training AI models on Graphite workflows
- Building AI assistants that understand Graphite commands
- Creating context for LLM-powered development tools
- Offline reference for Graphite features
- Automated documentation analysis and search

## Related Links

- [Graphite Website](https://graphite.dev/)
- [Graphite CLI GitHub](https://github.com/withgraphite/graphite-cli)
- [llms.txt Standard](https://llmstxt.org/)

---

**Last Updated**: 2025-11-18
**Update Script**: `update-scripts/graphite-docs.py`
**Upstream Source**: https://graphite.com/docs/
