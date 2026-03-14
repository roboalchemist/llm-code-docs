# Source: https://docs.acceldata.io/api/data-quality-execution-and-results.md

# Policy Executions and Results

Use these APIs to retrieve execution details and results for a specific Data Quality policy run.  

They are typically used to **monitor policy performance**, **debug failures**, and **view rule-level outcomes**.

## Endpoint(s)

```none
GET  /catalog-server/api/rules/data-quality/:id/executions					 (list executions)
GET  /catalog-server/api/rules/data-quality/executions/:id           (execution details)
GET  /catalog-server/api/rules/data-quality/executions/:id/result    (execution result)
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | integer | Yes | Unique ID of the Data Quality **policy execution** (not the policy itself) | 


Note Use the execution `id` obtained from the **List Executions** endpoint (`/data-quality/:id/executions`) to query these APIs.

## Sample Requests

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-quality/executions/99999" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY"
```



**Execution result**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-quality/executions/99999/result" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY"
```

