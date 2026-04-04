# MCP Server

The CE.SDK MCP server provides a standardized interface that allows any compatible AI assistant to search and access our documentation. This enables AI tools like Claude, Cursor, and VS Code Copilot to provide more accurate, context-aware help when working with CE.SDK.

## What is MCP?[#](#what-is-mcp)

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that enables AI assistants to securely connect to external data sources. By connecting your AI tools to our MCP server, you get:

*   **Accurate answers**: AI assistants can search and retrieve the latest CE.SDK documentation
*   **Context-aware help**: Get platform-specific guidance for your development environment
*   **Up-to-date information**: Always access current documentation without relying on training data

## Available Tools[#](#available-tools)

The MCP server exposes two tools:

| Tool | Description |
| --- | --- |
| `search` | Search documentation by query string |
| `fetch` | Retrieve the full content of a document by ID |

## Server Endpoint[#](#server-endpoint)

| URL | Transport |
| --- | --- |
| `https://mcp.img.ly/mcp` | Streamable HTTP |

No authentication is required.

## Setup Instructions[#](#setup-instructions)

### Claude Code[#](#claude-code)

Add the MCP server with a single command:

Terminal window

```
claude mcp add --transport http imgly_docs https://mcp.img.ly/mcp
```

### Claude Desktop[#](#claude-desktop)

1.  Open Claude Desktop and go to **Settings** (click your profile icon)
2.  Navigate to **Connectors** in the sidebar
3.  Click **Add custom connector**
4.  Enter the URL: `https://mcp.img.ly/mcp`
5.  Click **Add** to connect

### Cursor[#](#cursor)

Add the following to your Cursor MCP configuration. You can use either:

*   **Project-specific**: `.cursor/mcp.json` in your project root
*   **Global**: `~/.cursor/mcp.json`

```
{  "mcpServers": {    "imgly_docs": {      "url": "https://mcp.img.ly/mcp"    }  }}
```

### VS Code[#](#vs-code)

Add to your workspace configuration at `.vscode/mcp.json`:

```
{  "servers": {    "imgly_docs": {      "type": "http",      "url": "https://mcp.img.ly/mcp"    }  }}
```

### Windsurf[#](#windsurf)

Add the following to your Windsurf MCP configuration at `~/.codeium/windsurf/mcp_config.json`:

```
{  "mcpServers": {    "imgly_docs": {      "serverUrl": "https://mcp.img.ly/mcp"    }  }}
```

### Other Clients[#](#other-clients)

For other MCP-compatible clients, use the endpoint `https://mcp.img.ly/mcp` with HTTP transport. Refer to your client’s documentation for the specific configuration format.

## Usage[#](#usage)

Once configured, your AI assistant will automatically have access to CE.SDK documentation. You can ask questions like:

*   “How do I add a text block in CE.SDK?”
*   “Show me how to export a design as PNG”
*   “What are the available blend modes?”

The AI will search our documentation and provide answers based on the latest CE.SDK guides and API references.

---



[Source](https:/img.ly/docs/cesdk/vue/get-started/existing-project-o8789u)