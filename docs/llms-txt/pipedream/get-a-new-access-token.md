# Source: https://pipedream.com/docs/rest-api/api-reference/oauth/get-a-new-access-token.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a new access token

Exchanges a client ID and client secret for a new access token.

#### Endpoint

```
POST /oauth/token
```

#### Parameters

<ParamField body="grant_type" type="string">
  The OAuth grant type. For Pipedream, this is always `client_credentials`.
</ParamField>

***

<ParamField body="client_id" type="string">
  The client ID of the OAuth app.
</ParamField>

***

<ParamField body="client_secret" type="string">
  The client secret of the OAuth app.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/oauth/token \
    -H 'Content-Type: application/json' \
    -d '{ "grant_type": "client_credentials", "client_id": "<client_id>", "client_secret": "<client secret>" }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "access_token": "<access token (a JWT)>",
    "token_type": "Bearer",
    "expires_in": 3600,
    "created_at": 1645142400
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
