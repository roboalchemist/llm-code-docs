# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/durable-endpoints

# Durable Endpoints&#x20;

Create durable HTTP endpoints using `inngest.endpoint()`. Each step within the handler is checkpointed, allowing automatic recovery from failures.

```ts
import { Inngest, step } from "inngest";
import { endpointAdapter } from "inngest/edge";

const inngest = new Inngest({ id: "my-app", endpointAdapter });

export const handler = inngest.endpoint(async (req: Request): Promise<Response> => {
  const data = await step.run("fetch-data", async () => {
    return await fetchExternalAPI();
  });

  return Response.json({ data });
});
```

***

## Setup

### `endpointAdapter`

The `endpointAdapter` must be passed to the Inngest client constructor to enable Durable Endpoints.

```ts
import { Inngest } from "inngest";
import { endpointAdapter } from "inngest/edge";

const inngest = new Inngest({
  id: "my-app",
  endpointAdapter,
});
```

> **Callout:** The endpointAdapter is imported from inngest/edge (or any compatible
> framework entrypoint) and is required for Durable Endpoints to function. Without it,
> inngest.endpoint() will not be available.

***

## `inngest.endpoint(handler): Handler`

Creates a durable endpoint handler that can use step primitives for checkpointing.

- `handler` ((...args: any\[]) => any): A handler function compatible with the framework you're using. This would be the usual function you use for a request handler before wrapping in inngest.endpoint().Within this handler, you can use all step primitives (step.run(), step.sleep(), step.waitForEvent()) for durable execution.

**Returns:** A request handler for your framework.

```ts
export const handler = inngest.endpoint(
  async (req: Request): Promise<Response> => {
    const url = new URL(req.url);
    const id = url.searchParams.get("id");

    const result = await step.run("process", async () => {
      return await processItem(id);
    });

    return Response.json({ result });
  }
);
```

***

## Available Step Methods

Within a Durable Endpoint handler, you have access to all step methods: see [Available Step Methods](/docs-markdown/learn/inngest-steps#available-step-methods).

For example:

### `step.run(id, fn)`

Execute and checkpoint a function. If the endpoint is retried, completed steps return their cached result instantly.

```ts
const user = await step.run("fetch-user", async () => {
  return await db.users.findOne({ id: userId });
});
```

See [step.run() reference](/docs-markdown/reference/typescript/v4/functions/step-run) for full documentation.

### `step.sleep(id, duration)`

Pause execution for a specified duration. The endpoint will be resumed after the sleep completes.

```ts
await step.sleep("rate-limit-pause", "30s");
```

See [step.sleep() reference](/docs-markdown/reference/typescript/v4/functions/step-sleep) for full documentation.

### `step.waitForEvent(id, options)`

Wait for an external event before continuing. Useful for human-in-the-loop workflows.

```ts
const approval = await step.waitForEvent("wait-for-approval", {
  event: "approval/received",
  match: "data.requestId",
  timeout: "24h",
});
```

See [step.waitForEvent() reference](/docs-markdown/reference/typescript/v4/functions/step-wait-for-event) for full documentation.

***

## Passing Data to Endpoints

> **Callout:** POST body is not yet supported. Use query string parameters to pass data to Durable Endpoints. POST body support is coming soon.

```ts
export const handler = inngest.endpoint(async (req: Request): Promise<Response> => {
  const url = new URL(req.url);

  // Read data from query parameters
  const userId = url.searchParams.get("userId");
  const action = url.searchParams.get("action");

  // Process with durable steps
  const result = await step.run("process", async () => {
    return await processAction(userId, action);
  });

  return Response.json({ result });
});
```

***

## Returning Responses

However you return data in your framework is compatible with Durable Endpoints.

For example, using a regular Web API request:

```ts
// JSON response
return Response.json({ success: true, data: result });

// Text response
return new Response("OK", { status: 200 });

// Error response
return new Response(JSON.stringify({ error: "Not found" }), {
  status: 404,
  headers: { "Content-Type": "application/json" },
});
```

***

## Error Handling

Errors thrown within `step.run()` will trigger automatic retries. Use standard try/catch for custom error handling:

```ts
export const handler = inngest.endpoint(async (req: Request): Promise<Response> => {
  try {
    const result = await step.run("risky-operation", async () => {
      return await riskyAPICall();
    });

    return Response.json({ result });
  } catch (error) {
    // All retries exhausted, handle gracefully
    return Response.json(
      { error: "Operation failed after retries" },
      { status: 500 }
    );
  }
});
```

***

## Framework Integration

Durable Endpoints is only available for Bun and Next.js API endpoints.

[Reach out on Discord](/discord) to ask support for additional frameworks.

***

## Requesting a Durable Endpoint

Durable Endpoints behave like regular API endpoints on the success path. You can request them from your front-end (*or back-end*) using `fetch()` or your favorite query or http library.

When a failure triggers retries or long-running steps like `step.waitForEvent()`
are used, a Durable Endpoint redirects to a separate endpoint that waits for the
call to finish.

By default, this is an endpoint either in the Inngest Dev Server or Inngest
Cloud, depending on which environment you're in, but `inngest.endpointProxy()`
can be used to create your own URL to satisfy CORS constraints when the endpoint
is used from browsers.

```typescript
// When setting the `endpointAdapter`, use `.withOptions()` to set more config
const inngest = new Inngest({
  id: "my-app",
  endpointAdapter: endpointAdapter.withOptions({
    asyncRedirectUrl: "/wait",
  }),
});

// Then create the route with `inngest.endpointProxy()`
Bun.serve({
  port: 3000,
  routes: {
    "/process": ...,
    "/wait": inngest.endpointProxy(),
  },
});
```

Requests will now be redirected to `/wait`.