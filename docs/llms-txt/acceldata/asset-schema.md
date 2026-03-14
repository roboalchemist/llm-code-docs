# Source: https://docs.acceldata.io/api/asset-schema.md

# Asset Schema

Returned by:

- [Discover Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/api/discover-assets)
- [Search Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/api/search-assets)
- [Get Asset by ID or UID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/get-asset-by-id-or-uid)

## Top-level Fields

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| id | integer | Internal system ID | 12616 | 
| uid | string | Unique identifier | sales.customer_table | 
| name | string | Display name | customer_orders | 
| parentId | integer | Parent asset ID | 1001 | 
| assemblyId | integer | Source/assembly ID | 5 | 
| isCustom | boolean | User-created asset flag | false | 
| isDeleted | boolean | Asset deletion status | false | 
| assetType | object | See Asset Types Schema | { "id": 2, "name": "TABLE" } | 


## Example JSON

```json
{ 
  "id": 12616, 
  "uid": "sales.customer_table", 
  "name": "customer_orders", 
  "assemblyId": 5 
}
```

