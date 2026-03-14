# Source: https://docs.logrocket.com/docs/mcp.md

# LogRocket MCP Server

An MCP server for integrating LogRocket data with your LLM applications

## Summary

An MCP (Model Context Protocol) server that allows Cursor, Claude Code, Codex, and other MCP clients to query the LogRocket API in natural language to access information about your LogRocket sessions, metrics, issues, and more. For example, allows you to:

* Pull in context about your app's behavior to help with debugging and fixing errors
* Get a better sense of how users interact with your app
* Query a user or account's sessions for targeted investigation

See [Ask Galileo](https://docs.logrocket.com/docs/ask-galileo) for information about what the LogRocket MCP server can help with.

## Example Prompts

Here are some examples of how you can use the LogRocket MCP server in your AI-assisted workflow:

* **Fix user-reported issues:** "User X reported a problem with checkout. Can you use LogRocket to watch their sessions, figure out the root cause, and fix it?"
* **Understand feature usage:** "I'm about to work on the search feature — can you use LogRocket to help me understand how it's currently being used?"
* **Triage new issues:** "Can you look at LogRocket for new issues from the past week, try to figure out their root causes, and then suggest which ones I can fix?"
* **Check for regressions:** "Look at all commits from last week, and check LogRocket data to ensure they didn't introduce any regressions."
* **Prioritize your work:** "Use LogRocket to watch sessions and look at issues to figure out what is highest priority that I work on next."

## Suggested Automations

Because the MCP server can be called programmatically by AI agents, you can also set up powerful automations that continuously leverage LogRocket data:

* **Research churning customers and low NPS scores:** Automatically pull LogRocket sessions for users who are churning or leaving low NPS scores to understand what went wrong in their experience.
* **Research new support tickets:** Connect to your help desk to automatically research incoming support tickets using LogRocket session data. LogRocket offers out-of-the-box integrations with [Zendesk](https://docs.logrocket.com/docs/zendesk) and [Intercom](https://docs.logrocket.com/docs/intercom) to attach session replays directly to tickets.
* **Summarize user behavior for sales and customer success:** Automatically generate summaries of how key accounts are using your product, giving your sales and customer success teams actionable insights.
* **Connect LogRocket with your backend data:** Build a skill that allows your agent to correlate LogRocket frontend data with backend observability tools (e.g., Datadog MCP) for end-to-end debugging.
* **Run daily or weekly reports:** Schedule an agent to look for new issues and UX frustration signals on a recurring basis, so your team is always aware of emerging problems.

## Setup

The LogRocket MCP server is available at `https://mcp.logrocket.com/mcp`. The setup instructions below use this URL. It allows your MCP client to access the same LogRocket organizations and projects you can access in your browser.

You can also choose to restrict your MCP client's access to a specific LogRocket organization or LogRocket project by adding to the MCP server URL's path:

* To scope to an organization, use `https://mcp.logrocket.com/mcp/<your_organization_id>`
* To scope to a project, use `https://mcp.logrocket.com/mcp/<your_organization_id>/<your_project_id>`

You can find organization and project IDs in most LogRocket URLs (e.g., `https://app.logrocket.com/<your_organization_id>/<your_project_id>/s/...`). You can also find them in the LogRocket dashboard under **Settings > Project Settings**. The App ID listed there has the form `<your_org_id>/<your_project_id>`.

### Cursor

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=logrocket\&config=eyJ1cmwiOiJodHRwczovL21jcC5sb2dyb2NrZXQuY29tL21jcCJ9)

To install manually:

1. Press `⌘` + `Shift` + `J` to open Cursor Settings.
2. Select **Tools & MCP**.
3. Select **New MCP Server**.
4. ```json
   {
     "mcpServers": {
       "logrocket": {
         "url": "https://mcp.logrocket.com/mcp"
       }
     }
   }
   ```
5. **Connect** to the MCP server in the settings screen to authenticate.

### Claude Code

1. Open your terminal to access the CLI.
2. `claude mcp add --transport http logrocket https://mcp.logrocket.com/mcp`.
3. Follow the prompts to authenticate.
   1. If authentication doesn't happen automatically, trigger it manually with `/mcp`.

### Codex

Codex stores MCP configuration in `~/.codex/config.toml` (or a project-scoped `.codex/config.toml`). You can add the LogRocket server via the CLI or by editing the config file.

**Using the CLI:**

1. Open your terminal and run:
   ```bash
   codex mcp add logrocket --url https://mcp.logrocket.com/mcp
   ```
2. Run `codex mcp login logrocket` and follow the prompts to authenticate.

**Using config.toml:**

1. Open `~/.codex/config.toml` (or in the Codex IDE extension: MCP settings → Open config.toml from the gear menu).
2. Add a `[mcp_servers.logrocket]` section with the server URL:
   ```toml
   [mcp_servers.logrocket]
   url = "https://mcp.logrocket.com/mcp"
   ```
3. Run `codex mcp login logrocket` and follow the prompts to authenticate.

In the Codex TUI, use `/mcp` to see your active MCP servers.

### VS Code

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_LogRocket_MCP-764abc?style=flat\&logo=visualstudiocode\&logoColor=ffffff)](vscode:mcp/install?%7B%22name%22%3A%22LogRocket%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.logrocket.com%2Fmcp%22%7D)

To install manually:

1. Press `⌘` + `P` and search for **MCP: Add Server**.
2. Select **HTTP (HTTP or Server-Sent Events)**.
3. Enter the URL from above (e.g., `https://mcp.logrocket.com/mcp`) and hit enter.
4. Enter the name **LogRocket** and hit enter.
5. Follow the prompts to authenticate.
6. Activate the server using **MCP: List Servers**, selecting **LogRocket**, then selecting **Start Server**.

<br />