# Source: https://docs.acceldata.io/api/manage-data-drift-policy-by-name.md

# Manage Policy By Name

Use these endpoints to **retrieve, update, delete, archive, unarchive,** or **toggle scheduling** of a Data Drift policy by its **name**.

This is useful when referencing policies in automation pipelines without knowing their IDs.

## Endpoint(s)

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | /catalog-server/api/rules/data-drift/byName/:name | Retrieve full details of a Data Drift policy by its name. | 
| PUT | /catalog-server/api/rules/data-drift/byName/:name | Update an existing Data Drift policy using its name. | 
| DELETE | /catalog-server/api/rules/data-drift/byName/:name | Delete (archive) a Data Drift policy by name. | 
| POST | /catalog-server/api/rules/data-drift/byName/:name/unarchive | Unarchive a previously deleted Data Drift policy by name. | 
| PUT | /catalog-server/api/rules/data-drift/byName/:name/schedule | Enable or disable scheduling and define a cron schedule. | 
| GET | /catalog-server/api/rules/data-drift/byName/:name/executions | List all executions for this Data Drift policy. | 
| POST | /catalog-server/api/rules/data-drift/byName/:name/executions | Trigger a new execution for the Data Drift Policy. | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| name | string | Yes | The name of the Data Drift policy. | 


## Sample Requests

**Get Policy:**

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-drift/byName/Customer_Data_Drift"
```

