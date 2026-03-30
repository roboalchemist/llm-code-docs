# Source: https://docs.acceldata.io/api/get-execution-results.md

# Get Execution Results

Execution result APIs return the **detailed rule-level output** of a policy run. Results include metrics, item evaluations, unmatched records (for reconciliation), drift statistics, freshness calculations, and anomaly detections.

Each policy type exposes its own result endpoint:

### Data Quality

```http
GET /catalog-server/api/rules/data-quality/executions/:id/result
```



### Reconciliation

```http
GET /catalog-server/api/rules/reconciliation/executions/:id/result
```



### Data Drift

```http
GET /catalog-server/api/rules/data-drift/executions/:id/result
```



### Schema Drift

```http
GET /catalog-server/api/rules/schema-drift/executions/:id/result
```



### Data Freshness (Cadence)

```http
GET /catalog-server/api/rules/data-cadence/executions/:executionId/result
```



### Data Anomaly

```http
GET /catalog-server/api/rules/profile-anomaly/executions/:executionId/result
```



## Path Parameters (generic pattern)

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` or `executionId` | string | Yes | Execution identifier | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/data-drift/executions/54321/result" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

