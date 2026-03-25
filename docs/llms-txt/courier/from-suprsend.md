# Source: https://www.courier.com/docs/tutorials/migrate/from-suprsend.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from SuprSend to Courier

> Move your notification infrastructure from SuprSend to Courier. Covers concept mapping, key differences, and a step-by-step migration plan.

This guide helps you plan and execute a migration from SuprSend to Courier. It covers how the two platforms compare, where Courier gives you more flexibility, and a concrete step-by-step plan for moving everything over.

## Mapping SuprSend Concepts to Courier

| SuprSend                                                                | Courier                                                                                         |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Workflows](https://docs.suprsend.com/docs/workflows)                   | [Automations](/platform/automations/automations-overview)                                       |
| [Templates](https://docs.suprsend.com/docs/templates)                   | [Templates](/platform/content/template-designer/template-designer-overview)                     |
| [Vendors](https://docs.suprsend.com/docs/vendors)                       | [Integrations](/external-integrations/integrations-overview)                                    |
| [Smart Channel Routing](https://docs.suprsend.com/docs/design-workflow) | [Channel Priority](/platform/sending/channel-priority) + [Failover](/platform/sending/failover) |
| [Batching](https://docs.suprsend.com/docs/batch)                        | [Digest](/platform/automations/digest)                                                          |
| [Subscribers](https://docs.suprsend.com/docs/users)                     | [Users / Profiles](/platform/users/users-overview)                                              |
| [Preferences](https://docs.suprsend.com/docs/preferences)               | [Preferences](/platform/preferences/preferences-overview)                                       |
| [Inbox](https://docs.suprsend.com/docs/inbox-quick-start)               | [Inbox](/platform/inbox/inbox-overview)                                                         |
| [Tenants](https://docs.suprsend.com/docs/tenants)                       | [Tenants](/platform/tenants/tenants-overview)                                                   |

### Workflows and Automations

SuprSend [workflows](https://docs.suprsend.com/docs/workflows) use four node types (trigger, function, branch, delivery) to orchestrate notification logic. Courier [Automations](/platform/automations/automations-overview) give you the same capabilities with a visual designer and a programmatic API.

| SuprSend Node         | Courier Equivalent                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Trigger node          | Automation trigger (API invoke, [webhook](/platform/automations/webhook-trigger), or [schedule](/platform/automations/scheduling)) |
| Delay (function node) | [Delay node](/platform/sending/delay)                                                                                              |
| Batch (function node) | [Digest node](/platform/automations/digest)                                                                                        |
| Branch node           | [Condition node](/platform/automations/control-flow)                                                                               |
| Delivery node         | Send node (references a template + routing)                                                                                        |

The important difference: automations and templates are separate resources in Courier. A send node references a template by ID, so your product team can change what a notification says without opening the workflow, and engineers can adjust timing and conditions without touching copy.

Build automations visually in the [Automations Designer](/platform/automations/designer) or define them through the [Automations API](/api-reference/automations/invoke-an-automation).

### Templates

SuprSend organizes notification content in [template groups](https://docs.suprsend.com/docs/templates), with separate templates per channel. Courier [templates](/platform/content/template-designer/template-designer-overview) take a unified approach: a single resource holds content for every channel (email, SMS, push, chat, inbox), so you design all channel variants in one place.

The visual Designer uses drag-and-drop content blocks, and there's a code-first path through [Elemental](/platform/content/elemental/elemental-overview) JSON if you prefer to define content programmatically. Both support `{{variable}}` Handlebars-style personalization, channel-specific overrides, and [localization](/platform/content/localization).

Because templates live in the Designer, your product team can update copy, layout, and branding without writing code or waiting for a deploy. Publish when ready and it's live immediately.

### Integrations

What SuprSend calls [vendors](https://docs.suprsend.com/docs/vendors), Courier calls [Integrations](/external-integrations/integrations-overview). These are the provider connections (SendGrid, Twilio, FCM, Slack, etc.) that handle actual message delivery.

Courier supports 50+ providers. You can wire up multiple providers for the same channel type, and Courier [fails over](/platform/sending/failover) between them automatically. If your primary email provider goes down, traffic shifts to the backup without any code changes or manual intervention.

### Routing

Courier's `single` [routing method](/platform/sending/channel-priority) replicates SuprSend's [smart channel routing](https://docs.suprsend.com/docs/design-workflow): channels are tried in the order you specify, and delivery stops at the first success. For situations where you want to reach users everywhere at once, the `all` method broadcasts to every listed channel simultaneously.

Routing is configured per send request or per template, and you can layer provider-level [failover](/platform/sending/failover) on top; so you get fallback at both the channel and provider layers.

### Digests and Batching

Courier's [Digest](/platform/automations/digest) node works the same way as SuprSend's [batch function](https://docs.suprsend.com/docs/batch): collect matching events over a configurable time window, then send a single summary notification. Your template gets access to the full list of digested events, so you can render rich summaries across email, push, or in-app.

### Users and Profiles

Courier [profiles](/platform/users/users-overview) store recipient data: email, phone, push tokens, and any custom properties you need. Profiles accept nested JSON natively, which is useful for structured data like subscription tiers, team roles, or feature flags.

Profiles can be created ahead of time through the API or identified inline at send time. Pass a `user_id` that doesn't exist yet and Courier creates the profile automatically.

### Preferences

SuprSend's [preference system](https://docs.suprsend.com/docs/preferences) supports global channel opt-outs, category-level controls, and per-category overrides. Courier [Preferences](/platform/preferences/preferences-overview) support the same hierarchy and enforce them automatically at send time, so you don't need conditional logic in your code.

On top of the API, Courier ships a [hosted preference page](/platform/preferences/hosted-page) you can deploy in minutes and embeddable [React components](/platform/preferences/embedding-preferences) for in-app preference centers. No custom UI work required.

### In-App Notifications

Courier [Inbox](/platform/inbox/inbox-overview) is a real-time in-app notification center with drop-in components for [React](/sdk-libraries/courier-react-web), [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), and [vanilla JS](/sdk-libraries/courier-js-web). It runs on the same delivery pipeline as email, push, and SMS, so there's no separate provider to configure.

Out of the box you get read/unread state, archiving, per-user history, [toast notifications](/platform/inbox/notify-with-toasts), and [tab-based organization](/platform/inbox/organize-with-tabs).

### Tenants

[Tenants](/platform/tenants/tenants-overview) work similarly across both platforms. You scope branding, preference defaults, and notification feeds to individual customer organizations. Pass a `tenant_id` at send time and Courier applies per-tenant branding and preferences automatically. Branding lives directly on the Tenant resource rather than as a separate object.

## Why Courier

* **Content and logic stay separate.** Templates and automations are independent. Your product team updates copy in the Designer while engineers tune workflow timing; neither blocks the other.
* **Visual template designer.** Build email, SMS, push, and chat content with drag-and-drop blocks. Preview across channels, personalize with variables, and publish without deploying code.
* **Flexible routing.** Priority-based fallback (`single`) or broadcast to all channels (`all`). Configure multiple providers per channel for automatic failover at the provider level too.
* **Built-in in-app channel.** Courier Inbox works without a third-party provider. Drop in a React, iOS, or Android component and deliver in-app notifications on the same pipeline as email and push.
* **Hosted preferences out of the box.** Ship a user-facing preference center with a single config, or embed React components directly in your app. No custom UI required.
* **50+ integrations.** Email, SMS, push, chat, webhooks, CDPs, and observability tools. Switch providers without changing your send code.
* **Full delivery observability.** [Message Logs](/platform/analytics/message-logs) track every message from API request to provider delivery with a detailed timeline, error details, and rendered content inspection.

## Migration Steps

<Steps>
  <Step title="Create your Courier workspace">
    [Sign up](https://app.courier.com/signup) and create a workspace. Courier gives you separate Test and Production [environments](/platform/workspaces/environments-api-keys) with independent API keys, so you can migrate safely without affecting live traffic.
  </Step>

  <Step title="Configure integrations">
    Go to **Integrations** in your Courier dashboard and connect the same providers you use as SuprSend vendors (SendGrid, Twilio, FCM, etc.). Each provider maps to a channel type (email, SMS, push, chat). You can configure multiple providers per channel for [failover](/platform/sending/failover).

    If you use SuprSend's inbox, enable [Courier Inbox](/platform/inbox/inbox-overview); no external provider needed.
  </Step>

  <Step title="Recreate templates">
    SuprSend template groups contain per-channel templates. In Courier, a single [template](/platform/content/template-designer/template-designer-overview) holds content for all channels:

    1. Create a new template for each notification type
    2. Add channel-specific content blocks (email body, SMS text, push title/body, etc.)
    3. Use `{{variable}}` syntax for dynamic data; both platforms use the same Handlebars-style approach
    4. Publish the template to make it available for sending
  </Step>

  <Step title="Recreate workflows as automations">
    If you use SuprSend workflows with delays, batching, or branching, recreate them in [Automations](/platform/automations/automations-overview). You can build automations visually in the [Automations Designer](/platform/automations/designer) or define them programmatically via the [Automations API](/api-reference/automations/invoke-an-automation).

    For simple notification types that don't need orchestration (no delays, no digests), you can skip automations entirely and send directly via the [Send API](/platform/sending/send-message).
  </Step>

  <Step title="Migrate user data">
    Create user profiles in Courier with the same identifiers you use in SuprSend. You can create profiles via the [Profiles API](/api-reference/user-profiles/create-a-profile) or inline at send time.

    ```json  theme={null}
    {
      "user_id": "user_123",
      "profile": {
        "email": "user@example.com",
        "phone_number": "+15551234567",
        "custom": {
          "name": "Jane Doe",
          "plan": "enterprise"
        }
      }
    }
    ```

    For bulk migration, use the [Bulk API](/api-reference/bulk/create-a-bulk-job) to upsert users in batches.
  </Step>

  <Step title="Set up preferences">
    If you use SuprSend's preference system, recreate your structure in Courier:

    1. Define [subscription topics](/platform/preferences/preferences-overview) that map to your SuprSend categories
    2. Configure default channel routing per topic
    3. Migrate user preference selections via the [Preferences API](/api-reference/user-preferences/get-users-preferences)

    Courier also provides a [hosted preference page](/platform/preferences/hosted-page) you can deploy immediately, or [React components](/platform/preferences/embedding-preferences) for embedding preferences in your app.
  </Step>

  <Step title="Update your send calls">
    Replace SuprSend's workflow trigger calls with Courier's [Send API](/platform/sending/send-message). A basic send looks like this:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/send \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "to": { "user_id": "user_123" },
            "template": "order-confirmation",
            "data": {
              "order_id": "ORD-456",
              "total": "$79.99"
            }
          }
        }'
      ```

      ```javascript Node.js theme={null}
      import { CourierClient } from "@trycourier/courier";

      const courier = new CourierClient({ authorizationToken: "YOUR_API_KEY" });

      await courier.send({
        message: {
          to: { user_id: "user_123" },
          template: "order-confirmation",
          data: {
            order_id: "ORD-456",
            total: "$79.99",
          },
        },
      });
      ```

      ```python Python theme={null}
      from courier.client import Courier

      client = Courier(authorization_token="YOUR_API_KEY")

      client.send(
        message={
          "to": {"user_id": "user_123"},
          "template": "order-confirmation",
          "data": {
            "order_id": "ORD-456",
            "total": "$79.99",
          },
        }
      )
      ```
    </CodeGroup>

    Courier handles routing, preferences, and failover automatically based on your template and workspace configuration. For multi-channel sends, set the `routing` field:

    ```json  theme={null}
    {
      "message": {
        "to": { "user_id": "user_123" },
        "template": "order-confirmation",
        "routing": {
          "method": "single",
          "channels": ["push", "email", "sms"]
        }
      }
    }
    ```

    This tries push first, then email, then SMS; the same pattern as SuprSend's smart channel routing.
  </Step>

  <Step title="Test and cut over">
    1. Send test messages in your Test environment and verify delivery in [Message Logs](https://app.courier.com/logs)
    2. Validate that preferences, routing, and template rendering match your SuprSend setup
    3. Switch your production code to use Courier's Production API key
    4. Monitor [Message Logs](/platform/analytics/message-logs) and [Analytics](/platform/analytics/analytics) for delivery confirmation
  </Step>
</Steps>

## API Mapping

| Operation            | SuprSend                                        | Courier                                                                                                                                    |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Send a notification  | `POST /trigger`                                 | [`POST /send`](/api-reference/send/send-a-message)                                                                                         |
| Create/update a user | `POST /subscriber`                              | [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                       |
| Get a user           | `GET /subscriber/:id`                           | [`GET /profiles/:id`](/api-reference/user-profiles/get-a-profile)                                                                          |
| Set user preferences | `POST /subscriber/:id/category/:cat/preference` | [`PUT /users/:id/preferences/:topic`](/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic) |
| Get message status   | `GET /event/:id`                                | [`GET /messages/:id`](/api-reference/sent-messages/get-message)                                                                            |
| Bulk operations      | Batch API                                       | [`POST /bulk`](/api-reference/bulk/create-a-bulk-job)                                                                                      |
| Create/update tenant | Tenant API                                      | [`PUT /tenants/:id`](/api-reference/tenants/create-or-replace-a-tenant)                                                                    |

## What's Next

<CardGroup cols={2}>
  <Card title="Quickstart" icon="bolt" href="/getting-started/quickstart">
    Send your first notification in under 2 minutes
  </Card>

  <Card title="Template Designer" icon="palette" href="/platform/content/template-designer/template-designer-overview">
    Build notification content with the visual editor
  </Card>

  <Card title="Automations" icon="arrow-progress" href="/platform/automations/automations-overview">
    Add delays, conditions, digests, and branching to your notification workflows
  </Card>

  <Card title="Preferences" icon="sliders" href="/platform/preferences/preferences-overview">
    Let users control which notifications they receive
  </Card>
</CardGroup>
