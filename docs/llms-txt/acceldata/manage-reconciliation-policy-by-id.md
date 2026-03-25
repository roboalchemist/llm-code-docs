# Source: https://docs.acceldata.io/api/manage-reconciliation-policy-by-id.md

# Manage Reconciliation Policy by ID

Use these endpoints when you need to:

- **Retrieve** the current configuration of a specific policy (GET).
- **Update** rule definitions or metadata (PUT).
- **Archive or unarchive** a policy when it’s no longer or newly needed (DELETE / POST).
- **Enable or disable scheduling** to control automatic runs (PUT schedule).
- **Inspect rule items** associated with the policy (GET items).
- **List historical executions** of the policy to monitor its performance (GET executions).

## Endpoint(s)

```none
GET    /catalog-server/api/rules/reconciliation/:id                  (Retrieve a policy by id)
PUT    /catalog-server/api/rules/reconciliation/:id
DELETE /catalog-server/api/rules/reconciliation/:id
POST   /catalog-server/api/rules/reconciliation/:id/unarchive
PUT    /catalog-server/api/rules/reconciliation/:id/schedule
GET    /catalog-server/api/rules/reconciliation/:id/executions
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | integer | Yes | Unique numeric ID of the Reconciliation policy. | 


## Sample Request

**Toggle schedule**

```bash
curl -X PUT "https://{HOST}/catalog-server/api/rules/reconciliation/82338/schedule" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" -d '{"rule":{"scheduled":true}}'
```

