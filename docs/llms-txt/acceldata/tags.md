# Source: https://docs.acceldata.io/api/tags.md

# Tags

Tags let you group and classify assets with business-friendly labels. Use them to make discovery easier for non-technical users.
For example, you can tag tables with "Finance", "PII", or "Gold Dataset" so analysts know which datasets are approved for reporting.
APIs allow you to automate this tagging at scale, ensuring consistent classification across the enterprise.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id/tags`
- `POST /catalog-server/api/assets/:id/tag`
- `DELETE /catalog-server/api/assets/:id/tag/:tagId`

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 
| tagId | int | No | Tag ID | `101` | 


## Sample Request

```bash
curl -X POST "https://demo.acceldata.io/catalog-server/api/assets/12616/tag"
```



## Response Schema

See [Tags Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/tags-schema).