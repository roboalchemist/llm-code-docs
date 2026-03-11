# Source: https://docs.linkup.so/pages/integrations/mcp/mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Linkup MCP Server

> Linkup MCP Server allows you to use the Linkup API in your MCP clients.

Developed by Anthropic, the [Model Context Protocol](https://github.com/modelcontextprotocol) (MCP) is an open protocol that standardizes how applications provide context to LLMs. It is particularly helpful when building agents and complex workflows on top of LLMs.

> Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

-*Anthropic*

<Info>
  Learn more about the Model Context Protocol in Anthropic's [official documentation](https://modelcontextprotocol.io/introduction)
</Info>

<CardGroup cols={3}>
  <Card title="Remote MCP" icon="cloud" href="#remote-mcp">
    Use our hosted MCP endpoint (recommended)
  </Card>

  <Card title="MCPB Bundle" icon="cube" href="#mcpb-bundle">
    Single-file bundle for Claude Desktop
  </Card>

  <Card title="Local MCP" icon="computer" href="#local-mcp">
    Run MCP locally with NPM package
  </Card>
</CardGroup>

<Card title="GitHub Repository" icon="github" href="https://github.com/LinkupPlatform/linkup-mcp-server">
  View the source code and see detailed documentation
</Card>

<Tip>
  The Linkup MCP server is compatible with any MCP client, such as [Cursor](https://docs.cursor.com/context/model-context-protocol) or [Claude
  Desktop](https://modelcontextprotocol.io/quickstart/user). Choose between local installation or our hosted endpoint based on your needs.
</Tip>

## Features

The Linkup MCP server provides two powerful tools:

* **🔍 `linkup-search`**: Real-time web search with natural language queries
  * Standard and deep search modes
  * Access to current information from trusted sources

* **🌐 `linkup-fetch`**: Fetch and extract content from any webpage
  * Optional JavaScript rendering for dynamic content
  * Perfect for article extraction and content analysis

<img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/mcp/mcp_demo.gif?s=de115049197d3e3c40c318f6c158b4a4" alt="MCP demo" width="800" height="660" data-path="pages/integrations/mcp/mcp_demo.gif" />

## Remote MCP

Use our hosted MCP endpoint for a quick setup without any local installation. This is the recommended approach for most users.

### Prerequisites

To use Remote MCP, you need:

* A Linkup API key
* Any MCP client that supports HTTP/SSE connections

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

### Quick Start with Smithery

The easiest way to get started is using [Smithery](https://smithery.ai/server/@LinkupPlatform/linkup-mcp-server).
From there, you'll be able to install the server into your favorite MCP compatible client. The remote MCP server is using the Streamable HTTP transport.

### Manual Configuration

<Tabs>
  <Tab title="Cursor">
    [![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=linkup\&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbWNwLmxpbmt1cC5zby9tY3A%2FYXBpS2V5PVlPVVJfQVBJX0tFWSJ9)

    Add to your `~/.cursor/mcp.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "linkup": {
          "type": "http",
          "url": "https://mcp.linkup.so/mcp?apiKey=YOUR_API_KEY"
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    Add to your VS Code MCP config:

    ```json  theme={null}
    {
      "servers": {
        "linkup": {
          "url": "https://mcp.linkup.so/mcp?apiKey=YOUR_API_KEY",
          "type": "http"
        }
      }
    }
    ```
  </Tab>
</Tabs>

<Info>
  Don't forget to replace `YOUR_API_KEY` with your actual API key!
</Info>

## MCPB Bundle

Download a pre-built MCPB (MCP Bundle) - a self-contained, single-file package that works across compatible MCP clients. This is the recommended approach for Claude Desktop.

### What is MCPB?

MCPB (MCP Bundle) is a new format developed by Anthropic for distributing MCP servers. Learn more in the [official MCPB documentation](https://github.com/anthropics/mcpb).

### Download

**Quick Download:**

```bash  theme={null}
curl -L -o linkup-mcp-server.mcpb https://github.com/LinkupPlatform/linkup-mcp-server/releases/latest/download/linkup-mcp-server.mcpb
```

Or download directly from [here](https://github.com/LinkupPlatform/linkup-mcp-server/releases/latest/download/linkup-mcp-server.mcpb).

### Installation

<Steps>
  <Step title="Download the MCPB file">
    Use the curl command above or download from GitHub releases.
  </Step>

  <Step title="Install in Claude Desktop">
    Double-click the `.mcpb` file to install it in Claude Desktop.
  </Step>

  <Step title="Configure API Key">
    When prompted, enter your Linkup API key.
  </Step>
</Steps>

## Local MCP

Run the Linkup MCP server locally using NPM.

### Prerequisites

* A Linkup API key
* Node.js (v18.0.0 or higher)

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

### Configuration Examples

<Tabs>
  <Tab title="Claude Desktop">
    Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "linkup": {
          "command": "npx",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Cursor">
    Edit `~/.cursor/mcp.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "linkup": {
          "command": "npx",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    Add to your VS Code MCP config:

    ```json  theme={null}
    {
      "servers": {
        "linkup": {
          "command": "npx",
          "type": "stdio",
          "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_LINKUP_API_KEY"]
        }
      }
    }
    ```
  </Tab>
</Tabs>

Replace `YOUR_LINKUP_API_KEY` with your actual API key, then restart your application.

<Info>
  For more configuration examples and advanced usage, see the [GitHub README](https://github.com/LinkupPlatform/linkup-mcp-server#readme).
</Info>

## Available Tools

Once configured, you'll have access to two powerful tools:

### linkup-search

Search the web in real time to retrieve current information, facts, and news from trusted sources.

**Parameters:**

* `query` (required): Natural language search query. Full questions work best.
* `depth` (optional): Search depth - "standard" (default) or "deep"
  * **standard**: For queries with direct answers (weather, stock prices, simple facts)
  * **deep**: For complex research requiring analysis across multiple sources

**Example prompts:**

* "Search for the latest news about AI developments"
* "What's the current weather in Tokyo?"
* "Find information about the new EU AI Act"

### linkup-fetch

Fetch and extract content from any webpage URL.

**Parameters:**

* `url` (required): The URL to fetch content from
* `renderJs` (optional): Whether to render JavaScript content (default: false)
  * Enable for dynamic pages that load content via JavaScript
  * Note: Makes the request slower

**Example prompts:**

* "Fetch the content from [https://example.com/article](https://example.com/article)"
* "Get this blog post and summarize it: [https://blog.example.com/post](https://blog.example.com/post)"
* "What are the events happening in Paris this week? Fetch the content from [https://example.com/events](https://example.com/events)"

## Troubleshooting

### Authentication Format

**Important**: The new version (2.x) of the Linkup MCP server uses a different authentication format:

✅ **Correct (v2.x)**:

```json  theme={null}
{
  "args": ["-y", "linkup-mcp-server", "apiKey=YOUR_API_KEY"]
}
```

❌ **Old format (v1.x)**:

```json  theme={null}
{
  "env": {
    "LINKUP_API_KEY": "YOUR_API_KEY"
  }
}
```

If you were using v1.x, please update your configuration to the new format.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).