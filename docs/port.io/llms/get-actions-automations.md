# Source: https://docs.port.io/api-reference/get-actions-automations.md

# Get actions/automations

```
GET 
/v1/actions
```

This route allows you to fetch one or more self-service actions and/or automations in your Port account.<br /><br />The call will perform a logical `AND` between all query parameters below, and return all actions and automations that match the criteria.<br /><br />To learn more about actions and automations, check out the [documentation](https://docs.port.io/actions-and-automations/).<br />

Version parameter

Set the `version` parameter to `v2` for the latest version of the API.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404

Default Response

A resource with the provided identifier was not found
