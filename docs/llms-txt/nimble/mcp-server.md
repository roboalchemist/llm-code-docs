# Source: https://docs.nimbleway.io/ai-agents/mcp-server.md

# MCP Server

<mark style="color:purple;">**`Nimble Labs Feature`**</mark>

{% hint style="info" %}
The features included in the "Labs" section are **experimental** and provided for evaluation purposes only. These features may not be fully tested, stable, or integrated with all existing functionality. Future versions may differ from the current implementation.

If you are interested in using any of these experimental features in a production environment, please reach out to our team for guidance and support. Your feedback is valuable in helping us improve these features, and we welcome any issues, suggestions, or feedback you may have.
{% endhint %}

Most AI agents are blind. They hallucinate, they guess, they fail. All because they can't see the real world.

[Model Control Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard developed by [Anthropic](https://www.anthropic.com/). It gives AI agents a simple, standardized way to plug into tools, data, and services.

The Nimble MCP Server bridges this gap by providing real-time, structured web data that transforms how agents interact with the digital world. With tools for web search, location data, and business intelligence, it turns chaotic web information into signals your agents can actually use.

### Available Tools

The Nimble MCP Server provides powerful tools for web data extraction, including generic web retrieval from any website, Google Maps intelligence, and specialized e-commerce data collection. These tools enable real-time content extraction through web searches, comprehensive local business data gathering, and structured product information retrieval from major retail platforms. Whether you need to monitor competitors, analyze customer reviews, track product prices, or gather market intelligence, Nimble's tools transform unstructured web data into actionable insights.

→ [View detailed documentation for all tools](https://docs.nimbleway.io/ai-agents/mcp-server/available-tools)

### Quick Start

The fastest way to use this MCP server is to connect to our official remote instance using Server-Sent Events (SSE) transport. This allows you to use the server without installing it locally.

#### Remote Connection Setup (SSE)

1. **Get a Nimble API Key**:
   * Register for an account at [Nimble's signup page](https://app.nimbleway.com/signup)
   * Navigate to your "Account settings" page and open the "API KEYS" tab
   * Click on "+ Add Key" to generate a new token and copy it.<br>

2. **Prerequisites**:
   * Ensure you have [Node.js and npm](https://nodejs.org/) installed on your system
   * The configuration below uses `npx` to run the MCP remote client without needing a local installation<br>

3. **Add Configuration to your MCP-Compatible Client**:

   This configuration works with [Claude Desktop](https://claude.ai/download), [Cursor](https://www.cursor.com/), [Qodo](https://www.qodo.ai/), and any other client that supports Model Context Protocol (MCP).<br>

   Add this configuration to your `claude_desktop_config.json`:

   ```
   {
     "mcpServers": {
       "nimble-mcp-server": {
         "command": "npx",
         "args": [
           "-y", "mcp-remote@latest", "https://mcp.nimbleway.com/sse", 
           "--header", "Authorization:${NIMBLE_API_KEY}"
           ],
         "env": {
           "NIMBLE_API_KEY": "Bearer XXX"
         }
       }
     }
   }
   ```

   \
   \&#xNAN;***Note:***&#x20;

   * *Replace `Bearer XXX` with your actual Nimble API key.*
   * ***After modifying the config file, you must restart Claude Desktop** for changes to take effect*
     * ***macOS users**: Quit Claude Desktop completely (Cmd+Q) and relaunch*
     * ***Windows users**: You may need to fully terminate the application:*
       1. *Close Claude Desktop window*
          1. *Open Task Manager (Ctrl+Shift+Esc)*
          2. *Find and end any "Claude" processes*
          3. *Relaunch Claude Desktop*

   *For detailed setup instructions and troubleshooting, see the* [*official MCP quickstart guide*](https://modelcontextprotocol.io/quickstart/user)*.*

   &#x20;

4. **Start using the MCP tools with your AI agent!**

<figure><img src="https://1919898886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZNy4aqrBN53tR8DpTEuW%2Fuploads%2FUXumrKmCQv9YfvSzptSN%2Fimage.png?alt=media&#x26;token=170fd42b-1050-42a1-b13d-73705227f43d" alt=""><figcaption><p>Example using Nimble Maps API in Claude Desktop</p></figcaption></figure>

We can't wait to see what cool things your AI agents will do with our tools! Have ideas for making these tools better or need help getting started? Drop us a line - we're here to help your agents get the data they need!
