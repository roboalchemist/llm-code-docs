# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams/use-case-get-user-access-token.md

# Use case: Get user access token &#x20;

This article describes a use case to demonstrate the usage of `Get user access token` configuration option in the MS Teams channel. It explains how to integrate with Microsoft Graph API on behalf of the user in the Avaamo Conversational AI Platform using the user access token. &#x20;

### Pre-requisite

You must deploy your agent in the MS Teams channel with the `Get user access token` enabled. See [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.

### Agent implementation

Consider that you wish to use the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) and access your information. Since you have enabled `Get user access token` option in the MS Teams channel, you can now access the API using the user access token available in the `context.user.sso_token` property.&#x20;

The following is a sample code demonstrating the usage of the user access token and how the same token can be used to access other applications on behalf of the user:&#x20;

{% code overflow="wrap" %}

```javascript
let resp = fetch("https://graph.microsoft.com/v1.0/me", {
    method: "GET",
    headers: {
        "Authorization": `Bearer ${context.user.sso_token}`
    }
}).then(e => e.json()).then(e => e);
resp = await (resp);
console.log("user", context.user);
console.log("resp", resp);
return resp;
```

{% endcode %}
