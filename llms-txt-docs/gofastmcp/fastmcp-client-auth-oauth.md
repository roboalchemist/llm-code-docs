# Source: https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth.md

# oauth

# `fastmcp.client.auth.oauth`

## Functions

### `check_if_auth_required` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
check_if_auth_required(mcp_url: str, httpx_kwargs: dict[str, Any] | None = None) -> bool
```

Check if the MCP endpoint requires authentication by making a test request.

**Returns:**

* True if auth appears to be required, False otherwise

## Classes

### `ClientNotFoundError` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Raised when OAuth client credentials are not found on the server.

### `TokenStorageAdapter` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `clear` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
clear(self) -> None
```

#### `get_tokens` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
get_tokens(self) -> OAuthToken | None
```

#### `set_tokens` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L107" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
set_tokens(self, tokens: OAuthToken) -> None
```

#### `get_client_info` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
get_client_info(self) -> OAuthClientInformationFull | None
```

#### `set_client_info` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L121" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
set_client_info(self, client_info: OAuthClientInformationFull) -> None
```

### `OAuth` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

OAuth client provider for MCP servers with browser-based authentication.

This class provides OAuth authentication for FastMCP clients by opening
a browser for user authorization and running a local callback server.

**Methods:**

#### `redirect_handler` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L226" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
redirect_handler(self, authorization_url: str) -> None
```

Open browser for authorization, with pre-flight check for invalid client.

#### `callback_handler` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L247" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
callback_handler(self) -> tuple[str, str | None]
```

Handle OAuth callback and return (auth\_code, state).

#### `async_auth_flow` <sup><a href="https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/client/auth/oauth.py#L286" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
async_auth_flow(self, request: httpx.Request) -> AsyncGenerator[httpx.Request, httpx.Response]
```

HTTPX auth flow with automatic retry on stale cached credentials.

If the OAuth flow fails due to invalid/stale client credentials,
clears the cache and retries once with fresh registration.
