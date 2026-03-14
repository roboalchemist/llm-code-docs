# Source: https://documentation.onesignal.com/docs/en/preference-center.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preference center

> Learn how to implement a custom user preference center in your app or website using OneSignal APIs to manage notification topics, frequencies, channels, and data privacy settings.

## What is a preference center?

A Preference Center is a page on your app or website that allows your users to control how and what kind of messages they receive from you. For more details and reasons why to create a Preference Center, see [A Guide to User Preference Centers](https://onesignal.com/blog/a-guide-to-user-preference-centers).

This guide explains the technical setup needed to include a user preference center in your app or website using OneSignal's APIs. In this guide we discuss how to:

* assign topics, categories, and frequency controls with [Data Tags](./add-user-data-tags)
* collect new communication channels (push notifications, email, SMS)
* disable communication channels if the user wants to opt-out
* handle data compliance
* delete user data

## Requirements

* OneSignal's Mobile SDKs version 5+ and/or Web SDK 16+
* Setting the [External ID or Alias](./users)
* OneSignal does not provide any APIs for creating the Preference Center layout, only the APIs to GET, PATCH, and DELETE Users and Subscriptions
  * If you have a website and need a simple preference center, try our [Category Prompt](./permission-requests)

### Additional recommended reading

* [A Guide to User Preference Centers](https://onesignal.com/blog/a-guide-to-user-preference-centers)
* [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk)
* [Handling Personal Data](./handling-personal-data)

## Setup

When the user lands on your preference center, use the [View user](/reference/view-user) API to pull the OneSignal data for the user based on either the `external_id` or a custom alias you set. This will provide you the user `properties` and `subscriptions`. Helpful data includes but not limited to:

* `properties`: the user data
  * `tags` - custom data you send to OneSignal
  * `language` - the language code for the user
* `subscriptions`: the messaging channels and subscription status
  * `id` - the Subscription ID
  * `type` - `Email`, `SMS`, \*Push (`AndroidPush`, `iOSPush`, `ChromePush`, `SafariPush`, etc)
  * `enabled` - `true` means subscribed, `false` means unsubscribed
  * `token` - the push token, email address, or phone number depending on the subscription type

<CodeGroup>
  ```json json theme={null}
  {
    "properties": {
      "tags": {
        "finance": "1",
        "tech": "1",
        "sports": "1",
        "breaking-news": "0",
        "entertainment": "0",
        "deals": "0",
        "newsletter-frequency": "weekly",
        "customer_status": "Enterprise",
        "event": "1693411710",
        "first_name": "Jon",
        "last_name": "F"
      },
      "language": "en"
    },
    "subscriptions": [
      {
        "id": "sub_id_1",
        "type": "Email",
        "token": "email@example.com",
        "enabled": true
      },
      {
        "id": "sub_id_2",
        "type": "SMS",
        "token": "1234567890",
        "enabled": true
      },
      {
        "id": "sub_id_3",
        "type": "ChromePush",
        "token": "some_token_here",
        "enabled": true
      }
    ]
  }
  ```
</CodeGroup>

Use the data provided to populate the preference center as needed.

## Assign categories and frequency controls

Refer to [Data Tags](./add-user-data-tags). Tags are key-value pairs used to segment and personalize. Use string-encoded integers or timestamps to enable range-based filtering.

Users can toggle interests (e.g., `sports: 1`) or set frequency tags like `newsletter-frequency: weekly`. Use this data in [Segments](./segmentation) or the [Create notification](/reference/create-message) API with filters.

To update a tag, call the [Update user](/reference/update-user) API.

## Collect new communication channels

Check `subscriptions` for type and enabled status. Show `token` only for email/SMS, not for push.

<Warning>
  If contact info exists in your system but not yet in OneSignal, use your own
  DB as a fallback to display it.
</Warning>

### Email & SMS updates

Use `addEmail`, `addSms` SDK methods or [Create subscription](/reference/create-subscription) and [Update subscription](/reference/update-subscription) APIs. Subscription `id` is required for updates.

### Push updates

If push is not enabled, prompt user.

* For mobile apps: [Prompt for Push Permissions](./prompt-for-push-permissions)
* For web: use [Native Browser Prompt](./permission-requests) or [Slide Prompt](./permission-requests)

## Disable communication channels

Use [Update subscription](/reference/update-subscription) to set `enabled` to `false`. Toggle to `true` to opt-in again.

## Handle data compliance

Prevent SDK init by default and require user consent to initialize. See [Handling Personal Data](./handling-personal-data).

## Delete user data

Use [Delete user](/reference/delete-user) API to fully remove a user from OneSignal.

***

Built with [Mintlify](https://mintlify.com).
