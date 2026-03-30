# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# events

# `prefect.cli.events`

Events command — native cyclopts implementation.

Stream and emit events.

## Functions

### `stream` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/events.py#L30" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stream()
```

Subscribe to the event stream, printing each event as it is received.

### `emit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/events.py#L112" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit(event: str)
```

Emit a single event to Prefect.


Built with [Mintlify](https://mintlify.com).