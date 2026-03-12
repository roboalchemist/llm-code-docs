# Source: https://docs.port.io/api-reference/fetch-the-history-of-an-entitys-properties.md

# Fetch the history of an entity's properties

```
POST 
/v1/entities/properties-history
```

This route allows you to retrieve historical values for a selected list of an entity's properties over a given time range.<br /><br />To learn more about entities, check out the [entity documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Retrieved successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
