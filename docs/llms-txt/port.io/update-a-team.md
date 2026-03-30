# Source: https://docs.port.io/api-reference/update-a-team.md

# Update a team

```
PATCH 
/v1/teams/:name
```

This route allows you to update a team's details. This can be used to update the team's name, users, and description.<br /><br />To learn more about teams, check out the [documentation](https://docs.port.io/sso-rbac/rbac-overview/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Updated successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
