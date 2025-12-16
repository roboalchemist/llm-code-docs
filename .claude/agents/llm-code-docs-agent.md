# llm-code-docs Agent

Agent specialized for working with the llm-code-docs repository - a centralized AI-readable documentation hub.

## Repository Location

`~/github/llm-code-docs/`

## Repository Structure

```
llm-code-docs/
├── docs/
│   ├── llms-txt/          # llms.txt standard docs (285+ sites) - HIGHEST PRIORITY
│   ├── github-scraped/    # Git repository extractions (28 repos)
│   ├── github-repos/      # GitHub repo READMEs
│   └── web-scraped/       # Custom web scrapers (15 sets)
├── scripts/
│   ├── llms-sites.yaml    # Registry of llms.txt sites
│   ├── repo_config.yaml   # Git repo extraction config
│   ├── llms-txt-scraper.py      # Main llms.txt downloader
│   ├── find-llms-txt.sh         # Probe domain for llms.txt
│   ├── extract_docs.py          # Git repo extractor
│   ├── update-index.py          # Regenerate index.yaml
│   └── update.sh                # Master update orchestrator
├── index.yaml             # Auto-generated documentation index
├── CLAUDE.md              # Full repo documentation
└── todo.md                # Documentation wishlist
```

## Documentation Priority

1. **llms.txt** - Highest quality, official AI-optimized format
2. **GitHub repos** - Comprehensive docs from source
3. **Web scraping** - Last resort for critical documentation

## Key Commands

For **reading** documentation, use the `/RTFM` command:
```
/RTFM <topic>
```

For **writing/adding** documentation, use the `/WTFM` command:
```
/WTFM <topic>
```

These commands contain the authoritative procedures for finding and adding documentation.

## Quick Reference

### Check if docs exist for a topic
```bash
ls ~/github/llm-code-docs/docs/llms-txt/ | grep -i <topic>
grep -i <topic> ~/github/llm-code-docs/index.yaml
```

### Probe a domain for llms.txt
```bash
~/github/llm-code-docs/scripts/find-llms-txt.sh <domain>
```

### Add new llms.txt site
1. Add to `scripts/llms-sites.yaml` (alphabetical order)
2. Run: `python3 scripts/llms-txt-scraper.py --site <name>`
3. Run: `python3 scripts/update-index.py`

### Update all documentation
```bash
cd ~/github/llm-code-docs && ./scripts/update.sh
```

## Current Stats

Check `index.yaml` for current counts:
- llms.txt sites: 285+ configured
- GitHub repos: 28 configured
- Web scraped: 15 sets

## Guidelines

1. Always check if documentation already exists before adding
2. Prefer llms.txt sources over custom scrapers
3. Use `find-llms-txt.sh` to probe for llms.txt before assuming it doesn't exist
4. Keep `llms-sites.yaml` alphabetically sorted
5. Run `update-index.py` after adding new sources
6. Commit and push after adding documentation
