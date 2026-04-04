Source: https://docs.slack.dev/changelog/2026/02/17/slack-mcp

# Announcing the Slack MCP server and Real-time Search API

February 17, 2026

We're excited to announce the release of not one, but _two_, major components designed to significantly enhance how Large Language Models (LLMs) and AI agents interact with your workspace data: the Slack Model Context Protocol (MCP) server and the Real-time Search (RTS) API!

## Slack MCP Server {#slack-mcp-server}

The MCP server enables AI agents to interact with Slack content through tools designed for LLM-driven discovery, configuration, and execution. Unlike APIs, the MCP server is built specifically for LLM consumption with robust descriptions and examples that return natural language responses. Refer to our documentation to learn more about the [Slack MCP server](/ai/slack-mcp-server).

## Real-time Search API {#real-time-search-api}

The Data Access API has evolved into the [Real-time Search API](/apis/web-api/real-time-search-api)! This API allows users to access Slack data through a secure search interface, enabling third-party applications to retrieve relevant Slack data without storing customer information on external servers. Get started using the Real-time Search API with [this guide](/apis/web-api/real-time-search-api) or get straight to business with the [method reference](/reference/methods/assistant.search.context).

### Scope updates to assistant.search.context {#scope-updates-to-assistantsearchcontext}

Along with these changes, the [`assistant.search.context`](/reference/methods/assistant.search.context) API method has undergone a scope change. The `assistant.search.context` API method moved away from the single `search:read` scope to a set of granular `search:read.*` scopes:

* [`search:read.public`](/reference/scopes/search.read.public) (required) - for public channel access
* [`search:read.private`](/reference/scopes/search.read.private) - for private channels (with user consent)
* [`search:read.im`](/reference/scopes/search.read.im) - for direct messages (with user consent)
* [`search:read.mpim`](/reference/scopes/search.read.mpim) - for multi-party direct messages (with user consent)

This change allows for more granular control over what data AI-enabled apps can access.

**Tags:**

* [Announcement](/changelog/tags/announcement)
* [New Feature](/changelog/tags/new-feature)
