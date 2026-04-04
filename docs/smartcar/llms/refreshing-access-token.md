# Source: https://smartcar.com/docs/api-reference/authorization/refreshing-access-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Refreshing Access Tokens

> Your access token will expire **2 hours** after it is issued. When this happens, your application can retrieve a new one by using the corresponding `refresh_token` without requiring the user to re-authenticate.

<Warning>
  A refresh token is invalidated 10 minutes after use. If your first attempt at refreshing tokens fails, ensure you retry within 10 minutes.
  Please ensure you're persisting **both the newly minted access and refresh token**. Failure to do so will require the user to authenticate again after the access token has expired.
</Warning>

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

<ParamField header="Content-Type" type="string" initialValue="application/x-www-form-urlencoded" required>
  Must be set to `application/x-www-form-urlencoded`, matching the format of the request body.
</ParamField>

<ParamField header="User-Agent" type="string" required>
  A valid HTTP User Agent value. This value is typically included in the HTTP requests by the client that is making the request. You usually don't have to set this manually.
</ParamField>

<RequestExample>
  <Snippet file="authorization/code-group-token-refresh.mdx" />
</RequestExample>

**Body**

<ParamField query="grant_type" type="string" initialValue="refresh_token" required>
  This value must be set to `refresh_token`
</ParamField>

<ParamField query="refresh_token" type="string" initialValue="3e565aed-d4b2-4296-9b4c-aec35825a6aa" required>
  The refresh token received in the response with the access token from an [auth code exchange](/api-reference/authorization/auth-code-exchange)
  or prior token refresh.
</ParamField>

**Response**

<Snippet file="response-token-pair.mdx" />
