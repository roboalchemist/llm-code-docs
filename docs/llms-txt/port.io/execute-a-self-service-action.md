# Source: https://docs.port.io/api-reference/execute-a-self-service-action.md

# Execute a self-service action

```
POST 
/v1/actions/:action_identifier/runs
```

This route allows you to execute a self-service action, thus creating an action run.<br /><br />To learn more about action runs, check out the [documentation](https://docs.port.io/create-self-service-experiences/reflect-action-progress/).

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 202
* 401
* 404
* 413
* 422

OK

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
