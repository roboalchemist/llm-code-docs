# Source: https://docs.acceldata.io/api/get-asset-by-id-or-uid.md

# Get Asset by ID or UID

This API is helpful when you already know an asset’s unique identifier. For example, a downstream workflow may reference the UID of a critical dataset. Instead of searching, you can directly retrieve it to confirm details like its parent schema, type, or lineage connections.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id`
- `GET /catalog-server/api/assets/byUid/:uid`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 
| uid | string | Yes | Asset UID | `sales.table` | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/assets/12616"
```



## Response Schema

See [Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/asset-schema).