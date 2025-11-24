# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository provides centralized, AI-readable documentation extracted from 175+ frameworks, libraries, and developer tools. It includes automated extraction tools that keep documentation current with upstream sources.

**Purpose**: Serve as a comprehensive documentation hub optimized for LLM consumption and AI-assisted development.

## Repository Architecture

### Three-Tier Documentation Structure

1. **llms.txt-Compliant Documentation** (`llms-txt-docs/`) - **HIGHEST PRIORITY**
   - **233 sites** following the llms.txt standard (https://llmstxt.org/)
   - Each site in its own subdirectory: `llms-txt-docs/{site-name}/`
   - Parallel downloads with 15 concurrent workers
   - File-level caching with 23-hour freshness window
   - Recent additions: `gradio/`, `vite/`, `ant-design/`, `ollama/`, `react/`
   - Examples: `llms-txt-docs/anthropic/`, `llms-txt-docs/vercel-ai-sdk/`, `llms-txt-docs/bun/`

2. **Git-Based Documentation Extractions** (`github-scraped-docs/`)
   - `circuitpython/` - MicroPython for microcontrollers
   - `click/` - Python CLI framework (Pallets)
   - `fastapi/` - Modern Python web framework
   - `flask/` - Lightweight WSGI web framework (Pallets)
   - `go-docs/` - Go programming language official docs
   - `goose/` - AI-powered developer agent (Block)
   - `python-docs/` - Python 3.13 official documentation
   - `sqlalchemy/` - Python SQL toolkit and ORM
   - `textual/` - TUI framework documentation
   - And more (15 total repositories)

3. **Web-Scraped Documentation** (`web-scraped-docs/`)
   - `claude-code-sdk/` - Anthropic's Claude Code SDK (HTML scraping)
   - `notion/` - Notion API documentation
   - `perplexity/` - Perplexity API documentation
   - `openrouter/` - OpenRouter models catalog
   - `readmes/` - Individual README files from GitHub

### Configuration Files

- **`update-scripts/llms-sites.yaml`** - Central registry of 170 llms.txt-compliant sites
  - Structure: `name`, `base_url`, `description`, optional `rate_limit_seconds`
  - Alphabetically sorted by name
  - Used by `llms-txt-scraper.py` for bulk downloads

- **`update-scripts/repo_config.yaml`** - Git repository extraction config
  - 15 repositories: CircuitPython, Click, FastAPI, Flask, SQLAlchemy, Go, Python, Goose, and more
  - Each repo specifies: `repo_url`, `source_folder`, `target_folder`, `branch`
  - All target folders now under `github-scraped-docs/`

### Update Scripts Architecture

**Primary Scripts:**
- `llms-txt-scraper.py` - **Main workhorse** - Downloads from 170+ llms.txt sites in parallel
- `extract_docs.py` - Git repository cloner/extractor (15 repositories)
- `update.sh` - Master orchestrator that runs all update scripts sequentially

**Discovery Scripts** (research tools, not run automatically):
- `discover-llms-txt-sites.py` - Multi-API discovery (Brave, Exa, Tavily)
- `discover-llms-txt-serper.py` - Serper API-based discovery
- Various sidebar extractors for specific sites

## Common Development Workflows

### Update All Documentation

```bash
# Run master update script
./update-scripts/update.sh

# This executes in order:
# 1. extract_docs.py (15 Git repositories)
# 2. claude-code-sdk-docs.py
# 3. llms-txt-scraper.py (170 sites in parallel)
```

### Update Specific llms.txt Sites

```bash
# Update single site
python3 update-scripts/llms-txt-scraper.py --site anthropic

# Update multiple sites
python3 update-scripts/llms-txt-scraper.py --site vercel-ai-sdk --site langchain

# Force re-download (ignore 23hr cache)
python3 update-scripts/llms-txt-scraper.py --force

# Control parallelism
python3 update-scripts/llms-txt-scraper.py --workers 20

# Download modes
python3 update-scripts/llms-txt-scraper.py --mode full        # Only llms-full.txt
python3 update-scripts/llms-txt-scraper.py --mode individual  # Only individual .md files
python3 update-scripts/llms-txt-scraper.py --mode both        # Default: both files
```

### Add New llms.txt Site

1. **Add to YAML configuration:**
   ```bash
   # Edit update-scripts/llms-sites.yaml
   # Add new entry in alphabetical order:
   - name: new-site-name
     base_url: https://example.com/
     description: Site description
   ```

2. **Download documentation:**
   ```bash
   python3 update-scripts/llms-txt-scraper.py --site new-site-name
   ```

3. **Verify extraction:**
   ```bash
   ls -lh llms-txt-docs/new-site-name/
   grep -l '```' llms-txt-docs/new-site-name/*.md | wc -l  # Check for code examples
   ```

### Remove Sites with No Documentation

When sites don't have working llms.txt files:

```bash
# Create cleanup script
cat > /tmp/remove-empty-sites.py << 'EOF'
import yaml
from pathlib import Path

config_file = Path('update-scripts/llms-sites.yaml')
docs_dir = Path('llms-txt-docs')

with open(config_file) as f:
    config = yaml.safe_load(f)

empty_sites = []
for site in config['sites']:
    site_dir = docs_dir / site['name']
    if not site_dir.exists() or len(list(site_dir.glob('*.md'))) == 0:
        empty_sites.append(site['name'])

print(f"Found {len(empty_sites)} sites with no documentation")
print('\n'.join(empty_sites))

# Remove from config
config['sites'] = [s for s in config['sites'] if s['name'] not in empty_sites]

with open(config_file, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)
EOF

python3 /tmp/remove-empty-sites.py
```

### Rename Incorrectly Named Folders

When generic folder names like `docs-*` need proper site names:

```python
import yaml
from pathlib import Path

renames = {
    'docs-5': 'apify',
    'docs-10': 'litellm',
    # ... more renames
}

# Update YAML
config_file = Path('update-scripts/llms-sites.yaml')
with open(config_file) as f:
    config = yaml.safe_load(f)

for site in config['sites']:
    if site['name'] in renames:
        site['name'] = renames[site['name']]

config['sites'] = sorted(config['sites'], key=lambda x: x['name'])

with open(config_file, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

# Rename directories
docs_dir = Path('llms-txt-docs')
for old_name, new_name in renames.items():
    old_dir = docs_dir / old_name
    new_dir = docs_dir / new_name
    if old_dir.exists() and not new_dir.exists():
        old_dir.rename(new_dir)
```

## File-Level Caching System

The scraper implements smart caching to avoid redundant downloads:

- **Cache Duration**: 23 hours (configurable in `is_file_recent()`)
- **Behavior**: Files downloaded within last 23 hours are skipped unless `--force` is used
- **Logging**: Shows skip reason with file age: `"⏭ Skipping file.md: Downloaded 5.2h ago"`
- **Override**: Use `--force` flag to re-download all files regardless of age

This reduces server load and speeds up incremental updates from hours to minutes.

## Parallel Download Strategy

The scraper uses Python's `ThreadPoolExecutor` for concurrent downloads:

- **Default workers**: 15 concurrent threads
- **Thread-safe printing**: All console output uses `print_lock` to prevent garbled output
- **Error handling**: Individual site failures don't stop the entire run
- **Progress tracking**: Real-time status updates for each site as downloads complete

Typical performance: **170 sites downloaded in ~5-10 minutes** (vs. 2+ hours serial).

## Quality Verification

After downloading documentation, verify completeness:

```bash
# Check file sizes (small files may be incomplete)
ls -lh llms-txt-docs/*/[a-z]*.md | awk '{print $5, $9}' | sort -h | tail -20

# Count total files per site
for dir in llms-txt-docs/*; do
    echo "$(basename $dir): $(find $dir -name '*.md' | wc -l) files"
done

# Check for code examples (should have ```  markers)
grep -l '```' llms-txt-docs/anthropic/*.md | wc -l

# Verify source headers are present
grep -L "^# Source:" llms-txt-docs/vercel-ai-sdk/*.md
```

**Expected characteristics:**
- Files should have `# Source: URL` headers at the top
- Code-heavy docs should contain ``` markers
- Critical files (API references) typically >15KB
- No extraction artifacts like `javascript:void(0)` or CSS class names

## Git Workflow

### Committing Documentation Updates

When adding/updating large documentation sets:

```bash
# Stage changes
git add llms-txt-docs/ github-scraped-docs/ web-scraped-docs/ update-scripts/

# Commit with descriptive message
git commit -m "Update documentation sources

- Updated llms.txt sites in llms-txt-docs/
- Updated Git repos in github-scraped-docs/
- Updated web scrapers in web-scraped-docs/"

# Push (may encounter GitHub secret scanning)
git push origin master
```

### Handling GitHub Push Protection

If push fails due to test API keys in documentation:

```bash
# Identify secrets from error message
# Example: Discord bot token at line 32 in bun/discordjs.md

# Redact exact secret values
sed -i 's/NzkyNzE1NDU0MTk2MDg4ODQy\.X-hvzA\.Ovy4MCQywSkoMRRclStW4xAYK7I/DISCORD_TOKEN_REDACTED/g' llms-txt-docs/bun/discordjs.md

# Amend commit with redactions
git add llms-txt-docs/bun/discordjs.md
git commit --amend --no-edit

# Push again
git push origin master
```

**Common test credentials to redact:**
- Stripe test keys: `sk_test_[A-Za-z0-9]{24,}`
- Discord bot tokens: Long base64-like strings
- API proxy passwords: `auto_[a-z0-9]{32}`

## Discovery Workflow

When expanding the documentation catalog:

1. **Discover new sites** using multi-API search:
   ```bash
   python3 update-scripts/discover-llms-txt-sites.py
   # Uses: Brave Search, Exa AI, Tavily, Serper (fallback)
   ```

2. **Extract unique URLs** from search results

3. **Add to YAML** with proper metadata:
   ```python
   # Generate site names from URLs
   def generate_site_name(url):
       domain = urlparse(url).netloc.replace('www.', '')
       return re.sub(r'[^a-z0-9-]', '', domain.lower())
   ```

4. **Test download** on new sites:
   ```bash
   python3 update-scripts/llms-txt-scraper.py --site new-site --mode both
   ```

5. **Clean up failures** - remove sites with 404s or empty content

## Special Cases

### Git-Based Documentation Extraction

Uses `extract_docs.py` with git clone instead of HTTP downloads for 15 repositories:

```bash
# Run all Git extractions
python3 update-scripts/extract_docs.py

# Configuration examples in repo_config.yaml:
# - CircuitPython: adafruit/circuitpython (docs/)
# - FastAPI: fastapi/fastapi (docs/en/docs/)
# - Go: golang/website (_content/)
# - Python: python/cpython (Doc/, branch: 3.13)
# - SQLAlchemy: sqlalchemy/sqlalchemy (doc/build/)
```

**Why Git extraction over llms.txt:**
- More detailed/comprehensive documentation
- Access to unreleased docs (specific branches)
- Better structured source files
- Full control over extraction process

### Claude Code SDK (Custom HTML Scraper)

Downloads from Anthropic docs with live sidebar extraction:

```bash
python3 update-scripts/claude-code-sdk-docs.py
# Parses sidebar for complete file list
# Downloads as markdown using pandoc if available
```

## Repository Statistics

Current scale:
- **170 active llms.txt sites** in YAML configuration (`llms-txt-docs/`)
- **233 documentation directories** in llms-txt-docs/
- **15 Git-based repository extractions** in `github-scraped-docs/`
- **5 web-scraped documentation sets** in `web-scraped-docs/`
- **12,000+ markdown/RST files** across all sources
- **300MB+ total documentation** optimized for AI consumption

### Directory Structure
```
llm-code-docs/
├── llms-txt-docs/           # llms.txt standard docs (233 sites)
├── github-scraped-docs/     # Git repository extractions (15 repos)
├── web-scraped-docs/        # Custom web scrapers (5 sets)
└── update-scripts/          # All extraction and update scripts
```

### Notable Additions (2025-11-24)
- **llms.txt sites**: Gradio (272KB), Vite (480KB), Ant Design (1.2MB), Ollama (592KB), React (3.1MB)
- **Git repos**: Click (280KB), FastAPI (19MB), Flask (992KB), SQLAlchemy (6.2MB), Go (197MB), Python 3.13 (18MB), Goose (37MB)
- **Total new docs**: 255MB+ across 4,675+ files
- **Reorganization**: Moved all docs into organized subdirectories

Updated: 2025-11-24

## Key Design Principles

1. **Idempotent updates** - Re-running scripts is safe and efficient
2. **Fail-soft** - Individual site failures don't stop bulk operations
3. **Smart caching** - Avoid redundant downloads with time-based freshness checks
4. **Parallel execution** - Maximize throughput with concurrent workers
5. **Quality verification** - Post-download checks ensure complete content capture
6. **Git-friendly naming** - Descriptive folder names, not generic "docs-N" patterns
- llms.txt are considered of better/higher priority than github derived docs