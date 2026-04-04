# Source: https://www.thundercompute.com/docs/guides/mcp-server-for-managing-gpus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install MCP Server

> Install the Mintlify MCP server to host Thunder Compute docs locally. Enables AI tools like Cursor to provide instant answers based on documentation.

## TL;DR

```
# 1 – install the docs bundle
npx @mintlify/mcp@latest add thundercompute

# 2 – start the server
node ~/.mcp/thundercompute/src/index.js
```

Your **Thunder Compute MCP** server is now live at [**http://localhost:5001**](http://localhost:5001) and ready for any AI client.

## Connect in Cursor

1. Open **Cursor → Settings → Docs**.
2. **Add Source** → `http://localhost:5001`.
3. Ask something like *"How do I submit a batch to Thunder Compute?"*.

## Update docs

Run the install command again whenever you need the latest release:

```
npx @mintlify/mcp@latest add thundercompute
```
