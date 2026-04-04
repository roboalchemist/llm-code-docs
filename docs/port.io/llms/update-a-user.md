# Source: https://docs.port.io/api-reference/update-a-user.md

# Update a user

```
PATCH 
/v1/users/:user_email
```

This route allows you to update a user's details. This can be used to update the user's role/s and team/s.<br /><br />To learn more about users, roles, and teams, check out the [documentation](https://docs.port.io/sso-rbac/rbac-overview/).

## Request[â](#request "Direct link to request")

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
