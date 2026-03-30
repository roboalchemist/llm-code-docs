# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-models-logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# logging

# `prefect.settings.models.logging`

## Functions

### `max_log_size_smaller_than_batch_size` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/logging.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
max_log_size_smaller_than_batch_size(values: dict[str, Any]) -> dict[str, Any]
```

Validator for settings asserting the batch size and match log size are compatible

## Classes

### `LoggingToAPISettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/logging.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling logging to the API

**Methods:**

#### `emit_warnings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/logging.py#L84" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit_warnings(self) -> Self
```

Emits warnings for misconfiguration of logging settings.

#### `settings_customise_sources` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/base.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
settings_customise_sources(cls, settings_cls: type[BaseSettings], init_settings: PydanticBaseSettingsSource, env_settings: PydanticBaseSettingsSource, dotenv_settings: PydanticBaseSettingsSource, file_secret_settings: PydanticBaseSettingsSource) -> tuple[PydanticBaseSettingsSource, ...]
```

Define an order for Prefect settings sources.

The order of the returned callables decides the priority of inputs; first item is the highest priority.

See [https://docs.pydantic.dev/latest/concepts/pydantic\_settings/#customise-settings-sources](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources)

#### `to_environment_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/base.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
to_environment_variables(self, exclude_unset: bool = False, include_secrets: bool = True, include_aliases: bool = False) -> dict[str, str]
```

Convert the settings object to a dictionary of environment variables.

### `LoggingSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/logging.py#L91" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling logging behavior

**Methods:**

#### `settings_customise_sources` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/base.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
settings_customise_sources(cls, settings_cls: type[BaseSettings], init_settings: PydanticBaseSettingsSource, env_settings: PydanticBaseSettingsSource, dotenv_settings: PydanticBaseSettingsSource, file_secret_settings: PydanticBaseSettingsSource) -> tuple[PydanticBaseSettingsSource, ...]
```

Define an order for Prefect settings sources.

The order of the returned callables decides the priority of inputs; first item is the highest priority.

See [https://docs.pydantic.dev/latest/concepts/pydantic\_settings/#customise-settings-sources](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources)

#### `to_environment_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/base.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
to_environment_variables(self, exclude_unset: bool = False, include_secrets: bool = True, include_aliases: bool = False) -> dict[str, str]
```

Convert the settings object to a dictionary of environment variables.


Built with [Mintlify](https://mintlify.com).