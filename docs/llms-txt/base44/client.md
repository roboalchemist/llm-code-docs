# Source: https://docs.base44.com/developers/references/sdk/getting-started/client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Base44 client

> Learn how to work with the Base44 client

The Base44 client is your interface to the Base44 SDK. It provides access to all SDK modules and automatically manages authentication tokens.

You can use the client in two ways:

* **Inside Base44 apps**: The client is automatically created and configured for you.
* **External apps**: Create the client yourself to use Base44 as a backend for your own app.

## Inside Base44 apps

When Base44 generates your app, the SDK client is pre-configured and ready to use.

### Frontend client

In your frontend code, the client is already imported and available as `base44`.

<CodeGroup>
  ```typescript Frontend code theme={null}
  import { base44 } from "@/api/base44Client";

  // The client is pre-configured and ready to use
  const user = await base44.auth.me();
  const userTasks = await base44.entities.Task.filter({
    assignedTo: user.id,
    status: "pending",
  });

  console.log(`${user.name} has ${userTasks.length} pending tasks`);
  ```
</CodeGroup>

### Backend functions

In Base44-hosted backend functions, create the client from the incoming request. Base44 injects the necessary authentication headers automatically.

<CodeGroup>
  ```typescript Backend function theme={null}
  import { createClientFromRequest } from "npm:@base44/sdk";

  Deno.serve(async (req) => {
    const base44 = createClientFromRequest(req);

    // Get the current user and their data
    const user = await base44.auth.me();
    const userTasks = await base44.entities.Task.filter({
      assignedTo: user.id,
      status: "pending",
    });

    return Response.json({
      user: user.name,
      pendingTasks: userTasks.length,
    });
  });
  ```
</CodeGroup>

## External apps

When building your own app that uses Base44 as a backend, create and configure the client yourself using `createClient()`.

### Installation

Install the SDK via npm:

```bash  theme={null}
npm install @base44/sdk
```

### Create the client

Create a client by providing your app ID, which you can find in the Base44 editor URL:

```
https://app.base44.com/apps/<your-app-id>/editor/...
```

<CodeGroup>
  ```typescript Create client theme={null}
  import { createClient } from "@base44/sdk";

  // Create a client for your Base44 app
  const base44 = createClient({
    appId: "your-app-id", // Find this in the Base44 editor URL
  });

  // Read public data (anonymous access)
  const products = await base44.entities.Products.list();
  ```
</CodeGroup>

### User authentication

Authenticate users with email and password or through social providers. The client automatically applies the token to subsequent requests. Social authentication is available for Google, Microsoft, Facebook, and Apple using [`loginWithProvider()`](/developers/references/sdk/docs/interfaces/auth#loginwithprovider).

<CodeGroup>
  ```typescript Email and password theme={null}
  import { createClient } from "@base44/sdk";

  const base44 = createClient({
    appId: "your-app-id",
  });

  // Authenticate a user (token is automatically set)
  await base44.auth.loginViaEmailPassword("user@example.com", "password");

  // Now operations use the authenticated user's permissions
  const userOrders = await base44.entities.Orders.list();
  ```

  ```typescript Social login theme={null}
  import { createClient } from "@base44/sdk";

  const base44 = createClient({
    appId: "your-app-id",
  });

  // Login with Google (redirects to Google OAuth)
  base44.auth.loginWithProvider('google', '/dashboard');
  ```
</CodeGroup>

## Service role

By default, the client operates with user-level permissions, limiting access to what the current user can see and do. The service role provides elevated permissions for backend operations and is only available in Base44-hosted backend functions.

<Note>
  Service role authentication is only available in Base44-hosted backend
  functions. External backends can't use service role permissions.
</Note>

A client with service role authentication allows backend code to:

* Access data and operations with the same permissions as your app's admin.
* Use admin modules like the [`connectors`](/developers/references/sdk/docs/interfaces/connectors) module.

To use service role authentication, access modules through `base44.asServiceRole` instead of directly on the client. For example, `base44.asServiceRole.entities.Task.list()` operates with admin permissions, while `base44.entities.Task.list()` uses the current user's permissions.

When using `createClientFromRequest()` in a backend function, the service role is automatically available:

<CodeGroup>
  ```typescript Backend function with service role theme={null}
  import { createClientFromRequest } from "npm:@base44/sdk";

  Deno.serve(async (req) => {
    const base44 = createClientFromRequest(req);

    // Access all data with admin-level permissions
    const allOrders = await base44.asServiceRole.entities.Orders.list();

    return Response.json({ orders: allOrders });
  });
  ```
</CodeGroup>

## See more

<CardGroup cols={2}>
  <Card title="createClient()" icon="code" href="/developers/references/sdk/docs/functions/createClient">
    Complete API reference
  </Card>

  <Card title="createClientFromRequest()" icon="code" href="/developers/references/sdk/docs/functions/createClientFromRequest">
    Backend client creation
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).