# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-vapi.md

# Usage with Vapi

This guide outlines how to connect Make MCP server with Vapi. &#x20;

**Prerequisites**

* Vapi account
* [MCP token](https://developers.make.com/mcp-server/connect-using-mcp-token)

### Installation

To connect Make MCP server to Vapi:&#x20;

1. Open your Vapi account.&#x20;
2. Navigate to **Tools** on the left sidebar. &#x20;
3. Click the **Create Tool** button, then select **MCP**.&#x20;
4. Configure the tool name and describe when to use the tool.&#x20;
5. In **Server URL**, add the following URL:

```
https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/stateless
```

{% hint style="success" %}
If you experience connection issues, you can add  `/stream`  instead of `/stateless` to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

6. Replace `<MAKE_ZONE>` and `<MCP_TOKEN>` with your actual values.

* `MAKE_ZONE` - The zone your organization is hosted in (e.g., `eu2.make.com`).
* `MCP_TOKEN` - You can generate your MCP token in your Make profile.

Optionally, to control which scenarios are available as tools, you can further configure the URL according to the levels outlined in[ scenarios as tools access control](https://developers.make.com/mcp-server/connect-using-mcp-token/broken-reference).

7. In **Timeout**, enter an appropriate timeout for your use case.&#x20;
8. In **MCP Settings**, select **Streamable HTTP** or **Server-Sent Events (SSE).**
9. Click **Save**.&#x20;

You have now connected Make MCP server to Vapi.&#x20;

{% hint style="warning" %}
MCP Tool calls from Vapi Assistants may exceed Make API rate limits, resulting in rate limit errors. Check your Make API rate limit, as defined in your plan, in [Make API rate limits](https://developers.make.com/api-documentation/getting-started/rate-limiting).
{% endhint %}
