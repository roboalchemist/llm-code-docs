# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-ordering-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.server.events.ordering`

Manages the partial causal ordering of events for a particular consumer.  This module
maintains a buffer of events to be processed, aiming to process them in the order they
occurred causally.

## Functions

### `get_triggers_causal_ordering` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L90" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_triggers_causal_ordering() -> CausalOrdering
```

### `get_task_run_recorder_causal_ordering` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L102" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_run_recorder_causal_ordering() -> CausalOrdering
```

## Classes

### `CausalOrderingModule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `EventArrivedEarly` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `MaxDepthExceeded` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L51" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `event_handler` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `CausalOrdering` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L62" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `event_has_been_seen` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L67" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
event_has_been_seen(self, event: Union[UUID, Event]) -> bool
```

#### `forget_follower` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L76" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
forget_follower(self, follower: ReceivedEvent) -> None
```

#### `get_followers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L79" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_followers(self, leader: ReceivedEvent) -> List[ReceivedEvent]
```

#### `get_lost_followers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_lost_followers(self) -> List[ReceivedEvent]
```

#### `preceding_event_confirmed` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
preceding_event_confirmed(self, handler: event_handler, event: ReceivedEvent, depth: int = 0) -> AsyncContextManager[None]
```

#### `record_event_as_seen` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_event_as_seen(self, event: ReceivedEvent) -> None
```

#### `record_follower` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/__init__.py#L73" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_follower(self, event: ReceivedEvent) -> None
```


Built with [Mintlify](https://mintlify.com).