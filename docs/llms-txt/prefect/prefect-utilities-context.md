# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# context

# `prefect.utilities.context`

## Functions

### `temporary_context` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/context.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_context(context: Context) -> Generator[None, Any, None]
```

### `get_task_run_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/context.py#L24" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_run_id() -> Optional[UUID]
```

### `get_flow_run_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/context.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_flow_run_id() -> Optional[UUID]
```

### `get_task_and_flow_run_ids` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/context.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_and_flow_run_ids() -> tuple[Optional[UUID], Optional[UUID]]
```

Get the task run and flow run ids from the context, if available.

**Returns:**

* tuple\[Optional\[UUID], Optional\[UUID]]: a tuple of the task run id and flow run id


Built with [Mintlify](https://mintlify.com).