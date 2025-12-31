# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers.md

# Source: https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md

# Cloudflare Workers

<Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-js/tree/main/examples/cloudflare-workers" horizontal>
  You can find the project source code on GitHub.
</Card>

<Card title="Deploy With Cloudflare Workers" icon="cloudflare" href="https://deploy.workers.cloudflare.com/?url=https://github.com/upstash/qstash-workflow-example-cloudflare-workers" horizontal>
  Deploy the project to Cloudflare Workers with a single click.
</Card>

This guide provides detailed, step-by-step instructions on how to use and deploy Upstash Workflow with Cloudflare Workers. You can also explore our [Cloudflare Workers example](https://github.com/upstash/workflow-js/tree/main/examples/cloudflare-workers) or [Hono.js Cloudflare Workers example](https://github.com/upstash/workflow-js/tree/main/examples/cloudflare-workers-hono) for detailed, end-to-end examples and best practices.

## Prerequisites

1. An Upstash QStash API key.
2. Node.js and npm (another package manager) installed.

If you haven't obtained your QStash API key yet, you can do so by [signing up](https://console.upstash.com/login) for an Upstash account and navigating to your QStash dashboard.

## Step 1: Installation

First, install the Workflow SDK in your worker project:

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

Create a `.dev.vars` file in your project root and add your QStash token. This key is used to authenticate your application with the QStash service.

```bash Terminal theme={"system"}
touch .dev.vars
```

Upstash Workflow is powered by [QStash](/qstash/overall/getstarted), which requires access to your endpoint to execute workflows. When your app is deployed, QStash will use the app's URL. However, for local development, you have two main options: [use a local QStash server or set up a local tunnel](/workflow/howto/local-development).

### Option 1: Local QStash Server

To start the local QStash server, run:

```bash  theme={"system"}
npx @upstash/qstash-cli dev
```

Once the command runs successfully, you’ll see `QSTASH_URL` and `QSTASH_TOKEN` values in the console. Add these values to your `.dev.vars` file:

```txt .dev.vars theme={"system"}
QSTASH_URL="http://127.0.0.1:8080"
QSTASH_TOKEN="<QSTASH_TOKEN>"
```

This approach allows you to test workflows locally without affecting your billing. However, runs won't be logged in the Upstash Console.

### Option 2: Local Tunnel

Alternatively, you can set up a local tunnel. For this option:

1. Copy the `QSTASH_TOKEN` from the Upstash Console.
2. Update your `.dev.vars` file with the following:

```txt .dev.vars theme={"system"}
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

To define a workflow endpoint with Cloudflare Workers, navigate into your workers entrypoint file (usually `src/index.ts`) and add the following code:

```typescript src/index.ts theme={"system"}
import { serve } from "@upstash/workflow/cloudflare"

interface Env {
  ENVIRONMENT: "development" | "production"
}

export default serve<{ text: string }>(
  async (context) => {
    const initialPayload = context.requestPayload.text

    const result = await context.run("initial-step", async () => {
        console.log(`Step 1 running with payload: ${initialPayload}`)

        return { text: "initial step ran" }
      }
    )

    await context.run("second-step", async () => {
      console.log(`Step 2 running with result from step 1: ${result.text}`)
    })
  }
)
```

## Step 4: Run the Workflow Endpoint

To start your worker locally, run the following command:

```bash Terminal theme={"system"}
npm run wrangler dev
```

Executing this command prints a local URL to your workflow endpoint. By default, this URL is `http://localhost:8787`.

You can verify your correct environment variable setup by checking the wrangler output, which should now have access to your `QSTASH_TOKEN` binding and log your local URL:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=707cec511359835449c86699cb91de29" data-og-width="1122" width="1122" data-og-height="524" height="524" data-path="img/qstash-workflow/wrangler.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0015387b2cb15a57dc551aa28a97eb5a 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fefc9cb350d93dcc2ba2ae75af33444a 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=76795e5a692e024263b10123c4df1aa4 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0b95c822fdf5022159caa4bcdfe4f6cc 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1e347cb36ad119611d338dd3e7497c4d 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/wrangler.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e2a023d8ab3f3a7fc0d9eee18ba2ed37 2500w" />
</Frame>

Then, make a POST request to your workflow endpoint. For each workflow run, a unique workflow run ID is returned:

```bash Terminal theme={"system"}
curl -X POST https://localhost:8787/ -D '{"text": "hello world!"}'

# result: {"workflowRunId":"wfr_xxxxxx"}
```

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3536436ca84be611df74e8f0c9da3dd8" data-og-width="1765" width="1765" data-og-height="584" height="584" data-path="img/qstash-workflow/workers_local_request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=bcceb8996cb4efcfd07b66f2d6f41256 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=feaba5ae13295f5749cda6187322cb48 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5681fd9d6446929480e65e262360ccd6 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9f41dfd3fdcdf275a630ad42c8cb836b 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=de4a09255a54bc0e31d0d4d13ddb2d20 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/workers_local_request.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=44e6b099d57d05ef9d696a3d125e6177 2500w" />
</Frame>

See the [documentation on starting a workflow](/workflow/howto/start) for other ways you can start your workflow.

If you didn't set up local QStash development server, you can use this ID to track the workflow run and see its status in your QStash workflow dashboard. All steps are listed with their statuses, headers, and body for a detailed overview of your workflow from start to finish. Click on a step to see its detailed logs.

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d62fa91b9bcfc9c845105c42dae6f1e0" data-og-width="1656" width="1656" data-og-height="1080" height="1080" data-path="img/qstash-workflow/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8b59e83f0dc4ac843391ad758f34f0e8 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=000f796c9f6977bd9918ffcb657fbee3 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8609b0c44963e73b7be7b1eac2f855bf 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2a37385f1f54c7ed8597051b02dfb783 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=b2b4cdfe944c486ed4c73078c2509222 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c3a84ffafdd7cbe5b00be4e435dacf84 2500w" />
</Frame>

## Step 5: Deploying to Production

When deploying your Cloudflare Worker with Upstash Workflow to production, there are a few key points to keep in mind:

1. **Environment Variables**: Make sure that all necessary environment variables from your `.dev.vars` file are set in your Cloudflare Worker project settings. For example, your `QSTASH_TOKEN`, `ENVIRONMENT`, and any other configuration variables your workflow might need.

2. **Remove Local Development Settings**: In your production code, you can remove or conditionally exclude any local development settings. For example, if you used [local tunnel for local development](/workflow/howto/local-development#local-tunnel-with-ngrok)

3. **Deployment**: Deploy your Cloudflare Worker to production as you normally would, for example using the Cloudflare CLI:

   ```bash Terminal theme={"system"}
   wrangler deploy
   ```

4. **Verify Workflow Endpoint**: After deployment, verify that your workflow endpoint is accessible by making a POST request to your production URL:

   ```bash Terminal theme={"system"}
   curl -X POST https://<YOUR-PRODUCTION-URL>/ -D '{"text": "hello world!"}'
   ```

5. **Monitor in QStash Dashboard**: Use the QStash dashboard to monitor your production workflows. You can track workflow runs, view step statuses, and access detailed logs.

6. **Set Up Alerts**: Consider setting up alerts in Sentry or other monitoring tools to be notified of any workflow failures in production.

## Next Steps

1. Learn how to protect your workflow endpoint from unauthorized access by [securing your workflow endpoint](/workflow/howto/security).

2. Explore [the source code](https://github.com/upstash/workflow-js/tree/main/examples/cloudflare-workers) for a detailed, end-to-end example and best practices.

3. For setting up and testing your workflows in a local environment, check out our [local development guide](/workflow/howto/local-development).
