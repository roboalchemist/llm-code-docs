# Source: https://docs.acceldata.io/api/related-child-asset-schema.md

# Related Child Asset Schema

Returned by [Retrieve Child Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/api/retrieve-child-assets).

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| data | array | List of child asset objects | 
| meta | object | Pagination info | 


## Example JSON

```json
{ 
  "data": 
  	[
      { "id": 1002, 
       "name": "orders" 
      }
    ], 
  "meta": 
  	{ "total": 1 
    } 
}
```

