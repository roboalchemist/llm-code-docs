# Source: https://scrapfly.io/docs/mcp/integrations/custom-client

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/integrations/custom-client

Markdown Content:
1.   [MCP Documentation](https://scrapfly.io/docs/mcp)
2.   [Integrations](https://scrapfly.io/docs/mcp/integrations)
3.   Custom MCP Client

[Prerequisites](https://scrapfly.io/docs/mcp/integrations/custom-client#prerequisites)
--------------------------------------------------------------------------------------

Before getting started, make sure you have the following:

*   Programming experience in Python, JavaScript, or TypeScript
*   Understanding of async/await and HTTP protocols
*   Node.js 18+ or Python 3.8+ installed
*   Your Scrapfly API key (only if not using OAuth2)

[Overview](https://scrapfly.io/docs/mcp/integrations/custom-client#overview)
----------------------------------------------------------------------------

The Model Context Protocol (MCP) is a standard for connecting AI applications to external data sources and tools. This guide shows you how to build a custom MCP client that connects to the Scrapfly MCP server.

**What You'll Build:** An MCP client application that connects to `https://mcp.scrapfly.io/mcp` and can call Scrapfly's web scraping tools programmatically.

[Setup Instructions](https://scrapfly.io/docs/mcp/integrations/custom-client#setup)
-----------------------------------------------------------------------------------

1.   **Install MCP SDK**
Install the official Model Context Protocol SDK for your language:

**Python:**

`pip install mcp anthropic` 
**JavaScript/TypeScript:**

`npm install @modelcontextprotocol/sdk @anthropic-ai/sdk` Tip: MCP Protocol Specification
For advanced use cases, review the official MCP specification:

[https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction) 
2.   **Create Basic MCP Client (Python)**
Build a simple MCP client that connects to Scrapfly MCP server:

```
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from anthropic import Anthropic

async def main():
    # Define Scrapfly MCP server connection
    server_params = StdioServerParameters(
        command="npx",
        args=["mcp-remote", "https://mcp.scrapfly.io/mcp"],
        env=None
    )

    # Connect to Scrapfly MCP server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"Available Scrapfly tools: {len(tools.tools)}")

            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Example: Call web_get_page tool
            result = await session.call_tool(
                name="web_get_page",
                arguments={
                    "url": "https://news.ycombinator.com",
                    "pow": "..."  # Get this from scraping_instruction_enhanced first
                }
            )

            print("Scraped content:")
            print(result.content[0].text)

# Run the client
asyncio.run(main())
``` 
**Important:** The `pow` parameter is required for scraping. Call `scraping_instruction_enhanced` first to get it, or use OAuth2 which handles this automatically.

3.   **Create Basic MCP Client (JavaScript/TypeScript)**
Build an MCP client in JavaScript or TypeScript:

```
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

async function main() {
  // Create transport to Scrapfly MCP server
  const transport = new StdioClientTransport({
    command: "npx",
    args: ["mcp-remote", "https://mcp.scrapfly.io/mcp"]
  });

  // Create MCP client
  const client = new Client(
    {
      name: "scrapfly-client",
      version: "1.0.0"
    },
    {
      capabilities: {}
    }
  );

  // Connect to server
  await client.connect(transport);

  // List available tools
  const tools = await client.listTools();
  console.log(`Available Scrapfly tools: ${tools.tools.length}`);

  tools.tools.forEach(tool => {
    console.log(`  - ${tool.name}: ${tool.description}`);
  });

  // Call web_get_page tool
  const result = await client.callTool({
    name: "web_get_page",
    arguments: {
      url: "https://news.ycombinator.com",
      pow: "..."  // Get from scraping_instruction_enhanced
    }
  });

  console.log("Scraped content:");
  console.log(result.content[0].text);

  // Close connection
  await client.close();
}

main().catch(console.error);
``` 
4.   **Implement OAuth2 Authentication**
For production applications, use OAuth2 instead of API keys:

### Python OAuth2 Flow

```
import asyncio
import webbrowser
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def connect_with_oauth():
    """Connect to Scrapfly MCP with OAuth2"""

    server_params = StdioServerParameters(
        command="npx",
        args=["mcp-remote", "https://mcp.scrapfly.io/mcp"]
        # No API key in args - OAuth2 will handle authentication
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # On first connection, the server will return an OAuth2 URL
            # You can detect this and open the browser automatically:
            # webbrowser.open(oauth_url)

            # After OAuth2 authorization, tools become available
            tools = await session.list_tools()
            print(f"Authenticated! {len(tools.tools)} tools available")

            return session

asyncio.run(connect_with_oauth())
``` 

**OAuth2 Benefits:**

    *   No API keys in code or config files
    *   Automatic token refresh
    *   Better security and audit trail
    *   User-specific authentication

5.   **Build AI Agent with MCP Tools**
Integrate Scrapfly MCP tools with an AI agent using Anthropic SDK:

```
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from anthropic import Anthropic

async def build_agent():
    """Build an AI agent that can use Scrapfly tools"""

    # Connect to Scrapfly MCP
    server_params = StdioServerParameters(
        command="npx",
        args=["mcp-remote", "https://mcp.scrapfly.io/mcp"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Get available tools
            tools_response = await session.list_tools()
            tools = tools_response.tools

            # Initialize Anthropic client
            client = Anthropic()

            # Create AI agent with Scrapfly tools
            messages = [{
                "role": "user",
                "content": "Scrape the top 5 posts from Hacker News and summarize them"
            }]

            # Agent loop
            while True:
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=4096,
                    tools=[{
                        "name": tool.name,
                        "description": tool.description,
                        "input_schema": tool.inputSchema
                    } for tool in tools],
                    messages=messages
                )

                # Check if agent wants to use a tool
                if response.stop_reason == "tool_use":
                    tool_use = next(
                        block for block in response.content
                        if block.type == "tool_use"
                    )

                    # Call the tool via MCP
                    tool_result = await session.call_tool(
                        name=tool_use.name,
                        arguments=tool_use.input
                    )

                    # Add tool result to conversation
                    messages.append({
                        "role": "assistant",
                        "content": response.content
                    })
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": tool_result.content[0].text
                        }]
                    })
                else:
                    # Agent is done
                    print(response.content[0].text)
                    break

asyncio.run(build_agent())
``` 
**Pro Tip:** This agent will automatically call `scraping_instruction_enhanced` first to get required parameters!

6.   **Error Handling and Best Practices**
Implement robust error handling for production applications:

```
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def robust_mcp_client():
    """MCP client with error handling"""

    try:
        server_params = StdioServerParameters(
            command="npx",
            args=["mcp-remote", "https://mcp.scrapfly.io/mcp"]
        )

        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize with timeout
                await asyncio.wait_for(
                    session.initialize(),
                    timeout=30.0
                )

                # Call tool with error handling
                try:
                    result = await session.call_tool(
                        name="web_get_page",
                        arguments={
                            "url": "https://web-scraping.dev",
                            "pow": "..."
                        }
                    )

                    if result.isError:
                        print(f"Tool error: {result.content[0].text}")
                    else:
                        print(f"Success: {result.content[0].text}")

                except Exception as tool_error:
                    print(f"Tool call failed: {tool_error}")

    except asyncio.TimeoutError:
        print("Connection timeout - MCP server not responding")
    except Exception as e:
        print(f"MCP client error: {e}")

asyncio.run(robust_mcp_client())
``` 

[Example Prompts](https://scrapfly.io/docs/mcp/integrations/custom-client#examples)
-----------------------------------------------------------------------------------

###### Custom Research Assistant

Build a command-line tool that scrapes web pages and answers questions using Claude

###### Internal Automation Platform

Create an internal tool that integrates web scraping into your company's workflows

###### Data Collection Pipeline

Build a scheduled job that scrapes data and stores it in your database

###### Custom AI Agent

Develop a specialized AI agent with web scraping capabilities for your use case

[Troubleshooting](https://scrapfly.io/docs/mcp/integrations/custom-client#troubleshooting)
------------------------------------------------------------------------------------------

**Problem:** Cannot connect to Scrapfly MCP server

**Solution:**

*   Verify `npx` is available: `npx --version`
*   Check internet connectivity to `https://mcp.scrapfly.io/mcp`
*   Ensure Node.js 18+ is installed
*   Try running `npx mcp-remote https://mcp.scrapfly.io/mcp` manually

**Problem:** Tool calls return errors or fail

**Solution:**

*   Ensure you call `scraping_instruction_enhanced` first to get `pow` parameter
*   Check tool arguments match expected schema
*   Verify API key or OAuth2 authentication is working
*   Review error messages in tool call results

**Problem:** OAuth2 authorization does not complete

**Solution:**

*   Detect OAuth2 URL in initial connection response
*   Open URL in browser automatically or prompt user
*   Wait for OAuth2 completion before making tool calls
*   For headless environments, use API key authentication instead

**Problem:** MCP session times out or disconnects

**Solution:**

*   Implement connection retry logic
*   Keep session alive with periodic health checks
*   Reconnect automatically on disconnect
*   Increase timeout values for long-running operations

**Problem:** Tool schema or argument type errors

**Solution:**

*   Use `list_tools()` to get exact schema for each tool
*   Validate arguments against schema before calling
*   Check parameter types (string, boolean, integer, etc.)
*   Review MCP protocol specification for correct formats

**Problem:** Slow tool calls or high latency

**Solution:**

*   Implement caching for frequently scraped URLs
*   Use async/await properly to avoid blocking
*   Batch similar requests when possible
*   Monitor network latency and optimize connection settings

[Next Steps](https://scrapfly.io/docs/mcp/integrations/custom-client#next-steps)
--------------------------------------------------------------------------------

*   [Explore available MCP tools](https://scrapfly.io/docs/mcp/tools) and their capabilities
*   [See real-world examples](https://scrapfly.io/docs/mcp/examples) of what you can build
*   [Learn about authentication methods](https://scrapfly.io/docs/mcp/authentication) in detail
*   [Read the FAQ](https://scrapfly.io/docs/mcp/faq) for common questions
