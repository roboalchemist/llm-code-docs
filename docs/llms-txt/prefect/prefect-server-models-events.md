# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# events

# `prefect.server.models.events`

## Functions

### `flow_run_state_change_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
flow_run_state_change_event(session: AsyncSession, occurred: datetime, flow_run: ORMFlowRun, initial_state_id: Optional[UUID], initial_state: Optional[schemas.states.State], validated_state_id: Optional[UUID], validated_state: schemas.states.State) -> Event
```

### `state_payload` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L262" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
state_payload(state: Optional[schemas.states.State]) -> Optional[Dict[str, str]]
```

Given a State, return the essential string parts of it for use in an
event payload

### `deployment_status_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L294" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
deployment_status_event(session: AsyncSession, deployment_id: UUID, status: DeploymentStatus, occurred: DateTime) -> Event
```

### `work_queue_status_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L365" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
work_queue_status_event(session: AsyncSession, work_queue: 'ORMWorkQueue', occurred: DateTime) -> Event
```

### `work_pool_status_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L401" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
work_pool_status_event(event_id: UUID, occurred: DateTime, pre_update_work_pool: Optional['ORMWorkPool'], work_pool: 'ORMWorkPool') -> Event
```

### `work_pool_updated_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L422" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
work_pool_updated_event(session: AsyncSession, work_pool: 'ORMWorkPool', changed_fields: Dict[str, Dict[str, Any]], occurred: DateTime) -> Event
```

Create an event for work pool field updates (non-status).

### `work_queue_updated_event` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/events.py#L448" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
work_queue_updated_event(session: AsyncSession, work_queue: 'ORMWorkQueue', changed_fields: Dict[str, Dict[str, Any]], occurred: DateTime) -> Event
```

Create an event for work queue field updates (non-status).


Built with [Mintlify](https://mintlify.com).