# Source: https://braintrust.dev/docs/reference/mcp.md

# Model Context Protocol (MCP)

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is a standardized framework that enables AI models to interact with external data sources and tools. It allows for real-time access to your Braintrust experiments, datasets, logs, and documentation directly from your coding environment.

## Getting started

Braintrust provides an MCP server that gives your AI tools direct access to your data and documentation. The server uses the latest HTTP MCP format and
OAuth 2.0 for secure authentication. If you are using SSO, the MCP server authenticates via your SSO provider. If you are self-hosting Braintrust, the MCP server
is built into your hosted instance, so the data it processes stays within your environment.

### Find your MCP URL

If you are using hosted Braintrust, use the following URL for the MCP server:

```
https://api.braintrust.dev/mcp
```

If you are self-hosting Braintrust, your MCP URL will be:

```
<YOUR_API_URL>/mcp
```

<Note>
  Make sure your API has the `MCP_SERVER_URL` environment variable set to `<YOUR_API_URL>` so
  the OAuth discovery endpoints work correctly. If you are using Terraform, this
  is set automatically.
</Note>

### Recommended: Hosted MCP server

For the most streamlined setup, we recommend using the hosted MCP server. Add the following to your MCP configuration file (for example, `.cursor/mcp.json`):

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

For self-hosted instances, replace `https://api.braintrust.dev/mcp` with `<YOUR_API_URL>/mcp`.

### Tool-specific setup

MCP is supported in many tools, including:

* [Claude Code](https://www.anthropic.com/claude-code)
* [Cursor](https://www.cursor.com/)
* VS Code with [Copilot](https://code.visualstudio.com/docs/editor/github-copilot)
* [Windsurf](https://docs.codeium.com/windsurf)
* [Claude Desktop](https://claude.ai/download)

#### Claude Code

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Add Braintrust MCP server
claude mcp add --transport http braintrust https://api.braintrust.dev/mcp

# Start Claude Code
claude

# Authenticate the MCP tools by typing /mcp
/mcp
```

#### Cursor

Use the following link to automatically add Braintrust to your Cursor configuration:

[Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=braintrust\&config=eyJ1cmwiOiJodHRwczovL2FwaS5icmFpbnRydXN0LmRldi9tY3AifQ%3D%3D)

You can also configure your `mcp.json` manually:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

Once added, Cursor will prompt you to authenticate via the OAuth flow.

#### VS Code

To add Braintrust to VS Code:

1. Run **MCP: Add Server** from the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS)
2. Select HTTP and enter the following details:
   * URL: `https://api.braintrust.dev/mcp`
   * Name: `Braintrust`
   * Select Global or Workspace depending on your needs
3. Select **Add**

#### Windsurf

Add the following to your Windsurf `mcp_config.json`:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "mcpServers": {
    "braintrust": {
      "url": "https://api.braintrust.dev/mcp"
    }
  }
}
```

#### Claude Desktop

1. Open Claude Desktop settings by navigating to the **Gear icon → Settings**
2. Navigate to **Connectors** and select **Add custom connector**
3. Enter the following details:
   * **Name**: `Braintrust`
   * **URL**: `https://api.braintrust.dev/mcp`

## Authentication

The hosted MCP server uses OAuth 2.0 for secure authentication. When you first connect:

1. Your AI tool automatically triggers the OAuth flow, which uses PKCE to support dynamic client registration
2. A browser window opens asking you to log into Braintrust
3. After successful authentication, you'll see a consent screen showing the redirect URL
4. Select **Yes, I trust this URL - Proceed** to complete the setup
5. Your AI tool now has access to your Braintrust data

## Available tools

Once connected, your AI tools have access to the following Braintrust features.

### Documentation search

**`search_docs`** - Search Braintrust documentation using semantic search

* Find guides, API references, and code examples
* Get contextual help for experiments, datasets, prompts, and evaluations
* Example: "How do I create a custom scorer?"

### Object resolution

**`resolve_object`** - Convert between names and IDs for Braintrust objects

* Look up experiments, datasets, projects by name or ID
* Get permalinks to share specific objects
* Example: "Find the ID for my 'sentiment-analysis' experiment"

### Recent objects

**`list_recent_objects`** - Browse your recent projects, experiments, and datasets

* List recent experiments in a project
* Find recently created datasets
* Discover available prompts and functions
* Example: "Show me my recent experiments in the 'chatbot' project"

### Schema analysis

**`infer_schema`** - Understand the structure of your data

* Analyze experiment outputs and metadata fields
* See sample values and data types
* Plan better queries and evaluations
* Example: "What fields are available in my experiment data?"

### BTQL queries

**`btql_query`** - Execute powerful queries using [Braintrust Query Language](/reference/btql)

* Analyze experiment performance across multiple runs
* Filter and aggregate evaluation results
* Compare models, prompts, and configurations
* Query production logs and traces
* Example: "Compare accuracy scores between my GPT-4 and Claude experiments"

### Experiment summaries

**`summarize_experiment`** - Get high-level performance summaries

* View aggregated scores, costs, and latency metrics
* Compare against baseline experiments
* Understand overall experiment performance
* Example: "Summarize the results of my latest A/B test"

### Permalink generation

**`generate_permalink`** - Create shareable links to Braintrust objects

* Generate URLs for experiments, datasets, and projects
* Share results with teammates
* Create bookmarks for important objects
* Example: "Create a link to share my experiment results"

## Example queries

Once connected, you can query experiments, analyze results, and get documentation help directly from your IDE using natural language.

### Experiment analysis

* "What were the accuracy scores for my recent sentiment analysis experiments?"
* "Compare the cost and latency between GPT-4 and Claude in my chatbot experiments"
* "Show me experiments where the factuality score was below 0.7"

### Data exploration

* "List my recent datasets in the recommendation engine project"
* "What's the schema of my customer feedback experiment?"
* "Find experiments that used the 'production-prompts' dataset"

### Documentation and learning

* "How do I implement custom scoring functions?"
* "Show me examples of BTQL queries for error analysis"
* "What's the difference between experiments and project logs?"

### Sharing and collaboration

* "Generate a link to my latest A/B test results"
* "Create a permalink to the customer-reviews dataset"

## Troubleshooting

* **OAuth flow fails or gets stuck**: Clear your browser cache and try incognito mode/private browsing. For SSO users, ensure you're logged into your SSO provider.
* **Invalid client or unauthorized errors**: Verify your MCP URL is exactly `https://api.braintrust.dev/mcp` (no trailing slash) and ensure your client supports MCP Authorization specification v1.0+.
* **Connection timeouts or server not found**: Check your internet connection. Corporate networks may need to allowlist `api.braintrust.dev` and `*.braintrust.dev`.
* **Self-hosted instance not connecting**: Verify your API URL format is `<YOUR_API_URL>/mcp` and ensure the `MCP_SERVER_URL` environment variable is set correctly.
* **MCP server not appearing in client**: Restart your client application and verify your JSON configuration syntax is valid.
* **Access denied errors**: Verify you have access to the requested project in the Braintrust web interface.
* **BTQL queries failing**: Test your query in the Braintrust web interface first and verify column names with the `infer_schema` tool.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt