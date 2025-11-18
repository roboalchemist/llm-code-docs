# Augment Code Documentation

This directory contains LLM-optimized documentation for [Augment Code](https://www.augmentcode.com/), an AI-powered coding assistant.

## What is Augment Code?

Augment Code is an AI coding assistant that helps developers:
- Generate code from natural language descriptions
- Refactor and improve existing code
- Debug and fix errors
- Navigate and understand codebases
- Support multiple programming languages and frameworks

## Documentation Format

The documentation here is extracted from Augment's official LLM-friendly documentation following the [llms.txt](https://llmstxt.org/) standard.

### 1. Individual Files (72 files)
Individual markdown files for each documentation page, ideal for:
- Efficient context management (load only what you need)
- Targeted documentation lookup
- Reduced token usage in LLM contexts

### 2. Comprehensive File
- `augment-code-full.md` - Complete Augment documentation in a single file (~471 KB)
- Useful for full-context searches and comprehensive reference

## Contents

The documentation covers:

### Getting Started
- **Installation**: Setting up Augment in your editor
- **Authentication**: API keys and account setup
- **Quick Start**: First steps with Augment
- **Configuration**: Customizing Augment settings

### Features
- **Code Generation**: Creating code from descriptions
- **Code Completion**: Intelligent autocomplete
- **Code Explanation**: Understanding complex code
- **Refactoring**: Improving code quality
- **Debugging**: Finding and fixing issues

### Integrations
- **VS Code**: Visual Studio Code extension
- **JetBrains IDEs**: IntelliJ, PyCharm, etc.
- **CLI**: Command-line interface
- **ACP Mode**: Agent Client Protocol integration

### Advanced Topics
- **Custom Models**: Using custom AI models
- **Context Management**: Optimizing context windows
- **Team Features**: Collaboration and sharing
- **API Reference**: Programmatic access

## Updating This Documentation

To update the Augment Code documentation to the latest version:

```bash
# From repository root - updates all llms.txt sites
python3 update-scripts/llms-txt-scraper.py

# Update only Augment docs
python3 update-scripts/llms-txt-scraper.py --site augment-code

# Or use the master update script
./update-scripts/update.sh
```

## File Statistics

- **Individual Files**: 72 markdown files
- **Total Size**: ~964 KB
- **Comprehensive File**: augment-code-full.md (~471 KB)
- **Coverage**: Complete Augment Code documentation

## Source

All documentation is sourced from:
- **Index**: https://docs.augmentcode.com/llms.txt
- **Full**: https://docs.augmentcode.com/llms-full.txt
- **Human-readable**: https://docs.augmentcode.com/

## Use Cases

This documentation is ideal for:
- Training AI models on Augment Code usage
- Building AI assistants that integrate with Augment
- Creating context for LLM-powered development tools
- Offline reference for Augment features
- Automated documentation analysis and search
- Efficient context loading (use individual files instead of full file)

## Related Links

- [Augment Code Website](https://www.augmentcode.com/)
- [Augment Documentation](https://docs.augmentcode.com/)
- [Agent Client Protocol](https://agentclientprotocol.com/)
- [llms.txt Standard](https://llmstxt.org/)

---

**Last Updated**: 2025-11-18
**Update Script**: `update-scripts/llms-txt-scraper.py`
**Configuration**: `update-scripts/llms-sites.yaml`
**Upstream Source**: https://docs.augmentcode.com/
