# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-logs-stream.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# stream

# `prefect.server.logs.stream`

Log streaming for live log distribution via websockets.

## Functions

### `subscribed` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
subscribed(filter: LogFilter) -> AsyncGenerator['Queue[Log]', None]
```

Subscribe to a stream of logs matching the given filter.

**Args:**

* `filter`: The log filter to apply

### `logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
logs(filter: LogFilter) -> AsyncGenerator[AsyncIterable[Log | None], None]
```

Create a stream of logs matching the given filter.

**Args:**

* `filter`: The log filter to apply

### `log_matches_filter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L99" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
log_matches_filter(log: Log, filter: LogFilter) -> bool
```

Check if a log matches the given filter criteria.

**Args:**

* `log`: The log to check
* `filter`: The filter to apply

**Returns:**

* True if the log matches the filter, False otherwise

### `distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L150" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
distributor() -> AsyncGenerator[messaging.MessageHandler, None]
```

Create a message handler that distributes logs to subscribed clients.

### `start_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L190" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_distributor() -> None
```

Starts the distributor consumer as a global background task

### `stop_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L202" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop_distributor() -> None
```

Stops the distributor consumer global background task

### `run_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L253" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_distributor(started: asyncio.Event) -> NoReturn
```

Runs the distributor consumer forever until it is cancelled

## Classes

### `LogDistributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L220" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Service for distributing logs to websocket subscribers

**Methods:**

#### `all_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
all_services(cls) -> Sequence[type[Self]]
```

Get list of all service classes

#### `enabled` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L234" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
enabled(cls) -> bool
```

#### `enabled` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
enabled(cls) -> bool
```

Whether the service is enabled

#### `enabled_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L83" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
enabled_services(cls) -> list[type[Self]]
```

Get list of enabled service classes

#### `environment_variable_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L230" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
environment_variable_name(cls) -> str
```

#### `environment_variable_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
environment_variable_name(cls) -> str
```

#### `run_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L104" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_services(cls) -> NoReturn
```

Run enabled services until cancelled.

#### `running` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
running(cls) -> AsyncGenerator[None, None]
```

A context manager that runs enabled services on entry and stops them on
exit.

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L226" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

The Prefect setting that controls whether the service is enabled

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L237" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

Start running the service, which may run indefinitely

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/logs/stream.py#L249" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

Stop the service


Built with [Mintlify](https://mintlify.com).