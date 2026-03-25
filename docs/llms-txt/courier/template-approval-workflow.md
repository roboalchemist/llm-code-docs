# Source: https://www.courier.com/docs/platform/content/template-approval-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Approval Workflow

> Require external review before publishing template changes. Courier emits webhooks on submission, locks the draft, and publishes only after checks are resolved via API.

## Overview

The template approval workflow lets you require external review before publishing template changes. When enabled, templates enter a read-only state after submission and can only be published after checks are resolved via API.

## How It Works

When a template is submitted for review, Courier emits a `notification:submitted` webhook. Your external system receives the event, runs its review process, and calls the Courier API to publish or reject the template.

<Frame caption="Approval workflow flow">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/diagram.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=69a0b82d5622e67ec8d563eceb14566c" alt="Approval workflow diagram showing submission, webhook, review, and publish steps" width="1224" height="1192" data-path="assets/platform/content/diagram.png" />
</Frame>

## Enable Checks for a Template

Enable checks on each template that requires an approval workflow:

1. Open the notification template
2. Click the Settings gear
3. Navigate to the **Checks** tab
4. Enable custom checks

<Frame caption="Enable custom checks in template settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/template-checks.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=67327ca4006e7f2711462ec39fa54b52" alt="Checks tab in template settings with custom checks toggle" width="2502" height="1308" data-path="assets/platform/content/template-checks.png" />
</Frame>

The template's publish button is replaced with a **Send for Review** option.

<Frame caption="Send for Review button replaces Publish">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/template-send-for-review.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=26475906c946d1cef2d26b3814fbe3b3" alt="Template showing Send for Review button" width="1880" height="866" data-path="assets/platform/content/template-send-for-review.png" />
</Frame>

After submission, the template enters a read-only state. No changes can be made to the latest draft until the submission is resolved or canceled.

<Frame caption="Template in read-only state after submission">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/template-read-only.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=2f5d24b00122887795867e01c2bb2c98" alt="Template in read-only state with cancel submission option" width="1880" height="866" data-path="assets/platform/content/template-read-only.png" />
</Frame>

## Webhooks

Configure a webhook in **Settings > Webhooks** to receive submission events. The webhook fires when a notification is submitted, canceled, or published. Courier sends all event types to the same webhook endpoint, so filter on the `type` field.

<Frame caption="Webhook Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/webhook-settings.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=607f36ef395a90471d2e4534e70b5403" alt="Webhook configuration in Courier settings" width="2770" height="1156" data-path="assets/platform/content/webhook-settings.png" />
</Frame>

<Frame caption="Edit Webhook Dialog">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/edit-webhook-dialog.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=05f0eea593be4ebb78f7ffded4da41cc" alt="Edit webhook dialog with URL and event configuration" width="2818" height="1342" data-path="assets/platform/content/edit-webhook-dialog.png" />
</Frame>

### Event Types

```json  theme={null}
{
  "data": {
    "id": "<NOTIFICATION_ID>",
    "submission_id": "<SUBMISSION_ID>"
  },
  "type": "notification:submitted"
}
```

For other notification event types, see the [webhook documentation](/platform/workspaces/outbound-webhooks).

Once you receive a `notification:submitted` event, trigger your external approval workflow. When the review is complete, [publish the template](#publishing-the-template).

## Fetching Content (Optional)

After receiving the `notification:submitted` event, you can retrieve the template content for use in your review process:

```
GET /notifications/:notification_id/draft/content
```

<Frame caption="Sample Template">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/sample-template.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=b987c77e57b737ff89da9e932493999b" alt="Sample notification template in the designer" width="1378" height="1508" data-path="assets/platform/content/sample-template.png" />
</Frame>

### Sample Response

```json  theme={null}
{
  "blocks": [
    {
      "alias": "Greetings",
      "context": "This is where we greet a new user",
      "id": "block_43c114d9-9cfd-4340-808f-17e2fc7a4c87",
      "type": "text",
      "checksum": "fb60f2098fa407a4ff8d48e3e908d889",
      "content": "Hello <variable id=\"3\">{name}</variable>, Welcome to <highlight id=\"6\">Courier</highlight>!"
    },
    {
      "id": "block_f19dd58f-d32c-41b8-911c-239053d34803",
      "type": "markdown",
      "content": "Ready, <variable id=\"3\">{name}</variable>? Get started [here](http://daringfireball.net/projects/markdown/).",
      "checksum": "d06665ec3f663789db81474bc1a82fc5"
    }
  ],
  "channels": [
    {
      "id": "channel_f2e7b2e9-187f-40d9-9725-636d6c59833a",
      "type": "email",
      "content": {
        "subject": "New Subject"
      },
      "checksum": "96bcf212afa5cae1c7918280743aec71"
    }
  ],
  "checksum": "22d224a20345f1e3d3cf4c231243a747"
}
```

### Checksums

Each block, channel, and notification includes an MD5 checksum. Use these to track content changes across submissions and manage translation workflows.

## Publishing the Template

Once all checks are resolved, call the API to publish the template:

```
PUT /notifications/:notification_id/:submission_id/checks
```

```json  theme={null}
{
  "checks": [
    {
      "status": "RESOLVED"
    }
  ]
}
```

To reject a submission, see [Cancel a submission](#cancel-a-submission). You can also set the check status to `FAILED` or `PENDING` for more complex state management in your approval workflow.

### Fetching Checks

```
GET /notifications/:notification_id/:submission_id/checks
```

Example: `GET /notifications/SFTYJKSF0241SVH2TWY97TTFFTQG/1630424150210/checks`

```json  theme={null}
{
  "checks": [
    {
      "id": "B5BYH93H4D4XRPJBMZJGB43TJEZ3",
      "status": "PENDING",
      "type": "custom",
      "updated": 1630424150210
    }
  ]
}
```

### Cancel a Submission

Cancel a submission by deleting it. This moves the template back to a draft state and sets all checks to `FAILED`. Once canceled, setting a check to `RESOLVED` will not publish that submission.

```
DELETE /notifications/:notification_id/:submission_id/checks
```

## Submitted Keys

Submitted keys let you send notifications using draft content that has been submitted for review but not yet published. This is useful for testing changes before they go live.

| Template State       | What Submitted Key Uses        |
| -------------------- | ------------------------------ |
| Published            | Published notification content |
| Submitted for review | Latest draft content           |

Manage submitted keys in **Settings > API Keys**.

<Frame caption="Submitted Keys in API Key settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/Yy12YQJXNoKdo-Rl/assets/platform/content/submitted-keys.png?fit=max&auto=format&n=Yy12YQJXNoKdo-Rl&q=85&s=8d6be4feb43f84534e0782710b5da02a" alt="Submitted keys section in API Keys settings" width="2856" height="1642" data-path="assets/platform/content/submitted-keys.png" />
</Frame>

<CardGroup cols={2}>
  <Card title="Outbound Webhooks" href="/platform/workspaces/outbound-webhooks" icon="webhook">
    Configure webhook endpoints for notification events
  </Card>

  <Card title="Send API" href="/api-reference/send/send-a-message" icon="paper-plane">
    Send notifications using template IDs or event aliases
  </Card>
</CardGroup>
