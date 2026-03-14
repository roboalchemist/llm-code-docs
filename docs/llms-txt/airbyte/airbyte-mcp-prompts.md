# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/mcp/airbyte-mcp-prompts.md

# Module airbyte.mcp.prompts

Copy Page

MCP prompt definitions for the PyAirbyte MCP server.

This module defines prompts that can be invoked by MCP clients to perform common workflows.

## Functions[​](#functions "Direct link to Functions")

`register_prompts(app: FastMCP) ‑> None` : Register prompts with the FastMCP app.

Args: app: FastMCP application instance

`test_my_tools_prompt(scope: "Annotated[str | None, Field(description='Optional free-form text to focus or constrain testing. This can be a single word, a sentence, or a paragraph describing the desired scope or constraints.')]" = None) ‑> list[dict[str, str]]` : Generate a prompt that instructs the agent to test available tools.
