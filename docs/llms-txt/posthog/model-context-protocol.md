# Source: https://posthog.com/docs/model-context-protocol.md

# Model Context Protocol (MCP) - Docs

The PostHog [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server enables your AI agents and tools to directly interact with PostHog's products.

## Quick install using the PostHog wizard

Besides being able to [quickly set up your project using AI](/docs/getting-started/install?tab=wizard.md), the [PostHog Wizard](https://github.com/PostHog/wizard) can also install the MCP server directly into **Cursor**, **Claude Code**, **Claude Desktop**, **Codex**, **VS Code** and **Zed**.

Terminal

PostHog AI

```bash
npx @posthog/wizard mcp add
```

We're working on adding more supported tools to the wizard. If you're using another option, you can manually install our MCP server with the instructions below.

## Manual install

Add the MCP configuration to your client. When you first use the MCP server, you'll be prompted to log in to PostHog to authenticate.

## Claude Code

Run the following command in your shell. The next time you run [Claude Code](https://www.anthropic.com/claude-code), it will have access to the PostHog MCP.

Terminal

PostHog AI

```bash
claude mcp add --transport http posthog https://mcp.posthog.com/mcp -s user
```

## Claude Desktop

1.  Open [Claude Desktop](http://claude.ai/download) and navigate to **Settings > Developer**
2.  Click **Edit Config** to open the configuration file
3.  Update `claude_desktop_config.json` with the following configuration:

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://mcp.posthog.com/sse"
      ]
    }
  }
}
```

4.  **Save** the configuration file and **restart Claude Desktop**
5.  The MCP server should show as **PostHog** in your list of Connectors found in **Settings > Connectors**

## Codex

Run the following command in your shell. [Codex](https://openai.com/index/introducing-codex/) supports native OAuth, so you'll be prompted to log in to PostHog when you first use the MCP.

Terminal

PostHog AI

```bash
codex mcp add posthog --url https://mcp.posthog.com/mcp
```

## Cursor

1.  Open [Cursor](https://cursor.com) and navigate to **Cursor Settings > Tools & Integrations**
2.  Click **New MCP Server**
3.  Update `mcp.json` with the following configuration:

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "url": "https://mcp.posthog.com/mcp"
    }
  }
}
```

4.  **Save** the configuration file
5.  You should see **posthog** under **MCP Tools** with a green status

## Windsurf

1.  Open [Windsurf](https://windsurf.com/) and navigate to **Windsurf Settings > Cascade > MCP Servers**
2.  Click **Manage MCP Servers**
3.  Click **View raw config**
4.  Update `mcp_config.json` with the following configuration:

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://mcp.posthog.com/sse"
      ]
    }
  }
}
```

## VS Code

1.  Open [Visual Studio Code](https://code.visualstudio.com/). In the command palette, run: `MCP: Open User Configuration` to open the configuration file
2.  Update `mcp.json` with the following configuration:

JSON

PostHog AI

```json
{
  "servers": {
    "posthog": {
      "type": "http",
      "url": "https://mcp.posthog.com/mcp"
    }
  }
}
```

3.  **Save** the configuration file
4.  The MCP server will now be available the next time you chat with Copilot

## Zed

1.  Open [Zed](https://zed.dev) and update `settings.json` with the following configuration:

JSON

PostHog AI

```json
{
  "context_servers": {
    "posthog": {
      "enabled": true,
      "url": "https://mcp.posthog.com/mcp"
    }
  }
}
```

2.  **Save** the configuration file
3.  The PostHog MCP server will be available

## Lovable

Custom MCP servers require a [paid Lovable plan](https://docs.lovable.dev/integrations/mcp-servers).

1.  Go to **Settings** → **Connectors** → **Personal connectors**
2.  Click **New MCP server**
3.  Enter the name `PostHog` and URL `https://mcp.posthog.com/mcp`
4.  Under **Authentication**, select **OAuth**
5.  Click **Add & authorize**, then log in to PostHog when prompted

For more details on setting up PostHog in your Lovable project, see the [Lovable integration guide](/docs/integrations/lovable.md).

## Replit

