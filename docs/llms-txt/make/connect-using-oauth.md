# Source: https://developers.make.com/mcp-server/connect-using-oauth.md

# Connect using OAuth

You can connect Make MCP server to MCP clients using OAuth.&#x20;

OAuth is recommended due to its simple and secure setup, with a universal URL that eliminates the need to configure the URL with an MCP token.&#x20;

### Connection URL

To connect Make MCP server using OAuth, use this URL for Stateless HTTP Streamable:

```json
https://mcp.make.com
```

{% hint style="success" %}
If you experience connection issues, you can add  `/stateless` or  `/stream`  to the end of the URL. If your client only supports SSE, add  `/sse` instead.&#x20;
{% endhint %}

### Access control

While connecting Make MCP server with an MCP client, you will select the organization and granted scopes in the OAuth consent screen. Scopes determine the tools available to the MCP client.&#x20;

Consent screen example:

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FuVHgjJgl2C4fAEPim28w%2Fimage.png?alt=media&#x26;token=31a8d0e0-0213-4e61-934e-c8bc754a018d" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
The `Run your scenarios` scope provides access to all **on-demand** and **active** scenarios within a specific organization.&#x20;

For more granular control, a [Teams plan](https://www.make.com/en/pricing) or higher allows you to limit scenario access to specific teams in your organization, as you can create user accounts that have access only to particular teams.
{% endhint %}

To complete the connection, refer to the Usage page of your MCP client (e.g., Usage with Cursor).
