# Claude Documentation

This directory contains LLM-optimized documentation for [Claude](https://www.anthropic.com/claude), Anthropic's AI assistant.

## What is Claude?

Claude is a family of large language models developed by Anthropic. Claude offers:
- Advanced reasoning and analysis capabilities
- Long context windows (up to 200K tokens)
- Strong coding and technical abilities
- Vision capabilities for image analysis
- Multiple model tiers (Opus, Sonnet, Haiku)

## Documentation Format

The documentation here is extracted from Claude's official LLM-friendly documentation following the [llms.txt](https://llmstxt.org/) standard.

### 1. Individual Files (216 files)
Individual markdown files for each documentation page, ideal for:
- Efficient context management (load only what you need)
- Targeted documentation lookup
- Reduced token usage in LLM contexts

### 2. Comprehensive File
- `claude-docs-full.md` - Complete Claude documentation in a single file (~4.4 MB)
- Useful for full-context searches and comprehensive reference

## Contents

The documentation covers:

### API Documentation
- **Messages API**: Core API for Claude interactions
- **Batch Processing**: Batch API for asynchronous requests
- **Streaming**: Real-time response streaming
- **Vision**: Image analysis capabilities
- **Tool Use**: Function calling and computer use

### Development Resources
- **SDKs**: Python and TypeScript client libraries
- **Best Practices**: Prompting techniques and optimization
- **Rate Limits**: API quotas and rate limiting
- **Error Handling**: Error codes and debugging

### Prompt Engineering
- **Chain of Thought**: Advanced reasoning techniques
- **Few-shot Learning**: Examples and demonstrations
- **Prompt Library**: Pre-built prompt templates
- **Metaprompting**: System prompts and instructions

### Enterprise Features
- **Administration API**: Organization management
- **Workspaces**: Team collaboration
- **Usage Tracking**: Monitoring and analytics
- **Security**: Authentication and access control

## Updating This Documentation

To update the Claude documentation to the latest version:

```bash
# From repository root - updates all llms.txt sites
python3 update-scripts/llms-txt-scraper.py

# Update only Claude docs
python3 update-scripts/llms-txt-scraper.py --site claude-docs

# Or use the master update script
./update-scripts/update.sh
```

## File Statistics

- **Individual Files**: 216 markdown files
- **Total Size**: ~8.7 MB
- **Comprehensive File**: claude-docs-full.md (~4.4 MB)
- **Coverage**: Complete Claude API and developer documentation

## Source

All documentation is sourced from:
- **Index**: https://docs.claude.com/llms.txt
- **Full**: https://docs.claude.com/llms-full.txt
- **Human-readable**: https://docs.claude.com/

## Use Cases

This documentation is ideal for:
- Training AI models on Claude API usage
- Building AI assistants that use Claude
- Creating context for LLM-powered development tools
- Offline reference for Claude features
- Automated documentation analysis and search
- Efficient context loading (use individual files instead of full file)

## Related Links

- [Anthropic Website](https://www.anthropic.com/)
- [Claude Console](https://console.anthropic.com/)
- [Claude API](https://docs.anthropic.com/)
- [llms.txt Standard](https://llmstxt.org/)

---

**Last Updated**: 2025-11-18
**Update Script**: `update-scripts/llms-txt-scraper.py`
**Configuration**: `update-scripts/llms-sites.yaml`
**Upstream Source**: https://docs.claude.com/
