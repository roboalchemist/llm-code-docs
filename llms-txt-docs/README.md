# llms.txt-Compliant Documentation

This directory contains documentation from websites that follow the [llms.txt standard](https://llmstxt.org/) for LLM-friendly documentation.

## What is llms.txt?

The llms.txt standard is a proposal for providing LLM-friendly content through:
- `/llms.txt` - A markdown file with structured links to documentation
- `/llms-full.txt` - A comprehensive single-file version of all documentation
- Individual `.md` files - Clean markdown versions of each documentation page

This standard makes it easy for AI systems to:
- Discover documentation efficiently
- Load only relevant sections (reducing context usage)
- Access clean, structured content without HTML/JavaScript overhead

## Sites in This Directory

### claude-docs/
**Source**: https://docs.claude.com/
**Description**: Anthropic Claude AI assistant documentation
**Files**: 216 markdown files (8.7 MB)
**Content**: API reference, prompt engineering, best practices, SDKs

### augment-code/
**Source**: https://docs.augmentcode.com/
**Description**: Augment Code AI coding assistant documentation
**Files**: 72 markdown files (964 KB)
**Content**: IDE integrations, CLI tools, ACP mode, features

### graphite/
**Source**: https://graphite.com/docs/
**Description**: Graphite stacked pull requests and developer tools
**Files**: 91 markdown files (1.4 MB)
**Content**: CLI commands, web dashboard, merge queues, AI reviews

## Directory Structure

Each site directory contains:
```
site-name/
├── README.md              # Site-specific documentation
├── site-name-full.md      # Comprehensive single-file version
└── *.md                   # Individual documentation pages
```

## Updating Documentation

To update all llms.txt-compliant sites:

```bash
# From repository root
python3 update-scripts/llms-txt-scraper.py

# Update specific site only
python3 update-scripts/llms-txt-scraper.py --site claude-docs

# Update all documentation (including non-llms.txt sites)
./update-scripts/update.sh
```

## Adding New Sites

To add a new llms.txt-compliant site:

1. Edit `update-scripts/llms-sites.yaml`:
```yaml
sites:
  - name: new-site-name
    base_url: https://example.com/
    description: Brief description of the site
```

2. Run the scraper:
```bash
python3 update-scripts/llms-txt-scraper.py --site new-site-name
```

3. The documentation will be automatically downloaded to `llms-txt-docs/new-site-name/`

## Configuration

Sites are configured in: `update-scripts/llms-sites.yaml`

The scraper supports:
- `--site SITENAME` - Download only a specific site
- `--mode full` - Download only comprehensive files
- `--mode individual` - Download only individual files
- `--mode both` - Download both formats (default)

## Why Separate llms.txt Documentation?

This separation helps organize documentation by collection method:
- **llms-txt-docs/**: Sites following the standardized llms.txt format
- **Root directory**: Sites using custom extraction methods

Benefits:
- Clear organization by documentation standard
- Easy to identify which sites can be updated via generic scraper
- Simplified maintenance and updates

## Related Links

- [llms.txt Standard](https://llmstxt.org/)
- [llms.txt Proposal](https://github.com/AnswerDotAI/llms-txt)
- [llmstxt Directory](https://llmstxt.site/)

---

**Last Updated**: 2025-11-18
**Scraper Script**: `update-scripts/llms-txt-scraper.py`
**Configuration**: `update-scripts/llms-sites.yaml`
