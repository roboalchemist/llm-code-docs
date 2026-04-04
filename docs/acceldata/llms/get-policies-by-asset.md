# Source: https://docs.acceldata.io/api/get-policies-by-asset.md

# Get Policies by Asset

Use this endpoint when you want to know **which Data Freshness policy is attached to a specific asset** (e.g., a key warehouse table).

Typical use cases:

- From an asset-centric view: “show me the freshness policy for this table”
- Building an inventory of all freshness SLAs per asset
- Checking whether a given critical asset is covered by any Data Freshness policy

## Endpoint

```http
GET /catalog-server/api/rules/data-cadence/byAsset/:id
```



## Path Parameter

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | Asset ID of the asset whose Data Freshness policy you want to retrieve. | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/rules/data-cadence/byAsset/1202692" \
  -H "accessKey: <YOUR_ACCESS_KEY>" \
  -H "secretKey: <YOUR_SECRET_KEY>" \
  -H "Accept: application/json"
```



The response includes:

- `details` – configuration for how freshness is evaluated for this asset (backing asset, execution order, thresholds, etc.)
- `rule` – the underlying Data Freshness policy definition (name, description, alerting setup, threshold levels, etc.)