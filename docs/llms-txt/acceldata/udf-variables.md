# Source: https://docs.acceldata.io/api/udf-variables.md

# UDF Variables

User-Defined Variables are custom key–value pairs associated with assets. They’re useful for passing parameters into rules or transformations. For example, you might store a `threshold=0.95` variable for a table, and reference it in a data quality policy to ensure completeness stays above 95%.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id/udf-variables`
- `POST /catalog-server/api/assets/:id/udf-variables`
- `GET /catalog-server/api/assets/:id/udf-variables/:variableId`
- `PUT /catalog-server/api/assets/:id/udf-variables/:variableId`
- `DELETE /catalog-server/api/assets/:id/udf-variables/:variableId`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 
| variableId | int | No | Variable ID (for GET/PUT/DELETE) | `3001` | 


## Request Body

```json
{
  "key": "threshold",
  "value": "0.95"
}
```



## Sample Request

```bash
curl -X POST "https://demo.acceldata.io/catalog-server/api/assets/12616/udf-variables"
```



## Response Schema

See [Udf Variables](../schemas/udf-variables.md)