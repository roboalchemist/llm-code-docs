# Source: https://docs.base44.com/developers/backend/overview/local-dev/get-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Local development setup

> Set up the Base44 dev server and connect your frontend to it

Local development runs two processes side by side. The Base44 dev server handles your backend, and your usual frontend dev server runs the UI. Your frontend talks to the local backend through the SDK.

## Prerequisites

If your project has backend functions, you need to install [Deno](https://docs.deno.com/runtime/getting_started/installation/) to run them locally.

## Configure your frontend client

If your project has a frontend that uses the SDK, you need to tell it where to send requests. By default, the SDK sends requests to Base44's hosted backend. To use the local dev server instead, pass `serverUrl` to your client configuration when running in development mode. In production, omit `serverUrl` so the SDK uses its default.

The approach is to detect whether your code is running in a development environment, then conditionally set `serverUrl` to point at the local dev server. Most frameworks provide a built-in way to check this.

<Steps>
  <Step title="Detect development mode">
    Use the pattern that matches your environment:

    <CodeGroup>
      ```javascript Vite theme={null}
      const isDev = import.meta.env.DEV;
      ```

      ```javascript Node.js, Webpack, Next.js theme={null}
      const isDev = process.env.NODE_ENV !== "production";
      ```

      ```javascript React Native theme={null}
      const isDev = __DEV__;
      ```

      ```javascript Deno theme={null}
      const isDev = Deno.env.get("DENO_ENV") !== "production";
      ```
    </CodeGroup>
  </Step>

  <Step title="Pass serverUrl conditionally">
    When creating the client, include `serverUrl` only in development:

    ```javascript  theme={null}
    import { createClient } from "@base44/sdk";

    const base44 = createClient({
      appId: "your-app-id",
      ...(isDev && { serverUrl: "http://localhost:4400" }),
    });
    ```

    * In development, `isDev` is `true` and the SDK sends requests to `localhost:4400`
    * In production builds, `isDev` is `false`, `serverUrl` is omitted, and the SDK uses the default Base44 backend
  </Step>
</Steps>

## Run the dev servers

Each time you develop locally, you need two terminals running side by side.

<Steps>
  <Step title="Start the backend">
    In one terminal, run [`dev`](/developers/references/cli/commands/dev) from your project directory:

    ```bash  theme={null}
    base44 dev
    ```

    This starts the local backend on `http://localhost:4400`.
  </Step>

  <Step title="Start the frontend">
    In a second terminal, start your frontend dev server as you normally would. For example, with Vite:

    ```bash  theme={null}
    npm run dev
    ```

    All SDK calls from your frontend now go to the local Base44 dev server.
  </Step>
</Steps>

## See also

* [Local development overview](/developers/backend/overview/local-dev/local-development-overview): What runs locally, what's forwarded, and how it works
* [`dev`](/developers/references/cli/commands/dev): CLI command reference with flags
* [`serverUrl`](/developers/references/sdk/docs/interfaces/CreateClientConfig): SDK client configuration


Built with [Mintlify](https://mintlify.com).