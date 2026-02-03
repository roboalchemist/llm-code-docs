# Source: https://configcat.com/docs/api/reference/delete-environment.md

# Delete Environment

Copy page

This endpoint removes an Environment identified by the `environmentId` parameter. If the `cleanupAuditLogs` flag is set to true, it also deletes the audit log records related to the environment (except for the `Created a new environment` and `Deleted an environment` records).

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 204
* 400
* 404
* 429

When the delete was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
