# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/mcp/airbyte-mcp-server.md

# Module airbyte.mcp.server

Copy Page

Experimental MCP (Model Context Protocol) server for PyAirbyte connector management.

## Variables[​](#variables "Direct link to Variables")

`app` : The Airbyte MCP Server application instance.

## Functions[​](#functions "Direct link to Functions")

`main() ‑> None` : @private Main entry point for the MCP server.

This function starts the FastMCP server to handle MCP requests.

It should not be called directly; instead, consult the MCP client documentation for instructions on how to connect to the server.
