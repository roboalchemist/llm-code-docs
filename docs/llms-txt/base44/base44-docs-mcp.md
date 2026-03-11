# Source: https://docs.base44.com/developers/backend/overview/base44-docs-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Base44 Docs MCP

> Let AI assistants search Base44 documentation while you develop

The Base44 Docs MCP server lets AI assistants like Cursor, Claude Desktop, and VS Code search Base44 documentation directly. Ask questions about the SDK, CLI, entities, or any Base44 feature and get answers with links to the relevant docs.

Results come from live documentation, so you always get the latest information.

## Connect your AI assistant

Add it to your AI tool's MCP configuration:

```json  theme={null}
"base44-docs": {
  "type": "http",
  "url": "https://docs.base44.com/mcp"
}
```

<Tip>Some tools require a restart to pick up new MCP configurations.</Tip>

## Available tools

The server provides a single search tool that can:

* **Search all documentation:** Query guides, API references, and tutorials.
* **Return code examples:** Get SDK usage examples and implementation patterns.
* **Filter results:** Narrow searches by version, language, API-only, or code-only content.
* **Link to sources:** Every result includes a direct link to the documentation page.

## Example prompts

Once connected, ask your AI assistant questions like:

* "How do I create an entity with the Base44 SDK?"
* "What types of authentication can I use?"
* "What CLI commands are available for deployment?"
* "How do security rules work in Base44?"

The AI will search the documentation and return relevant information with links to learn more.

## See also

* [Base44 MCP server](/developers/backend/overview/mcp-server): Create and manage backend projects from AI assistants
* [Skills](/developers/backend/overview/skills): Reusable instructions that teach AI coding agents how to perform Base44-specific tasks


Built with [Mintlify](https://mintlify.com).