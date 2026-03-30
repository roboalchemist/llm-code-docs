# Source: https://docs.prefect.io/v3/api-ref/python/prefect-task_worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_worker

# `prefect.task_worker`

## Functions

### `should_try_to_read_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
should_try_to_read_parameters(task: Task[P, R], task_run: TaskRun) -> bool
```

Determines whether a task run should read parameters from the result store.

### `create_status_server` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L427" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_status_server(task_worker: TaskWorker) -> FastAPI
```

### `aserve` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L452" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aserve(*tasks: Task[P, R]) -> None
```

Serve the provided tasks so that their runs may be submitted to
and executed in the engine. Tasks do not need to be within a flow run context to be
submitted. You must `.submit` the same task object that you pass to `serve`.

**Args:**

* `- tasks`: A list of tasks to serve. When a scheduled task run is found for a
  given task, the task run will be submitted to the engine for execution.
* `- limit`: The maximum number of tasks that can be run concurrently. Defaults to 10.
  Pass `None` to remove the limit.
* `- status_server_port`: An optional port on which to start an HTTP server
  exposing status information about the task worker. If not provided, no
  status server will run.
* `- timeout`: If provided, the task worker will exit after the given number of
  seconds. Defaults to None, meaning the task worker will run indefinitely.

### `serve` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L555" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
serve(*tasks: Task[P, R]) -> None
```

Serve the provided tasks so that their runs may be submitted to
and executed in the engine. Tasks do not need to be within a flow run context to be
submitted. You must `.submit` the same task object that you pass to `serve`.

**Args:**

* `- tasks`: A list of tasks to serve. When a scheduled task run is found for a
  given task, the task run will be submitted to the engine for execution.
* `- limit`: The maximum number of tasks that can be run concurrently. Defaults to 10.
  Pass `None` to remove the limit.
* `- status_server_port`: An optional port on which to start an HTTP server
  exposing status information about the task worker. If not provided, no
  status server will run.
* `- timeout`: If provided, the task worker will exit after the given number of
  seconds. Defaults to None, meaning the task worker will run indefinitely.

### `store_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L604" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
store_parameters(result_store: ResultStore, identifier: UUID, parameters: dict[str, Any]) -> None
```

Store parameters for a task run in the result store.

**Args:**

* `result_store`: The result store to store the parameters in.
* `identifier`: The identifier of the task run.
* `parameters`: The parameters to store.

### `read_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L633" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_parameters(result_store: ResultStore, identifier: UUID) -> dict[str, Any]
```

Read parameters for a task run from the result store.

**Args:**

* `result_store`: The result store to read the parameters from.
* `identifier`: The identifier of the task run.

**Returns:**

* The parameters for the task run.

## Classes

### `StopTaskWorker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L62" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Raised when the task worker is stopped.

### `TaskWorker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

This class is responsible for serving tasks that may be executed in the background
by a task runner via the traditional engine machinery.

When `start()` is called, the task worker will open a websocket connection to a
server-side queue of scheduled task runs. When a scheduled task run is found, the
scheduled task run is submitted to the engine for execution with a minimal `EngineContext`
so that the task run can be governed by orchestration rules.

**Args:**

* `- tasks`: A list of tasks to serve. These tasks will be submitted to the engine
  when a scheduled task run is found.
* `- limit`: The maximum number of tasks that can be run concurrently. Defaults to 10.
  Pass `None` to remove the limit.

**Methods:**

#### `astart` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L177" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
astart(self, timeout: Optional[float] = None) -> None
```

Starts a task worker, which runs the tasks provided in the constructor.

**Args:**

* `timeout`: If provided, the task worker will exit after the given number of
  seconds. Defaults to None, meaning the task worker will run indefinitely.

#### `astop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L219" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
astop(self) -> None
```

Stops the task worker's polling cycle.

#### `available_tasks` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L165" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
available_tasks(self) -> Optional[int]
```

#### `client_id` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L141" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
client_id(self) -> str
```

#### `current_tasks` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L157" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
current_tasks(self) -> Optional[int]
```

#### `execute_task_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L399" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
execute_task_run(self, task_run: TaskRun) -> None
```

Execute a task run in the task worker.

#### `handle_sigterm` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L168" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handle_sigterm(self, signum: int, frame: object) -> None
```

Shuts down the task worker when a SIGTERM is received.

#### `limit` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L153" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
limit(self) -> Optional[int]
```

#### `start` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L207" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start(self, timeout: Optional[float] = None) -> None
```

Starts a task worker, which runs the tasks provided in the constructor.

**Args:**

* `timeout`: If provided, the task worker will exit after the given number of
  seconds. Defaults to None, meaning the task worker will run indefinitely.

#### `started` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L149" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
started(self) -> bool
```

#### `started_at` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L145" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
started_at(self) -> Optional[DateTime]
```

#### `stop` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/task_worker.py#L233" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop(self) -> None
```

Stops the task worker's polling cycle.


Built with [Mintlify](https://mintlify.com).