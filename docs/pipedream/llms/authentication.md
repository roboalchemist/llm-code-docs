# Source: https://pipedream.com/docs/connect/api-reference/authentication.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

The Pipedream Connect API supports two authentication methods:

1. **OAuth access tokens**: Server-side authentication using client credentials
2. **Connect tokens**: Client-side authentication using short-lived tokens scoped to individual end users

Both approaches support scopes to limit access to specific operations.

## OAuth Access Tokens

OAuth access tokens are used for server-side API requests. They're generated using the client credentials flow and expire after 1 hour.

**Why OAuth?**

✅ OAuth clients are tied to the Pipedream workspace and administered by workspace admins \
✅ Tokens are short-lived \
✅ OAuth access tokens support scopes, limiting access to specific operations

<Note>
  Since API requests are meant to be made server-side, and since grants are not tied to individual end users, all OAuth clients are [**Client Credentials** applications](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/).
</Note>

### Creating an OAuth client

1. Visit the [API settings](https://pipedream.com/settings/api) for your Pipedream workspace
2. Click the **New OAuth Client** button
3. Name your client and click **Create**
4. Copy the client ID and secret (the secret will not be accessible again)

### How to get an access token

In the client credentials model, you exchange your OAuth client ID and secret for an access token. Then you use the access token to make API requests.

Pipedream offers [TypeScript](https://www.npmjs.com/package/@pipedream/sdk), [Python](https://pypi.org/project/pipedream), and [Java](https://central.sonatype.com/artifact/com.pipedream/pipedream) SDKs, which abstract the process of generating and refreshing fresh access tokens.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { PipedreamClient } from "@pipedream/sdk";

  const client = new PipedreamClient({
    clientId: "YOUR_CLIENT_ID",
    clientSecret: "YOUR_CLIENT_SECRET",
    projectEnvironment: "YOUR_PROJECT_ENVIRONMENT",
    projectId: "YOUR_PROJECT_ID",
    // Optional: specify scopes (defaults to "*")
    scope: "connect:accounts:read connect:accounts:write"
  });
  await client.accounts.retrieve("account_id");

  ```

  ```python Python theme={null}
  from pipedream import Pipedream

  pd = Pipedream(
      client_id="YOUR_CLIENT_ID",
      client_secret="YOUR_CLIENT_SECRET",
      project_id="YOUR_PROJECT_ID",
      project_environment="YOUR_PROJECT_ENVIRONMENT",
      # Optional: specify scopes (defaults to "*")
      scope="connect:accounts:read connect:accounts:write"
  )
  await pd.accounts.retrieve("account_id")
  ```

  ```java Java theme={null}
  import com.pipedream.api.BaseClient;

  BaseClient client = BaseClient
      .builder()
      .clientId("YOUR_CLIENT_ID")
      .clientSecret("YOUR_CLIENT_SECRET")
      .projectId("YOUR_PROJECT_ID")
      .projectEnvironment("YOUR_PROJECT_ENVIRONMENT")
      // Optional: specify scopes (defaults to "*")
      .scope("connect:accounts:read connect:accounts:write")
      .build();
  ```

</CodeGroup>

You can also manage this token refresh process yourself, using the `/oauth/token` API endpoint:

```bash  theme={null}
curl https://api.pipedream.com/v1/oauth/token \
  -H 'Content-Type: application/json' \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "<client_id>",
    "client_secret": "<client_secret>",
    "scope": "connect:accounts:read connect:accounts:write"
  }'
```

The `scope` parameter is optional and accepts a space-separated list of scopes. If omitted, the token defaults to `*` (full access).

Access tokens expire after 1 hour. Store access tokens securely in your server.

### OAuth scopes

OAuth access tokens support scopes to limit access to specific operations. When creating an access token, you can optionally specify a space-separated list of scopes. If no scope is specified, the token defaults to `*` (full access).

**Available scopes:**

| Scope                             | Description                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| `*`                               | Full access to every OAuth-protected endpoint                                             |
| `connect:*`                       | Full access to all Connect API endpoints (components, projects, triggers, accounts, etc.) |
| `connect:actions:*`               | Full access to Connect actions                                                            |
| `connect:triggers:*`              | Full access to Connect triggers                                                           |
| `connect:accounts:read`           | List and fetch Connect accounts for an external user                                      |
| `connect:accounts:write`          | Create or remove Connect accounts                                                         |
| `connect:deployed_triggers:read`  | Read deployed triggers and related data like events, pipelines and webhooks               |
| `connect:deployed_triggers:write` | Modify or delete deployed triggers                                                        |
| `connect:usage:read`              | List Connect usage records for a time window                                              |
| `connect:users:read`              | List and fetch external users                                                             |
| `connect:users:write`             | Delete external users                                                                     |
| `connect:tokens:create`           | Create Connect session tokens                                                             |
| `connect:proxy`                   | Invoke the Connect proxy                                                                  |
| `connect:workflow:invoke`         | Invoke Connect workflows on behalf of a user                                              |

### Revoking a client secret

1. Visit your workspace's [API settings](https://pipedream.com/settings/api)
2. Click the **…** button to the right of the OAuth client whose secret you want to revoke, then click **Rotate client secret**
3. Copy the new client secret (it will not be accessible again)

### OAuth security

See [the OAuth section of the security docs](/privacy-and-security/#pipedream-rest-api-security-oauth-clients) for more information on how Pipedream secures OAuth credentials.

## Connect Tokens

Connect tokens are short-lived tokens that enable you to securely make client-side requests on behalf of end users. They're created server-side and passed to your frontend to authenticate requests.

### Creating a Connect token

Use the [Create Connect token](/connect/api-reference/create-connect-token) endpoint to generate a token for an external user:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { PipedreamClient } from "@pipedream/sdk";

  const client = new PipedreamClient({
    clientId: "YOUR_CLIENT_ID",
    clientSecret: "YOUR_CLIENT_SECRET",
    projectEnvironment: "YOUR_PROJECT_ENVIRONMENT",
    projectId: "YOUR_PROJECT_ID"
  });

  const { token, expires_at } = await client.createConnectToken({
    externalUserId: "user-123",
    // Optional: customize TTL (defaults to 4 hours)
    expiresIn: 3600, // 1 hour
    // Optional: restrict scopes (defaults to "connect:*")
    scope: "connect:accounts:read connect:accounts:write"
  });

  ```

  ```python Python theme={null}
  from pipedream import Pipedream

  pd = Pipedream(
      client_id="YOUR_CLIENT_ID",
      client_secret="YOUR_CLIENT_SECRET",
      project_id="YOUR_PROJECT_ID",
      project_environment="YOUR_PROJECT_ENVIRONMENT"
  )

  result = pd.create_connect_token(
      external_user_id="user-123",
      # Optional: customize TTL (defaults to 4 hours)
      expires_in=3600,  # 1 hour
      # Optional: restrict scopes (defaults to "connect:*")
      scope="connect:accounts:read connect:accounts:write"
  )
  token = result.token
  expires_at = result.expires_at
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.pipedream.com/v1/connect/{project_id}/tokens \
    -H 'Authorization: Bearer <access_token>' \
    -H 'Content-Type: application/json' \
    -d '{
      "external_user_id": "user-123",
      "expires_in": 3600,
      "scope": "connect:accounts:read connect:accounts:write"
    }'
  ```

</CodeGroup>

### Connect token TTL

Connect tokens have a customizable time-to-live (TTL):

* **Minimum:** 1 second
* **Maximum:** 14,400 seconds (4 hours)
* **Default:** 14,400 seconds (4 hours)

Specify the TTL using the `expires_in` parameter (in seconds) when creating a token.

### Connect token scopes

Connect tokens support the same scopes as OAuth access tokens. When creating a Connect token, you can optionally specify a space-separated list of scopes. If no scope is specified, the token defaults to `connect:*` (full access to all Connect API endpoints).

**Available scopes:**

| Scope                             | Description                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| `connect:*`                       | Full access to all Connect API endpoints (components, projects, triggers, accounts, etc.) |
| `connect:actions:*`               | Full access to Connect actions                                                            |
| `connect:triggers:*`              | Full access to Connect triggers                                                           |
| `connect:accounts:read`           | List and fetch Connect accounts for an external user                                      |
| `connect:accounts:write`          | Create or remove Connect accounts                                                         |
| `connect:deployed_triggers:read`  | Read deployed triggers and related data like events, pipelines and webhooks               |
| `connect:deployed_triggers:write` | Modify or delete deployed triggers                                                        |
| `connect:usage:read`              | List Connect usage records for a time window                                              |
| `connect:users:read`              | List and fetch external users                                                             |
| `connect:users:write`             | Delete external users                                                                     |
| `connect:tokens:create`           | Create Connect session tokens                                                             |
| `connect:proxy`                   | Invoke the Connect proxy                                                                  |
| `connect:workflow:invoke`         | Invoke Connect workflows on behalf of a user                                              |

<Note>
  Connect tokens cannot be granted the `*` scope. The maximum scope available is `connect:*`.
</Note>

Built with [Mintlify](https://mintlify.com).
