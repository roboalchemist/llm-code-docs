# Source: https://docs.startree.ai/corecapabilities/ai/mcp/cursor.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cursor IDE

# Cursor IDE Integration

Configure Cursor IDE to connect with your StarTree MCP Server for natural language analytics directly within your development environment.

## Prerequisites

* Cursor IDE installed ([download here](https://cursor.sh/))
* **StarTree MCP Server already installed** ([see installation guide](https://docs.startree.ai/corecapabilities/ai/mcp/installation))

## Configuration Steps

Since you already have a working `.env` file in your mcp-pinot directory, Cursor will automatically use those settings. No need to duplicate configuration!

Create or edit `~/.cursor/mcp.json`

```json  theme={null}
{
  "mcpServers": {
    "pinot": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-pinot",
        "run",
        "mcp_pinot/server.py"
      ]
    }
  }
}
```

Replace `/path/to/mcp-pinot` with the absolute path to your mcp-pinot directory

Add this config in Cursor MCP global settings

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/images/Screenshot2025-06-04at7.42.51AM.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=875c61eb96e5b3b93db34f57127a4184" alt="Screenshot2025 06 04at7 42 51AM Pn" width="1954" height="732" data-path="images/Screenshot2025-06-04at7.42.51AM.png" />

### Restart Cursor IDE

Completely restart Cursor IDE for the configuration to take effect.

## Verify Connection

Try asking questions related to Pinot:

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/images/Screenshot2025-06-04at7.44.46AM.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=7b7045352a54cf86e99fe8bbb65f6cb6" alt="Screenshot2025 06 04at7 44 46AM Pn" width="1052" height="1060" data-path="images/Screenshot2025-06-04at7.44.46AM.png" />

Built with [Mintlify](https://mintlify.com).
