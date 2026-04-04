# Source: https://docs.xano.com/developer-mcp/tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools Reference

> Complete reference for all tools available in the Xano Developer MCP

The Xano Developer MCP provides 6 tools for AI-assisted XanoScript development. These tools are automatically available to your AI assistant once the MCP server is connected.

## validate\_xanoscript

Validates XanoScript code for syntax errors. Returns a list of errors with line and column positions, or confirms the code is valid. The language server auto-detects the object type (table, function, query, etc.) from the code syntax.

### Parameters

| Parameter | Type   | Required | Description                     |
| --------- | ------ | -------- | ------------------------------- |
| `code`    | string | Yes      | The XanoScript code to validate |

### Response

| Field     | Type    | Description                                                                            |
| --------- | ------- | -------------------------------------------------------------------------------------- |
| `valid`   | boolean | Whether the code is valid                                                              |
| `errors`  | array   | List of errors, each with `range` (start/end line and column), `message`, and `source` |
| `message` | string  | Human-readable result summary                                                          |

### Examples

**Valid code:**

```
validate_xanoscript({ code: "var $result { value = 1 + 2 }" })
```

Returns:

```json  theme={null}
{
  "valid": true,
  "errors": [],
  "message": "XanoScript is valid. No syntax errors found."
}
```

**Invalid code:**

```
validate_xanoscript({ code: "var $result { value = }" })
```

Returns errors with the exact line and column where the issue was found, making it easy to pinpoint and fix problems.

<Tip>
  Use this tool as you write XanoScript to catch syntax errors before pushing code to Xano. AI assistants will often call this automatically after generating code.
</Tip>

***

## xanoscript\_docs

Retrieves XanoScript programming language documentation. Call without parameters for the overview. Use `topic` for specific documentation, or `file_path` for context-aware docs based on the file you're editing.

### Parameters

| Parameter   | Type   | Required | Description                                                                  |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `topic`     | string | No       | Specific documentation topic to retrieve                                     |
| `file_path` | string | No       | File path being edited (e.g., `apis/users/create.xs`) for context-aware docs |
| `mode`      | string | No       | `full` (default) or `quick_reference` for a compact syntax cheatsheet        |

### Available Topics

<Tabs>
  <Tab title="Core Language">
    | Topic    | Description                                                   |
    | -------- | ------------------------------------------------------------- |
    | `readme` | XanoScript overview, workspace structure, and quick reference |
    | `syntax` | Expressions, operators, filters, and system variables         |
    | `types`  | Data types, input blocks, and validation                      |
    | `schema` | Runtime schema parsing and validation                         |
  </Tab>

  <Tab title="Data">
    | Topic       | Description                                                 |
    | ----------- | ----------------------------------------------------------- |
    | `tables`    | Database schema definitions with indexes and relationships  |
    | `database`  | All `db.*` operations: query, get, add, edit, patch, delete |
    | `addons`    | Reusable subqueries for fetching related data               |
    | `streaming` | Streaming data from files, requests, and responses          |
  </Tab>

  <Tab title="APIs & Endpoints">
    | Topic      | Description                                                     |
    | ---------- | --------------------------------------------------------------- |
    | `apis`     | HTTP endpoint definitions with authentication and CRUD patterns |
    | `tasks`    | Scheduled and cron jobs                                         |
    | `triggers` | Event-driven handlers (table, realtime, workspace, agent, MCP)  |
    | `realtime` | Real-time channels and events for push updates                  |
  </Tab>

  <Tab title="AI & Agents">
    | Topic         | Description                                         |
    | ------------- | --------------------------------------------------- |
    | `agents`      | AI agent configuration with LLM providers and tools |
    | `tools`       | AI tools for agents and MCP servers                 |
    | `mcp-servers` | MCP server definitions exposing tools               |
  </Tab>

  <Tab title="Configuration">
    | Topic          | Description                                                            |
    | -------------- | ---------------------------------------------------------------------- |
    | `workspace`    | Workspace-level settings: environment variables, preferences, realtime |
    | `branch`       | Branch-level settings: middleware, history retention, visual styling   |
    | `middleware`   | Request/response interceptors for functions, queries, tasks, and tools |
    | `integrations` | Cloud storage, Redis, security, and external APIs                      |
  </Tab>

  <Tab title="Development">
    | Topic         | Description                                                  |
    | ------------- | ------------------------------------------------------------ |
    | `testing`     | Unit tests, mocks, and assertions                            |
    | `debugging`   | Logging, inspecting, and debugging XanoScript execution      |
    | `frontend`    | Static frontend development and deployment                   |
    | `run`         | Run job and service configurations for the Xano Job Runner   |
    | `performance` | Performance optimization best practices                      |
    | `security`    | Security best practices for authentication and authorization |
  </Tab>
</Tabs>

### Context-Aware Docs

When `file_path` is provided, the tool automatically returns all documentation relevant to the type of file you're editing. For example:

| File Path                   | Topics Returned                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `apis/users/create.xs`      | syntax, types, apis, database, testing, integrations, performance, realtime, schema, security, streaming              |
| `tables/product.xs`         | syntax, tables                                                                                                        |
| `agents/support-bot.xs`     | syntax, types, agents                                                                                                 |
| `functions/utils/format.xs` | syntax, types, functions, database, testing, integrations, performance, realtime, schema, security, streaming, addons |

