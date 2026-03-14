# Source: https://docs.acceldata.io/api/schema-drift-execution---results.md

# Policy Execution and Results

Use these endpoints to **retrieve detailed execution information and results** of Schema Drift policies.  

The results include drift type, affected columns, and timestamps of detected schema changes.

## Endpoint(s)

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | /catalog-server/api/rules/schema-drift/executions/:id | Retrieve detailed execution metadata for the Schema Drift policy. | 
| GET | /catalog-server/api/rules/schema-drift/executions/:id/result | Retrieve detailed drift detection results for a specific execution. | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | Unique ID of the Schema Drift policy. | 


## Sample Request

**Execution Details**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/schema-drift/executions/98765"
```



**Execution Result**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/schema-drift/executions/98765/result"
```

