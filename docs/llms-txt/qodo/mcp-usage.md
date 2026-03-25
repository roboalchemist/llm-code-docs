# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/usage/mcp-usage.md

# MCP Usage

## Using Qodo Context Engine as an MCP

{% hint style="success" %}
Supported for single-tenant and on-prem deployments.&#x20;
{% endhint %}

### What is MCP?

MCP stands for **Model Context Protocol.** It's an open protocol that standardizes how tools and services expose structured context to AI models.

It defines a consistent way for applications to communicate with AI, making it easier to integrate external systems like version control, issue trackers, or shell environments into your workflow.

### Why use Qodo Context Engine as an MCP server?

Qodo Context Engine offers a deeply indexed, AI-enhanced view of your organization’s codebase.

Using it as an MCP server means:

* You can connect products like Claude Desktop, Cursor, or others directly to your remote codebase via Qodo Context Engine.
* You get consistent, organization-aware responses, grounded in your real repositories, services, and documentation.
* You benefit from Qodo Context Engine’s agentic reasoning and advanced retrieval, even outside the Qodo interface.
* Eliminate context switching—your tools now understand your code as if a senior engineer were helping.

***

## Setup and Installation

{% hint style="warning" %}

### Before you start

Contact Qodo to receive your **client domain and token**.

These are necessary for setting up Qodo Context Engine as an MCP.
{% endhint %}

### Requirements

* Node.js installed (v18.0.0 and above)
* Cursor, Windsurf, Claude Desktop or another MCP Client

### Installation

You can add Qodo Context Engine as an MCP server to any product that supports the Model Context Protocol (MCP).

Check out our open source repository:

{% embed url="<https://github.com/qodo-ai/open-aware>" %}

Installation steps vary by tool:

<details>

<summary>Cursor</summary>

1. Open **Cursor Settings**.
2. Navigate to the **MCP** section and select **Add new global MCP server**.
3. Paste the [Qodo Aware MCP configuration](https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/setup-qodo-aware/mcp#configuration) in your `mcp.json` file.

You can also add Qodo Aware to a specific project by creating a separate `mcp.json` file inside the project directory. [See Cursor's MCP documentation](https://github.com/geelen/mcp-remote#using-with-cursor) to learn more.

</details>

<details>

<summary>Windsurf</summary>

Add the [Qodo Aware MCP configuration](https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/setup-qodo-aware/mcp#configuration) to your Windsurf MCP config file.

</details>

<details>

<summary>Claude Desktop</summary>

Add the [Qodo Aware MCP configuration](https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/setup-qodo-aware/mcp#configuration) to your Claude Desktop `claude_desktop_config.json` file.

</details>

<details>

<summary>GitHub Copilot</summary>

Add the [Qodo Aware MCP configuration](https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/setup-qodo-aware/mcp#configuration) to the `mcp` section of your Copilot Coding Agent configuration file:

Repository -> Settings -> Copilot -> Coding agent -> **MCP configuration**.

For more information, see the [official GitHub documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).

</details>

<details>

<summary>Other Products</summary>

If your product supports MCP, [add the Qodo Aware configuration](https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/setup-qodo-aware/mcp#configuration) wherever MCP servers are defined in that tool’s settings or configuration file.

</details>

### Configuration

```json
{
  "mcpServers": {
    "remote-codebase-search": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://<QODO_AWARE_CLIENT_DOMAIN>/mcp/",
        "--header",
        "Authorization:${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "Bearer <QODO_AWARE_TOKEN>"
      }
    }
  }
}
```

Replace `QODO_AWARE_CLIENT_DOMAIN` and `QODO_AWARE_TOKEN` with your client domain and token.
