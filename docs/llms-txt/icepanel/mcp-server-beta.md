# Source: https://docs.icepanel.io/experiments/mcp-server-beta.md

# MCP server (beta)

IcePanel contains a rich amount of data about your software architecture — everything from systems, apps, stores, components, relationships, and the details about them. As your model grows, making sense of your architecture gets harder.

Connect your data in IcePanel with your LLM of choice and ask it questions to quickly get answers about your software architecture.

## What is MCP?

The Model Context Protocol (MCP) is a standard for applications to communicate with LLMs. Anthropic created MCP in November 2024, and it has quickly gained widespread adoption. Think of it as a layer between your app and LLMs, a ["USB-C port for AI applications"](https://docs.anthropic.com/en/docs/agents-and-tools/mcp).

MCP is an open protocol supported by most apps like Cursor, Claude and CoPilot. ChatGPT plans on releasing an integration [soon](https://x.com/OpenAIDevs/status/1904957755829481737). IcePanel's MCP integration will work with any app that supports [tools](https://modelcontextprotocol.io/docs/concepts/tools).

### How it works

After configuring your AI client with IcePanel, you'll be able to ask it things like:

* What are my landscapes?
* Details about any model objects — "What does IcePanel do?"
* Object relationships — "What is this API service connected to?"
* Technology information — "What are the most commonly used tech in my system?"
* Team ownership — "What does *team X* own?"

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FKk48EE7KUvNtyp86wCfR%2Fmcp-server.gif?alt=media&#x26;token=55991e3c-c7bb-47b4-b3e3-60d379183ac9" alt=""><figcaption><p>MCP with Claude</p></figcaption></figure>

## Setup

### Prerequisites

* Node.js (Latest LTS version recommended)
* One of the supported MCP Clients:
  * Claude Desktop
  * Cursor
  * Windsurf

### Installation

1. **Get your organization's ID**
   * Visit [IcePanel](https://app.icepanel.io/)
   * Click on your landscape in the top left to open the dropdown
   * Beside your org name, click the gear icon
   * Keep your "Organization Identifier" handy!
2. **Generate API Key**
   * Visit [IcePanel](https://app.icepanel.io/)
   * Click on your landscape in the top left to open the dropdown
   * Beside your org name, click the gear icon
   * Click on the 🔑 API keys link in the sidebar
   * Generate a new API key
   * Read permissions recommended
3. **Install**
   * <https://github.com/IcePanel/mcp-server>

## Environment Variables

* `API_KEY`: Your IcePanel API key (required)
* `ORGANIZATION_ID`: Your IcePanel organization ID (required)
* `ICEPANEL_API_BASE_URL`: (Optional) Override the API base URL for different environments

## Configure your MCP Client

Add this to your MCP Clients' MCP config file:

```json
{
  "mcpServers": {
    "@icepanel/icepanel": {
      "command": "npx",
      "args": ["-y", "@icepanel/mcp-server@latest", "API_KEY=\"your-api-key\"", "ORGANIZATION_ID=\"your-org-id\""]
    }
  }
}
```

### ✉️ Support

* Reach out to [Support](mailto:support@icepanel.io) if you experience any issues.

### 📝 License

MIT License

### 🙏 Acknowledgments

* Thanks to our beta testers and community members
