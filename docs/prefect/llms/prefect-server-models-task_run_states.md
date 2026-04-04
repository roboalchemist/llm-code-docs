# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-task_run_states.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# task_run_states

# `prefect.server.models.task_run_states`

Functions for interacting with task run state ORM objects.
Intended for internal use by the Prefect REST API.

## Functions

### `read_task_run_state` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_run_states.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_run_state(db: PrefectDBInterface, session: AsyncSession, task_run_state_id: UUID) -> Union[orm_models.TaskRunState, None]
```

Reads a task run state by id.

**Args:**

* `session`: A database session
* `task_run_state_id`: a task run state id

**Returns:**

* orm\_models.TaskRunState: the task state

### `read_task_run_states` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_run_states.py#L34" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_task_run_states(db: PrefectDBInterface, session: AsyncSession, task_run_id: UUID) -> Sequence[orm_models.TaskRunState]
```

Reads task runs states for a task run.

**Args:**

* `session`: A database session
* `task_run_id`: the task run id

**Returns:**

* List\[orm\_models.TaskRunState]: the task run states

### `delete_task_run_state` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/task_run_states.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_task_run_state(db: PrefectDBInterface, session: AsyncSession, task_run_state_id: UUID) -> bool
```

Delete a task run state by id.

**Args:**

* `session`: A database session
* `task_run_state_id`: a task run state id

**Returns:**

* whether or not the task run state was deleted


Built with [Mintlify](https://mintlify.com).