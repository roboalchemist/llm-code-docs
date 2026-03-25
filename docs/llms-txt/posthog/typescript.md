# Source: https://posthog.com/docs/endpoints/start-here/retrieve-data/typescript.md

# Retrieve data from your endpoint with TypeScript - Docs

Call PostHog endpoints from TypeScript with type safety.

## Basic request

typescript

PostHog AI

```typescript
interface EndpointResponse {
  results: Record<string, unknown>[];
  columns: string[];
  hasMore: boolean;
}
async function callEndpoint(endpointName: string): Promise<EndpointResponse> {
  const response = await fetch(
    `<ph_app_host>/api/environments/{project_id}/endpoints/${endpointName}/run`,
    {
      headers: {
        "Authorization": `Bearer ${process.env.POSTHOG_PERSONAL_API_KEY}`
      }
    }
  );
  return response.json();
}
const data = await callEndpoint("daily_active_users");
```

## With variables

typescript

PostHog AI

```typescript
async function callEndpoint(
  endpointName: string,
  variables: Record<string, string>
): Promise<EndpointResponse> {
  const response = await fetch(
    `<ph_app_host>/api/environments/{project_id}/endpoints/${endpointName}/run`,
    {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.POSTHOG_PERSONAL_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ variables })
    }
  );
  return response.json();
}
const data = await callEndpoint("customer_events", { customer_id: "cust_123" });
```

For fully type-safe SDKs generated from your endpoint schemas, see [OpenAPI SDK generation](/docs/endpoints/start-here/retrieve-data/openapi.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better