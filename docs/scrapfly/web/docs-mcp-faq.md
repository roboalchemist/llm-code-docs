# Source: https://scrapfly.io/docs/mcp/faq

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/faq

Markdown Content:
MCP FAQ
-------

Find quick answers to common questions about the Scrapfly MCP Server. Use the tag filter on the right to browse by category.

> **Looking for Scrape API documentation?**If you're using Scrapfly's REST API directly (not through MCP), see the [Scrape API FAQ](https://scrapfly.io/docs/scrape-api/faq)instead.

[What is MCP and why should I use it?](https://scrapfly.io/docs/mcp/faq#what-is-mcp)
------------------------------------------------------------------------------------

#General

The **Model Context Protocol (MCP)** is an open standard by Anthropic that enables AI models to interact with external tools and live data sources. Instead of relying solely on training data, AI can make real-time requests and receive structured responses.

Scrapfly's MCP server gives your AI direct access to web data through our production-grade scraping infrastructure-bypassing anti-bot protections, rendering JavaScript, and managing proxies automatically.

[How is MCP different from using Scrapfly's API directly?](https://scrapfly.io/docs/mcp/faq#mcp-vs-api)
-------------------------------------------------------------------------------------------------------

#General

MCP provides a standardized, AI-native interface. Key differences:

*   **Automated protocol handling** - Tool discovery, validation, and error handling built-in
*   **AI reasoning** - Your AI determines which tool to use without custom integration code
*   **Natural language** - Simply ask your AI; it handles the technical details
*   **Universal compatibility** - Works identically across Claude Desktop, Cursor, Cline, and custom clients

_Think of it as "AI-native" vs. "AI-compatible."_

[Which AI models and clients support MCP?](https://scrapfly.io/docs/mcp/faq#supported-clients)
----------------------------------------------------------------------------------------------

#General#Features

MCP is client-agnostic. Any AI model can use MCP tools if the client supports the protocol:

*   **Claude Desktop** - Native MCP support from Anthropic
*   **Cursor** - Full MCP integration
*   **Cline** (formerly Claude Dev) - VS Code extension with MCP
*   **Custom clients** - Build your own using the MCP SDK

[Is the MCP server open source?](https://scrapfly.io/docs/mcp/faq#open-source)
------------------------------------------------------------------------------

#General#Advanced

**Yes!** The Scrapfly MCP server is fully open source on [GitHub](https://github.com/scrapfly/scrapfly-mcp).

*   Self-host on your infrastructure
*   Contribute features and improvements
*   Fork for custom needs
*   Audit code for security and compliance

[How do I get started?](https://scrapfly.io/docs/mcp/faq#getting-started)
-------------------------------------------------------------------------

#Setup

1.   **Get an API key** - Sign up at [scrapfly.io/register](https://scrapfly.io/register) (1,000 free credits)
2.   **Configure your MCP client** - Add Scrapfly MCP server to your config file
3.   **Restart your client** - Claude Desktop, Cursor, etc.
4.   **Start scraping** - Ask your AI to scrape any website!

See the [Getting Started Guide](https://scrapfly.io/docs/mcp/getting-started) for detailed instructions.

[Where is the MCP configuration file located?](https://scrapfly.io/docs/mcp/faq#config-location)
------------------------------------------------------------------------------------------------

#Setup

**Claude Desktop:**

*   **macOS:**`~/Library/Application Support/Claude/claude_desktop_config.json`
*   **Windows:**`%APPDATA%\Claude\claude_desktop_config.json`

**Cursor:**

*   Settings → Features → MCP Servers
*   Or edit `.cursor/mcp.json` in your workspace

[My MCP setup isn't working. What should I check?](https://scrapfly.io/docs/mcp/faq#setup-not-working)
------------------------------------------------------------------------------------------------------

#Setup#Troubleshooting

Common troubleshooting steps:

1.   **Verify API key** - Check for typos, ensure key is active
2.   **Validate JSON syntax** - No trailing commas, proper quotes
3.   **Restart client** - Completely quit and relaunch
4.   **Check logs** - Look for error messages
5.   **Test connection** - Run `npx mcp-remote https://mcp.scrapfly.io/mcp?key=YOUR_KEY`
6.   **Verify Node.js** - Ensure npx/Node.js is installed

[Can I use multiple Scrapfly projects?](https://scrapfly.io/docs/mcp/faq#multiple-projects)
-------------------------------------------------------------------------------------------

#Setup#Features

Yes! Configure multiple MCP servers with different API keys:

```
{
  "mcpServers": {
    "scrapfly-production": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.scrapfly.io/mcp?key=PROD_KEY"]
    },
    "scrapfly-development": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.scrapfly.io/mcp?key=DEV_KEY"]
    }
  }
}
```

[When should I use OAuth2 vs API key authentication?](https://scrapfly.io/docs/mcp/faq#oauth-vs-apikey)
-------------------------------------------------------------------------------------------------------

#Authentication#Security

| Scenario | Recommended Method |
| --- | --- |
| Personal laptop, local development | Query Parameter (API key in URL) |
| Production deployment | **OAuth2** |
| Remote MCP server | **OAuth2** |
| Shared/team environment | **OAuth2** |
| Custom programmatic client | Authorization Header |

See the [Authentication Guide](https://scrapfly.io/docs/mcp/authentication) for details.

[How does the OAuth2 flow work?](https://scrapfly.io/docs/mcp/faq#oauth-flow)
-----------------------------------------------------------------------------

#Authentication

1.   Your MCP client connects without an API key
2.   Server initiates OAuth2 flow and provides authorization URL
3.   You open the URL in your browser and log in to Scrapfly
4.   You grant permission for MCP access
5.   Server receives token and stores it securely
6.   Future requests use the stored token automatically

Tokens automatically refresh before expiration, and you can revoke access anytime from your dashboard.

[How often should I rotate API keys?](https://scrapfly.io/docs/mcp/faq#api-key-rotation)
----------------------------------------------------------------------------------------

#Authentication#Security

**With OAuth2:** Token rotation is automatic - no manual intervention needed.

**With API keys:** We recommend rotating keys every 90 days as a security best practice. Generate new keys in your [dashboard](https://scrapfly.io/dashboard).

[When should I use `web_get_page` vs `web_scrape`?](https://scrapfly.io/docs/mcp/faq#web-get-page-vs-web-scrape)
----------------------------------------------------------------------------------------------------------------

#Tools

**Use `web_get_page` when:**

*   You just need the page content quickly
*   Simple scraping without complex interactions
*   Cost optimization is important (uses fewer credits)

**Use `web_scrape` when:**

*   You need browser automation (clicks, form fills, scrolling)
*   Authentication/login flows are required
*   Custom headers, cookies, or POST requests needed
*   Multiple screenshots per request
*   Complex LLM-powered data extraction

[What is the `pow` parameter?](https://scrapfly.io/docs/mcp/faq#pow-parameter)
------------------------------------------------------------------------------

#Tools

`pow` stands for "Proof of Work" and is a required parameter for scraping tools. It's obtained by calling the `scraping_instruction_enhanced` tool first:

1.   AI calls `scraping_instruction_enhanced`
2.   Tool returns instructions + POW value
3.   AI uses POW value in `web_get_page` or `web_scrape` calls

This ensures AI models follow best practices and understand rate limits before making requests.

#Tools#Features

Pre-trained extraction models for common data types:

*   `product` / `product_listing` - E-commerce products
*   `article` - News articles and blog posts
*   `review_list` - Customer reviews
*   `job_posting` / `job_listing` - Job postings
*   `real_estate_property` / `real_estate_property_listing` - Property listings
*   `hotel` / `hotel_listing` - Hotel information
*   `event` - Event details
*   `organization` - Company/org information
*   `social_media_post` - Social media content
*   And more!

See the [Tools documentation](https://scrapfly.io/docs/mcp/tools#extraction-models) for the complete list.

#Tools#Features

Yes! Use the `extraction_prompt` parameter in `web_scrape`:

```
{
  "tool": "web_scrape",
  "parameters": {
    "url": "https://web-scraping.dev",
    "pow": "...",
    "extraction_prompt": "Extract all product names, prices, and availability status as a JSON array"
  }
}
```

Scrapfly's LLM will process the page and extract data according to your custom prompt.

[Are there rate limits?](https://scrapfly.io/docs/mcp/faq#rate-limits)
----------------------------------------------------------------------

#Features

Yes, Scrapfly has concurrency limits that vary by subscription plan. Concurrency measures the number of simultaneous requests that can be in flight at once.

You can check your current concurrency limits and usage using the `info_account` MCP tool, or by viewing your plan details on the [pricing page](https://scrapfly.io/pricing).

See the [Scrape API FAQ](https://scrapfly.io/docs/scrape-api/faq#concurrency) for more details about concurrency and how it works.

[What's included in the free tier?](https://scrapfly.io/docs/mcp/faq#free-tier)
-------------------------------------------------------------------------------

#Billing

New accounts get **1,000 free API credits** to test all features. No credit card required.

A simple page fetch typically costs 1-3 credits. Advanced features (JavaScript rendering, residential proxies, etc.) cost more. See the [pricing page](https://scrapfly.io/pricing) for details.

[How much does each request cost?](https://scrapfly.io/docs/mcp/faq#credit-costs)
---------------------------------------------------------------------------------

#Billing

| Feature | Credit Cost |
| --- | --- |
| Base scrape request | 1-3 credits |
| JavaScript rendering | +5 credits |
| Anti-scraping protection (ASP) | +10-30 credits (variable) |
| Residential proxies | +25 credits |
| Screenshot | +5 credits each |
| LLM extraction | +10-50 credits (variable) |

Actual cost is returned in every response. Check the [billing documentation](https://scrapfly.io/docs/scrape-api/billing) for details.

[How can I optimize costs?](https://scrapfly.io/docs/mcp/faq#optimize-costs)
----------------------------------------------------------------------------

#Billing

*   **Use `web_get_page`** instead of `web_scrape` for simple requests
*   **Disable `render_js`** for static pages
*   **Start with datacenter proxies** - Only escalate to residential if blocked
*   **Enable caching** - Set `cache: true` for frequently accessed pages
*   **Use extraction models** - Pre-trained models are more efficient than custom prompts
*   **Check `scraping_instruction_enhanced`** - Get optimal configurations

[How do I track my usage?](https://scrapfly.io/docs/mcp/faq#track-usage)
------------------------------------------------------------------------

#Billing

1.   **MCP tool** - Call `info_account` to get real-time usage stats
2.   **Dashboard** - View detailed usage in your [Scrapfly dashboard](https://scrapfly.io/dashboard)
3.   **Response headers** - Every scraping response includes cost in headers

[I'm getting blocked by websites. How can I avoid this?](https://scrapfly.io/docs/mcp/faq#getting-blocked)
----------------------------------------------------------------------------------------------------------

#Troubleshooting

1.   **Enable ASP** - Anti-scraping protection is on by default in `web_get_page`
2.   **Use residential proxies** - Set `proxy_pool: "public_residential_pool"`
3.   **Rotate country** - Try different proxy locations
4.   **Adjust timing** - Add `rendering_wait` to appear more human-like
5.   **Check robots.txt** - Respect website scraping policies

[JavaScript content isn't rendering. What's wrong?](https://scrapfly.io/docs/mcp/faq#js-not-rendering)
------------------------------------------------------------------------------------------------------

#Troubleshooting

Ensure `render_js: true` is set. Also check:

*   Add `rendering_wait` - Give page time to load
*   Use `wait_for_selector` - Wait for specific elements
*   Check network inspector - Some sites block headless browsers
*   Enable ASP - Helps bypass headless browser detection

[Requests are slow. How can I speed them up?](https://scrapfly.io/docs/mcp/faq#slow-requests)
---------------------------------------------------------------------------------------------

#Troubleshooting

*   **Disable unnecessary features** - Turn off `render_js` if not needed
*   **Use datacenter proxies** - Faster than residential
*   **Reduce `rendering_wait`** - Don't wait longer than necessary
*   **Use webhooks** - For long-running requests, get results asynchronously
*   **Request multiple pages in parallel** - MCP supports concurrent tool calls

[Is my scraped data stored by Scrapfly?](https://scrapfly.io/docs/mcp/faq#data-stored)
--------------------------------------------------------------------------------------

#Security

Scrape requests and responses are **temporarily logged** for debugging and monitoring (visible in your dashboard). Log retention periods vary by subscription plan-see the [Monitoring documentation](https://scrapfly.io/docs/monitoring#log-retention) for details.

**Privacy Protection:** Scrapfly automatically filters sensitive data from logs. Passwords, tokens, API keys, emails, and other credentials matching common patterns (e.g., `password`, `token`, `secret`, `auth`) are automatically redacted and replaced with `<SECRET>` in stored logs.

You can disable logging entirely by adjusting settings in [Project Settings](https://scrapfly.io/docs/project).

[How secure are API keys?](https://scrapfly.io/docs/mcp/faq#api-key-security)
-----------------------------------------------------------------------------

#Security

API keys are transmitted over HTTPS and stored securely. Best practices:

*   Never commit keys to version control
*   Use OAuth2 for production and shared environments
*   Rotate keys regularly (every 90 days)
*   Use project-specific keys to limit scope
*   Monitor usage for anomalies

#Security

Yes. Scrapfly is GDPR compliant. We:

*   Process data according to our [Privacy Policy](https://scrapfly.io/privacy-policy)
*   Support data deletion requests
*   Provide data export functionality
*   Use EU-based infrastructure for EU customers (available on request)

[Can I self-host the MCP server?](https://scrapfly.io/docs/mcp/faq#self-hosting)
--------------------------------------------------------------------------------

#Advanced

Yes! The MCP server is fully open source. Self-hosting steps:

1.   Clone the repository: `git clone https://github.com/scrapfly/scrapfly-mcp`
2.   Install dependencies: `npm install`
3.   Configure your Scrapfly API key
4.   Run the server: `npm start`

See the [GitHub README](https://github.com/scrapfly/scrapfly-mcp#self-hosting) for detailed instructions.

[Can I add custom tools to the MCP server?](https://scrapfly.io/docs/mcp/faq#custom-tools)
------------------------------------------------------------------------------------------

#Advanced

Yes! Since the server is open source, you can:

*   Fork the repository
*   Add your custom tool implementations
*   Register new tools in the MCP server
*   Self-host with your custom tools

Contributions are welcome! Submit a pull request to share tools with the community.

[How do webhooks work with MCP?](https://scrapfly.io/docs/mcp/faq#webhooks)
---------------------------------------------------------------------------

#Advanced

For long-running requests, use webhooks to get results asynchronously:

1.   Include `webhook: "https://your-endpoint.com/callback"` in your request
2.   Scrapfly returns immediately with request ID
3.   When scraping completes, Scrapfly POSTs results to your webhook
4.   Your AI can poll or wait for the webhook callback

##### Still Have Questions?

Get help from our team with any questions not covered in this FAQ.

[Contact Support](https://scrapfly.io/docs/support)
