# Source: https://docs.airbyte.com/ai-agents/api/api-reference/create-account-applications-scoped-token.md

# Create Scoped Token

```
POST 
/api/v1/account/applications/scoped-token
```

**Requires an Access Token as the bearer token.**

Generate a new scoped token.

You can safely share it with your end users and it will allow them to manage their configured sources.

## Request[​](#request "Direct link to request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 422
* 500

Successful Response

Bad request

Forbidden

Unprocessable entity

Internal server error
