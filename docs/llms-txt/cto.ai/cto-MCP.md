# Source: https://docs.cto.new/integrations/cto-MCP.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cto.new/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server

> Connect to cto from other tools via MCP

## Functionality

The MCP server lets you access select cto.new functionality. Currently you can:

* List repos/projects configured with cto.new
* List tasks previously run (overview of 10 most recent tasks with status, PR, etc)
* Start a task (provide a prompt to start a remote task in cto.new)

<Warning>
  The MCP server is in beta
</Warning>

## Auth

Authentication is done via OAuth which your client must support. Clients with this support include:

* Cursor
* VSCode
* Claude

## Setup

Our MCP sever supports streamable HTTP transport only.

You can access the MCP server here:

`https://mcp.enginelabs.ai/mcp`

Here is an example `.cursor/mcp.json` file:

```
{
  "mcpServers": {
    "cto.new": {
      "url": "https://mcp.enginelabs.ai/mcp"
    }
  }
}
```

Our MCP server is remote only.

For clients that do not natively support OAuth with HTTP transport MCP servers, you can use the `mcp-remote` package to wrap the MCP server:

```
{
  "mcpServers": {
    "cto.new": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.enginelabs.ai/mcp"]
    }
  }
}
```


Built with [Mintlify](https://mintlify.com).