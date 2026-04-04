# Source: https://docs.acceldata.io/api/retrieve-child-assets.md

# Retrieve Child Assets

Assets often have hierarchical relationships — databases contain schemas, schemas contain tables, and tables contain columns. This API helps you traverse that hierarchy. For example, you might retrieve all child tables under a schema to ensure every dataset in a business domain is being monitored.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint

`GET /catalog-server/api/assets/:id/childAssets`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Parent ID | `1001` | 


## Response Schema

See [Related Child Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/related-child-asset-schema).