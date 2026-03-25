# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-api-ui-schemas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# schemas

# `prefect.server.api.ui.schemas`

## Functions

### `validate_obj` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/api/ui/schemas.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate_obj(json_schema: dict[str, Any] = Body(..., embed=True, alias='schema', validation_alias='schema', json_schema_extra={'additionalProperties': True}), values: dict[str, Any] = Body(..., embed=True, json_schema_extra={'additionalProperties': True}), db: PrefectDBInterface = Depends(provide_database_interface)) -> SchemaValuesValidationResponse
```


Built with [Mintlify](https://mintlify.com).