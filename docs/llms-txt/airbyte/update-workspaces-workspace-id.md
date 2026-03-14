# Source: https://docs.airbyte.com/ai-agents/api/api-reference/update-workspaces-workspace-id.md

# Update Workspace

```
PUT 
/api/v1/workspaces/:workspace_id
```

Update an external user's name, status, and/or cache setting.

* Set `name` to update the external user name
* Set `status` to 'active' or 'inactive' to change the external user status
* When setting status to 'inactive', all active connections for the external user will be automatically disabled
* Set `cache_enabled` to true/false to enable or disable Context Store caching for this external user

## Request[​](#request "Direct link to request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 422
* 500

Successful Response

Bad request

Forbidden

Unprocessable entity

Internal server error
