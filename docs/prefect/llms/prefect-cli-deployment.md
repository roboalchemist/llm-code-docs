# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# deployment

# `prefect.cli.deployment`

Deployment command — native cyclopts implementation.

Manage deployments and deployment schedules.

## Functions

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L140" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(name: str)
```

View details about a deployment.

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L195" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls(flow_name: Annotated[Optional[list[str]], cyclopts.Parameter('flow_name', help='One or more flow names to filter deployments by.')] = None)
```

View all deployments or deployments for specific flows.

### `run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L279" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run(name: Annotated[Optional[str], cyclopts.Parameter('name', help="A deployed flow's name: <FLOW_NAME>/<DEPLOYMENT_NAME>")] = None)
```

Create a flow run for the given flow and deployment.

The flow run will be scheduled to run immediately unless `--start-in` or
`--start-at` is specified. The flow run will not execute until a worker
starts. To watch the flow run until it reaches a terminal state, use the
`--watch` flag.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L567" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(name: Annotated[Optional[str], cyclopts.Parameter('name', help="A deployed flow's name: <FLOW_NAME>/<DEPLOYMENT_NAME>")] = None)
```

Delete a deployment.

### `create_schedule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L647" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_schedule(name: str)
```

Create a schedule for a given deployment.

### `delete_schedule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L827" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_schedule(deployment_name: str, schedule_id: UUID)
```

Delete a deployment schedule.

### `pause_schedule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L989" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
pause_schedule(deployment_name: Annotated[Optional[str], cyclopts.Parameter('deployment_name')] = None, schedule_id: Annotated[Optional[UUID], cyclopts.Parameter('schedule_id')] = None)
```

Pause deployment schedules.

### `resume_schedule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L1017" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
resume_schedule(deployment_name: Annotated[Optional[str], cyclopts.Parameter('deployment_name')] = None, schedule_id: Annotated[Optional[UUID], cyclopts.Parameter('schedule_id')] = None)
```

Resume deployment schedules.

### `list_schedules` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L1045" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
list_schedules(deployment_name: str)
```

View all schedules for a deployment.

### `clear_schedules` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/deployment.py#L1114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_schedules(deployment_name: str)
```

Clear all schedules for a deployment.


Built with [Mintlify](https://mintlify.com).