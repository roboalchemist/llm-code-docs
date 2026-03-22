# Source: https://scrapfly.io/docs/mcp/integrations/llamaindex

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/integrations/llamaindex

Markdown Content:
Scrapfly MCP Integration for LlamaIndex | Setup Guide
===============

[![Image 1: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)Docs](https://scrapfly.io/docs)

Search documentation...⌘K

Ask AI[Sign in](https://scrapfly.io/login)[Get Started](https://scrapfly.io/register)

[Products](https://scrapfly.io/docs/mcp/integrations/llamaindex#)

[![Image 2](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Server](https://scrapfly.io/docs/mcp/getting-started)[![Image 3](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started)[![Image 4](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/docs/screenshot-api/getting-started)[![Image 5](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/docs/extraction-api/getting-started)[![Image 6](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176) Proxy Saver](https://scrapfly.io/docs/proxy-saver/getting-started)[![Image 7](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/docs/crawler-api/getting-started)

[SDKs](https://scrapfly.io/docs/mcp/integrations/llamaindex#)

[![Image 8](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/python-icon.svg?version=0.1.176) Python SDK](https://scrapfly.io/docs/sdk/python)[![Image 9](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/typescript-icon.svg?version=0.1.176) TypeScript SDK](https://scrapfly.io/docs/sdk/typescript)[![Image 10](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/golang-icon-transperant.svg?version=0.1.176) Golang SDK](https://scrapfly.io/docs/sdk/golang)[![Image 11](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/scrapy-icon.svg?version=0.1.176) Scrapy SDK](https://scrapfly.io/docs/sdk/scrapy)

[Visual API](https://scrapfly.io/docs/mcp/integrations/llamaindex#)

[![Image 12](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/dashboard/playground/web-scraper)[![Image 13](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/dashboard/playground/extraction)[![Image 14](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/dashboard/playground/crawler)[![Image 15](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/dashboard/playground/screenshot)[![Image 16](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Playground](https://scrapfly.io/dashboard/playground/mcp)

[Tools](https://scrapfly.io/docs/mcp/integrations/llamaindex#)

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
*   [Integrations](https://scrapfly.io/docs/mcp/integrations/llamaindex#mcp-integrations-collapse)

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
*   [Integrations](https://scrapfly.io/docs/mcp/integrations/llamaindex#mcp-integrations-collapse)

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

LlamaIndex
==========

[View as markdown](https://scrapfly.io/docs/mcp/integrations/llamaindex?view=markdown)

[Copy for LLM](https://scrapfly.io/docs/mcp/integrations/llamaindex#)

[Copy for LLM](https://scrapfly.io/docs/mcp/integrations/llamaindex#)[![Image 29](https://unpkg.com/@lobehub/icons-static-webp@latest/light/openai.webp) Open in ChatGPT](https://chatgpt.com/?hints=search&prompt=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fllamaindex%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 30](https://unpkg.com/@lobehub/icons-static-webp@latest/light/claude-color.webp) Open in Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fllamaindex%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 31](https://unpkg.com/@lobehub/icons-static-webp@latest/light/perplexity-color.webp) Open in Perplexity](https://www.perplexity.ai/search/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fllamaindex%20so%20I%20can%20ask%20questions%20about%20it.)

![Image 32: LlamaIndex logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/llamaindex-icon.svg?version=0.1.176)

Data framework for LLM applications. Connect Scrapfly to LlamaIndex agents and workflows for intelligent web data ingestion and RAG applications.

AI Framework Python TypeScript[Official Website](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/mcp/)

1.   [MCP Documentation](https://scrapfly.io/docs/mcp)
2.   [Integrations](https://scrapfly.io/docs/mcp/integrations)
3.   LlamaIndex

[Prerequisites](https://scrapfly.io/docs/mcp/integrations/llamaindex#prerequisites)
-----------------------------------------------------------------------------------

Before getting started, make sure you have the following:

*   Python 3.8+ installed
*   `llama-index-tools-mcp` package installed
*   Your Scrapfly API key

[Setup Instructions](https://scrapfly.io/docs/mcp/integrations/llamaindex#setup)
--------------------------------------------------------------------------------

LlamaIndex supports MCP servers through the tools integration. Follow these steps to connect Scrapfly for web data ingestion.

1.   **Install Required Packages**
Install LlamaIndex MCP integration tools:

`pip install llama-index-tools-mcp` [](https://scrapfly.io/docs/mcp/integrations/llamaindex)[](https://scrapfly.io/docs/mcp/integrations/llamaindex)  Tip: Development Environment
Use a virtual environment for Python projects:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install llama-index-tools-mcp
``` [](https://scrapfly.io/docs/mcp/integrations/llamaindex)[](https://scrapfly.io/docs/mcp/integrations/llamaindex)   
2.   **Initialize Scrapfly MCP Tools**
Connect to the Scrapfly MCP server and load tools into LlamaIndex:

### Python Example with API Key

```
import asyncio

from llama_index.tools.mcp import (
    BasicMCPClient,
    get_tools_from_mcp_url,
    aget_tools_from_mcp_url,
)

mcp_client = BasicMCPClient("https://mcp.scrapfly.io/mcp?key=YOUR_API_KEY")

async def main():
    tools = await aget_tools_from_mcp_url(
        "https://mcp.scrapfly.io/mcp?key=YOUR_API_KEY",
        client=mcp_client
    )

    for tool in tools:
        print(f"  - {tool.metadata.name}")

asyncio.run(main())
``` [](https://scrapfly.io/docs/mcp/integrations/llamaindex)[](https://scrapfly.io/docs/mcp/integrations/llamaindex)  
3.   **Create a LlamaIndex Agent with Scrapfly**
Build an agent that can scrape web data and integrate it into your LlamaIndex workflow:

```
from llama_index.core.agent import ReActAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.tools.mcp import MCPToolProvider

# Initialize Scrapfly MCP tools
scrapfly_provider = MCPToolProvider(
    server_name="scrapfly",
    command="npx",
    args=["mcp-remote", "https://mcp.scrapfly.io/mcp"]
)

scrapfly_tools = scrapfly_provider.get_tools()

# Initialize LLM
llm = Anthropic(model="claude-3-5-sonnet-20241022")

# Create agent with Scrapfly tools
agent = ReActAgent.from_tools(
    tools=scrapfly_tools,
    llm=llm,
    verbose=True
)

# Use the agent to scrape and process data
response = agent.chat(
    "Scrape the top posts from Hacker News and create a summary"
)

print(response)
``` [](https://scrapfly.io/docs/mcp/integrations/llamaindex)[](https://scrapfly.io/docs/mcp/integrations/llamaindex)  
4.   **Build a RAG Pipeline with Web Data**
Use Scrapfly to ingest live web content into a LlamaIndex RAG application:

```
import asyncio

from llama_index.core import VectorStoreIndex, Document
from llama_index.core.agent import ReActAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.tools.mcp import (
    BasicMCPClient,
    get_tools_from_mcp_url,
    aget_tools_from_mcp_url,
)

async def main():
    # Initialize Scrapfly MCP
    scrapfly_provider = BasicMCPClient("https://mcp.scrapfly.io/mcp?key=YOUR_API_KEY")

    scrapfly_tools = await aget_tools_from_mcp_url(
            "https://mcp.scrapfly.io/mcp?key=YOUR_API_KEY",
            client=scrapfly_provider
        )

    llm = Anthropic(model="claude-3-5-sonnet-20241022")

    # Create agent that can scrape web data
    agent = ReActAgent.from_tools(
        tools=scrapfly_tools,
        llm=llm,
        verbose=True
    )

    # Scrape web content
    response = agent.chat(
        "Scrape the documentation from https://scrapfly.io/docs and return the content"
    )

    # Convert scraped content to documents
    documents = [
        Document(text=response.response)
    ]

    # Build vector index from scraped data
    index = VectorStoreIndex.from_documents(documents)

    # Query the index
    query_engine = index.as_query_engine()
    result = query_engine.query("What is web scraping?")
    print(result)

asyncio.run(main())
``` [](https://scrapfly.io/docs/mcp/integrations/llamaindex)[](https://scrapfly.io/docs/mcp/integrations/llamaindex)  

[Example Prompts](https://scrapfly.io/docs/mcp/integrations/llamaindex#examples)
--------------------------------------------------------------------------------

###### RAG with Live Web Data

Scrape documentation from https://web-scraping.dev and answer questions about it

###### Knowledge Base Construction

Scrape blog posts from multiple sources and build a searchable knowledge base

###### Research Agent with Web Access

Research the latest AI trends by scraping tech news sites and summarize findings

###### Document Ingestion Pipeline

Scrape product documentation from competitor sites and compare features

[Troubleshooting](https://scrapfly.io/docs/mcp/integrations/llamaindex#troubleshooting)
---------------------------------------------------------------------------------------

##### Import Error: llama-index-tools-mcp not found

**Problem:**`ModuleNotFoundError: No module named 'llama_index.tools.mcp'`

**Solution:**

*   Install the package: `pip install llama-index-tools-mcp`
*   Verify Python environment: `which python`
*   Try upgrading: `pip install --upgrade llama-index-tools-mcp`
*   Check LlamaIndex version is 0.10.0+: `pip show llama-index`

##### npx Command Not Found

**Problem:** MCPToolProvider cannot execute `npx` command

**Solution:**

*   Ensure Node.js 18+ is installed: `node --version`
*   Verify `npx` is in PATH: `npx --version`
*   Restart terminal after installing Node.js
*   Try specifying full path: `command="/usr/local/bin/npx"`

##### OAuth2 in Production/CI Environments

**Problem:** OAuth2 cannot open browser in headless environment

**Solution:**

*   Use API key authentication for production deployments
*   Store API key in environment variable: `SCRAPFLY_API_KEY`
*   Load from environment: `args=["mcp-remote", f"https://mcp.scrapfly.io/mcp?key={os.getenv('SCRAPFLY_API_KEY')}"]`

##### Agent Not Using Scrapfly Tools

**Problem:** Agent does not call Scrapfly tools when asked to scrape

**Solution:**

*   Verify tools loaded: `print([tool.metadata.name for tool in scrapfly_tools])`
*   Check LLM supports function calling (Claude 3+, GPT-4+)
*   Use explicit prompts mentioning "scrape" or "web data"
*   Enable verbose mode: `verbose=True` in agent creation

##### Document Ingestion Errors

**Problem:** Scraped content cannot be converted to Document objects

**Solution:**

*   Ensure scraped content is text/markdown format
*   Check response format from Scrapfly MCP tools
*   Parse response before creating Document: `Document(text=str(response))`
*   Handle empty or malformed responses with error checking

[Next Steps](https://scrapfly.io/docs/mcp/integrations/llamaindex#next-steps)
-----------------------------------------------------------------------------

*   [Explore available MCP tools](https://scrapfly.io/docs/mcp/tools) and their capabilities
*   [See real-world examples](https://scrapfly.io/docs/mcp/examples) of what you can build
*   [Learn about authentication methods](https://scrapfly.io/docs/mcp/authentication) in detail
*   [Read the FAQ](https://scrapfly.io/docs/mcp/faq) for common questions

[Back to All Integrations](https://scrapfly.io/docs/mcp/integrations)

#### **Summary**

*   [Prerequisites](https://scrapfly.io/docs/mcp/integrations/llamaindex#prerequisites)
*   [Setup Instructions](https://scrapfly.io/docs/mcp/integrations/llamaindex#setup)
*   [Example Prompts](https://scrapfly.io/docs/mcp/integrations/llamaindex#examples)
*   [Troubleshooting](https://scrapfly.io/docs/mcp/integrations/llamaindex#troubleshooting)
*   [Next Steps](https://scrapfly.io/docs/mcp/integrations/llamaindex#next-steps)

esc to close

##### Search

↑↓ to navigate↵ to select esc to close

![Image 33: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)
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

[Close](https://scrapfly.io/docs/mcp/integrations/llamaindex#)[Open Full Docs](https://scrapfly.io/docs/mcp/integrations/llamaindex#)
