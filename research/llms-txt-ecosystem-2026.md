# Research: llms.txt Ecosystem & Adoption (2026)

## Executive Summary

As of March 2026, the llms.txt standard (proposed September 2024) has achieved **grassroots adoption** with 784+ websites implementing it, but **zero major LLM providers officially support it**. The ecosystem divides clearly into:

- **4 platforms with native/automatic support** (auto-generates for all hosted sites)
- **12+ frameworks with official/community plugins** (requires setup/installation)
- **20+ generators and integration tools** (CLI, GitHub Actions, crawlers, CMS modules)

Adoption surged in November 2024 when **Mintlify** rolled out automatic generation across its entire platform, instantly creating llms.txt for thousands of documentation sites.

---

## 1. Platforms with Native/Automatic Support

These platforms **automatically generate llms.txt** for all hosted documentation without user setup:

### Enterprise Documentation Platforms (Auto-generates)

| Platform | Support Type | Auto-generates | Notes |
|----------|-------------|---|---|
| **Mintlify** | Native | ✅ All sites | Rolled out Nov 2024; generated `/llms.txt`, `/llms-full.txt`, `.md` versions. Collaborated with Anthropic on llms-full.txt structure. **Adoption catalyst** — triggered thousands of sites overnight |
| **Fern** | Native | ✅ All sites | Full native integration; generates token-optimized files |
| **ReadMe** | Native | ✅ All sites | Automatic generation across platform |

### Framework with Built-in Support

| Framework | Support Type | Auto-generates | Notes |
|-----------|-------------|---|---|
| **Drupal 10.3+** | Native Recipe | ✅ Yes | "A Drupal Recipe providing full support for the llms.txt proposal" — built into CMS itself |
| **nbdev** | Native | ✅ Yes | "All projects automatically create `.md` versions of pages by default" |
| **FastHTML** | Native | ✅ Yes | Documentation follows both `/llms.txt` and `.md` file proposals |

### CMS with Native Support

| CMS | Support Type | Auto-generates | Notes |
|-----|-------------|---|---|
| **WordPress** | Native (Yoast SEO) | ✅ Yes | Yoast SEO v25.6+ auto-generates llms.txt files; widely used by WordPress sites |

---

## 2. Documentation Frameworks with Official/Popular Plugins

These require installation/setup but are maintained as **official or heavily-adopted community plugins**:

### Docusaurus Ecosystem (3 plugins)

| Plugin | Status | Stars | Notes |
|--------|--------|-------|-------|
| **docusaurus-plugin-llms** | Official | ✅ Community | Generates concatenated markdown from documentation under `/llms.txt` following llmstxt.org standard |
| **docusaurus-plugin-llms-txt** | Community | ✅ Popular | Din0s version: generates concatenated markdown file; actively maintained |

### VitePress Ecosystem (1 plugin)

| Plugin | Status | Stars | Notes |
|--------|--------|-------|-------|
| **vitepress-plugin-llms** | Community | ✅ Popular | Okineadev: generates LLM-friendly documentation. Creates `/llms.txt` (main file with links), `/llms-full.txt` (complete markdown), and `.md` versions of individual pages |

### MkDocs Ecosystem (1 plugin)

| Plugin | Status | Package | Notes |
|--------|--------|---------|-------|
| **mkdocs-llmstxt** | Community | ✅ PyPI | Pawamoy: `pip install mkdocs-llmstxt`; generates `/llms.txt` |

### Astro Ecosystem (2 plugins)

| Plugin | Status | Stars | Notes |
|--------|--------|-------|-------|
| **astro-llms-txt** | Community | ✅ Popular | 4hse: Minimal generator plugin |
| **astro-llms-generate** | Community | ✅ Popular | ColdranAI: auto-discovers and processes all pages; generates `/llms.txt` (smart index), `/llms-small.txt` (structure-only), `/llms-full.txt` (complete markdown) |

### Next.js / Full-Stack Frameworks

| Plugin | Status | Framework | Notes |
|--------|--------|-----------|-------|
| **Fumadocs** | Framework-Based | Next.js | Does NOT auto-generate; provides building blocks requiring custom implementation. Teams must "configure routes and maintain the integration themselves" |
| **Scalar** | Framework-Based | Flexible | Does NOT auto-generate; framework-based approach requiring custom setup |

---

## 3. Generators, Crawlers & Integration Tools

### Command-Line Tools & Libraries

