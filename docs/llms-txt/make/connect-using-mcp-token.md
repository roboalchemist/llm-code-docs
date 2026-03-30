# Source: https://developers.make.com/mcp-server/connect-using-mcp-token.md

# Connect using MCP token

You can connect Make MCP server to a client using an MCP token in the connection URL. An MCP token is an API token that you create in Make for adding Make MCP server to an MCP client.&#x20;

### Obtain MCP token&#x20;

To obtain an MCP token:

1. In the top-right corner of your Make account, click your name.
2. Click **Profile**.&#x20;
3. Navigate to the **API access** tab.&#x20;
4. In **Tokens**, click **Add token**, which opens a dialog.

<figure><img src="https://3035801395-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyHSLDvK9bMDQI1lCXXt6%2Fuploads%2FBPDdl6ZhvVRLXL0jKBid%2Fnew%20mcp%20token%20geeneration.png?alt=media&#x26;token=b5bf78ed-0659-40c7-8a4c-687eec0083c6" alt="" width="375"><figcaption></figcaption></figure>

5. Select your desired scopes, including the `mcp:use` scope if you want to make your scenarios available as tools.
6. In **Label**, name your API token.&#x20;
7. Click **Add**.

You have now generated an MCP token for your MCP client. Include this token in the connection URL. To complete the connection, refer to the Usage page of your MCP client (e.g., Usage with Cursor).

{% hint style="danger" %}
An MCP token is a secret key. Treat it as sensitive information and share it only with trusted parties.
{% endhint %}

### Access control&#x20;

To control which scenarios are available as tools through your MCP token, see [Scenarios as tools access control](https://developers.make.com/mcp-server/connect-using-mcp-token/scenarios-as-tools-access-control).&#x20;
