# Source: https://docs.acceldata.io/api/manage-data-quality-by-id.md

# Manage Policies by ID

Once a Data Quality policy has been created, these APIs allow you to fully manage its lifecycle — from retrieving its details to scheduling or archiving it.

Use these endpoints when you need to:

- **Retrieve** the current configuration of a specific policy (GET).
- **Update** rule definitions or metadata (PUT).
- **Archive or unarchive** a policy when it’s no longer or newly needed (DELETE / POST).
- **Enable or disable scheduling** to control automatic runs (PUT schedule).
- **Inspect rule items** associated with the policy (GET items).
- **List historical executions** of the policy to monitor its performance (GET executions).

These operations are typically used in:

- Automating policy updates and maintenance
- Managing active vs. inactive rules across environments
- Troubleshooting and auditing data quality checks

Note Most of these endpoints require the policy ID, which can be obtained from the **List All Policies** or **Create Policy** endpoints.

## Endpoint(s)

```none
GET    /catalog-server/api/rules/data-quality/:id           (get)
PUT    /catalog-server/api/rules/data-quality/:id           (update)
DELETE /catalog-server/api/rules/data-quality/:id           (delete/archive)
POST   /catalog-server/api/rules/data-quality/:id/unarchive (unarchive)
PUT    /catalog-server/api/rules/data-quality/:id/schedule  (toggle schedule)
GET    /catalog-server/api/rules/data-quality/:id/items     (list items)
GET    /catalog-server/api/rules/data-quality/:id/executions (list executions)
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | integer | Yes | Unique numeric ID of the Data Quality policy. | 


## Sample Request

### Get

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-quality/10566"
```



### Update

```bash
curl -X PUT "https://{HOST}/catalog-server/api/rules/data-quality/10566" \
  -H "Authorization: Bearer $TOKEN" -H "accessKey: $ACCESS_KEY" -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  			"rule":{
        		"scheduled":true,
        		"schedule":"0 15 * * *"
        	}
       }'
```

