# Source: https://docs.prefect.io/v3/api-ref/python/prefect-assets-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# core

# `prefect.assets.core`

## Functions

### `add_asset_metadata` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/assets/core.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
add_asset_metadata(asset: str | Asset, metadata: dict[str, Any]) -> None
```

## Classes

### `AssetProperties` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/assets/core.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Metadata properties to configure on an Asset

**Methods:**

#### `model_validate_list` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
model_validate_list(cls, obj: Any) -> list[Self]
```

#### `reset_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset_fields(self: Self) -> Self
```

Reset the fields of the model that are in the `_reset_fields` set.

**Returns:**

* A new instance of the model with the reset fields.

### `Asset` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/assets/core.py#L36" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Assets are objects that represent materialized data,
providing a way to track lineage and dependencies.

**Methods:**

#### `add_metadata` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/assets/core.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
add_metadata(self, metadata: dict[str, Any]) -> None
```

#### `model_validate_list` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
model_validate_list(cls, obj: Any) -> list[Self]
```

#### `reset_fields` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/_internal/schemas/bases.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reset_fields(self: Self) -> Self
```

Reset the fields of the model that are in the `_reset_fields` set.

**Returns:**

* A new instance of the model with the reset fields.


Built with [Mintlify](https://mintlify.com).