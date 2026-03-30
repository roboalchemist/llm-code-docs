# Source: https://docs.airbyte.com/ai-agents/api/api-reference/create-account-applications-token.md

# Generate Application Token

```
POST 
/api/v1/account/applications/token
```

Generate an application access token using client credentials. This endpoint is intentionally unauthenticated - authentication is performed via client\_id and client\_secret in the request body. Returns a self-signed JWT token that can be used for all API calls.

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
