# Source: https://docs.intelligems.io/developer-resources/mcp-server/google-gemini.md

# Google Gemini

{% hint style="warning" %}
Custom Connectors require a Google Gemini Enterprise plan.&#x20;
{% endhint %}

Add the Intelligems MCP Server using the Gemini CLI:

```bash
# Add with HTTP transport (recommended)
gemini mcp add --transport http intelligems https://ai.intelligems.io/mcp

# Or with SSE transport
gemini mcp add --transport sse intelligems https://ai.intelligems.io/mcp/sse
```

Alternatively, add the server to your `~/.gemini/settings.json` (user-wide) or `.gemini/settings.json` (project-level):

```json
{
  "mcpServers": {
    "intelligems": {
      "httpUrl": "https://ai.intelligems.io/mcp"
    }
  }
}
```

**Management commands:**

```bash
gemini mcp list           # View all configured servers
gemini mcp remove intelligems # Remove the server
```
