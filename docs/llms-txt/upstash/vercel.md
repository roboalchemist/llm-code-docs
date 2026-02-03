# Source: https://upstash.com/docs/workflow/troubleshooting/vercel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel

# Common Issues and Solutions

### Preview Deployment Protection

**Problem:**
When Deployment Protection setting is enabled on Vercel, it's not possible to trigger and complete a workflow run on a preview deployment.

**Solution:**
Vercel provides a way to bypass this protection by using a bypass secret. To create one, follow these steps:

<Steps>
  <Step title="Settings">Go to **Deployment Protection** section under your Vercel project settings.</Step>

  <Step title="Find related section">
    Click on **Add Secret** under **Protection Bypass for Automation** section.

    <Frame>
      <img src="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=f2009e2c2fef6af028da4fdad7171a33" data-og-width="1257" width="1257" data-og-height="827" height="827" data-path="img/workflow/troubleshooting/vercel-deployment-protection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=280&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=8f365114b95d945dc41b5e20dc753272 280w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=560&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=88ffcf217af52b1b8c0b44d2d9aa60bb 560w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=840&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=41f11cf66b9b17ef7f1d21aa03359b3d 840w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=1100&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=4fd84d87a095adc3ebbeac886341e6b4 1100w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=1650&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=9685a2db3af0c538dfff4942421b09eb 1650w, https://mintcdn.com/upstash/pBXejvUl5XQn4tWO/img/workflow/troubleshooting/vercel-deployment-protection.png?w=2500&fit=max&auto=format&n=pBXejvUl5XQn4tWO&q=85&s=715936038c9c5a5a9540274b343fe8aa 2500w" />
    </Frame>
  </Step>

  <Step title="Generate a bypass token">Don't forget to save it and store it as an environment variable (e.g., `VERCEL_AUTOMATION_BYPASS_SECRET`).</Step>
</Steps>

Now that you have a bypass token, you need to pass it as a header in two places to bypass deployment protection.

## Using the Bypass Secret

### Step 1: Configure QStash Client with Headers

[Configure the QStash client](/workflow/basics/serve/advanced#param-qstash-client) with the bypass header in your workflow serve options. This ensures that all workflow steps, including `context.invoke` calls, will include the bypass header automatically:

```ts  theme={"system"}
import { Client } from '@upstash/qstash'
import { serve } from '@upstash/workflow/nextjs'

export const { POST } = serve<string>(async (context) => {
  // your workflow logic
}, {
  qstashClient: new Client({
    token: process.env.QSTASH_TOKEN!,
    headers: {
      "x-vercel-protection-bypass": process.env.VERCEL_AUTOMATION_BYPASS_SECRET!
    }
  })
})
```

### Step 2: Pass Header When Triggering

When [triggering the workflow](/workflow/howto/start) using `curl` or `client.trigger`, you must also pass the bypass secret as a header:

<CodeGroup>
  ```ts client.trigger theme={"system"}
  import { Client } from "@upstash/workflow";

  const client = new Client({ token: "<QSTASH_TOKEN>" })

  await client.trigger({
    url: "https://vercel-preview.com/workflow",
    headers: {
      "x-vercel-protection-bypass": process.env.VERCEL_AUTOMATION_BYPASS_SECRET!
    },
    body: "Hello world!"
  })
  ```

  ```bash cURL theme={"system"}
  curl -X POST \
    'https://vercel-preview.com/workflow' \
    -H 'x-vercel-protection-bypass: <PROTECTION_BYPASS_SECRET>' \
    -d 'Hello world!'
  ```
</CodeGroup>

<Warning>
  Note that you should apply both of the steps above. The header must be passed when triggering the workflow AND configured in the QStash client for subsequent workflow steps to work properly.
</Warning>
