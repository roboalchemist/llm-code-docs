# Source: https://docs.port.io/api-reference/update-an-action-run.md

# Update an action run

```
PATCH 
/v1/actions/runs/:run_id
```

This route allows you to update an action run's details. This can be used to update the run's status & label, and add links to it (e.g. external logs of the job runner).<br /><br />To learn more about action runs, check out the [documentation](https://docs.port.io/create-self-service-experiences/reflect-action-progress/).

Version parameter value

Set the `version` parameter to `v2` for the latest version of the API.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

OK

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
