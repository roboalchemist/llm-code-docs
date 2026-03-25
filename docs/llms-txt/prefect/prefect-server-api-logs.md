# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# logs

# `prefect.server.api.logs`

Routes for interacting with log objects.

## Functions

### `create_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/logs.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_logs(logs: Sequence[LogCreate], db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

Create new logs from the provided schema.

For more information, see [https://docs.prefect.io/v3/how-to-guides/workflows/add-logging](https://docs.prefect.io/v3/how-to-guides/workflows/add-logging).

### `read_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/logs.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_logs(limit: int = dependencies.LimitBody(), offset: int = Body(0, ge=0), logs: Optional[LogFilter] = None, sort: LogSort = Body(LogSort.TIMESTAMP_ASC), db: PrefectDBInterface = Depends(provide_database_interface)) -> Sequence[Log]
```

Query for logs.

### `stream_logs_out` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/logs.py#L63" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stream_logs_out(websocket: WebSocket) -> None
```

Serve a WebSocket to stream live logs


Built with [Mintlify](https://mintlify.com).