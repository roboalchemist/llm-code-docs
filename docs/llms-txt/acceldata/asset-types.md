# Source: https://docs.acceldata.io/api/asset-types.md

# Asset Types

Asset Types define the categories of supported objects (e.g., `DATABASE` , `TABLE`, `FILE`). Use this API when building user interfaces or filtering results.

For example, you might want to display only FILE-type assets when exploring a data lake.

> ⚠️ All endpoints require authentication. See [Authorization & Headers](../authorization.md).

## Endpoint

`GET /catalog-server/api/asset-types`

## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/asset-types"
```



## Response Schema

See [Asset Types Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/asset-types-schema).