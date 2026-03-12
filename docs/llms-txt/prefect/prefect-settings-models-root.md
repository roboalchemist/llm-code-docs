# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-models-root.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# root

# `prefect.settings.models.root`

## Functions

### `canonical_environment_prefix` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L390" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
canonical_environment_prefix(settings: 'Settings') -> str
```

## Classes

### `Settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Settings for Prefect using Pydantic settings.

See [https://docs.pydantic.dev/latest/concepts/pydantic\_settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings)

**Methods:**

#### `connected_to_cloud` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L256" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
connected_to_cloud(self) -> bool
```

True when the API URL points at the configured Prefect Cloud API.

#### `copy_with_update` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L267" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
copy_with_update(self: Self, updates: Optional[Mapping['Setting', Any]] = None, set_defaults: Optional[Mapping['Setting', Any]] = None, restore_defaults: Optional[Iterable['Setting']] = None) -> Self
```

Create a new Settings object with validation.

**Args:**

* `updates`: A mapping of settings to new values. Existing values for the
  given settings will be overridden.
* `set_defaults`: A mapping of settings to new default values. Existing values for
  the given settings will only be overridden if they were not set.
* `restore_defaults`: An iterable of settings to restore to their default values.

**Returns:**

* A new Settings object.

#### `emit_warnings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L249" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
emit_warnings(self) -> Self
```

More post-hoc validation of settings, including warnings for misconfigurations.

#### `hash_key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L338" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
hash_key(self) -> str
```

Return a hash key for the settings object.  This is needed since some
settings may be unhashable, like lists.

#### `post_hoc_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/models/root.py#L187" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
post_hoc_settings(self) -> Self
```

Handle remaining complex default assignments that aren't yet migrated to dependent settings.

With Pydantic 2.10's dependent settings feature, we've migrated simple path-based defaults
to use default\_factory. The remaining items here require access to the full Settings instance
or have complex interdependencies that will be migrated in future PRs.

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