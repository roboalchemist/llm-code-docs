# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-subscriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# subscriptions

# `prefect.server.utilities.subscriptions`

## Functions

### `accept_prefect_socket` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/subscriptions.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
accept_prefect_socket(websocket: WebSocket) -> Optional[WebSocket]
```

### `still_connected` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/subscriptions.py#L102" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
still_connected(websocket: WebSocket) -> bool
```

Checks that a client websocket still seems to be connected during a period where
the server is expected to be sending messages.


Built with [Mintlify](https://mintlify.com).