# Source: https://docs.port.io/api-reference/create-credentials.md

# Create credentials

```
POST 
/v1/apps
```

This route allows you to create a set of credentials in your Port organization, containing a `client ID` and `client secret`.

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
