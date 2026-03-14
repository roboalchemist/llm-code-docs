# Source: https://docs.acceldata.io/api/list-asset-facets.md

# List Asset Facets

Facets let you refine large asset lists. Use this API when building search or filtering interfaces. For example, if your enterprise has thousands of assets, you could retrieve facets like schema names, asset types, or owners, and let users drill down to “all tables in the finance schema owned by the compliance team.”

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint

`GET /catalog-server/api/assets/list/facets`

## Query Parameters

| Parameter | Type | Description | 
| ---- | ---- | ---- | 
| pages | string | Page number | 
| size | string | Results per page | 
| parents | string | If true, include parents up to root | 
| watchers | string | If true, only watched assets | 
| asset___type_ids | string | Comma-separated asset type IDs | 


Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/assets/list/facets?page=1&size=50"
```



## Response Schema

See [Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/asset-schema).