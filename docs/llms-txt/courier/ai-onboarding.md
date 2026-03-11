# Source: https://www.courier.com/docs/tools/ai-onboarding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build with AI

> Use Courier with AI coding agents via the CLI, MCP server, agent skills, and machine-readable docs.

Courier provides multiple integration points for AI coding agents. Choose what fits your workflow, or combine them.

## Courier CLI

The CLI gives agents (and you) direct shell access to all 81 Courier API endpoints. Install once, set your API key, and any agent that can run shell commands can send messages, inspect delivery logs, and manage users. See the [CLI reference](/tools/cli) for the full command list.

```bash  theme={null}
npm install -g @trycourier/cli
export COURIER_API_KEY="your-api-key"
```

```bash  theme={null}
courier send message \
  --message.to.user_id "user-123" \
  --message.template "order-confirmation" \
  --message.data '{"orderId": "ORD-456"}'
```

Every command supports `--format json` for machine-readable output.

## MCP Server

The [MCP server](/tools/mcp) provides structured tool access for AI agents. Agents discover available tools automatically and call them with typed parameters; no shell commands needed.

<Tabs>
  <Tab title="Cursor">
    [![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=courier\&config=eyJ1cmwiOiJodHRwczovL21jcC5jb3VyaWVyLmNvbSIsImhlYWRlcnMiOnsiYXBpX2tleSI6IlhYWFgifX0%3D)

    Or add manually to your `mcp.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "courier": {
          "url": "https://mcp.courier.com",
          "headers": {
            "api_key": "XXXX"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Claude Code">
    ```bash  theme={null}
    claude mcp add --transport http courier https://mcp.courier.com --header api_key:XXXX
    ```
  </Tab>
</Tabs>

See [MCP Server](/tools/mcp) for setup on Claude Desktop, Windsurf, VSCode, and OpenAI API, plus the complete tool list.

## Courier Skills

[Agent skill packs](/tools/courier-skills) that teach your AI coding assistant Courier notification best practices. Covers channel selection, compliance, reliability patterns, and more.

<Tabs>
  <Tab title="Cursor (global)">
    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git ~/.cursor/skills/courier-skills
    ```
  </Tab>

  <Tab title="Cursor (project)">
    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git .cursor/skills/courier-skills
    ```
  </Tab>

  <Tab title="Claude Code">
    ```bash  theme={null}
    git clone https://github.com/trycourier/courier-skills.git ~/.claude/skills/courier-skills
    ```
  </Tab>
</Tabs>

Once installed, your agent automatically gets routing guidance, compliance rules, and code patterns for all 7 channels and 28 notification types. See [Courier Skills](/tools/courier-skills) for coverage details and how the routing works.

## Docs for Agents

Courier's documentation is available as machine-readable indexes that AI agents can fetch to discover all available pages, API endpoints, and guides:

| URL                                                           | Description                                 |
| ------------------------------------------------------------- | ------------------------------------------- |
| [`llms.txt`](https://www.courier.com/docs/llms.txt)           | Structured index of all documentation pages |
| [`llms-full.txt`](https://www.courier.com/docs/llms-full.txt) | Full documentation content in a single file |

These follow the [llms.txt standard](https://llmstxt.org/) and are generated automatically from these docs. Agents that support llms.txt can discover Courier's CLI, MCP server, SDKs, and API reference without any configuration.

## Quick Starts

Common tasks you can hand to an agent with the CLI or MCP server installed:

**Send a test message:**

```bash  theme={null}
courier send message \
  --message.to.email "test@example.com" \
  --message.content.title "Hello" \
  --message.content.body "Test from CLI"
```

**Debug a failed delivery:**

```bash  theme={null}
courier messages list --format json --transform "results.#(status=UNDELIVERABLE)"
courier messages history --message-id "MSG_ID" --format json
```

**Check a user's profile:**

```bash  theme={null}
courier profiles retrieve --user-id "user-123" --format json
```

## What's Next

<CardGroup cols={2}>
  <Card title="CLI Reference" icon="terminal" href="/tools/cli">
    Full command list, output formats, and global flags.
  </Card>

  <Card title="MCP Server" icon="microchip-ai" href="/tools/mcp">
    Setup for all supported editors and the complete tool list.
  </Card>

  <Card title="Agent Skills" icon="brain" href="/tools/courier-skills">
    Coverage details and how the skill routing works.
  </Card>

  <Card title="API Reference" icon="code" href="/reference/get-started">
    REST API documentation for all 81 endpoints.
  </Card>
</CardGroup>
