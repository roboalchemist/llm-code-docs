# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/remote-mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote MCP Server

> Expose your index via MCP over HTTP for remote clients in 3 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

<Note>
  **For local MCP integration** with Claude Desktop, Claude Code, Cursor, or other agents, see [Local MCP Server](/context-services/context-connectors/quickstart/claude-desktop-integration).
</Note>

## Prerequisites

* Node.js 18+
* Augment API credentials
* An indexed project (see [Index and Search Code](/context-services/context-connectors/quickstart/index-git-repos))

## Steps

### 1. Install

```bash  theme={null}
npm install @augmentcode/context-connectors @modelcontextprotocol/sdk
```

### 2. Set credentials

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
```

### 3. Start the server

```bash  theme={null}
npx ctxc mcp http -i my-project --port 8080 --api-key "secret"
```

You should see:

```
MCP HTTP server running at http://localhost:8080/mcp
```

### 4. Test with curl

First, initialize a session:

```bash  theme={null}
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer secret" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": { "name": "curl-test", "version": "1.0.0" }
    }
  }' -i
```

Note the `mcp-session-id` header in the response. Use it for subsequent requests:

```bash  theme={null}
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer secret" \
  -H "mcp-session-id: <session-id-from-initialize>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "search",
      "arguments": { "query": "authentication" }
    }
  }'
```

You should see JSON search results.

## Done!

Your index is accessible via MCP over HTTP at `http://localhost:8080/mcp`. Remote clients can now search your codebase using the Model Context Protocol over HTTP.

## Also Works With

| Instead of...  | Try...                                                           |
| -------------- | ---------------------------------------------------------------- |
| localhost only | `--host 0.0.0.0` to accept external connections                  |
| No CORS        | `--cors "*"` or `--cors "https://myapp.com"` for browser clients |
| Full access    | `--search-only` to disable file operations                       |
| Local storage  | `--store s3` with `CC_S3_BUCKET` for shared indexes              |
