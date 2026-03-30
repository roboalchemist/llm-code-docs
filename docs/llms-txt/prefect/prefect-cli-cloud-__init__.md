# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-cloud-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.cli.cloud`

Cloud command — authenticate and interact with Prefect Cloud.

## Functions

### `login` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/cloud/__init__.py#L55" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
login()
```

Log in to Prefect Cloud.
Creates a new profile configured to use the specified PREFECT\_API\_KEY.
Uses a previously configured profile if it exists.

### `logout` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/cloud/__init__.py#L283" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
logout()
```

Logout the current workspace.
Reset PREFECT\_API\_KEY and PREFECT\_API\_URL to default.

### `workspace_ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/cloud/__init__.py#L316" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
workspace_ls()
```

List available workspaces.

### `workspace_set` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/cloud/__init__.py#L350" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
workspace_set()
```

Set current workspace. Shows a workspace picker if no workspace is specified.


Built with [Mintlify](https://mintlify.com).