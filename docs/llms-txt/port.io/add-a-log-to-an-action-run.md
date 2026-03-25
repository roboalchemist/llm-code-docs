# Source: https://docs.port.io/api-reference/add-a-log-to-an-action-run.md

# Add a log to an action run

```
POST 
/v1/actions/runs/:run_id/logs
```

This route allows you to send a log message back to Port, which will be displayed in the action run's page. You can also use this route to update the run's termination status (SUCCESS/FAILURE) and label describing the status.<br /><br />To learn more about action runs, check out the [documentation](https://docs.port.io/create-self-service-experiences/reflect-action-progress/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 201
* 401
* 404
* 413
* 422

OK

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
