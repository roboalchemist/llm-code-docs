# Source: https://braintrust.dev/docs/integrations/developer-tools/mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Braintrust MCP

> Access Braintrust from AI coding tools

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) enables AI coding tools to access your Braintrust data directly. Query experiments, search documentation, and analyze production logs from Claude Code, Cursor, VS Code, Windsurf, and Claude Desktop.

## Set up the MCP server

Braintrust provides a hosted MCP server with OAuth 2.0 authentication. Add it to your AI tool's configuration:

### Claude Code

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Install Claude Code (if not already installed)
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-project

# Add Braintrust MCP server
claude mcp add --transport http braintrust https://api.braintrust.dev/mcp

# Start Claude Code
claude

# Authenticate by typing /mcp
/mcp
```

### Codex (OpenAI)

Add the following lines to `~/.codex/config.toml`

```toml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
[mcp_servers.braintrust]
url = "https://api.braintrust.dev/mcp"
bearer_token_env_var = "BRAINTRUST_API_KEY"
```

Then launch codex with the `BRAINTRUST_API_KEY` envar set to your api key. Run the `/mcp` command to verify Braintrust is installed.

### Cursor

Click to automatically add Braintrust:

[Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=braintrust\&config=eyJ1cmwiOiJodHRwczovL2FwaS5icmFpbnRydXN0LmRldi9tY3AifQ%3D%3D)

Or manually add to `.cursor/mcp.json`:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

### VS Code

1. Open Command Palette (Ctrl+Shift+P or Cmd+Shift+P)
2. Run **MCP: Add Server**
3. Select **HTTP** and enter:
   * URL: `https://api.braintrust.dev/mcp`
   * Name: `Braintrust`
4. Click **Add**

### Windsurf

Add to `mcp_config.json`:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

### Claude Desktop

1. Open **Settings** (gear icon)
2. Navigate to **Connectors** > **Add custom connector**
3. Enter:
   * Name: `Braintrust`
   * URL: `https://api.braintrust.dev/mcp`

### OpenCode

Add the Braintrust MCP to your [OpenCode Config](https://opencode.ai/docs/config/):

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "braintrust": {
      "type": "remote",
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

Then run the following command to authenticate in a web browser:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
opencode mcp auth braintrust
```

## Authenticate

The MCP server uses OAuth 2.0 with PKCE for secure authentication. On first connection, the OAuth flow opens automatically:

1. Your AI tool triggers the OAuth flow
2. A browser window opens asking you to log into Braintrust
3. After authentication, review the consent screen showing the redirect URL
4. Click **Yes, I trust this URL - Proceed**
5. Return to your AI tool

Your tool now has access to your Braintrust data.

### Token lifecycle

The OAuth flow provides two types of tokens:

* **Access tokens**: Short-lived tokens (typically 1 hour) used to authenticate API requests
* **Refresh tokens**: Long-lived tokens used to obtain new access tokens when they expire

Your AI tool manages these tokens automatically. When an access token expires, the tool uses the refresh token to get a new one without requiring you to re-authenticate. Tokens are cached locally by your AI tool for convenience.

## Available tools

The MCP server provides these tools to your AI assistant:

### Search documentation

**`search_docs`** - Find guides, API references, and code examples:

* "How do I create a custom scorer?"
* "Show me examples of BTQL queries"
* "What's the difference between experiments and project logs?"

### Resolve objects

**`resolve_object`** - Convert names to IDs and vice versa:

* "Find the ID for my 'sentiment-analysis' experiment"
* "What's the name of experiment abc123?"

### List recent objects

**`list_recent_objects`** - Browse projects, experiments, and datasets:

* "Show me my recent experiments in the 'chatbot' project"
* "List datasets in the recommendation engine project"

### Infer schemas

**`infer_schema`** - Understand data structure:

* "What fields are available in my experiment data?"
* "Show me the schema for production logs"

### Query with BTQL

**`btql_query`** - Execute BTQL queries:

* "Compare accuracy scores between my GPT-4 and Claude experiments"
* "Show experiments where factuality score was below 0.7"
* "What were the costs for my recent chatbot experiments?"

### Summarize experiments

**`summarize_experiment`** - Get performance summaries:

* "Summarize the results of my latest A/B test"
* "Compare my experiment against the baseline"

### Generate permalinks

**`generate_permalink`** - Create shareable links:

* "Create a link to share my experiment results"
* "Generate a permalink to the customer-reviews dataset"

## Example workflows

### Analyze experiment results

Ask your AI assistant:

```
What were the accuracy scores for my recent sentiment analysis experiments?
Compare costs between GPT-4 and Claude experiments.
```

The MCP server queries your data and returns results directly in the conversation.

### Debug production issues

```
Show me logs from the last hour where errors occurred.
What's the average latency for the summarizer prompt today?
```

### Share findings with teammates

```
Generate a link to my latest A/B test results.
Create a permalink to the customer-feedback dataset.
```

## Self-hosted instances

For self-hosted Braintrust, use your API URL:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://your-api-url.com/mcp"
    }
  }
}
```

<Note>
  Set the `MCP_SERVER_URL` environment variable to your API URL for OAuth discovery. Terraform deployments handle this automatically.
</Note>

## Troubleshooting

**OAuth fails or gets stuck**: Clear browser cache and try incognito mode. For SSO, ensure you're logged into your SSO provider.

**Invalid client errors**: Verify the URL is exactly `https://api.braintrust.dev/mcp` (no trailing slash).

**Connection timeouts**: Check internet connection. Corporate networks may need to allowlist `api.braintrust.dev` and `*.braintrust.dev`.

**MCP server not appearing**: Restart your AI tool and verify JSON configuration syntax.

**Access denied**: Verify you can access the project in the Braintrust web interface.

**BTQL queries failing**: Test queries in the web interface first. Use `infer_schema` to verify column names.

## Next steps

* [Use the Data API](/api-reference) for programmatic access
* [Query with SQL](/reference/sql) for complex data analysis
* [View logs](/observe/view-logs) in the web interface
* [Run evaluations](/evaluate/run-evaluations) and analyze with MCP
