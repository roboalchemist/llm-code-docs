# Source: https://docs.port.io/api-reference/create-multiple-entities.md

# Create multiple entities

```
POST 
/v1/blueprints/:blueprint_identifier/entities/bulk
```

This route allows you to create multiple entities (No more than 20 entities per request) in your software catalog based on an existing blueprint in your data model. It can also be used to overwrite or update existing entities.<br /><br />To learn more about entities, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).<br /><br />**Note:** A failure response does not necessarily mean that all entities failed. A `207 Multi-Status` response indicates that some entities were successfully created while others failed.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 207
* 401
* 404
* 413
* 422

Created successfully.

Partially created successfully. Some entities were created while others failed.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
