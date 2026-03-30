# Source: https://docs.prefect.io/v3/api-ref/python/prefect-types-names.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# names

# `prefect.types.names`

## Functions

### `raise_on_name_alphanumeric_dashes_only` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
raise_on_name_alphanumeric_dashes_only(value: str | None, field_name: str = 'value') -> str | None
```

### `raise_on_name_alphanumeric_underscores_only` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L50" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
raise_on_name_alphanumeric_underscores_only(value: str | None, field_name: str = 'value') -> str | None
```

### `raise_on_name_alphanumeric_dashes_underscores_only` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L63" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
raise_on_name_alphanumeric_dashes_underscores_only(value: str, field_name: str = 'value') -> str
```

### `non_emptyish` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L83" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
non_emptyish(value: str) -> str
```

### `validate_uri` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L146" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate_uri(value: str) -> str
```

Validate that a string is a valid URI with lowercase protocol.

### `validate_valid_asset_key` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/types/names.py#L192" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate_valid_asset_key(value: str) -> str
```

Validate asset key with character restrictions and length limit.


Built with [Mintlify](https://mintlify.com).