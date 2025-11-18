# Source: https://upstash.com/docs/workflow/features/failure-callback.md

# Overview

When you define a workflow endpoint, you can attach a failure function to the workflow that allows you to execute custom logic when a workflow run fails after exhausting all retry attempts.

This feature ensures that you can perform cleanup operations, logging, alerting, or any other custom error handling logic before the failed workflow run is moved to the Dead Letter Queue (DLQ).

<Frame caption="Failure function is executed automatically when worklow run fails">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=65d05df8e2b6870a0f71164fbcac04b8" data-og-width="2728" width="2728" data-og-height="2068" height="2068" data-path="img/workflow/failure_function.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=adbc4d16270f2deb60df588faaa7c84c 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=1dbced323d50902d0175292eaa88e64c 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=b1a91a444c572359d726bf255d568f55 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=06a319628696f4af84f5423af228ff62 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=c198b70450e9d331aae0071f3f4b2570 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/failure_function.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=de7f0d18b7530df7f59ecf22ccf45089 2500w" />
</Frame>

The failure function automatically receives the workflow run context and the reason for the failure, so you can decide how to handle it.

<CodeGroup>
  ```typescript TypeScript theme={"system"}
  import { serve } from "@upstash/workflow/nextjs";

  export const { POST } = serve<string>(
    async (context) => {
      // Your workflow logic...
    },
    {
      failureFunction: async ({
        context,
        failStatus,
        failResponse,
        failHeaders,
      }) => {

        // 👇 Log error to monitoring system
        await logToSentry(...);

        // 👇 Send alert to team
        await sendSlackAlert(...);

        // 👇 Perform cleanup operations
        await cleanupWorkflowResources(...);
      },
    }
  ```

  );
</CodeGroup>

You cannot create new workflow steps inside the `failureFunction` using `context`.
The `context` provided here is only meant to expose workflow run properties (like URL, payload, and headers).
Think of the failure function as an individual `context.run` step. It executes once with the provided context but cannot define further steps.

<Info>
  If you use a custom authorization method to secure your workflow endpoint, add authorization to the `failureFunction` too.
  Otherwise, anyone could invoke your failure function with a request.

  Read more here: [securing your workflow endpoint](/workflow/howto/security).
</Info>

## Parameters

The `failureFunction` receives an object with the following parameters:

<ParamField body="context" type="object">
  The workflow context object containing:

  <Expandable>
    <ParamField body="workflowRunId" type="string">
      The ID of the failed workflow run
    </ParamField>

    <ParamField body="url" type="string">
      The publicly accessible workflow endpoint URL
    </ParamField>

    <ParamField body="requestPayload" type="string">
      The original request payload that triggered the workflow
    </ParamField>

    <ParamField body="headers" type="string">
      The original request headers
    </ParamField>

    <ParamField body="env" type="string">
      Environment variables
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="failStatus" type="number">
  The HTTP status code returned by the failed workflow step.
</ParamField>

<ParamField body="failResponse" type="number">
  The response body returned by the failed workflow step.
</ParamField>

<ParamField body="failHeaders" type="number">
  The response headers returned by the failed workflow step.
</ParamField>

## Configuration

You can enable failure function for a workflow run when starting it:

```typescript Configure Retry Attempt Count theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  // 👇 Activates the failure function execution if it is defined
  useFailureFunction: true,
  keepTriggerConfig: true,
})
```
