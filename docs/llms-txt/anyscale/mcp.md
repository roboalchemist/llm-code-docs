# Source: https://docs.anyscale.com/mcp.md

# Basics of MCP

[View Markdown](/mcp.md)

# Basics of MCP

This page introduces the Model Context Protocol (MCP) and explains how it enables AI applications to connect securely to data sources and tools.

## What is MCP?[​](#what-is-mcp "Direct link to What is MCP?")

**Model Context Protocol (MCP)** is an open standard that enables AI applications to connect external systems such as data sources, APIs and tools. See the [MCP documentation](https://modelcontextprotocol.io/docs/getting-started/intro).

Without a standard protocol like MCP, you must write custom integration code for every tool or API an AI agent needs to use. This code often isn't reusable, and adding or switching tools requires significant effort. For example, switching from Google Search to Bing requires rewriting the integration code.

MCP solves this by serving as a universal bridge between AI applications and external systems, allowing models to:

* Access up-to-date data from various sources or APIs.
* Execute tools and functions with a consistent protocol.
* Swap or add new tools and leverage a community-built ecosystem.

## Local and remote MCP servers[​](#local-remote-servers "Direct link to Local and remote MCP servers")

*Local MCP servers* run on your machine and connect to clients through the stdio transport. Use local servers to access local files and developer tools without exposing services to the network. In MCP-compatible applications such as Claude Desktop or Cursor, you add servers locally and the client requests your permission before executing each tool call. Local servers don't require inbound ports or cloud hosting.

*Remote MCP servers* run on the internet and connect to clients through streamable HTTP transport mechanism. Remote servers expose tools, prompts, and resources that multiple MCP hosts or applications can access. These servers typically require authentication. You configure clients with the server URL and authentication credentials. Use remote servers for shared resources and production deployments instead of single-user development.

## Scalable deployment of remote MCPs with Ray Serve and Anyscale services[​](#scalable-deployment "Direct link to Scalable deployment of remote MCPs with Ray Serve and Anyscale services")

MCP deployments range from do-it-yourself clusters to managed services. Running MCP on Kubernetes requires managing YAML configurations, ingress exposure, autoscaling policies, monitoring, metrics, and Role-Based Access Control (RBAC).

Ray Serve streamlines deployment with built-in autoscaling, fault tolerance, and Ray dashboards for observability.

Anyscale services add production-ready capabilities including zone-aware scheduling, high-availability (HA) head nodes, and comprehensive observability through enhanced dashboards, distributed tracing, and centralized log aggregation. Anyscale services also provide built-in authentication, integration with your cloud's secret manager, and native multi-application orchestration. These features make Anyscale services the recommended path for scalable, production-ready MCP deployment.

To deploy MCP with Ray Serve on Anyscale, see [Deploy scalable MCP servers with Ray Serve](/mcp/scalable-remote-mcp-deployment.md).

## Key participants of MCP[​](#key-participants "Direct link to Key participants of MCP")

The MCP architecture consists of three core participants: hosts, clients, and servers.

### MCP hosts[​](#mcp-hosts "Direct link to MCP hosts")

*MCP hosts* are the applications that you interact with, such as an AI agent or a desktop application such as Claude Desktop. The host contains the core logic and determines when to use an MCP tool or resource.

### MCP servers[​](#mcp-servers "Direct link to MCP servers")

*MCP servers* are lightweight, specialized applications that expose data sources and tools to an MCP client. Each server wraps a specific resource, such as a database, API such as Google Search, or a set of functions.

An MCP server contains:

* **Tools (mostly used)**: Functions that the MCP host (such as an AI agent) can call to perform specific actions. A tool definition includes its `name`, a human-readable `description` from the docstring, and an `inputSchema` that defines the expected arguments using JSON schema.
* **Resources**: Data from files, APIs, or databases that the MCP host can read to understand context. Resources are similar to a `GET` endpoint in a REST API and provide data without performing significant computation.
* **Prompts**: Predefined prompt templates stored on the server that the MCP host can retrieve and use.

See the [server concepts documentation](https://modelcontextprotocol.io/docs/learn/server-concepts).

### MCP clients[​](#mcp-clients "Direct link to MCP clients")

*MCP clients* act as a bridge, connecting an MCP host to one or more MCP servers. The client discovers what capabilities a server offers and handles the communication for tool execution. Its primary functions are:

* **Discover available tools**: The client queries connected servers using `list_tools()` to discover available tools and understand their capabilities.
* **Handle tool execution**: When the host decides to use a tool, the client executes it with the required arguments through `call_tool(tool_name, tool_params)` and passes the results back.

See the [client concepts documentation](https://modelcontextprotocol.io/docs/learn/client-concepts).

## Transport mechanisms[​](#transport-mechanisms "Direct link to Transport mechanisms")

MCP supports multiple transport mechanisms for different use cases:

* **[stdio](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio)**: Used for local development. The client launches the MCP server as a subprocess, creating a direct one-to-one coupling. Communication occurs over standard input (`stdin`) and standard output (`stdout`). When the client exits, the server subprocess terminates automatically.
* **[Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http)**: The modern standard for network-based communication in distributed deployments. It uses a single `/mcp` endpoint, supports bidirectional communication, and enables stateless server designs, which improves scalability and reliability.
* **HTTP with Server-Sent Events (SSE) (legacy)**: This mechanism has been deprecated in favor of streamable HTTP.

## Use the MCP inspector[​](#mcp-inspector "Direct link to Use the MCP inspector")

The MCP inspector is a developer tool for testing and debugging MCP servers. Use it to validate server tools, resources, and prompts during development. See the [MCP inspector repository](https://github.com/modelcontextprotocol/inspector).

note

Use version 0.12.0 or later to support Streamable HTTP mode.

To launch the MCP inspector, run:

```
npx -y @modelcontextprotocol/inspector
```

If the inspector starts successfully, you see output similar to the following:

```
🔍 MCP Inspector is up and running at http://127.0.0.1:6274
```

## Next steps[​](#next-steps "Direct link to Next steps")

* For a hands-on introduction and overview of the resources on MCP, see [MCP quickstart](/mcp/mcp-quickstart-guide.md).
* To learn about deploying MCP with Ray Serve and Anyscale services, or integrating MCP with multiple existing Ray Serve applications using MCP gateway, see [Deploy scalable MCP servers with Ray Serve](/mcp/scalable-remote-mcp-deployment.md).
* To convert stdio-based MCP servers to HTTP services, see [Convert stdio MCP servers to HTTP with Ray Serve](/mcp/convert-stdio-to-http.md).
