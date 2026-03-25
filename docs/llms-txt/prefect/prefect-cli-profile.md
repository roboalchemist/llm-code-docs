# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# profile

# `prefect.cli.profile`

Profile command — native cyclopts implementation.

Manages Prefect profiles.

## Functions

### `ls` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ls()
```

List profile names.

### `create` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create(name: str)
```

Create a new profile.

### `use` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L118" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
use(name: str)
```

Set the given profile to active.

### `delete` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L190" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete(name: str)
```

Delete the given profile.

### `rename` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L219" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
rename(name: str, new_name: str)
```

Change the name of a profile.

### `inspect` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L249" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
inspect(name: Annotated[Optional[str], cyclopts.Parameter(help='Name of profile to inspect; defaults to active.')] = None)
```

Display settings from a given profile; defaults to active.

### `populate_defaults` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L300" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
populate_defaults()
```

Populate the profiles configuration with default base profiles,
preserving existing user profiles.

### `check_server_connection` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L389" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
check_server_connection() -> ConnectionStatus
```

## Classes

### `ConnectionStatus` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/profile.py#L378" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `auto` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/collections.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
auto() -> str
```

Exposes `enum.auto()` to avoid requiring a second import to use `AutoEnum`


Built with [Mintlify](https://mintlify.com).