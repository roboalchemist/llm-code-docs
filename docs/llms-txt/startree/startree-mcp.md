# Source: https://docs.startree.ai/corecapabilities/query_data/mcp/startree-mcp.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# StarTree MCP server

StarTree provides an ability to deploy a MCP server within the environment. This can be leveraged for various agentic workflows and conversational analytics use cases.

<img src="https://mintcdn.com/startree/db5_Hpj5dSqLuq1y/corecapabilities/query_data/images/startree-mcp.png?fit=max&auto=format&n=db5_Hpj5dSqLuq1y&q=85&s=568000ea4758892ed63ae3f6ac85c1c7" alt="StarTree MCP" width="1884" height="844" data-path="corecapabilities/query_data/images/startree-mcp.png" />

This MCP server is based off of OSS GitHub - [startreedata/mcp-pinot](https://github.com/startreedata/mcp-pinot): MCP Server for Apache Pinot and exposes several tools such as: list\_tables, table\_details, create\_schema, read\_query etc. It provides OAuth based authentication flow for the clients.

<Info>
  Once, deployed, MCP server will be available at [<u>https://mcp.\<domain>/mcp</u>](https://mcp.\{domain}/mcp)
</Info>

**For installation** - please reach out to your StarTree representative.

## Conversational Queries on Startree

One common pattern we see is use of this MCP server in conversational analytics on top of Pinot and StarTree. You can hook up this MCP server to your favorite AI tool: Claude, Librechat and be able to simply ask natural language questions against the Pinot table.

### Example: Claude Code

* Install claude code: [Quickstart - Claude Docs](https://docs.claude.com/en/docs/claude-code/quickstart)
* Add mcp server and use it following: [Connect Claude Code to tools via MCP - Claude Docs](https://docs.claude.com/en/docs/claude-code/mcp#authenticate-with-remote-mcp-servers)
  * Ex: `claude mcp add --transport http pinot-mcp https://mcp.<domain>/mcp`
* In Claude code, use the command `/mcp` to authenticate with StarTree MCP server
* Start asking questions. For example, in our demo clickstream Pinot table, we asked this question: "For clickstream table in Pinot, what's the conversion rate ?" Here's the output from Claude Code

<img src="https://mintcdn.com/startree/OEv_LmKt0guvQI7k/images/claude-code-output.png?fit=max&auto=format&n=OEv_LmKt0guvQI7k&q=85&s=a5ef6284002209c05d20b7ba3f94461e" alt="Claude Code Output Pn" width="2680" height="1284" data-path="images/claude-code-output.png" />

## Limitations

* At the moment (Nov, 2025) MCP server with OAuth does not seem to work with Claude desktop because of an existing bug.

Built with [Mintlify](https://mintlify.com).
