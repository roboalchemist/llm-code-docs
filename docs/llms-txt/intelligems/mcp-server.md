# Source: https://docs.intelligems.io/developer-resources/mcp-server.md

# MCP Server

The Intelligems MCP (Model Context Protocol) Server provides AI assistants like Claude, ChatGPT, and Gemini with secure, authenticated access to your Intelligems data and Shopify store information through a standardized protocol.

## What is MCP?

The Model Context Protocol (MCP) is an open standard created by Anthropic that allows AI assistants to securely connect to external data sources and tools. The Intelligems MCP Server implements this protocol to give AI assistants controlled access to:

* Your Intelligems experiments and experiences
* Organization configuration
* Shopify store catalog, collections, and pages
* Analytics and audience data
* Custom events and integrations

## Prerequisites

* An active Intelligems account
* A Shopify store connected to Intelligems
* An MCP-compatible AI client (e.g., Claude Desktop, ChatGPT, Gemini, etc.)

## Installation

The Intelligems MCP Server is hosted at: `https://ai.intelligems.io`

No installation is required - the server is hosted by Intelligems and ready to use.

## Configuration

Add the Intelligems MCP Server to your AI client's configuration following the applicable guide linked below:

1. [Claude (Desktop & Code)](https://docs.intelligems.io/developer-resources/mcp-server/claude)
2. [ChatGPT](https://docs.intelligems.io/developer-resources/mcp-server/chatgpt)
3. [Google Gemini](https://docs.intelligems.io/developer-resources/mcp-server/google-gemini)

#### **Other MCP Clients:**

Refer to your client's documentation for adding OAuth2-authenticated SSE-based or http MCP servers.

* HTTP: `https://ai.intelligems.io/mcp` (recommended)
* SSE: `https://ai.intelligems.io/mcp/sse`

## Multi-Organization Support

If you have access to multiple Intelligems organizations, you can specify which one to use:

* During initial authentication, choose any organization installed on Intelligems. This is only used for authentication.
* Most tools accept an optional `organization` parameter to override the default
* Use the `getOrganizationsList` tool to see all organizations you have access to
* If you would like to always use a specific organization, add a System Prompt or Custom Instruction to your LLM with these details.
