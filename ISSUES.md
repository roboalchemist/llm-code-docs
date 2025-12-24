# DOCS Project Issues

Issue breakdown for the llm-code-docs project. Based on analysis of:
- Current repo implementation (328 sources, 288 fetched)
- Wishlist in `todo.md`
- Joplin planning notes

---

## Completed Issues

### Infrastructure (Done)

| ID | Title | Status |
|----|-------|--------|
| DOCS-1 | Set up base repo structure with docs/, scripts/ directories | done |
| DOCS-2 | Create llms-txt scraper (scripts/llms-txt-scraper.py) | done |
| DOCS-3 | Create update.sh orchestration script | done |
| DOCS-4 | Create index.yaml auto-generation (scripts/update-index.py) | done |
| DOCS-5 | Create GitHub README scraper (scripts/pull-readmes.py) | done |
| DOCS-6 | Set up llms-sites.yaml configuration | done |
| DOCS-7 | Set up repo_config.yaml for GitHub repos | done |
| DOCS-8 | Create CLAUDE.md agent instructions | done |
| DOCS-9 | Create AGENTS.md specialized agent documentation | done |
| DOCS-10 | Create README.md project documentation | done |

### Scrapers (Done)

| ID | Title | Status |
|----|-------|--------|
| DOCS-11 | Create AWS CLI docs scraper (aws-cli-docs.py) | done |
| DOCS-12 | Create Claude Code docs scraper (claude-code-router-docs.py) | done |
| DOCS-13 | Create Electron docs scraper (electron-docs.py) | done |
| DOCS-14 | Create FAISS wiki scraper (faiss-wiki-scraper.py) | done |
| DOCS-15 | Create Graphite docs scraper (graphite-docs.py) | done |
| DOCS-16 | Create HTMX docs scraper (htmx-docs.py) | done |
| DOCS-17 | Create Mistral Vibe docs scraper (mistral-vibe-docs.py) | done |
| DOCS-18 | Create Namecheap docs scraper (namecheap-docs.py) | done |
| DOCS-19 | Create Ntfy docs scraper (ntfy-docs.py) | done |
| DOCS-20 | Create ONNX Runtime docs scraper (onnxruntime-docs.py) | done |
| DOCS-21 | Create OpenWakeWord docs scraper (openwakeword-docs.py) | done |
| DOCS-22 | Create Rustdesk docs scraper (rustdesk-docs.py) | done |
| DOCS-23 | Create Sentence Transformers docs scraper (sentence-transformers-docs.py) | done |
| DOCS-24 | Create Tailwind docs scraper (tailwind-docs.py) | done |
| DOCS-25 | Create Voyage docs scraper (voyage-docs.py) | done |
| DOCS-26 | Create 1Password docs scraper (1password-docs.py) | done |
| DOCS-27 | Create Common Voice docs scraper (common-voice-docs.py) | done |
| DOCS-28 | Create DagsHub docs scraper (dagshub-docs.py) | done |
| DOCS-29 | Create Nemo Framework docs scraper (nemo-framework-docs.py) | done |
| DOCS-30 | Create Nomic docs scraper (nomic-docs.py) | done |
| DOCS-31 | Create Mozilla Data Collective docs scraper (mozilla-data-collective-docs.py) | done |

---

## In Progress / Partial Issues

| ID | Title | Status | Notes |
|----|-------|--------|-------|
| DOCS-32 | Fix failing llms.txt sites | in-progress | 39 of 285 sites failing to fetch |
| DOCS-33 | Discover new llms.txt sites automatically | in-progress | discover-llms-txt-serper.py exists but needs scheduling |

---

## Todo Issues

### Hub Integration (High Priority)

| ID | Title | Priority | Description |
|----|-------|----------|-------------|
| DOCS-34 | Integrate llmstxthub.com as discovery source | high | Scrape https://llmstxthub.com/ for new llms.txt sites |
| DOCS-35 | Integrate thedaviddias/llms-txt-hub | high | Pull from GitHub repo's websites.json |
| DOCS-36 | Integrate SecretiveShell/Awesome-llms-txt | high | Pull from awesome list |
| DOCS-37 | Integrate directory.llmstxt.cloud | high | Scrape directory for sites |
| DOCS-38 | Integrate llmstxt.site | high | Scrape directory for sites |

### Missing Python Libraries (Medium Priority)

