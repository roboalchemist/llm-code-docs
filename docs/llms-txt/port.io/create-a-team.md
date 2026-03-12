# Source: https://docs.port.io/api-reference/create-a-team.md

# Create a team

```
POST 
/v1/teams
```

This route allows you to create a new team in your Port organization.<br /><br />To learn more about teams, check out the [documentation](https://docs.port.io/sso-rbac/rbac-overview/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Created successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
