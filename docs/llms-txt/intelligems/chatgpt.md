# Source: https://docs.intelligems.io/developer-resources/mcp-server/chatgpt.md

# ChatGPT

{% hint style="warning" %}
Custom Connectors require a ChatGPT Plus, Team, or Enterprise plan.
{% endhint %}

ChatGPT supports MCP servers through Developer Mode. To add the Intelligems MCP Server:

1. Open ChatGPT in your web browser
2. Click your profile name in the sidebar and select Settings
3. Navigate to Apps & Connectors > Advanced settings
4. Enable Developer mode
5. Return to Apps & Connectors and click Create
6. Configure the connector:
   * **Name:** Intelligems
   * **MCP Server URL:** `https://ai.intelligems.io/mcp`
   * **Authentication:** Select OAuth
   * Check "I understand and want to continue"
7. Click Create and complete the OAuth authorization flow

**To use in a chat:**

1. Open a new chat
2. Click the + icon in the message bar
3. Select More > Developer Mode
4. Choose Add sources and enable the Intelligems MCP server
