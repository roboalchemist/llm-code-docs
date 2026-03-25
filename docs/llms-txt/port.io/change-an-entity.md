# Source: https://docs.port.io/api-reference/change-an-entity.md

# Change an entity

```
PUT 
/v1/blueprints/:blueprint_identifier/entities/:entity_identifier
```

This route allows you to edit a specific entity in your software catalog and update its properties.<br /><br />To learn more about entities, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).

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
