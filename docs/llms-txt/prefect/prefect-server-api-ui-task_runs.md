# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-ui-task_runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_runs

# `prefect.server.api.ui.task_runs`

## Functions

### `read_dashboard_task_run_counts` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/task_runs.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_dashboard_task_run_counts(task_runs: schemas.filters.TaskRunFilter, flows: Optional[schemas.filters.FlowFilter] = None, flow_runs: Optional[schemas.filters.FlowRunFilter] = None, deployments: Optional[schemas.filters.DeploymentFilter] = None, work_pools: Optional[schemas.filters.WorkPoolFilter] = None, work_queues: Optional[schemas.filters.WorkQueueFilter] = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> List[TaskRunCount]
```

### `read_task_run_counts_by_state` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/task_runs.py#L163" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_run_counts_by_state(flows: Optional[schemas.filters.FlowFilter] = None, flow_runs: Optional[schemas.filters.FlowRunFilter] = None, task_runs: Optional[schemas.filters.TaskRunFilter] = None, deployments: Optional[schemas.filters.DeploymentFilter] = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.states.CountByState
```

### `read_task_run_with_flow_run_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/task_runs.py#L181" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_run_with_flow_run_name(task_run_id: UUID = Path(..., description='The task run id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.ui.UITaskRun
```

Get a task run by id.

## Classes

### `TaskRunCount` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/task_runs.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `model_validate_list` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
model_validate_list(cls, obj: Any) -> list[Self]
```

#### `reset_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset_fields(self: Self) -> Self
```

Reset the fields of the model that are in the `_reset_fields` set.

**Returns:**

* A new instance of the model with the reset fields.

#### `ser_model` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/task_runs.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ser_model(self) -> dict[str, int]
```


Built with [Mintlify](https://mintlify.com).