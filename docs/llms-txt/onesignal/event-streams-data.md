# Source: https://documentation.onesignal.com/docs/en/event-streams-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Stream data reference

> Schema reference for all event, message, user, and subscription properties available in Event Streams and Webhooks, with Liquid syntax for each field.

Access event stream data [using Liquid syntax](./using-liquid-syntax). Wrap any field in `{{ }}` to include it in your Event Stream body. See [Examples](./event-streams#example-body).

<Warning>
  Message data for Journeys and API sends is retained for 30 days. Interaction events (clicks, opens, unsubscribes) that occur after 30 days may have blank message properties. To recover the data, correlate the `message.id` from the interaction event with the original `sent` event, which contains the full message data.
</Warning>

## `event` properties

Every event includes the core fields below. Channel-specific fields under `event.data.*` are included only when applicable — see [Channel-specific fields](#channel-specific-fields).

<ParamField body="event.kind" type="string">
  The event type, combining channel and action (e.g. `message.push.clicked`, `message.email.bounced`). See the full list of values in the [event kind reference](#event-kind-reference) below. **Liquid:** `{{ event.kind }}`
</ParamField>

<ParamField body="event.id" type="UUID">
  A unique, OneSignal-generated identifier for each individual event in UUID v4 format. Use this ID for idempotent delivery tracking. For the message or template identifier, use [`message.id`](#message-id) or [`message.template_id`](#template-id). **Liquid:** `{{ event.id }}`
</ParamField>

<ParamField body="event.timestamp" type="integer">
  UNIX timestamp of the event. **Liquid:** `{{ event.timestamp }}`
</ParamField>

<ParamField body="event.datetime" type="string">
  Human-readable time of the event in UTC as an ISO 8601 string (e.g., "2024-02-21T23:45:15.228Z"). **Liquid:** `{{ event.datetime }}`
</ParamField>

<ParamField body="event.app_id" type="UUID">
  The OneSignal [App ID](./keys-and-ids). **Liquid:** `{{ event.app_id }}`
</ParamField>

<ParamField body="event.subscription_device_type" type="string">
  The subscription type (e.g. `iOS`, `Android`, `Chrome`, `Email`, `SMS`). **Liquid:** `{{ event.subscription_device_type }}`
</ParamField>

<ParamField body="event.subscription_id" type="UUID">
  The OneSignal [Subscription ID](./subscriptions). **Liquid:** `{{ event.subscription_id }}`
</ParamField>

<ParamField body="event.onesignal_id" type="UUID">
  The OneSignal [User ID](./users). **Liquid:** `{{ event.onesignal_id }}`
</ParamField>

<ParamField body="event.external_id" type="string">
  Your user ID set as the OneSignal [External ID](./users) alias. Can be empty if not set. **Liquid:** `{{ event.external_id }}`
</ParamField>

### Channel-specific fields

These `event.data.*` fields are only present for certain event kinds.

#### In-app message events

Included with `message.iam.*` events. See [In-app message Event Streams](./iam-event-streams) for details.

<ParamField body="event.data.page_name" type="string">
  The name of the in-app message page or card displayed. **Liquid:** `{{ event.data.page_name }}`
</ParamField>

<ParamField body="event.data.page_id" type="string">
  Unique identifier for the in-app message page or card displayed. **Liquid:** `{{ event.data.page_id }}`
</ParamField>

<ParamField body="event.data.target_name" type="string">
  The name of the button or image block element clicked. The element must contain an [in-app click action](./iam-click-actions). **Liquid:** `{{ event.data.target_name }}`
</ParamField>

<ParamField body="event.data.target_id" type="string">
  Unique identifier for the button or image block element clicked. **Liquid:** `{{ event.data.target_id }}`
</ParamField>

#### Live Activity events

Included with `message.live_activity.*` events.

<ParamField body="event.data.live_activity_id" type="string">
  Unique identifier for a specific Live Activity (e.g., "Knicks vs Cavs - Oct 22 7PM"). **Liquid:** `{{ event.data.live_activity_id }}`
</ParamField>

<ParamField body="event.data.live_activity_type" type="string">
  Grouping label for Live Activity categories (e.g., "Knicks\_games"). **Liquid:** `{{ event.data.live_activity_type }}`
</ParamField>

#### Failed events

Included with `message.push.failed` and `message.email.failed` events.

<ParamField body="event.data.failure_reason" type="string">
  The reason the message failed to send. See [Push Message Reports](./push-notification-message-reports#failure-message-troubleshooting) or [Email Message Reports](./email-message-reports#why-are-my-emails-marked-as-failed) for common reasons. **Liquid:** `{{ event.data.failure_reason }}`
</ParamField>

### Event kind reference

For detailed definitions of each metric, see the [Metrics Glossary](./analytics-metrics-glossary).

| Message Event Kind (OneSignal) | Event name (in data set)             | Event Description                                                                                                                                                                   |
| ------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Push Sent                      | `message.push.sent`                  | Push notification successfully sent to the push services (FCM, APNS, etc).                                                                                                          |
| Push Received                  | `message.push.received`              | Push notification received by recipient. Not available on all platforms. See [Confirmed Delivery](./confirmed-delivery) for more details.                                           |
| Push Clicked                   | `message.push.clicked`               | User tapped the push notification to open the app on device.                                                                                                                        |
| Push Failed                    | `message.push.failed`                | Push failed to be sent. See [Push Message Reports](./push-notification-message-reports) for details.                                                                                |
| Push Unsubscribed              | `message.push.unsubscribed`          | User unsubscribed on push [subscription](./subscriptions). See [When do push subscription statuses update?](./subscriptions#when-do-push-subscription-statuses-update%3F).          |
| In-App Impression              | `message.iam.impression`             | In-App Message successfully displayed on device.                                                                                                                                    |
| In-App Clicked                 | `message.iam.clicked`                | User tapped an element on the In-App Message.                                                                                                                                       |
| In-App Page Displayed          | `message.iam.page_displayed`         | In-App Message page was displayed. Helpful for tracking carousels.                                                                                                                  |
| Email Sent                     | `message.email.sent`                 | Email successfully sent.                                                                                                                                                            |
| Email Received                 | `message.email.received`             | Email received by recipient.                                                                                                                                                        |
| Email Opened                   | `message.email.opened`               | Email was opened by recipient. See [Email Message Reports](./email-message-reports) for details.                                                                                    |
| Email Link Clicked             | `message.email.clicked`              | User tapped a link in the email.                                                                                                                                                    |
| Email Unsubscribed             | `message.email.unsubscribed`         | User unsubscribed from email via the [unsubscribe link](./unsubscribe-links-email-subscriptions).                                                                                   |
| Email Reported As Spam         | `message.email.reported_as_spam`     | User reported the email as spam. Gmail requires [Google Postmaster Tools](./google-postmaster-tools) to track. See [Email deliverability](./email-deliverability) for more details. |
| Email Bounced                  | `message.email.bounced`              | Email returned to sender due to permanent error. See [Email Message Reports](./email-message-reports) for details.                                                                  |
| Email Failed                   | `message.email.failed`               | Email could not be delivered. See [Email Message Reports](./email-message-reports) for details.                                                                                     |
| Email Suppressed               | `message.email.suppressed`           | Email could not be sent because the email address is on the [Suppression list](./email-deliverability).                                                                             |
| SMS Sent                       | `message.sms.sent`                   | SMS sent to recipient.                                                                                                                                                              |
| SMS Failed                     | `message.sms.failed`                 | SMS failed to send. See [SMS Message Reports](./sms-message-reports) for details.                                                                                                   |
| SMS Delivered                  | `message.sms.delivered`              | SMS successfully delivered.                                                                                                                                                         |
| SMS Undelivered                | `message.sms.undelivered`            | SMS could not be sent. See [SMS Message Reports](./sms-message-reports) for details.                                                                                                |
| Live Activity Sent             | `message.live_activity.sent`         | Live Activity successfully sent to FCM/APNS.                                                                                                                                        |
| Live Activity Delivered        | `message.live_activity.delivered`    | Live Activity received by recipient.                                                                                                                                                |
| Live Activity Unsubscribed     | `message.live_activity.unsubscribed` | User unsubscribed from Live Activities.                                                                                                                                             |
| Live Activity Failed           | `message.live_activity.failed`       | Live Activity failed to send.                                                                                                                                                       |
| Live Activity Clicked          | `message.live_activity.clicked`      | Live Activity clicked by user.                                                                                                                                                      |

### Example event object

Copy this Liquid template into your Event Stream body to capture all event fields:

```json JSON theme={null}
{
  "event.kind": "{{ event.kind }}",
  "event.id": "{{ event.id }}",
  "event.timestamp": "{{ event.timestamp }}",
  "event.datetime": "{{ event.datetime }}",
  "event.app_id": "{{ event.app_id }}",
  "event.subscription_device_type": "{{ event.subscription_device_type }}",
  "event.subscription_id": "{{ event.subscription_id }}",
  "event.onesignal_id": "{{ event.onesignal_id }}",
  "event.external_id": "{{ event.external_id }}",
  "event.data.page_name": "{{ event.data.page_name }}",
  "event.data.page_id": "{{ event.data.page_id }}",
  "event.data.target_name": "{{ event.data.target_name }}",
  "event.data.target_id": "{{ event.data.target_id }}",
  "event.data.failure_reason": "{{ event.data.failure_reason }}"
}
```

<Accordion title="Example rendered output">
  What a push click event looks like after Liquid rendering:

  ```json JSON theme={null}
  {
    "event.kind": "message.push.clicked",
    "event.id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "event.timestamp": 1708559115,
    "event.datetime": "2024-02-21T23:45:15.228Z",
    "event.app_id": "your-onesignal-app-id",
    "event.subscription_device_type": "iOS",
    "event.subscription_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "event.onesignal_id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
    "event.external_id": "user_12345",
    "event.data.page_name": "",
    "event.data.page_id": "",
    "event.data.target_name": "",
    "event.data.target_id": "",
    "event.data.failure_reason": ""
  }
  ```

  Channel-specific fields like `event.data.page_name` are empty for event kinds that don't include them.
</Accordion>

***

## `message` properties

The `message` object describes the message sent to the end-user, including its ID, template, content, and URLs.

<ParamField body="message.id" type="UUID">
  The message ID generated by OneSignal. **Liquid:** `{{ message.id }}`
</ParamField>

<ParamField body="message.name" type="string">
  The name of the message as set in the dashboard or using the API `name` property. **Liquid:** `{{ message.name }}`
</ParamField>

<ParamField body="message.title" type="object">
  The push message title or email subject. For push, returns a localized object like `{'en':'Your title'}`. For email, returns the subject line as a plain string. Set via the dashboard or the API `headings` / `email_subject` properties. **Liquid:** `{{ message.title }}`
</ParamField>

<ParamField body="message.contents" type="object">
  The push or SMS message content (clipped at 50 characters). Email contents (`email_body`) are not provided. Set via the dashboard or the API `contents` property. **Liquid:** `{{ message.contents }}`
</ParamField>

<ParamField body="message.template_id" type="UUID">
  The template ID for a message sent via Journeys or the API `template_id` property. **Liquid:** `{{ message.template_id }}`
</ParamField>

<ParamField body="message.url" type="string">
  The message's launch URL when using a single URL that is web and app agnostic. See [URLs, Links and Deep Links](./links). **Liquid:** `{{ message.url }}`
</ParamField>

<ParamField body="message.app_url" type="string">
  The app-specific launch URL when using separate web and app URLs. See [URLs, Links and Deep Links](./links). **Liquid:** `{{ message.app_url }}`
</ParamField>

<ParamField body="message.web_url" type="string">
  The web-specific launch URL when using separate web and app URLs. See [URLs, Links and Deep Links](./links). **Liquid:** `{{ message.web_url }}`
</ParamField>

<ParamField body="message.live_activity_event_kind" type="string">
  The Live Activity action type: `start`, `update`, or `end`. Only present for `message.live_activity.*` events. **Liquid:** `{{ message.live_activity_event_kind }}`
</ParamField>

### Example message object

Copy this Liquid template into your Event Stream body to capture all message fields:

```json JSON theme={null}
{
  "message.id": "{{ message.id }}",
  "message.name": "{{ message.name }}",
  "message.title": "{{ message.title }}",
  "message.contents": "{{ message.contents }}",
  "message.template_id": "{{ message.template_id }}",
  "message.url": "{{ message.url }}",
  "message.app_url": "{{ message.app_url }}",
  "message.web_url": "{{ message.web_url }}"
}
```

<Accordion title="Example rendered output">
  A push notification message:

  ```json JSON theme={null}
  {
    "message.id": "f3c9cd09-10d7-4f59-b9bc-66e16607f1d5",
    "message.name": "weekly-promo-push",
    "message.title": "{'en':'Flash Sale: 50% Off Today'}",
    "message.contents": "{'en':'Shop now and save on select items'}",
    "message.template_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "message.url": "https://example.com/sale",
    "message.app_url": "",
    "message.web_url": ""
  }
  ```

  An email message — `message.title` is the subject line as a plain string, and `message.contents` is empty because email body content is not included in Event Stream data:

  ```json JSON theme={null}
  {
    "message.id": "e2d3c4b5-a6f7-8901-bcde-f12345678901",
    "message.name": "onboarding-welcome-email",
    "message.title": "Welcome to Acme — here's how to get started",
    "message.contents": "",
    "message.template_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "message.url": "",
    "message.app_url": "",
    "message.web_url": ""
  }
  ```

</Accordion>

***

## `user` properties

The `user` object contains profile-level data for the user who received the message.

<ParamField body="user.onesignal_id" type="string">
  The user's OneSignal ID. **Liquid:** `{{ user.onesignal_id }}`
</ParamField>

<ParamField body="user.external_id" type="string">
  The user's External ID. **Liquid:** `{{ user.external_id }}`
</ParamField>

<ParamField body="user.tags" type="object">
  The user's [tags](./add-user-data-tags). Access the full object with `{{ user.tags }}` or a specific tag with `{{ user.tags.your_tag }}`. Use a default to handle missing tags: `{{ user.tags.your_tag | default: '' }}`.
</ParamField>

<ParamField body="user.language" type="string">
  The user's language code. **Liquid:** `{{ user.language }}`
</ParamField>

***

## `subscription` properties

These properties describe the [subscription](./subscriptions) that received the message.

<ParamField body="user.subscription.id" type="string">
  The subscription's OneSignal ID. **Liquid:** `{{ user.subscription.id }}`
</ParamField>

<ParamField body="user.subscription.app_id" type="string">
  The OneSignal App ID. **Liquid:** `{{ user.subscription.app_id }}`
</ParamField>

<ParamField body="user.subscription.subscription_token" type="string">
  The subscription's platform-specific token. For **Email**, this is the email address. For **SMS**, a phone number in E.164 format. For **Push**, the push token. **Liquid:** `{{ user.subscription.subscription_token }}`
</ParamField>

<ParamField body="user.subscription.session_count" type="number">
  Total sessions recorded for this subscription. **Liquid:** `{{ user.subscription.session_count }}`
</ParamField>

<ParamField body="user.subscription.language" type="string">
  The language code set on the subscription. **Liquid:** `{{ user.subscription.language }}`
</ParamField>

<ParamField body="user.subscription.game_version" type="string">
  The app or game version reported by the subscription. **Liquid:** `{{ user.subscription.game_version }}`
</ParamField>

<ParamField body="user.subscription.last_active" type="number">
  UNIX timestamp of the subscription's most recent session. **Liquid:** `{{ user.subscription.last_active }}`
</ParamField>

<ParamField body="user.subscription.play_time" type="number">
  Total play time recorded for this subscription, in seconds. **Liquid:** `{{ user.subscription.play_time }}`
</ParamField>

<ParamField body="user.subscription.amount_spent" type="number">
  Total in-app purchase amount recorded for this subscription. **Liquid:** `{{ user.subscription.amount_spent }}`
</ParamField>

<ParamField body="user.subscription.created_at" type="number">
  UNIX timestamp of when the subscription was created. **Liquid:** `{{ user.subscription.created_at }}`
</ParamField>

<ParamField body="user.subscription.subscribed" type="boolean">
  Whether the subscription is currently opted in. **Liquid:** `{{ user.subscription.subscribed }}`
</ParamField>

<ParamField body="user.subscription.sdk" type="string">
  The OneSignal SDK version on the subscription's device. **Liquid:** `{{ user.subscription.sdk }}`
</ParamField>

<ParamField body="user.subscription.device_model" type="string">
  The device hardware model (e.g., "iPhone14,2", "Pixel 7"). **Liquid:** `{{ user.subscription.device_model }}`
</ParamField>

<ParamField body="user.subscription.device_os" type="string">
  The device operating system and version (e.g., "iOS 17.2", "Android 14"). **Liquid:** `{{ user.subscription.device_os }}`
</ParamField>

***

## Related pages

<Columns cols={2}>
  <Card title="Event Streams" icon="bolt" href="./event-streams">
    Set up and configure Event Streams, including setup, body templates, and debugging.
  </Card>

  <Card title="Using Liquid syntax" icon="code" href="./using-liquid-syntax">
    Reference for Liquid syntax used to personalize Event Stream bodies.
  </Card>

  <Card title="In-app message Event Streams" icon="message" href="./iam-event-streams">
    Details on in-app message event data and carousel tracking.
  </Card>

  <Card title="Metrics Glossary" icon="chart-bar" href="./analytics-metrics-glossary">
    Definitions for all message event metrics across channels.
  </Card>
</Columns>

***

## FAQ

### Why is some event data missing or blank?

Message data for Journeys and API sends is retained for 30 days. If a user interacts with a message (click, open, unsubscribe) more than 30 days after it was sent, the associated message properties may be blank. To work around this, correlate the `message.id` from the interaction event with the original `sent` event, which contains the full message data.

### What is the difference between `event.id` and `message.id`?

`event.id` is a unique identifier for the individual event (e.g., one specific click). `message.id` is the identifier for the message that was sent — multiple events can share the same `message.id` (for example, a `sent` event and a `clicked` event for the same push notification).

### What format is `message.title` for push vs email?

For push notifications, `message.title` returns a localized object like `{'en':'Your title'}`. For email, it returns the subject line as a plain string. The format depends on the channel.

### Are Custom Events included in Event Streams?

No. Event Streams contain **message events** (sent, clicked, opened, bounced, etc.) — not [Custom Events](./custom-events). Custom Events are user actions you send *into* OneSignal. Event Streams export message delivery and engagement data *out of* OneSignal.

### How do I reference a specific tag in my Event Stream body?

Use `{{ user.tags.your_tag_key }}` with the exact tag key. To avoid errors when a tag is not set, add a default: `{{ user.tags.your_tag_key | default: '' }}`. See [Using Liquid syntax](./using-liquid-syntax) for more details.

***

Built with [Mintlify](https://mintlify.com).
