# Source: https://dev.writer.com/home/mcp-server.md

# MCP server

This guide shows you how to use the Writer MCP server to orchestrate multiple Writer API calls through AI assistants like [Claude Desktop](https://claude.ai/download) and [Cursor](https://www.cursor.com/), or your own custom MCP client.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that enables AI assistants to interact with external tools and data sources. After completing these steps, you can chain together multi-step workflows without hardcoding API calls.

## Install and configure the MCP server

### Set up your Writer API key

The MCP server requires your Writer API key as an environment variable. If you don't have an API key, you can [create one](/api-reference/api-keys).

Store your API key in a `.env` file with the name `WRITER_API_KEY`. For example:

```bash  theme={null}
export WRITER_API_KEY=your-api-key-here
```

Then source the environment file in your shell:

```bash  theme={null}
source .env
```

<Note>
  The MCP server will show a fatal error if the `WRITER_API_KEY` environment variable is missing or empty. Make sure to set this environment variable before running the MCP server.
</Note>

### Install and run the MCP server

You can install and run the Writer MCP server using [`npx`](https://docs.npmjs.com/cli/v8/commands/npx). Set the `WRITER_API_KEY` environment variable before running the MCP server.

The following command installs and runs the latest version of the Writer MCP server:

```bash  theme={null}
npx -y writer-sdk-mcp@latest
```

<Note>
  You can also install the MCP server globally and run it anytime.

  ```bash  theme={null}
  npm install -g writer-sdk-mcp

  mcp-server
  ```
</Note>

### Configure your MCP client

Add the Writer MCP server to your MCP client configuration, such as [`claude_desktop_config.json` for Claude Desktop](https://modelcontextprotocol.io/docs/develop/connect-local-servers) or [`mcp.json` for Cursor](https://cursor.com/docs/context/mcp). For example, here's how to configure the MCP server for Claude Desktop:

<Tabs>
  <Tab title="Claude Desktop">
    Add to your [`claude_desktop_config.json`](https://modelcontextprotocol.io/docs/develop/connect-local-servers):

    ```json claude_desktop_config.json theme={null}
    {
      "mcpServers": {
        "writer": {
          "command": "npx",
          "args": ["-y", "writer-sdk-mcp@latest"],
          "env": {
            "WRITER_API_KEY": "your-api-key-here"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Cursor">
    Add to your [`mcp.json`](https://cursor.com/docs/context/mcp):

    ```json mcp.json theme={null}
    {
      "mcpServers": {
        "writer": {
          "command": "npx",
          "args": ["-y", "writer-sdk-mcp@latest"],
          "env": {
            "WRITER_API_KEY": "your-api-key-here"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### Interact with the MCP server in an AI client

After you've added your MCP server to your client configuration, you can interact with it by sending requests to the MCP server. Each client has a different way to interact with the MCP server.

For conversational AI assistants like Claude Desktop and Cursor, you can interact with the MCP server by sending messages to the assistant. For example, to upload a file to Writer, you can send a message like "Upload this image to Writer" and the assistant can use the MCP server to accomplish the task.

## Build custom MCP clients

You can also create your own MCP client using any MCP-compatible package like [Strands](https://strandsagents.com/latest/), [LangChain](https://python.langchain.com/), or other MCP libraries. The Writer MCP server follows the standard MCP protocol, so you can integrate it with any client that implements the protocol.

The following example shows how to create a custom MCP client using the Strands SDK.

### Set up the Strands SDK

First, install the Strands SDK, the Writer dependency, and the Strands Agent Tools package:

```bash  theme={null}
pip install 'strands-agents[writer]' strands-agents-tools
```

### Create a custom MCP client

Next, create a custom MCP client that uses the Writer MCP server to respond to user requests.

The example first creates an `MCPClient` using Strands Tools to connect to the Writer MCP server, then sets up the Writer model to be used by the agent for handling requests.

The `writer_mcp_client.list_tools_sync()` method retrieves the list of available tools from the Writer MCP server. The agent then uses these tools to respond to user requests related to content workflow automation.

```python content_workflow_client.py theme={null}
import os
from strands import Agent
from strands.models.writer import WriterModel
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

# Connect to the Writer MCP server using stdio transport
writer_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="npx",
        args=["-y", "writer-sdk-mcp@latest"],
        env={"WRITER_API_KEY": os.environ["WRITER_API_KEY"]}
    )
))

# Initialize the Writer model
writer_model = WriterModel(
    client_args={"api_key": os.environ["WRITER_API_KEY"]},
    model_id="palmyra-x5",
)

def content_workflow_client(user_request: str):
    """Custom MCP client that orchestrates complex content workflows using Writer MCP tools."""
    with writer_mcp_client:
        tools = writer_mcp_client.list_tools_sync()
        agent = Agent(
            model=writer_model,
            tools=tools,
            system_prompt="""You are a content workflow assistant that can:
            - Upload and analyze files
            - Generate content using Writer's models
            - Query Knowledge Graphs for research
            - Analyze images and extract insights
            - Chain multiple operations together seamlessly
            
            Use the available Writer MCP tools to fulfill user requests efficiently."""
        )
        return agent(user_request)

# Example usage
if __name__ == "__main__":
    # Research and content generation task
    response = content_workflow_client("Research and create content about sustainable fashion trends, including a blog post outline and social media content ideas")
    print("Research & Content:", response)
```

### Troubleshoot common issues

**MCP server shows fatal error about missing API key**: verify your API key is set correctly:

```bash  theme={null}
echo $WRITER_API_KEY
```

If the environment variable is not set, run:

```bash  theme={null}
export WRITER_API_KEY=your-api-key-here
```

**MCP client fails to initialize with "Connection closed" error**: this usually means the MCP server couldn't start due to a missing API key. When using Strands SDK, make sure to pass the environment variable to the MCP server:

```python  theme={null}
# Correct way to pass environment variables to MCP server
writer_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="npx",
        args=["-y", "writer-sdk-mcp@latest"],
        env={"WRITER_API_KEY": os.environ["WRITER_API_KEY"]}  # This is required!
    )
))
```

**Tools not appearing**: check that the MCP server is properly configured in your client and restart the client application.

**Permission errors**: ensure your API key has the necessary permissions for the operations you want to perform.

## Next steps

Now that you've set up the MCP server, you can use it to build complex workflows without writing custom integration code. Next, you can explore the following resources to help you get the most out of the MCP server:

* Explore [Writer's API reference](/api-reference) to understand all available endpoints
* Learn about [tool calling](/home/tool-calling) for more advanced integrations
* Check out [Knowledge Graphs](/home/knowledge-graph) for building intelligent content systems
* Review [vision analysis](/home/analyze-images) for image processing workflows
