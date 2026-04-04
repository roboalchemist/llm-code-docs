# Source: https://docs.port.io/api-reference/rotate-a-users-credentials.md

# Rotate a user's credentials

```
POST 
/v1/rotate-credentials/:user_email
```

This route allows you to rotate a user's credentials and generate new ones.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
