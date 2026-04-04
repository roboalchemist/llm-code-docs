# Source: https://gofastmcp.com/getting-started/welcome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://gofastmcp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome to FastMCP 3.0!

> The fast, Pythonic way to build MCP servers and clients.

<img src="https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=ed5a792b94ca3d10ae2545461c4cc84d" alt="'F' logo on a watercolor background" noZoom className="rounded-2xl block dark:hidden" data-og-width="1368" width="1368" data-og-height="566" height="566" data-path="assets/brand/f-watercolor-waves-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=280&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=671e47d6dc6c7432d86373ecd4be213c 280w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=560&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=f9adab52c71d209409de050e3d8cf1d6 560w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=840&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=23e7505146369d330a49d3e8e1399ddf 840w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=1100&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=22bfe92301388bc0fbb975c70f07a313 1100w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=1650&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=2aba2f0af93e283d5bb78a1075879deb 1650w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-2.png?w=2500&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=b113f6b9b89f0bc511f29c16cdc043ab 2500w" />

<img src="https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=722c3437ce47b4eff4e19e0beb7be363" alt="'F' logo on a watercolor background" noZoom className="rounded-2xl hidden dark:block" data-og-width="1616" width="1616" data-og-height="656" height="656" data-path="assets/brand/f-watercolor-waves-dark-2.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=280&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=5bc6ef4e62c6178640411ed93891548c 280w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=560&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=ecc5741c8f653169271c4a5b75138cc8 560w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=840&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=2a9ec0400f1c6adb06746aa9d541ab30 840w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=1100&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=4935c8925c35dfab1f9c3ce43b11666a 1100w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=1650&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=78649fe63464814c70f194142a995850 1650w, https://mintcdn.com/fastmcp/vP28Y_HI4lA7ZSYM/assets/brand/f-watercolor-waves-dark-2.jpeg?w=2500&fit=max&auto=format&n=vP28Y_HI4lA7ZSYM&q=85&s=2ee5444cbcbca78b9b34ef5527ef8351 2500w" />

**FastMCP is the standard framework for building MCP applications.** The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code:

```python {1} theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

<Tip>
  **This documentation is for FastMCP 3.0**, which is currently in beta. For the 2.x release, see the [FastMCP 2.0 documentation](/v2/getting-started/welcome).
</Tip>

FastMCP is made with 💙 by [Prefect](https://www.prefect.io/).

## Move Fast and Make Things

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) lets you give agents access to your tools and data. But building an effective MCP server is harder than it looks.

Give your agent too much—hundreds of tools, verbose responses—and it gets overwhelmed. Give it too little and it can't do its job. The protocol itself is complex, with layers of serialization, validation, and error handling that have nothing to do with your business logic. And the spec keeps evolving; what worked last month might already need updating.

The real challenge isn't implementing the protocol. It's delivering **the right information at the right time**.

That's the problem FastMCP solves—and why it's become the standard. FastMCP 1.0 was incorporated into the official MCP SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.

The framework is built on three abstractions that map to the decisions you actually need to make:

* **[Components](/servers/tools)** are what you expose: tools, resources, and prompts. Wrap a Python function, and FastMCP handles the schema, validation, and docs.
* **[Providers](/servers/providers/overview)** are where components come from: decorated functions, files on disk, OpenAPI specs, remote servers—your logic can live anywhere.
* **[Transforms](/servers/transforms/transforms)** shape what clients see: namespacing, filtering, authorization, versioning. The same server can present differently to different users.

These compose cleanly, so complex patterns don't require complex code. And because FastMCP is opinionated about the details, like serialization, error handling, and protocol compliance, **best practices are the path of least resistance**. You focus on your logic; the MCP part just works.

Ready to build? Start with the [installation guide](/getting-started/installation) or jump straight to the [quickstart](/getting-started/quickstart). When you're ready to deploy, [Prefect Horizon](https://www.prefect.io/horizon) offers free hosting for FastMCP users.

<Tip>
  **This documentation reflects FastMCP's `main` branch**, meaning it always reflects the latest development version. Features are generally marked with version badges (e.g. `New in version: 3.0.0`) to indicate when they were introduced. Note that this may include features that are not yet released.
</Tip>

## LLM-Friendly Docs

The FastMCP documentation is available in multiple LLM-friendly formats:

### MCP Server

The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`.

In fact, you can use FastMCP to search the FastMCP docs:

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://gofastmcp.com/mcp") as client:
        result = await client.call_tool(
            name="SearchFastMcp", 
            arguments={"query": "deploy a FastMCP server"}
        )
    print(result)

asyncio.run(main())
```

### Text Formats

The docs are also available in [llms.txt format](https://llmstxt.org/):

* [llms.txt](https://gofastmcp.com/llms.txt) - A sitemap listing all documentation pages
* [llms-full.txt](https://gofastmcp.com/llms-full.txt) - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. For example, this page becomes `https://gofastmcp.com/getting-started/welcome.md`.

You can also copy any page as markdown by pressing "Cmd+C" (or "Ctrl+C" on Windows) on your keyboard.
