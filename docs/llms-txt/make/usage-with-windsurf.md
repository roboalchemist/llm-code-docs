# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-windsurf.md

# Usage with Windsurf

This guide outlines how to connect Make MCP server with Windsurf using OAuth.&#x20;

**Prerequisites**

* [Windsurf](https://windsurf.com/download)&#x20;
* [Node.js](https://nodejs.org/en)

### Installation

To connect Make MCP server to Windsurf:

1. In Windsurf, click the **Settings** icon in the top-right corner, and select **Windsurf Settings**.&#x20;
2. In Cascade, click the **Open MCP Marketplace** link next to **MCP Servers**.&#x20;
3. In **Installed MCPs**, click the **Settings** icon to open the `mcp.config.json` configuration file.&#x20;
4. Add the following configuration:

```json
{
  "mcpServers": {
    "make": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.make.com"
      ]
    }
  }
}
```

{% hint style="success" %}
&#x20;If you experience connection issues, you can add `/stateless` or `/stream` to the end of the connection URL.&#x20;
{% endhint %}

5. Enter `Ctrl` + `S` (Windows) or `Cmd` + `S` (Mac) to save. The OAuth consent screen opens in a new browser window.
6. In the consent screen, select your organization and scopes, then click **Allow**.
7. Return to the **Installed MCPs** section to check whether Make MCP server connected successfully.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FMKR8Kt0hdKRsybXhx1Br%2FWindsurf%20view.png?alt=media&#x26;token=84a30ffa-a89b-47de-b52c-b04514b9c8da" alt="" width="563"><figcaption></figcaption></figure>

You have now connected Make MCP server to Windsurf.&#x20;

### Call tools on Windsurf

You can call Make MCP tools in the chat:

1. Click the **Toggle Cascade Side Bar** icon in the top-right corner, or enter `Ctrl`+`Alt`+`B` (Windows) or `Cmd`+`Option`+`B` (Mac).
2. Enter a question related to your connected Make MCP tools.

Windsurf calls the relevant tool and responds to your question.&#x20;
