# Source: https://docs.anyscale.com/mcp/convert-stdio-to-http.md

# Convert stdio MCP servers to HTTP with Ray Serve

[View Markdown](/mcp/convert-stdio-to-http.md)

# Convert stdio MCP servers to HTTP with Ray Serve

This page explains how to convert existing stdio-based Model Context Protocol (MCP) servers into scalable stdio-proxied HTTP MCP services on Anyscale using Ray Serve. You learn when to use this approach, how the architecture works, and best practices for production deployment.

For native streamable HTTP MCP service implementations and advanced concepts, see [Deploy scalable MCP servers with Ray Serve](/mcp/scalable-remote-mcp-deployment.md).

## Why create a stdio-proxied service?[​](#why-convert "Direct link to Why create a stdio-proxied service?")

This approach is useful when you need to deploy existing stdio-based MCP Docker images where you can't modify the source code. Ray Serve lets you run these images as HTTP MCP services without changing their implementation.

Additionally, a stdio-proxied HTTP MCP service exposes simple HTTP endpoints—GET `/tools` and POST `/call`—that make it easier to integrate with your agent applications.

However, Anyscale recommends using native streamable HTTP MCP service implementations for better performance and capabilities. See [Deploy scalable MCP servers with Ray Serve](/mcp/scalable-remote-mcp-deployment.md) for the recommended approach.

## Choose the right deployment approach[​](#approach-choice "Direct link to Choose the right deployment approach")

Deploy a **native streamable HTTP MCP service** on Ray Serve when the following apply:

* You build custom MCP servers from scratch.
* You use GPUs with deep learning models or run compute-heavy tool workloads.
* You integrate with Cursor or Claude apps over remote MCP servers.
* You want the best performance and streaming capabilities.

Deploy a **stdio-proxied HTTP MCP service** when the following apply:

* You need quick deployment for an existing stdio MCP Docker image.
* You can't modify the MCP server source code.
* Your MCP tools are CPU-bound or use small models.
* You prefer simple HTTP endpoints (GET `/tools` and POST `/call`) for tool discovery and invocation.
* You accept a small performance overhead from the container runtime.

For native implementations, see [Deploy scalable MCP servers with Ray Serve](/mcp/scalable-remote-mcp-deployment.md).

## Get started[​](#get-started "Direct link to Get started")

To create a stdio-proxied HTTP MCP service with Ray Serve on Anyscale, use the MCP template notebook. See [Anyscale MCP template](https://console.anyscale.com/template-preview/mcp-ray-serve).

## Architecture[​](#architecture "Direct link to Architecture")

Ray Serve hosts an HTTP application that proxies requests to a stdio MCP server running inside a container runtime on each replica. The application exposes endpoints to list available tools and invokes them with JSON payloads. Ray Serve manages replica processes and forwards requests to healthy instances.

![Architecture diagram showing Ray Serve hosting an HTTP application that proxies to stdio MCP servers in containers](https://agent-and-mcp.s3.us-east-2.amazonaws.com/mcp/diagrams/single_mcp_docker_ray_serve.png)

Key components:

* **Ingress**: FastAPI application mounted as Ray Serve ingress that exposes HTTP endpoints.
* **Stdio bridging**: Each replica runs a stdio MCP server in a container runtime and connects through stdin and stdout.
* **Tooling surface**: Endpoints for tool discovery and tool execution.

This design lets you operate prebuilt MCP servers as managed HTTP services without modifying the server code.

## Deploy multiple MCP services[​](#multiple-services "Direct link to Deploy multiple MCP services")

You can deploy multiple MCP services together using Ray Serve. For example, deploy Brave Search and Fetch services together.

See [Deploying multiple MCP services with Ray Serve](https://console.anyscale.com/template-preview/mcp-ray-serve?file=%252Ffiles%252F04%2520Deploy_multiple_mcp_stdio_docker_images_with_ray_serve.ipynb) for examples on how to add more MCP services and bind them in the router. This pattern provides a clean, extensible path to production deployment.
