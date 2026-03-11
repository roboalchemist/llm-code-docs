# Source: https://docs.anyscale.com/mcp/mcp-quickstart-guide.md

# MCP quickstart

[View Markdown](/mcp/mcp-quickstart-guide.md)

# MCP quickstart

This guide helps you set up your first Model Context Protocol (MCP) server and client. You learn how to deploy MCP servers locally for development and on Anyscale for scalable production deployments.

## Deploy scalable MCP servers on Anyscale[​](#deploy-on-anyscale "Direct link to Deploy scalable MCP servers on Anyscale")

For production deployments that require high availability and scalability, use the Anyscale MCP template.

### Use the Anyscale template[​](#anyscale-template "Direct link to Use the Anyscale template")

To deploy MCP servers on Anyscale, follow these steps:

1. Open the [Anyscale MCP template](https://console.anyscale.com/template-preview/mcp-ray-serve).
2. Click **Launch** to deploy the example.
3. Follow the template instructions to customize the deployment for your use case.

The MCP template provides four end-to-end examples for deploying and scaling MCP servers using Ray Serve and Anyscale services. These examples cover both streamable HTTP and stdio transport types:

1. **Deploy a custom MCP in streamable HTTP**: Deploys a custom weather MCP server in streamable HTTP mode behind FastAPI and Ray Serve. This example demonstrates autoscaling, load balancing, and end-to-end testing on Anyscale.

2. **Build an MCP gateway with existing Ray Serve apps**: Sets up a single MCP gateway that multiplexes requests to multiple pre-existing Ray Serve apps under one unified `/mcp` endpoint. This approach requires no code changes in the underlying services.

3. **Deploy a single MCP stdio Docker image as an HTTP service**: Wraps a stdio-only MCP Docker image (such as Brave Search) with Ray Serve to expose `/tools` and `/call` HTTP endpoints. This pattern enables horizontal scaling without rebuilding the image.

4. **Deploy multiple MCP stdio Docker images as HTTP services**: Extends the single Docker image pattern to run several stdio-based MCP images side by side.

## Local MCP deployment tutorial[​](#local-deployment "Direct link to Local MCP deployment tutorial")

Create and run MCP servers locally using hands-on examples. The tutorial demonstrates MCP with different transport modes (stdio, SSE, and streamable HTTP) using a simple calculator server example.

Follow the complete tutorial in the GitHub repository:

**[github.com/anyscale/mcp-quickstart](https://github.com/anyscale/mcp-quickstart)**

The repository includes:

* Complete working examples for all transport modes.
* Integration guides for Claude Desktop and Cursor.
* Docker deployment configurations.
* Step-by-step instructions with code.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

### Anyscale MCP webinars[​](#webinars "Direct link to Anyscale MCP webinars")

* [Unlocking Agentic AI with MCP](https://www.youtube.com/watch?v=R2vqlGJ5Wes): Webinar covering the basics of MCP.
* [Agentic AI in Practice: Build Scalable and Production Ready MCP Servers](https://www.youtube.com/watch?v=RB8k69RLY9M): Webinar covering scalable deployment of MCP with Ray Serve and Anyscale services.

### MCP documentation and tools[​](#mcp-docs "Direct link to MCP documentation and tools")

* [MCP introduction](https://modelcontextprotocol.io/introduction): Official introduction to the Model Context Protocol.
* [MCP documentation](https://docs.anthropic.com/en/docs/mcp): Anthropic's comprehensive MCP documentation.
* [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk): Official Python SDK for building MCP servers and clients.
* [MCP Inspector](https://github.com/modelcontextprotocol/inspector): Tool for debugging and testing MCP servers.

### MCP server collections[​](#server-collections "Direct link to MCP server collections")

* [Official MCP servers list](https://github.com/modelcontextprotocol/servers): Anthropic's curated list of MCP server implementations.
* [Docker MCP images](https://hub.docker.com/catalogs/mcp): Pre-built Docker images for MCP servers.
* [Awesome MCP servers](https://mcpservers.org/): Community-maintained directory of MCP servers.
