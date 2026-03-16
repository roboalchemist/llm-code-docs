# Source: https://scrapfly.io/docs/scrape-api/proxy-mode/apify

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/proxy-mode/apify

Markdown Content:
How to Use Scrapfly Proxy with Apify | Custom Proxy Integration
===============

[![Image 1: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)Docs](https://scrapfly.io/docs)

Search documentation...⌘K

Ask AI[Sign in](https://scrapfly.io/login)[Get Started](https://scrapfly.io/register)

[Products](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)

[![Image 2](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Server](https://scrapfly.io/docs/mcp/getting-started)[![Image 3](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started)[![Image 4](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/docs/screenshot-api/getting-started)[![Image 5](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/docs/extraction-api/getting-started)[![Image 6](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176) Proxy Saver](https://scrapfly.io/docs/proxy-saver/getting-started)[![Image 7](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/docs/crawler-api/getting-started)

[SDKs](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)

[![Image 8](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/python-icon.svg?version=0.1.176) Python SDK](https://scrapfly.io/docs/sdk/python)[![Image 9](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/typescript-icon.svg?version=0.1.176) TypeScript SDK](https://scrapfly.io/docs/sdk/typescript)[![Image 10](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/golang-icon-transperant.svg?version=0.1.176) Golang SDK](https://scrapfly.io/docs/sdk/golang)[![Image 11](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/scrapy-icon.svg?version=0.1.176) Scrapy SDK](https://scrapfly.io/docs/sdk/scrapy)

[Visual API](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)

[![Image 12](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/dashboard/playground/web-scraper)[![Image 13](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/dashboard/playground/extraction)[![Image 14](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/dashboard/playground/crawler)[![Image 15](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/dashboard/playground/screenshot)[![Image 16](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Playground](https://scrapfly.io/dashboard/playground/mcp)

[Tools](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)

[ScrapeGround](https://scrapfly.io/scrapeground)[web-scraping.dev](https://web-scraping.dev/)[httpbin.dev](https://httpbin.dev/)[JA3 Fingerprinter](https://scrapfly.io/web-scraping-tools/ja3-fingerprint)[HTTP2 Fingerprinter](https://scrapfly.io/web-scraping-tools/http2-fingerprint)

[Academy](https://scrapfly.io/academy)[Changelog](https://scrapfly.io/docs/release-notes)

Dashboard

*   [Intro](https://scrapfly.io/docs)
*   [Project](https://scrapfly.io/docs/project)
*   [Account](https://scrapfly.io/docs/account)
*   [Workspace & Team](https://scrapfly.io/docs/workspace-and-team)
*   [Billing](https://scrapfly.io/docs/billing)

Products

![Image 17](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176)MCP Server NEW

*   [Getting Started](https://scrapfly.io/docs/mcp/getting-started)
*   [Tools & API Spec](https://scrapfly.io/docs/mcp/tools)
*   [Authentication](https://scrapfly.io/docs/mcp/authentication)
*   [Examples & Use Cases](https://scrapfly.io/docs/mcp/examples)
*   [FAQ](https://scrapfly.io/docs/mcp/faq)
*   [Integrations](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#mcp-integrations-collapse)

    *   [Overview](https://scrapfly.io/docs/mcp/integrations)
    *    AI Assistants & Code Editors 
    *   [Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop)
    *   [Claude Code](https://scrapfly.io/docs/mcp/integrations/claude-code)
    *   [ChatGPT](https://scrapfly.io/docs/mcp/integrations/chatgpt)
    *   [Cursor](https://scrapfly.io/docs/mcp/integrations/cursor)
    *   [Cline](https://scrapfly.io/docs/mcp/integrations/cline)
    *   [Windsurf](https://scrapfly.io/docs/mcp/integrations/windsurf)
    *   [Zed](https://scrapfly.io/docs/mcp/integrations/zed)
    *   [Roo Code](https://scrapfly.io/docs/mcp/integrations/roo-code)
    *   [VS Code](https://scrapfly.io/docs/mcp/integrations/vscode)
    *    AI Frameworks & SDKs 
    *   [LangChain](https://scrapfly.io/docs/mcp/integrations/langchain)
    *   [LlamaIndex](https://scrapfly.io/docs/mcp/integrations/llamaindex)
    *   [CrewAI](https://scrapfly.io/docs/mcp/integrations/crewai)
    *   [OpenAI](https://scrapfly.io/docs/mcp/integrations/openai)
    *    No-Code & Automation 
    *   [n8n](https://scrapfly.io/docs/mcp/integrations/n8n)
    *   [Make](https://scrapfly.io/docs/mcp/integrations/make)
    *   [Zapier](https://scrapfly.io/docs/mcp/integrations/zapier)
    *   [Vapi AI](https://scrapfly.io/docs/mcp/integrations/vapi)
    *   [Agent Builder](https://scrapfly.io/docs/mcp/integrations/agent-builder)
    *   [Custom Client](https://scrapfly.io/docs/mcp/integrations/custom-client)

![Image 18](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176)Web Scraping API

*   [Getting started](https://scrapfly.io/docs/scrape-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/scrape-api/specification)
*   [Monitoring](https://scrapfly.io/docs/monitoring)
*   [Customize Request](https://scrapfly.io/docs/scrape-api/custom)
*   [Debug](https://scrapfly.io/docs/scrape-api/debug)
*   [Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)
*   [Proxy](https://scrapfly.io/docs/scrape-api/proxy)
*   [Proxy Mode](https://scrapfly.io/docs/scrape-api/proxy-mode)
*   [Screaming Frog](https://scrapfly.io/docs/scrape-api/proxy-mode/screaming-frog)
*   [Apify](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)
*   [(Auto) Data Extraction](https://scrapfly.io/docs/scrape-api/extraction)
*   [Javascript Rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering)
*   [Javascript Scenario](https://scrapfly.io/docs/scrape-api/javascript-scenario)
*   [SSL](https://scrapfly.io/docs/scrape-api/ssl)
*   [DNS](https://scrapfly.io/docs/scrape-api/dns)
*   [Cache](https://scrapfly.io/docs/scrape-api/cache)
*   [Session](https://scrapfly.io/docs/scrape-api/session)
*   [Webhook](https://scrapfly.io/docs/scrape-api/webhook)
*   [Screenshot](https://scrapfly.io/docs/scrape-api/screenshot)
*   [Errors](https://scrapfly.io/docs/scrape-api/errors)
*   [Timeout](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [Throttling](https://scrapfly.io/docs/throttling)
*   [Troubleshoot](https://scrapfly.io/docs/scrape-api/troubleshoot)
*   [Billing](https://scrapfly.io/docs/scrape-api/billing)
*   [FAQ](https://scrapfly.io/docs/scrape-api/faq)

![Image 19](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176)Crawler API EA

*   [Getting started](https://scrapfly.io/docs/crawler-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/crawler-api/specification)
*   [Retrieving Results](https://scrapfly.io/docs/crawler-api/results)
*   [WARC Format](https://scrapfly.io/docs/crawler-api/warc-format)
*   [Data Extraction](https://scrapfly.io/docs/crawler-api/extraction-rules)
*   [Webhook](https://scrapfly.io/docs/crawler-api/webhook)
*   [Billing](https://scrapfly.io/docs/crawler-api/billing)
*   [Errors](https://scrapfly.io/docs/crawler-api/errors)
*   [Troubleshoot](https://scrapfly.io/docs/crawler-api/troubleshoot)
*   [FAQ](https://scrapfly.io/docs/crawler-api/faq)

![Image 20](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176)Screenshot API

*   [Getting started](https://scrapfly.io/docs/screenshot-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/screenshot-api/specification)
*   [Accessibility Testing](https://scrapfly.io/docs/screenshot-api/accessibility)
*   [Webhook](https://scrapfly.io/docs/screenshot-api/webhook)
*   [Billing](https://scrapfly.io/docs/screenshot-api/billing)
*   [Errors](https://scrapfly.io/docs/screenshot-api/errors)

![Image 21](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176)Extraction API

*   [Getting started](https://scrapfly.io/docs/extraction-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/extraction-api/specification)
*   [Rules Template](https://scrapfly.io/docs/extraction-api/rules-and-template)
*   [LLM Extraction](https://scrapfly.io/docs/extraction-api/llm-prompt)
*   [AI Auto Extraction](https://scrapfly.io/docs/extraction-api/automatic-ai)
*   [Webhook](https://scrapfly.io/docs/extraction-api/webhook)
*   [Billing](https://scrapfly.io/docs/extraction-api/billing)
*   [Errors](https://scrapfly.io/docs/extraction-api/errors)
*   [FAQ](https://scrapfly.io/docs/extraction-api/faq)

![Image 22](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176)Proxy Saver

*   [Getting started](https://scrapfly.io/docs/proxy-saver/getting-started)
*   [Fingerprints](https://scrapfly.io/docs/proxy-saver/fingerprints)
*   [Optimizations](https://scrapfly.io/docs/proxy-saver/optimizations)
*   [SSL Certificates](https://scrapfly.io/docs/proxy-saver/certificates)
*   [Protocols](https://scrapfly.io/docs/proxy-saver/protocols)
*   [Pacfile](https://scrapfly.io/docs/proxy-saver/pacfile)
*   [Secure Credentials](https://scrapfly.io/docs/proxy-saver/security)
*   [Billing](https://scrapfly.io/docs/proxy-saver/billing)

Tools FREE

*   [Antibot Detector](https://scrapfly.io/docs/tools/antibot-detector)

SDK

*   [Golang BETA](https://scrapfly.io/docs/sdk/golang)
*   [Python](https://scrapfly.io/docs/sdk/python)
*   [Typescript NEW](https://scrapfly.io/docs/sdk/typescript)
*   [Scrapy](https://scrapfly.io/docs/sdk/scrapy)

Integrations NEW

*   [Getting Started](https://scrapfly.io/docs/integration/getting-started)
*   [Langchain](https://scrapfly.io/docs/integration/langchain)
*   [LlamaIndex](https://scrapfly.io/docs/integration/llamaindex)
*   [CrewAI](https://scrapfly.io/docs/integration/crewai)
*   [Zapier](https://scrapfly.io/docs/integration/zapier)
*   [Make](https://scrapfly.io/docs/integration/make)
*   [n8n](https://scrapfly.io/docs/integration/n8n)
*   [Agent Skills](https://scrapfly.io/docs/integration/agent-skills)

Dashboard

*   [Intro](https://scrapfly.io/docs)
*   [Project](https://scrapfly.io/docs/project)
*   [Account](https://scrapfly.io/docs/account)
*   [Workspace & Team](https://scrapfly.io/docs/workspace-and-team)
*   [Billing](https://scrapfly.io/docs/billing)

Products

![Image 23](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176)MCP Server NEW

*   [Getting Started](https://scrapfly.io/docs/mcp/getting-started)
*   [Tools & API Spec](https://scrapfly.io/docs/mcp/tools)
*   [Authentication](https://scrapfly.io/docs/mcp/authentication)
*   [Examples & Use Cases](https://scrapfly.io/docs/mcp/examples)
*   [FAQ](https://scrapfly.io/docs/mcp/faq)
*   [Integrations](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#mcp-integrations-collapse)

    *   [Overview](https://scrapfly.io/docs/mcp/integrations)
    *    AI Assistants & Code Editors 
    *   [Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop)
    *   [Claude Code](https://scrapfly.io/docs/mcp/integrations/claude-code)
    *   [ChatGPT](https://scrapfly.io/docs/mcp/integrations/chatgpt)
    *   [Cursor](https://scrapfly.io/docs/mcp/integrations/cursor)
    *   [Cline](https://scrapfly.io/docs/mcp/integrations/cline)
    *   [Windsurf](https://scrapfly.io/docs/mcp/integrations/windsurf)
    *   [Zed](https://scrapfly.io/docs/mcp/integrations/zed)
    *   [Roo Code](https://scrapfly.io/docs/mcp/integrations/roo-code)
    *   [VS Code](https://scrapfly.io/docs/mcp/integrations/vscode)
    *    AI Frameworks & SDKs 
    *   [LangChain](https://scrapfly.io/docs/mcp/integrations/langchain)
    *   [LlamaIndex](https://scrapfly.io/docs/mcp/integrations/llamaindex)
    *   [CrewAI](https://scrapfly.io/docs/mcp/integrations/crewai)
    *   [OpenAI](https://scrapfly.io/docs/mcp/integrations/openai)
    *    No-Code & Automation 
    *   [n8n](https://scrapfly.io/docs/mcp/integrations/n8n)
    *   [Make](https://scrapfly.io/docs/mcp/integrations/make)
    *   [Zapier](https://scrapfly.io/docs/mcp/integrations/zapier)
    *   [Vapi AI](https://scrapfly.io/docs/mcp/integrations/vapi)
    *   [Agent Builder](https://scrapfly.io/docs/mcp/integrations/agent-builder)
    *   [Custom Client](https://scrapfly.io/docs/mcp/integrations/custom-client)

![Image 24](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176)Web Scraping API

*   [Getting started](https://scrapfly.io/docs/scrape-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/scrape-api/specification)
*   [Monitoring](https://scrapfly.io/docs/monitoring)
*   [Customize Request](https://scrapfly.io/docs/scrape-api/custom)
*   [Debug](https://scrapfly.io/docs/scrape-api/debug)
*   [Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)
*   [Proxy](https://scrapfly.io/docs/scrape-api/proxy)
*   [Proxy Mode](https://scrapfly.io/docs/scrape-api/proxy-mode)
*   [Screaming Frog](https://scrapfly.io/docs/scrape-api/proxy-mode/screaming-frog)
*   [Apify](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)
*   [(Auto) Data Extraction](https://scrapfly.io/docs/scrape-api/extraction)
*   [Javascript Rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering)
*   [Javascript Scenario](https://scrapfly.io/docs/scrape-api/javascript-scenario)
*   [SSL](https://scrapfly.io/docs/scrape-api/ssl)
*   [DNS](https://scrapfly.io/docs/scrape-api/dns)
*   [Cache](https://scrapfly.io/docs/scrape-api/cache)
*   [Session](https://scrapfly.io/docs/scrape-api/session)
*   [Webhook](https://scrapfly.io/docs/scrape-api/webhook)
*   [Screenshot](https://scrapfly.io/docs/scrape-api/screenshot)
*   [Errors](https://scrapfly.io/docs/scrape-api/errors)
*   [Timeout](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [Throttling](https://scrapfly.io/docs/throttling)
*   [Troubleshoot](https://scrapfly.io/docs/scrape-api/troubleshoot)
*   [Billing](https://scrapfly.io/docs/scrape-api/billing)
*   [FAQ](https://scrapfly.io/docs/scrape-api/faq)

![Image 25](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176)Crawler API EA

*   [Getting started](https://scrapfly.io/docs/crawler-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/crawler-api/specification)
*   [Retrieving Results](https://scrapfly.io/docs/crawler-api/results)
*   [WARC Format](https://scrapfly.io/docs/crawler-api/warc-format)
*   [Data Extraction](https://scrapfly.io/docs/crawler-api/extraction-rules)
*   [Webhook](https://scrapfly.io/docs/crawler-api/webhook)
*   [Billing](https://scrapfly.io/docs/crawler-api/billing)
*   [Errors](https://scrapfly.io/docs/crawler-api/errors)
*   [Troubleshoot](https://scrapfly.io/docs/crawler-api/troubleshoot)
*   [FAQ](https://scrapfly.io/docs/crawler-api/faq)

![Image 26](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176)Screenshot API

*   [Getting started](https://scrapfly.io/docs/screenshot-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/screenshot-api/specification)
*   [Accessibility Testing](https://scrapfly.io/docs/screenshot-api/accessibility)
*   [Webhook](https://scrapfly.io/docs/screenshot-api/webhook)
*   [Billing](https://scrapfly.io/docs/screenshot-api/billing)
*   [Errors](https://scrapfly.io/docs/screenshot-api/errors)

![Image 27](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176)Extraction API

*   [Getting started](https://scrapfly.io/docs/extraction-api/getting-started)
*   [API Specification](https://scrapfly.io/docs/extraction-api/specification)
*   [Rules Template](https://scrapfly.io/docs/extraction-api/rules-and-template)
*   [LLM Extraction](https://scrapfly.io/docs/extraction-api/llm-prompt)
*   [AI Auto Extraction](https://scrapfly.io/docs/extraction-api/automatic-ai)
*   [Webhook](https://scrapfly.io/docs/extraction-api/webhook)
*   [Billing](https://scrapfly.io/docs/extraction-api/billing)
*   [Errors](https://scrapfly.io/docs/extraction-api/errors)
*   [FAQ](https://scrapfly.io/docs/extraction-api/faq)

![Image 28](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176)Proxy Saver

*   [Getting started](https://scrapfly.io/docs/proxy-saver/getting-started)
*   [Fingerprints](https://scrapfly.io/docs/proxy-saver/fingerprints)
*   [Optimizations](https://scrapfly.io/docs/proxy-saver/optimizations)
*   [SSL Certificates](https://scrapfly.io/docs/proxy-saver/certificates)
*   [Protocols](https://scrapfly.io/docs/proxy-saver/protocols)
*   [Pacfile](https://scrapfly.io/docs/proxy-saver/pacfile)
*   [Secure Credentials](https://scrapfly.io/docs/proxy-saver/security)
*   [Billing](https://scrapfly.io/docs/proxy-saver/billing)

Tools FREE

*   [Antibot Detector](https://scrapfly.io/docs/tools/antibot-detector)

SDK

*   [Golang BETA](https://scrapfly.io/docs/sdk/golang)
*   [Python](https://scrapfly.io/docs/sdk/python)
*   [Typescript NEW](https://scrapfly.io/docs/sdk/typescript)
*   [Scrapy](https://scrapfly.io/docs/sdk/scrapy)

Integrations NEW

*   [Getting Started](https://scrapfly.io/docs/integration/getting-started)
*   [Langchain](https://scrapfly.io/docs/integration/langchain)
*   [LlamaIndex](https://scrapfly.io/docs/integration/llamaindex)
*   [CrewAI](https://scrapfly.io/docs/integration/crewai)
*   [Zapier](https://scrapfly.io/docs/integration/zapier)
*   [Make](https://scrapfly.io/docs/integration/make)
*   [n8n](https://scrapfly.io/docs/integration/n8n)
*   [Agent Skills](https://scrapfly.io/docs/integration/agent-skills)

Apify with Scrapfly Proxy Mode
==============================

[View as markdown](https://scrapfly.io/docs/scrape-api/proxy-mode/apify?view=markdown)

[Copy for LLM](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)

[Copy for LLM](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)[![Image 29](https://unpkg.com/@lobehub/icons-static-webp@latest/light/openai.webp) Open in ChatGPT](https://chatgpt.com/?hints=search&prompt=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Fproxy-mode%2Fapify%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 30](https://unpkg.com/@lobehub/icons-static-webp@latest/light/claude-color.webp) Open in Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Fproxy-mode%2Fapify%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 31](https://unpkg.com/@lobehub/icons-static-webp@latest/light/perplexity-color.webp) Open in Perplexity](https://www.perplexity.ai/search/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Fproxy-mode%2Fapify%20so%20I%20can%20ask%20questions%20about%20it.)

[Apify](https://apify.com/) is a cloud-based web scraping and automation platform. It provides a rich ecosystem of pre-built actors, crawlers (Cheerio, Playwright, Puppeteer), and the Crawlee framework for building custom scrapers.

By configuring Apify to use Scrapfly's [Proxy Mode](https://scrapfly.io/docs/scrape-api/proxy-mode) as a custom proxy, you get automatic anti-bot bypass, JavaScript rendering, proxy rotation, and geo-targeting on every request — without modifying your scraping logic.

[Why Use Scrapfly with Apify?](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#why)
----------------------------------------------------------------------------------------

*   **Anti-bot bypass** — Automatically handle Cloudflare, Akamai, PerimeterX, DataDome, and other protections.
*   **Proxy rotation** — Scrapfly manages proxy rotation across datacenter and residential pools.
*   **JavaScript rendering** — Get fully rendered HTML even with CheerioCrawler (no need for Playwright).
*   **Geo-targeting** — Route requests through specific countries for localized content.
*   **Drop-in replacement** — Replace Apify Proxy with Scrapfly Proxy using a single URL change.

[Proxy URL](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#proxy-url)
---------------------------------------------------------------------------

Use the following proxy URL in your Apify configuration:

`http://OPTIONS:YOUR_API_KEY@proxy.scrapfly.io:7777`

[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)

Replace `OPTIONS` with your desired scraping options (e.g., `country-us-asp-true`) and `YOUR_API_KEY` with your Scrapfly API key. Use `scrape` as the username for default settings.

[JavaScript / TypeScript (Apify SDK)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#javascript-sdk)
----------------------------------------------------------------------------------------------------------

### [CheerioCrawler](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#cheerio-crawler)

```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

const proxyConfiguration = await Actor.createProxyConfiguration({
    proxyUrls: [
        'http://country-us-asp-true:YOUR_API_KEY@proxy.scrapfly.io:7777',
    ],
});

const crawler = new CheerioCrawler({
    proxyConfiguration,
    async requestHandler({ request, $ }) {
        const title = $('title').text();
        const description = $('meta[name="description"]').attr('content');
        console.log(`${request.url}: ${title}`);

        await Actor.pushData({ url: request.url, title, description });
    },
});

await crawler.run(['https://web-scraping.dev/products']);
await Actor.exit();
```

[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)

### [PlaywrightCrawler](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#playwright-crawler)

```
import { Actor } from 'apify';
import { PlaywrightCrawler } from 'crawlee';

await Actor.init();

// Disable Scrapfly JS rendering since Playwright handles it
const proxyConfiguration = await Actor.createProxyConfiguration({
    proxyUrls: [
        'http://renderJs-false-asp-true:YOUR_API_KEY@proxy.scrapfly.io:7777',
    ],
});

const crawler = new PlaywrightCrawler({
    proxyConfiguration,
    async requestHandler({ request, page }) {
        const title = await page.title();
        console.log(`${request.url}: ${title}`);
    },
});

await crawler.run(['https://web-scraping.dev/products']);
await Actor.exit();
```

[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)

> **Tip:**When using PlaywrightCrawler or PuppeteerCrawler, set `renderJs-false`in the proxy username to avoid double-rendering. The browser already executes JavaScript — Scrapfly only needs to handle anti-bot protection and proxy rotation.

[Python (Apify SDK)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#python-sdk)
-------------------------------------------------------------------------------------

```
from apify import Actor
from crawlee.cheerio_crawler import CheerioCrawler

async def main() -> None:
    async with Actor:
        proxy_configuration = await Actor.create_proxy_configuration(
            proxy_urls=[
                'http://country-us-asp-true:YOUR_API_KEY@proxy.scrapfly.io:7777',
            ],
        )

        crawler = CheerioCrawler(
            proxy_configuration=proxy_configuration,
        )

        @crawler.router.default_handler
        async def default_handler(context):
            title = context.soup.title.string if context.soup.title else ''
            await context.push_data({'url': context.request.url, 'title': title})

        await crawler.run(['https://web-scraping.dev/products'])
```

[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)

[Actor Input (JSON)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#actor-input)
--------------------------------------------------------------------------------------

If you're running an existing Apify actor from the Apify Console or via API, pass Scrapfly as a custom proxy in the actor input:

```
{
    "startUrls": [
        { "url": "https://web-scraping.dev/products" }
    ],
    "proxyConfiguration": {
        "useApifyProxy": false,
        "proxyUrls": [
            "http://country-us-asp-true:YOUR_API_KEY@proxy.scrapfly.io:7777"
        ]
    }
}
```

[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)[](https://scrapfly.io/docs/scrape-api/proxy-mode/apify)

> **Important:**Set `"useApifyProxy": false`when providing custom proxy URLs. This ensures Apify routes requests through Scrapfly instead of its own proxy infrastructure.

[Recommended Options](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#recommended-options)
-----------------------------------------------------------------------------------------------

| Use Case | Proxy Username | Description |
| --- | --- | --- |
| **CheerioCrawler** | `country-us-asp-true` | Full JS rendering + anti-bot (Cheerio gets rendered HTML). |
| **PlaywrightCrawler** | `renderJs-false-asp-true` | Anti-bot only (browser handles JS). |
| **Residential proxies** | `proxyPool-public_residential_pool` | Use residential IPs for heavily protected sites. |
| **With caching** | `cache-true-cacheTtl-3600` | Cache responses for 1 hour to save credits on retries. |

See the full [Proxy Mode options reference](https://scrapfly.io/docs/scrape-api/proxy-mode#options) for all available settings.

#### **Summary**

*   [Why Use Scrapfly with Apify?](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#why)
*   [Proxy URL](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#proxy-url)
*   [JavaScript / TypeScript (Apify SDK)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#javascript-sdk)
*   [Python (Apify SDK)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#python-sdk)
*   [Actor Input (JSON)](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#actor-input)
*   [Recommended Options](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#recommended-options)

esc to close

##### Search

↑↓ to navigate↵ to select esc to close

![Image 32: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)
The ultimate data collection APIs for developers. Scrape, capture, and extract web data with battle-tested tools that scale.

[](https://github.com/scrapfly)[](https://www.linkedin.com/company/scrapfly)[](https://www.youtube.com/@scrapfly)[](https://x.com/Scrapfly_dev)

### Company

*   [Careers](https://scrapfly.io/jobs)
*   [Why Scrapfly?](https://scrapfly.io/why-choose-scrapfly)
*   [Pricing](https://scrapfly.io/pricing)
*   [Status](https://scrapfly.statuspage.io/)

### Resources

*   [API Docs](https://scrapfly.io/docs)
*   [Academy](https://scrapfly.io/academy)
*   [Blog](https://scrapfly.io/blog/)
*   [Tools](https://scrapfly.io/web-scraping-tools)
*   [FAQ](https://scrapfly.io/faq)
*   [Alternatives](https://scrapfly.io/compare)

### Legal

*   [Terms of Service](https://scrapfly.io/terms-of-service)
*   [Privacy Policy](https://scrapfly.io/privacy-policy)
*   [DPA](https://scrapfly.io/data-processing-agreement)
*   [KYC](https://scrapfly.io/kyc-and-safety)

#### Integrations

*   [Zapier](https://scrapfly.io/integration/zapier)
*   [Make](https://scrapfly.io/integration/make)
*   [N8n](https://scrapfly.io/integration/n8n)
*   [LlamaIndex](https://scrapfly.io/integration/llamaindex)
*   [LangChain](https://scrapfly.io/integration/langchain)
*   [CrewAI](https://scrapfly.io/integration/crewai)

#### Learn Web Scraping

*   [Python](https://scrapfly.io/blog/posts/everything-to-know-about-web-scraping-python/)
*   [NodeJS](https://scrapfly.io/blog/posts/web-scraping-with-nodejs/)
*   [PHP](https://scrapfly.io/blog/posts/web-scraping-with-php-101/)
*   [Ruby](https://scrapfly.io/blog/posts/web-scraping-with-ruby/)
*   [Scrapy](https://scrapfly.io/blog/posts/web-scraping-with-scrapy/)
*   [Puppeteer](https://scrapfly.io/blog/posts/web-scraping-with-puppeteer-and-nodejs/)

#### Use Cases

*   [AI Training](https://scrapfly.io/use-case/ai-training-web-scraping)
*   [eCommerce](https://scrapfly.io/use-case/ecommerce-web-scraping)
*   [Real Estate](https://scrapfly.io/use-case/real-estate-web-scraping)
*   [Finance](https://scrapfly.io/use-case/finance-web-scraping)
*   [SERP & SEO](https://scrapfly.io/use-case/seo-and-serp-web-scraping)
*   [Travel](https://scrapfly.io/use-case/travel-web-scraping)

#### Popular Tools

*   [cURL to Python](https://scrapfly.io/web-scraping-tools/curl-python)
*   [JA3 Fingerprint](https://scrapfly.io/web-scraping-tools/ja3-fingerprint)
*   [HTTP2 Fingerprint](https://scrapfly.io/web-scraping-tools/http2-fingerprint)
*   [Selector Tester](https://scrapfly.io/web-scraping-tools/css-xpath-tester)
*   [Antibot Detector](https://scrapfly.io/antibot-detector)
*   [Unblocker](https://scrapfly.io/unblocker)

#### Anti-Bot Bypass

*   [Cloudflare](https://scrapfly.io/bypass/cloudflare)
*   [Akamai](https://scrapfly.io/bypass/akamai)
*   [DataDome](https://scrapfly.io/bypass/datadome)
*   [Incapsula](https://scrapfly.io/bypass/incapsula)
*   [PerimeterX](https://scrapfly.io/bypass/perimeterx)
*   [View All](https://scrapfly.io/bypass)

© 2026 Scrapfly. The Best Web Scraping API For Developers.

[Is Web Scraping Legal?](https://scrapfly.io/is-web-scraping-legal)•[Open Source Scrapers](https://github.com/scrapfly/scrapfly-scrapers)

##### Quick Preview

[Close](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)[Open Full Docs](https://scrapfly.io/docs/scrape-api/proxy-mode/apify#)
