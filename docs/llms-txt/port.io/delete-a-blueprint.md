# Source: https://docs.port.io/api-reference/delete-a-blueprint.md

# Delete a blueprint

```
DELETE 
/v1/blueprints/:identifier
```

This route allows you to delete a specific blueprint in your Port account.<br /><br />To learn more about blueprints, check out the [documentation](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/).<br /><br />**Note:** Before deleting a blueprint, make sure all associated entities have been deleted. Entity deletion may take a few seconds to complete, so plan accordingly when using the [**Delete an entity**](https://docs.port.io/api-reference/delete-an-entity) endpoint before this endpoint in scripts or automations.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Deleted successfully.

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
