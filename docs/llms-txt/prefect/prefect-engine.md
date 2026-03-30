# Source: https://docs.prefect.io/v3/api-ref/python/prefect-engine.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# engine

# `prefect.engine`

## Functions

### `handle_engine_signals` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/engine.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handle_engine_signals(flow_run_id: UUID | None = None)
```

Handle signals from the orchestrator to abort or pause the flow run or otherwise
handle unexpected exceptions.

This context manager will handle exiting the process depending on the signal received.

**Args:**

* `flow_run_id`: The ID of the flow run to handle signals for.


Built with [Mintlify](https://mintlify.com).