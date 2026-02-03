# Source: https://gofastmcp.com/python-sdk/fastmcp-server-low_level.md

> ## Documentation Index
> Fetch the complete documentation index at: https://gofastmcp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# low_level

# `fastmcp.server.low_level`

## Classes

### `MiddlewareServerSession` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

ServerSession that routes initialization requests through FastMCP middleware.

**Methods:**

#### `fastmcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L45" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
fastmcp(self) -> FastMCP
```

Get the FastMCP instance.

### `LowLevelServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L132" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `fastmcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L146" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
fastmcp(self) -> FastMCP
```

Get the FastMCP instance.

#### `create_initialization_options` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L153" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
create_initialization_options(self, notification_options: NotificationOptions | None = None, experimental_capabilities: dict[str, dict[str, Any]] | None = None, **kwargs: Any) -> InitializationOptions
```

#### `get_capabilities` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
get_capabilities(self, notification_options: NotificationOptions, experimental_capabilities: dict[str, dict[str, Any]]) -> mcp.types.ServerCapabilities
```

Override to set capabilities.tasks as a first-class field per SEP-1686.

This ensures task capabilities appear in capabilities.tasks instead of
capabilities.experimental.tasks, which is required by the MCP spec and
enables proper task detection by clients like VS Code Copilot 1.107+.

#### `run` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L193" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
run(self, read_stream: MemoryObjectReceiveStream[SessionMessage | Exception], write_stream: MemoryObjectSendStream[SessionMessage], initialization_options: InitializationOptions, raise_exceptions: bool = False, stateless: bool = False)
```

Overrides the run method to use the MiddlewareServerSession.

#### `read_resource` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L229" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
read_resource(self) -> Callable[[Callable[[AnyUrl], Awaitable[mcp.types.ReadResourceResult | mcp.types.CreateTaskResult]]], Callable[[AnyUrl], Awaitable[mcp.types.ReadResourceResult | mcp.types.CreateTaskResult]]]
```

Decorator for registering a read\_resource handler with CreateTaskResult support.

The MCP SDK's read\_resource decorator does not support returning CreateTaskResult
for background task execution. This decorator wraps the result in ServerResult.

This decorator can be removed once the MCP SDK adds native CreateTaskResult support
for resources.

#### `get_prompt` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L273" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
get_prompt(self) -> Callable[[Callable[[str, dict[str, Any] | None], Awaitable[mcp.types.GetPromptResult | mcp.types.CreateTaskResult]]], Callable[[str, dict[str, Any] | None], Awaitable[mcp.types.GetPromptResult | mcp.types.CreateTaskResult]]]
```

Decorator for registering a get\_prompt handler with CreateTaskResult support.

The MCP SDK's get\_prompt decorator does not support returning CreateTaskResult
for background task execution. This decorator wraps the result in ServerResult.

This decorator can be removed once the MCP SDK adds native CreateTaskResult support
for prompts.
