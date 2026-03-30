# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-schema_tools-validation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# validation

# `prefect.utilities.schema_tools.validation`

## Functions

### `is_valid_schema` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L65" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_valid_schema(schema: ObjectSchema, preprocess: bool = True) -> None
```

### `validate` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L74" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate(obj: dict[str, Any], schema: ObjectSchema, raise_on_error: bool = False, preprocess: bool = True, ignore_required: bool = False, allow_none_with_default: bool = False) -> list[JSONSchemaValidationError]
```

### `is_valid` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L112" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
is_valid(obj: dict[str, Any], schema: ObjectSchema) -> bool
```

### `prioritize_placeholder_errors` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L117" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
prioritize_placeholder_errors(errors: list[JSONSchemaValidationError]) -> list[JSONSchemaValidationError]
```

### `build_error_obj` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L141" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build_error_obj(errors: list[JSONSchemaValidationError]) -> dict[str, Any]
```

### `process_properties` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L232" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
process_properties(properties: dict[str, dict[str, Any]], required_fields: list[str], allow_none_with_default: bool = False) -> None
```

### `preprocess_schema` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L246" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
preprocess_schema(schema: ObjectSchema, allow_none_with_default: bool = False) -> ObjectSchema
```

## Classes

### `CircularSchemaRefError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L18" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `ValidationError` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/schema_tools/validation.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).