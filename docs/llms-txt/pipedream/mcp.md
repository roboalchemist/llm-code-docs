# Source: https://pipedream.com/docs/connect/mcp.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Servers

> Use Pipedream MCP with popular AI frameworks and LLMs to add 10,000+ tools to your AI application.

export const PUBLIC_APPS = '3,000';

Pipedream offers a dedicated MCP ([Model Context Protocol](https://modelcontextprotocol.io/)) server for all of our {PUBLIC_APPS}+ integrated apps. This server enables AI assistants like Claude or ChatGPT to securely access and interact with thousands of APIs through a standardized communication protocol, performing real-world tasks using your or your users’ accounts.

Pipedream’s MCP server is powered by [Pipedream Connect](https://pipedream.com/connect) and includes:

* Access to {PUBLIC_APPS}+ apps and APIs through a consistent interface
* Over 10,000 pre-built tools
* Fully-managed OAuth and secure credential storage

<Note>
  User credentials are encrypted at rest and all requests are made through Pipedream’s servers, never directly exposing credentials to AI models. Read more about how we protect user credentials [here](/privacy-and-security/#third-party-oauth-grants-api-keys-and-environment-variables).
</Note>

## Available integrations and tools

Pipedream provides MCP servers for all our [supported apps](https://mcp.pipedream.com/). Each app has its own dedicated MCP server with tools specific to that API. For example:

* **[Slack](https://mcp.pipedream.com/app/slack)**: Send messages, manage channels, create reminders, and more
* **[GitHub](https://mcp.pipedream.com/app/github)**: Create issues, manage pull requests, search repositories
* **[Google Sheets](https://mcp.pipedream.com/app/google-sheets)**: Read and write data, format cells, create charts

Explore the full list of available MCP servers at [mcp.pipedream.com](https://mcp.pipedream.com) and learn more about [app discovery](/connect/app-discovery).

## Getting started

You can use Pipedream's MCP servers in two ways:

1. **[As a developer](/connect/mcp/developers/)**: Host your own MCP servers for your application or organization
2. **[As an end user](/connect/mcp/users/)**: Connect your accounts through our hosted MCP servers at [mcp.pipedream.com](https://mcp.pipedream.com)

<Note>
  **Try out Pipedream MCP in our chat app at [chat.pipedream.com](https://chat.pipedream.com)** and explore the code [here](https://github.com/PipedreamHQ/mcp-chat).
</Note>

## Security

Like the rest of Pipedream Connect, MCP servers follow strict security best practices:

* **Credential isolation**: Each user’s credentials are stored securely and isolated from other users
* **No credential exposure**: Credentials are never exposed to AI models or your client-side code
* **Revocable access**: Users can revoke access to their connected accounts at any time

For more information on security, see our [security documentation](/privacy-and-security/).

## Use cases

Pipedream MCP enables AI assistants to perform a wide range of tasks:

* **Productivity automation**: Schedule meetings, send emails, create documents
* **Data analysis**: Query databases, analyze spreadsheets, generate reports
* **Content creation**: Post social media updates, create marketing materials
* **Customer support**: Respond to inquiries, create tickets, update CRM records
* **Developer workflows**: Create issues, review code, deploy applications

## Supported tools

* Each MCP server provides tools specific to that app. Tools are automatically created based on Pipedream’s [registry of pre-built actions](https://github.com/PipedreamHQ/pipedream/tree/master/components)
* You can find the supported tools for a given app on its MCP server page or search for specific actions here: [pipedream.com/explore](https://pipedream.com/explore#popular-actions)

## Pricing

* Anyone can use Pipedream’s hosted MCP servers for their own use **for free**
* To use Pipedream MCP in your own app or agent to make tool calls on behalf of your users, you can get started for free in development mode
* [Visit the pricing page](https://pipedream.com/pricing?plan=Connect) when you’re ready to ship to production

## Additional resources

* [Pipedream hosted MCP servers](https://mcp.pipedream.com)
* [MCP official spec](https://modelcontextprotocol.io/)
* [MCP inspector tool](https://modelcontextprotocol.io/tools/inspector/)

Built with [Mintlify](https://mintlify.com).
