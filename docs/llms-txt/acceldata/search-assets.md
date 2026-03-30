# Source: https://docs.acceldata.io/api/search-assets.md

# Search Assets

Use this when you know part of an asset’s name or ID and need to quickly locate it. For example, if a business analyst asks for “customer_orders,” you can search by name fragment to retrieve the exact table in Snowflake or Hive, without scrolling through hundreds of results.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint

`GET /catalog-server/api/assets/search`

## Query Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| name | string | No | Full or partial name of asset | `customer_orders` | 
| ids | string | No | Comma-separated list of internal asset IDs | `12616,12617` | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/assets/search?name=customer"
```



## Response Schema

See [Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/asset-schema).