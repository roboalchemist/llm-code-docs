# Source: https://docs.prefect.io/v3/api-ref/python/prefect-logging-clients.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# clients

# `prefect.logging.clients`

## Functions

### `http_to_ws` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L67" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
http_to_ws(url: str) -> str
```

### `logs_out_socket_from_api_url` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L71" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
logs_out_socket_from_api_url(url: str) -> str
```

### `get_logs_subscriber` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_logs_subscriber(filter: Optional['LogFilter'] = None, reconnection_attempts: int = 10) -> 'PrefectLogsSubscriber'
```

Get a logs subscriber based on the current Prefect configuration.

Similar to get\_events\_subscriber, this automatically detects whether
you're using Prefect Cloud or OSS and returns the appropriate subscriber.

## Classes

### `PrefectLogsSubscriber` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L127" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Subscribes to a Prefect logs stream, yielding logs as they occur.

Example:

from prefect.logging.clients import PrefectLogsSubscriber
from prefect.client.schemas.filters import LogFilter, LogFilterLevel
import logging

filter = LogFilter(level=LogFilterLevel(ge\_=logging.INFO))

async with PrefectLogsSubscriber(filter=filter) as subscriber:
async for log in subscriber:
print(log.timestamp, log.level, log.message)

**Methods:**

#### `client_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L193" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
client_name(self) -> str
```

### `PrefectCloudLogsSubscriber` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L321" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Logs subscriber for Prefect Cloud

**Methods:**

#### `client_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/logging/clients.py#L193" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
client_name(self) -> str
```


Built with [Mintlify](https://mintlify.com).