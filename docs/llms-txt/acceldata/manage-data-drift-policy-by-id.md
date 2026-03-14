# Source: https://docs.acceldata.io/api/manage-data-drift-policy-by-id.md

# Manage Policy by ID

Use these endpoints to **retrieve**, **update**, **delete**, **archive**, **unarchive**, or **toggle the schedule** of a Data Drift policy by its unique ID.  

Managing by ID is useful for direct integrations and automations.

## Endpoint(s)

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | /catalog-server/api/rules/data-drift/:id | Retrieve full details of a Data Drift policy by its unique ID. | 
| PUT | /catalog-server/api/rules/data-drift/:id | Update an existing Data Drift policy (e.g., thresholds, columns, description). | 
| DELETE | /catalog-server/api/rules/data-drift/:id | Delete (archive) a Data Drift policy by ID. | 
| POST | /catalog-server/api/rules/data-drift/:id/unarchive | Unarchive a previously deleted Data Drift policy. | 
| PUT | /catalog-server/api/rules/data-drift/:id/schedule | Enable or disable scheduling for the policy and define a cron schedule if needed. | 
| GET | /catalog-server/api/rules/data-drift/:id/executions | List all execution history for the Data Drift policy. | 
