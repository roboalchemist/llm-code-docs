# Source: https://docs.port.io/api-reference/approve-an-action-run.md

# Approve an action run

```
PATCH 
/v1/actions/runs/:run_id/approval
```

This route allows you to approve or decline a request to execute an action that requires approval.<br /><br />To learn more about manual approval for actions, check out the [documentation](https://docs.port.io/create-self-service-experiences/set-self-service-actions-rbac/#configure-manual-approval-for-actions).<br />

Version parameter value

Set the `version` parameter to `v2` for the latest version of the API.

## Request[â](#request "Direct link to request")

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
