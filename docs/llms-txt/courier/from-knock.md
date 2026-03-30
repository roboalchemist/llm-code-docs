# Source: https://www.courier.com/docs/tutorials/migrate/from-knock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from Knock to Courier

> Move your notification infrastructure from Knock to Courier. Covers concept mapping, key differences, and a step-by-step migration plan.

This guide helps you plan and execute a migration from Knock to Courier. It covers how the two platforms compare, where Courier gives you more flexibility, and a concrete step-by-step plan for moving everything over.

## Mapping Knock Concepts to Courier

| Knock                                                              | Courier                                                                                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [Channels](https://docs.knock.app/concepts/channels)               | [Integrations](/external-integrations/integrations-overview)                                                |
| [Workflows](https://docs.knock.app/concepts/workflows)             | [Templates](/platform/content/content-overview) + [Automations](/platform/automations/automations-overview) |
| [Recipients / Users](https://docs.knock.app/concepts/users)        | [Users / Profiles](/platform/users/users-overview)                                                          |
| [Objects](https://docs.knock.app/concepts/objects)                 | `data` on send                                                                                              |
| [Preferences](https://docs.knock.app/preferences/overview)         | [Preferences](/platform/preferences/preferences-overview)                                                   |
| [Tenants](https://docs.knock.app/concepts/tenants)                 | [Tenants](/platform/tenants/tenants-overview)                                                               |
| [Feeds](https://docs.knock.app/integrations/in-app/knock) (in-app) | [Inbox](/platform/inbox/inbox-overview)                                                                     |
| [Commits](https://docs.knock.app/concepts/commits)                 | Publish (draft/live)                                                                                        |

### Integrations

Knock [Channels](https://docs.knock.app/concepts/channels) map to Courier [Integrations](/external-integrations/integrations-overview), where you configure delivery providers like SendGrid, Twilio, and FCM. You can wire up multiple providers for the same channel type and Courier automatically [fails over](/platform/sending/failover) between them; if your primary email provider is down, the backup kicks in without any code changes on your side.

With 50+ supported providers across email, SMS, push, chat, and webhooks, you're unlikely to hit a gap. And because provider config lives in the dashboard, swapping or adding a provider never requires a deploy.

### Templates and Automations

Knock bundles notification content and delivery logic into a single [Workflow](https://docs.knock.app/concepts/workflows). Courier splits these into two independent resources, and this is the most meaningful architectural difference between the platforms.

[Templates](/platform/content/template-designer/template-designer-overview) own the content layer. You design them visually in the Designer (drag-and-drop blocks for email, SMS, push, and chat) or define them in code with [Elemental](/platform/content/elemental/elemental-overview) JSON. Either way, your product team can ship copy changes without an engineering cycle.

[Automations](/platform/automations/automations-overview) own the orchestration layer: delays, conditions, branching, [digests](/platform/automations/digest), and [cancellation](/tutorials/automations/how-to-cancel-an-automation). An automation's send node references a template by ID, so the two evolve independently. A PM updates a welcome email while an engineer tunes the onboarding sequence, and they never step on each other.

### Users and Profiles

Courier [profiles](/platform/users/users-overview) store everything about a recipient: email, phone, push tokens, and any custom properties you need for personalization. Profiles accept nested JSON, so structured data like feature flags, team roles, or subscription tiers fits naturally.

You can create profiles ahead of time through the API, or identify users inline at send time. If you pass a `user_id` that doesn't exist yet, Courier creates the profile on the fly.

### Passing Context

Where Knock uses [Objects](https://docs.knock.app/concepts/objects) as non-user entities that can receive notifications, Courier keeps things simpler: you pass arbitrary context through the `data` field on each send request. No need to create and manage separate entity types; any data your template needs for rendering just goes in `data`.

### Preferences

Knock's [PreferenceSet](https://docs.knock.app/preferences/overview) maps to Courier [Preferences](/platform/preferences/preferences-overview), which let users opt out by channel, category, or specific notification topic. Courier enforces these automatically at send time; you don't need conditional logic in your code.

On top of the API, Courier ships a [hosted preference page](/platform/preferences/hosted-page) you can deploy in minutes and embeddable [React components](/platform/preferences/embedding-preferences) for building a preference center directly into your app. No custom UI work required.

### Tenants

[Tenants](/platform/tenants/tenants-overview) in Courier work much like [Tenants](https://docs.knock.app/concepts/tenants) in Knock. You scope branding, preference defaults, and notification feeds to individual customer organizations, workspaces, or accounts. Pass a `tenant_id` at send time and Courier applies per-tenant branding and preference defaults automatically.

One difference: Courier stores branding attributes directly on the Tenant resource rather than as a separate Brands object.

### In-App Notifications

Knock's [Feeds](https://docs.knock.app/integrations/in-app/knock) map to Courier [Inbox](/platform/inbox/inbox-overview), a real-time in-app notification center with drop-in components for [React](/sdk-libraries/courier-react-web), [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), and [vanilla JS](/sdk-libraries/courier-js-web). It runs on the same pipeline as your other channels, so there's no extra provider to configure; enable it and start sending.

Out of the box you get read/unread state, archiving, per-user history, and [toast notifications](/platform/inbox/notify-with-toasts).

### Versioning

Knock uses a git-style [commit model](https://docs.knock.app/concepts/commits) to version dashboard changes. Courier uses a simpler draft/published model. You edit templates and automations in draft, preview them, and publish when ready. Published versions are immutable, so you always have a clear snapshot of what's live.

## Why Courier

* **Content and logic stay separate.** Templates and automations are independent. Your product team updates copy in the Designer while engineers tune workflow timing; neither blocks the other.
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
    Go to **Integrations** in your Courier dashboard and connect the same providers you use in Knock (SendGrid, Twilio, FCM, etc.). Each provider maps to a channel type (email, SMS, push, chat). You can configure multiple providers per channel for [failover](/platform/sending/failover).

    If you use Knock's in-app feed, enable [Courier Inbox](/platform/inbox/inbox-overview); no external provider needed.
  </Step>

  <Step title="Recreate templates">
    Knock workflows combine content and logic. In Courier, start by recreating the content portion as [templates](/platform/content/template-designer/template-designer-overview) in the Designer:

    1. Create a new template for each notification type
    2. Add content blocks for each channel (email, SMS, push, etc.)
    3. Use `{{variable}}` syntax for dynamic data; Courier supports the same Handlebars-style variables
    4. Publish the template to make it available for sending

    If your Knock workflows include orchestration logic (delays, conditions, batching), recreate that separately in [Automations](/platform/automations/automations-overview).
  </Step>

  <Step title="Migrate user data">
    Create user profiles in Courier with the same identifiers you use in Knock. You can create profiles via the [Profiles API](/api-reference/user-profiles/create-a-profile) or inline at send time.

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
    If you use Knock's PreferenceSet, recreate your preference structure in Courier:

    1. Define [subscription topics](/platform/preferences/preferences-overview) that map to your Knock categories
    2. Configure default channel routing per topic
    3. Migrate user preference selections via the [Preferences API](/api-reference/user-preferences/get-users-preferences)

    Courier also provides a [hosted preference page](/platform/preferences/hosted-page) you can deploy immediately, or [React components](/platform/preferences/embedding-preferences) for embedding preferences in your app.
  </Step>

  <Step title="Update your send calls">
    Replace Knock's workflow trigger calls with Courier's [Send API](/platform/sending/send-message). A basic send looks like this:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/send \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "to": { "user_id": "user_123" },
            "template": "welcome-email",
            "data": {
              "name": "Jane Doe",
              "action_url": "https://app.example.com"
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
          template: "welcome-email",
          data: {
            name: "Jane Doe",
            action_url: "https://app.example.com",
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
          "template": "welcome-email",
          "data": {
            "name": "Jane Doe",
            "action_url": "https://app.example.com",
          },
        }
      )
      ```
    </CodeGroup>

    Courier handles routing, preferences, and failover automatically based on your template and workspace configuration.
  </Step>

  <Step title="Test and cut over">
    1. Send test messages in your Test environment and verify delivery in [Message Logs](https://app.courier.com/logs)
    2. Validate that preferences, routing, and template rendering match your Knock setup
    3. Switch your production code to use Courier's Production API key
    4. Monitor [Message Logs](/platform/analytics/message-logs) and [Analytics](/platform/analytics/analytics) for delivery confirmation
  </Step>
</Steps>

## API Mapping

| Operation            | Knock                                                  | Courier                                                                                                                                    |
| -------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Send a notification  | `POST /workflows/:key/trigger`                         | [`POST /send`](/api-reference/send/send-a-message)                                                                                         |
| Create/update a user | `PUT /users/:id`                                       | [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                       |
| Get a user           | `GET /users/:id`                                       | [`GET /profiles/:id`](/api-reference/user-profiles/get-a-profile)                                                                          |
| Set user preferences | `PUT /users/:id/preferences`                           | [`PUT /users/:id/preferences/:topic`](/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic) |
| Get message status   | `GET /messages/:id`                                    | [`GET /messages/:id`](/api-reference/sent-messages/get-message)                                                                            |
| List messages        | `GET /messages`                                        | [`GET /messages`](/api-reference/sent-messages/list-messages)                                                                              |
| Bulk send            | `POST /workflows/:key/trigger` (with recipients array) | [`POST /bulk`](/api-reference/bulk/create-a-bulk-job)                                                                                      |
| Create/update tenant | `PUT /tenants/:id`                                     | [`PUT /tenants/:id`](/api-reference/tenants/create-or-replace-a-tenant)                                                                    |

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
