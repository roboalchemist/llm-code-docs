# Source: https://docs.port.io/api-reference/delete-a-team.md

# Delete a team

```
DELETE 
/v1/teams/:name
```

This route allows you to delete a team in your Port organization.<br /><br />To learn more about teams, check out the [documentation](https://docs.port.io/sso-rbac/rbac-overview/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Deleted successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
