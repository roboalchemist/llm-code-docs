# Source: https://configcat.com/docs/api/reference/get-auditlogs.md

# List Audit log items for Product

Copy page

This endpoint returns the list of Audit log items for a given Product and the result can be optionally filtered by Config and/or Environment.

If neither `fromUtcDateTime` nor `toUtcDateTime` is set, the audit logs for the **last 7 days** will be returned.

The distance between `fromUtcDateTime` and `toUtcDateTime` cannot exceed **30 days**.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
