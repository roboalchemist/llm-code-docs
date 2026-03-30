---
name: llm-code-docs-repo
description: Repository management for llm-code-docs - adding new documentation sources, updating existing docs, running scrapers, and maintaining the index. For searching docs, use the llm-code-docs CLI instead.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# llm-code-docs Repository Management

## Overview
This skill covers managing the documentation repository at `~/github/llm-code-docs`. For **searching** documentation, use the `llm-code-docs` CLI (`llm-code-docs search`, `llm-code-docs suggest`).

## Adding New Documentation

### Priority Order
1. **llms.txt** - Check first (highest quality)
2. **Git repos** - For comprehensive source docs
3. **Web scraping** - Last resort

### Add llms.txt Site
```bash
cd ~/github/llm-code-docs
./scripts/find-llms-txt.sh example.com
# Edit scripts/llms-sites.yaml (alphabetical order)
python3 scripts/llms-txt-scraper.py --site example-site
python3 scripts/update-index.py
```

### Add Git Repository
```bash
# Edit scripts/repo_config.yaml
python3 scripts/extract_docs.py
python3 scripts/update-index.py
```

### Add Web Scraper
```bash
cp scripts/ntfy-docs.py scripts/newsite-docs.py
# Edit BASE_URL, DOC_PAGES, output path
python3 scripts/newsite-docs.py
python3 scripts/update-index.py
```

## Updating Documentation
```bash
./scripts/update.sh                                    # Update everything
python3 scripts/llms-txt-scraper.py --site anthropic   # Single site
python3 scripts/llms-txt-scraper.py --force            # Force re-download
```

## Key Scripts

| Script | Purpose |
|--------|---------|
| `find-llms-txt.sh` | Probe domain for llms.txt |
| `llms-txt-scraper.py` | Download from 228+ llms.txt sites |
| `extract_docs.py` | Clone and extract Git repositories |
| `update-index.py` | Rebuild index.yaml |
| `update.sh` | Master update orchestrator |
