# Source: https://docs.airbyte.com/ai-agents/api/api-reference/update-oauth-credentials.md

# Configure connector OAuth

```
PUT 
/api/v1/oauth/credentials
```

Create or update OAuth credentials for the user's organization.

This endpoint:

1. Extracts organization\_id from the user's token
2. Validates the configuration against the connector's OAuth spec
3. Stores secrets and replaces them with secret coordinates
4. Proxies the credentials to Coral's organization OAuth endpoint
5. Saves the record to Sonar's database

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
