# Source: https://docs.port.io/api-reference/change-a-webhook.md

# Change a webhook

```
PUT 
/v1/webhooks/:identifier
```

This route allows you to modify a webhook in your Port organization. You can also modify it via the [data sources page](https://app.getport.io/settings/data-sources) of your Port account.<br /><br />To learn more about webhooks, check out the [documentation](https://docs.port.io/build-your-software-catalog/custom-integration/webhook/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
