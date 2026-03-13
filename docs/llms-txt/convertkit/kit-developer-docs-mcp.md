# Source: https://developers.kit.com/mcp/kit-developer-docs-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Kit Developer Docs MCP

> Connect AI coding agents directly to Kit's developer documentation using the Model Context Protocol

The Kit Developer Docs MCP (Model Context Protocol) server gives AI coding agents direct, real-time access to Kit's developer documentation. Rather than copying and pasting docs into your AI client, your agent can query Kit's full API reference, App Store guidelines, plugin architecture, and more on demand — always up to date. In supported clients, your agent can go further and make live Kit API calls on your behalf and spin up local servers to test OAuth flows end-to-end.

Using the MCP server is also significantly more effective than relying on your AI client's web search:

* **Always current** — MCP queries the live documentation directly, so your agent is never working from a stale search index or cached page
* **Token efficient** — web search retrieves full pages including navigation, markup, and boilerplate, all of which consume context window tokens. MCP returns only the structured content your agent actually needs, keeping responses faster and context usage lean

### MCP server URL

To get started, point your MCP-compatible AI assistant to this remote MCP URL — for example, by [adding a custom connector in Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). See full setup guides below.

```
https://developers.kit.com/mcp
```

## What your agent can do

Once connected, your AI agent can:

* Query any Kit API v4 endpoint reference, including request parameters, response shapes, and authentication requirements
* Understand Kit App Store requirements, submission criteria, and app configuration options
* Look up plugin component library usage, content block flows, and automation node configuration
* Reference OAuth flows, webhook event schemas, and pagination patterns
* **Make live API calls on your behalf** — in supported agentic clients (such as Claude Desktop, Claude Code, and Cline), your agent can use the API reference to construct and execute Kit API requests directly, without you writing a single line of code
* **Spin up a local OAuth server for testing** — ask your agent to start a local redirect server so you can complete the OAuth authorization flow end-to-end in your development environment before shipping. See [App Authentication](/kit-app-store/authentication) for how to configure OAuth in your app and make authenticated API calls

## Setup guides

### Claude Desktop

1. Open Claude Desktop and go to **Settings → Developer → Edit Config**, or open the config file directly:
   * macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   * Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the Kit MCP server:

```json  theme={null}
{
  "mcpServers": {
    "kit": {
      "url": "https://developers.kit.com/mcp"
    }
  }
}
```

3. Save and restart Claude Desktop. The Kit docs will be available as a tool in all your conversations.

### Claude Code

Run the following command in your terminal:

```bash  theme={null}
claude mcp add --transport http kit https://developers.kit.com/mcp
```

The Kit MCP server will be available in all Claude Code sessions in that project.

### Cursor

1. Open Cursor and go to **Settings → Tools & Integrations → MCP Tools → New MCP Server**.
2. Add a new server with the following configuration:

```json  theme={null}
{
  "mcpServers": {
    "kit": {
      "url": "https://developers.kit.com/mcp"
    }
  }
}
```

Alternatively, create or edit `.cursor/mcp.json` at the root of your project with the same configuration. See [Cursor's MCP guide](https://docs.cursor.com/context/model-context-protocol) for more details.

### Windsurf

1. Open Windsurf and go to **Windsurf Settings → Cascade → MCP Servers → Add Server**.
2. Select **HTTP/SSE** as the server type and enter `https://developers.kit.com/mcp` as the URL.

Or edit `~/.codeium/windsurf/mcp_config.json` directly:

```json  theme={null}
{
  "mcpServers": {
    "kit": {
      "serverUrl": "https://developers.kit.com/mcp"
    }
  }
}
```

See [Windsurf's MCP documentation](https://docs.windsurf.com/windsurf/mcp) for more details.

### Cline (VS Code)

1. Open VS Code with the Cline extension installed.
2. In the Cline sidebar, click the **MCP Servers** icon and then **Edit MCP Settings**.
3. Add the Kit server:

```json  theme={null}
{
  "mcpServers": {
    "kit": {
      "url": "https://developers.kit.com/mcp",
      "transport": "http"
    }
  }
}
```

See [Cline's MCP documentation](https://docs.cline.bot/mcp/connecting-to-a-remote-server) for more details.

## Other ways to use AI with Kit docs

The MCP server is the recommended way to give your AI agent access to Kit's developer documentation — it's real-time, always up to date, and requires no manual steps. For AI clients that don't yet support MCP, there are two additional options.

### llms.txt

[llms.txt](/llms.txt) is a single file containing all the content in the Kit developer documentation hub, following an emerging industry standard for making web content accessible to LLMs.

You can load it by pasting the URL directly into your AI client, or copying and uploading the file if your client doesn't support URL reading:

* [**Open in Claude**](https://claude.ai/new?q=Read+from%20https%3A%2F%2Fdevelopers.kit.com%2Fllms.txt)
* [**Open in ChatGPT**](https://chatgpt.com/?hints=search\&q=Read%20from%20https%3A%2F%2Fdevelopers.kit.com%2Fllms.txt%20so%20I%20can%20ask%20questions%20about%20it.)
* **Cursor:** Add `https://developers.kit.com/llms.txt` as a docs source via [Cursor's @Docs feature](https://docs.cursor.com/context/@-symbols/@-docs)
* **Other LLMs:** Request your client to read from `https://developers.kit.com/llms.txt`

<Note>llms.txt can become large enough to exceed some LLMs' context windows. If that happens, use the page-level method below, or switch to the MCP server which retrieves only what's needed on demand.</Note>

### Page-level

For focused questions on a single topic, every page in the docs has a **Copy page** button in the top-right corner. This copies the page's markdown content, which you can paste directly into any AI client — or use the **Open in ChatGPT / Open in Claude** shortcuts to start a conversation immediately.

<img width="400" alt="AI developer documentation menu" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/ai-dev-docs-menu.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=aee9ac983fe7be4d4c63cdf8646fbaa0" data-path="images/kit_app_store/ai-dev-docs-menu.png" />

## Tips for working with AI agents

* **Be specific in your prompts.** Ask your agent to "look up the Kit API v4 subscribers endpoint" rather than "how does Kit work" — targeted queries return better results.
* **Combine with page-level context.** For deep dives into a single topic, use the "Copy page" button on any docs page alongside your MCP-connected agent.
* **Verify important details.** AI agents can misinterpret or hallucinate details — always verify generated code against the [API reference](/api-reference/overview) before shipping.

<Note>
  If you run into issues or have feedback on the Kit MCP server, reach out to us via the [Kit Developer Community](https://kit.typeform.com/to/f8urvmPe).
</Note>


Built with [Mintlify](https://mintlify.com).