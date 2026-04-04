# Source: https://docs.airbyte.com/ai-agents/api/api-reference/delete-oauth-credentials-connector-type-connector-type.md

# Delete connector OAuth

```
DELETE 
/api/v1/oauth/credentials/connector_type/:connector_type
```

Delete OAuth credentials for the user's organization.

Deletes from Airbyte first, then soft-deletes the local record. Idempotent: returns 204 even if no record exists.

## Request[​](#request "Direct link to request")

## Responses[​](#responses "Direct link to Responses")

* 204
* 400
* 403
* 422
* 500

Successful Response

Bad request

Forbidden

Unprocessable entity

Internal server error
