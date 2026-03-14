# Source: https://docs.acceldata.io/api/data-drift-policy-execution---results.md

# Policy Execution and Results

Use these endpoints to **retrieve the detailed results of Data Drift policy executions**.  

This includes drift metrics, thresholds, execution status, and drift detection details for each monitored column.

## Endpoint(s)

| Method | Path | 
| ---- | ---- | 
| GET | /catalog-server/api/rules/data-drift/executions/:id | 
| GET | /catalog-server/api/rules/data-drift/executions/:id/result | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | The unique ID of the policy execution. | 


## Sample Requests

**Execution details:**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-drift/executions/78432"
```



**Execution result:**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-drift/executions/78432/result"
```