1.  [Add PostHog to Replit](https://replit.com/integrations?mcp=eyJkaXNwbGF5TmFtZSI6IlBvc3RIb2ciLCJiYXNlVXJsIjoiaHR0cHM6Ly9tY3AucG9zdGhvZy5jb20vbWNwIn0=)
2.  When prompted, log in to PostHog to authorize access
3.  The PostHog MCP server will now be available in your Replit Agent

## v0

1.  In a v0 chat, click the **+** button in the bottom left
2.  Click **MCPs**
3.  Click **Add MCP**
4.  Select **Custom MCP**
5.  Enter the name `PostHog` and URL `https://mcp.posthog.com/mcp`
6.  Under **Authentication**, select **OAuth**
7.  Click **Add**, then authorize with PostHog when prompted

Alternatively, you can use a [personal API key](/docs/integrations/v0.md#oauth-not-refreshing) with Bearer authentication.

Be mindful of prompt injection – LLMs can be tricked into following untrusted commands, so always review tool calls before executing them.

Using an API key instead of OAuth?

If your MCP client doesn't support OAuth, you can authenticate manually:

1.  Create a [personal API key](https://app.posthog.com/settings/user-api-keys?preset=mcp_server) using the **MCP Server** preset (this scopes access to a specific project)
2.  Add the `Authorization: Bearer YOUR_API_KEY` header to your MCP configuration

Example for Cursor (add to `.cursor/mcp.json`):

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "url": "https://mcp.posthog.com/mcp",
      "headers": {
        "Authorization": "Bearer phx_your_api_key_here"
      }
    }
  }
}
```

Pinning to a specific organization or project?

If you're building a programmatic integration or want to restrict the MCP session to a specific organization or project, you can pin the context using headers or query parameters.

When you pin the context, the `switch-organization` and `switch-project` tools are automatically excluded from the available tool list:

-   When `projectId` is provided: both `switch-organization` and `switch-project` are excluded
-   When only `organizationId` is provided: only `switch-organization` is excluded

**Headers:**

-   `x-posthog-organization-id` - Pin to a specific organization
-   `x-posthog-project-id` - Pin to a specific project

**Query parameters:**

-   `organization_id` - Pin to a specific organization
-   `project_id` - Pin to a specific project

Example for Cursor (add to `.cursor/mcp.json`):

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "url": "https://mcp.posthog.com/mcp",
      "headers": {
        "Authorization": "Bearer phx_your_api_key_here",
        "x-posthog-organization-id": "your_org_id",
        "x-posthog-project-id": "your_project_id"
      }
    }
  }
}
```

Enabling read-only mode?

Read-only mode restricts the MCP server to only expose tools that don't modify data (i.e., tools annotated with `readOnlyHint: true`). This is useful when you want to limit an agent to querying and listing data without the ability to create, update, or delete resources.

You can enable read-only mode using a header or query parameter:

**Header:**

-   `x-posthog-readonly` - Set to `true` or `1`

**Query parameter:**

-   `readonly` - Set to `true` or `1`

Example for Cursor (add to `.cursor/mcp.json`):

JSON

PostHog AI

```json
{
  "mcpServers": {
    "posthog": {
      "url": "https://mcp.posthog.com/mcp",
      "headers": {
        "Authorization": "Bearer phx_your_api_key_here",
        "x-posthog-readonly": "true"
      }
    }
  }
}
```

## Available Tools

Tools trigger actions on behalf of the user based on the goals and information already in the context of the LLM.

Here's a list of tools we provide:

### Actions

| Tool | Purpose |
| --- | --- |
| action-create | Create action |
| action-delete | Delete action |
| action-get | Get action |
| action-update | Update action |
| actions-get-all | Get all actions |

### Annotations

| Tool | Purpose |
| --- | --- |
| annotation-create | Create annotation |
| annotation-delete | Delete annotation |
| annotation-retrieve | Retrieve annotation |
| annotations-list | List annotations |
| annotations-partial-update | Update annotation |

### Cohorts

| Tool | Purpose |
| --- | --- |
| cohorts-add-persons-to-static-cohort-partial-update | Add persons to static cohort |
| cohorts-create | Create cohort |
| cohorts-list | List all cohorts |
| cohorts-partial-update | Update cohort |
| cohorts-retrieve | Get cohort |
| cohorts-rm-person-from-static-cohort-partial-update | Remove person from static cohort |

### Dashboards

| Tool | Purpose |
| --- | --- |
| dashboard-create | Create dashboard |
| dashboard-delete | Delete dashboard |
| dashboard-get | Get dashboard |
| dashboard-reorder-tiles | Reorder dashboard tiles |
| dashboard-update | Update dashboard |
| dashboards-get-all | Get all dashboards |

### Data schema

| Tool | Purpose |
| --- | --- |
| read-data-schema | Explore the user's events, actions, properties, and property values. |
| read-data-warehouse-schema | Read core data warehouse schemas and table lists. |

### Debug

| Tool | Purpose |
| --- | --- |
| debug-mcp-ui-apps | Debug tool for testing MCP Apps SDK. |

### Documentation

| Tool | Purpose |
| --- | --- |
| docs-search | Search the PostHog documentation for information. |

### Error tracking

| Tool | Purpose |
| --- | --- |
| error-details | Get the details of an error in the project. |
| error-tracking-issues-list | List error tracking issues |
| error-tracking-issues-partial-update | Update error tracking issue |
| error-tracking-issues-retrieve | Get error tracking issue |
| list-errors | List errors in the project. |
| update-issue-status | Update the status of an error tracking issue. |

