# Source: https://docs.xano.com/developer-mcp/resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resources & Library Usage

> Access XanoScript documentation as MCP resources and use the package as an npm library

Beyond its tools, the Xano Developer MCP also exposes XanoScript documentation as MCP resources for direct access, and can be imported as an npm library for custom integrations.

## MCP Resources

The server exposes 26 XanoScript documentation files as MCP resources. These can be read directly by URI without calling a tool, which is useful for MCP clients that support resource access.

| Resource URI                     | Description                          |
| -------------------------------- | ------------------------------------ |
| `xanoscript://docs/readme`       | Overview and quick reference         |
| `xanoscript://docs/syntax`       | Expressions, operators, and filters  |
| `xanoscript://docs/types`        | Data types and validation            |
| `xanoscript://docs/tables`       | Database schema definitions          |
| `xanoscript://docs/functions`    | Reusable function stacks             |
| `xanoscript://docs/apis`         | HTTP endpoint definitions            |
| `xanoscript://docs/tasks`        | Scheduled and cron jobs              |
| `xanoscript://docs/triggers`     | Event-driven handlers                |
| `xanoscript://docs/database`     | Database operations                  |
| `xanoscript://docs/agents`       | AI agent configuration               |
| `xanoscript://docs/tools`        | AI tools for agents                  |
| `xanoscript://docs/mcp-servers`  | MCP server definitions               |
| `xanoscript://docs/testing`      | Unit tests and mocks                 |
| `xanoscript://docs/integrations` | External service integrations        |
| `xanoscript://docs/frontend`     | Static frontend development          |
| `xanoscript://docs/run`          | Run job and service configurations   |
| `xanoscript://docs/addons`       | Reusable subqueries for related data |
| `xanoscript://docs/debugging`    | Logging and debugging tools          |
| `xanoscript://docs/performance`  | Performance optimization             |
| `xanoscript://docs/realtime`     | Real-time channels and events        |
| `xanoscript://docs/schema`       | Runtime schema parsing               |
| `xanoscript://docs/security`     | Security best practices              |
| `xanoscript://docs/streaming`    | Data streaming operations            |
| `xanoscript://docs/middleware`   | Request/response interceptors        |
| `xanoscript://docs/branch`       | Branch-level settings                |
| `xanoscript://docs/workspace`    | Workspace-level settings             |

***

## npm Library Usage

The `@xano/developer-mcp` package can also be imported directly as an npm library, allowing you to integrate its capabilities into your own applications or build custom MCP servers.

### Installation

```bash  theme={null}
npm install @xano/developer-mcp
```

### Entry Points

The package provides three entry points:

| Import Path                  | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| `@xano/developer-mcp`        | Main library entry (recommended)             |
| `@xano/developer-mcp/tools`  | Tools module directly                        |
| `@xano/developer-mcp/server` | Server module (for extending the MCP server) |

### Core Functions

```typescript  theme={null}
import {
  validateXanoscript,
  xanoscriptDocs,
  metaApiDocs,
  runApiDocs,
  cliDocs,
  mcpVersion
} from '@xano/developer-mcp';
```

| Function                   | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| `validateXanoscript(args)` | Validate XanoScript code and get detailed error info |
| `xanoscriptDocs(args)`     | Get XanoScript language documentation                |
| `metaApiDocs(args)`        | Get Meta API documentation                           |
| `runApiDocs(args)`         | Get Run API documentation                            |
| `cliDocs(args)`            | Get CLI documentation                                |
| `mcpVersion()`             | Get the package version                              |

### Building Custom MCP Servers

If you want to build a custom MCP server that includes XanoScript capabilities, you can use the tool definitions and handler:

```typescript  theme={null}
import {
  toolDefinitions,
  handleTool,
  toMcpResponse
} from '@xano/developer-mcp';

// toolDefinitions: Array of MCP tool definitions
// handleTool: Dispatches tool calls to the correct handler
// toMcpResponse: Converts a ToolResult to MCP response format
```

### Utility Functions

```typescript  theme={null}
import {
  getDocsForFilePath,
  extractQuickReference,
  getXanoscriptDocsVersion
} from '@xano/developer-mcp';
```

| Function                     | Description                                       |
| ---------------------------- | ------------------------------------------------- |
| `getDocsForFilePath(path)`   | Get matching documentation topics for a file path |
| `extractQuickReference(doc)` | Extract the Quick Reference section from a doc    |
| `getXanoscriptDocsVersion()` | Get the documentation version from `version.json` |

### TypeScript Types

All types are exported for TypeScript consumers:

```typescript  theme={null}
import type {
  ValidateXanoscriptArgs,
  ValidationResult,
  ParserDiagnostic,
  XanoscriptDocsArgs,
  XanoscriptDocsResult,
  MetaApiDocsArgs,
  MetaApiDocsResult,
  RunApiDocsArgs,
  RunApiDocsResult,
  CliDocsArgs,
  CliDocsResult,
  McpVersionResult,
  ToolResult,
  DocConfig
} from '@xano/developer-mcp';
```

***

## Source Code

The Xano Developer MCP is open source under the MIT license.

<CardGroup cols={2}>
  <Card title="GitHub" icon="github" href="https://github.com/xano-inc/xano-developer-mcp">
    View the source code and contribute
  </Card>

  <Card title="npm" icon="npm" href="https://www.npmjs.com/package/@xano/developer-mcp">
    View the package on npm
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).