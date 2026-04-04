# Source: https://docs.acceldata.io/api/get-asset-metadata.md

# Retrieve Asset Metadata

Use this when you need to understand the **structure** of an asset. Metadata provides column names, types, and statistics that are essential for governance or policy creation. For example, a compliance officer might review whether a “customer” table includes personally identifiable fields such as `ssn` or `email`.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint

`GET /catalog-server/api/assets/:id/metadata`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/assets/12616/metadata"
```



## Response Schema

See [Asset Metadata Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/metadata-schema).