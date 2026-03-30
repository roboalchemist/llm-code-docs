# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-services-event_logger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# event_logger

# `prefect.server.events.services.event_logger`

## Classes

### `EventLogger` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/services/event_logger.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A debugging service that logs events to the console as they arrive.

**Methods:**

#### `all_services` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
all_services(cls) -> Sequence[type[Self]]
```

Get list of all service classes

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

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/services/event_logger.py#L31" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

The Prefect setting that controls whether the service is enabled

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/services/event_logger.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

Start running the service, which may run indefinitely

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/services/event_logger.py#L66" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

Stop the service


Built with [Mintlify](https://mintlify.com).