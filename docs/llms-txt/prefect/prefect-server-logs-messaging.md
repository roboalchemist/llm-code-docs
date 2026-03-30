# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-logs-messaging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# messaging

# `prefect.server.logs.messaging`

Log messaging for streaming logs through the messaging system.

## Functions

### `create_log_publisher` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/messaging.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_log_publisher() -> AsyncGenerator[messaging.Publisher, None]
```

Creates a publisher for sending logs to the messaging system.

**Returns:**

* A messaging publisher configured for the "logs" topic

### `publish_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/messaging.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
publish_logs(logs: list[Log]) -> None
```

Publishes logs to the messaging system.

**Args:**

* `logs`: The logs to publish


Built with [Mintlify](https://mintlify.com).