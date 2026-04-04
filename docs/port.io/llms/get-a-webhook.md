# Source: https://docs.port.io/api-reference/get-a-webhook.md

# Get a webhook

```
GET 
/v1/webhooks/:identifier
```

This route allows you to fetch a specific webhook in your Port organization. You can also see it in the [data sources page](https://app.getport.io/settings/data-sources) of your Port account.<br />To learn more about webhooks, check out the [documentation](https://docs.port.io/build-your-software-catalog/custom-integration/webhook/).<br /><br />**Permission requirements**<br />To use this endpoint, you must have a `moderator` or `admin` role in your Port organization.<br />To learn more about the different roles and permissions, please refer to the [documentation](https://docs.port.io/sso-rbac/users-and-teams/manage-users-teams/#roles--permissions).

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404

Default Response

A resource with the provided identifier was not found
