# Source: https://docs.acceldata.io/api/list-executions--all-policies-.md

# List Executions (All Policies)

Use this endpoint to retrieve a **global list of all policy executions**, regardless of policy type. This is useful for dashboards, monitoring tools, time-based queries, and SLA reporting.

## Endpoint

```http
GET /catalog-server/api/rules/executions
```



## Query Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `ruleType` | string | No | Filter by policy type (e.g., DATA_QUALITY, RECONCILIATION, DATA_ DRIFT, etc.) | 
| `executionStatus` | string | No | Filter by status (SUCCESS, WARNING, FAILURE, ERROR, etc.) | 
| `resultStatus` | string | No | Filter based on evaluation result category. | 
| `assetId` | integer | No | Return executions related to a specific asset. | 
| `from` | string | No | Start timestamp (ISO). | 
| `to` | string | No | End timestamp (ISO). | 
| pagination params | integer | No | Standard pagination fields (page, size). | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/executions?ruleType=DATA_QUALITY&executionStatus=FAILURE" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

