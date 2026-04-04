# Source: https://www.speakeasy.com/md/docs/standalone-mcp/customize-tools.md

# Customize Tools

You can customize how your API operations are exposed as MCP tools using the `x-speakeasy-mcp` OpenAPI extension. This allows you to control tool names, descriptions, scopes, and whether specific operations should be included in your MCP server.

## Set the configuration options

The `x-speakeasy-mcp` extension can be used on any operation to customize the MCP tool:

```yaml filename="openapi.yaml"
paths:
  /products:
    post:
      operationId: createProduct
      tags: [products]
      summary: Create product
      description: API endpoint for creating a product in the CMS
      x-speakeasy-mcp:
        disabled: false
        name: create-product
        scopes: [write, ecommerce]
        description: |
          Creates a new product using the provided form. The product name should
          not contain any special characters or harmful words.
      # ...
```

### `disabled` (_optional_, default: `false`)

If set to `true`, the generator will not create the MCP tool for this operation.

### `name` (_optional_)

This is the name of the MCP tool. The default value is derived from `operationId`, `tags`, `x-speakeasy-name-override`, and `x-speakeasy-name-group`. In the example above, the default name would be `products_create-product`.

### `title` (_optional_)

A human-friendly display name for the tool. While `name` serves as the programmatic identifier, `title` provides a readable name shown in client interfaces like VS Code Copilot Chat. For example, a tool with `name: "search_repositories"` could have `title: "Search repositories"` for better user experience.

```yaml
x-speakeasy-mcp:
  name: search_repositories
  title: Search repositories
  description: Search for GitHub repositories using various filters
```

### `scopes` (_optional_)

You can use scopes to tag tools so that users can choose which set of tools they want to mount when the MCP server starts. For example, tagging relevant operations with a `read` scope allows users to start a server in read-only mode.

### `description` (_optional_)

Each MCP tool description is passed as context to MCP clients and language models. The default value is the OpenAPI operation summary and description. It's a good practice to review and customize these descriptions for better context.

### `readOnlyHint` (_optional_, default: `false`)

Indicates whether the tool modifies its environment. Set to `true` for tools that only read data without making changes.

```yaml
x-speakeasy-mcp:
  readOnlyHint: true
  description: Retrieve driver statistics without modifying any data
```

### `destructiveHint` (_optional_, default: `true`)

Indicates whether the tool performs destructive updates to its environment. Set to `false` for tools that only perform additive updates. This property is meaningful only when `readOnlyHint` is `false`.

```yaml
x-speakeasy-mcp:
  readOnlyHint: false
  destructiveHint: true
  description: Delete a driver record permanently from the system
```

### `idempotentHint` (_optional_, default: `false`)

Indicates whether calling the tool repeatedly with the same arguments has no additional effect on its environment. Set to `true` for idempotent operations. This property is meaningful only when `readOnlyHint` is `false`.

```yaml
x-speakeasy-mcp:
  readOnlyHint: false
  idempotentHint: true
  description: Update driver status - calling multiple times with same status has no additional effect
```

### `openWorldHint` (_optional_, default: `true`)

Indicates whether the tool interacts with an "open world" of external entities. Set to `false` for tools whose domain of interaction is closed. For example, a web search tool has an open world, whereas a memory tool does not.

```yaml
x-speakeasy-mcp:
  openWorldHint: false
  description: Query the internal driver database - does not access external systems
```

## Use overlays

[Overlays](/openapi/overlays) are a convenient way you can add the `x-speakeasy-mcp` extension to existing OpenAPI documents without modifying them. To create an Overlay file, you can use the Speakeasy [Overlay Playground](https://overlay.speakeasy.com/).

For example, you can add scopes based on HTTP methods:

```yaml filename="overlay.yaml"
overlay: 1.0.0
info:
  title: Add MCP scopes
  version: 0.0.0
actions:
  - target: $.paths.*["get","head","query"]
    update: { "x-speakeasy-mcp": { "scopes": ["read"] } }

  - target: $.paths.*["post","put","delete","patch"]
    update: { "x-speakeasy-mcp": { "scopes": ["write"] } }
```

## Advanced usage

### Specify scopes at runtime

When starting the MCP server, you can specify which scopes to include using the `--scope` flag:

```json
{
  "mcpServers": {
    "MyAPI": {
      "command": "npx",
      "args": ["your-npm-package@latest", "start", "--scope", "read"],
      "env": {
        "API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

This example configuration only mounts tools tagged with the `read` scope, creating a read-only server. You can specify multiple scopes by repeating the flag:

```json
{
  "mcpServers": {
    "MyAPI": {
      "command": "npx",
      "args": ["your-npm-package@latest", "start", "--scope", "read", "--scope", "admin"],
      "env": {
        "API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

### Specify individual tools

You can further limit the subset of tools mounted on an MCP server by specifying individual tool names using the `--tool` flag:

```json
{
  "mcpServers": {
    "MyAPI": {
      "command": "npx",
      "args": ["your-npm-package@latest", "start", "--tool", "list-products", "--tool", "get-product"],
      "env": {
        "API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
