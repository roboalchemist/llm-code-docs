# Source: https://docs.acceldata.io/api/manage-schema-drift-policy-by-name.md

# Manage Policy by Name

Use these endpoints to **retrieve, update, delete,** or **execute Schema Drift policies** by their names.  

This is helpful for managing policies in automation or CI/CD workflows where policy names are stable identifiers.

## Endpoint(s)

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | /catalog-server/api/rules/schema-drift/byName/:name | Retrieve details of a Schema Drift policy by name. | 
| PUT | /catalog-server/api/rules/schema-drift/byName/:name | Update a Schema Drift policy configuration using its name. | 
| DELETE | /catalog-server/api/rules/schema-drift/byName/:name | Delete (archive) a Schema Drift policy by name. | 
| GET | /catalog-server/api/rules/schema-drift/byName/:name/executions | List all executions for this Schema Drift policy. | 
| POST | /catalog-server/api/rules/schema-drift/byName/:name/executions | Trigger a new execution of the Schema Drift policy. | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| name | string | Yes | The name of the Schema Drift policy. | 


## Sample Request

**Get Policy**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/schema-drift/byName/Customer_Schema_Drift"
```



**Execute Policy**

```bash
curl -X POST "https://{HOST}/catalog-server/api/rules/schema-drift/byName/Customer_Schema_Drift/executions"
```

