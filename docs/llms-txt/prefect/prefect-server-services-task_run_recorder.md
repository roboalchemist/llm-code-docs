# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-task_run_recorder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_run_recorder

# `prefect.server.services.task_run_recorder`

## Functions

### `task_run_from_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
task_run_from_event(event: ReceivedEvent) -> TaskRun
```

### `db_recordable_task_run_from_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L110" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
db_recordable_task_run_from_event(event: ReceivedEvent) -> tuple[TaskRun, dict[str, Any]]
```

### `record_task_run_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L141" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_task_run_event(event: ReceivedEvent, depth: int = 0) -> None
```

Record a single task run event in the database

### `record_bulk_task_run_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L185" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_bulk_task_run_events(events: list[ReceivedEvent]) -> None
```

Record multiple task run events in the database, taking advantage of bulk inserts.

### `handle_task_run_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L251" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handle_task_run_events(events: list[ReceivedEvent], depth: int = 0) -> None
```

### `record_lost_follower_task_run_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L279" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_lost_follower_task_run_events() -> None
```

### `periodically_process_followers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L296" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
periodically_process_followers(periodic_granularity: timedelta) -> NoReturn
```

Periodically process followers that are waiting on a leader event that never arrived

### `consumer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L321" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
consumer(write_batch_size: int, flush_every: int, max_persist_retries: int = DEFAULT_PERSIST_MAX_RETRIES) -> AsyncGenerator[MessageHandler, None]
```

## Classes

### `RetryableEvent` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L315" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `TaskRunRecorder` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L413" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Constructs task runs and states from client-emitted events

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

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L420" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

#### `service_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
service_settings(cls) -> ServicesBaseSetting
```

The Prefect setting that controls whether the service is enabled

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L437" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self, max_persist_retries: int = DEFAULT_PERSIST_MAX_RETRIES) -> NoReturn
```

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self) -> NoReturn
```

Start running the service, which may run indefinitely

#### `started_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L428" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
started_event(self) -> asyncio.Event
```

#### `started_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L434" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
started_event(self, value: asyncio.Event) -> None
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/task_run_recorder.py#L464" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/base.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

Stop the service


Built with [Mintlify](https://mintlify.com).