# Source: https://docs.gitguardian.com/ggmcp-docs/installation.md

# Installation

> Install the GitGuardian MCP server in Cursor, Claude Desktop, Windsurf, or Zed.

# Installation

:::warning[Beta]
The GitGuardian MCP Server is currently in **beta**. Features and behavior may change as we iterate based on user feedback.
:::

## Prerequisites

- A [GitGuardian](https://www.gitguardian.com/) account
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

## Install in Cursor

Click the one-click install button from the [GitHub README](https://github.com/GitGuardian/gg-mcp#installation-with-cursor), or add manually to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "GitGuardianDeveloper": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/GitGuardian/gg-mcp.git",
        "developer-mcp-server"
      ]
    }
  }
}
```

## Other IDEs

For **Claude Desktop**, **Windsurf**, and **Zed** installation instructions, see the [GitHub README](https://github.com/GitGuardian/gg-mcp#installation).

## Instance configuration

The server defaults to GitGuardian SaaS (US). For other instances, set the `GITGUARDIAN_URL` environment variable:

| Instance | URL |
|----------|-----|
| SaaS US *(default)* | `https://dashboard.gitguardian.com` |
| SaaS EU | `https://dashboard.eu1.gitguardian.com` |
| Self-hosted | Your instance URL (e.g., `https://dashboard.gitguardian.mycorp.local`) |

See [Configuration](https://github.com/GitGuardian/gg-mcp#configuration-for-different-gitguardian-instances) for all environment variables.
