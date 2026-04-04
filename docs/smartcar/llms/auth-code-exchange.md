# Source: https://smartcar.com/docs/api-reference/authorization/auth-code-exchange.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auth Code Exchange

> To interact with the Smartcar API, you will need to exchange your authorization code from the [Connect redirect](https://smartcar.com/docs/connect/handle-the-response) for an access token. Check the [overview](https://smartcar.com/docs/api-reference/authorization/overview) page for how to manage your tokens.

## Requesting Access Tokens

**Headers**

<Snippet file="header-basic-auth.mdx" />

<ParamField header="Content-Type" type="string" initialValue="application/x-www-form-urlencoded" required>
  Must be set to `application/x-www-form-urlencoded`, matching the format of the request body.
</ParamField>

<ParamField header="User-Agent" type="string" required>
  A valid HTTP User Agent value. This value is typically included in the HTTP requests by the client that is making the request. You usually don't have to set this manually.
</ParamField>

**Body**

<ParamField query="code" type="string" required>
  The authorization code received in the handle response step.
</ParamField>

<ParamField query="grant_type" type="string" required>
  This value must be set to `authorization_code`
</ParamField>

<ParamField query="redirect_uri" type="string" required>
  The `redirect_uri` provided in the redirect to Connect step. This value is checked to match the URI sent when the user was directed to Connect.
</ParamField>

<Info>
  If you launch Connect from a single-page or mobile application, `redirect_uri` **must** match the URI passed in your Connect URL, not the redirect for your backend.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl https://auth.smartcar.com/oauth/token \
  -X POST \
  -H 'Authorization: Basic base64({client_id}:{client_secret})' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=authorization_code&code=35a59c0b-745c-436c-a8a2-7758e718dcb8&redirect_uri=https://example.com/home'
  ```

  ```python Python SDK theme={null}
    access = client.exchange_code('{code}')
  ```

  ```node Node SDK theme={null}
    access = client.exchangeCode('{code}');;
  ```

  ```java Java SDK theme={null}
    Auth access = authClient.exchangeCode("{code}");
  ```

  ```ruby Ruby SDK theme={null}
    access = client.exchange_code("{code}")
  ```
</RequestExample>

## Response

<Snippet file="response-token-pair.mdx" />