The `syntax` topic is always included as a foundation. The `readme` topic is never auto-included (call it explicitly for the overview).

### Quick Reference Mode

Use `mode: "quick_reference"` for compact output that only returns the Quick Reference section from each doc. This is recommended when you need to conserve context window space.

### Examples

```
// Get the overview
xanoscript_docs()

// Get full function docs
xanoscript_docs({ topic: "functions" })

// Context-aware: all docs relevant to API files
xanoscript_docs({ file_path: "apis/users/create.xs" })

// Compact quick reference for database operations
xanoscript_docs({ topic: "database", mode: "quick_reference" })
```

***

## meta\_api\_docs

Retrieves documentation for Xano's Meta API, which provides programmatic access to manage workspaces, databases, APIs, functions, agents, and more.

### Parameters

| Parameter         | Type    | Required | Description                                                   |
| ----------------- | ------- | -------- | ------------------------------------------------------------- |
| `topic`           | string  | Yes      | Documentation topic to retrieve                               |
| `detail_level`    | string  | No       | `overview`, `detailed` (default), or `examples`               |
| `include_schemas` | boolean | No       | Include JSON schemas for requests/responses (default: `true`) |

### Available Topics

| Topic            | Description                          |
| ---------------- | ------------------------------------ |
| `start`          | Getting started with the Meta API    |
| `authentication` | API authentication and authorization |
| `workspace`      | Workspace management endpoints       |
| `apigroup`       | API group operations                 |
| `api`            | API endpoint management              |
| `table`          | Database table operations            |
| `function`       | Function management                  |
| `task`           | Scheduled task operations            |
| `agent`          | AI agent configuration               |
| `tool`           | AI tool management                   |
| `mcp_server`     | MCP server endpoints                 |
| `middleware`     | Middleware configuration             |
| `branch`         | Branch management                    |
| `realtime`       | Real-time channel operations         |
| `file`           | File management                      |
| `history`        | Version history                      |
| `workflows`      | Step-by-step workflow guides         |

### Detail Levels

* **`overview`** — Returns just the method, path, and description for each endpoint
* **`detailed`** — Includes parameters, request body details, and response schemas
* **`examples`** — Adds full request/response examples with code blocks

### Examples

```
// Get started
meta_api_docs({ topic: "start" })

// Full table management docs
meta_api_docs({ topic: "table", detail_level: "detailed" })

// API examples without schemas
meta_api_docs({ topic: "api", detail_level: "examples", include_schemas: false })

// Workflow guides
meta_api_docs({ topic: "workflows" })
```

***

## run\_api\_docs

Retrieves documentation for Xano's Run API, which provides runtime execution, session management, and XanoScript execution capabilities.

<Note>
  The Run API uses a fixed base URL: `https://app.dev.xano.com/api:run/<endpoint>` — this is **not** your Xano instance URL.
</Note>

### Parameters

| Parameter         | Type    | Required | Description                                                   |
| ----------------- | ------- | -------- | ------------------------------------------------------------- |
| `topic`           | string  | Yes      | Documentation topic to retrieve                               |
| `detail_level`    | string  | No       | `overview`, `detailed` (default), or `examples`               |
| `include_schemas` | boolean | No       | Include JSON schemas for requests/responses (default: `true`) |

### Available Topics

| Topic       | Description                               |
| ----------- | ----------------------------------------- |
| `start`     | Getting started with the Run API          |
| `run`       | Execute XanoScript code and API endpoints |
| `session`   | Session management for stateful execution |
| `history`   | Execution history and debugging           |
| `data`      | Data operations and variable management   |
| `workflows` | Step-by-step workflow guides              |

### Examples

```
// Get started
run_api_docs({ topic: "start" })

// Full execution docs
run_api_docs({ topic: "run", detail_level: "detailed" })

// Session examples
run_api_docs({ topic: "session", detail_level: "examples" })
```

***

## cli\_docs

Retrieves documentation for the Xano CLI (`@xano/cli`), covering local development workflows, code sync, and XanoScript execution from the command line.

### Parameters

| Parameter      | Type   | Required | Description                                     |
| -------------- | ------ | -------- | ----------------------------------------------- |
| `topic`        | string | Yes      | Documentation topic to retrieve                 |
| `detail_level` | string | No       | `overview`, `detailed` (default), or `examples` |

### Available Topics

| Topic         | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `start`       | Getting started — installation and setup                     |
| `profile`     | Profile management — credentials and multi-environment setup |
| `workspace`   | Workspace operations — pull/push code sync                   |
| `branch`      | Branch management                                            |
| `function`    | Function management — list, get, create, edit                |
| `run`         | Run API commands — execute code, manage projects/sessions    |
| `static_host` | Static hosting — deploy frontend builds                      |
| `integration` | CLI + Meta API integration guide — when to use each          |

### Examples

```
// Get started
cli_docs({ topic: "start" })

// When to use CLI vs Meta API
cli_docs({ topic: "integration" })

// Full workspace commands
cli_docs({ topic: "workspace", detail_level: "detailed" })
```

***

## mcp\_version

Returns the current version of the Xano Developer MCP server.

### Parameters

None.

### Response

Returns the version string (e.g., `"1.0.31"`).

### Example

```
mcp_version()
// Returns: "1.0.31"
```


Built with [Mintlify](https://mintlify.com).