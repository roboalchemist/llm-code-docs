# Source: https://docs.port.io/api-reference/rotate-secret.md

# Rotate secret

```
POST 
/v1/apps/:id/rotate-secret
```

This route allows you to rotate the secret of a set of credentials in your Port organization.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

OK

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
