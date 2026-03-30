# Source: https://docs.port.io/api-reference/get-all-action-runs.md

# Get all action runs

```
GET 
/v1/actions/runs
```

This route allows you to fetch all action runs in your Port account. The route will perform a logical `AND` between all query parameters below, and return all action runs that match the criteria.<br /><br />To learn more about action runs, check out the [documentation](https://docs.port.io/create-self-service-experiences/reflect-action-progress/).<br />

Version parameter

Set the `version` parameter to `v2` for the latest version of the API.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404

Retrieved successfully.

Default Response

A resource with the provided identifier was not found
