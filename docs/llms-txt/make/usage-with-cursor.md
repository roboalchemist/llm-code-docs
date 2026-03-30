# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-cursor.md

# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-cursor.md

# Usage with Cursor

This guide outlines how to connect Make MCP server with Cursor using OAuth.&#x20;

**Prerequisites**

* Cursor account (Desktop version)

### Installation

To connect Make MCP server to Cursor:

1. Open your Cursor account.&#x20;
2. On the upper right-hand side, click the gear icon to open the **Cursor Settings** dialog.&#x20;
3. In the left sidebar, click **Tools & Integrations** (or **Tools**, if you're on the Free Plan).
4. Under **MCP Tools**, click **Add Custom MCP** to open the editor for the `mcp.json` file.

<div align="center"><figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FVKzamHi8yhhLaLjxw25h%2Fcursor%20app.png?alt=media&#x26;token=101b62f1-4b2c-4fe8-b963-86e9fd2b18cd" alt="" width="375"><figcaption></figcaption></figure></div>

5. In the editor, add the configuration.

Use the following URL:

```
https://mcp.make.com
```

Configuration example:

```json
{
  "mcpServers": {
    "make": {
      "url": "https://mcp.make.com"
    }
  }
}
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or  `/stream`  to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

6. In **MCP Tools**, you'll see Make added as an MCP tool. Click **Needs login**.

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FsPn874DqyVBCrDfZwc84%2Fneeds%20login.png?alt=media&#x26;token=208c439c-2d30-4d46-8a56-78130bb4a8e1" alt="" width="375"><figcaption></figcaption></figure>

7. In the dialog, click **Open**, which opens an OAuth consent screen.&#x20;
8. In the **Organization** dropdown, select the organization that can access the server.
9. Select its granted scopes.&#x20;
10. Click **Allow**, then **Open Cursor**.&#x20;
11. Click **Open** to allow the extension to open the URI.&#x20;

You have now connected Make MCP server to Cursor.&#x20;
