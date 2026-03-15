# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/luciq-mcp-server.md

# Luciq MCP Server

{% hint style="info" %}

#### Beta Availability Notice

The Luciq MCP Server is currently in **Private Beta - Early Access.**\
It’s still under active development, and we’re collecting early feedback from selected customers before general release. You may experience incomplete functionality or changes between versions.

\
If you’d like to join the beta or share feedback, contact <support@luciq.ai>.
{% endhint %}

### Connect your AI IDE directly to Luciq’s mobile observability data.

The **Luciq MCP (Model Context Protocol) Serve**r provides a standardized, secure interface that allows any compatible AI model or IDE, such as Cursor, Claude Code, or VS Code MCP clients, to access **crash data, analytics, and debugging insights** from Luciq.

Use natural language to query and explore your app’s health directly inside your IDE:

{% hint style="success" %}
“List my Android apps”\
“Show me production crashes from the last week”\
“Get crash #42 details”
{% endhint %}

***

### Overview

Luciq MCP follows the **authenticated remote** [MCP spec](https://modelcontextprotocol.io/specification/2025-03-26), enabling AI-native tools to connect safely to your workspace.

The server exposes tools for:

* Listing applications
* Fetching crash reports
* Retrieving detailed crash traces
* Discovering crash patterns

#### What is MCP?

Model Context Protocol ([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)) is an open standard introduced by Anthropic. It defines a secure, language-agnostic way for AI tools (like Claude or Cursor) to connect to external data sources and APIs.

In simple terms: MCP allows your AI IDE to “talk to Luciq”, requesting crash logs, analytics, or version data directly from your app’s workspace, using standardized JSON-RPC calls.

Luciq’s MCP Server brings this capability to **mobile observability**, making it the first MCP integration designed specifically for **mobile debugging and release management.**

#### Why MCP?

* **Standardized Interface**. Works natively across all MCP-compatible IDEs
* **AI-Ready**. Lets LLM-powered assistants reason over Luciq data.
* **Simple Integration**. One configuration file, no SDKs required.
* **Secure by Design**. Token-based access scoped to your workspace

***

### Quick Start

Get your first response in **under two minutes.**

**Prerequisites**

* A Luciq account
* Your registered email
* A personal access token (request via <support@luciq.ai>)

<table><thead><tr><th width="169.42578125">Tool</th><th>What it Does</th><th>Example Prompt</th></tr></thead><tbody><tr><td>listApplications</td><td>Lists all apps connected to your workspace</td><td>"List my Android apps."</td></tr><tr><td>listCrashes</td><td>Retrieves crash reports for a specific app or environment</td><td>"Show production crashes for luciqai."</td></tr><tr><td>crashDetails</td><td>Displays stack trace and metadata for a crash</td><td>"Get details for crash #42."</td></tr><tr><td>crashPatterns</td><td>Aggregates crash data by device, OS, or version</td><td>"Show crash patterns for crash #5 grouped by devices."</td></tr></tbody></table>

***

### Demo

{% embed url="<https://streamable.com/73j693>" %}

***

### Next Steps

* See [Authentication & Setup](https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/luciq-mcp-server/mcp-server-authentication-and-setup) for detailed configuration guides.
* Explore [MCP Tools](https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/luciq-mcp-server/mcp-tools-reference) for available detailed documentation of tools.
* Join the **Private Beta feedback program** at <support@luciq.ai>.

***

### FAQs

**Why am I seeing “App not found”?**\
Your token may not have permission for that app or mode.\
Check with your Luciq admin.

**Can I rotate tokens?**\
Yes — contact <support@luciq.ai> to regenerate.

**Does Luciq support OAuth 2.1?**

Coming soon. Current auth is token-based via headers.
