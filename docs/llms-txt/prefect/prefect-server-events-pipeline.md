# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# pipeline

# `prefect.server.events.pipeline`

## Classes

### `EventsPipeline` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/pipeline.py#L7" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `events_to_messages` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/pipeline.py#L9" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
events_to_messages(events: list[Event]) -> list[MemoryMessage]
```

#### `process_events` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/pipeline.py#L20" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
process_events(self, events: list[Event]) -> None
```

#### `process_message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/pipeline.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
process_message(self, message: MemoryMessage) -> None
```

Process a single event message

#### `process_messages` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/pipeline.py#L24" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
process_messages(self, messages: list[MemoryMessage]) -> None
```


Built with [Mintlify](https://mintlify.com).