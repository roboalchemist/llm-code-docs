# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# automation

# `prefect.cli.automation`

Automation command — native cyclopts implementation.

Manage automations.

## Functions

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls()
```

List all automations.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L96" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(name: Annotated[Optional[str], cyclopts.Parameter(show=False)] = None)
```

Inspect an automation.

### `resume` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L174" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
resume(name: Annotated[Optional[str], cyclopts.Parameter(show=False)] = None)
```

Resume an automation.

### `pause` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L225" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
pause(name: Annotated[Optional[str], cyclopts.Parameter(show=False)] = None)
```

Pause an automation.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L276" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(name: Annotated[Optional[str], cyclopts.Parameter(show=False)] = None)
```

Delete an automation.

### `create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L370" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create()
```

Create one or more automations from a file or JSON string.

### `update` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/automation.py#L466" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update()
```

Update an existing automation from a file or JSON string.


Built with [Mintlify](https://mintlify.com).