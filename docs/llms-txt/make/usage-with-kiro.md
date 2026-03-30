# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-kiro.md

# Usage with Kiro

This guide outlines how to connect Make MCP server with Kiro using OAuth.&#x20;

**Prerequisites**

* [Kiro](https://kiro.dev/docs/getting-started/installation/)

### Installation

To connect Make MCP server to Kiro:

1. In Kiro, click the ghost icon on the left sidebar.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2F31zI2Txj9D0pC0v2YziS%2Fghost%20left%20sidebar.png?alt=media&#x26;token=1fd000db-c267-4c29-8276-6d8c20117163" alt="" width="563"><figcaption></figcaption></figure>

2. Hover over the **MCP servers** section and click the **Open MCP Config** icon.
3. In the `mcp.json` configuration, add the following:&#x20;

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
If you experience connection issues, you can add `/stateless` or `/stream` to the end of the connection URL. For SSE, add  `/sse` instead.
{% endhint %}

5. Enter `Ctrl` + `S` (Windows) or `Cmd` + `S` (Mac) to save. The OAuth consent screen opens in a new browser window.
6. In the consent screen, select your organization and scopes, then click **Allow**.
7. Return to the **MCP servers** section to check whether Make MCP server connected successfully.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FcqgWYNyy3nS1t9hmbnYS%2Fkiro%20terminal.png?alt=media&#x26;token=848945e9-240a-471d-8e44-6bd5af688620" alt="" width="563"><figcaption></figcaption></figure>

You have now connected Make MCP server to Kiro.&#x20;

### Call tools on Kiro

You can call Make MCP tools in the chat:

1. To open the chat, enter  `Ctrl` + `L` (Windows) or `Cmd` + `L` (Mac).&#x20;
2. Enter a question related to your connected Make MCP tools.
3. When asked for permission to call a specific MCP tool, click **Accept**.&#x20;

Kiro calls the relevant tool and responds to your question.&#x20;
