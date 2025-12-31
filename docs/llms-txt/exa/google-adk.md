# Source: https://docs.exa.ai/integrations/google-adk.md

# Google ADK

Learn how to use Exa's search API with Google's Agent Development Kit (ADK). Google ADK works with Exa through our MCP (Model Context Protocol) server.

For the official Google ADK documentation about Exa integration, visit the [Google ADK Exa integration page](https://google.github.io/adk-docs/tools/third-party/exa/).

## What is Google ADK?

Google's Agent Development Kit (ADK) is a simple framework for building AI agents. It helps developers create and run AI agents that can do different tasks. ADK works with Google's Gemini models and other AI systems. It makes building agents feel more like regular software development.

## Exa MCP Integration

Exa has an MCP server that works with Google ADK. This lets your ADK agents search the web, find similar content, get clean text from web pages, and do research - all using Exa websearch.

## Prerequisites

* Create an [API Key](https://dashboard.exa.ai/api-keys) in Exa.

## Use with Google ADK

You can use Exa with Google ADK in two ways: with a local MCP server or a remote MCP server.

### Local MCP Server

```python  theme={null}
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

EXA_API_KEY = "YOUR_EXA_API_KEY"

root_agent = Agent(
    model="gemini-2.5-pro",
    name="exa_agent",
    instruction="Help users get information from Exa",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "exa-mcp-server",
                        # (Optional) Choose which tools to use
                        # If you don't pick any tools, all tools will be used by default
                        # "--tools=get_code_context_exa,web_search_exa",
                    ],
                    env={
                        "EXA_API_KEY": EXA_API_KEY,
                    }
                ),
                timeout=30,
            ),
        )
    ],
)
```

### Remote MCP Server

```python  theme={null}
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

EXA_API_KEY = "YOUR_EXA_API_KEY"

root_agent = Agent(
    model="gemini-2.5-pro",
    name="exa_agent",
    instruction="""Help users get information from Exa""",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://mcp.exa.ai/mcp?exaApiKey=" + EXA_API_KEY,
                # (Optional) Choose which tools to use
                # If you don't pick any tools, all tools will be used by default
                # url="https://mcp.exa.ai/mcp?exaApiKey=" + EXA_API_KEY + "&enabledTools=%5B%22crawling_exa%22%5D",
            ),
        )
    ],
)
```

## More Resources

* [Exa MCP Server Documentation](https://docs.exa.ai/reference/exa-mcp)
* [Exa MCP Server Repository](https://github.com/exa-labs/exa-mcp-server)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt