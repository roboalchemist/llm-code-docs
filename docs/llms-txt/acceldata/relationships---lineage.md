# Source: https://docs.acceldata.io/api/relationships---lineage.md

# Relationships & Lineage

Lineage shows how data flows between assets. Use this API when you need to understand dependencies or impacts. For example, if a column in the “sales” table changes type, lineage can reveal all downstream dashboards that will be affected. You can also create lineage manually to model transformations not automatically captured.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /torch-pipeline/api/assets/:assetId/lineage`
- `POST /torch-pipeline/api/assets/:assetId/lineage`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| assetId | int | Yes | Asset ID | 12616 | 


## Query Parameters (GET)

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| sublevellineage | boolean | No | `true`  for column-level view  ID | false | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/torch-pipeline/api/assets/12616/lineage?sublevellineage=false"
```

