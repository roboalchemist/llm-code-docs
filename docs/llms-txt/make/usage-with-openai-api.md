# Source: https://developers.make.com/mcp-server/connect-using-mcp-token/usage-with-openai-api.md

# Usage with OpenAI API

This guide outlines how to connect Make MCP server with the OpenAI API.&#x20;

**Prerequisites**

* [MCP token](https://developers.make.com/mcp-server/connect-using-mcp-token)

### Installation

To add Make MCP server through the OpenAI API:

1. Configure your API call with the following:

```sh
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "input": "List all available tools.",
  "tools": [
    {
      "type": "mcp",
      "server_label": "make",
      "server_url": "https://<MAKE_ZONE>/mcp/stateless",
      }
    ]
  }'
```

{% hint style="success" %}
If you experience connection issues, you can add  `/stream`  instead of `/stateless` to the end of your connection URL. For SSE, add  `/sse`  instead.&#x20;
{% endhint %}

2. Replace `<MAKE_ZONE>`  with your actual values.

* `MAKE_ZONE` - The zone your organization is hosted in (e.g., `eu2.make.com`).

You have now added Make MCP server through the OpenAI API.&#x20;
