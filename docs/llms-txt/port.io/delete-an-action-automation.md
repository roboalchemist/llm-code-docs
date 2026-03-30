# Source: https://docs.port.io/api-reference/delete-an-action-automation.md

# Delete an action/automation

```
DELETE 
/v1/actions/:action_identifier
```

This route allows you to delete a self-service action or automation.<br /><br />To learn more about actions and automations, check out the [documentation](https://docs.port.io/actions-and-automations/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
