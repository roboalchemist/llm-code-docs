# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-task_queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_queue

# `prefect.server.task_queue`

Implements an in-memory task queue for delivering background task runs to TaskWorkers.

## Classes

### `TaskQueue` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L17" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `configure_task_key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
configure_task_key(cls, task_key: str, scheduled_size: Optional[int] = None, retry_size: Optional[int] = None) -> None
```

#### `enqueue` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
enqueue(cls, task_run: schemas.core.TaskRun) -> None
```

#### `for_key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
for_key(cls, task_key: str) -> Self
```

#### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L66" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(self) -> schemas.core.TaskRun
```

#### `get_nowait` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L73" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_nowait(self) -> schemas.core.TaskRun
```

#### `put` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
put(self, task_run: schemas.core.TaskRun) -> None
```

#### `reset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset(cls) -> None
```

A unit testing utility to reset the state of the task queues subsystem

#### `retry` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L83" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
retry(self, task_run: schemas.core.TaskRun) -> None
```

### `MultiQueue` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L87" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A queue that can pull tasks from from any of a number of task queues

**Methods:**

#### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/task_queue.py#L95" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(self) -> schemas.core.TaskRun
```

Gets the next task\_run from any of the given queues


Built with [Mintlify](https://mintlify.com).