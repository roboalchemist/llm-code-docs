# Source: https://docs.acceldata.io/api/preview-sample-data.md

# Preview Sample Data

Before applying policies or creating reports, it’s useful to see a slice of the data itself. This API retrieves up to the first 100 rows of an asset. For example, a data engineer can validate that the “orders” table contains recent transactions before applying a freshness check.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

1. **Initiate Sample Job:** `POST /catalog-server/api/assets/:id/sample/async`

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 
| invalidateCache | boolean | No | If true, bypass cached sample | `true` | 


2. **Poll Job Result:** `GET /catalog-server/api/assets/sample/result/:requestId`

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| requestId | string | Yes | Returned from async request | `abc123` | 


## Sample Request

```bash
curl -X POST "https://demo.acceldata.io/catalog-server/api/assets/12616/sample/async"
```



## Response Schema

See [Sample Data Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/sample-data-schema).