### Events & properties

| Tool | Purpose |
| --- | --- |
| event-definition-update | Update an event definition's metadata. |
| event-definitions-list | List all event definitions in the project with optional filtering. |
| properties-list | Get properties for events or persons. |

### Experiments

| Tool | Purpose |
| --- | --- |
| experiment-create | Create A/B test experiment with guided metric and feature flag setup |
| experiment-delete | Delete an experiment by ID. |
| experiment-get | Get details of a specific experiment. |
| experiment-get-all | Get all experiments in the project. |
| experiment-results-get | Get comprehensive experiment results including metrics and exposure data. |
| experiment-update | Update an existing experiment with lifecycle management and restart capability. |

### Feature flags

| Tool | Purpose |
| --- | --- |
| create-feature-flag | Create feature flag |
| delete-feature-flag | Delete feature flag |
| feature-flag-get-all | Get all feature flags |
| feature-flag-get-definition | Get feature flag definition |
| update-feature-flag | Update feature flag |

### Function templates

| Tool | Purpose |
| --- | --- |
| cdp-function-templates-list | List function templates |
| cdp-function-templates-retrieve | Get function template |

### Functions

| Tool | Purpose |
| --- | --- |
| cdp-functions-create | Create function |
| cdp-functions-delete | Delete function |
| cdp-functions-invocations-create | Test-invoke function |
| cdp-functions-list | List functions |
| cdp-functions-partial-update | Update function |
| cdp-functions-rearrange-partial-update | Reorder transformation execution |
| cdp-functions-retrieve | Get function |

### Insights & analytics

| Tool | Purpose |
| --- | --- |
| insight-create-from-query | Save a query as an insight. |
| insight-delete | Delete an insight by ID. |
| insight-get | Get a specific insight by ID. |
| insight-query | Execute a query on an existing insight to get its results/data. |
| insight-update | Update an existing insight by ID. |
| insights-get-all | Get all insights in the project with optional filtering. |
| query-generate-hogql-from-question | Queries project's PostHog data based on a provided natural language question. |
| query-run | Run a trend, funnel, paths or HogQL query. |

### LLM analytics

| Tool | Purpose |
| --- | --- |
| evaluation-create | Create a new evaluation. |
| evaluation-delete | Delete an evaluation. |
| evaluation-get | Get a specific evaluation by ID. |
| evaluation-run | Run an evaluation on a specific event. |
| evaluation-update | Update an evaluation. |
| evaluations-get | List LLM analytics evaluations. |
| get-llm-total-costs-for-project | Fetches the total LLM daily costs for each model for a project over a given number of days. |

### Logs

| Tool | Purpose |
| --- | --- |
| logs-list-attribute-values | Get values for a log attribute. |
| logs-list-attributes | List available log attributes. |
| logs-query | Search and query logs in the project. |

### Organization & project management

| Tool | Purpose |
| --- | --- |
| organization-details-get | Get the details of the active organization. |
| organizations-get | Get the organizations the user has access to. |
| projects-get | Fetches projects that the user has access to in the current organization. |
| property-definitions | Get event and property definitions for the project. |
| switch-organization | Change the active organization from the default organization. |
| switch-project | Change the active project from the default project. |

### Prompts

| Tool | Purpose |
| --- | --- |
| prompt-create | Create prompt |
| prompt-get | Get prompt |
| prompt-list | List prompts |
| prompt-update | Update prompt |

### Reverse proxy

| Tool | Purpose |
| --- | --- |
| proxy-create | Create reverse proxy |
| proxy-delete | Delete reverse proxy |
| proxy-get | Get reverse proxy details |
| proxy-list | List reverse proxies |
| proxy-retry | Retry reverse proxy provisioning |

### Search

| Tool | Purpose |
| --- | --- |
| entity-search | Search for entities by name or description. |

### SQL

| Tool | Purpose |
| --- | --- |
| execute-sql | Execute an SQL query. |

### Surveys

| Tool | Purpose |
| --- | --- |
| survey-create | Creates a new survey in the project. |
| survey-delete | Delete a survey by ID. |
| survey-get | Get a specific survey by ID. |
| survey-stats | Get response statistics for a specific survey. |
| survey-update | Update an existing survey by ID. |
| surveys-get-all | Get all surveys in the project with optional filtering. |
| surveys-global-stats | Get aggregated response statistics across all surveys. |

### Workflows

| Tool | Purpose |
| --- | --- |
| workflows-get | Get workflow |
| workflows-list | List workflows |

## Example prompts

Here are some examples of what you can ask your AI agent to do with the PostHog MCP server:

