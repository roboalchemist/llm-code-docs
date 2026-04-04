# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-models-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# cloud

# `prefect.settings.models.cloud`

## Functions

### `default_cloud_ui_url` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/cloud.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
default_cloud_ui_url(settings: 'CloudSettings') -> Optional[str]
```

## Classes

### `CloudSettings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/cloud.py#L31" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for interacting with Prefect Cloud

**Methods:**

#### `post_hoc_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/cloud.py#L59" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
post_hoc_settings(self) -> Self
```

refactor on resolution of [https://github.com/pydantic/pydantic/issues/9789](https://github.com/pydantic/pydantic/issues/9789)

we should not be modifying **pydantic\_fields\_set** directly, but until we can
define dependencies between defaults in a first-class way, we need clean up
post-hoc default assignments to keep set/unset fields correct after instantiation.

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