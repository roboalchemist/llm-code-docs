# Source: https://docs.port.io/api-reference/create-a-blueprint.md

# Create a blueprint

```
POST 
/v1/blueprints
```

This route allows you to create a new blueprint in your data model.<br /><br />To learn more about blueprints, check out the [documentation](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/).

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
