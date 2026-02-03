# Source: https://trigger.dev/docs/guides/frameworks/nextjs-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Triggering tasks with webhooks in Next.js

> Learn how to trigger a task from a webhook in a Next.js app.

## Prerequisites

* [A Next.js project, set up with Trigger.dev](/guides/frameworks/nextjs)
* [cURL](https://curl.se/) installed on your local machine. This will be used to send a POST request to your webhook handler.

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/nextjs-webhooks/my-app">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Adding the webhook handler

The webhook handler in this guide will be an API route.

This will be different depending on whether you are using the Next.js pages router or the app router.

### Pages router: creating the webhook handler

Create a new file `pages/api/webhook-handler.ts` or `pages/api/webhook-hander.js`.

In your new file, add the following code:

```ts /pages/api/webhook-handler.ts theme={"theme":"css-variables"}
import { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  // Parse the webhook payload
  const payload = req.body;

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  res.status(200).json({ message: "OK" });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

### App router: creating the webhook handler

Create a new file in the `app/api/webhook-handler/route.ts` or `app/api/webhook-handler/route.js`.

In your new file, add the following code:

```ts /app/api/webhook-handler/route.ts theme={"theme":"css-variables"}
import type { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  // Parse the webhook payload
  const payload = await req.json();

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  return NextResponse.json("OK", { status: 200 });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

## Triggering the task locally

Now that you have your webhook handler set up, you can trigger the 'Hello World' task from it. We will do this locally using cURL.

<Steps>
  <Step title="Run your Next.js app and the Trigger.dev dev server">
    First, run your Next.js app.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npm run dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm run dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dev
      ```
    </CodeGroup>

    Then, open up a second terminal window and start the Trigger.dev dev server:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Trigger the webhook with some dummy data">
    To send a POST request to your webhook handler, open up a terminal window on your local machine and run the following command:

    <Tip>
      If `http://localhost:3000` isn't the URL of your locally running Next.js app, replace the URL in
      the below command with that URL instead.
    </Tip>

    ```bash  theme={"theme":"css-variables"}
    curl -X POST -H "Content-Type: application/json" -d '{"Name": "John Doe", "Age": "87"}' http://localhost:3000/api/webhook-handler
    ```

    This will send a POST request to your webhook handler, with a JSON payload.
  </Step>

  <Step title="Check the task ran successfully">
    After running the command, you should see a successful dev run and a 200 response in your terminals.

    If you now go to your [Trigger.dev dashboard](https://cloud.trigger.dev), you should also see a successful run for the 'Hello World' task, with the payload you sent, in this case; `{"name": "John Doe", "age": "87"}`.
  </Step>
</Steps>

## Learn more about Next.js and Trigger.dev

### Walk-through guides from development to deployment

<CardGroup cols={2}>
  <Card title="Next.js - setup guide" icon="N" href="/guides/frameworks/nextjs">
    Learn how to setup Trigger.dev with Next.js, using either the pages or app router.
  </Card>

  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/guides/frameworks/nextjs-webhooks">
    Learn how to create a webhook handler for incoming webhooks in a Next.js app, and trigger a task from it.
  </Card>
</CardGroup>

### Task examples

<CardGroup cols={2}>
  <Card title="Fal.ai with Realtime in Next.js" img="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9ac31bb57678b222a82b04055184eea0" href="/guides/examples/fal-ai-realtime" data-og-width="1442" width="1442" data-og-height="812" height="812" data-path="images/fal-realtime-thumbnail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=086231461af2b9520f9200889fc04724 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c5ab58baba8000266aac79117dc8944d 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=988fe253a646e5af2188f81297d01897 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=db65bbdf0995fc1ac72bda2512c31800 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=6e7890d597065f8bc9edd0ac90257185 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=60bc05bc63c0c1d1ad59eaafb0808aa6 2500w">
    Generate an image from a prompt using Fal.ai and Trigger.dev Realtime.
  </Card>

  <Card title="Generate a cartoon using Fal.ai in Next.js" img="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=003d7870f36310d14ca9a71a952667d3" href="/guides/examples/fal-ai-image-to-cartoon" data-og-width="1442" width="1442" data-og-height="816" height="816" data-path="images/fal-generate-cartoon-thumbnail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ec0e05813f874082257e2d32bad407a8 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f3f70889ad11953d44f72224712722aa 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b8df38a222a7431d55a1af1af61dffd1 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=268ac6b0faf34bb46a8a8d676658b0b8 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4be96f4df2d49b7a71d0e960df9cc93b 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=bc15e1a3df4484cfdcd200d49fd1ac4b 2500w">
    Convert an image to a cartoon using Fal.ai.
  </Card>

  <Card title="Vercel sync environment variables" icon="code" href="/guides/examples/vercel-sync-env-vars">
    Learn how to automatically sync environment variables from your Vercel projects to Trigger.dev.
  </Card>

  <Card title="Vercel AI SDK" icon="code" href="/guides/examples/vercel-ai-sdk">
    Learn how to use the Vercel AI SDK, which is a simple way to use AI models from different
    providers, including OpenAI, Anthropic, Amazon Bedrock, Groq, Perplexity etc.
  </Card>
</CardGroup>
