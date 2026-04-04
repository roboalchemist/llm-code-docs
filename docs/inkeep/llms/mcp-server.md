# Source: https://docs.inkeep.com/talk-to-your-agents/mcp-server

# MCP Server (/talk-to-your-agents/mcp-server)

Learn how to use the MCP server to talk to your agents



The MCP server allows you to talk to your agents through the Model Context Protocol.

<>
  ## Authentication

  Choose the authentication method:

  <Tabs>
    <Tab title="Using an API Key">
      **Create an API Key:**

      1. Open the Visual Builder Dashboard
      2. Go to your Project → **API Keys**
      3. Click **Create**, select the target agent
      4. Copy the API key (it will be shown once) and store it securely

      **Request Header:**

      ```http
      Authorization: Bearer <api_key>
      ```
    </Tab>

    <Tab title="Without API key">
      When running the API server locally with `pnpm dev`, authentication is automatically bypassed. You can use headers in the request instead:

      **Request Headers:**

      ```http
      x-inkeep-tenant-id: <tenant-id>
      x-inkeep-project-id: <project-id>
      x-inkeep-agent-id: <agent-id>
      ```

      <Warning>
        This mode is for development only. Never use in production as it bypasses all security checks.
      </Warning>
    </Tab>
  </Tabs>

  See [Authentication → Run API](/api-reference/authentication/run-api) for more details.
</>

## MCP Server Implementation

The MCP server is implemented in the `@inkeep/agents-api` library and provides a standard interface for agent communication.

## Available Tools

The MCP server exposes one core tool:

### send-query-to-agent

Sends a query to your agent's default sub-agent. This tool:

* **Name**: `send-query-to-agent`
* **Description**: Dynamically generated based on your agent's name and description
* **Parameters**:
  * `query` (string): The query to send to the agent
* **Returns**: The agent's response as text content

**Example usage in Cursor:**
When the MCP server is configured, Cursor will automatically discover this tool and you can use it by asking questions. The tool will route your query to the appropriate sub-agent in your agent and return the response.

The tool handles:

* Message creation and conversation management
* Sub-agent execution with your configured tools and capabilities
* Context resolution if your agent has context configuration
* Error handling and response formatting

## Using with Cursor

### Quick Install (Inkeep Hosted Docs MCP)

Install the Inkeep Agents documentation MCP server with one click:

<div
  style={{
  display: "flex",
  gap: "10px",
  marginBottom: "16px",
  flexWrap: "wrap",
}}
>
  <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=inkeep-agents&config=eyJ1cmwiOiJodHRwczovL2FnZW50cy5pbmtlZXAuY29tL21jcCJ9">
    <img src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add to Cursor" style={{ height: "40px" }} />
  </a>

  <a href="vscode:mcp/install?%7B%22name%22%3A%22inkeep-agents%22%2C%22type%22%3A%22sse%22%2C%22url%22%3A%22https%3A%2F%2Fagents.inkeep.com%2Fmcp%22%7D">
    <img src="https://img.shields.io/badge/VS_Code-Install_Inkeep_Agents-0098FF?style=flat-square&logo=visualstudiocode&logoColor=ffffff" alt="Install in VS Code" />
  </a>
</div>

### Manual Configuration

Add the following configuration to your Cursor MCP settings.

#### Example

Example when using an API key for auth:

```json
{
  "AgentName": {
    "type": "mcp",
    "url": "http://<your-agents-api-url>/run/v1/mcp",
    "headers": {
      "Authorization": "Bearer <agent_api_key>"
    }
  }
}
```

## Session Management (Required by MCP HTTP Transport)

* Initialize a session by sending an `initialize` JSON-RPC request to `/run/v1/mcp`.
* The server will respond and set `Mcp-Session-Id` in response headers.
* For all subsequent JSON-RPC requests in that session, include `Mcp-Session-Id` header with the value from initialization.

<Note>
  Session management is required by MCP’s HTTP transport. If `Mcp-Session-Id` is
  missing or invalid on follow-up requests, the server will return a JSON-RPC
  error (e.g., "Session not found").
</Note>

## Configuration Notes

* **URL**: Point to your `agents-api` instance (default: `http://localhost:3002`)
* **Headers**: Use the appropriate authentication mode per the section above
* **Authorization**: Only required outside development mode
