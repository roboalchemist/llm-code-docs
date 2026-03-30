# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-task_workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_workers

# `prefect.server.models.task_workers`

## Functions

### `observe_worker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
observe_worker(task_keys: List[TaskKey], worker_id: WorkerId) -> None
```

### `forget_worker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L93" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
forget_worker(worker_id: WorkerId) -> None
```

### `get_workers_for_task_keys` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L99" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_workers_for_task_keys(task_keys: List[TaskKey]) -> List[TaskWorkerResponse]
```

### `get_all_workers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L105" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_all_workers() -> List[TaskWorkerResponse]
```

## Classes

### `TaskWorkerResponse` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `InMemoryTaskWorkerTracker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `forget_worker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
forget_worker(self, worker_id: WorkerId) -> None
```

#### `get_all_workers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_all_workers(self) -> List[TaskWorkerResponse]
```

#### `get_workers_for_task_keys` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L51" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_workers_for_task_keys(self, task_keys: List[TaskKey]) -> List[TaskWorkerResponse]
```

#### `observe_worker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
observe_worker(self, task_keys: List[TaskKey], worker_id: WorkerId) -> None
```

#### `reset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_workers.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset(self) -> None
```

Testing utility to reset the state of the task worker tracker


Built with [Mintlify](https://mintlify.com).