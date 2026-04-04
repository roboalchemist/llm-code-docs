# Source: https://docs.port.io/api-reference/create-an-entity.md

# Create an entity

```
POST 
/v1/blueprints/:blueprint_identifier/entities
```

This route allows you to create an entity in your software catalog based on an existing blueprint in your data model. It can also be used to overwrite or update an existing entity.<br /><br />To learn more about entities, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 201
* 401
* 404
* 413
* 422

Created successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
