# Agent Instructions for llm-code-docs

This file helps AI agents find and use documentation from this repository effectively.

## Quick Start

This repository contains **300MB+ of AI-optimized documentation** for 200+ libraries and frameworks. Documentation is organized by extraction source:

| Directory | Count | Description |
|-----------|-------|-------------|
| `docs/llms-txt/` | 172+ sites | llms.txt standard docs (highest quality) |
| `docs/github-scraped/` | 15 repos | Git repository extractions |
| `docs/web-scraped/` | 2 sources | Custom web scraping |

## Finding Documentation

### By Library Name

Most documentation directories match the library/framework name:

```bash
# React docs
docs/llms-txt/react/

# FastAPI docs
docs/github-scraped/fastapi/

# LangChain docs
docs/llms-txt/langchain/

# Anthropic/Claude docs
docs/llms-txt/anthropic/
```

### By Category

**AI/ML Frameworks:**
- `docs/llms-txt/anthropic/` - Claude AI
- `docs/llms-txt/langchain/` - LangChain Python
- `docs/llms-txt/langchain-js/` - LangChain JavaScript
- `docs/llms-txt/langgraph/` - LangGraph agents
- `docs/llms-txt/crewai/` - CrewAI multi-agent
- `docs/llms-txt/litellm/` - LiteLLM proxy
- `docs/llms-txt/ollama/` - Ollama local LLMs
- `docs/llms-txt/groq/` - Groq inference
- `docs/github-scraped/goose/` - Goose AI agent

**Web Frameworks:**
- `docs/github-scraped/fastapi/` - FastAPI
- `docs/github-scraped/flask/` - Flask
- `docs/llms-txt/nextjs/` - Next.js
- `docs/llms-txt/nuxt/` - Nuxt.js
- `docs/llms-txt/astro/` - Astro

**Frontend:**
- `docs/llms-txt/react/` - React
- `docs/llms-txt/vuejs/` - Vue.js
- `docs/llms-txt/vite/` - Vite
- `docs/llms-txt/ant-design/` - Ant Design
- `docs/llms-txt/gradio/` - Gradio

**Databases & ORMs:**
- `docs/github-scraped/sqlalchemy/` - SQLAlchemy
- `docs/llms-txt/prisma/` - Prisma
- `docs/llms-txt/redis/` - Redis
- `docs/llms-txt/turso/` - Turso SQLite
- `docs/llms-txt/pinecone/` - Pinecone vectors

**Infrastructure:**
- `docs/llms-txt/cloudflare/` - Cloudflare
- `docs/llms-txt/vercel/` - Vercel
- `docs/llms-txt/stripe/` - Stripe payments

**CLI/TUI:**
- `docs/github-scraped/click/` - Click CLI
- `docs/github-scraped/textual/` - Textual TUI
- `docs/llms-txt/bun/` - Bun runtime

**Languages:**
- `docs/github-scraped/python-docs/` - Python 3.13
- `docs/github-scraped/go-docs/` - Go language

## Using Documentation

### File Structure

Each documentation source has its own structure:

**docs/llms-txt:**
```
docs/llms-txt/anthropic/
├── llms.txt           # Index file
├── llms-full.txt      # Combined documentation (if available)
├── overview.md        # Individual doc pages
├── api-reference.md
└── ...
```

**docs/github-scraped:**
```
docs/github-scraped/fastapi/
├── docs/              # Original doc structure preserved
│   ├── en/
│   │   └── docs/
│   │       ├── index.md
│   │       └── ...
```

### Recommended Reading Order

1. **Start with `llms.txt`** - Contains doc overview and structure
2. **Check `llms-full.txt`** - Combined single-file version (if exists)
3. **Read specific files** - For detailed topics

### Example: Finding API Information

```bash
# For Claude/Anthropic API
grep -r "messages" docs/llms-txt/anthropic/

# For FastAPI endpoints
grep -r "@app.get" docs/github-scraped/fastapi/

# For React hooks
grep -r "useState\|useEffect" docs/llms-txt/react/
```

## Index Reference

Check `index.yaml` in the repository root for:
- Complete list of all documentation sources
- Status of each source (fetched, partial, not_yet)
- URLs and descriptions
- Paths to documentation directories

## Documentation Quality Tiers

1. **Tier 1 (Best)**: `docs/llms-txt/` - Optimized for LLM consumption
2. **Tier 2 (Good)**: `docs/github-scraped/` - Complete but may need filtering
3. **Tier 3 (Varies)**: `docs/web-scraped/` - Custom extraction, quality varies

## Common Tasks

### Find All Docs for a Topic
```bash
grep -rl "authentication\|auth\|oauth" docs/llms-txt/ docs/github-scraped/
```

### List Available Frameworks
```bash
ls docs/llms-txt/
ls docs/github-scraped/
```

## Notes for Agent Developers

- **Prefer docs/llms-txt/** when available (higher quality for LLMs)
- **Large frameworks** (FastAPI, Go, Python) are in docs/github-scraped/
- **Check index.yaml** for the complete documentation catalog
- **Code examples** are preserved in markdown code blocks

## Not Yet Available

See `index.yaml` under `not_yet_fetched` for libraries identified but not yet extracted. Common ones include:
- PyTorch, scikit-learn, numpy, pandas
- Playwright, Jest, pytest
- Express, TypeScript
- Tailwind CSS

---

*This repository is updated regularly. Check git log for recent additions.*
