# Source: https://docs.acceldata.io/api/create-and-list-reconciliation-policies.md

# Create and List Policies

Use the following APIs to create a reconciliation policy and list the existing reconciliation policies.

## Endpoint(s)

```none
GET  /catalog-server/api/rules/reconciliation     (list)
POST /catalog-server/api/rules/reconciliation     (create)
```



## Query Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| page | integer | No | Page number to retrieve when listing policies (default: 0). | 
| size | integer | No | Page size for pagination (default: 25). | 
| onlyActive | boolean | No | If `true`, returns only active Reconciliation policies. | 


Notes

- `POST` is used to **create** a Reconciliation policy (body required, no query params).
- `GET` lists Reconciliation policies with pagination support.

## Sample Requests

**Create (example)** — equality on a join of two assets

```bash
curl -X POST "https://{HOST}/catalog-server/api/rules/reconciliation" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "rule":{
          "name":"ORDERS_vs_ORDERS_STG",
          "type":"RECONCILIATION",
          "details":{
            "leftBackingAssetId":123,
            "rightBackingAssetId":124,
            "joinConditions":[{"leftColumnName":"id","rightColumnName":"id","operation":"EQ"}]
          },
          "thresholdLevel": {
      			"type": "ABSOLUTE",
      			"config": {
        			"direction": "ABOVE",
        			"success": 100,
        			"warning": 70
      				}
    			}
        },
        "items":[{"measurementType":"EQUALITY","executionOrder":1}]
      }'
```

