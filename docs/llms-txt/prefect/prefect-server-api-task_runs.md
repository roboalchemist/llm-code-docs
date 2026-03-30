# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-task_runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_runs

# `prefect.server.api.task_runs`

Routes for interacting with task run objects.

## Functions

### `create_task_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L52" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_task_run(task_run: schemas.actions.TaskRunCreate, response: Response, db: PrefectDBInterface = Depends(provide_database_interface), orchestration_parameters: Dict[str, Any] = Depends(orchestration_dependencies.provide_task_orchestration_parameters)) -> schemas.core.TaskRun
```

Create a task run. If a task run with the same flow\_run\_id,
task\_key, and dynamic\_key already exists, the existing task
run will be returned.

If no state is provided, the task run will be created in a PENDING state.

For more information, see [https://docs.prefect.io/v3/concepts/tasks](https://docs.prefect.io/v3/concepts/tasks).

### `update_task_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_task_run(task_run: schemas.actions.TaskRunUpdate, task_run_id: UUID = Path(..., description='The task run id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

Updates a task run.

### `count_task_runs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L113" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_task_runs(db: PrefectDBInterface = Depends(provide_database_interface), flows: schemas.filters.FlowFilter = None, flow_runs: schemas.filters.FlowRunFilter = None, task_runs: schemas.filters.TaskRunFilter = None, deployments: schemas.filters.DeploymentFilter = None) -> int
```

Count task runs.

### `task_run_history` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
task_run_history(history_start: DateTime = Body(..., description="The history's start time."), history_end: DateTime = Body(..., description="The history's end time."), history_interval_seconds: float = Body(..., description='The size of each history interval, in seconds. Must be at least 1 second.', json_schema_extra={'format': 'time-delta'}), flows: schemas.filters.FlowFilter = None, flow_runs: schemas.filters.FlowRunFilter = None, task_runs: schemas.filters.TaskRunFilter = None, deployments: schemas.filters.DeploymentFilter = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> List[schemas.responses.HistoryResponse]
```

Query for task run history data across a given range and interval.

### `read_task_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L178" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_run(task_run_id: UUID = Path(..., description='The task run id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.core.TaskRun
```

Get a task run by id.

### `read_task_runs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L195" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_runs(sort: schemas.sorting.TaskRunSort = Body(schemas.sorting.TaskRunSort.ID_DESC), limit: int = dependencies.LimitBody(), offset: int = Body(0, ge=0), flows: Optional[schemas.filters.FlowFilter] = None, flow_runs: Optional[schemas.filters.FlowRunFilter] = None, task_runs: Optional[schemas.filters.TaskRunFilter] = None, deployments: Optional[schemas.filters.DeploymentFilter] = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> List[schemas.core.TaskRun]
```

Query for task runs.

### `paginate_task_runs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L222" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
paginate_task_runs(sort: schemas.sorting.TaskRunSort = Body(schemas.sorting.TaskRunSort.ID_DESC), limit: int = dependencies.LimitBody(), page: int = Body(1, ge=1), flows: Optional[schemas.filters.FlowFilter] = None, flow_runs: Optional[schemas.filters.FlowRunFilter] = None, task_runs: Optional[schemas.filters.TaskRunFilter] = None, deployments: Optional[schemas.filters.DeploymentFilter] = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> TaskRunPaginationResponse
```

Pagination query for task runs.

### `delete_task_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L274" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_task_run(docket: dependencies.Docket, task_run_id: UUID = Path(..., description='The task run id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> None
```

Delete a task run by id.

### `delete_task_run_logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L294" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_task_run_logs() -> None
```

### `set_task_run_state` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L310" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_task_run_state(task_run_id: UUID = Path(..., description='The task run id', alias='id'), state: schemas.actions.StateCreate = Body(..., description='The intended state.'), force: bool = Body(False, description='If false, orchestration rules will be applied that may alter or prevent the state transition. If True, orchestration rules are not applied.'), db: PrefectDBInterface = Depends(provide_database_interface), response: Response = None, task_policy: TaskRunOrchestrationPolicy = Depends(orchestration_dependencies.provide_task_policy), orchestration_parameters: Dict[str, Any] = Depends(orchestration_dependencies.provide_task_orchestration_parameters)) -> OrchestrationResult
```

Set a task run state, invoking any orchestration rules.

### `scheduled_task_subscription` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/task_runs.py#L358" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
scheduled_task_subscription(websocket: WebSocket) -> None
```


Built with [Mintlify](https://mintlify.com).