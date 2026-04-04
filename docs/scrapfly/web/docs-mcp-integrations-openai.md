# Source: https://scrapfly.io/docs/mcp/integrations/openai

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/integrations/openai

Markdown Content:
Scrapfly MCP Integration for OpenAI Assistants API | Setup Guide
===============

[![Image 1: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)Docs](https://scrapfly.io/docs)

Search documentation...⌘K

Ask AI[Sign in](https://scrapfly.io/login)[Get Started](https://scrapfly.io/register)

[Products](https://scrapfly.io/docs/mcp/integrations/openai#)

[![Image 2](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Server](https://scrapfly.io/docs/mcp/getting-started)[![Image 3](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started)[![Image 4](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/docs/screenshot-api/getting-started)[![Image 5](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/docs/extraction-api/getting-started)[![Image 6](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/proxy-saver-icon.svg?version=0.1.176) Proxy Saver](https://scrapfly.io/docs/proxy-saver/getting-started)[![Image 7](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/docs/crawler-api/getting-started)

[SDKs](https://scrapfly.io/docs/mcp/integrations/openai#)

[![Image 8](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/python-icon.svg?version=0.1.176) Python SDK](https://scrapfly.io/docs/sdk/python)[![Image 9](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/typescript-icon.svg?version=0.1.176) TypeScript SDK](https://scrapfly.io/docs/sdk/typescript)[![Image 10](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/golang-icon-transperant.svg?version=0.1.176) Golang SDK](https://scrapfly.io/docs/sdk/golang)[![Image 11](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/scrapy-icon.svg?version=0.1.176) Scrapy SDK](https://scrapfly.io/docs/sdk/scrapy)

[Visual API](https://scrapfly.io/docs/mcp/integrations/openai#)

[![Image 12](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/web-scraping-api-icon.svg?version=0.1.176) Web Scraping API](https://scrapfly.io/dashboard/playground/web-scraper)[![Image 13](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/extraction-api-icon.svg?version=0.1.176) Extraction API](https://scrapfly.io/dashboard/playground/extraction)[![Image 14](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/crawler-api-icon.svg?version=0.1.176) Crawler API](https://scrapfly.io/dashboard/playground/crawler)[![Image 15](https://cdn.scrapfly.io/0.1.176/www/public/svg/home/screenshot-api-icon.svg?version=0.1.176) Screenshot API](https://scrapfly.io/dashboard/playground/screenshot)[![Image 16](https://cdn.scrapfly.io/0.1.176/www/public/svg/mcp-logo.svg?version=0.1.176) MCP Playground](https://scrapfly.io/dashboard/playground/mcp)

[Tools](https://scrapfly.io/docs/mcp/integrations/openai#)

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
*   [Integrations](https://scrapfly.io/docs/mcp/integrations/openai#mcp-integrations-collapse)

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
*   [Integrations](https://scrapfly.io/docs/mcp/integrations/openai#mcp-integrations-collapse)

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

OpenAI Assistants API
=====================

[View as markdown](https://scrapfly.io/docs/mcp/integrations/openai?view=markdown)

[Copy for LLM](https://scrapfly.io/docs/mcp/integrations/openai#)

[Copy for LLM](https://scrapfly.io/docs/mcp/integrations/openai#)[![Image 29](https://unpkg.com/@lobehub/icons-static-webp@latest/light/openai.webp) Open in ChatGPT](https://chatgpt.com/?hints=search&prompt=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fopenai%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 30](https://unpkg.com/@lobehub/icons-static-webp@latest/light/claude-color.webp) Open in Claude](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fopenai%20so%20I%20can%20ask%20questions%20about%20it.)[![Image 31](https://unpkg.com/@lobehub/icons-static-webp@latest/light/perplexity-color.webp) Open in Perplexity](https://www.perplexity.ai/search/new?q=Read%20from%20https%3A%2F%2Fscrapfly.io%2Fdocs%2Fmcp%2Fintegrations%2Fopenai%20so%20I%20can%20ask%20questions%20about%20it.)

![Image 32: OpenAI Assistants API logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/openai-icon.svg?version=0.1.176)

OpenAI's Assistants API with function calling. Integrate Scrapfly web scraping as custom functions for GPT-4 assistants with autonomous data collection capabilities.

AI Platform Python JavaScript TypeScript REST API[Official Website](https://platform.openai.com/docs/assistants/tools/function-calling)

1.   [MCP Documentation](https://scrapfly.io/docs/mcp)
2.   [Integrations](https://scrapfly.io/docs/mcp/integrations)
3.   OpenAI Assistants API

[Prerequisites](https://scrapfly.io/docs/mcp/integrations/openai#prerequisites)
-------------------------------------------------------------------------------

Before getting started, make sure you have the following:

*   OpenAI API key ([get one here](https://platform.openai.com/api-keys))
*   Your Scrapfly API key
*   Python 3.8+, Node.js 18+, or any HTTP client

**Note:** OpenAI Assistants API does not natively support MCP servers. Instead, we integrate Scrapfly through [function calling](https://platform.openai.com/docs/assistants/tools/function-calling), where your code bridges between the assistant and Scrapfly's API. 

[Setup Instructions](https://scrapfly.io/docs/mcp/integrations/openai#setup)
----------------------------------------------------------------------------

Integrate Scrapfly with OpenAI Assistants by creating function definitions that call Scrapfly's API. This takes about 10 minutes to set up.

1.   **Install OpenAI SDK**
Install the OpenAI SDK for your platform:

**Python:**

`pip install openai requests` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  
**JavaScript/TypeScript:**

`npm install openai axios` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  Tip: Environment Variables
Store your API keys in environment variables:

```
export OPENAI_API_KEY="your-openai-key"
export SCRAPFLY_API_KEY="your-scrapfly-key"
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)   
2.   **Define Scrapfly Function Schemas**
Create function definitions that describe Scrapfly's capabilities to the OpenAI assistant:

### Python Example

```
import openai
import requests
import os

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define Scrapfly function schema
scrapfly_function = {
    "type": "function",
    "function": {
        "name": "scrape_webpage",
        "description": "Scrape content from a webpage using Scrapfly. Returns the page content in markdown format.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to scrape (must start with http:// or https://)"
                },
                "render_js": {
                    "type": "boolean",
                    "description": "Whether to render JavaScript on the page (default: true)"
                },
                "format": {
                    "type": "string",
                    "enum": ["markdown", "text", "clean_html", "raw"],
                    "description": "Output format (default: markdown)"
                }
            },
            "required": ["url"]
        }
    }
}
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  
### JavaScript/TypeScript Example

```
import OpenAI from "openai";
import axios from "axios";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const scrapflyFunction = {
  type: "function" as const,
  function: {
    name: "scrape_webpage",
    description: "Scrape content from a webpage using Scrapfly. Returns the page content in markdown format.",
    parameters: {
      type: "object",
      properties: {
        url: {
          type: "string",
          description: "The URL to scrape (must start with http:// or https://)"
        },
        render_js: {
          type: "boolean",
          description: "Whether to render JavaScript on the page (default: true)"
        },
        format: {
          type: "string",
          enum: ["markdown", "text", "clean_html", "raw"],
          description: "Output format (default: markdown)"
        }
      },
      required: ["url"]
    }
  }
};
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  
3.   **Implement Function Handler**
Create a function that executes Scrapfly API calls when the assistant requests web scraping:

### Python Handler

```
def scrape_webpage(url: str, render_js: bool = True, format: str = "markdown") -> str:
    """Execute Scrapfly API call"""

    scrapfly_url = "{{ public_api_endpoint }}/scrape"
    params = {
        "key": os.getenv("SCRAPFLY_API_KEY"),
        "url": url,
        "render_js": str(render_js).lower(),
        "format": format
    }

    response = requests.get(scrapfly_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("result", {}).get("content", "No content found")
    else:
        return f"Error scraping {url}: {response.status_code}"
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  
### JavaScript/TypeScript Handler

```
async function scrapeWebpage(
  url: string,
  renderJs: boolean = true,
  format: string = "markdown"
): Promise {
  const response = await axios.get("{{ public_api_endpoint }}/scrape", {
    params: {
      key: process.env.SCRAPFLY_API_KEY,
      url: url,
      render_js: renderJs.toString(),
      format: format
    }
  });

  if (response.status === 200) {
    return response.data.result?.content || "No content found";
  } else {
    return `Error scraping ${url}: ${response.status}`;
  }
}
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  
4.   **Create OpenAI Assistant with Scrapfly Function**
Create an assistant that can call your Scrapfly function:

### Python Example

```
# Create assistant with Scrapfly function
assistant = client.beta.assistants.create(
    name="Web Research Assistant",
    instructions="You are a helpful assistant that can scrape and analyze web content. Use the scrape_webpage function to fetch data from URLs.",
    model="gpt-4-turbo",
    tools=[scrapfly_function]
)

# Create a thread and run
thread = client.beta.threads.create()

# User message
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Scrape the top posts from https://news.ycombinator.com and summarize them"
)

# Run the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Handle function calling
import time
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "requires_action":
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []

        for tool_call in tool_calls:
            if tool_call.function.name == "scrape_webpage":
                import json
                args = json.loads(tool_call.function.arguments)
                result = scrape_webpage(**args)
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": result
                })

        # Submit function outputs
        client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )

    time.sleep(1)

# Get final response
messages = client.beta.threads.messages.list(thread_id=thread.id)
print(messages.data[0].content[0].text.value)
``` [](https://scrapfly.io/docs/mcp/integrations/openai)[](https://scrapfly.io/docs/mcp/integrations/openai)  **Important:** Replace API keys with your actual keys. [Sign up for free](https://scrapfly.io/register) to get your Scrapfly API key.  

[Example Prompts](https://scrapfly.io/docs/mcp/integrations/openai#examples)
----------------------------------------------------------------------------

###### Research Assistant

Scrape the documentation from https://web-scraping.dev and explain how their API works

###### Price Monitoring Bot

Check the current price of the product at https://web-scraping.dev/product

###### News Aggregation

Scrape the latest tech news from Hacker News and TechCrunch, then summarize

###### Competitive Analysis

Compare features listed on these competitor websites: [url1, url2, url3]

[Troubleshooting](https://scrapfly.io/docs/mcp/integrations/openai#troubleshooting)
-----------------------------------------------------------------------------------

##### Function Not Being Called

**Problem:** Assistant does not call the scrape_webpage function

**Solution:**

*   Ensure function schema is properly defined in `tools` parameter
*   Use explicit prompts mentioning "scrape" or "fetch from URL"
*   Check assistant instructions guide it to use the function
*   Verify you're using a model that supports function calling (GPT-4, GPT-3.5-turbo)

##### Scrapfly API Errors

**Problem:** Function returns error messages from Scrapfly API

**Solution:**

*   Verify Scrapfly API key is correct and active
*   Check URL is properly formatted (must start with http:// or https://)
*   Ensure you have sufficient Scrapfly credits
*   Review Scrapfly API response for specific error details

##### Run Status Stuck in requires_action

**Problem:** Run never completes, stuck waiting for tool outputs

**Solution:**

*   Ensure you're calling `submit_tool_outputs` for all tool calls
*   Check that tool_call_id matches the requested tool call
*   Verify function output is a string (not None or empty)
*   Add error handling in function to always return a result

##### Rate Limiting Issues

**Problem:** Hitting rate limits on OpenAI or Scrapfly APIs

**Solution:**

*   Add exponential backoff retry logic in function handler
*   Check OpenAI API rate limits for your tier
*   Monitor Scrapfly usage and upgrade plan if needed
*   Implement caching for frequently scraped URLs

##### Large Content Responses

**Problem:** Scraped content too large for function output

**Solution:**

*   Truncate large responses before returning
*   Use format="text" instead of "markdown" for smaller output
*   Implement pagination or chunking for large pages
*   Summarize content in the function before returning

[Next Steps](https://scrapfly.io/docs/mcp/integrations/openai#next-steps)
-------------------------------------------------------------------------

*   [Explore available MCP tools](https://scrapfly.io/docs/mcp/tools) and their capabilities
*   [See real-world examples](https://scrapfly.io/docs/mcp/examples) of what you can build
*   [Learn about authentication methods](https://scrapfly.io/docs/mcp/authentication) in detail
*   [Read the FAQ](https://scrapfly.io/docs/mcp/faq) for common questions

[Back to All Integrations](https://scrapfly.io/docs/mcp/integrations)

#### **Summary**

*   [Prerequisites](https://scrapfly.io/docs/mcp/integrations/openai#prerequisites)
*   [Setup Instructions](https://scrapfly.io/docs/mcp/integrations/openai#setup)
*   [Example Prompts](https://scrapfly.io/docs/mcp/integrations/openai#examples)
*   [Troubleshooting](https://scrapfly.io/docs/mcp/integrations/openai#troubleshooting)
*   [Next Steps](https://scrapfly.io/docs/mcp/integrations/openai#next-steps)

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

[Close](https://scrapfly.io/docs/mcp/integrations/openai#)[Open Full Docs](https://scrapfly.io/docs/mcp/integrations/openai#)
