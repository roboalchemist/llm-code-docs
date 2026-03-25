# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-openai.md

# Usage with OpenAI

This guide outlines how to connect Make MCP server with OpenAI using an MCP token.

**Prerequisites**

* OpenAI Platform account
* [MCP token](https://developers.make.com/mcp-server/connect-using-mcp-token)

### Installation

To connect Make MCP server to OpenAI:

1. In OpenAI's Playground, sign in to your OpenAI account.&#x20;
2. Navigate to **Prompts**.&#x20;
3. In **Tools**, click the **+** button.
4. Select **MCP Server**.&#x20;
5. In the dialog, click **Add new** to display the form below.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FmBUZGbPtiMSyuIO8X13z%2Fopenai%20mcp%20server.png?alt=media&#x26;token=cda2743b-a3d7-4cf0-9171-b331c049878f" alt="" width="376"><figcaption></figcaption></figure>

6. In **URL**, add the following URL:

```
https://<MAKE_ZONE>/mcp/stateless
```

{% hint style="success" %}
If you experience connection issues, you can add  `/stream`  instead of `/stateless` to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

7. Replace `<MAKE_ZONE>` with your actual values.

* `MAKE_ZONE` - The zone your organization is hosted in (e.g., `eu2.make.com`).

8. In **Label**, name your Make MCP server.
9. In **Authentication**, select **Access token / API key**. &#x20;
10. Add your MCP token to the field that requires an access token.&#x20;
11. Click **Connect**.&#x20;

You have now connected Make MCP server to OpenAI.&#x20;
