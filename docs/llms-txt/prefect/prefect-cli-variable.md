# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# variable

# `prefect.cli.variable`

Variable command — native cyclopts implementation.

Manage Prefect variables.

## Functions

### `list_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/variable.py#L39" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
list_variables()
```

List variables.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/variable.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(name: str)
```

View details about a variable.

### `get` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/variable.py#L138" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get(name: str)
```

Get a variable's value.

### `unset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/variable.py#L191" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
unset(name: str)
```

Unset a variable.


Built with [Mintlify](https://mintlify.com).