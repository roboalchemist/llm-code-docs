# Source: https://docs.port.io/api-reference/get-an-integrations-metrics-and-sync-status.md

# Get an integration's metrics and sync status

```
GET 
/v1/integration/:integrationInternalId/syncMetrics
```

This route allows you to get a specific integration's metrics and sync status either the latest one or for a specific resync.<br /><br />It returns the sync's execution status and detailed metrics per kind for each phase of the sync.<br />For example, the number of fetched objects in the sync's fetch phase, number of objects that were mapped in the mapping phase, etc.<br /><br />To learn more about integrations, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/).<br /><br />**Permission requirements**<br />To use this endpoint, you must have a `moderator` or `admin` role in your Port organization.<br />To learn more about the different roles and permissions, please refer to the [documentation](https://docs.port.io/sso-rbac/users-and-teams/manage-users-teams/#roles--permissions).

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 500

Default Response

Default Response

Default Response

Default Response
