# Source: https://docs.base44.com/developers/references/sdk/getting-started/third-party-apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to third-party APIs

> Choose the right approach for integrating external services into your Base44 app

Base44 provides several ways to connect your app to external APIs. Each approach has different trade-offs around setup complexity, credential management, and flexibility.

<CardGroup cols={3}>
  <Card title="Connectors" icon="link" href="#connectors">
    OAuth login to services like Slack, Google Calendar, or Discord
  </Card>

  <Card title="Custom integrations" icon="plug" href="#custom-integrations">
    Workspace-wide API access via OpenAPI specs
  </Card>

  <Card title="Backend functions" icon="code" href="#backend-functions">
    Backend code with full control over requests
  </Card>
</CardGroup>

## Connectors

Connectors let app builders authenticate their apps with third-party services using OAuth. When they connect an integration like Slack, Google Calendar, or Discord, their app uses their account to access that service. All users of the app interact with the same connected account.

With connectors, you're responsible for making the API calls yourself. Each app can have one connection per integration type, and only one app builder can authorize each connection.

<CodeGroup>
  ```typescript Get a connection theme={null}
  const { accessToken } = await base44.asServiceRole.connectors.getConnection(
    "googlecalendar"
  );

  // Use the token to call the API directly
  const response = await fetch(
    "https://www.googleapis.com/calendar/v3/calendars",
    {
      headers: { Authorization: `Bearer ${accessToken}` },
    }
  );

  const calendars = await response.json();
  ```
</CodeGroup>

<Card title="connectors" icon="link" href="/developers/references/sdk/docs/interfaces/connectors">
  Complete API reference
</Card>

## Custom integrations

Custom integrations let you call external APIs using shared credentials that aren't specific to a user or app. A workspace administrator imports an OpenAPI specification, configures the credentials, and then any app in the workspace can call that API through the SDK. Requests are proxied through Base44's backend, so secrets never reach the browser. Once an integration is set up, all apps in the workspace share it. Developers never handle API keys directly, so the admin can rotate credentials without touching app code.

<CodeGroup>
  ```typescript Call a custom integration theme={null}
  const response = await base44.integrations.custom.call(
    "my-crm", // integration slug
    "get:/contacts", // endpoint: method:path format
    {
      pathParams: { id: "123" },
      queryParams: { limit: 10 },
    }
  );

  if (response.success) {
    console.log(response.data);
  }
  ```
</CodeGroup>

<Card title="custom integrations" icon="plug" href="/developers/references/sdk/docs/type-aliases/integrations#customintegrationsmodule">
  Complete API reference
</Card>

## Backend functions

Backend functions run on the server, so you can safely store API keys and secrets as environment variables without exposing them to the browser. Use backend functions when you need full control over API requests, want to add custom logic or data transformation, or are working with APIs that don't have a custom integration available. Your frontend calls the backend function, which then makes the external API request and returns the result.

<CodeGroup>
  ```typescript Backend function theme={null}
  // In your backend function
  export default async function handler(request: Request) {
    const apiKey = process.env.EXTERNAL_API_KEY;

    const response = await fetch("https://api.example.com/data", {
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
    });

    return Response.json(await response.json());
  }
  ```

  ```typescript Call from frontend theme={null}
  // Call the backend function from your frontend
  const result = await base44.functions.invoke("myFunction", {});
  ```
</CodeGroup>

<Card title="functions" icon="code" href="/developers/references/sdk/docs/interfaces/functions">
  Learn more about backend functions
</Card>


Built with [Mintlify](https://mintlify.com).