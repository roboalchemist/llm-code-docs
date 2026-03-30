# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# context

# `prefect.settings.context`

## Functions

### `get_current_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/context.py#L10" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_current_settings() -> Settings
```

Returns a settings object populated with values from the current settings context
or, if no settings context is active, the environment.

### `temporary_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/context.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_settings(updates: Optional[Mapping['Setting', Any]] = None, set_defaults: Optional[Mapping['Setting', Any]] = None, restore_defaults: Optional[Iterable['Setting']] = None) -> Generator[Settings, None, None]
```

Temporarily override the current settings by entering a new profile.

See `Settings.copy_with_update` for details on different argument behavior.

Examples:

```python  theme={null}
from prefect.settings import PREFECT_API_URL

with temporary_settings(updates={PREFECT_API_URL: "foo"}):
   assert PREFECT_API_URL.value() == "foo"

   with temporary_settings(set_defaults={PREFECT_API_URL: "bar"}):
        assert PREFECT_API_URL.value() == "foo"

   with temporary_settings(restore_defaults={PREFECT_API_URL}):
        assert PREFECT_API_URL.value() is None

        with temporary_settings(set_defaults={PREFECT_API_URL: "bar"})
            assert PREFECT_API_URL.value() == "bar"
assert PREFECT_API_URL.value() is None
```


Built with [Mintlify](https://mintlify.com).