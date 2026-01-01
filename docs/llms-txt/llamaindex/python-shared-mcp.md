# LlamaIndex Documentation

Source: https://developers.llamaindex.ai/python/shared/mcp/

---

# MCP Documentation Search

As part of the LlamaIndex documentation, we serve a hosted MCP server that
allows any agent to search the LlamaIndex documentation.

The hosted MCP server is available at the following URL:

    
    
    https://developers.llamaindex.ai/mcp

The server ships with the following tools:

  1. `search_docs` — a basic lexical search using BM25
  2. `grep_docs` — exact search using regex
  3. `read_doc` — provides an interface to read the entire contents of any given page path

![MCP Server](/python/_astro/mcp.Bn5KN2fe_ZcctxN.webp)

## Configure your Agent

Section titled “Configure your Agent”

### Cursor

Section titled “Cursor”

You can [click to install to cursor directly](cursor://anysphere.cursor-
deeplink/mcp/install?name=llama-index-
docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ%3D%3D)
or add the following to your `mcp.json` configuration:

    
    
    {
    
      "mcpServers": {
    
        "llama_index_docs": {
    
          "url": "https://developers.llamaindex.ai/mcp"
    
        }
    
      }
    
    }

### Claude Code

Section titled “Claude Code”

Add the documentation search tools to your Claude Code agent with a single
command:

Terminal window

    
    
    claude mcp add llama-index-docs --transport http https://developers.llamaindex.ai/mcp

### OpenAI Codex

Section titled “OpenAI Codex”

Add the documentation search tools to your OpenAI Codex agent by adding the
following section to your `config.toml`:

Terminal window

    
    
    [mcp_servers.llama_index_docs]
    
    url = "https://developers.llamaindex.ai/mcp"

### LlamaIndex Agents

Section titled “LlamaIndex Agents”

Install llama-index and the MCP tools package:

Terminal window

    
    
    pip install llama-index llama-index-tools-mcp

And then directly use the MCP tools in your agent:

    
    
    from llama_index.core.agent import FunctionAgent, ToolCall, ToolCallResult
    
    from llama_index.llms.openai import OpenAI
    
    from llama_index.tools.mcp import McpToolSpec, BasicMCPClient
    
    
    
    
    
    
    
    async def main():
    
        client = BasicMCPClient("https://developers.llamaindex.ai/mcp")
    
        tool_spec = McpToolSpec(client=client)
    
        tools = await tool_spec.to_tool_list_async()
    
    
    
    
        agent = FunctionAgent(
    
            llm=OpenAI(model="gpt-4.1", api_key="sk-..."),
    
            tools=tools,
    
            system_prompt="You are a helpful assistant that has access to tools to search the LlamaIndex documentation."
    
        )
    
    
    
    
        while True:
    
            query = input("Query: ")
    
            handler = agent.run(query)
    
            async for ev in handler.stream_events():
    
                if isinstance(ev, ToolCall):
    
                    print(f"Calling tool {ev.tool_name} with input {ev.tool_kwargs}")
    
                if isinstance(ev, ToolCallResult):
    
                    print(f"Tool {ev.tool_name} returned {ev.tool_output}")
    
    
    
    
            resp = await handler
    
            print("")
    
            print(resp)
    
            print("=================")
    
    
    
    
    if __name__ == "__main__":
    
        import asyncio
    
        asyncio.run(main())

[ Previous  
Cloud API Reference 🔗 ](/python/../cloud-api-reference/llama-platform/) [ Next  
Getting Started ](/python/llamaagents/llamactl/getting-started/)

