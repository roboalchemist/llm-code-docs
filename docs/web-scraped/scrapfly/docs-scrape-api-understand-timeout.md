# Source: https://scrapfly.io/docs/scrape-api/understand-timeout

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/understand-timeout

Markdown Content:
Scrapfly Web Scraping API | Understand how timeout are working
===============

[![Image 1: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)Docs](https://scrapfly.io/docs)

Search documentation...⌘K

Ask AI[Sign in](https://scrapfly.io/login)[Get Started](https://scrapfly.io/register)

[Products](https://scrapfly.io/docs/scrape-api/understand-timeout#)

[![Image 2](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Server](https://scrapfly.io/docs/mcp/getting-started)[![Image 3](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started)[![Image 4](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/docs/screenshot-api/getting-started)[![Image 5](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/docs/extraction-api/getting-started)[![Image 6](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176) Proxy Saver](https://scrapfly.io/docs/proxy-saver/getting-started)[![Image 7](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/docs/crawler-api/getting-started)

[SDKs](https://scrapfly.io/docs/scrape-api/understand-timeout#)

[![Image 8](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/python-icon.svg?version=0.1.176) Python SDK](https://scrapfly.io/docs/sdk/python)[![Image 9](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/typescript-icon.svg?version=0.1.176) TypeScript SDK](https://scrapfly.io/docs/sdk/typescript)[![Image 10](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/golang-icon-transperant.svg?version=0.1.176) Golang SDK](https://scrapfly.io/docs/sdk/golang)[![Image 11](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/scrapy-icon.svg?version=0.1.176) Scrapy SDK](https://scrapfly.io/docs/sdk/scrapy)

[Visual API](https://scrapfly.io/docs/scrape-api/understand-timeout#)

[![Image 12](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/dashboard/playground/web-scraper)[![Image 13](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/dashboard/playground/extraction)[![Image 14](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/dashboard/playground/crawler)[![Image 15](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/dashboard/playground/screenshot)[![Image 16](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Playground](https://scrapfly.io/dashboard/playground/mcp)

[Tools](https://scrapfly.io/docs/scrape-api/understand-timeout#)

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
*   [Integrations](https://scrapfly.io/docs/scrape-api/understand-timeout#mcp-integrations-collapse)

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
*   [Integrations](https://scrapfly.io/docs/scrape-api/understand-timeout#mcp-integrations-collapse)

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

Understanding Scrapfly Timeouts
===============================

[View as markdown](https://scrapfly.io/docs/scrape-api/understand-timeout?view=markdown)

[Copy for LLM](https://scrapfly.io/docs/scrape-api/understand-timeout#)

[Copy for LLM](https://scrapfly.io/docs/scrape-api/understand-timeout#)[![Image 29](https://unpkg.com/@lobehub/icons-static-webp@latest/light/openai.webp) Open in ChatGPT](https://chatgpt.com/?hints=search&prompt=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Funderstand-timeout%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 30](https://unpkg.com/@lobehub/icons-static-webp@latest/light/claude-color.webp) Open in Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Funderstand-timeout%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 31](https://unpkg.com/@lobehub/icons-static-webp@latest/light/perplexity-color.webp) Open in Perplexity](https://www.perplexity.ai/search/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fscrape-api%2Funderstand-timeout%20so%20I%20can%20ask%20questions%20about%20it.)

Scrapfly's [timeout configuration](https://scrapfly.io/docs/scrape-api/getting-started#api_param_timeouts) allows you to **set a deadline** for each scrape request. If a scrape doesn't complete within the defined timeout, it will be stopped and a Scrapfly error response will be returned.

> **Critical: Configure Your HTTP Client Timeout**
> 
> For the best experience, configure your HTTP client with a **minimum timeout of 155 seconds**.
> 
> If you use a custom Scrapfly timeout, add `+5s`overhead to your client read timeout.

[Quick Reference](https://scrapfly.io/docs/scrape-api/understand-timeout#quick-reference)
-----------------------------------------------------------------------------------------

Common timeout configurations for different scenarios:

| Scenario | Scrapfly Parameters | Your HTTP Client Timeout |
| --- | --- | --- |
| **Default (Managed by Scrapfly)** Best for most use cases | `retry=true` (default) | 155s |
| **Simple HTML Scraping** No JavaScript, no ASP | `retry=false` `timeout=15000` | 20s (15s + 5s overhead) |
| **JavaScript Rendering** Browser-based scraping | `retry=false` `timeout=30000` | 35s (30s + 5s overhead) |
| **Anti-Scraping Protection (ASP)** Bypassing bot protection | `retry=false` `timeout=60000` | 65s (60s + 5s overhead) |
| **Complex JavaScript Scenarios** Multi-step browser automation | `retry=false` `timeout=90000` | 95s (90s + 5s overhead) |

*   [Basics](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [Timeout Flow](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [Usage Examples](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [FAQ](https://scrapfly.io/docs/scrape-api/understand-timeout)

### [How Timeouts Work](https://scrapfly.io/docs/scrape-api/understand-timeout#how-it-works)

Scrapfly scrape speeds depend on many factors including:

*   **JavaScript rendering:** Browser-based scraping takes longer than simple HTTP requests
*   **JavaScript scenarios:** Complex browser automation adds execution time
*   **Anti-bot bypass:** Solving CAPTCHAs and bypassing protection mechanisms requires additional time
*   **Website performance:** Slow or unresponsive websites naturally take longer to scrape

**Typical scrape durations:**

*   Simple scrapes: **Less than 5 seconds**
*   JavaScript rendering: **10-30 seconds**
*   Complex scenarios or anti-bot bypass: **30-90 seconds**

### [When Should I Configure Timeout?](https://scrapfly.io/docs/scrape-api/understand-timeout#when-to-configure)

Generally, it's best to trust Scrapfly's default timeout management (`retry=true`). However, custom timeouts are useful for:

##### Real-Time Scraping

When you need the fastest possible response and can accept failures, use lower timeouts to avoid waiting unnecessarily.

##### Slow Websites

For websites with heavy JavaScript or slow response times, increase the timeout to allow more time for completion.

##### Complex Automation

JavaScript scenarios with multiple steps (clicking, scrolling, form filling) require longer timeouts to complete all actions.

##### Anti-Bot Bypass

When using ASP with `retry=false`, increase timeout to at least 60 seconds to allow time for protection bypass.

> **Important:**Custom timeout configuration requires `retry=false`. With `retry=true`(default), Scrapfly automatically manages timeouts for optimal results.

### [Timeout Requirements & Limits](https://scrapfly.io/docs/scrape-api/understand-timeout#timeout-requirements)

Timeout requirements vary based on enabled features:

| Configuration | Default Timeout | Minimum Allowed | Maximum Allowed |
| --- | --- | --- | --- |
| `asp=false, js=false` | 15s | 15s | 30s |
| `asp=false, js=true` (no scenario) | 30s | 30s | 60s |
| `asp=false, js=true` (with scenario) | 30s | 30s | 90s |
| `asp=true` | 30s | 30s | 150s |

> **ASP + retry=false Recommendation:**When using `asp=true`with `retry=false`, the default 30s timeout may not be sufficient. We recommend a **minimum of 60 seconds**to allow adequate time for anti-bot protection bypass.

### [Timeout Flow Visualization](https://scrapfly.io/docs/scrape-api/understand-timeout#timeout-flow-diagram)

This diagram shows how Scrapfly determines timeout values based on your configuration. **Blue dashed boxes** indicate configurable timeouts, while **red boxes** indicate timeouts managed automatically by Scrapfly.

100%

 Drag to pan, Ctrl/Cmd+scroll to zoom, double-click for fullscreen

> ##### Understanding the Diagram
> 
> 
> *   **retry=true (Right Path):** Scrapfly automatically manages timeouts and retries. Your client timeout should be **155 seconds**.
> *   **retry=false (Left Path):** You control the timeout explicitly. Add **+5s overhead** to your client timeout.
> *   **Blue Dashed Boxes:** Timeouts you can customize with the `timeout` parameter.
> *   **Red Boxes:** Fixed timeouts managed by Scrapfly (with `retry=true`).

### [Usage Examples](https://scrapfly.io/docs/scrape-api/understand-timeout#usage-examples)

To configure a custom scrape timeout, use `retry=false` and `timeout=<milliseconds>` query parameters.

#### Example: 20 Second Timeout

[Curl](https://scrapfly.io/docs/scrape-api/understand-timeout#player-a34658)[HTTP](https://scrapfly.io/docs/scrape-api/understand-timeout#http-a34658)

[](https://scrapfly.io/docs/scrape-api/understand-timeout)[](https://scrapfly.io/docs/scrape-api/understand-timeout)[](https://scrapfly.io/login)

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "retry=false" \
--data-urlencode "timeout=20000" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/delay/5"
```

`https://api.scrapfly.io/scrape?retry=false&timeout=20000&key=&url=https%3A%2F%2Fhttpbin.dev%2Fdelay%2F5`

> **Remember:**Your HTTP client timeout should be **25 seconds**(20s + 5s overhead) for this example.

#### Client Configuration Examples

*   [Python](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [Node.js](https://scrapfly.io/docs/scrape-api/understand-timeout)
*   [PHP](https://scrapfly.io/docs/scrape-api/understand-timeout)

`Python client with 95s timeout`

[](https://scrapfly.io/docs/scrape-api/understand-timeout)[](https://scrapfly.io/docs/scrape-api/understand-timeout)

`Node.js client with 95s timeout`

[](https://scrapfly.io/docs/scrape-api/understand-timeout)[](https://scrapfly.io/docs/scrape-api/understand-timeout)

`PHP client with 95s timeout`

[](https://scrapfly.io/docs/scrape-api/understand-timeout)[](https://scrapfly.io/docs/scrape-api/understand-timeout)

### [Frequently Asked Questions](https://scrapfly.io/docs/scrape-api/understand-timeout#faq-section)

##### I want to run a JavaScript scenario that requires 90s in the worst case. How should I configure it?

**Configuration:**

*   Scrapfly: `retry=false&timeout=90000`
*   Your HTTP client: **95 seconds** (90s + 5s overhead)

This ensures your JavaScript scenario has the full 90 seconds to complete, and your client won't disconnect prematurely.

##### I'm scraping a website without JavaScript and want the lowest timeout possible. What should I use?

**Configuration:**

*   Scrapfly: `retry=false&timeout=15000`
*   Your HTTP client: **20 seconds** (15s + 5s overhead)

**Note:** This only works when `asp=false` and `render_js=false`. 15 seconds is the minimum allowed timeout for simple HTTP scraping.

##### Should I always use retry=false for custom timeouts?

**Yes.** Custom timeout configuration requires `retry=false`. When `retry=true` (default), Scrapfly automatically manages timeouts and retries for optimal reliability.

**Use retry=true when:**

*   You want maximum reliability and don't mind longer wait times
*   You're scraping difficult targets with anti-bot protection
*   You want Scrapfly to handle retries automatically

**Use retry=false when:**

*   You need precise control over timeout durations
*   You're implementing your own retry logic
*   You need the fastest possible response (fail fast)

##### Why do I need to add +5s overhead to my HTTP client timeout?

The +5s overhead accounts for:

*   **Network latency:** Time for request/response transmission
*   **Processing overhead:** Time for Scrapfly to process and package the response
*   **Connection establishment:** Initial connection setup time

Without this overhead, your client might disconnect before receiving Scrapfly's response, even if the scrape completed successfully within the timeout.

##### What happens if a scrape exceeds the timeout?

When a scrape exceeds the configured timeout:

1.   The scrape operation is immediately stopped
2.   A Scrapfly error response is returned
3.   You'll receive one of the timeout-related error codes (see below)
4.   No partial data is returned

Check the [Related Errors](https://scrapfly.io/docs/scrape-api/understand-timeout#errors) section for specific timeout error codes and their meanings.

[Related Errors](https://scrapfly.io/docs/scrape-api/understand-timeout#errors)
-------------------------------------------------------------------------------

When a timeout occurs, you may encounter one of the following error codes. Click on each error for detailed information and troubleshooting steps.

*   [ERR::SCRAPE::OPERATION_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::OPERATION_TIMEOUT?iframe=1)
*   [ERR::SCRAPE::SCENARIO_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::SCENARIO_TIMEOUT?iframe=1)
*   [ERR::ASP::TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::TIMEOUT?iframe=1)
*   [ERR::SCRAPE::DRIVER_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_TIMEOUT?iframe=1)

*   [ERR::ASP::CAPTCHA_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_TIMEOUT?iframe=1)
*   [ERR::PROXY::TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::TIMEOUT?iframe=1)
*   [ERR::EXTRACTION::TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::EXTRACTION::TIMEOUT?iframe=1)

#### **Summary**

*   [Quick Reference](https://scrapfly.io/docs/scrape-api/understand-timeout#quick-reference)
*   [Related Errors](https://scrapfly.io/docs/scrape-api/understand-timeout#errors)

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

[Close](https://scrapfly.io/docs/scrape-api/understand-timeout#)[Open Full Docs](https://scrapfly.io/docs/scrape-api/understand-timeout#)

##### Diagram

100%

×
