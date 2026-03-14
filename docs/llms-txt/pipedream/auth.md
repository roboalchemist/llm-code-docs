# Source: https://pipedream.com/docs/workflows/building-workflows/code/python/auth.md

# Source: https://pipedream.com/docs/workflows/building-workflows/code/nodejs/auth.md

# Source: https://pipedream.com/docs/rest-api/auth.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

The Pipedream API supports two methods of authentication: [OAuth](/rest-api/auth/#oauth) and [User API keys](/rest-api/auth/#user-api-keys).

<Note>
  Looking for the Pipedream Connect API? [Go here](/connect/api-reference/introduction).
</Note>

**We use OAuth** for the majority of the API, for a few reasons:

✅ OAuth clients are tied to the workspace and are administered by workspace admins\
✅ Tokens are short-lived\
✅ OAuth clients support scopes, limiting access to specific operations\
✅ Limit access to specific Pipedream projects (coming soon)

## OAuth

Workspace administrators can create OAuth clients in your workspace’s [API settings](https://pipedream.com/settings/api).

Since API requests are meant to be made server-side, and since grants are not tied to individual end users, all OAuth clients are [**Client Credentials** applications](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/).

### Creating an OAuth client

1. Visit the [API settings](https://pipedream.com/settings/api) for your workspace.
2. Click the **New OAuth Client** button.
3. Name your client and click **Create**.
4. Copy the client secret. **It will not be accessible again**. Click **Close**.
5. Copy the client ID from the list.

### How to get an access token

In the client credentials model, you exchange your OAuth client ID and secret for an access token. Then you use the access token to make API requests.

If you’re running a server that executes JavaScript, we recommend using [the Pipedream SDK](/connect/api-reference/introduction), which automatically refreshes tokens for you.

```javascript  theme={null}
import { PipedreamClient } from "@pipedream/sdk";
 
// These secrets should be saved securely and passed to your environment
const client = new PipedreamClient({
  clientId: "YOUR_CLIENT_ID",
  clientSecret: "YOUR_CLIENT_SECRET",
  projectId: "YOUR_PROJECT_ID", // This is typically required for most Connect API endpoints
  projectEnvironment: "development" // or "production"
});
 
// Use the SDK's helper methods to make requests
const accounts = await client.accounts.list({ include_credentials: 1 });
 
// Or make any Pipedream API request with the fresh token
const accounts = await client.makeAuthorizedRequest("/accounts", {
  method: "GET",
  params: {
    include_credentials: 1,
  }
});
```

You can also manage this token refresh process yourself, using the `/oauth/token` API endpoint:

```bash  theme={null}
curl https://api.pipedream.com/v1/oauth/token \
  -H 'Content-Type: application/json' \
  -d '{ "grant_type": "client_credentials", "client_id": "<client_id>", "client_secret": "<client secret>" }'
```

Access tokens expire after 1 hour. Store access tokens securely, server-side.

### Revoking a client secret

1. Visit your workspace’s [API settings](https://pipedream.com/settings/api).
2. Click the **…** button to the right of the OAuth client whose secret you want to revoke, then click **Rotate client secret**.
3. Copy the new client secret. **It will not be accessible again**.

### OAuth security

See [the OAuth section of the security docs](/privacy-and-security/#pipedream-rest-api-security-oauth-clients) for more information on how Pipedream secures OAuth credentials.

## User API keys

<Warning>
  User API keys are only supported for a limited number of endpoints. You should use OAuth instead.
</Warning>

When you sign up for Pipedream, an API key is automatically generated for your user account. You can use this key to authorize requests to the API.

You’ll find this API key in your [User Settings](https://pipedream.com/user) (**My Account** -> **API Key**).

This key is tied to your user account and provides full access to any resources your user has access to, across workspaces.

### Revoking your API key

You can revoke your API key in your [Account Settings](https://pipedream.com/settings/account) (**Settings** -> **Account**). Click on the **REVOKE** button directly to the right of your API key.

This will revoke your original API key, generating a new one. Any API requests made with the original token will yield a `401 Unauthorized` error.

## Authorizing API requests

Whether you use OAuth access tokens or user API keys, Pipedream uses [Bearer Authentication](https://oauth.net/2/bearer-tokens/) to authorize your access to the API or SSE event streams. When you make API requests, pass an `Authorization` header of the following format:

```
# OAuth access token
Authorization: Bearer <access token>

# User API key
Authorization: Bearer <api key>
```

For example, here’s how you can use `cURL` to fetch profile information for the authenticated user:

```bash  theme={null}
curl 'https://api.pipedream.com/v1/users/me' \
  -H 'Authorization: Bearer <api_key>'
```

## Using the Pipedream CLI

You can [link the CLI to your Pipedream account](/cli/login/), which will automatically pass your API key in the `Authorization` header with every API request.

Built with [Mintlify](https://mintlify.com).
