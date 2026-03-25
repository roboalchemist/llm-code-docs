# Source: https://documentation.onesignal.com/reference/create-message.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending messages with the OneSignal API

> Step-by-step guide to send push notifications, emails, SMS, and Live Activities using OneSignal’s API.

## Overview

This guide walks you through sending messages with the OneSignal API—from choosing a target audience to composing content, scheduling delivery, and validating responses. You’ll find channel-specific options, performance guidance, and common pitfalls to avoid.

### Prerequisites

1. Complete [Channel Setup](/docs/en/channel-setup) for the channels you’ll use: Push, Email, SMS, Live Activities.
2. Start accumulating [Subscriptions](/docs/en/subscriptions) for your users.
3. Have your REST API Key and App ID ready. See [Keys and IDs](/docs/en/keys-and-ids).

***

## Choose your target audience

You can target users with **one of the following methods per request**:

* **Aliases**: Specific users via unique IDs, emails, or phone numbers.
* **Segments**: Groups based on predefined behaviors or attributes.
* **Filters**: Custom rules using tags, location, activity, and more.

<Warning>
  Only one targeting method is allowed per message. For example, you cannot mix aliases and filters.
</Warning>

Additionally, you can target specific platforms (e.g. `isAndroid`, `isIos`, `isAnyWeb`) when sending push notifications.

### Aliases, emails, phone numbers

Target specific users or lists of users (up to 20,000 entries per request). This method is best for [Transactional Messages](/docs/en/transactional-messages).

