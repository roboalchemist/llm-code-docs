# Source: https://www.courier.com/docs/tutorials/ops/safe-notification-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Safe Notification Deployment

> Move notification templates from Test to Production safely using draft keys, the approval workflow, asset migration, and post-deploy verification.

Courier's two-environment model (Test and Production) lets you develop and validate notification changes without touching live traffic. This tutorial walks through a recommended promotion workflow; from building in Test, through staging and approval, to production migration and verification.

## Prerequisites

* A Courier workspace with at least one [integration](/external-integrations/integrations-overview) configured
* Familiarity with the [Send API](/platform/sending/send-message)

## Step 1: Build in Test

Switch to the Test environment using the toggle in the lower-left settings menu. Everything you create here; templates, brands, subscription topics; is fully isolated from Production.

<Frame caption="Switch to the Test environment">
  <img src="https://mintcdn.com/courier-4f1f25dc/4A6zrFrERiXvAT84/assets/platform/content/environments-switch-toggle.png?fit=max&auto=format&n=4A6zrFrERiXvAT84&q=85&s=75f5cfc97c0cc94689e66f740d2b1304" alt="Environment toggle in the settings menu" width="1796" height="1014" data-path="assets/platform/content/environments-switch-toggle.png" />
</Frame>

Create or edit your template, then send test notifications using your Test API key. Test sends only appear in the Test environment dashboard and never reach production recipients (unless you use real contact info).

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer YOUR_TEST_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": { "email": "test@example.com" },
        "template": "YOUR_TEMPLATE_ID",
        "data": { "name": "Test User" }
      }
    }'
  ```

  ```bash CLI theme={null}
  export COURIER_API_KEY="YOUR_TEST_API_KEY"
  courier send --email test@example.com --template YOUR_TEMPLATE_ID --name "Test User"
  ```
</CodeGroup>

<Tip>
  Configure a separate provider API key for your Test environment (e.g., a sandbox SendGrid key) so test sends never reach real inboxes. Set this under each integration's Test Configuration.
</Tip>

## Step 2: Stage with draft keys

Draft keys let you preview unpublished template changes against real send payloads before publishing. This catches rendering issues early.

<Frame caption="API Keys settings showing key types">
  <img src="https://mintcdn.com/courier-4f1f25dc/4A6zrFrERiXvAT84/assets/platform/content/environments-api-keys.png?fit=max&auto=format&n=4A6zrFrERiXvAT84&q=85&s=c9cd3f3333e3090c1654e5e12163feec" alt="API Keys settings page" width="3454" height="1922" data-path="assets/platform/content/environments-api-keys.png" />
</Frame>

You can generate draft keys from [Settings > API Keys](https://app.courier.com/settings/api-keys). When you send with a draft key, Courier renders the latest unpublished draft of the template rather than the last published version.

```bash  theme={null}
curl -X POST https://api.courier.com/send \
  -H "Authorization: Bearer YOUR_DRAFT_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "to": { "email": "reviewer@yourteam.com" },
      "template": "YOUR_TEMPLATE_ID",
      "data": { "name": "Draft Preview" }
    }
  }'
```

Check the rendered output in [Message Logs](/platform/analytics/message-logs) to confirm variables, branding, and channel content look correct before publishing.

## Step 3: Get approval (optional)

If your team requires review before publishing, enable the [Template Approval Workflow](/platform/content/template-approval-workflow). When enabled, the "Publish Changes" button is replaced with "Send for Review," and the template enters a read-only state until the submission is resolved via API.

This is useful for teams that need compliance review, copy editing, or multi-stakeholder sign-off before changes go live. Skip this step if your team doesn't need formal approval gates.

## Step 4: Promote to Production

Once your template is published in Test and validated, migrate it to Production:

<Steps>
  <Step title="Open the template">
    Navigate to the notification template you want to promote.
  </Step>

  <Step title="Open the migration modal">
    Click the dropdown on the "Publish Changes" button and select "Migrate Assets."
  </Step>

  <Step title="Review and copy">
    Courier copies the template and all dependencies (brands, tags, subscription topics) to the destination environment. Choose "Copy Assets" to copy without publishing, or "Copy And Publish" to go live immediately.
  </Step>
</Steps>

<Frame caption="Migrate Assets from Test to Production">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/workspaces/environments-migrate-assets.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=f4378611567920d81f9aca5bb01d30dd" alt="Migrate Assets button in the template editor" width="2866" height="1438" data-path="assets/platform/workspaces/environments-migrate-assets.png" />
</Frame>

If you have multiple workspaces, you can also select a destination workspace in the migration modal.

## Step 5: Verify

After promotion, confirm everything works in Production:

1. **Check Message Logs.** Open [Message Logs](/platform/analytics/message-logs) in the Production environment and verify that sends are rendering and delivering as expected.

2. **Run a smoke test.** Use the CLI or API with your Production key to send a test notification to an internal recipient:

```bash  theme={null}
export COURIER_API_KEY="YOUR_PRODUCTION_API_KEY"
courier send --email ops@yourteam.com --template YOUR_TEMPLATE_ID --name "Smoke Test"
```

3. **Inspect the timeline.** In Message Logs, expand the message and review the timeline to confirm the correct template version was used and the provider accepted the send.

<CardGroup cols={2}>
  <Card title="Environments & API Keys" href="/platform/workspaces/environments-api-keys" icon="key">
    Manage environments, keys, and asset migration
  </Card>

  <Card title="Template Approval Workflow" href="/platform/content/template-approval-workflow" icon="clipboard-check">
    Require review before publishing template changes
  </Card>

  <Card title="Message Logs" href="/platform/analytics/message-logs" icon="chart-line">
    Monitor delivery status and debug issues
  </Card>

  <Card title="Courier CLI" href="/tools/cli" icon="terminal">
    Send, test, and manage notifications from the command line
  </Card>
</CardGroup>
