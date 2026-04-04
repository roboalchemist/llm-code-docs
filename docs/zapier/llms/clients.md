# Source: https://docs.zapier.com/mcp/clients.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

Zapier MCP integrates with a variety of Model Context Protocol (MCP) clients, allowing you to connect your AI workflows with different development environments and platforms.

## Supported Clients

Zapier MCP currently supports the following official MCP clients:

### AI Platforms & APIs

* **Anthropic API** - Direct integration with Anthropic's API
* **Claude** - Claude desktop application
* **Claude Code** - Claude's code-focused interface
* **OpenAI API** - Direct integration with OpenAI's API
* **ChatGPT** - Zapier MCP as a Custom Connector for use in [ChatGPT Developer Mode](https://platform.openai.com/docs/guides/developer-mode)
* **Microsoft Copilot Studio** - Create Microsoft Copilot Agents with Tools

### Development Environments

* **Cursor** - AI-powered code editor
* **VS Code** - Visual Studio Code with MCP extension
* **Windsurf** - Modern development environment

### Voice Assistants

* **ElevenLabs** - AI-powered voice assistant
* **Vapi** - Voice agents for developers

### Programming Languages

* **Python** - MCP client for Python applications
* **TypeScript** - MCP client for TypeScript/JavaScript applications

### Other Integrations

* **Other** - Additional community and third-party clients

## Request a New Client

Looking to get your MCP client featured as an official client compatible with Zapier MCP?

[Submit a Client Request →](https://mcp.zapier.app/client-request)

### Requirements for New Clients

To ensure compatibility with Zapier MCP, your client must:

* **Support streamable HTTP** - We no longer support SSE MCP servers

Not a requirement, but preferred:

* **Implement OAuth with Dynamic Client Registration** - As outlined in the [official MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization#authorization-flow)

These requirements ensure secure, scalable integration with Zapier's infrastructure while providing the best experience for users.

## Disconnecting OAuth-Connected Clients

If you need to revoke or sever the connection between Zapier MCP and an OAuth-connected client (such as Claude or Microsoft Copilot Studio), you can do so by deleting the server itself. This will immediately terminate the connection and prevent further access to your Zapier MCP account from that client.

You'll need to re-authenticate if you recreate the server.
