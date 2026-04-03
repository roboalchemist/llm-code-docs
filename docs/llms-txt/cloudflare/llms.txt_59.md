# Source: https://developers.cloudflare.com/browser-rendering/llms.txt

# Browser Rendering

Control and interact with headless browser instances programmatically

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/browser-rendering/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Browser Rendering llms-full.txt](https://developers.cloudflare.com/browser-rendering/llms-full.txt) for the complete Browser Rendering documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Browser Rendering](https://developers.cloudflare.com/browser-rendering/index.md): Control headless browsers with Cloudflare's Workers Browser Rendering API. Automate tasks, take screenshots, convert pages to PDFs, and test web apps.

## Get started

- [Get started](https://developers.cloudflare.com/browser-rendering/get-started/index.md)

## Examples

- [Examples](https://developers.cloudflare.com/browser-rendering/examples/index.md)

## REST API

- [REST API](https://developers.cloudflare.com/browser-rendering/rest-api/index.md)
- [Reference](https://developers.cloudflare.com/browser-rendering/rest-api/api-reference/index.md)
- [/content - Fetch HTML](https://developers.cloudflare.com/browser-rendering/rest-api/content-endpoint/index.md)
- [/crawl - Crawl web content](https://developers.cloudflare.com/browser-rendering/rest-api/crawl-endpoint/index.md)
- [/json - Capture structured data using AI](https://developers.cloudflare.com/browser-rendering/rest-api/json-endpoint/index.md)
- [/links - Retrieve links from a webpage](https://developers.cloudflare.com/browser-rendering/rest-api/links-endpoint/index.md)
- [/markdown - Extract Markdown from a webpage](https://developers.cloudflare.com/browser-rendering/rest-api/markdown-endpoint/index.md)
- [/pdf - Render PDF](https://developers.cloudflare.com/browser-rendering/rest-api/pdf-endpoint/index.md)
- [/scrape - Scrape HTML elements](https://developers.cloudflare.com/browser-rendering/rest-api/scrape-endpoint/index.md)
- [/screenshot - Capture screenshot](https://developers.cloudflare.com/browser-rendering/rest-api/screenshot-endpoint/index.md)
- [/snapshot - Take a webpage snapshot](https://developers.cloudflare.com/browser-rendering/rest-api/snapshot/index.md)

## Workers Bindings

- [Workers Bindings](https://developers.cloudflare.com/browser-rendering/workers-bindings/index.md)
- [Deploy a Browser Rendering Worker with Durable Objects](https://developers.cloudflare.com/browser-rendering/workers-bindings/browser-rendering-with-do/index.md): Use the Browser Rendering API along with Durable Objects to take screenshots from web pages and store them in R2.
- [Reuse sessions](https://developers.cloudflare.com/browser-rendering/workers-bindings/reuse-sessions/index.md)
- [Deploy a Browser Rendering Worker](https://developers.cloudflare.com/browser-rendering/workers-bindings/screenshots/index.md)

## Playwright

- [Playwright](https://developers.cloudflare.com/browser-rendering/playwright/index.md): Learn how to use Playwright with Cloudflare Workers for browser automation. Access Playwright API, manage sessions, and optimize browser rendering.
- [Playwright MCP](https://developers.cloudflare.com/browser-rendering/playwright/playwright-mcp/index.md): Deploy a Playwright MCP server that uses Browser Rendering to provide browser automation capabilities to your agents.

## Puppeteer

- [Puppeteer](https://developers.cloudflare.com/browser-rendering/puppeteer/index.md): Learn how to use Puppeteer with Cloudflare Workers for browser automation. Access Puppeteer API, manage sessions, and optimize browser rendering.

## Stagehand

- [Stagehand](https://developers.cloudflare.com/browser-rendering/stagehand/index.md): Deploy a Stagehand server that uses Browser Rendering to provide browser automation capabilities to your agents.

## FAQ

- [FAQ](https://developers.cloudflare.com/browser-rendering/faq/index.md)

## Limits

- [Limits](https://developers.cloudflare.com/browser-rendering/limits/index.md): Learn about the limits associated with Browser Rendering.

## Pricing

- [Pricing](https://developers.cloudflare.com/browser-rendering/pricing/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/browser-rendering/changelog/index.md): Review recent changes to Worker Browser Rendering.

## MCP server

- [MCP server](https://developers.cloudflare.com/browser-rendering/mcp-server/index.md)

## features

- [Custom fonts](https://developers.cloudflare.com/browser-rendering/features/custom-fonts/index.md): Learn how to add custom fonts to Browser Rendering for use in screenshots and PDFs.

## how-to

- [Use browser rendering with AI](https://developers.cloudflare.com/browser-rendering/how-to/ai/index.md)
- [Generate OG images for Astro sites](https://developers.cloudflare.com/browser-rendering/how-to/og-images-astro/index.md)
- [Generate PDFs Using HTML and CSS](https://developers.cloudflare.com/browser-rendering/how-to/pdf-generation/index.md)
- [Build a web crawler with Queues and Browser Rendering](https://developers.cloudflare.com/browser-rendering/how-to/queues/index.md)

## reference

- [Automatic request headers](https://developers.cloudflare.com/browser-rendering/reference/automatic-request-headers/index.md)
- [Browser close reasons](https://developers.cloudflare.com/browser-rendering/reference/browser-close-reasons/index.md)
- [robots.txt and sitemaps](https://developers.cloudflare.com/browser-rendering/reference/robots-txt/index.md)
- [Supported fonts](https://developers.cloudflare.com/browser-rendering/reference/supported-fonts/index.md)
- [REST API timeouts](https://developers.cloudflare.com/browser-rendering/reference/timeouts/index.md)
- [Wrangler](https://developers.cloudflare.com/browser-rendering/reference/wrangler/index.md): Use Wrangler, a command-line tool, to deploy projects using Cloudflare's Workers Browser Rendering API.