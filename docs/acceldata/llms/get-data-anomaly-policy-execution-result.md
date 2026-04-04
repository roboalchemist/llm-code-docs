# Source: https://docs.acceldata.io/api/get-data-anomaly-policy-execution-result.md

# Get Policy Execution Results

Use this endpoint when you need to retrieve the **results** of a specific anomaly detection run.
 This includes:

- Execution status
- Anomaly detection output
- Timestamp details
- Child job executions (if applicable)

This endpoint returns the **full execution detail** for one anomaly detection job.

## Endpoint

```http
GET /catalog-server/api/rules/profile-anomaly/executions/:executionId/result
```



## Path Parameter

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `executionId` | integer | Yes | The execution ID to fetch results for the policy. | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/profile-anomaly/executions/67890/result" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

