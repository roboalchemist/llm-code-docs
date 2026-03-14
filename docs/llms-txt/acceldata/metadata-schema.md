# Source: https://docs.acceldata.io/api/metadata-schema.md

# Metadata Schema

Returned by [Retrieve Asset Metadata](https://docs.acceldata.io/acceldata-data-observability-cloud/api/get-asset-metadata).

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| columns | array | List of column definitions | 


## Nested: columns[]

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| name | string | Column name | email | 
| dataType | string | Column type | string | 
| nullable | boolean | Whether null allowed | true | 
| comment | string | Column description | Customer email | 


## Example JSON

```json
{
  "columns": [
    { "name": "id", "dataType": "integer", "nullable": false },
    { "name": "email", "dataType": "string", "nullable": true }
  ]
}
```

