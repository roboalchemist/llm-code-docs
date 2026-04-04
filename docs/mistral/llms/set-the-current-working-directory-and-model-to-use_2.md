# Set the current working directory and model to use
cwd = Path(__file__).parent
MODEL = "mistral-medium-latest"

async def main():
    # Initialize the Mistral client with your API key
    api_key = os.environ["MISTRAL_API_KEY"]
    client = Mistral(api_key)
```

#### Step 2: Define Server URL and Create MCP Client

Next, we define the URL for the remote MCP server and create an MCP client to connect to it.

```python
    # Define the URL for the remote MCP server
    server_url = "https://mcp.semgrep.ai/sse"
    mcp_client = MCPClientSSE(sse_params=SSEServerParams(url=server_url, timeout=100))
```

#### Step 3: Create a Run Context and Register MCP Client

We create a Run Context for the agent and register the MCP client with it.

```python
    # Create a run context for the agent
    async with RunContext(
        model=MODEL,
    ) as run_ctx:
        # Register the MCP client with the run context
        await run_ctx.register_mcp_client(mcp_client=mcp_client)
```

#### Step 4: Run the Agent and Print Results

Finally, we run the agent with a query and print the results.

```python
        # Run the agent with a query
        run_result = await client.beta.conversations.run_async(
            run_ctx=run_ctx,
            inputs="Can you write a hello_world.py and check for security vulnerabilities",
        )

        # Print the results
        print("All run entries:")
        for entry in run_result.output_entries:
            print(f"{entry}")
            print()
        print(f"Final Response: {run_result.output_as_text}")

if __name__ == "__main__":
    asyncio.run(main())
```

  </TabItem>

  <TabItem value="remote-mcp-auth" label="Remote MCP Server with Auth">

### How to Use a Remote MCP Server with Authentication

Here is how to use a remote MCP server with authentication.

#### Step 1: Initialize the Mistral Client

First, we import everything needed. Most of the required modules are available with our `mistralai` package. All the MCP Clients will be run asynchronously, so we will create an async main function where the main code will reside.

```python
#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer


from mistralai import Mistral
from mistralai.extra.run.context import RunContext
from mistralai.extra.mcp.sse import MCPClientSSE, SSEServerParams
from mistralai.extra.mcp.auth import build_oauth_params