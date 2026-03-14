# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-claude-desktop.md

# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-claude-desktop.md

# Usage with Claude Desktop

This guide outlines how to connect Make MCP server with Claude Desktop using OAuth.&#x20;

**Prerequisites**

* Claude Desktop account (paid subscription)

### Installation

To connect Make MCP server to Claude Desktop:

1. Open your Claude Desktop account.
2. Click your profile name on the left sidebar, then **Settings**.
3. In **Settings**, navigate to **Connectors**.&#x20;
4. Click **Add custom connector**, which opens a dialog.&#x20;
5. In the **URL** field, add the following URL:&#x20;

```json
https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or  `/stream`  to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

6. In **Connectors**, find Make and click **Connect.**

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2F6td0CHbrb0jkrX1ZeAkb%2FMCP%20connect%20no%20magent.png?alt=media&#x26;token=39caf49e-9e17-4dd1-9279-1810bae672e4" alt="" width="375"><figcaption></figcaption></figure>

7. In the OAuth consent screen, select the organization in **Organization** and its granted scopes.
8. Click **Allow** to proceed.&#x20;

You've now connected Make MCP server to Claude Desktop.&#x20;
