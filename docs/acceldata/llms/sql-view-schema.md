# Source: https://docs.acceldata.io/api/sql-view-schema.md

# SQL View Schema

Returned by [SQL Views](https://docs.acceldata.io/acceldata-data-observability-cloud/api/sql-views).

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| id | integer | SQL view ID | 
| name | string | View name | 
| query | string | SQL definition | 
| assemblyId | integer | Source assembly | 
| assetTypeId | integer | Asset type | 


## Example JSON

```json
{ 
  "id": 501, 
  "name": "regional_sales", 
  "query": "SELECT * FROM orders" 
}
```

