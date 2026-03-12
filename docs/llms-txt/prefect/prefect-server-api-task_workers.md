# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-task_workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_workers

# `prefect.server.api.task_workers`

## Functions

### `read_task_workers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_workers.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_workers(task_worker_filter: Optional[TaskWorkerFilter] = Body(default=None, description='The task worker filter', embed=True)) -> List[TaskWorkerResponse]
```

Read active task workers. Optionally filter by task keys.

For more information, see [https://docs.prefect.io/v3/how-to-guides/workflows/run-background-tasks](https://docs.prefect.io/v3/how-to-guides/workflows/run-background-tasks).

## Classes

### `TaskWorkerFilter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_workers.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).