# Source: https://docs.port.io/api-reference/delete-multiple-entities.md

# Delete multiple entities

```
POST 
/v1/blueprints/:blueprint_identifier/bulk/entities/delete
```

This route allows you to delete multiple entities (up to 100 entities per request) from a specific blueprint in your software catalog. All entities must belong to the same blueprint.<br /><br />If any entity has dependent entities and delete\_dependents is false, the entire operation will fail and no entities will be deleted.<br /><br />To learn more about entities, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Entities deleted successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
