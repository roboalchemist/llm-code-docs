# Source: https://upstash.com/docs/workflow/quickstarts/nuxt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Nuxt

<Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-js/tree/main/examples/nuxt" horizontal>
  You can find the project source code on GitHub.
</Card>

<Card title="Deploy With Vercel" icon="triangle" iconType="sharp-solid" href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fupstash%2Fworkflow-js%2Ftree%2Fmain%2Fworkflow%2Fnuxt&env=QSTASH_TOKEN&envDescription=You%20can%20access%20this%20variable%20from%20Upstash%20Console%2C%20under%20QStash%20page.%20&project-name=workflow-nuxt&repository-name=workflow-nuxt&demo-title=Upstash%20Workflow%20Example&demo-description=A%20Nuxt%20application%20utilizing%20Upstash%20Workflow" horizontal>
  Deploy the project to Vercel with a single click.
</Card>

This guide provides detailed, step-by-step instructions on how to use and deploy Upstash Workflow with Nuxt.js. You can also explore our [Nuxt example](https://github.com/upstash/workflow-js/tree/main/examples/nuxt) for a detailed, end-to-end example and best practices.

## Prerequisites

1. An Upstash QStash API key.
2. Node.js and npm (another package manager) installed.

If you haven't obtained your QStash API key yet, you can do so by [signing up](https://console.upstash.com/login) for an Upstash account and navigating to your QStash dashboard.

## Step 1: Installation

First, install the Workflow SDK in your Nuxt project:

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

## Step 2: Configure Environment Variables

Create a `.env.local` file in your project root and add your QStash token. This token is used to authenticate your application with the QStash service.

```bash Terminal theme={"system"}
touch .env.local
```

Upstash Workflow is powered by [QStash](/qstash/overall/getstarted), which requires access to your endpoint to execute workflows. When your app is deployed, QStash will use the app's URL. However, for local development, you have two main options: [use a local QStash server or set up a local tunnel](/workflow/howto/local-development).

### Option 1: Local QStash Server

To start the local QStash server, run:

```bash  theme={"system"}
npx @upstash/qstash-cli dev
```

Once the command runs successfully, you’ll see `QSTASH_URL` and `QSTASH_TOKEN` values in the console. Add these values to your `.env.local` file:

```txt  theme={"system"}
QSTASH_URL="http://127.0.0.1:8080"
QSTASH_TOKEN="<QSTASH_TOKEN>"
```

This approach allows you to test workflows locally without affecting your billing. However, runs won't be logged in the Upstash Console.

### Option 2: Local Tunnel

Alternatively, you can set up a local tunnel. For this option:

1. Copy the `QSTASH_TOKEN` from the Upstash Console.
2. Update your `.env.local` file with the following:

```txt  theme={"system"}
QSTASH_TOKEN="***"
UPSTASH_WORKFLOW_URL="<UPSTASH_WORKFLOW_URL>"
```

* Replace `***` with your actual QStash token.
* Set `UPSTASH_WORKFLOW_URL` to the public URL provided by your local tunnel.

Here’s where you can find your QStash token:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=df12ba48119bcdd13a675e53b43ab74d" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c251f0eeb0a6973ff498f9e9930aed70 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d452c08e1a638dff258d938aa8544f25 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6b197538fe5190c7936b751ec228ef39 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=63da8b3df03c88ff0a7700af7a5db6fb 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8df98665037cf63deb6b48d5c22d3f6b 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3ef0ab4137bdec59b7cb772550933e1 2500w" />
</Frame>

Using a local tunnel connects your endpoint to the production QStash, enabling you to view workflow logs in the Upstash Console.

## Step 3: Create a Workflow Endpoint

A workflow endpoint allows you to define a set of steps that, together, make up a workflow. Each step contains a piece of business logic that is automatically retried on failure, with easy monitoring via our visual workflow dashboard.

To define a workflow endpoint in a Nuxt.js project, navigate into the Nuxt.js `server/api` directory and create a new file, for example called `workflow.ts`. This file will contain your workflow:

```typescript server/api/workflow.ts theme={"system"}
import { serve } from "@upstash/workflow/h3"

const { handler } = serve(
  async (context) => {
    await context.run("initial-step", () => {
      console.log("initial step ran")
    })

    await context.run("second-step", () => {
      console.log("second step ran")
    })
  },
)

export default handler;
```

## Step 4: Run the Workflow Endpoint

After defining the endpoint, you can trigger your workflow by starting your app:

```bash Terminal theme={"system"}
npm run dev
```

Then, make a POST request to your workflow endpoint. For each workflow run, a unique workflow run ID is returned:

```bash Terminal theme={"system"}
curl -X POST https://localhost:3000/api/workflow

# result: {"workflowRunId":"wfr_xxxxxx"}
```

See the [documentation on starting a workflow](/workflow/howto/start) for other ways you can start your workflow.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4f2cbb67caa1985c680629d89c96fca4" data-og-width="1737" width="1737" data-og-height="634" height="634" data-path="img/qstash-workflow/nextjs_local_request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f41c789c5b932b1f055c0e268e5b9605 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=22cbc44e0f95850cc384949d6f7d89ae 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c87b767a909164536ed792b237ab7cb2 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=42d2f62728e193974c5cec61189918fa 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e1fabf80bcfe0aa313e60c593f807356 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1b5e61b1b8b06d07a84ac2f5f34810b0 2500w" />
</Frame>

If you are using a local tunnel, you can use this ID to track the workflow run and see its status in your QStash workflow dashboard. All steps are listed with their statuses, headers, and body for a detailed overview of your workflow from start to finish. Click on a step to see its detailed logs.

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d62fa91b9bcfc9c845105c42dae6f1e0" data-og-width="1656" width="1656" data-og-height="1080" height="1080" data-path="img/qstash-workflow/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8b59e83f0dc4ac843391ad758f34f0e8 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=000f796c9f6977bd9918ffcb657fbee3 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8609b0c44963e73b7be7b1eac2f855bf 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2a37385f1f54c7ed8597051b02dfb783 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=b2b4cdfe944c486ed4c73078c2509222 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c3a84ffafdd7cbe5b00be4e435dacf84 2500w" />
</Frame>

## Step 5: Deploying to Production

When deploying your Nuxt.js application with Upstash Workflow to production, there are a few key points to keep in mind:

1. **Environment Variables**: Make sure that all necessary environment variables are set in your platforms project settings. For example, your `QSTASH_TOKEN` and any other configuration variables your workflow might need.

2. **Remove Local Development Settings**: In your production code, you can remove or conditionally exclude any local development settings. For example, if you used [local tunnel for local development](/workflow/howto/local-development#local-tunnel-with-ngrok)

3. **Deployment**: Deploy your Nuxt application to Vercel, Cloudflare Pages or other platforms as you normally would. These platforms will automatically detect and build your Nuxt application.

4. **Verify Workflow Endpoint**: After deployment, verify that your workflow endpoint is accessible by making a POST request to your production URL:

   ```bash Terminal theme={"system"}
   curl -X POST https://<YOUR-PRODUCTION-URL>/api/workflow
   ```

5. **Monitor in QStash Dashboard**: Use the QStash dashboard to monitor your production workflows. You can track workflow runs, view step statuses, and access detailed logs.

6. **Set Up Alerts**: Consider setting up alerts in Sentry or other monitoring tools to be notified of any workflow failures in production.

## Next Steps

1. Learn how to protect your workflow endpoint from unauthorized access by [securing your workflow endpoint](/workflow/howto/security).

2. Explore [the source code](https://github.com/upstash/workflow-js/tree/main/examples/nuxt) for a detailed, end-to-end example and best practices.

3. For setting up and testing your workflows in a local environment, check out our [local development guide](/workflow/howto/local-development).
