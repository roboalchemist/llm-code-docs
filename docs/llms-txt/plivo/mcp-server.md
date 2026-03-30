# Source: https://plivo.com/docs/faq/developer-tools/mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI-Powered Documentation Search

> Connect your AI assistant to Plivo documentation using the Model Context Protocol (MCP)

Plivo provides an MCP server that allows AI assistants to search our documentation. Use it to get accurate, contextual answers about Plivo APIs, SDKs, and features directly in your development environment.

**MCP Server URL:** `https://plivo.com/docs/mcp`

***

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that lets AI applications connect to external tools and data sources. By connecting your AI assistant to Plivo's MCP server, it can search our documentation and provide accurate answers with direct links to relevant pages.

***

## Available Tools

| Tool          | Description                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| `SearchPlivo` | Search across the Plivo knowledge base to find relevant information, code examples, API references, and guides |

***

## Setup by Client

### Claude Desktop

Add to your Claude Desktop config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json  theme={null}
{
  "mcpServers": {
    "plivo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://plivo.com/docs/mcp"]
    }
  }
}
```

Restart Claude Desktop after saving.

### Claude Code (CLI)

```bash  theme={null}
claude mcp add plivo --transport http https://plivo.com/docs/mcp
```

### Cursor

Go to **Settings → MCP Servers** and add:

```json  theme={null}
{
  "mcpServers": {
    "plivo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://plivo.com/docs/mcp"]
    }
  }
}
```

### Cline (VS Code)

Open Cline settings and add to MCP configuration:

```json  theme={null}
{
  "plivo": {
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://plivo.com/docs/mcp"]
  }
}
```

### Windsurf

Add to your MCP configuration:

```json  theme={null}
{
  "mcpServers": {
    "plivo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://plivo.com/docs/mcp"]
    }
  }
}
```

***

## Using with OpenAI or Gemini

OpenAI and Google Gemini don't natively support MCP, but you can use MCP-compatible clients that support multiple models:

### Option 1: Use Cursor or Cline

Both Cursor and Cline support MCP and allow you to switch between Claude, GPT-4, and Gemini models:

1. Configure the MCP server as shown above
2. Change your model to GPT-4o or Gemini in the client settings
3. The client bridges MCP tools to the model's function calling

### Option 2: Direct API Integration

Call the MCP endpoint directly and include the results in your prompt:

```python  theme={null}
import requests
import openai  # or google.generativeai

# Search Plivo documentation
response = requests.post(
    "https://plivo.com/docs/mcp",
    json={
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "SearchPlivo",
            "arguments": {"query": "audio streaming websocket"}
        },
        "id": 1
    }
)
docs_context = response.json()

# Use with OpenAI
completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f"Answer using this context:\n{docs_context}"},
        {"role": "user", "content": "How do I set up audio streaming with Plivo?"}
    ]
)
print(completion.choices[0].message.content)
```

### Option 3: LangChain Integration

```python  theme={null}
from langchain_mcp import MCPToolkit
from langchain_openai import ChatOpenAI

toolkit = MCPToolkit(server_url="https://plivo.com/docs/mcp")
tools = toolkit.get_tools()

llm = ChatOpenAI(model="gpt-4o").bind_tools(tools)
response = llm.invoke("How do I make an outbound call with Plivo?")
```

***

## Example Queries

Once connected, try asking your AI assistant:

* "How do I make an outbound call with Plivo in Python?"
* "What are the audio streaming WebSocket message formats?"
* "Show me how to set up a Pipecat voice agent"
* "What XML elements can I use for IVR?"
* "How do I handle incoming SMS messages?"

The AI will search Plivo documentation and provide accurate answers with links to the relevant pages.

***

## Troubleshooting

| Issue                  | Solution                                                              |
| ---------------------- | --------------------------------------------------------------------- |
| "MCP server not found" | Ensure you have Node.js installed and `npx` is available in your PATH |
| Connection timeout     | Check your network connection and firewall settings                   |
| No search results      | Try rephrasing your query with different keywords                     |
| Tool not appearing     | Restart your AI client after configuration changes                    |

***

## Related

* [Model Context Protocol](https://modelcontextprotocol.io/) - MCP specification and documentation
* [MCP Remote](https://www.npmjs.com/package/mcp-remote) - NPM package for connecting to remote MCP servers