| ID | Title | Priority | Source |
|----|-------|----------|--------|
| DOCS-39 | Add PyTorch documentation | medium | pytorch.org |
| DOCS-40 | Add Hugging Face Transformers docs | medium | huggingface.co/docs/transformers |
| DOCS-41 | Add Hugging Face Diffusers docs | medium | huggingface.co/docs/diffusers |
| DOCS-42 | Add OpenAI API documentation | medium | platform.openai.com/docs |
| DOCS-43 | Add scikit-learn documentation | medium | scikit-learn.org |
| DOCS-44 | Add NumPy documentation | medium | numpy.org |
| DOCS-45 | Add Pandas documentation | medium | pandas.pydata.org |
| DOCS-46 | Add Matplotlib documentation | medium | matplotlib.org |
| DOCS-47 | Add LlamaIndex documentation | medium | docs.llamaindex.ai |
| DOCS-48 | Add LangGraph documentation | medium | langchain-ai.github.io/langgraph |
| DOCS-49 | Add LiteLLM documentation | medium | docs.litellm.ai |
| DOCS-50 | Add vLLM documentation | medium | docs.vllm.ai |
| DOCS-51 | Add Pydantic documentation | medium | docs.pydantic.dev |
| DOCS-52 | Add pytest documentation | medium | docs.pytest.org |
| DOCS-53 | Add Playwright documentation | medium | playwright.dev |
| DOCS-54 | Add Typer documentation | medium | typer.tiangolo.com |
| DOCS-55 | Add Rich documentation | medium | rich.readthedocs.io |
| DOCS-56 | Add Requests documentation | medium | docs.python-requests.org |
| DOCS-57 | Add HTTPX documentation | medium | python-httpx.org |
| DOCS-58 | Add tree-sitter documentation | medium | tree-sitter.github.io |
| DOCS-59 | Add Pillow documentation | medium | pillow.readthedocs.io |
| DOCS-60 | Add BeautifulSoup documentation | medium | crummy.com/software/BeautifulSoup |
| DOCS-61 | Add Celery documentation | medium | docs.celeryq.dev |

### Missing Node.js Libraries (Medium Priority)

| ID | Title | Priority | Source |
|----|-------|----------|--------|
| DOCS-62 | Add Jest documentation | medium | jestjs.io |
| DOCS-63 | Add Express documentation | medium | expressjs.com |
| DOCS-64 | Add Webpack documentation | medium | webpack.js.org |
| DOCS-65 | Add TypeScript documentation | medium | typescriptlang.org |
| DOCS-66 | Add React Testing Library docs | medium | testing-library.com |
| DOCS-67 | Add Radix UI documentation | medium | radix-ui.com |
| DOCS-68 | Add Three.js documentation | medium | threejs.org |
| DOCS-69 | Add D3 documentation | medium | d3js.org |
| DOCS-70 | Add Zustand documentation | medium | docs.pmnd.rs/zustand |
| DOCS-71 | Add React Hook Form docs | medium | react-hook-form.com |
| DOCS-72 | Add CodeMirror documentation | medium | codemirror.net/docs |

### Hardware/IoT Documentation (Medium Priority)

| ID | Title | Priority | Source |
|----|-------|----------|--------|
| DOCS-73 | Add Arduino documentation | medium | docs.arduino.cc |
| DOCS-74 | Add Raspberry Pi documentation | medium | raspberrypi.com/documentation |
| DOCS-75 | Add PlatformIO documentation | medium | docs.platformio.org |
| DOCS-76 | Add ESPHome documentation | medium | esphome.io |
| DOCS-77 | Add Home Assistant documentation | medium | home-assistant.io |
| DOCS-78 | Add Tasmota documentation | medium | tasmota.github.io/docs |
| DOCS-79 | Add SparkFun tutorials | medium | learn.sparkfun.com |
| DOCS-80 | Add Seeed Studio wiki | medium | wiki.seeedstudio.com |

### Automation & Infrastructure (Low Priority)

| ID | Title | Priority | Description |
|----|-------|----------|-------------|
| DOCS-81 | Add cron job for daily updates | low | Schedule update.sh to run daily |
| DOCS-82 | Add GitHub Actions for automated updates | low | CI/CD pipeline for doc fetching |
| DOCS-83 | Create MkDocs site discovery scraper | low | Find MkDocs-based documentation sites |
| DOCS-84 | Create Sphinx site discovery scraper | low | Find Sphinx-based documentation sites |
| DOCS-85 | Create Read the Docs discovery | low | Scrape readthedocs.io for projects |
| DOCS-86 | Implement Google dorking for doc discovery | low | Use search operators to find docs |
| DOCS-87 | Add mdream integration for HTML→MD | low | Use mdream for difficult sites |
| DOCS-88 | Add Jina Reader LM for complex sites | low | AI-powered HTML→markdown conversion |
| DOCS-89 | Create site health monitoring dashboard | low | Track success/failure rates over time |
| DOCS-90 | Add deduplication for overlapping sources | low | Handle same docs from multiple sources |

---

## Summary

| Category | Count |
|----------|-------|
| Completed | 31 |
| In Progress | 2 |
| Todo (High Priority) | 5 |
| Todo (Medium Priority) - Python | 23 |
| Todo (Medium Priority) - Node.js | 11 |
| Todo (Medium Priority) - IoT | 8 |
| Todo (Low Priority) | 10 |
| **Total** | **90** |

---

## Current Stats

From `index.yaml`:
- **Total sources**: 328
- **Total fetched**: 288
- **llms.txt**: 285 configured, 246 fetched (86%)
- **GitHub repos**: 28 configured, 27 fetched (96%)
- **Web scraped**: 15 configured, 15 fetched (100%)
