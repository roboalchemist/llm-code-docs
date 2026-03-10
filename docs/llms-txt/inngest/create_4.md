# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/client/create

# Create the Inngest Client

The `Inngest` client object is used to configure your application, enabling you to create functions and send events.

```ts
import { Inngest } from "inngest";

const inngest = new Inngest({
  id: "my-application",
});

```

***

## Configuration

- `id` (string): A unique identifier for your application. We recommend a hyphenated slug.

* `baseUrl` (string): Override the default (https\://inn.gs/) base URL for sending events. See also the INNGEST\_BASE\_URL environment variable.

- `env` (string): The environment name. Required only when using Branch Environments.

* `eventKey` (string): An Inngest Event Key. Alternatively, set the INNGEST\_EVENT\_KEY environment variable.

- `fetch` (Fetch API compatible interface): Override the default
  fetch
  implementation. Defaults to the runtime's native Fetch API.If you need to specify this, make sure that you preserve the function's binding, either by using .bind or by wrapping it in an anonymous function.

* `signingKey` (string): The signing key used to authenticate with Inngest Cloud. We recommend setting this via the INNGEST\_SIGNING\_KEY environment variable instead.

- `signingKeyFallback` (string): A fallback signing key, useful during key rotation. We recommend setting this via the INNGEST\_SIGNING\_KEY\_FALLBACK environment variable instead.

* `isDev` (boolean): Set to true to force Dev mode, setting default local URLs and turning off
  signature verification, or force Cloud mode with false. Alternatively, set INNGEST\_DEV.

- `logger` (Logger): A logger object that provides .info(), .warn(), .error(), and .debug() methods. The SDK uses Pino-style object-first logging. For string-first loggers like Winston, use wrapStringFirstLogger. Defaults to new ConsoleLogger(\{ level: "info" }) if not provided. See the logging reference for details.import \{ ConsoleLogger, Inngest } from "inngest";

  export const inngest = new Inngest(\{
  &#x20; id: "my-app",
  &#x20; logger: new ConsoleLogger(\{ level: "debug" }),
  });

* `internalLogger` (Logger): A separate logger for SDK internal messages (registration, request handling, middleware errors). If not provided, falls back to logger. Use this to route SDK internals separately from your function logs. See the logging reference for details.

- `middleware` (array): A stack of middleware to add to the client.

> **Callout:** We recommend setting the INNGEST\_EVENT\_KEY as an environment variable over using the eventKey option. As with any secret, it's not a good practice to hard-code the event key in your codebase.

## Cloud Mode and Dev Mode

An SDK can run in two separate "modes:" **Cloud** or **Dev**.

- **Cloud Mode**
  - 🔒 Signature verification **ON**
  - Defaults to communicating with Inngest Cloud (e.g. `https://api.inngest.com`)
- **Dev Mode**
  - ❌ Signature verification **OFF**
  - Defaults to communicating with an Inngest Dev Server (e.g. `http://localhost:8288`)

You can force either Dev or Cloud Mode by setting
[`INNGEST_DEV`](/docs-markdown/sdk/environment-variables#inngest-dev) or the
[`isDev`](#configuration) option.

If no mode is explicitly set, the SDK will default to **cloud mode** to ensure that Inngest applications are more secure by default. You can use `INNGEST_DEV` or `isDev=true` to let the SDK know that you are intentionally using development mode.

## Best Practices

### Share your client across your codebase

Instantiating the `Inngest` client in a single file and sharing it across your codebase is ideal as you only need a single place to configure your client and define types which can be leveraged anywhere you send events or create functions.

```ts
import { Inngest } from "inngest";

export const inngest = new Inngest({ id: "my-app" });

```

```ts {{ filename: './inngest/myFunction.ts' }}
import { inngest } from "./client";

export default inngest.createFunction(...);
```

### Handling multiple environments with middleware

If your client uses middleware, that middleware may import dependencies that are not supported across multiple environments such as "Edge" and "Serverless" (commonly with either access to WebAPIs or Node).

In this case, we'd recommend creating a separate client for each environment, ensuring Node-compatible middleware is only used in Node-compatible environments and vice versa.

This need is common in places where function execution should declare more involved middleware, while sending events from the edge often requires much less.

```ts
// inngest/client.ts
import { Inngest } from "inngest";
import { nodeMiddleware } from "some-node-middleware";

export const inngest = new Inngest({
  id: "my-app",
  middleware: [nodeMiddleware],
});

// inngest/edgeClient.ts
import { Inngest } from "inngest";

export const inngest = new Inngest({
  id: "my-app-edge",
});

```

Also see [Referencing functions](/docs-markdown/functions/references), which can help you invoke functions across these environments without pulling in any dependencies.