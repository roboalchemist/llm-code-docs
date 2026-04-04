# Source: https://gofastmcp.com/python-sdk/fastmcp-server-providers-openapi-components.md

> ## Documentation Index
> Fetch the complete documentation index at: https://gofastmcp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# components

# `fastmcp.server.providers.openapi.components`

OpenAPI component classes: Tool, Resource, and ResourceTemplate.

## Classes

### `OpenAPITool` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Tool implementation for OpenAPI endpoints.

**Methods:**

#### `run` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L108" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
run(self, arguments: dict[str, Any]) -> ToolResult
```

Execute the HTTP request using RequestDirector.

### `OpenAPIResource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L167" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Resource implementation for OpenAPI endpoints.

**Methods:**

#### `read` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L199" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
read(self) -> ResourceResult
```

Fetch the resource data by making an HTTP request.

### `OpenAPIResourceTemplate` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L281" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Resource template implementation for OpenAPI endpoints.

**Methods:**

#### `create_resource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/providers/openapi/components.py#L313" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
create_resource(self, uri: str, params: dict[str, Any], context: Context | None = None) -> Resource
```

Create a resource with the given parameters.
