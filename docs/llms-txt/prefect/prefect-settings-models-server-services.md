# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-models-server-services.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# services

# `prefect.settings.models.server.services`

## Classes

### `ServicesBaseSetting` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

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

### `ServerServicesCancellationCleanupSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the cancellation cleanup service

### `ServerServicesDBVacuumSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L48" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the database vacuum service

### `ServerServicesEventPersisterSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the event persister service

### `ServerServicesEventLoggerSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L156" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the event logger service

### `ServerServicesForemanSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L176" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the foreman service

### `ServerServicesLateRunsSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L257" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the late runs service

### `ServerServicesSchedulerSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L301" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the scheduler service

### `ServerServicesPauseExpirationsSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L433" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the pause expiration service

### `ServerServicesRepossessorSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L469" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the repossessor service

### `ServerServicesTaskRunRecorderSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L489" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the task run recorder service

### `ServerServicesTriggersSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L527" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling the triggers service

### `ServerServicesSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/server/services.py#L579" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for controlling server services

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