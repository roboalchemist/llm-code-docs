# Source: https://docs.prefect.io/v3/api-ref/python/prefect-settings-legacy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# legacy

# `prefect.settings.legacy`

## Classes

### `Setting` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Mimics the old Setting object for compatibility with existing code.

**Methods:**

#### `default` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
default(self) -> Any
```

#### `is_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_secret(self) -> bool
```

#### `name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L31" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
name(self) -> str
```

#### `value` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
value(self: Self) -> Any
```

#### `value_from` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/settings/legacy.py#L61" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
value_from(self: Self, settings: Settings) -> Any
```


Built with [Mintlify](https://mintlify.com).