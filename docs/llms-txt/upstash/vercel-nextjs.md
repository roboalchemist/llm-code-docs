# Source: https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md

# Next.js

This guide provides step-by-step instructions on how to use and deploy Upstash Workflow with Next.js.

<Columns cols={2}>
  <Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-js/tree/main/examples/nextjs" horizontal>
    You can find the project source code on GitHub.
  </Card>

  <Card title="Deploy With Vercel" icon="triangle" iconType="sharp-solid" href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fupstash%2Fworkflow-js%2Ftree%2Fmain%2Fworkflow%2Fnextjs&env=QSTASH_TOKEN&envDescription=You%20can%20access%20this%20variable%20from%20Upstash%20Console%2C%20under%20QStash%20page.%20&project-name=workflow-nextjs&repository-name=workflow-nextjs&demo-title=Upstash%20Workflow%20Example&demo-description=A%20Next.js%20application%20utilizing%20Upstash%20Workflow" horizontal>
    Deploy the project to Vercel with a single click.
  </Card>
</Columns>

## Prerequisites

* Node.js and npm (or another package manager) installed.

You can integrate Upstash Workflow into an existing Next.js app, or follow [this guide](https://nextjs.org/docs/app/getting-started/installation) to create a new Next.js project from scratch.

## Step 1: Installation

Run the following command to install the Upstash Workflow SDK in your Next.js app.

<Tabs>
  <Tab title="npm">
    ```bash  theme={"system"}
    npm install @upstash/workflow
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash  theme={"system"}
    pnpm install @upstash/workflow
    ```
  </Tab>

  <Tab title="bun">
    ```bash  theme={"system"}
    bun add @upstash/workflow
    ```
  </Tab>
</Tabs>

## Step 2: Run the development server

Upstash Workflow is built on top of Upstash QStash.

In a production environment, your application connects to the managed QStash servers hosted by Upstash.
This ensures that requests are delivered reliably, securely, and at scale without requiring you to run and maintain your own infrastructure.

For local development, you don't need to depend on the managed QStash servers. Instead, you can run a local QStash server directly on your machine.
This local server behaves just like the production version but does not require external network calls.

Start the local server with:

<Tabs>
  <Tab title="npm">
    ```bash  theme={"system"}
    npx @upstash/qstash-cli dev
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash  theme={"system"}
    pnpx @upstash/qstash-cli dev
    ```
  </Tab>
</Tabs>

When the server starts, it will print the credentials.
You'll need these values in the next step to connect your Next.js app to QStash.

You can enable local mode in the Upstash Workflow dashboard to use the UI while developing locally.

<Frame>
  <img src="https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=894b9d6a3d2dff99bed21683c3c01cd7" alt="Enable local mode on dashboard" data-og-width="2758" width="2758" data-og-height="1864" height="1864" data-path="img/qstash-workflow/local-dev.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=280&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=c408f8a396e346fc6bf86ce33f6453aa 280w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=560&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=b7c0049c3a1839305582c18b129192a5 560w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=840&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=85086a3a005d121cf4051e3ac405b1b0 840w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=1100&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=ba2c2aeb93018bf368c662d6424fc52d 1100w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=1650&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=35927ba49e0412a5658b869ee582b0c1 1650w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/local-dev.png?w=2500&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=8f4dd395f0da6319f1d412b654749366 2500w" />
</Frame>

## Step 3: Configure Environment Variables

Next, you need to configure your Next.js app to connect with the local QStash server by setting environment variables.

In the root of your project, create a `.env.local` file (or update your existing one) and add the values printed by the QStash local server:

```txt  theme={"system"}
QSTASH_URL="http://127.0.0.1:8080"
QSTASH_TOKEN="eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0="
QSTASH_CURRENT_SIGNING_KEY="sig_7kYjw48mhY7kAjqNGcy6cr29RJ6r"
QSTASH_NEXT_SIGNING_KEY="sig_5ZB6DVzB1wjE8S6rZ7eenA8Pdnhs"
```

<Tip>
  For production, replace these with your actual credentials from the Upstash Workflow dashboard.
</Tip>

## Step 3: Create a Workflow Endpoint

With your environment ready, the next step is to define your first workflow endpoint.

In Upstash Workflow, every workflow is exposed as an endpoint.
Every endpoint you expose using the SDK’s `serve()` function acts as a workflow that can be triggered independently.

In Next.js, these endpoints are implemented as **API routes**.

Create the file according to your router setup:

* App Router → put the endpoint under `app/api`
* Pages Router → put the endpoint under `pages/api`

<Tabs>
  <Tab title="App router">
    ```typescript app/api/workflow/route.ts theme={"system"}
    import { serve } from "@upstash/workflow/nextjs"

    export const { POST } = serve(
      async (context) => {
        await context.run("initial-step", () => {
          console.log("initial step ran")
        })

        await context.run("second-step", () => {
          console.log("second step ran")
        })
      }
    )
    ```
  </Tab>

  <Tab title="App router with request object">
    ```typescript app/api/workflow/route.ts theme={"system"}
    import { serve } from "@upstash/workflow/nextjs";
    import { NextRequest } from "next/server";

    export const POST = async (request: NextRequest) => {
      // do something with the native request object
      const { POST: handler } = serve(async (context) => {
        // Your workflow steps
      });

      return await handler(request);
    }
    ```
  </Tab>

  <Tab title="Pages Router">
    ```typescript src/pages/api/workflow.ts theme={"system"}
    import { servePagesRouter } from "@upstash/workflow/nextjs";

    const { handler } = servePagesRouter<string>(
      async (context) => {
        await context.run("initial-step", () => {
          console.log("initial step ran")
        })

        await context.run("second-step", () => {
          console.log("second step ran")
        })
      }
    )
    export default handler;
    ```
  </Tab>

  <Tab title="Pages Router with request object">
    ```typescript src/pages/api/workflow.ts theme={"system"}
    import type { NextApiRequest, NextApiResponse } from "next";
    import { servePagesRouter } from "@upstash/workflow/nextjs";

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      // do something with the native request object
      const { handler } = servePagesRouter(
        async (context) => {
          // Your workflow steps
        }
      )

      await handler(req, res)
    }
    ```
  </Tab>
</Tabs>

## Step 4: Run the Workflow Endpoint

Once your endpoint is defined, the next step is to trigger a workflow run.

You can start a new workflow run using the `trigger()` function from the Upstash Workflow SDK.

```javascript  theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: process.env.QSTASH_TOKEN! })

const { workflowRunId } = await client.trigger({
  url: `http://localhost:3000/api/workflow`,
  retries: 3,
  keepTriggerConfig: true,
});
```

<Info>
  The `trigger()` function should typically be called from a server-side action (not directly in client-side code) to keep your credentials secure.
</Info>

Check the Upstash Workflow dashboard to view logs of your workflow run:

<Frame>
  <img src="https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=e3f20497f5d50f6bfec30b4ed8ee90ff" alt="Debug a workflow run on UI" data-og-width="2758" width="2758" data-og-height="1864" height="1864" data-path="img/qstash-workflow/run-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=280&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=96c8fe0b3cb3662f3e41398a382cecbf 280w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=560&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=14594dfb7ed28e821056fabb40097a70 560w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=840&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=8f1b7a01cea89106d227d1d0372a1cc2 840w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=1100&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=9af11ef94799753afbd2c1c0953e76c3 1100w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=1650&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=be5d6a683aabc669a23a571e9c32bf1a 1650w, https://mintcdn.com/upstash/fkAt_mKC7aEhsSVz/img/qstash-workflow/run-view.png?w=2500&fit=max&auto=format&n=fkAt_mKC7aEhsSVz&q=85&s=5e629fdf6f7dec028a97a9ce467030ba 2500w" />
</Frame>

<Tip>
  Inside the `trigger()` call, you need to provide the URL of your workflow endpoint:

  * Local development → use the URL where your app is running, for example: [http://localhost:3000/api/PATH](http://localhost:3000/api/PATH)
  * Production → use the URL of your deployed app, for example: [https://yourapp.com/api/PATH](https://yourapp.com/api/PATH)

  To avoid hardcoding URLs, you can define a `BASE_URL` constant and set it based on the environment.
  A common pattern is to check an environment variable that only exists in production:

  ```javascript  theme={"system"}
  const BASE_URL = process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : `http://localhost:3000`

  const { workflowRunId } = await client.trigger({
    url: `${BASE_URL}/api/workflow`,
    retries: 3,
    keepTriggerConfig: true,
  });
  ```
</Tip>

## Step 5: Deploying to Production

You now have everything you need to deploy your application to production! 🎉

Before deploying, make sure your configuration no longer relies on local development settings:

* **Workflow URL**: Update the `trigger()` call to use your production domain (see the tip above for using a dynamic `BASE_URL`).
* **Credentials**: Replace local QStash credentials with your production tokens.
* **Environment Variables**: Verify that all required variables are set correctly in your deployment environment.

## Next Steps

Now that you've created and deployed your first workflow, here are some recommended guides to continue learning:

1. **[Learn the Workflow API](/workflow/basics/context)**: Dive deeper into the full API surface and advanced capabilities.

2. **[Configure Workflow Runs](/workflow/basics/client)**: Learn how to configure workflow execution to fit your app's needs.

3. **[Handle Failures](/workflow/howto/failures)**: Understand how to detect and recover from failed workflow runs.
