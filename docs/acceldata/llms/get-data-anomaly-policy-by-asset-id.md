# Source: https://docs.acceldata.io/api/get-data-anomaly-policy-by-asset-id.md

# Get Policy by Asset ID

Use this API to retrieve anomaly policies **associated with a specific asset**.
 This is commonly used in:

- Data lineage tools
- Asset overview dashboards
- SLA coverage or “policy inventory” reports

## Endpoint

```http
GET /catalog-server/api/rules/profile-anomaly/byAsset/:id
```



## Path Parameter

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | integer | Yes | Asset ID whose anomaly policies you want to fetch | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/profile-anomaly/byAsset/9623966" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

