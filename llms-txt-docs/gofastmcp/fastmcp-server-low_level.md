# Source: https://gofastmcp.com/python-sdk/fastmcp-server-low_level.md

# low_level

# `fastmcp.server.low_level`

## Classes

### `MiddlewareServerSession` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

ServerSession that routes initialization requests through FastMCP middleware.

**Methods:**

#### `fastmcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
fastmcp(self) -> FastMCP
```

Get the FastMCP instance.

### `LowLevelServer` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `fastmcp` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
fastmcp(self) -> FastMCP
```

Get the FastMCP instance.

#### `create_initialization_options` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L110" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
create_initialization_options(self, notification_options: NotificationOptions | None = None, experimental_capabilities: dict[str, dict[str, Any]] | None = None, **kwargs: Any) -> InitializationOptions
```

#### `run` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/low_level.py#L125" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
run(self, read_stream: MemoryObjectReceiveStream[SessionMessage | Exception], write_stream: MemoryObjectSendStream[SessionMessage], initialization_options: InitializationOptions, raise_exceptions: bool = False, stateless: bool = False)
```

Overrides the run method to use the MiddlewareServerSession.
