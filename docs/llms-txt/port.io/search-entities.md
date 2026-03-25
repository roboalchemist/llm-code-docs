# Source: https://docs.port.io/api-reference/search-entities.md

# Search entities

```
POST 
/v1/entities/search
```

This route allows you to search for entities in your software catalog based on a given set of rules.<br /><br />To learn more about entities, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).<br /><br />For more details about Port's search mechanism, rules, and operators - see the [search & query documentation](https://docs.port.io/search-and-query/overview).

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Retrieved successfully (this response can be compressed).

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
