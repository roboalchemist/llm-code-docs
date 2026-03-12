# Source: https://docs.prefect.io/v3/api-ref/python/prefect-runtime-task_run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_run

# `prefect.runtime.task_run`

Access attributes of the current task run dynamically.

Note that if a task run cannot be discovered, all attributes will return empty values.

You can mock the runtime attributes for testing purposes by setting environment variables
prefixed with `PREFECT__RUNTIME__TASK_RUN`.

Available attributes:

* `id`: the task run's unique ID
* `name`: the name of the task run
* `tags`: the task run's set of tags
* `parameters`: the parameters the task was called with
* `run_count`: the number of times this task run has been run
* `task_name`: the name of the task

## Functions

### `get_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_id() -> str | None
```

### `get_tags` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L95" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_tags() -> list[str]
```

### `get_run_count` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_run_count() -> int
```

### `get_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L111" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_name() -> str | None
```

### `get_task_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L119" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_name() -> str | None
```

### `get_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L127" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_parameters() -> dict[str, Any]
```

### `get_task_run_api_url` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L135" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_run_api_url() -> str | None
```

### `get_task_run_ui_url` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/runtime/task_run.py#L143" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_task_run_ui_url() -> str | None
```


Built with [Mintlify](https://mintlify.com).