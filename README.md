# LLM Code Documentation Repository

Centralized, AI-readable documentation extracted from 598+ frameworks, libraries, and developer tools. Automated extraction tools keep documentation current with upstream sources.

## Repository Structure

```
llm-code-docs/
├── docs/
│   ├── llms-txt/           # 339 sites following llms.txt standard (HIGHEST PRIORITY)
│   ├── github-scraped/     # 136 Git repository extractions
│   ├── web-scraped/        # 122 web-scraped documentation sources
│   └── github-repos/       # Individual GitHub repo docs
├── scripts/                # All extraction and update tools
├── AGENTS.md               # Guide for AI agents using these docs
├── CLAUDE.md               # AI assistant instructions
├── index.yaml              # Index of all documentation sources
└── README.md               # This file
```

## For AI Agents

See [AGENTS.md](./AGENTS.md) for detailed guidance on finding and using documentation in this repository.

## Documentation Sources

### llms.txt Standard Sites (`docs/llms-txt/`)

**339 sites** following the [llms.txt standard](https://llmstxt.org/) - optimized for LLM consumption.

Notable sources include:
- **AI/LLM**: Anthropic, OpenAI, Vercel AI SDK, LangChain, Ollama
- **Web Frameworks**: Next.js, React, Vue, Astro, Remix, SvelteKit
- **Python**: FastAPI, Pydantic, Streamlit, Gradio
- **JavaScript**: Bun, Deno, Vite, Vitest, Zod
- **Databases**: Supabase, PlanetScale, Turso, Neon
- **Infrastructure**: Cloudflare, Vercel, Fly.io, Railway

### Git Repository Extractions (`docs/github-scraped/`)

**136 repositories** cloned and extracted for comprehensive documentation, including:

| Category | Examples |
|----------|----------|
| AI/ML | vLLM, TensorRT-LLM, Whisper, Stable Diffusion, RAGFlow, FAISS |
| Python | FastAPI, Flask, Celery, Gunicorn, HTTPX, Matplotlib |
| JavaScript | ESLint, Jest, Express, Electron, Mermaid, XtermJS |
| Go | Go docs, gopls, golangci-lint, Delve, govulncheck |
| DevOps | Caddy, Trivy, Steampipe, SearXNG, WasmEdge |
| Language Servers | Neovim, nvim-lspconfig, pygls, vscode-languageserver |

### Web-Scraped Documentation (`docs/web-scraped/`)

**122 sources** scraped from documentation sites without llms.txt support, including:
- **Cloud APIs**: AWS SDK, Google Cloud, Azure IoT, Datadog, Sentry
- **UI Libraries**: Emotion, Formik, Storybook, React Flow, Excalidraw
- **Dev Tools**: DBeaver, Dependabot, Semgrep, Percy, Chromatic
- **AI/ML**: GPT4All, Lepton AI, Ultralytics YOLOv8, Magenta

## Quick Start

### Update All Documentation

```bash
./scripts/update.sh
```

### Update Specific Sources

```bash
# Update all llms.txt sites (339 sites in parallel)
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

- **339** llms.txt documentation sites
- **136** Git repository extractions
- **122** web-scraped documentation sources
- **43,000+** markdown/RST files
- **5.4GB** total documentation

## Contributing

### Add a New llms.txt Site

1. Check if the site has llms.txt support (visit `{docs-url}/llms.txt`)
2. Edit `scripts/llms-sites.yaml` with the new entry
3. Run `python3 scripts/llms-txt-scraper.py --site new-site`
4. Verify extraction: `ls -lh docs/llms-txt/new-site/`

### Add a GitHub Repository

1. Edit `scripts/repo_config.yaml` with repo details
2. Run `python3 scripts/extract_docs.py`

### Suggest a Library

Check `index.yaml` under `not_yet_fetched` for libraries we've identified but haven't extracted.

**Priority order:**
1. **llms.txt** - Highest quality, official AI-optimized format
2. **Git repos** - Comprehensive but requires custom configuration
3. **Web scraping** - Last resort for critical documentation

---

Maintained for AI-assisted development across multiple frameworks and tools.
