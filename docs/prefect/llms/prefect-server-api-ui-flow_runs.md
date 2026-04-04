# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-ui-flow_runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# flow_runs

# `prefect.server.api.ui.flow_runs`

## Functions

### `read_flow_run_history` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/flow_runs.py#L48" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_flow_run_history(sort: schemas.sorting.FlowRunSort = Body(schemas.sorting.FlowRunSort.EXPECTED_START_TIME_DESC), limit: int = Body(1000, le=1000), offset: int = Body(0, ge=0), flows: schemas.filters.FlowFilter = None, flow_runs: schemas.filters.FlowRunFilter = None, task_runs: schemas.filters.TaskRunFilter = None, deployments: schemas.filters.DeploymentFilter = None, work_pools: schemas.filters.WorkPoolFilter = None, db: PrefectDBInterface = Depends(provide_database_interface)) -> List[SimpleFlowRun]
```

### `count_task_runs_by_flow_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/flow_runs.py#L97" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
count_task_runs_by_flow_run(flow_run_ids: list[UUID] = Body(default=..., embed=True, max_items=200), db: PrefectDBInterface = Depends(provide_database_interface)) -> dict[UUID, int]
```

Get task run counts by flow run id.

## Classes

### `SimpleFlowRun` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/flow_runs.py#L27" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

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


Built with [Mintlify](https://mintlify.com).