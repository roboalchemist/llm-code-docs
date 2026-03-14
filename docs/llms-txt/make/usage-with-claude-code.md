# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-claude-code.md

# Usage with Claude Code

This guide outlines how to connect Make MCP server with Claude Code using OAuth.&#x20;

**Prerequisites**

* [Claude Code ](https://code.claude.com/docs/en/setup)
* [Node.js](https://nodejs.org/en)

### Installation

To connect Make MCP server to Claude Code:

1. In your terminal, open a new tab.
2. Run the following command, depending on your transport method:

**Streamable HTTP**

```
claude mcp add --transport http make https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or `/stream` to the end of the connection URL.
{% endhint %}

**Server-Sent Events (SSE)**

```
claude mcp add --transport sse make https://mcp.make.com/sse
```

3. Run the command `Claude`.
4. Run `/mcp` to connect to available MCP servers.&#x20;
5. In the OAuth consent screen in the new browser window, select your organization and scopes.
6. The response in the CLI indicates whether your Make server connected successfully.&#x20;

You have now connected Make MCP server to Claude Code.&#x20;

### Call tools on Claude Code&#x20;

You can call Make MCP tools in the Claude CLI:

1. Enter a question related to your connected Make MCP tools.
2. When asked if you want to proceed, select `Yes`.

Claude Code calls the relevant tool and responds to your question.&#x20;
