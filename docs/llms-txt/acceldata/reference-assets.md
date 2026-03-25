# Source: https://docs.acceldata.io/api/reference-assets.md

# Reference Assets

Reference Assets are datasets used as a baseline for validation. Use this API when you want to compare new ingested data against a trusted reference. For example, mark last month’s “customer_master” table as reference, and automatically validate that the new load has the same schema and data distribution.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/reference-assets`
- `GET /catalog-server/api/assets/reference-assets/jobs`
- `PUT /catalog-server/api/assets/reference-assets/jobs/:jobId/cancel`
- `PUT /catalog-server/api/assets/byUid/:uid/config/reference-configuration`
- `GET /catalog-server/api/assets/:id/reference-assets/inferredMetadata`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| jobId | string | No | Validation job ID (cancel) | `job-789` | 
| uid | string | No | Asset UID for reference config | `gold.customer_master` | 
| id | int | No | Asset ID for inferred metadata | `12616` | 


## Sample Request

```bash
curl -X PUT "https://demo.acceldata.io/catalog-server/api/assets/byUid/gold.customer_master/config/reference-configuration"
  -d '{"validateNow": true}'
```



## Response Schema

See [Reference Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/reference-asset-schema).