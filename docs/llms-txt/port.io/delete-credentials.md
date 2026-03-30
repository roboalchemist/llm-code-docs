# Source: https://docs.port.io/api-reference/delete-credentials.md

# Delete credentials

```
DELETE 
/v1/apps/:id
```

This route allows you to delete a set of credentials in your Port organization.

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
