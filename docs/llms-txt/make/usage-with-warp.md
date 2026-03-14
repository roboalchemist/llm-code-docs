# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-warp.md

# Usage with Warp

This guide outlines how to connect Make MCP server with Warp using OAuth.&#x20;

**Prerequisites**

* [Warp](https://www.warp.dev/download)

### Installation

To connect Make MCP server to Warp:

1. In Warp Drive, go to **MCP Servers** under **Personal**.&#x20;
2. Click **Add.**
3. Enter the following configuration:

```json
{
  "make": {
    "url": "https://mcp.make.com"}
  }
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or  `/stream`  to the end of your connection URL. For SSE, add  `/sse` instead.
{% endhint %}

4. Click **Save** and wait for Make MCP server to connect.&#x20;
5. In the OAuth consent screen, select your organization and scopes, then click **Allow**.

You have now connected Make MPC server to Warp.&#x20;

### Call tools on Warp&#x20;

You can call Make MCP tools in the Warp terminal:

1. Enter a question related to your connected Make MCP tools.
2. When asked for permission to call a specific MCP tool, click **Run**.&#x20;

Warp calls the relevant tool and responds to your question.&#x20;
