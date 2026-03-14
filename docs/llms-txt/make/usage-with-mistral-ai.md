# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-mistral-ai.md

# Usage with Mistral AI

This guide outlines how to connect Make MCP server to Mistral AI's Le Chat using OAuth.

**Prerequisites**

* Mistral AI account

#### Installation <a href="#installation" id="installation"></a>

To connect Make MCP server to Mistral AI:

1. Open Mistral AI and go to Le Chat.&#x20;
2. Click **Intelligence** in the left sidebar and select **Connectors**.&#x20;
3. Click **Add Connector** on the right side.&#x20;
4. Go to the **Custom MCP Connector** tab.&#x20;
5. In **Connector Name**, name your MCP server to identify it later, for example, "Make."
6. In **Connector Server**, add the following URL:

```
https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or `/stream` to the end of your connection URL. For SSE, add `/sse` instead.
{% endhint %}

7. In **Authentication Method**, select **OAuth2.1** from the dropdown.&#x20;
8. Click **Connect**.&#x20;
9. In the OAuth consent screen, select the organization in **Organization** and its granted scopes.
10. Click **Allow** to proceed.

You've now connected Make MCP server to Mistral AI.&#x20;

To use it in a chat, click your Make MCP server in the **Connectors** section, then click **New Chat**.&#x20;
