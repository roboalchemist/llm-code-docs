# Source: https://www.courier.com/docs/tutorials/migrate/from-onesignal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from OneSignal to Courier

> Move your notification infrastructure from OneSignal to Courier. Covers concept mapping, key differences, and a step-by-step migration plan.

This guide helps you plan and execute a migration from OneSignal to Courier. It covers how the two platforms compare, where Courier gives you more flexibility, and a concrete step-by-step plan for moving everything over.

## Mapping OneSignal Concepts to Courier

| OneSignal                                                                  | Courier                                                                                       |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Apps](https://documentation.onesignal.com/docs/en/apps-organizations)     | [Workspaces](/platform/workspaces/workspaces-overview)                                        |
| [Segments](https://documentation.onesignal.com/docs/en/segmentation)       | [Audiences](/platform/users/audiences)                                                        |
| [Templates](https://documentation.onesignal.com/docs/en/templates)         | [Templates](/platform/content/template-designer/template-designer-overview)                   |
| [Journeys](https://documentation.onesignal.com/docs/journeys-overview)     | [Automations](/platform/automations/automations-overview)                                     |
| [Subscriptions](https://documentation.onesignal.com/docs/en/subscriptions) | Channel tokens on [User Profiles](/platform/users/users-overview)                             |
| [Users / Aliases](https://documentation.onesignal.com/docs/en/aliases)     | [Users / Profiles](/platform/users/users-overview)                                            |
| [Tags](https://documentation.onesignal.com/docs/en/add-user-data-tags)     | Custom properties on profiles + [Preferences](/platform/preferences/preferences-overview)     |
| [Outcomes](https://documentation.onesignal.com/docs/custom-outcomes)       | [Analytics](/platform/analytics/analytics) + [Message Logs](/platform/analytics/message-logs) |
| In-App Messages                                                            | [Inbox](/platform/inbox/inbox-overview)                                                       |

### Apps and Workspaces

OneSignal [apps](https://documentation.onesignal.com/docs/en/apps-organizations) map to Courier [workspaces](/platform/workspaces/workspaces-overview). Each workspace has its own integrations, templates, and user profiles. Courier gives you separate Test and Production [environments](/platform/workspaces/environments-api-keys) within a workspace, so you can develop safely without affecting live traffic.

### Segments and Audiences

OneSignal [segments](https://documentation.onesignal.com/docs/en/segmentation) use filters on user attributes, activity, and tags to create dynamic groups. Courier [Audiences](/platform/users/audiences) work similarly: define filter rules on profile attributes and Courier keeps membership current as profiles change.

For static subscriber groups (mailing lists, beta testers, etc.), Courier also supports [Lists](/api-reference/lists/get-all-lists).

### Templates

OneSignal [templates](https://documentation.onesignal.com/docs/en/templates) are reusable message blueprints for push, email, and SMS. Courier [templates](/platform/content/template-designer/template-designer-overview) take a unified approach: a single resource holds content for every channel (email, SMS, push, chat, inbox), so you design all channel variants in one place.

The visual Designer uses drag-and-drop content blocks, and there's a code-first path through [Elemental](/platform/content/elemental/elemental-overview) JSON if you prefer to define content programmatically. Both support `{{variable}}` Handlebars-style personalization, channel-specific overrides, and [localization](/platform/content/localization).

OneSignal uses Liquid syntax for templating; Courier uses Handlebars. The concepts are similar (conditionals, loops, variable interpolation), just with different syntax.

### Journeys and Automations

OneSignal [Journeys](https://documentation.onesignal.com/docs/journeys-overview) are automated multi-step message flows. Courier [Automations](/platform/automations/automations-overview) serve the same purpose with delays, conditions, branching, [digests](/platform/automations/digest), and [cancellation](/tutorials/automations/how-to-cancel-an-automation).

| Journey Step       | Courier Equivalent                                   |
| ------------------ | ---------------------------------------------------- |
| Send message       | Send node (references a template)                    |
| Wait               | [Delay node](/platform/sending/delay)                |
| Yes/No branch      | [Condition node](/platform/automations/control-flow) |
| Multi-split branch | Multiple condition nodes                             |

Build automations visually in the [Automations Designer](/platform/automations/designer) or define them through the [Automations API](/api-reference/automations/invoke-an-automation).

### Users, Subscriptions, and Profiles

OneSignal separates [users](https://documentation.onesignal.com/docs/en/aliases) (identified by aliases) from [subscriptions](https://documentation.onesignal.com/docs/en/subscriptions) (individual devices, email addresses, phone numbers). Courier consolidates these into a single [profile](/platform/users/users-overview) per user that stores all contact information: email, phone, push tokens, and custom properties.

Profiles accept nested JSON natively, so structured data like account tiers, team roles, or feature flags fits naturally. You can create profiles ahead of time through the API, or identify users inline at send time.

### Tags and Preferences

OneSignal [tags](https://documentation.onesignal.com/docs/en/add-user-data-tags) are key-value pairs on users used for both targeting and preference management. In Courier, these split into two features:

* **Custom profile properties**: Store arbitrary attributes on user profiles for targeting and personalization
* **[Preferences](/platform/preferences/preferences-overview)**: A dedicated system for notification opt-in/opt-out by channel, category, or specific topic, enforced automatically at send time

Courier also ships a [hosted preference page](/platform/preferences/hosted-page) you can deploy in minutes and embeddable [React components](/platform/preferences/embedding-preferences) for building a preference center directly into your app.

### In-App Messages and Inbox

OneSignal's in-app messages are modal overlays triggered by user activity. Courier [Inbox](/platform/inbox/inbox-overview) is a persistent in-app notification center with drop-in components for [React](/sdk-libraries/courier-react-web), [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), and [vanilla JS](/sdk-libraries/courier-js-web).

Inbox runs on the same delivery pipeline as email, push, and SMS; there's no separate provider to configure. Out of the box you get read/unread state, archiving, per-user history, [toast notifications](/platform/inbox/notify-with-toasts), and [tab-based organization](/platform/inbox/organize-with-tabs).

### Outcomes and Analytics

OneSignal [Outcomes](https://documentation.onesignal.com/docs/custom-outcomes) track conversion events tied to notifications. Courier provides delivery observability through [Message Logs](/platform/analytics/message-logs) (per-message timeline from API request to provider delivery) and [Analytics](/platform/analytics/analytics) (aggregate delivery and engagement metrics). For piping events to your own analytics, configure [Outbound Webhooks](/platform/workspaces/outbound-webhooks).

## Why Courier

* **Truly multi-channel.** Courier treats email, SMS, push, chat, webhooks, and in-app as equal channels with unified orchestration. You're not bolting non-push channels onto a push-first platform.
* **Content and logic stay separate.** Templates and automations are independent resources. Your product team updates copy in the Designer while engineers tune workflow timing; neither blocks the other.
* **Visual template designer.** Build email, SMS, push, and chat content with drag-and-drop blocks. Preview across channels, personalize with variables, and publish without deploying code.
* **Automatic failover.** Configure multiple providers per channel and Courier fails over automatically. If your primary email provider goes down, traffic shifts to the backup without code changes.
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
    Go to **Integrations** in your Courier dashboard and connect delivery providers for each channel you use in OneSignal. If you send push via FCM and APNs, configure both. For email and SMS, connect your providers (SendGrid, Twilio, etc.). You can configure multiple providers per channel for [failover](/platform/sending/failover).

    For in-app notifications, enable [Courier Inbox](/platform/inbox/inbox-overview); no external provider needed.
  </Step>

  <Step title="Recreate templates">
    OneSignal templates are per-channel. In Courier, a single [template](/platform/content/template-designer/template-designer-overview) holds content for all channels:

    1. Create a new template for each notification type
    2. Add content blocks for each channel (email body, SMS text, push title/body, etc.)
    3. Convert Liquid variables to Handlebars syntax (`{{variable}}`); the data comes from the send request's `data` field
    4. Publish the template to make it available for sending
  </Step>

  <Step title="Migrate user data">
    Create user profiles in Courier that consolidate your OneSignal user and subscription data. You can create profiles via the [Profiles API](/api-reference/user-profiles/create-a-profile) or inline at send time.

    ```json  theme={null}
    {
      "user_id": "user_123",
      "profile": {
        "email": "user@example.com",
        "phone_number": "+15551234567",
        "firebaseToken": "fcm_device_token_here",
        "custom": {
          "name": "Jane Doe",
          "plan": "enterprise"
        }
      }
    }
    ```

    For bulk migration, use the [Bulk API](/api-reference/bulk/create-a-bulk-job) to upsert users in batches. Map OneSignal `external_id` to Courier `user_id` for a seamless transition.
  </Step>

  <Step title="Set up preferences">
    If you use OneSignal tags for opt-in/opt-out management, recreate that structure using Courier [Preferences](/platform/preferences/preferences-overview):

    1. Define [subscription topics](/platform/preferences/preferences-overview) for each notification category
    2. Configure default channel routing per topic
    3. Migrate user preference selections via the [Preferences API](/api-reference/user-preferences/get-users-preferences)

    Courier also provides a [hosted preference page](/platform/preferences/hosted-page) you can deploy immediately, or [React components](/platform/preferences/embedding-preferences) for embedding preferences in your app.
  </Step>

  <Step title="Update your send calls">
    Replace OneSignal's Create Notification API calls with Courier's [Send API](/platform/sending/send-message):

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

    This tries push first, then email, then SMS; the first successful delivery wins.
  </Step>

  <Step title="Recreate automations">
    If you use OneSignal Journeys, recreate them in Courier [Automations](/platform/automations/automations-overview). Build visually in the [Automations Designer](/platform/automations/designer) or define them via the [Automations API](/api-reference/automations/invoke-an-automation).

    For simple notification types that don't need orchestration, you can skip automations entirely and send directly via the Send API.
  </Step>

  <Step title="Test and cut over">
    1. Send test messages in your Test environment and verify delivery in [Message Logs](https://app.courier.com/logs)
    2. Validate that preferences, routing, and template rendering match your OneSignal setup
    3. Switch your production code to use Courier's Production API key
    4. Monitor [Message Logs](/platform/analytics/message-logs) and [Analytics](/platform/analytics/analytics) for delivery confirmation
  </Step>
</Steps>

## API Mapping

| Operation            | OneSignal                                               | Courier                                                                                                                                                |
| -------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Send a notification  | `POST /notifications`                                   | [`POST /send`](/api-reference/send/send-a-message)                                                                                                     |
| Create/update a user | `POST /apps/:id/users`                                  | [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                                   |
| Get a user           | `GET /apps/:id/users/by/external_id/:id`                | [`GET /profiles/:id`](/api-reference/user-profiles/get-a-profile)                                                                                      |
| Add a subscription   | `POST /apps/:id/users/by/external_id/:id/subscriptions` | Push tokens on [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                    |
| Manage segments      | `POST /apps/:id/segments`                               | [`PUT /audiences/:id`](/api-reference/audiences/get-an-audience)                                                                                       |
| Get message status   | `GET /notifications/:id`                                | [`GET /messages/:id`](/api-reference/sent-messages/get-message)                                                                                        |
| Bulk operations      | `POST /notifications` (with `include_aliases`)          | [`POST /bulk`](/api-reference/bulk/create-a-bulk-job)                                                                                                  |
| Create a template    | `POST /templates`                                       | [Template Designer](/platform/content/template-designer/template-designer-overview) or [Elemental API](/platform/content/elemental/elemental-overview) |

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
