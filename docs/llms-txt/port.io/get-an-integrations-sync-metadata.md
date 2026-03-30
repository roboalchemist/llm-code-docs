# Source: https://docs.port.io/api-reference/get-an-integrations-sync-metadata.md

# Get an integration's sync metadata

```
GET 
/v1/integration/:integrationInternalId/syncsMetadata
```

This route allows you to get an integration's sync metadata, which includes the sync's ID, state, creation and last update dates.

Returns resyncs from the last 4 days, or the 50 most recent ones.

**Permission requirements**<br />To use this endpoint, you must have a `moderator` or `admin` role in your Port organization.<br />To learn more about the different roles and permissions, please refer to the [documentation](https://docs.port.io/sso-rbac/users-and-teams/manage-users-teams/#roles--permissions).

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
