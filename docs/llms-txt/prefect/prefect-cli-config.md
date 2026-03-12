# Source: https://docs.prefect.io/v3/api-ref/python/prefect-cli-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# config

# `prefect.cli.config`

Config command — native cyclopts implementation.

Manages Prefect settings and profiles.

## Functions

### `set_` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/config.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_(settings: Annotated[list[str], cyclopts.Parameter(help='Settings in VAR=VAL format')]) -> None
```

Change the value for a setting by setting the value in the current profile.

### `validate` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/config.py#L89" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate() -> None
```

Read and validate the current profile.

Deprecated settings will be automatically converted to new names.

### `unset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/config.py#L105" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
unset(setting_names: Annotated[list[str], cyclopts.Parameter(help='Setting names to unset')]) -> None
```

Restore the default value for a setting.

Removes the setting from the current profile.

### `view` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/cli/config.py#L161" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
view() -> None
```

Display the current settings.


Built with [Mintlify](https://mintlify.com).