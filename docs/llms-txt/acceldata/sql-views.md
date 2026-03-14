# Source: https://docs.acceldata.io/api/sql-views.md

# SQL Views

SQL Views (Custom Assets) let you create virtual assets on top of existing datasets. Use this API when you need derived datasets for analysis. 

For example, create a “regional_sales” view that aggregates transactions across multiple source tables.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `POST /catalog-server/api/custom-assets/sql-view`
- `GET /catalog-server/api/custom-assets/sql-view/:id`
- `PUT /catalog-server/api/custom-assets/sql-view/:id`
- `DELETE /catalog-server/api/custom-assets/sql-view/:id`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | SQL View ID | 501 | 


## Request Body (POST)

```json
{
  "data": {
    "asset": {
      "name": "regional_sales",
      "assemblyId": 5,
      "assetTypeId": 2,
      "isCustom": true
    },
    "details": {
      "query": "SELECT region, SUM(sales) as total FROM orders GROUP BY region"
    }
  }
}
```



## Sample Request

```bash
curl -X POST "https://demo.acceldata.io/catalog-server/api/custom-assets/sql-view" 
  -d '{"data":{"asset":{"name":"regional_sales","assemblyId":5,"assetTypeId":2,"isCustom":true},"details":{"query":"SELECT region, SUM(sales) as total FROM orders GROUP BY region"}}}'
```



## Response Schema

See [SQL View Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/sql-view-schema).