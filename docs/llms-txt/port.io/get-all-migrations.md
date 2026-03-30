# Source: https://docs.port.io/api-reference/get-all-migrations.md

# Get all migrations

```
GET 
/v1/migrations
```

This route allows you to fetch all migrations (both past and present) in your Port organization.<br /><br />The call will perform a logical `AND` operation on the query parameters below, and return all migrations that match the criteria.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404

Default Response

A resource with the provided identifier was not found
