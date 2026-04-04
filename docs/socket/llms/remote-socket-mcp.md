# Source: https://docs.socket.dev/docs/remote-socket-mcp.md

# Remote Socket MCP

The easiest way to get started is to use our public Socket MCP server. **No API key or authentication required!** Click a button below to install the public server in your favorite AI assistant.

Click here to install Socket MCP in your IDE: [![Install in VS Code](https://img.shields.io/badge/VS_Code-Socket_MCP-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=socket-mcp\&config=\{"url":"https://mcp.socket.dev/","type":"http"}) [![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=socket-mcp\&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbWNwLnNvY2tldC5kZXYifQ%3D%3D)

## Manual Installation Instructions

<details>
  <summary><b>Install in Claude Desktop or Claude Code</b></summary>

  > \[!NOTE]\
  > Custom integrations are not available to all paid versions of Claude. Check [here](https://support.anthropic.com/en/articles/11175166-about-custom-integrations-using-remote-mcp) for more information.

  To use the public Socket MCP server with Claude Desktop:

  1. In Claude Desktop, go to Settings > Developer > Edit Config.

  2. Add the Socket MCP server configuration:

  ```json
  {
    "mcpServers": {
      "socket-mcp": {
        "type": "http",
        "url": "https://mcp.socket.dev/"
      }
    }
  }
  ```

  3. Save the configuration and restart Claude Desktop.

  4. Now you can ask Claude questions like "Check the security score for express version 4.18.2".

  The process is similar for Claude Code. See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp) for more details. Here's an example command to add the Socket MCP server:

  ```bash
  claude mcp add --transport http socket-mcp https://mcp.socket.dev/
  ```
</details>

<details>
  <summary><b>Install in VS Code</b></summary>

  You can install the Socket MCP server using the VS Code CLI:

  ```bash
  # For VS Code with GitHub Copilot
  code --add-mcp '{"name":"socket-mcp","type":"http","url":"https://mcp.socket.dev/}'
  ```

  After installation, the Socket MCP server will be available for use with your GitHub Copilot agent in VS Code.

  Alternatively, you can manually add it to your VS Code MCP configuration in `.vscode/mcp.json`:

  ```json
  {
    "servers": {
      "socket-mcp": {
        "type": "http",
        "url": "https://mcp.socket.dev/"
      }
    }
  }
  ```
</details>

<details>
  <summary><b>Install in Cursor</b></summary>

  Go to `Cursor Settings` -> `MCP` -> `Add new MCP Server`. Name it "socket-mcp", use `http` type with URL `https://mcp.socket.dev/`.

  ```json
  {
    "mcpServers": {
      "socket-mcp": {
        "type": "http",
        "url": "https://mcp.socket.dev/"
      }
    }
  }
  ```
</details>

<details>
  <summary><b>Install in Windsurf</b></summary>

  > \[!WARNING]\
  > Windsurf does not support `http` type MCP servers yet. Use the `stdio` configuration [below](#option-2a-stdio-mode-default).

  To use the Socket MCP server in Windsurf:

  1. Open Windsurf Settings
  2. Navigate to MCP Servers section
  3. Add a new server with the following configuration:

  ```json
  {
      "mcpServers": {
          "socket-mcp": {
              "serverUrl": "https://mcp.socket.dev/mcp"
          }
      }
  }
  ```

  4. Save the configuration and restart Windsurf if needed.
</details>