<Accordion title="Aliases, emails, and phone numbers targeting parameters.">
  <ParamField path="include_aliases" type="object">
    Target up to 20,000 users by their `external_id`, `onesignal_id`, or a custom alias. Combine with `target_channel` to select the delivery channel.

    ```json  theme={null}
    {
      "include_aliases": {
        "external_id": [
          "user1",
          "user2",
          "user3"
        ]
      },
      "target_channel": "push"
    }
    ```
  </ParamField>

  <ParamField path="target_channel" type="string">
    The targeted delivery channel. Required when using `include_aliases` or `included_segments` and sending SMS/RCS. Accepts `"push"`, `"email"`, or `"sms"`.

    ```json  theme={null}
    {
      "target_channel": "push"
    }
    ```
  </ParamField>

  <ParamField path="include_subscription_ids" type="array">
    Target users' specific [Subscriptions](/docs/en/subscriptions) by ID. Max 20,000 `subscription_id` per request.

    ```json  theme={null}
    {
      "include_subscription_ids": [
        "1dd608f2-c6a1-11e3-851d-000c2940e62c"
      ]
    }
    ```
  </ParamField>

  <ParamField path="email_to" type="array">
    Send email to specific email addresses (max 20,000 per request). Can only be used when sending [Email](/reference/email). If the email address does not exist within the OneSignal App, then a new email Subscription will be created.

    ```json  theme={null}
    {
      "email_to": [
        "user1@example.com",
        "user2@example.com"
      ]
    }
    ```
  </ParamField>

  <ParamField path="include_phone_numbers" type="array">
    Send SMS/MMS/RCS to phone number in [E.164 format](/docs/en/sms-faq#what-is-the-e164-format) (max 20,000 per request). Can only be used when sending [SMS/MMS/RCS](/reference/sms). If the phone number does not exist within the OneSignal App, then a new SMS Subscription will be created.

    ```json  theme={null}
    {
      "include_phone_numbers": [
        "+19999999999"
      ]
    }
    ```
  </ParamField>
</Accordion>

***

### Segments

Target users in existing [Segments](/docs/en/segmentation). Users in multiple Segments only receive the message once.

<Accordion title="Segments targeting parameters.">
  <ParamField path="included_segments" type="array">
    Target predefined [Segments](/docs/en/segmentation). Users that are in multiple segments will only be sent the message once. Combine with `excluded_segments` to exclude users from specific Segments. Requires `target_channel` to be set to `"sms"` or `isSms=true` when sending SMS/RCS.

    ```json  theme={null}
    {
      "included_segments": [
        "Active Users",
        "Inactive Users"
      ]
    }
    ```
  </ParamField>

  <ParamField path="excluded_segments" type="array">
    Exclude users in these [Segments](/docs/en/segmentation) even if they're in `included_segments`.

    ```json  theme={null}
    {
      "included_segments": [
        "Subscribed Users"
      ],
      "excluded_segments": [
        "Inactive Users"
      ]
    }
    ```
  </ParamField>
</Accordion>

***

### `filters`

Build real-time audiences with `AND`/`OR` logic. No need to create segments first.

You can include up to **200 total entries per request**. This includes filter rows (e.g., each `field`) and logical operators like `{"operator": "OR"}`.

<Accordion title="Filters targeting parameter details.">
  **Performance guidance:**

* **Fast**: Tag filters using `"="` or `"exists"`, and filters on `last_session`, `session_count`, or `country`.
* **Slower**: Negation filters (`"!="`, `"not_exists"`)—especially with users who have many tags. Contact support to request indexing optimizations.
* **Slow by default**: Numeric comparisons (`">"`, `"<"`) on tags or custom properties. Indexing may be available on request.
* **Mixed performance**: Combining tag filters with other fields may increase computation time.

  <ParamField path="operator" type="string">
    - Implicit `AND` logic between filters. Use `"operator": "OR"` to start a new branch.
    - `OR` filters are mutually exclusive. Recipients only need to satisfy one condition.
    - Allowed values: `"AND"`, `"OR"`.

    <CodeGroup>
      ```json AND example theme={null}
      // Users must satisfy both filters to be included.
      // Notice the AND operator is not required

      "filters": [
      {"field": "tag", "key": "level", "relation": "=", "value": "10"},
      {"field": "amount_spent", "relation": ">","value": "0"}
      ]

      // The same example using the AND operator. This is not required.
      "filters": [
      {"field": "tag", "key": "level", "relation": "=", "value": "10"},
      {"operator": "AND"},
      {"field": "amount_spent", "relation": ">","value": "0"}
      ]

      ```

      ```json OR example theme={null}
      // Users can satisfy either filter to be included.

      "filters": [
        {"field": "tag", "key": "level", "relation": "=", "value": "10"},
        {"operator": "OR"},
        {"field": "tag", "key": "level", "relation": "=", "value": "20"}
      ]
      ```

      ```json Combinations theme={null}
      // In this example, users must either have:
      // The specified session_count AND tag requirement
      // Or it will be all records where last_session is satisfied
      {
        "name": "2 filters or 1",
        "filters": [
          {"field": "session_count", "relation": ">", "value": "2"},
          {"operator": "AND"},
          {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"},
          {"operator": "OR"},
          {"field": "last_session", "relation": "<", "hours_ago": "30"}
        ]
      }

      // Similar to the first example, this shows how to require a specific field
      // across other filters

      {
        "name": "3 filters, 1 required across all",
        "filters": [
          {"field": "session_count", "relation": ">", "value": "2"},
          {"operator": "AND"},
          {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"},
          {"operator": "OR"},
          {"field": "last_session", "relation": "<", "hours_ago": "30"},
          {"operator": "AND"},
          {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"}
        ]
      }

      // Example of 3 user groups with 2 requirements
      // (group_1 OR group_2 OR group_3) AND (requirement_1 OR requirement_2)

      {
        "name": "3 groups with 2 requirements",
        "filters": [
          {"field": "tag", "relation": "exists", "key": "group_1"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_1"},
          {"operator": "OR"},
          {"field": "tag", "relation": "exists", "key": "group_1"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_2"},
          {"operator": "OR"},
          {"field": "tag", "relation": "exists", "key": "group_2"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_1"},
          {"operator": "OR"},
          {"field": "tag", "relation": "exists", "key": "group_2"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_2"},
          {"operator": "OR"},
          {"field": "tag", "relation": "exists", "key": "group_3"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_1"},
          {"operator": "OR"},
          {"field": "tag", "relation": "exists", "key": "group_3"},
          {"operator": "AND"},
          {"field": "tag", "relation": "exists", "key": "requirement_2"}
        ]
      }
      ```
    </CodeGroup>
  </ParamField>

  <ParamField path="field" type="object">
    ### `tag`

    Target based on custom user [Data Tags](/docs/en/add-user-data-tags).

    <Warning>
      Do not use tags for targeting individual users like a "user id".
      Instead use [External ID](/docs/en/users) or custom [Aliases](/docs/en/aliases) and the `include_aliases` targeting property.
    </Warning>

    * `relation` = `">"`, `"<"`, `"="`, `"!="`, `"exists"`, `"not_exists"`, `"time_elapsed_gt"`, (time elapsed greater than) and `"time_elapsed_lt"` (time elapsed less than)
      * `time_elapsed_gt/lt` fields correspond to [Time Operators](/docs/en/time-operators) and require a paid plan.
    * `key` = Tag key to compare.
    * `value` = Tag value to compare. Not required for `"exists"` or `"not_exists"`.

      ```json  theme={null}
      "filters": [
        {"field": "tag", "key": "level", "relation": "=", "value": "10"}
      ]
      ```

    ### `country`

    Country of the user.

    * `relation` = `"="`, `"!="`, `"exists"`, `"not_exists"`
    * `value` = Tag value to compare. Not required for `"exists"` or `"not_exists"`.

      ```json  theme={null}
      "filters": [
        {"field": "country", "relation": "=", "value": "US"}
      ]
      ```

    ### `last_session`

    Time since user last used the app (in `hours_ago`).

    * `relation` = `">"` or `"<"`
    * `hours_ago` = number of hours before or after the user's last session. Example: `"1.1"`

      ```json  theme={null}
      "filters": [
        {"field": "last_session", "relation": ">","hours_ago": "10"}
      ]
      ```

    ### `first_session`

    Time since user first used the app or was created (in `hours_ago`).

    * `relation` = `">"` or `"<"`
    * `hours_ago` = number of hours before or after the user's first session. Example: `"1.1"`

      ```json  theme={null}
      "filters": [
        {"field": "first_session", "relation": "<","hours_ago": "24"}
      ]
      ```

    ### `session_count`

    Total number of sessions by the user.

    * `relation` = `">"`, `"<"`, `"="` or `"!="`
    * `value` = number sessions. Example: `"1"`

      ```json  theme={null}
      "filters": [
        {"field": "session_count", "relation": ">","value": "5"}
      ]
      ```

    ### `session_time`

    Total time spent in the app (in seconds).

    * `relation` = `">"` or `"<"`
    * `value` = Time in seconds the user has been in your app. Example: 1 day is `"86400"` seconds

      ```json  theme={null}
      "filters": [
        {"field": "session_time", "relation": ">","value": "86400"}
      ]
      ```

    ### `language`

    User’s language code (e.g., "en"). See [Multi-Language Messaging](/docs/en/multi-language-messaging) for details and [supported language codes](/docs/en/multi-language-messaging#supported-languages).

    * `relation` = `"="` or `"!="`
    * `value` = 2 character language code. Example: `"en"`.

      ```json  theme={null}
      "filters": [
        {"field": "language", "relation": "=","value": "en"},
        {"operator": "OR"},
        {"field": "language", "relation": "=","value": "es"}
      ]
      ```

    ### `app_version`

    Subscription's app version.

    * `relation` = `">"`, `"<"`, `"="` or `"!="`
    * `value` = app version. Example: `"1.0.0"`

      ```json  theme={null}
      "filters": [
        {"field": "app_version", "relation": "=","value": "1.0.1"}
      ]
      ```

    ### `location`

    Target by GPS coordinates and radius. See [Location-Triggered Notifications](/docs/en/location-triggered-event) for details.

    * `radius` = in meters
    * `lat` = latitude
    * `long` = longitude

      ```json  theme={null}
      "filters": [
        {"field": "location", "radius": "1000","lat": "37.77", "long":"-122.43"}
      ]
      ```
  </ParamField>
</Accordion>

***

## Craft your message

Each channel has its own set of fields. At a minimum, you need the following to send a displayable message:

* **Push & SMS** use `contents`
* **Email** uses `email_subject` and `email_body`
* Or reuse `template_id` if you created [Templates](/docs/en/templates).

<CodeGroup>
  ```json Push & SMS theme={null}
  // Message request body
  {
    "contents": {
      "en": "Hello, world",
      "es": "Hola Mundo",
      "fr": "Bonjour le monde",
      "zh-Hans": "你好世界"
    }
  }
  ```

  ```json Email theme={null}
  // Message request body
  {
    "email_subject": "Hello, world",
    "email_body": "<html><body><h1>Hello, world</h1></body></html>"
  }
  ```

</CodeGroup>

For advanced customization—like adding images, buttons, sounds, or tracking—see the channel-specific options below.

### Push notification options

Below are the most common parameters for push notifications. For the full list of options, see the [Push notification reference](/reference/push-notification).

<Accordion title="📲 Push Notification Options.">
  ### 📄 Content & text

* [`contents`](/reference/push-notification#body-contents) – Main message body.
* [`headings`](/reference/push-notification#body-headings) – Title of the notification.
* [`subtitle`](/reference/push-notification#body-subtitle) – Secondary line of text.
* [`template_id`](/reference/push-notification#body-template-id) – Use a [pre-defined template](/docs/en/templates) for common message types.

### 🖼 Appearance

* [`ios_attachments`](/reference/push-notification#body-ios-attachments) – Images/video/media.
* [`big_picture`](/reference/push-notification#body-big-picture) – Large image (Android).
* [`chrome_web_image`](/reference/push-notification#body-chrome-web-image) – Large image (Chrome).
* [`small_icon`](/reference/push-notification#body-small-icon)
* [`large_icon`](/reference/push-notification#body-large-icon)
* [`buttons`](/reference/push-notification#body-buttons) – Action buttons.

### 🔔 Delivery & priority

* [`android_channel_id`](/reference/push-notification#body-android-channel-id)
* [`priority`](/reference/push-notification#body-priority) – Delivery urgency.
* [`ios_interruption_level`](/reference/push-notification#body-ios-interruption-level)
* [`collapse_id`](/reference/push-notification#body-collapse-id) – Replaces older messages.

### 🧩 Data & Extras

* [`data`](/reference/push-notification#body-data) – Custom key-value pairs sent to your app.
* [`url`](/reference/push-notification#body-url) – Opens when notification is tapped.
</Accordion>

### Email options

<Accordion title="📧 Email Options">
  ### 📄 Content

* [`email_subject`](/reference/email#body-email-subject)
* [`email_body`](/reference/email#body-email-body)
* [`email_preheader`](/reference/email#body-email-preheader)

### 🖼 Appearance

* [`template_id`](/reference/email#body-template-id) – Use a [pre-defined template](/docs/en/templates) for common message types.

### 📬 Sender Info

* [`email_from_name`](/reference/email#body-email-from-name)
* [`email_reply_to`](/reference/email#body-email-reply-to)
</Accordion>

### SMS/MMS options

<Accordion title="💬 SMS/MMS Options">
  ### 📄 Content

* [`contents`](/reference/sms#body-contents)
* [`template_id`](/reference/sms#body-template-id) – Use a [pre-defined template](/docs/en/templates) for common message types.

### 🖼 Media (MMS only)

* [`sms_media_urls`](/reference/sms#body-sms-media-urls)

### 📬 Sender Info

* [`sms_from`](/reference/sms#body-sms-from)
</Accordion>

***

## Schedule & per-user delivery

By default, messages are sent immediately. You can schedule delivery in advance and optimize timing per-user based on their local timezone or recent activity.

<Accordion title="Schedule delivery and per-user optimization parameters.">
  <ParamField path="send_after" type="string">
    Schedule delivery for a future date/time (in UTC). The format must be valid per the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard and compatible with [`JavaScript’s Date() parser`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#datestring).

    ```json  theme={null}
    {
      "send_after": "2025-09-24T14:00:00-07:00"
    }
    ```
  </ParamField>

  <ParamField path="delayed_option" type="string">
    Controls how push and email messages are delivered on a per-user basis. Not available for SMS.

    * `'timezone'`: Sends at the same local time across time zones.
    * `'last-active'`: Delivers based on each user’s most recent session.

    Not compatible with [Push Throttling](/docs/en/throttling). If enabled, set `throttle_rate_per_minute` to `0`.

    ```json  theme={null}
    {
      "delayed_option": "last-active",
      "throttle_rate_per_minute": 0
    }
    ```
  </ParamField>

  <ParamField path="delivery_time_of_day" type="string">
    Use with `delayed_option: 'timezone'` to set a consistent daily delivery time. Accepted formats:

    * `"9:00AM"` (12-hour)
    * `"21:45"` (24-hour)
    * `"09:45:30"` (HH:mm:ss)

    Example – Send every day at 9 AM in each user's local time:

    ```json  theme={null}
    {
      "delayed_option": "timezone",
      "delivery_time_of_day": "9:00AM",
      "throttle_rate_per_minute": 0
    }
    ```
  </ParamField>
</Accordion>

***

## Submit the request

This final example sends a localized push notification to all subscribed users:

```curl  theme={null}
curl -X "POST" "https://api.onesignal.com/notifications" \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Key YOUR_API_KEY' \
     -d $'{
      "target_channel": "push",
      "included_segments": [
        "Subscribed Users"
      ],
      "app_id": "YOUR_APP_ID",
      "contents": {
        "en": "Hello, world",
        "es": "Hola mundo",
        "fr": "Bonjour le monde",
        "zh-Hans": "你好世界"
      }
    }'
```

Once the request is sent, OneSignal will send it to the appropriate downstream provider (e.g., Push: FCM, APNS, HMS; Email: your Email Service Provider; SMS: Twilio), who then delivers it to the end user.

### Handle the response

You will receive a `200` response code if the request is valid and accepted.

* If an `id` is returned, the message was created successfully. Save this `id` for future tracking and reference of message stats via [View Message API](/reference/view-message).
* If no `id` is returned, then the message was not created, likely due to no valid [Subscriptions](/docs/en/subscriptions) in the target audience.

**Response details by channel:**

* [Push](/reference/push-notification#response-id)
* [Email](/reference/email#response-id)
* [SMS](/reference/sms#response-id)

<Note>
  See our [REST API Overview](/reference/rest-api-overview#reliability-and-delivery) page for details on retries and [rate limits](/reference/rate-limits).
</Note>

***

## Next steps

Refer to the channel-specific APIs to customize delivery further:

* [Push notification](/reference/push-notification)
* [Email](/reference/email)
* [SMS](/reference/sms)
* [Live Activities](/reference/start-live-activity)
* [Server-Side SDKs](/docs/en/server-sdk-reference)

***

Built with [Mintlify](https://mintlify.com).
