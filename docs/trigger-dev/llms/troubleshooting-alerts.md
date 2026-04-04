# Source: https://trigger.dev/docs/troubleshooting-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts

> Get alerted when runs or deployments fail, or when deployments succeed.

We support receiving alerts for the following events:

* Run fails
* Deployment fails
* Deployment succeeds

## How to setup alerts

<Steps>
  <Step title="Create a new alert">
    Click on "Alerts" in the left hand side menu, then click on "New alert" to open the new alert modal.
    <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=66c28b50c37b92057afb4100948a6636" alt="Email alerts" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/troubleshooting-alerts-blank.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4b176aea4b6f3e15ffafca6e6929fa2d 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=7af7993456f897b29380e66137621443 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=095859343aefb995f836a40ecf8d637c 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=90f54ae0228df8ab27f24c1d0e2f5565 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e1e789dd4b16aa5fc5e40572c68878c5 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=6a45670b1c9e59da3cf3bfa6264af742 2500w" />
  </Step>

  <Step title="Choose your alert method">
    Choose to be notified by email, Slack notification or webhook whenever:

    * a run fails
    * a deployment fails
    * a deployment succeeds

      <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=69b2a564572a6b1fb1c5e3ee77d68c4a" alt="Email alerts" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/troubleshooting-alerts-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=3aaa12fe0241588d4f157848c12c60a9 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=d019d5515cecb2e093eff24458c9b18c 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=c2a0eefbce2ea17136c9ac531f2db3be 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=8bcfd8fcb725b464a6f26bd468c7907d 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=08cbccd0804107670b39370c6acaa828 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f6289e4f7dde170ab8b5ad4dab7b3fd0 2500w" />
  </Step>

  <Step title="Delete or disable alerts">
    Click on the triple dot menu on the right side of the table row and select "Disable" or "Delete".

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f3455ed01b0d4c7a66c855a3b7d0cc53" alt="Disable and delete alerts" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/troubleshooting-alerts-disable-delete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4a113eb9f70076a7e01425611f730ac4 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=c0b37bb579300563f46764736b233bf2 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=7651daf08e2fbaec97c7e31794814803 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0db4fa3993c9ef5bd1e4b853e1a2f07e 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f1d0e716322507096dc7f4ffed03d3fe 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ee5bf9572279a5a571b6cc33fc2d2a59 2500w" />
  </Step>
</Steps>

## Alert webhooks

For the alert webhooks you can use the SDK to parse them. Here is an example of how to parse the webhook payload in Remix:

```ts  theme={"theme":"css-variables"}
import { ActionFunctionArgs, json } from "@remix-run/server-runtime";
import { webhooks, WebhookError } from "@trigger.dev/sdk";

export async function action({ request }: ActionFunctionArgs) {
  // Make sure this is a POST request
  if (request.method !== "POST") {
    return json({ error: "Method not allowed" }, { status: 405 });
  }

  try {
    // Construct and verify the webhook event
    // This secret can be found on your Alerts page when you create a webhook alert
    const event = await webhooks.constructEvent(request, process.env.ALERT_WEBHOOK_SECRET!);

    // Process the event based on its type
    switch (event.type) {
      case "alert.run.failed": {
        console.log("[Webhook Internal Test] Run failed alert webhook received", { event });
        break;
      }
      case "alert.deployment.success": {
        console.log("[Webhook Internal Test] Deployment success alert webhook received", { event });
        break;
      }
      case "alert.deployment.failed": {
        console.log("[Webhook Internal Test] Deployment failed alert webhook received", { event });
        break;
      }
      default: {
        console.log("[Webhook Internal Test] Unhandled webhook type", { event });
      }
    }

    // Return a success response
    return json({ received: true }, { status: 200 });
  } catch (err) {
    // Handle webhook errors
    if (err instanceof WebhookError) {
      console.error("Webhook error:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    if (err instanceof Error) {
      console.error("Error processing webhook:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    // Handle other errors
    console.error("Error processing webhook:", { err });
    return json({ error: "Internal server error" }, { status: 500 });
  }
}
```

### Common properties

When you create a webhook alert, you'll receive different payloads depending on the type of alert. All webhooks share some common properties:

<ParamField path="id" type="string">
  A unique identifier for this webhook event
</ParamField>

<ParamField path="created" type="datetime">
  When this webhook event was created
</ParamField>

<ParamField path="webhookVersion" type="string">
  The version of the webhook payload format
</ParamField>

<ParamField path="type" type="string">
  The type of alert webhook. One of: `alert.run.failed`, `alert.deployment.success`, or `alert.deployment.failed`
</ParamField>

### Run Failed Alert

This webhook is sent when a run fails. The payload is available on the `object` property:

<ParamField path="object.task.id" type="string">
  Unique identifier for the task
</ParamField>

<ParamField path="object.task.filePath" type="string">
  File path where the task is defined
</ParamField>

<ParamField path="object.task.exportName" type="string">
  Name of the exported task function
</ParamField>

<ParamField path="object.task.version" type="string">
  Version of the task
</ParamField>

<ParamField path="object.task.sdkVersion" type="string">
  Version of the SDK used
</ParamField>

