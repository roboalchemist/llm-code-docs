# Source: https://docs.datadoghq.com/bits_ai/mcp_server.md

---
title: Datadog MCP Server
description: >-
  Connect AI agents to Datadog observability data using the MCP Server to query
  metrics, logs, traces, and other insights.
breadcrumbs: Docs > Bits AI > Datadog MCP Server
source_url: https://docs.datadoghq.com/mcp_server/index.html
---

# Datadog MCP Server

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

The Datadog MCP Server is in Preview. If you're interested in this feature, complete this form. Read more about the MCP Server on the [Datadog blog](https://www.datadoghq.com/blog/datadog-remote-mcp-server/).

[Request Access](https://www.datadoghq.com/product-preview/datadog-mcp-server/)
{% /callout %}

The Datadog MCP Server acts as a bridge between your observability data in Datadog and any AI agents that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Providing structured access to relevant Datadog contexts, features, and tools, the MCP Server lets you query and retrieve observability insights directly from AI-powered clients such as Cursor, OpenAI Codex, Claude Code, or your own AI agent.

- **Query** metrics, logs, traces, errors, dashboards, monitors, incidents, and servicesâ.
- **Generate code** based on prompts, errors, and existing code.
Use the [Datadog extension for Cursor](https://docs.datadoghq.com/developers/ide_plugins/vscode/?tab=cursor) to enhance the editor's AI-assisted coding capabilities with informed insights from Datadog. The Datadog MCP Server is included in the extension.
## Further reading{% #further-reading %}

- [Connect your AI agents to Datadog tools and context using the Datadog MCP Server](https://www.datadoghq.com/blog/datadog-remote-mcp-server/)
- [Datadog Extension for Cursor](https://docs.datadoghq.com/developers/ide_plugins/vscode/?tab=cursor)
- [Bits AI Overview](https://docs.datadoghq.com/bits_ai/)
- [Debug live production issues with the Datadog Cursor extension](https://www.datadoghq.com/blog/datadog-cursor-extension/)
- [Datadog + OpenAI: Codex CLI integration for AIâassisted DevOps](https://www.datadoghq.com/blog/openai-datadog-ai-devops-agent/)
