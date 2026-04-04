# Source: https://docs.together.ai/docs/mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Together AI MCP Server

> Install our MCP server in Cursor, Claude Code, or OpenCode in 1 click.

**Model Context Protocol** (MCP) allows your AI coding agents to access external tools and data sources. Connect to the Together AI documentation via MCP to get instant answers, code examples, and context about our platform directly in your favorite AI coding tools.

# One-Click Installs

Follow these quick one-click installs to get the Together AI MCP Server running in Cursor, Claude Code, OpenCode, VS Code, or Codex!

### Quick Start (Universal)

```bash  theme={null}
npx add-mcp https://docs.together.ai/mcp
```

### Claude Code

```bash  theme={null}
claude mcp add --transport http "TogetherAIDocs" https://docs.together.ai/mcp
```

### Cursor

<a href="https://cursor.com/en/install-mcp?name=together-docs&config=eyJ1cmwiOiJodHRwczovL2RvY3MudG9nZXRoZXIuYWkvbWNwIn0%3D" target="_blank" rel="noreferrer">
  <img noZoom alt="Install MCP Server" src="https://cursor.com/deeplink/mcp-install-dark.svg" width="126" height="28" />
</a>

For manual configuration, add this to your Cursor MCP settings:

```json  theme={null}
{
  "mcpServers": {
    "together-docs": {
      "url": "https://docs.together.ai/mcp"
    }
  }
}
```

### VS Code

[Install in VS Code](https://vscode.dev/redirect/mcp/install?name=Together%20AI%20Docs\&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fdocs.together.ai%2Fmcp%22%7D)

For manual configuration, add this to your VS Code settings.json:

```json  theme={null}
{
  "mcp": {
    "servers": {
      "together-docs": {
        "type": "http",
        "url": "https://docs.together.ai/mcp"
      }
    }
  }
}
```

### OpenAI Codex

See [OpenAI Codex](https://github.com/openai/codex) for more information.

**Remote Server Connection**

```toml  theme={null}
[mcp_servers.together_docs]
type = "http"
url = "https://docs.together.ai/mcp"
```

### Opencode

Add this to your Opencode configuration file.

**Remote Server Connection**

```json  theme={null}
{
  "mcp": {
    "together_docs": {
      "type": "remote",
      "url": "https://docs.together.ai/mcp",
      "enabled": true
    }
  }
}
```

## What you can do

Once installed, you supercharge your AI coding agents with direct knowledge about Together AI and can ask them to perform tasks like:

* "Write a script to do data processing with batch inference"
* "Build a simple chat app with Together's chat completions API"
* "What is the best open source model to use for frontier coding?"
* "How do I finetune my model on my own data?"

The MCP server provides tools to search and retrieve documentation content, making it easy to get accurate information without leaving your coding environment.

For more information about MCP, visit the [official MCP documentation](https://modelcontextprotocol.io/).


Built with [Mintlify](https://mintlify.com).