<ParamField path="object.task.cliVersion" type="string">
  Version of the CLI used
</ParamField>

<ParamField path="object.run.id" type="string">
  Unique identifier for the run
</ParamField>

<ParamField path="object.run.number" type="number">
  Run number
</ParamField>

<ParamField path="object.run.status" type="string">
  Current status of the run
</ParamField>

<ParamField path="object.run.createdAt" type="datetime">
  When the run was created
</ParamField>

<ParamField path="object.run.startedAt" type="datetime">
  When the run started executing
</ParamField>

<ParamField path="object.run.completedAt" type="datetime">
  When the run finished executing
</ParamField>

<ParamField path="object.run.isTest" type="boolean">
  Whether this is a test run
</ParamField>

<ParamField path="object.run.idempotencyKey" type="string">
  Idempotency key for the run
</ParamField>

<ParamField path="object.run.tags" type="string[]">
  Associated tags
</ParamField>

<ParamField path="object.run.error" type="object">
  Error information
</ParamField>

<ParamField path="object.run.isOutOfMemoryError" type="boolean">
  Whether the run was an out-of-memory error
</ParamField>

<ParamField path="object.run.machine" type="string">
  Machine preset used for the run
</ParamField>

<ParamField path="object.run.dashboardUrl" type="string">
  URL to view the run in the dashboard
</ParamField>

<ParamField path="object.environment.id" type="string">
  Environment ID
</ParamField>

<ParamField path="object.environment.type" type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField path="object.environment.slug" type="string">
  Environment slug
</ParamField>

<ParamField path="object.organization.id" type="string">
  Organization ID
</ParamField>

<ParamField path="object.organization.slug" type="string">
  Organization slug
</ParamField>

<ParamField path="object.organization.name" type="string">
  Organization name
</ParamField>

<ParamField path="object.project.id" type="string">
  Project ID
</ParamField>

<ParamField path="object.project.ref" type="string">
  Project reference
</ParamField>

<ParamField path="object.project.slug" type="string">
  Project slug
</ParamField>

<ParamField path="object.project.name" type="string">
  Project name
</ParamField>

### Deployment Success Alert

This webhook is sent when a deployment succeeds. The payload is available on the `object` property:

<ParamField path="object.deployment.id" type="string">
  Deployment ID
</ParamField>

<ParamField path="object.deployment.status" type="string">
  Deployment status
</ParamField>

<ParamField path="object.deployment.version" type="string">
  Deployment version
</ParamField>

<ParamField path="object.deployment.shortCode" type="string">
  Short code identifier
</ParamField>

<ParamField path="object.deployment.deployedAt" type="datetime">
  When the deployment completed
</ParamField>

<ParamField path="object.tasks" type="array">
  Array of deployed tasks with properties: id, filePath, exportName, and triggerSource
</ParamField>

<ParamField path="object.environment.id" type="string">
  Environment ID
</ParamField>

<ParamField path="object.environment.type" type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField path="object.environment.slug" type="string">
  Environment slug
</ParamField>

<ParamField path="object.organization.id" type="string">
  Organization ID
</ParamField>

<ParamField path="object.organization.slug" type="string">
  Organization slug
</ParamField>

<ParamField path="object.organization.name" type="string">
  Organization name
</ParamField>

<ParamField path="object.project.id" type="string">
  Project ID
</ParamField>

<ParamField path="object.project.ref" type="string">
  Project reference
</ParamField>

<ParamField path="object.project.slug" type="string">
  Project slug
</ParamField>

<ParamField path="object.project.name" type="string">
  Project name
</ParamField>

### Deployment Failed Alert

This webhook is sent when a deployment fails. The payload is available on the `object` property:

<ParamField path="object.deployment.id" type="string">
  Deployment ID
</ParamField>

<ParamField path="object.deployment.status" type="string">
  Deployment status
</ParamField>

<ParamField path="object.deployment.version" type="string">
  Deployment version
</ParamField>

<ParamField path="object.deployment.shortCode" type="string">
  Short code identifier
</ParamField>

<ParamField path="object.deployment.failedAt" type="datetime">
  When the deployment failed
</ParamField>

<ParamField path="object.error.name" type="string">
  Error name
</ParamField>

<ParamField path="object.error.message" type="string">
  Error message
</ParamField>

<ParamField path="object.error.stack" type="string">
  Error stack trace (optional)
</ParamField>

<ParamField path="object.error.stderr" type="string">
  Standard error output (optional)
</ParamField>

<ParamField path="object.environment.id" type="string">
  Environment ID
</ParamField>

<ParamField path="object.environment.type" type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField path="object.environment.slug" type="string">
  Environment slug
</ParamField>

<ParamField path="object.organization.id" type="string">
  Organization ID
</ParamField>

<ParamField path="object.organization.slug" type="string">
  Organization slug
</ParamField>

<ParamField path="object.organization.name" type="string">
  Organization name
</ParamField>

<ParamField path="object.project.id" type="string">
  Project ID
</ParamField>

<ParamField path="object.project.ref" type="string">
  Project reference
</ParamField>

<ParamField path="object.project.slug" type="string">
  Project slug
</ParamField>

<ParamField path="object.project.name" type="string">
  Project name
</ParamField>