### Feature flag management

**Prompt:** "Create a feature flag called 'new-checkout-flow' that's enabled for 20% of users"

The agent will use the `create-feature-flag` tool to create the flag with a 20% rollout and return the configuration including the key, rollout percentage, and a link to the flag in PostHog.

### Multivariate feature flags

**Prompt:** "Create a multivariate feature flag called 'homepage-hero-test' with three variants: control at 34%, variant\_a at 33%, and variant\_b at 33%"

The agent will use the `create-feature-flag` tool with a `multivariate` configuration to create the flag with multiple variants. Variant rollout percentages must be integers that sum to 100.

### Analytics queries

**Prompt:** "How many unique users signed up in the last 7 days, broken down by day?"

The agent will use the `query-run` tool to execute a trends query and return daily signup counts.

### Path analysis

**Prompt:** "What are the most common paths users take after signing up?"

The agent will use the `query-run` tool with a PathsQuery to analyze user journeys, returning the flow of events users follow after signup.

**Prompt:** "Show me the navigation paths from the pricing page to checkout"

The agent will execute a paths query with `startPoint` set to the pricing page and `endPoint` set to checkout, revealing the most common routes users take.

### SQL and HogQL queries

Your AI agent can execute complex HogQL queries to analyze both system data and analytics data in PostHog.

**Prompt:** "Query my feature flags to find all flags that are rolled out to less than 50% of users"

The agent will use SQL to query the `system.feature_flags` table and return flags filtered by rollout percentage.

**Prompt:** "Write a HogQL query to find users who triggered the signup event but didn't complete onboarding in the last 30 days"

The agent will construct and execute a HogQL query against the `events` table, using subqueries to find users who signed up but are missing the onboarding completion event.

**Prompt:** "What cohorts contain users who made a purchase in the last week?"

The agent will query `system.cohorts` and cross-reference with purchase events to identify relevant cohorts.

### A/B test creation

**Prompt:** "Create an A/B test for our pricing page that measures conversion to checkout"

The agent will use `experiment-create` to set up an experiment with control/test variants and configure a funnel metric measuring pricing page to checkout conversion.

### Error investigation

**Prompt:** "What are the top 5 errors in my project this week?"

The agent will use the `list-errors` tool to fetch error groups sorted by occurrence count and return details including affected user counts.

### Log investigation

**Prompt:** "Show me error logs from the payments service in the last hour"

The agent will use `logs-query` to search for logs filtered by severity level and service name, returning log entries with timestamps, messages, and trace information.

### Prompt management

**Prompt:** "List all prompts stored in my project"

The agent will use the `prompt-list` tool to retrieve all team prompts and return a summary with names, versions, and timestamps.

**Prompt:** "Create a prompt called 'code-reviewer' with instructions for reviewing pull requests"

The agent will use the `prompt-create` tool to create a new prompt with the specified name and content, making it available for use across all MCP-connected agents in your team.

**Prompt:** "Get the latest version of my 'support-assistant' prompt"

The agent will use the `prompt-get` tool to retrieve the full prompt content by name. You can also request a specific version if needed.

**Prompt:** "Update the 'onboarding-guide' prompt to include a section about feature flags"

The agent will use the `prompt-update` tool to publish a new version of the prompt with the updated content. The update includes conflict detection to prevent overwriting changes made by others.

## Prompts and resources

The MCP server provides **resources**, including framework-specific documentation and example code, to help agents build great PostHog integrations. You can try these yourself using the `posthog:posthog-setup` **prompt**, available via a slash command in your agent. Just hit the `/` key.

Currently we support Next.js, with more frameworks in progress.

## Privacy and support

-   **Privacy Policy:** [posthog.com/privacy](/privacy.md)
-   **Terms of Service:** [posthog.com/terms](/terms.md)
-   **Support:** [posthog.com/questions](/questions.md) or [in-app support](https://app.posthog.com/home#supportModal)

The MCP server acts as a proxy to your PostHog instance. It does not store your analytics data - all queries are executed against your PostHog project and results are returned directly to your AI client.

## Next steps

-   [Lovable integration](/docs/integrations/lovable.md): Set up PostHog in your Lovable project
-   [Replit integration](/docs/integrations/replit.md): Set up PostHog with Replit Agent
-   [v0 integration](/docs/integrations/v0.md): Set up PostHog with v0 and the Vercel Flags SDK
-   [PostHog MCP server](https://github.com/PostHog/posthog/tree/master/services/mcp): Check out GitHub repository for the MCP server
-   [Model Context Protocol](https://modelcontextprotocol.io/introduction): Learn more about the Model Context Protocol specification
-   [MCP: machine/copy paste](/blog/machine-copy-paste-mcp-intro.md): What exactly is MCP again?

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better