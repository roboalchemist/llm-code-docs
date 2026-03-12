# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# profiles

# `prefect.settings.profiles`

## Functions

### `load_profiles` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L303" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
load_profiles(include_defaults: bool = True) -> ProfilesCollection
```

Load profiles from the current profile path. Optionally include profiles from the
default profile path.

### `load_current_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L342" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
load_current_profile() -> Profile
```

Load the current profile from the default and current profile paths.

This will *not* include settings from the current settings context. Only settings
that have been persisted to the profiles file will be saved.

### `save_profiles` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L360" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
save_profiles(profiles: ProfilesCollection) -> None
```

Writes all non-default profiles to the current profiles path.

### `load_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L370" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
load_profile(name: str) -> Profile
```

Load a single profile by name.

### `update_current_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L381" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_current_profile(settings: dict[str | Setting, Any]) -> Profile
```

Update the persisted data for the profile currently in-use.

If the profile does not exist in the profiles file, it will be created.

Given settings will be merged with the existing settings as described in
`ProfilesCollection.update_profile`.

**Returns:**

* The new profile.

## Classes

### `Profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A user profile containing settings.

**Methods:**

#### `to_environment_variables` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
to_environment_variables(self) -> dict[str, str]
```

Convert the profile settings to a dictionary of environment variables.

#### `validate_settings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L77" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate_settings(self) -> None
```

Validate all settings in this profile by creating a partial Settings object
with the nested structure properly constructed using accessor paths.

### `ProfilesCollection` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L114" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

"
A utility class for working with a collection of profiles.

Profiles in the collection must have unique names.

The collection may store the name of the active profile.

**Methods:**

#### `active_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L137" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
active_profile(self) -> Profile | None
```

Retrieve the active profile in this collection.

#### `add_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L197" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
add_profile(self, profile: Profile) -> None
```

Add a profile to the collection.

If the profile name already exists, an exception will be raised.

#### `items` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L249" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
items(self) -> list[tuple[str, Profile]]
```

#### `names` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L130" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
names(self) -> set[str]
```

Return a set of profile names in this collection.

#### `remove_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L210" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
remove_profile(self, name: str) -> None
```

Remove a profile from the collection.

#### `set_active` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L145" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
set_active(self, name: str | None, check: bool = True) -> None
```

Set the active profile name in the collection.

A null value may be passed to indicate that this collection does not determine
the active profile.

#### `to_dict` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L231" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
to_dict(self) -> dict[str, Any]
```

Convert to a dictionary suitable for writing to disk.

#### `update_profile` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L156" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_profile(self, name: str, settings: dict[Setting, Any], source: Path | None = None) -> Profile
```

Add a profile to the collection or update the existing on if the name is already
present in this collection.

If updating an existing profile, the settings will be merged. Settings can
be dropped from the existing profile by setting them to `None` in the new
profile.

Returns the new profile object.

#### `without_profile_source` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/profiles.py#L216" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
without_profile_source(self, path: Path | None) -> 'ProfilesCollection'
```

Remove profiles that were loaded from a given path.

Returns a new collection.


Built with [Mintlify](https://mintlify.com).