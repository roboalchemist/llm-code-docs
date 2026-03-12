# Source: https://docs.acceldata.io/api/incremental-strategies.md

# Incremental Strategies

Incremental strategies define how new data is ingested or validated. Use this API when working with large, continuously growing datasets. For example, you can configure the “transactions” table to use a timestamp column as an incremental marker, so only new rows since the last run are checked — improving performance and reducing costs.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id/incremental-strategies`
- `PUT /catalog-server/api/assets/:id/config`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 


## Request Body

```json
{
  "incrementalColumn": "last_updated",
  "strategy": "TIMESTAMP"
}
```



## Sample Request

```bash
curl -X PUT "https://demo.acceldata.io/catalog-server/api/assets/12616/config"
```



## Response Schema

See [Incremental Strategy](../schemas/incremental-strategy.md)