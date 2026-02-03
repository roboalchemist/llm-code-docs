# Source: https://docs.intelligems.io/developer-resources/mcp-server/claude.md

# Claude

{% hint style="warning" %}
Custom Connectors require a Claude Pro, Max, Team or Enterprise plan.
{% endhint %}

The Intelligems MCP can be integrated with both Claude Desktop and Claude Code. Please see the applicable instructions below:&#x20;

## **Claude Desktop**

### **Install**

1. Open the [Claude Desktop](https://docs.intelligems.io/developer-resources/mcp-server/claude#claude-desktop) app.
2. Click your profile name in the sidebar and select Settings.
3. Go to the Connectors tab.
4. Select "Add custom connector"
5. Title it "Intelligems" and add a URL of [`https://ai.intelligems.io/mcp`](https://ai.intelligems.io/mcp).Then press Add

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FogGn1wX0SbQNreF8kW4I%2Fimage.png?alt=media&#x26;token=278c595d-4a9c-444f-88d5-17acf3fa8af2" alt=""><figcaption></figcaption></figure>

6. When starting a new chat, confirm that Intelligems is toggled on in the options menu, pictured below

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FAahsgcmuga8zFL7TkNcL%2FScreenshot%202025-12-04%20at%2010.06.44%E2%80%AFAM.png?alt=media&#x26;token=7cdada8b-3f48-459f-b443-bb50ccdc7e0b" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
In order to avoid hitting "Allow" every time Claude pulls information from Intelligems, go to Settings > Connectors > Configure next to Intelligems > switch the dropdown next to "Read-only tools" to "Always allow".&#x20;
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FberqwoQwIGOrS6OU0HCe%2FScreenshot%202025-12-04%20at%2010.05.22%E2%80%AFAM.png?alt=media&#x26;token=3a79d7ff-452f-41fb-8e69-5b16608c59f4" alt=""><figcaption></figcaption></figure>

## **Claude Code**

Add the Intelligems MCP Server using the CLI:

```bash
# Add with HTTP transport (recommended)
claude mcp add --transport http intelligems https://ai.intelligems.io/mcp

# Or with SSE transport
claude mcp add --transport sse intelligems https://ai.intelligems.io/mcp/sse
```

When you first use the server, Claude Code will trigger a browser-based OAuth login. Complete the authentication flow to authorize access to your Intelligems account. Tokens are stored securely and refresh automatically.

Alternatively, you can add the server to your `.mcp.json` configuration file in your project root or `~/.claude.json` for user-wide access:

```json
{
  "mcpServers": {
    "intelligems": {
      "type": "http",
      "url": "https://ai.intelligems.io/mcp"
    }
  }
}
```

**Management commands:**

```bash
claude mcp list           # View all configured servers
claude mcp get intelligems # Get server details
claude mcp remove intelligems # Remove the server
```
