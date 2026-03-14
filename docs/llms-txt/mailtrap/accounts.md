# Source: https://docs.mailtrap.io/developers/account-management/accounts.md

# Accounts

The Account ID is required when working with Account Management endpoints.

To find your Account ID, you can either:

* Use the endpoint below to list your accounts, or
* Find it in the UI under [Account Settings](https://mailtrap.io/account-management)

## List account(s) you have access to

> This endpoint returns account details for the authenticated user. If you are using \[Organizations and Sub-Accounts]\(<https://docs.mailtrap.io/account-and-organization/management/organization-and-sub-accounts>) and the API token was created at the organization level, the response will include all accounts within the organization.<br>

```json
{"openapi":"3.1.0","info":{"title":"Account Management","version":"2.0.0"},"tags":[{"name":"Accounts","description":"The Account ID is required when working with Account Management endpoints.\n\nTo find your Account ID, you can either:\n- Use the endpoint below to list your accounts, or\n- Find it in the UI under [Account Settings](https://mailtrap.io/account-management)\n"}],"servers":[{"description":"Mailtrap API","url":"https://mailtrap.io"}],"security":[{"HeaderAuth":[]},{"BearerAuth":[]}],"components":{"securitySchemes":{"HeaderAuth":{"type":"apiKey","description":"Pass the API token in the Api-Token","in":"header","name":"Api-Token"},"BearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"JWT"}},"responses":{"UNAUTHENTICATED":{"description":"Returns unauthorized error message. Check your credentials.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/UnauthenticatedResponse"}}}}},"schemas":{"UnauthenticatedResponse":{"title":"UnauthenticatedResponse","type":"object","properties":{"error":{"type":"string","description":"Error message"}}}}},"paths":{"/api/accounts":{"get":{"operationId":"getAllAccounts","summary":"List account(s) you have access to","description":"This endpoint returns account details for the authenticated user. If you are using [Organizations and Sub-Accounts](https://docs.mailtrap.io/account-and-organization/management/organization-and-sub-accounts) and the API token was created at the organization level, the response will include all accounts within the organization.\n","tags":["Accounts"],"responses":{"200":{"description":"Returns the list of accounts to which the API token has access. **access_levels** can return 1000 (account owner), 100 (admin), 10 (viewer).","content":{"application/json":{"schema":{"type":"array","items":{"type":"object","properties":{"id":{"type":"integer"},"name":{"type":"string"},"access_levels":{"type":"array","items":{"type":"integer"}}}}}}}},"401":{"$ref":"#/components/responses/UNAUTHENTICATED"}}}}}}
```
