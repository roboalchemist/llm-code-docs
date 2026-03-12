# Source: https://docs.port.io/api-reference/get-audit-logs.md

# Get audit logs

```
GET 
/v1/audit-log
```

This route allows you to fetch audit logs from your Port account. Your audit logs can also be viewed via [Port's UI](https://app.getport.io/settings/AuditLog).<br /><br />This route will perform a logical `AND` between all query parameters below, and return all logs that match the criteria.<br /><br />**Note:** Non-admin users have limited access to the audit logs API. They may:<br />- Pass an `identifier` to access a specific audit log.<br />- Pass an `entity` to retrieve audit logs of entities they have access to.<br />- Pass a `run_id` to retrieve audit logs of action runs they have access to.<br />Non-admin users **cannot** view audit logs of deleted entities.<br />

Beta integration value

The `integration` value in the `resources` parameter is **experimental**. Its behavior may change in future versions of the API.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404

Default Response

A resource with the provided identifier was not found
