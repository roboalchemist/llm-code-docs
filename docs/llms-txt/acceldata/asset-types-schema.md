# Source: https://docs.acceldata.io/api/asset-types-schema.md

# Asset Types Schema

Returned by [Asset Types](https://docs.acceldata.io/acceldata-data-observability-cloud/api/asset-types).

## Top-level Fields

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| id | integer | Asset type ID | 2 | 
| name | string | Asset type name | TABLE | 
| canProfile | boolean | Supports profiling | true | 
| canSample | boolean | Supports sampling | true | 
| canMonitor | boolean | Supports monitoring | true | 


## Example JSON

```json
{ 
  "id": 2, 
  "name": "TABLE", 
  "canProfile": true
}
```

