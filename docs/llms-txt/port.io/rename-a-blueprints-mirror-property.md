# Source: https://docs.port.io/api-reference/rename-a-blueprints-mirror-property.md

# Rename a blueprint's mirror property

```
PATCH 
/v1/blueprints/:blueprint_identifier/mirror/:property_identifier/rename
```

This route allows you to change the identifier of a mirror property in a specific blueprint in your Port account.<br /><br />To learn more about blueprints, check out the [documentation](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/).

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