| Tool | Language | Purpose | Status |
|------|----------|---------|--------|
| **llmstxt-cli** | CLI/Node | Install llms.txt docs as skills into 35+ AI coding agents | Active |
| **llms-txt-php** | PHP | Library for writing/reading llms.txt Markdown files | Community maintained |
| **llms_txt2ctx** | Python | CLI tool + Python module for parsing llms.txt files | Active |
| **llm-docs-builder** | Ruby | Transform/optimize markdown docs for LLMs | 79 GitHub stars |

### Web Crawlers & Generators

| Tool | Source | Technology | Notes |
|------|--------|-----------|-------|
| **Apify llms.txt Generator Actor** | Apify | Web scraper | Extracts website content; outputs available in Key-Value Store; supports deep crawls |
| **Firecrawl llms.txt Generator** | Firecrawl | Web scraper | Scrapes websites to generate llms.txt; simplest web-based approach |
| **dotenvx llmstxt** | dotenvx | CLI | Generates llms.txt using site's sitemap.xml |
| **llmoptimizer** | Generator | Multi-framework | Supports Next.js, Vite, Nuxt, Astro, Remix |

### CI/CD & Automation

| Tool | Platform | Purpose |
|------|----------|---------|
| **llms-txt-action** | GitHub Actions | Automates llms.txt creation in CI/CD |
| **llms-txt-generator** | MCP-enabled | AI-powered generation with Model Context Protocol support |

### IDE & Browser Extensions

| Tool | Type | Purpose |
|------|------|---------|
| **llmstxt Checker** | Chrome Extension | Verify website llms.txt implementation |
| **VS Code Extension** (vscode-llms-txt) | IDE Plugin | Search/explore llms.txt files directly in editor |
| **VS Code PagePilot** | IDE Plugin | Chat participant that auto-loads external context |
| **Raycast Extension** | Launcher | llms.txt discovery within Raycast |

### Integration Platforms

| Tool | Type | Purpose |
|------|------|---------|
| **MCP Explorer** | Protocol | Explore/analyze llms.txt using Model Context Protocol |
| **CrewAI** | AI Framework | AI-powered collaboration with llms.txt documentation support |
| **Fireworks AI** | Inference | Model deployment service offering llms.txt endpoints |

---

## 4. Early Adopter Sites (November 2024+)

The following major companies/products now have llms.txt files:

**Via Mintlify rollout (Nov 2024):**
- Anthropic
- Cursor
- Cloudflare
- Vercel
- Stripe
- Zapier
- Supabase
- ElevenLabs
- Shopify
- Hugging Face
- Pinecone
- NVIDIA

---

## 5. Adoption Statistics & Barriers

### Current Adoption

| Metric | Status | Source |
|--------|--------|--------|
| **Total sites with llms.txt** | 784+ | Grassroots tracking |
| **Adoption rate (sample)** | 10.13% | Analysis of 300K domains |
| **LLM providers officially using it** | 0 | As of 2026 |

### Major Barriers

1. **Zero LLM provider commitment** — No major AI company (OpenAI, Google, Meta, Anthropic via product) has officially announced they crawl/use llms.txt
2. **Google explicitly rejected it** — Compared to discredited keywords meta tag
3. **No measurable traffic impact** — 8/9 sites saw no traffic change after implementation
4. **No AI crawler acknowledgment** — None of the major AI crawlers have publicly claimed they extract via llms.txt

### Current State (March 2026)

**Not dead, but precarious:** The standard survives due to:
- Grassroots developer enthusiasm
- Practical utility for AI agent tooling (not LLM inference)
- Expected future CMS/platform adoption (reducing manual effort)

---

## 6. Summary: Native vs Plugin vs Generator

### Native Support (Automatic for all users)
**Count: 7**
- Mintlify ⭐ (adoption catalyst Nov 2024)
- Fern
- ReadMe
- Drupal 10.3+
- WordPress (Yoast SEO v25.6+)
- nbdev
- FastHTML

### Official/Popular Plugins (Framework-level, requires install)
**Count: 8**
- Docusaurus: docusaurus-plugin-llms (+ 1 community variant)
- VitePress: vitepress-plugin-llms
- MkDocs: mkdocs-llmstxt
- Astro: astro-llms-txt, astro-llms-generate
- Next.js: Fumadocs (framework-based, not auto)
- Scalar (framework-based, not auto)

