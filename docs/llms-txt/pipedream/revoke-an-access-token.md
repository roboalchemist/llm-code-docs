# Source: https://pipedream.com/docs/rest-api/api-reference/oauth/revoke-an-access-token.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke an access token

Revokes an access token, rendering it invalid for future requests.

#### Endpoint

```
POST /oauth/revoke
```

#### Parameters

<ParamField title="token" type="string">
  The access token to revoke.
</ParamField>

***

<ParamField title="client_id" type="string">
  The client ID of the OAuth app.
</ParamField>

***

<ParamField title="client_secret" type="string">
  The client secret of the OAuth app.
</ParamField>

***

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/oauth/revoke \
    -H 'Content-Type: application/json' \
    -d '{ "token": "<access token>", "client_id": "<client_id>", "client_secret": "<client secret>" }'
  ```
</RequestExample>

<ResponseExample>
  ```sh  theme={null}
  # This endpoint will return a `200 OK` response with an empty body if the token was successfully revoked:
  {}
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
