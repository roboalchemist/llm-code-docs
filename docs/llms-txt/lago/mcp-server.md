# Source: https://getlago.com/docs/guide/ai-agents/mcp-server.md

# Lago MCP Server

> Connect Lago live data, models, and billing logic to any AI system, bringing billing context and interactions everywhere.

The [Lago MCP Server](https://github.com/getlago/lago-agent-toolkit) (Model Context Protocol) is written in Rust and provides AI assistants (like Claude) with direct access to Lago's billing data.
The server acts as a bridge between AI models and the Lago API, enabling natural language queries about invoices, customers, and billing information.

<Frame caption="Lago MCP Server">
  <img src="https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=fca42564bb0f785c1fa7f759d3d9ecd2" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="changelog/images/20251215mcp-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=280&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=e6ebab646e7c8855bfa4b95ea2b62660 280w, https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=560&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=a7109174b044fc70f5b236f1d55ab96a 560w, https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=840&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=2e206ff9034596fbd3eb1a95c735241e 840w, https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=1100&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=d743f7d7c1b42a159860e2db89026195 1100w, https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=1650&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=dbb9d040456d29d78842aa8ca4a33460 1650w, https://mintcdn.com/lago-docs/2-k0Uplnuzl9sCzZ/changelog/images/20251215mcp-server.png?w=2500&fit=max&auto=format&n=2-k0Uplnuzl9sCzZ&q=85&s=681a66551c901773f8ad535d34285951 2500w" />
</Frame>

## Quick start using Claude Desktop

### Configure Claude Desktop

The easiest way to get started is using the pre-built Docker image with Claude Desktop:

```json  theme={"dark"}
{
  "mcpServers": {
    "lago": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--name", "lago-mcp-server",
        "-e", "LAGO_API_KEY=your_lago_api_key",
        "-e", "LAGO_API_URL=https://api.getlago.com/api/v1",
        "getlago/lago-mcp-server:latest"
      ]
    }
  }
}
```

### Set your credentials

Simply replace your `LAGO_API_KEY` with your actual Lago API key. You can find this in your Lago dashboard under API settings.
Also, make sure that you are using the right `LAGO_API_URL` for your Lago instance.

### Start chatting

Once configured, you can ask Claude natural language questions about your billing data:

* "Show me all pending invoices from last month"
* "Find all failed payment invoices"
* "Give me the total amount of overdue invoices for the month of March 2025"

The list of available commands and their descriptions can be found in the [Lago MCP Server GitHub repository](https://github.com/getlago/lago-agent-toolkit?tab=readme-ov-file#available-tools).
You can contribute to the project by adding more commands or improving existing ones.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://getlago.com/docs/llms.txt