### Generators & Tools (One-off or external)
**Count: 20+**
- CLI/libraries: 4 (llmstxt-cli, llms-txt-php, llms_txt2ctx, llm-docs-builder)
- Web crawlers: 4 (Apify, Firecrawl, dotenvx, llmoptimizer)
- CI/CD: 2 (GitHub Actions, MCP-enabled)
- Extensions: 4 (Chrome, VS Code x2, Raycast)
- Integrations: 3+ (MCP Explorer, CrewAI, Fireworks AI)

---

## 7. Key Timeline

| Date | Event |
|------|-------|
| Sept 2024 | llms.txt standard proposed by Jeremy Howard (Answer.AI) |
| Nov 2024 | **Mintlify rolls out automatic support** — adoption explodes |
| Dec 2024 - Mar 2026 | Framework plugins appear (Docusaurus, VitePress, MkDocs, Astro) |
| 2026 | CMS plugins expand (WordPress Yoast); generator ecosystem grows |

---

## 8. Sources

### Official Resources
- [llmstxt.org](https://llmstxt.org/) — Official specification
- [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) — Directory of implementations (729 ⭐)
- [llmstxthub.com](https://llmstxthub.com/) — Directory of AI-ready documentation

### Platform Articles
- [Fern: Best llms.txt Implementation Platforms](https://buildwithfern.com/post/best-llms-txt-implementation-platforms-ai-discoverable-apis)
- [Mintlify: What is llms.txt?](https://www.mintlify.com/blog/what-is-llms-txt)

### Adoption Analysis
- [Is llms.txt Dead? Current State 2025](https://llms-txt.io/blog/is-llms-txt-dead)
- [llms.txt in 2026: What It Does (and Doesn't) Do](https://searchsignal.online/blog/llms-txt-2026)
- [Should Websites Implement llms.txt in 2026?](https://www.linkbuildinghq.com/blog/should-websites-implement-llms-txt-in-2026/)
- [llms.txt for Websites: Complete 2026 Guide](https://www.bigcloudy.com/blog/what-is-llms-txt/)
- [What is llms.txt? 2026 Guide](https://www.bluehost.com/blog/what-is-llms-txt/)
- [Ahrefs: What Is llms.txt, and Should You Care About It?](https://ahrefs.com/blog/what-is-llms-txt/)

### GitHub & Tools
- [GitHub Topic: llms-txt](https://github.com/topics/llms-txt) — All 118+ repos tagged with llms-txt
- [GitHub: pawamoy/mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt)
- [GitHub: okineadev/vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms)
- [GitHub: rachfop/docusaurus-plugin-llms](https://github.com/rachfop/docusaurus-plugin-llms)
- [GitHub: din0s/docusaurus-plugin-llms-txt](https://github.com/din0s/docusaurus-plugin-llms-txt)
- [GitHub: 4hse/astro-llms-txt](https://github.com/4hse/astro-llms-txt)
- [GitHub: ColdranAI/astro-llms-generate](https://github.com/ColdranAI/astro-llms-generate)
- [GitHub: apify/actor-llmstxt-generator](https://github.com/apify/actor-llmstxt-generator)
- [GitHub: WP-Autoplugin/llms-txt-for-wp](https://github.com/WP-Autoplugin/llms-txt-for-wp)

---

## Analysis: What This Means

### For auto-doc Pipeline

**Relevant Findings:**
1. **Mintlify is the dominant platform** for automatic generation — if we're scraping docs, Mintlify-hosted sites will already have `/llms.txt`, `/llms-full.txt`, and `.md` versions available.
2. **Plugin adoption is framework-specific** — we should prioritize discovering:
   - Docusaurus sites (2 plugins available)
   - VitePress sites (1 plugin)
   - MkDocs sites (1 plugin)
   - Astro sites (2 plugins)
3. **WordPress adds llms.txt capability** via Yoast SEO v25.6+ — potentially thousands of sites could generate these files automatically.
4. **No major LLM provider supports it yet** — llms.txt is primarily useful for AI agents and tooling, not for training data or LLM context windows.
5. **Zero official adoption is a red flag** — the 784 grassroots sites are valuable for agent discovery, but this is NOT a standard Google, OpenAI, or Anthropic respect.

### Integration Points for auto-doc

- **Query all llms.txt-hub discovery data** for documentation sites with explicit llms.txt support
- **Check for llms.txt on discovered sites** as a high-confidence signal of structured documentation
- **Leverage framework-specific plugins** when discovering Docusaurus/VitePress/MkDocs/Astro sites
- **Consider post-processing with llms.txt generator** for final output standardization (optional)
