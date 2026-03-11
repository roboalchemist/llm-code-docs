# Source: https://www.courier.com/docs/tutorials/migrate/from-novu.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from Novu to Courier

> Move your notification infrastructure from Novu to Courier. Covers concept mapping, key differences, and a step-by-step migration plan.

This guide helps you plan and execute a migration from Novu to Courier. It covers how the two platforms compare, where Courier gives you more flexibility, and a concrete step-by-step plan for moving everything over.

## Mapping Novu Concepts to Courier

| Novu                                                              | Courier                                                                                                                                 |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Workflows](https://docs.novu.co/concepts/workflows)              | [Templates](/platform/content/template-designer/template-designer-overview) + [Automations](/platform/automations/automations-overview) |
| [Subscribers](https://docs.novu.co/platform/concepts/subscribers) | [Users / Profiles](/platform/users/users-overview)                                                                                      |
| [Topics](https://docs.novu.co/platform/concepts/topics)           | [Subscription Topics](/platform/preferences/preferences-overview)                                                                       |
| [Integrations](https://docs.novu.co/integrations/overview)        | [Integrations](/external-integrations/integrations-overview)                                                                            |
| [Digest](https://docs.novu.co/workflow/digest)                    | [Digest](/platform/automations/digest)                                                                                                  |
| [Delay](https://docs.novu.co/workflow/delay)                      | [Delay](/platform/sending/delay)                                                                                                        |
| [Preferences](https://docs.novu.co/platform/concepts/preferences) | [Preferences](/platform/preferences/preferences-overview)                                                                               |
| [Inbox](https://docs.novu.co/inbox/overview)                      | [Inbox](/platform/inbox/inbox-overview)                                                                                                 |
| [Tenants](https://docs.novu.co/platform/concepts/tenants)         | [Tenants](/platform/tenants/tenants-overview)                                                                                           |

### Workflows, Templates, and Automations

Novu [workflows](https://docs.novu.co/concepts/workflows) combine notification content, channel routing, and orchestration logic (digest, delay, conditions) into a single resource. Courier splits these into two independent pieces, and this is the most meaningful architectural difference between the platforms.

[Templates](/platform/content/template-designer/template-designer-overview) own the content layer. You design them visually in the Designer (drag-and-drop blocks for email, SMS, push, and chat) or define them in code with [Elemental](/platform/content/elemental/elemental-overview) JSON. Either way, your product team can ship copy changes without an engineering cycle.

[Automations](/platform/automations/automations-overview) own the orchestration layer: delays, conditions, branching, [digests](/platform/automations/digest), and [cancellation](/tutorials/automations/how-to-cancel-an-automation). An automation's send node references a template by ID, so the two evolve independently. A PM updates a welcome email while an engineer tunes the onboarding sequence, and they never step on each other.

| Novu Step Type                        | Courier Equivalent                                                     |
| ------------------------------------- | ---------------------------------------------------------------------- |
| Channel step (email, SMS, push, chat) | Send node (references a template)                                      |
| Digest step                           | [Digest node](/platform/automations/digest)                            |
| Delay step                            | [Delay node](/platform/sending/delay)                                  |
| Custom step                           | [Fetch Data node](/platform/automations/fetch-data) or condition logic |

Build automations visually in the [Automations Designer](/platform/automations/designer) or define them through the [Automations API](/api-reference/automations/invoke-an-automation).

### Subscribers and Users

Novu [subscribers](https://docs.novu.co/platform/concepts/subscribers) are the equivalent of Courier [profiles](/platform/users/users-overview). Both store recipient data: email, phone, push tokens, locale, and custom properties.

Courier profiles accept nested JSON natively, so structured data like account tiers, team roles, or feature flags fits naturally. You can create profiles ahead of time through the API, or identify users inline at send time. Pass a `user_id` that doesn't exist yet and Courier creates the profile on the fly.

### Topics and Subscription Topics

Novu [topics](https://docs.novu.co/platform/concepts/topics) group subscribers for bulk notification delivery. In Courier, the closest equivalent depends on your use case:

* **For notification categories** (letting users opt in/out of types of notifications): use [Subscription Topics](/platform/preferences/preferences-overview) within Preferences
* **For bulk delivery to groups**: use [Lists](/api-reference/lists/get-all-lists) or [Audiences](/platform/users/audiences)

### Integrations

Novu and Courier both call provider connections "integrations." Courier supports 50+ providers across email, SMS, push, chat, and webhooks. You can wire up multiple providers for the same channel type, and Courier [fails over](/platform/sending/failover) between them automatically. If your primary email provider goes down, traffic shifts to the backup without any code changes.

### Digest and Delay

Courier's [Digest](/platform/automations/digest) node works the same way as Novu's [digest step](https://docs.novu.co/workflow/digest): collect matching events over a configurable time window, then send a single summary notification. Your template gets access to the full list of digested events for rendering rich summaries.

[Delay](/platform/sending/delay) works similarly; specify a duration or a specific timestamp and the automation pauses before continuing to the next step.

### Preferences

Novu's [preference system](https://docs.novu.co/platform/concepts/preferences) supports global and per-workflow channel controls. Courier [Preferences](/platform/preferences/preferences-overview) support the same hierarchy (global, per-topic, per-channel) and enforce them automatically at send time.

On top of the API, Courier ships a [hosted preference page](/platform/preferences/hosted-page) you can deploy in minutes and embeddable [React components](/platform/preferences/embedding-preferences) for in-app preference centers. No custom UI work required.

### In-App Notifications

Novu's [Inbox](https://docs.novu.co/inbox/overview) component provides in-app notifications. Courier [Inbox](/platform/inbox/inbox-overview) serves the same purpose with drop-in components for [React](/sdk-libraries/courier-react-web), [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), and [vanilla JS](/sdk-libraries/courier-js-web).

Courier Inbox runs on the same delivery pipeline as email, push, and SMS; there's no separate service to manage. Out of the box you get read/unread state, archiving, per-user history, [toast notifications](/platform/inbox/notify-with-toasts), and [tab-based organization](/platform/inbox/organize-with-tabs).

### Tenants

[Tenants](/platform/tenants/tenants-overview) in Courier work much like [tenants](https://docs.novu.co/platform/concepts/tenants) in Novu. You scope branding, preference defaults, and notification feeds to individual customer organizations. Pass a `tenant_id` at send time and Courier applies per-tenant branding and preferences automatically.

## Why Courier

* **Fully managed infrastructure.** No self-hosting to maintain, no bridge endpoints to deploy. Courier handles orchestration, delivery, retries, and scaling.
* **Content and logic stay separate.** Templates and automations are independent resources. Your product team updates copy in the Designer while engineers tune workflow timing; neither blocks the other.
* **Visual template designer.** Build email, SMS, push, and chat content with drag-and-drop blocks. Preview across channels, personalize with variables, and publish without deploying code.
* **Built-in in-app channel.** Courier Inbox works without a third-party provider. Drop in a React, iOS, or Android component and deliver in-app notifications on the same pipeline as email and push.
* **Automatic failover.** Configure multiple providers per channel and Courier fails over automatically. If SendGrid goes down, your email still goes out through your backup provider.
* **Hosted preferences out of the box.** Ship a user-facing preference center with a single config, or embed React components directly in your app. No custom UI required.
* **50+ integrations.** Email, SMS, push, chat, webhooks, CDPs, and observability tools. Switch providers without changing your send code.
* **Full delivery observability.** [Message Logs](/platform/analytics/message-logs) track every message from API request to provider delivery with a detailed timeline, error details, and rendered content inspection.

## Migration Steps

<Steps>
  <Step title="Create your Courier workspace">
    [Sign up](https://app.courier.com/signup) and create a workspace. Courier gives you separate Test and Production [environments](/platform/workspaces/environments-api-keys) with independent API keys, so you can migrate safely without affecting live traffic.
  </Step>

  <Step title="Configure integrations">
    Go to **Integrations** in your Courier dashboard and connect the same providers you use in Novu (SendGrid, Twilio, FCM, etc.). Each provider maps to a channel type (email, SMS, push, chat). You can configure multiple providers per channel for [failover](/platform/sending/failover).

    If you use Novu's inbox component, enable [Courier Inbox](/platform/inbox/inbox-overview); no external provider needed.
  </Step>

  <Step title="Recreate templates">
    Novu workflows contain inline content per channel step. In Courier, extract the content into [templates](/platform/content/template-designer/template-designer-overview):

    1. Create a new template for each notification type
    2. Add content blocks for each channel (email body, SMS text, push title/body, etc.)
    3. Use `{{variable}}` syntax for dynamic data; both platforms use the same Handlebars-style approach
    4. Publish the template to make it available for sending
  </Step>

  <Step title="Recreate workflows as automations">
    If your Novu workflows include digest, delay, or conditional logic, recreate them in [Automations](/platform/automations/automations-overview). You can build automations visually in the [Automations Designer](/platform/automations/designer) or define them programmatically via the [Automations API](/api-reference/automations/invoke-an-automation).

    For simple notification types that don't need orchestration (no delays, no digests), you can skip automations entirely and send directly via the [Send API](/platform/sending/send-message).
  </Step>

  <Step title="Migrate subscriber data">
    Create user profiles in Courier with the same identifiers you use in Novu. You can create profiles via the [Profiles API](/api-reference/user-profiles/create-a-profile) or inline at send time.

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
    If you use Novu's subscriber preferences, recreate your structure in Courier:

    1. Define [subscription topics](/platform/preferences/preferences-overview) that map to your Novu workflow categories
    2. Configure default channel routing per topic
    3. Migrate subscriber preference selections via the [Preferences API](/api-reference/user-preferences/get-users-preferences)

    Courier also provides a [hosted preference page](/platform/preferences/hosted-page) you can deploy immediately, or [React components](/platform/preferences/embedding-preferences) for embedding preferences in your app.
  </Step>

  <Step title="Update your trigger calls">
    Replace Novu's workflow trigger calls with Courier's [Send API](/platform/sending/send-message):

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

    Courier handles routing, preferences, and failover automatically based on your template and workspace configuration.
  </Step>

  <Step title="Test and cut over">
    1. Send test messages in your Test environment and verify delivery in [Message Logs](https://app.courier.com/logs)
    2. Validate that preferences, routing, and template rendering match your Novu setup
    3. Switch your production code to use Courier's Production API key
    4. Monitor [Message Logs](/platform/analytics/message-logs) and [Analytics](/platform/analytics/analytics) for delivery confirmation
  </Step>
</Steps>

## API Mapping

| Operation                  | Novu                                    | Courier                                                                                                                                    |
| -------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Send a notification        | `POST /v1/events/trigger`               | [`POST /send`](/api-reference/send/send-a-message)                                                                                         |
| Create/update a subscriber | `PUT /v1/subscribers/:id`               | [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                       |
| Get a subscriber           | `GET /v1/subscribers/:id`               | [`GET /profiles/:id`](/api-reference/user-profiles/get-a-profile)                                                                          |
| Set preferences            | `PATCH /v2/subscribers/:id/preferences` | [`PUT /users/:id/preferences/:topic`](/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic) |
| Get message status         | `GET /v1/messages/:id`                  | [`GET /messages/:id`](/api-reference/sent-messages/get-message)                                                                            |
| List messages              | `GET /v1/messages`                      | [`GET /messages`](/api-reference/sent-messages/list-messages)                                                                              |
| Manage topics              | `POST /v1/topics`                       | [`PUT /lists/:id`](/api-reference/lists/update-a-list)                                                                                     |
| Bulk operations            | Bulk trigger                            | [`POST /bulk`](/api-reference/bulk/create-a-bulk-job)                                                                                      |

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
