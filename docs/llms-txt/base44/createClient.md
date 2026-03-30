# Source: https://docs.base44.com/developers/references/sdk/docs/functions/createClient.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# createClient

***

> **createClient**(`config`): `Base44Client`

Creates a Base44 client.

This is the main entry point for the Base44 SDK. It creates a client that provides access to the SDK's modules, such as [`entities`](../type-aliases/entities), [`auth`](../interfaces/auth), and [`functions`](../interfaces/functions).

How you get a client depends on your context:

* **Inside a Base44 app:** The client is automatically created and configured for you. Import it from `@/api/base44Client`.
* **External app using Base44 as a backend:** Call `createClient()` directly in your code to create and configure the client.

The client supports three authentication modes:

* **Anonymous**: Access modules without authentication using `base44.moduleName`. Operations are scoped to public data and permissions.
* **User authentication**: Access modules with user-level permissions using `base44.moduleName`. Operations are scoped to the authenticated user's data and permissions. Use `base44.auth.loginViaEmailPassword()` or other auth methods to get a token.
* **Service role authentication**: Access modules with elevated permissions using `base44.asServiceRole.moduleName`. Operations can access any data available to the app's admin. Only available in Base44-hosted backend functions. Create a client with service role authentication using [`createClientFromRequest()`](createClientFromRequest).

For example, when using the [`entities`](../type-aliases/entities) module:

* **Anonymous**: Can only read public data.
* **User authentication**: Can access the current user's data.
* **Service role authentication**: Can access all data that admins can access.

Most modules are available in all three modes, but with different permission levels. However, some modules are only available in specific authentication modes.

## Parameters

<ParamField body="config" type="CreateClientConfig" required>
  Configuration object for the client.
</ParamField>

<Accordion title="Properties">
  <ParamField body="serverUrl" type="string">
    The Base44 server URL.

    You don't need to set this for production use. The SDK defaults to `https://base44.app`.

    Set this when using a local development server to point SDK requests at your local machine instead of the hosted backend.
  </ParamField>

  <ParamField body="appId" type="string" required>
    The Base44 app ID.

    You can find the `appId` in the browser URL when you're in the app editor.
    It's the string between `/apps/` and `/editor/`.
  </ParamField>

  <ParamField body="token" type="string">
    User authentication token. Used to authenticate as a specific user.

    Inside Base44 apps, the token is managed automatically. For external apps, use auth methods like loginViaEmailPassword() which set the token automatically.
  </ParamField>

  <ParamField body="options" type="CreateClientOptions">
    Additional client options.

    <Accordion title="Properties">
      <ParamField body="onError" type="(error: Error) => void">
        Optional error handler that will be called whenever an API error occurs.
      </ParamField>
    </Accordion>
  </ParamField>
</Accordion>

## Returns

`Base44Client`

The Base44 client instance.

Provides access to all SDK modules for interacting with the app.

A configured Base44 client instance with access to all SDK modules.

<Accordion title="Properties">
  <ResponseField name="agents" type="AgentsModule" required>
    [Agents module](../interfaces/agents) for managing AI agent conversations.
  </ResponseField>

  <ResponseField name="analytics" type="AnalyticsModule" required>
    [Analytics module](../interfaces/analytics) for tracking custom events in your app.
  </ResponseField>

  <ResponseField name="appLogs" type="AppLogsModule" required>
    [App logs module](../interfaces/app-logs) for tracking app usage.
  </ResponseField>

  <ResponseField name="auth" type="AuthModule" required>
    [Auth module](../interfaces/auth) for user authentication and management.
  </ResponseField>

  <ResponseField name="entities" type="EntitiesModule" required>
    [Entities module](../type-aliases/entities) for CRUD operations on your data models.
  </ResponseField>

  <ResponseField name="functions" type="FunctionsModule" required>
    [Functions module](../interfaces/functions) for invoking custom backend functions.
  </ResponseField>

  <ResponseField name="integrations" type="IntegrationsModule" required>
    [Integrations module](../type-aliases/integrations) for calling pre-built integration endpoints.
  </ResponseField>

  <ResponseField name="cleanup" type="() => void" required>
    Cleanup function to disconnect WebSocket connections. Call when you're done with the client.
  </ResponseField>

  <ResponseField name="asServiceRole" type="object" required>
    Provides access to supported modules with elevated permissions.

    Service role authentication provides elevated permissions for backend operations. Unlike user authentication, which is scoped to a specific user's permissions, service role authentication has access to the data and operations available to the app's admin.

    <Accordion title="Properties">
      <ResponseField name="agents" type="AgentsModule" required>
        [Agents module](../interfaces/agents) with elevated permissions.
      </ResponseField>

      <ResponseField name="appLogs" type="AppLogsModule" required>
        [App logs module](../interfaces/app-logs) with elevated permissions.
      </ResponseField>

      <ResponseField name="connectors" type="ConnectorsModule" required>
        [Connectors module](../interfaces/connectors) for OAuth token retrieval.
      </ResponseField>

      <ResponseField name="entities" type="EntitiesModule" required>
        [Entities module](../type-aliases/entities) with elevated permissions.
      </ResponseField>

      <ResponseField name="functions" type="FunctionsModule" required>
        [Functions module](../interfaces/functions) with elevated permissions.
      </ResponseField>

      <ResponseField name="integrations" type="IntegrationsModule" required>
        [Integrations module](../type-aliases/integrations) with elevated permissions.
      </ResponseField>

      <ResponseField name="cleanup" type="() => void" required>
        Cleanup function to disconnect WebSocket connections.
      </ResponseField>
    </Accordion>
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Create a client for your app theme={null}
  import { createClient } from '@base44/sdk';

  const base44 = createClient({
    appId: 'my-app-id'
  });

  // Use the client to access your data
  const products = await base44.entities.Products.list();
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).