# Source: https://docs.port.io/api-reference/aggregate-entities-over-time.md

# Aggregate entities over time

```
POST 
/v1/entities/aggregate-over-time
```

This route allows you to perform an aggregation function on a blueprint's entities over a given time range.<br /><br />To learn more about entities, check out the [entity documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/#entities).<br /><br />For more details about Port's search mechanism, rules, and operators - see the [search & query documentation](https://docs.port.io/search-and-query/overview).

## Request[â](#request "Direct link to request")

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
