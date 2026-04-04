# Source: https://grafbase.com/docs/platform/grafbase-remote-mcp.md

# Grafbase Remote MCP

The Grafbase Dashboard and the Grafbase CLI interact with the platform over a GraphQL API. The Grafbase API is also available as Model Context Protocol server, implemented with the [Grafbase Gateway's built-in MCP server](https://grafbase.com/docs/gateway/mcp.md).

Since it implements the latest version of the MCP spec, you only need to configure the URL of the server to connect it to your client of choice. Here is what it looks like in [Cursor](https://cursor.com/):

```json
{
  "mcpServers": {
    "grafbase": {
      "url": "https://api.grafbase.com/mcp"
    }
  }
}
```

Your client will initiate the login process, just the same as logging in on the dashboard at grafbase.com or with the CLI using `grafbase login`. After that, you can ask questions and query data about your graphs, subgraphs, schemas, analytics, [schema proposals](https://grafbase.com/docs/platform/schema-proposals.md) and more.