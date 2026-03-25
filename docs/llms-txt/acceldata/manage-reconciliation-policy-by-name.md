# Source: https://docs.acceldata.io/api/manage-reconciliation-policy-by-name.md

# Manage Reconciliation Policy by Name

Use these endpoints to manage an existing Reconciliation policy using its **name** instead of the numeric ID.

## Endpoints

```none
GET    /catalog-server/api/rules/reconciliation/byName/:name						 (retrieve policy by name)
PUT    /catalog-server/api/rules/reconciliation/byName/:name						 (update policy) 
DELETE /catalog-server/api/rules/reconciliation/byName/:name						 (archive policy)	
POST   /catalog-server/api/rules/reconciliation/byName/:name/unarchive   (unarchive policy)
PUT    /catalog-server/api/rules/reconciliation/byName/:name/schedule    (Toggle schedule)
GET    /catalog-server/api/rules/reconciliation/byName/:name/executions  (List executions) 
POST   /catalog-server/api/rules/reconciliation/byName/:name/executions  (Trigger manual execution)
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| name | string | Yes | Unique name of the Reconciliation Policy. | 


## Sample Request

**Update Reconciliation Policy by Name**

```bash
curl -X PUT "https://{HOST}/catalog-server/api/rules/reconciliation/byName/Sales_Recon_Policy" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "accessKey: $ACCESS_KEY" \
  -H "secretKey: $SECRET_KEY" \
  -d '{
    "description": "Reconciliation policy to ensure sales data matches between source and target tables",
    "status": "ACTIVE",
    "scheduled": true,
    "schedule": "0 3 * * *",
    "source": {
      "connectionName": "sales_source",
      "database": "sales_db",
      "table": "transactions"
    },
    "target": {
      "connectionName": "sales_target",
      "database": "sales_warehouse",
      "table": "transactions"
    },
    "joinConditions": [
      {
        "sourceColumn": "transaction_id",
        "targetColumn": "transaction_id"
      }
    ],
    "matchRules": [
      {
        "sourceColumn": "amount",
        "targetColumn": "amount",
        "tolerance": 0
      },
      {
        "sourceColumn": "currency",
        "targetColumn": "currency"
      }
    ],
    "thresholds": {
      "maxMismatchPercentage": 5
    },
    "tags": ["finance", "critical"]
  }'
```

