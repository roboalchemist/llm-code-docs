# Source: https://docs.socket.dev/docs/local-socket-mcp.md

# Local Socket MCP

If you prefer to run your own instance, you can deploy the Socket MCP server locally using either stdio or HTTP modes.

## Getting an API key

To use a local Socket MCP Server, you need to create an API key. You can do this by following [these steps](https://docs.socket.dev/reference/creating-and-managing-api-tokens). The only required permission scope is `packages:list`, which allows the MCP server to query package metadata for dependency scores.

For local deployment, you have two options:

## Stdio Mode (Default)

Click a button below to install the self-hosted stdio server in your favorite AI assistant.

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Socket_MCP-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=socket-mcp\&config=\{"command":"npx","args":\["@socketsecurity/mcp@latest"],"type":"stdio"}) [![Install in Cursor (stdio)](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=socket-mcp-stdio\&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAc29ja2V0c2VjdXJpdHkvbWNwQGxhdGVzdCJdLCJlbnYiOnsiU09DS0VUX0FQSV9LRVkiOiJ5b3VyLWFwaS1rZXktaGVyZSJ9fQ==)

Claude Code (stdio mode) can be set up with the following command:

```bash
claude mcp add socket-mcp -e SOCKET_API_KEY="your-api-key-here" -- npx -y @socketsecurity/mcp@latest
```

This is how the configuration looks like on most MCP clients:

```json
{
  "mcpServers": {
    "socket-mcp": {
      "command": "npx",
      "args": ["@socketsecurity/mcp@latest"],
      "env": {
        "SOCKET_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

This approach automatically uses the latest version without requiring global installation.

## HTTP Mode

1. Run the server in HTTP mode using npx:
   ```bash
   MCP_HTTP_MODE=true SOCKET_API_KEY=your-api-key npx @socketsecurity/mcp@latest --http
   ```

2. Configure your MCP client to connect to the HTTP server:
   ```json
   {
     "mcpServers": {
       "socket-mcp": {
         "type": "http",
         "url": "http://localhost:3000"
       }
     }
   }
   ```