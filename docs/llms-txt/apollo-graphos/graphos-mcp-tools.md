# Source: https://www.apollographql.com/docs/graphos/platform/graphos-mcp-tools.md

# GraphOS MCP Tools

GraphOS MCP Tools provide access to Apollo's documentation and graph-building capabilities through Model Context Protocol (MCP). Connect these tools to your AI assistants to access Apollo's documentation and best practices directly in your agentic development workflows.

These tools help you build and evolve graphs, prototype API integrations, and experiment with different design approaches through natural language interactions with your AI assistant.

You can access GraphOS MCP Tools at `https://mcp.apollographql.com`.

## Available tools

### Apollo Docs Search

**Purpose**: Search across Apollo's official documentation to find the most relevant guides, examples, and best practices for GraphQL, GraphOS, schema design, deployment best practices, connectors, and more.

**Example**: "How do I enable entity caching with the Apollo Router?"

**Result**:

### Apollo Docs Read

**Purpose**: Retrieve the full Markdown content of any Apollo documentation page so your agent can go beyond code snippets and provide complete, detailed guidance.

**Example**: "Fetch the Router YAML config reference and list the top level properties."

**Result**:

### Apollo Connectors Spec

**Purpose**: Access the official specification for Apollo Connectors, giving your agent the knowledge it needs to create and modify Connectors in a schema.

**Examples**: "Add weather details to my schema using [https://api.weather.gov](https://api.weather.gov/) so I can expose weather conditions for airport cities."

**Result**: The output is too large to show, but your agentic coding tool will use the Apollo Connectors Spec tool to generate a graph that integrates with the [https://api.weather.gov](https://api.weather.gov/) REST API.

## Connect your AI agents to GraphOS MCP Tools

You need an MCP-compatible coding client or agentic runtime (for example, Claude Code, Cursor, Codex, Gemini CLI, etc).

> Note: GraphOS MCP Tools require clients that support [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http).

### Using Claude

GraphOS MCP Tools is available as a built-in connector in [Claude](https://claude.ai/) or Claude Desktop. No API key or configuration file is required.

1. In Claude, click the **+** icon in the chat input and select **Connectors**.

2. Find **GraphOS MCP Tools** in the list and click it to open the connector detail page, then click **Connect**.

3. Once connected, a toggle appears in the chat input. Enable it to give Claude access to Apollo's documentation and graph-building tools in that conversation. Claude automatically determines when to trigger the tools based on your prompt and asks for your permission before running them.

### Using Claude Code

If you're using [Claude Code](https://code.claude.com/docs/en/mcp#option-1:-add-a-remote-http-server), run the following command in your terminal:

```bash
claude mcp add --transport http graphos-tools https://mcp.apollographql.com
```

### Using Cursor

If you're using [Cursor](https://cursor.com/docs/context/mcp#installing-mcp-servers), click the following button to open the installation dialog:

Click **Install** to complete the process.

### Using VS Code

If you're using [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers#_add-an-mcp-server), add the following to your MCP settings configuration file:

```json title=.vscode/mcp.json
{
  "mcpServers": {
    "graphos-tools": {
      "url": "https://mcp.apollographql.com"
    }
  }
}
```

Alternatively, you can run the following command in your terminal to add the server globally:

```bash
code --add-mcp "{\"name\":\"graphos-tools\",\"url\": \"https://mcp.apollographql.com\"}"
```

### Using Codex CLI

If you're using [OpenAI Codex CLI](https://github.com/openai/codex/blob/main/docs/config.md#mcp-cli-commands), run the following command in your terminal to add the server globally:

```bash
codex mcp add graphos-tools --url https://mcp.apollographql.com
```

You may also need to enable the RMCP feature in your configuration file to use streamable HTTP. Add the following to your Codex configuration:

```toml title=codex.toml
experimental_use_rmcp_client = true
```

### Using Gemini CLI

If you're using [Google Gemini CLI](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html#configuration-structure), add the following to your MCP configuration file:

```json title=settings.json
{
  "mcpServers": {
    "graphos-tools": {
      "httpUrl": "https://mcp.apollographql.com"
    }
  }
}
```

### Using Copilot

If you're using the [GitHub Copilot coding agent](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp), configure MCP servers through your repository settings on GitHub.com:

1. Navigate to your repository's **Settings** > **Copilot** > **Coding agent**.

2. In the **MCP configuration** section, add the following JSON:

   ```json
   {
     "mcpServers": {
       "graphos-tools": {
         "type": "http",
         "url": "https://mcp.apollographql.com",
         "tools": ["ApolloDocsRead", "ApolloDocsSearch", "ApolloConnectorsSpec"]
       }
     }
   }
   ```

3. Click **Save MCP configuration**.

### Using other MCP-compatible clients

You can connect GraphOS MCP Tools to any other MCP-compatible client that supports Streamable HTTP. Use the endpoint `https://mcp.apollographql.com` and follow your client's documentation for adding MCP servers.

## Verify the connection

Try a question to confirm the connection is working:

```text
What is the Apollo Router config file option to control health checks?
```

This triggers a response from the documentation tools similar to the following:

You're ready to use GraphOS MCP Tools in your agentic development workflows.
