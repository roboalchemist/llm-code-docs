# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-gemini-cli.md

# Usage with Gemini CLI

This guide outlines how to connect Make MCP server with Gemini CLI using OAuth.&#x20;

**Prerequisites**

* [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation)
* [Node.js](https://nodejs.org/en/download)

### Installation

To connect Make MCP server to Gemini CLI:

1. In your terminal, run the following command, depending on your transport method:

**Streamable HTTP**

```json
gemini mcp add make --scope user --transport http https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or  `/stream`  to the end of your connection URL.&#x20;
{% endhint %}

**Server-Sent Events (SSE)**

```json
gemini mcp add make --scope user --transport sse https://mcp.make.com/sse
```

2. Run the `Gemini`  command to start Gemini.&#x20;
3. Run `/mcp list` to check if Make is among your configured MCP servers.
4. Run `/mcp auth make` to initiate authentication.&#x20;
5. In the OAuth consent screen, select your organization and scopes, then click **Allow**.

You have now connected Make MCP server to Gemini CLI.

### Call tools on Gemini CLI

You can call Make MCP tools in Gemini CLI:

1. Enter a question related to your connected Make MCP tools.
2. Grant permission for the suggested tool.&#x20;

Gemini CLI calls the relevant tool and responds to your question.&#x20;
