# Source: https://docs.prefect.io/v3/api-ref/python/prefect-events-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# worker

# `prefect.events.worker`

## Functions

### `should_emit_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
should_emit_events() -> bool
```

### `emit_events_to_cloud` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L48" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit_events_to_cloud() -> bool
```

### `should_emit_events_to_running_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
should_emit_events_to_running_server() -> bool
```

### `should_emit_events_to_ephemeral_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
should_emit_events_to_ephemeral_server() -> bool
```

## Classes

### `ProcessPoolForwardingEventsClient` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

An events client that forwards events to a parent process queue.

**Methods:**

#### `client_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/clients.py#L165" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
client_name(self) -> str
```

#### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/clients.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(self, event: Event) -> None
```

Emit a single event

### `EventsWorker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `attach_related_resources_from_context` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
attach_related_resources_from_context(self, event: Event) -> None
```

#### `instance` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L125" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
instance(cls: Type[Self], client_type: Optional[Type[EventsClient]] = None) -> Self
```

#### `set_client_override` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/events/worker.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_client_override(cls, client_type: Optional[Type[EventsClient]], **client_kwargs: Any) -> None
```


Built with [Mintlify](https://mintlify.com).