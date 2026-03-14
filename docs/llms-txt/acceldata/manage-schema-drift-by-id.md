# Source: https://docs.acceldata.io/api/manage-schema-drift-by-id.md

# Manage Policy by ID

Use these endpoints to **retrieve, update, delete, and schedule** Schema Drift policies by their unique ID.  

This is ideal for automations and workflows that identify policies by system-generated IDs.

## Endpoint(s)

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | /catalog-server/api/rules/schema-drift/:id | Retrieve full details of a Schema Drift policy by ID. | 
| PUT | /catalog-server/api/rules/schema-drift/:id | Update an existing Schema Drift policy. | 
| DELETE | /catalog-server/api/rules/schema-drift/:id | Delete (archive) a Schema Drift policy by ID. | 
| GET | /catalog-server/api/rules/schema-drift/:id/executions | Retrieve a list of all executions for this policy. | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | The unique ID of the Schema Drift policy. | 


## Sample Request

**GET Policy**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/schema-drift/10566"
```

