# Source: https://docs.acceldata.io/api/create-schema-drift-policy.md

# Create Schema Drift Policy

Use this endpoint to create a new Schema Drift policy that tracks structural changes in a table. 

It is typically used to ensure that downstream processes are not impacted by column-level schema changes.

## Endpoint

```bash
POST /catalog-server/api/rules/schema-drift
```



## Path & Query Parameters

This endpoint does not require any path or query parameters.

## Sample Request

```bash
curl -X POST "https://{HOST}/catalog-server/api/rules/schema-drift" \
  -H "Authorization: Bearer $TOKEN" \
  -H "accessKey: $ACCESS_KEY" \
  -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer_Schema_Drift",
    "description": "Detect column-level schema changes in the customers table",
    "status": "ACTIVE",
    "source": {
      "connectionName": "customer_warehouse",
      "database": "analytics",
      "table": "customers"
    },
    "tags": ["schema", "customer", "monitoring"]
  }'
```

