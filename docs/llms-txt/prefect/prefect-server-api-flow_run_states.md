# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-flow_run_states.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# flow_run_states

# `prefect.server.api.flow_run_states`

Routes for interacting with flow run state objects.

## Functions

### `read_flow_run_state` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/flow_run_states.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_flow_run_state(flow_run_state_id: UUID = Path(..., description='The flow run state id', alias='id'), db: PrefectDBInterface = Depends(provide_database_interface)) -> schemas.states.State
```

Get a flow run state by id.

For more information, see [https://docs.prefect.io/v3/concepts/flows#final-state-determination](https://docs.prefect.io/v3/concepts/flows#final-state-determination).

### `read_flow_run_states` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/flow_run_states.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_flow_run_states(flow_run_id: UUID, db: PrefectDBInterface = Depends(provide_database_interface)) -> List[schemas.states.State]
```

Get states associated with a flow run.


Built with [Mintlify](https://mintlify.com).