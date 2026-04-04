# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-flow_run_input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# flow_run_input

# `prefect.server.models.flow_run_input`

## Functions

### `create_flow_run_input` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/flow_run_input.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_flow_run_input(db: PrefectDBInterface, session: AsyncSession, flow_run_input: schemas.core.FlowRunInput) -> schemas.core.FlowRunInput
```

### `filter_flow_run_input` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/flow_run_input.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
filter_flow_run_input(db: PrefectDBInterface, session: AsyncSession, flow_run_id: uuid.UUID, prefix: str, limit: int, exclude_keys: List[str]) -> List[schemas.core.FlowRunInput]
```

### `read_flow_run_input` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/flow_run_input.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_flow_run_input(db: PrefectDBInterface, session: AsyncSession, flow_run_id: uuid.UUID, key: str) -> Optional[schemas.core.FlowRunInput]
```

### `delete_flow_run_input` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/flow_run_input.py#L76" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_flow_run_input(db: PrefectDBInterface, session: AsyncSession, flow_run_id: uuid.UUID, key: str) -> bool
```


Built with [Mintlify](https://mintlify.com).