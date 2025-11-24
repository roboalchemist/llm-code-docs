# LLM Code Documentation Repository

Centralized, AI-readable documentation extracted from 175+ frameworks, libraries, and developer tools. Automated extraction tools keep documentation current with upstream sources.

## Repository Structure

```
llm-code-docs/
├── docs/
│   ├── llms-txt/           # 238 sites following llms.txt standard (HIGHEST PRIORITY)
│   ├── github-scraped/     # 15 Git repository extractions
│   └── web-scraped/        # Custom web scrapers (Claude Code SDK, READMEs)
├── scripts/                # All extraction and update tools
├── CLAUDE.md               # AI assistant instructions
├── libraries-to-add.md     # Tracking list for future additions
└── README.md               # This file
```

## Documentation Sources

### llms.txt Standard Sites (`docs/llms-txt/`)

**238 sites** following the [llms.txt standard](https://llmstxt.org/) - optimized for LLM consumption.

Notable sources include:
- **AI/LLM**: Anthropic, OpenAI, Vercel AI SDK, LangChain, Ollama
- **Web Frameworks**: Next.js, React, Vue, Astro, Remix, SvelteKit
- **Python**: FastAPI, Pydantic, Streamlit, Gradio
- **JavaScript**: Bun, Deno, Vite, Vitest, Zod
- **Databases**: Supabase, PlanetScale, Turso, Neon
- **Infrastructure**: Cloudflare, Vercel, Fly.io, Railway

### Git Repository Extractions (`docs/github-scraped/`)

**15 repositories** cloned and extracted for comprehensive documentation:

| Project | Description |
|---------|-------------|
| CircuitPython | MicroPython for microcontrollers |
| MicroPython | Python for microcontrollers |
| Textual | Modern TUI framework |
| FastAPI | Modern Python web framework |
| Flask | Lightweight WSGI framework |
| Click | Python CLI framework |
| SQLAlchemy | Python SQL toolkit and ORM |
| Go | Official Go documentation |
| Python 3.13 | Official Python documentation |
| Goose | AI-powered developer agent |
| LibreChat | Multi-AI chat interface |
| Joplin | Note-taking application |
| BuildBuddy | Remote execution platform |
| esptool | ESP bootloader utility |

### Web-Scraped Documentation (`docs/web-scraped/`)

Custom scrapers for sites without llms.txt support:
- **Claude Code SDK** - Anthropic's Claude Code development tools
- **READMEs** - Individual README files from various projects

## Quick Start

### Update All Documentation

```bash
./scripts/update.sh
```

### Update Specific Sources

```bash
# Update all llms.txt sites (238 sites in parallel)
python3 scripts/llms-txt-scraper.py

# Update single site
python3 scripts/llms-txt-scraper.py --site anthropic

# Update Git repository extractions
python3 scripts/extract_docs.py

# Update Claude Code SDK docs
python3 scripts/claude-code-sdk-docs.py
```

### Add New llms.txt Site

1. Edit `scripts/llms-sites.yaml`:
   ```yaml
   - name: new-site
     base_url: https://example.com/
     description: Site description
   ```

2. Download:
   ```bash
   python3 scripts/llms-txt-scraper.py --site new-site
   ```

## Configuration

### llms.txt Sites (`scripts/llms-sites.yaml`)

Central registry of all llms.txt-compliant documentation sources. Each entry specifies:
- `name` - Unique identifier and output folder name
- `base_url` - URL where llms.txt is located
- `description` - Brief description of the documentation
- `rate_limit_seconds` (optional) - Delay between requests

### Git Repositories (`scripts/repo_config.yaml`)

Configuration for Git-based documentation extraction:
- `repo_url` - GitHub repository URL
- `source_folder` - Path to documentation within repo
- `target_folder` - Output path under `docs/github-scraped/`
- `branch` - Branch to clone (default: main/master)

## Features

- **Smart Caching**: 23-hour freshness window avoids redundant downloads
- **Parallel Downloads**: 15 concurrent workers for fast bulk updates
- **Source Headers**: Each file includes source URL for traceability
- **Error Resilience**: Individual failures don't stop bulk operations

## Statistics

- **238** llms.txt documentation sites
- **15** Git repository extractions
- **12,000+** markdown/RST files
- **300MB+** total documentation

## Adding Documentation

See `libraries-to-add.md` for tracked libraries awaiting documentation.

Priority order:
1. **llms.txt** - Highest quality, official AI-optimized format
2. **Git repos** - Comprehensive but requires custom configuration
3. **Web scraping** - Last resort for critical documentation

---

Maintained for AI-assisted development across multiple frameworks and tools.
