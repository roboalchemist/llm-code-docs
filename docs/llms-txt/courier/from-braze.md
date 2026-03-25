# Source: https://www.courier.com/docs/tutorials/migrate/from-braze.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from Braze to Courier

> Move your transactional notification infrastructure from Braze to Courier. Covers concept mapping, key differences, and a step-by-step migration plan.

This guide helps you plan and execute a migration of your transactional notification flows from Braze to Courier. It covers how the two platforms compare, where Courier gives you more flexibility for developer-facing use cases, and a concrete step-by-step plan for moving things over.

<Note>
  Braze is a full marketing automation platform covering campaigns, analytics, and customer engagement. This guide focuses specifically on migrating transactional and product notification workflows; marketing campaign orchestration is outside Courier's scope.
</Note>

## Mapping Braze Concepts to Courier

| Braze                                                                                                                     | Courier                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [Campaigns](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/)                                            | [Templates](/platform/content/template-designer/template-designer-overview) + [Send API](/platform/sending/send-message)             |
| [Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/)                                                  | [Automations](/platform/automations/automations-overview)                                                                            |
| [Segments](https://www.braze.com/docs/user_guide/engagement_tools/segments/)                                              | [Audiences](/platform/users/audiences)                                                                                               |
| [User Profiles](https://www.braze.com/docs/user_guide/data/unification/user_data/)                                        | [Users / Profiles](/platform/users/users-overview)                                                                                   |
| [Subscription Groups](https://www.braze.com/docs/user_guide/message_building_by_channel/sms_mms_rcs/subscription_groups/) | [Preferences](/platform/preferences/preferences-overview)                                                                            |
| [Content Cards](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards/)                         | [Inbox](/platform/inbox/inbox-overview)                                                                                              |
| [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/)         | `data` on send + [Fetch Data node](/platform/automations/fetch-data)                                                                 |
| [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/)                                       | [Outbound Webhooks](/platform/workspaces/outbound-webhooks)                                                                          |
| [Liquid templating](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/)                    | [Handlebars](/platform/content/template-designer/handlebars-designer) + [Variables](/platform/content/variables/inserting-variables) |

### Campaigns and Templates

Braze [campaigns](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/) bundle content, audience targeting, scheduling, and delivery into a single resource. Courier separates these concerns: [templates](/platform/content/template-designer/template-designer-overview) own the content, and the [Send API](/platform/sending/send-message) or [Automations](/platform/automations/automations-overview) handle delivery.

This separation means your product team can update notification copy in the visual Designer without touching delivery logic, and engineers can adjust routing or timing without risk of breaking template content.

Templates hold content for every channel (email, SMS, push, chat, inbox) in a single resource. You design them with drag-and-drop blocks or define them programmatically with [Elemental](/platform/content/elemental/elemental-overview) JSON.

### Canvas and Automations

Braze [Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/) is a visual workflow builder for multi-step, multi-channel journeys. Courier [Automations](/platform/automations/automations-overview) fill the same role for transactional flows: delays, conditions, branching, [digests](/platform/automations/digest), and [cancellation](/tutorials/automations/how-to-cancel-an-automation).

| Canvas Step    | Courier Equivalent                                           |
| -------------- | ------------------------------------------------------------ |
| Message step   | Send node (references a template)                            |
| Delay step     | [Delay node](/platform/sending/delay)                        |
| Decision split | [Condition node](/platform/automations/control-flow)         |
| Action paths   | Branching with conditions                                    |
| Audience paths | [Audience](/platform/users/audiences) filtering + conditions |

Build automations visually in the [Automations Designer](/platform/automations/designer) or define them through the [Automations API](/api-reference/automations/invoke-an-automation).

### Segments and Audiences

Braze [segments](https://www.braze.com/docs/user_guide/engagement_tools/segments/) use filters on user attributes, behaviors, and events. Courier [Audiences](/platform/users/audiences) provide similar dynamic grouping based on user profile attributes. Define filter rules once and Courier keeps the audience membership current as profiles change.

For simpler use cases, you can also target users with [Lists](/api-reference/lists/get-all-lists) (static subscriber groups) or send to individual users directly.

### Users and Profiles

Courier [profiles](/platform/users/users-overview) store everything about a recipient: email, phone, push tokens, and any custom properties you need for personalization. Profiles accept nested JSON natively, so structured data like account tiers, team roles, or feature flags fits naturally.

You can create profiles ahead of time through the API, or identify users inline at send time. If you pass a `user_id` that doesn't exist yet, Courier creates the profile on the fly.

### Subscription Groups and Preferences

Braze [subscription groups](https://www.braze.com/docs/user_guide/message_building_by_channel/sms_mms_rcs/subscription_groups/) manage opt-in/opt-out status per channel. Courier [Preferences](/platform/preferences/preferences-overview) go further: users can opt out by channel, category, or specific notification topic, and Courier enforces these automatically at send time.

On top of the API, Courier ships a [hosted preference page](/platform/preferences/hosted-page) you can deploy in minutes and embeddable [React components](/platform/preferences/embedding-preferences) for building a preference center directly into your app.

### Content Cards and Inbox

Braze [Content Cards](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards/) deliver persistent in-app content. Courier [Inbox](/platform/inbox/inbox-overview) serves a similar purpose as a real-time in-app notification center, with drop-in components for [React](/sdk-libraries/courier-react-web), [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), and [vanilla JS](/sdk-libraries/courier-js-web).

Inbox runs on the same delivery pipeline as email, push, and SMS; there's no separate provider to configure. Out of the box you get read/unread state, archiving, per-user history, [toast notifications](/platform/inbox/notify-with-toasts), and [tab-based organization](/platform/inbox/organize-with-tabs).

### Connected Content and Dynamic Data

Braze's [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/) pulls external data into templates at render time. In Courier, you pass all the data a template needs through the `data` field on the send request. For automation flows that need to fetch data mid-sequence, the [Fetch Data node](/platform/automations/fetch-data) calls external APIs and passes the response into subsequent steps.

### Templating Language

Braze uses [Liquid](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/) for message personalization. Courier uses [Handlebars](/platform/content/template-designer/handlebars-designer) with `{{variable}}` syntax. Both support conditionals, loops, and filters. Courier also provides built-in [helpers](/platform/content/template-designer/handlebars-helpers) for common operations like date formatting, string manipulation, and conditional rendering.

## Why Courier

* **API-first for developers.** Courier is built for transactional and product notifications. A single API call sends to any channel; no campaign setup required.
* **Content and logic stay separate.** Templates and automations are independent resources. Your product team updates copy in the Designer while engineers tune workflow timing; neither blocks the other.
* **Visual template designer.** Build email, SMS, push, and chat content with drag-and-drop blocks. Preview across channels, personalize with variables, and publish without deploying code.
* **Built-in in-app channel.** Courier Inbox works without a third-party provider. Drop in a React, iOS, or Android component and deliver in-app notifications on the same pipeline as email and push.
* **Automatic failover.** Configure multiple providers per channel and Courier fails over automatically. If your primary email provider goes down, traffic shifts to the backup without code changes.
* **50+ integrations.** Email, SMS, push, chat, webhooks, CDPs, and observability tools. Switch providers without changing your send code.
* **Full delivery observability.** [Message Logs](/platform/analytics/message-logs) track every message from API request to provider delivery with a detailed timeline, error details, and rendered content inspection.

## Migration Steps

<Steps>
  <Step title="Create your Courier workspace">
    [Sign up](https://app.courier.com/signup) and create a workspace. Courier gives you separate Test and Production [environments](/platform/workspaces/environments-api-keys) with independent API keys, so you can migrate safely without affecting live traffic.
  </Step>

  <Step title="Configure integrations">
    Go to **Integrations** in your Courier dashboard and connect the same providers you use in Braze (SendGrid, Twilio, FCM, etc.). Each provider maps to a channel type (email, SMS, push, chat). You can configure multiple providers per channel for [failover](/platform/sending/failover).

    If you use Braze Content Cards for in-app messaging, enable [Courier Inbox](/platform/inbox/inbox-overview); no external provider needed.
  </Step>

  <Step title="Recreate templates">
    Braze campaigns bundle content and delivery config together. In Courier, start by extracting the content portion into [templates](/platform/content/template-designer/template-designer-overview):

    1. Create a new template for each transactional notification type
    2. Add content blocks for each channel (email, SMS, push, etc.)
    3. Convert Liquid variables (`{{user.first_name}}`) to Handlebars syntax (`{{first_name}}`); the data comes from the send request's `data` field
    4. Publish the template to make it available for sending

    If your Braze campaigns include multi-step Canvas flows, recreate the orchestration separately in [Automations](/platform/automations/automations-overview).
  </Step>

  <Step title="Migrate user data">
    Create user profiles in Courier with the same identifiers you use in Braze. You can create profiles via the [Profiles API](/api-reference/user-profiles/create-a-profile) or inline at send time.

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
    If you use Braze subscription groups, recreate your preference structure in Courier:

    1. Define [subscription topics](/platform/preferences/preferences-overview) that map to your Braze subscription groups
    2. Configure default channel routing per topic
    3. Migrate user preference selections via the [Preferences API](/api-reference/user-preferences/get-users-preferences)

    Courier also provides a [hosted preference page](/platform/preferences/hosted-page) you can deploy immediately, or [React components](/platform/preferences/embedding-preferences) for embedding preferences in your app.
  </Step>

  <Step title="Update your send calls">
    Replace Braze's campaign trigger or Canvas trigger API calls with Courier's [Send API](/platform/sending/send-message):

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

  <Step title="Set up event streaming">
    If you use Braze Currents to stream delivery events, configure Courier [Outbound Webhooks](/platform/workspaces/outbound-webhooks) to forward message events (sent, delivered, opened, clicked) to your data warehouse or analytics pipeline.
  </Step>

  <Step title="Test and cut over">
    1. Send test messages in your Test environment and verify delivery in [Message Logs](https://app.courier.com/logs)
    2. Validate that preferences, routing, and template rendering match your Braze setup
    3. Switch your production code to use Courier's Production API key
    4. Monitor [Message Logs](/platform/analytics/message-logs) and [Analytics](/platform/analytics/analytics) for delivery confirmation
  </Step>
</Steps>

## API Mapping

| Operation            | Braze                           | Courier                                                                                                                                    |
| -------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Send a notification  | `POST /messages/send`           | [`POST /send`](/api-reference/send/send-a-message)                                                                                         |
| Trigger a workflow   | `POST /canvas/trigger/send`     | [`POST /automations/invoke`](/api-reference/automations/invoke-an-automation)                                                              |
| Create/update a user | `POST /users/track`             | [`PUT /profiles/:id`](/api-reference/user-profiles/create-a-profile)                                                                       |
| Get a user           | `POST /users/export/ids`        | [`GET /profiles/:id`](/api-reference/user-profiles/get-a-profile)                                                                          |
| Manage subscriptions | `POST /subscription/status/set` | [`PUT /users/:id/preferences/:topic`](/api-reference/user-preferences/update-or-create-user-preferences-for-a-specific-subscription-topic) |
| Get message status   | Campaign analytics endpoints    | [`GET /messages/:id`](/api-reference/sent-messages/get-message)                                                                            |
| Bulk operations      | `POST /users/track` (batch)     | [`POST /bulk`](/api-reference/bulk/create-a-bulk-job)                                                                                      |

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
