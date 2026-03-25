# Source: https://www.apollographql.com/docs/graphos/resources/use-docs-ai.md

# Use Apollo docs with AI

The development landscape is evolving, and AI-powered tools are becoming essential for augmenting workflows and enhancing developer productivity.

To help you build faster with Apollo, you can access Apollo documentation through AI assistants and code editors.

## Quick access in the documentation

While browsing through the documentation, you can ask a question about the page to start a conversation with ChatGPT or Claude. You can also find a contextual menu dropdown near the table of contents to copy the page content as Markdown.

![Context menu dropdown in the top right corner of a docs page and ask AI question box](/docs/_image/graphos/resources/use-docs-ai/aed13296bfd4?w=1200)

## Connect your AI agents to the MCP Server

Apollo provides an MCP server, called GraphOS MCP Tools, that gives your AI assistants access to Apollo's documentation as well as other graph-building capabilities.

This MCP server is hosted by Apollo and is available at `https://mcp.apollographql.com`.

To connect your AI agents to the MCP server, follow the instructions on the [GraphOS MCP Tools](https://www.apollographql.com/docs/graphos/platform/graphos-mcp-tools#connect-your-ai-agents-to-graphos-mcp-tools) page.

## Install Apollo GraphQL Skills for your AI agent

[Agent Skills](https://skills.sh/) are reusable capabilities for AI agents that provide specialized knowledge and best practices. The Apollo GraphQL Skills enhance your AI coding assistants with knowledge about Apollo Client, Apollo Server, Apollo Connectors, Rover CLI, GraphQL schema design, and more.

### Install Apollo GraphQL Skills

Install Apollo GraphQL Skills using the Skills CLI:

```bash
npx skills add apollographql/skills
```

The CLI guides you through an interactive installation:

1. **Select skills** - Choose which skills to install
2. **Select agents** - Pick target agents (Claude Code, Cursor, GitHub Copilot, etc.)
3. **Installation scope** - Project (committed with your code) or Global
4. **Installation method** - Symlink (recommended) or Copy

You can also install individual skills directly:

```bash
npx skills add apollographql/skills --skill apollo-client
```

### Available skills

Apollo GraphQL Skills include:

* **apollo-client** - Build React applications with Apollo Client 4.x for GraphQL data management, caching, and local state
* **apollo-server** - Build GraphQL servers with Apollo Server 4.x, including schemas, resolvers, authentication, and plugins
* **apollo-connectors** - Write Apollo Connectors schemas to integrate REST APIs into GraphQL
* **apollo-mcp-server** - Configure and use Apollo MCP Server to connect AI agents with GraphQL APIs
* **rover** - Manage GraphQL schemas and run local supergraph development with Apollo Rover CLI
* **graphql-schema** - Design GraphQL schemas following industry best practices for type design, naming, pagination, errors, and security
* **graphql-operations** - Write GraphQL operations (queries, mutations, fragments) following best practices for client-side development
* **rust-best-practices** - Write idiomatic Rust code following Apollo GraphQL's best practices handbook

### Usage

Skills activate automatically once installed. Your AI agent uses them when relevant tasks are detected. For example:

* "Set up Apollo Client in a React app" - Activates the `apollo-client` skill
* "Create an Apollo Server with user authentication" - Activates the `apollo-server` skill
* "Connect a REST API to a GraphQL schema" - Activates the `apollo-connectors` skill

For more information, see the [Apollo GraphQL Skills repository](https://github.com/apollographql/skills) on GitHub.
