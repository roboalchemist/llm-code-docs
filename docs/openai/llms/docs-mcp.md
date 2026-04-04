# Source: https://developers.openai.com/resources/guide/docs-mcp.md

# Source: https://developers.openai.com/resources/docs/docs-mcp.md

# Docs MCP

OpenAI hosts a public Model Context Protocol (MCP) server for developer documentation on developers.openai.com and platform.openai.com.

**Server URL (streamable HTTP):** `https://developers.openai.com/mcp`

## What it provides

- Read-only access to OpenAI developer documentation (search + page content).
- A way to pull documentation into your agent's context while you work.



This MCP server is documentation-only. It does not call the OpenAI API on your
  behalf.



## Quickstart



<div slot="codex">
    You can connect Codex to [MCP servers](https://developers.openai.com/codex/mcp) in the [CLI](https://developers.openai.com/codex/cli) or [IDE extension](https://developers.openai.com/codex/ide). The configuration is shared between both so you only have to set it up once.

    Add the server using the Codex CLI:

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
```

    Verify it's configured:

```bash
codex mcp list
```

    Alternatively, you can add it in `~/.codex/config.toml` directly:

```toml
[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

    To have Codex reliably use the MCP server, add this snippet to your `AGENTS.md`:

```
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.
```

  </div>

  <div slot="vs-code">
    VS Code supports MCP servers when using GitHub Copilot in Agent mode.

    Click the following link to add the Docs MCP to VS Code:

    Alternatively, you can manually add a `.vscode/mcp.json` in your project root:

```json
{
  "servers": {
    "openaiDeveloperDocs": {
      "type": "http",
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

    To have VS Code reliably use the MCP server, add this snippet to your `AGENTS.md`:

```
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.
```

    Open Copilot Chat, switch to **Agent** mode, enable the server in the tools picker, and ask an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

  </div>

  <div slot="cursor">
    Cursor has native MCP support and reads configuration from `mcp.json`.

    Install with Cursor:

    <a
      href="https://cursor.com/en-US/install-mcp?name=openaiDeveloperDocs&config=eyJ1cmwiOiAiaHR0cHM6Ly9kZXZlbG9wZXJzLm9wZW5haS5jb20vbWNwIn0%3D"
      class="inline-flex not-prose mb-4"
    >
      <img src="https://cursor.com/deeplink/mcp-install-dark.svg"
        alt="Install MCP Server in Cursor (light mode)"
        class="block h-auto w-auto dark:hidden"
      />
      <img src="https://cursor.com/deeplink/mcp-install-light.svg"
        alt="Install MCP Server in Cursor (dark mode)"
        class="hidden dark:block h-auto w-auto"
      />
    </a>

    Alternatively, create a `~/.cursor/mcp.json` (macOS/Linux) and add:

```json
{
  "mcpServers": {
    "openaiDeveloperDocs": {
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

    To have Cursor reliably use the MCP server, add this snippet to your `AGENTS.md`:

```
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.
```

    Restart Cursor and ask Cursor's agent an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

  </div>



## Tips

- If you don't have the snippet in the AGENTS.md file, you need to explicitly tell your agent to consult the Docs MCP server for the answer.
- If you have more than one MCP server, keep server names short and descriptive to aid the agent in selecting the server.