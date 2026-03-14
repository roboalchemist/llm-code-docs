# Source: https://docs.acceldata.io/api/create-data-drift-policy.md

# Create Data Drift Policy

Use this endpoint to create a new Data Drift policy that monitors changes in data distributions over time.  

This helps ensure that upstream data sources remain stable and alerts are raised when drifts exceed defined thresholds.

## Endpoint(s)

| Method | Path | 
| ---- | ---- | 
| POST | /catalog-server/api/rules/data-drift | 


## Path & Query Parameters

This endpoint does not accept any path or query parameters.

## Sample Request

```bash
curl -X POST "https://{HOST}/catalog-server/api/rules/data-drift" \
  -H "Authorization: Bearer $TOKEN" \
  -H "accessKey: $ACCESS_KEY" \
  -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer_Data_Drift",
    "description": "Detect drift in customer demographic attributes",
    "status": "ACTIVE",
    "source": {
      "connectionName": "customer_warehouse",
      "database": "analytics",
      "table": "customers"
    },
    "columns": [
      {
        "name": "age",
        "driftType": "NUMERIC",
        "threshold": 0.1
      },
      {
        "name": "country",
        "driftType": "CATEGORICAL",
        "threshold": 0.05
      }
    ],
    "tags": ["drift", "customer", "monitoring"]
  }'
```

