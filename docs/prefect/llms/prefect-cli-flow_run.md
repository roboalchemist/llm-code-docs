# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-flow_run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# flow_run

# `prefect.cli.flow_run`

Flow run command — native cyclopts implementation.

Interact with flow runs.

## Functions

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L103" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(id: UUID)
```

View details about a flow run.

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L154" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls()
```

View recent flow runs or flow runs for specific flows.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L281" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(id: UUID)
```

Delete a flow run by ID.

### `cancel` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L301" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
cancel(id: UUID)
```

Cancel a flow run by ID.

### `retry` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L323" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
retry(id_or_name: str)
```

Retry a failed or completed flow run.

### `logs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L482" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
logs(id: UUID)
```

View logs for a flow run.

### `execute` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/flow_run.py#L601" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
execute(id: Optional[UUID] = None)
```

Execute a flow run by ID.


Built with [Mintlify](https://mintlify.com).