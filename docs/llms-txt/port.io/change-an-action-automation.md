# Source: https://docs.port.io/api-reference/change-an-action-automation.md

# Change an action/automation

```
PUT 
/v1/actions/:action_identifier
```

This route allows you to change the details of an existing self-service action or automation in your Port account.<br /><br />To learn more about actions and automations, check out the [documentation](https://docs.port.io/actions-and-automations/).

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
