# Source: https://docs.port.io/api-reference/invite-a-user-to-your-organization.md

# Invite a user to your organization

```
POST 
/v1/users/invite
```

This route allows you to invite a user to your Port organization.<br /><br />To learn more about users, roles, and teams, check out the [documentation](https://docs.port.io/sso-rbac/rbac-overview/).

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
