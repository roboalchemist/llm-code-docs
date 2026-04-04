# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-chatgpt.md

# Source: https://developers.make.com/mcp-server/connect-using-oauth/usage-with-chatgpt.md

# Usage with ChatGPT

This guide outlines how to connect Make MCP server with ChatGPT using OAuth. &#x20;

**Prerequisites**

* ChatGPT account (paid subscription)

### Installation

To connect Make MCP server to ChatGPT:

1. Open the web version of ChatGPT.
2. Click on your profile name on the left sidebar.

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2Fz2kvotmKJc1ivVck4RgO%2Fchatgpt%20settings.png?alt=media&#x26;token=3182ef49-89a2-401d-93d3-b8c6cc275087" alt="" width="375"><figcaption></figcaption></figure>

3. Click **Settings** to open the settings dialog.&#x20;
4. Navigate to the **Connectors** section, then to **Advanced settings**.

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FB6YOWcXXBaEJdkA1NmDr%2Fchatgpt%20connectors.png?alt=media&#x26;token=cc47d0c8-8b6c-4352-a4f3-77cae102430d" alt="" width="375"><figcaption></figcaption></figure>

5. In **Advanced settings**, enable **Developer mode**.
6. Return to **Connectors**, and click the **Create** button that is now visible.
7. In the **New Connector** dialog, name your MCP server.&#x20;
8. In the **MCP Server URL** field, add the following URL:

```
https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add `/stateless` or  `/stream`  to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

9. In the **Authentication** dropdown, select **OAuth**.
10. Select the **I trust this application** checkbo&#x78;**.**&#x20;
11. Click the **Create** button.
12. In the OAuth consent screen, select your organization and its granted scopes.&#x20;
13. Click **Allow**.&#x20;

You have now connected Make MCP server to ChatGPT. In **Connectors**, you can click on it to expand its details and select which tools ChatGPT can use.&#x20;

### Enable in chat

After adding Make MCP server, you can enable it in the chat:

1. Open a new chat in ChatGPT.&#x20;
2. In the left-hand corner of the message bar, click the + sign to open a dropdown.&#x20;
3. Click **More**, then **Developer Mode**.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2F2Hgj5LTgn9hK547tfbZv%2Fchatgpt%20more.png?alt=media&#x26;token=82567a6a-c261-4eb7-82c6-c44f7c6c0665" alt="" width="263"><figcaption></figcaption></figure>

4. Click **Add sources**.
5. Enable Make MCP server.&#x20;

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FysKzNtiRDM60xXZRu3NT%2Fchatgpt%20enable%20in%20chat.png?alt=media&#x26;token=9a6c47d2-a47a-4884-98ad-001737e130fe" alt=""><figcaption></figcaption></figure>

You have now enabled Make MCP server in the chat, allowing ChatGPT to use Make tools when interacting with you.&#x20;
