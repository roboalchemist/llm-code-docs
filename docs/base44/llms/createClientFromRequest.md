# Source: https://docs.base44.com/developers/references/sdk/docs/functions/createClientFromRequest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# createClientFromRequest

***

> **createClientFromRequest**(`request`): `Base44Client`

Creates a Base44 client from an HTTP request.

This function is designed for use in Base44-hosted backend functions. For frontends and external backends, use [`createClient()`](createClient) instead.

When used in a Base44-hosted backend function, `createClientFromRequest()` automatically extracts authentication tokens from the request headers that Base44 injects when forwarding requests. The returned client includes service role access using `base44.asServiceRole`, which provides admin-level permissions.

To learn more about the Base44 client, see [`createClient()`](createClient).

## Parameters

<ParamField body="request" type="Request" required>
  The incoming HTTP request object containing Base44 authentication headers.
</ParamField>

## Returns

`Base44Client`

The Base44 client instance.

Provides access to all SDK modules for interacting with the app.

A configured Base44 client instance with authentication from the incoming request.

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

#### Examples

<CodeGroup>
  ```typescript User authentication in backend function theme={null}
  import { createClientFromRequest } from 'npm:@base44/sdk';

  Deno.serve(async (req) => {
    try {
      const base44 = createClientFromRequest(req);
      const user = await base44.auth.me();

      if (!user) {
        return Response.json({ error: 'Unauthorized' }, { status: 401 });
      }

      // Access user's data
      const userOrders = await base44.entities.Orders.filter({ userId: user.id });
      return Response.json({ orders: userOrders });
    } catch (error) {
      return Response.json({ error: error.message }, { status: 500 });
    }
  });
  ```

  ```typescript Service role authentication in backend function theme={null}
  import { createClientFromRequest } from 'npm:@base44/sdk';

  Deno.serve(async (req) => {
    try {
      const base44 = createClientFromRequest(req);

      // Access admin data with service role permissions
      const recentOrders = await base44.asServiceRole.entities.Orders.list('-created_at', 50);

      return Response.json({ orders: recentOrders });
    } catch (error) {
      return Response.json({ error: error.message }, { status: 500 });
    }
  });
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).