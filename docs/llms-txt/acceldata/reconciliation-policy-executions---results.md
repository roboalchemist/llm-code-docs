# Source: https://docs.acceldata.io/api/reconciliation-policy-executions---results.md

# Policy Executions and Results

Use these endpoints to retrieve **execution details and result payloads** for a specific Reconciliation policy run — typically to verify **source vs. target data matching outcomes**.

## Endpoint(s)

```none
GET  /catalog-server/api/rules/reconciliation/executions/:id           (execution details)
GET  /catalog-server/api/rules/reconciliation/executions/:id/result    (execution result)
```



## Path Parameters

| Name | Type | Required | Descriptions | 
| ---- | ---- | ---- | ---- | 
| id | integer | Yes | Unique ID of the **Reconciliation policy execution** (not the policy itself). | 


Note The `id` is obtained from the **List Executions** endpoint (`/reconciliation/:id/executions`).

## Sample Request

**Details**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/reconciliation/executions/5555" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY"
```

