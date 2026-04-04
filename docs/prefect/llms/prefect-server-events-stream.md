# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-stream.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# stream

# `prefect.server.events.stream`

## Functions

### `subscribed` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
subscribed(filter: EventFilter) -> AsyncGenerator['Queue[ReceivedEvent]', None]
```

### `events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
events(filter: EventFilter) -> AsyncGenerator[AsyncIterable[Optional[ReceivedEvent]], None]
```

### `distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
distributor() -> AsyncGenerator[messaging.MessageHandler, None]
```

### `start_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L109" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_distributor() -> None
```

Starts the distributor consumer as a global background task

### `stop_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L121" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop_distributor() -> None
```

Stops the distributor consumer global background task

### `run_distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run_distributor(started: asyncio.Event) -> NoReturn
```

Runs the distributor consumer forever until it is cancelled

## Classes

### `Distributor` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L139" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `all_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
all_services(cls) -> Sequence[type[Self]]
```

Get list of all service classes

#### `enabled` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L151" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

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

#### `environment_variable_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L147" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
environment_variable_name(cls) -> dict[str, str]
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

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L143" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

The Prefect setting that controls whether the service is enabled

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L154" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> None
```

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

Start running the service, which may run indefinitely

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/stream.py#L164" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

Stop the service


Built with [Mintlify](https://mintlify.com).