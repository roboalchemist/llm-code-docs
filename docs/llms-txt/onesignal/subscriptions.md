# Source: https://documentation.onesignal.com/docs/en/subscriptions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscriptions

> Understand and manage user Subscriptions across channels like mobile push, web push, email, and SMS. Learn how Subscriptions work, their properties, and how to update or migrate them.

## Overview

A **Subscription** represents a specific channel a user can receive messages through—such as an email address, phone number, or device. OneSignal supports four types of Subscriptions:

* **Email** – for sending email messages
* **SMS** – for sending text messages
* **Web Push** – for push notifications via web browsers
* **Mobile** – for push notifications, in-app messages, and Live Activities on mobile devices

Each user can have multiple Subscriptions. Use the [External ID](./users#external-id) to identify the user across all Subscriptions.

<Frame caption="OneSignal Dashboard Audience > Subscriptions page. Shows multiple Subscriptions associated with a single user via the External ID.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/subscription-types.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=7b88e08aaeb18e979c4e52949359ae36" width="3424" height="920" data-path="images/dashboard/subscription-types.png" />
</Frame>

In the image above, "userA" has 5 Subscriptions:

1. **Mobile** (iOS) created after installing the iOS app. Call `OneSignal.login` to set the External ID and link the Subscription to the user.
2. **SMS** created after the phone number provided within the iOS app. See [SMS Subscriptions](#sms-subscriptions) below for details.
3. **Web Push** created after subscribing to push on the website. Can receive push notifications.
4. **Email** created after the email address was provided. For sending email messages.
5. **Mobile** (Android) created after installing the Android app. Can receive push notifications, in-app messages, and Live Notifications.

<Note>
  A user can have a maximum of 20 Subscriptions. If a 21st is added, OneSignal removes the External ID from the oldest Subscription (based on last session) and assigns it a new OneSignal ID—effectively creating a new anonymous user for the inactive Subscription.

  However, OneSignal ensures at least 3 Email and 3 SMS Subscriptions (if applicable) are retained.

  See [Users](./users) for details.
</Note>

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/yZM6zn7nLDw?si=oT7ncbhX0sNtmKML" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## Subscription properties

Each Subscription has the following properties:

|         Property        | Description                                                                                                                                                                                                                                                                                                                   |
| :---------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       **Channel**       | Type of Subscription: `Email`, `SMS`, or `Push`. Push can be Mobile (iOS, Android, etc.) or Web. Only Mobile Push Subscriptions support in-app messages.                                                                                                                                                                      |
| **Subscription Status** | Indicates if the Subscription can receive messages. See [Subscription status](#subscription-statuses) for more details.                                                                                                                                                                                                       |
|     **Last Session**    | Timestamp of the last session tracked by the OneSignal SDK. For Email/SMS, it's based on the most recent push Subscription.                                                                                                                                                                                                   |
|    **Usage Duration**   | Total time (in seconds) the Subscription was active on the app or site tracked by the OneSignal SDK. Only tracked when session exceeds 60s.                                                                                                                                                                                   |
|       **Sessions**      | Count of how many times the app/site was opened. A new session starts after 30+ seconds of being out-of-focus.                                                                                                                                                                                                                |
|    **First Session**    | Timestamp when the first Subscription for the User was created.                                                                                                                                                                                                                                                               |
|      **IP Address**     | Network location when using OneSignal SDKs. Not collected in the EU. See [Handling Personal Data](./handling-personal-data).                                                                                                                                                                                                  |
|   **Subscription ID**   | UUID representing the specific Subscription. Used for identifying the Subscription.                                                                                                                                                                                                                                           |
|     **OneSignal ID**    | UUID representing the User. See [Users](./users).                                                                                                                                                                                                                                                                             |
|     **External ID**     | Your custom user ID. Helps link multiple Subscriptions to the same user.                                                                                                                                                                                                                                                      |
|        **Device**       | The device model the Subscription was created with. For example, `armv81` for web push browsers are Android devices.                                                                                                                                                                                                          |
|        **Email**        | Only set for Email Subscriptions.                                                                                                                                                                                                                                                                                             |
|     **Phone Number**    | Only set for SMS Subscriptions. Must be in [E.164 format](https://en.wikipedia.org/wiki/E.164).                                                                                                                                                                                                                               |
|     **App Version**     | From SDK: Android `versionCode`, iOS `CFBundleShortVersionString`.                                                                                                                                                                                                                                                            |
|     **SDK Version**     | Version of the OneSignal SDK used. See [GitHub > SDKs (select your SDK) > Releases](https://github.com/OneSignal/sdks).                                                                                                                                                                                                       |
|     **Timezone ID**     | From the device at time of last interaction.                                                                                                                                                                                                                                                                                  |
|       **Country**       | Derived from IP address.                                                                                                                                                                                                                                                                                                      |
|    **Location Point**   | Latitude/longitude if location tracking is enabled. See [Location-triggered notifications](./location-triggered-event).                                                                                                                                                                                                       |
|    **Language Code**    | From the device at time of Subscription creation. See [Multi-language messaging](./multi-language-messaging).                                                                                                                                                                                                                 |
|         **Tags**        | Custom key-value metadata. See [Tags](./add-user-data-tags).                                                                                                                                                                                                                                                                  |
|      **Push Token**     | Platform token used for push delivery (e.g., APNS or FCM). Only for Push Subscriptions.<br />- **iOS Push APNS token format**: 64 characters, hexadecimal characters only (0-9,a-f).<br />- **Android Push FCM token format**: Typically 163 characters, alphanumeric characters, may contain hyphens, colons and underscore. |
|        **Rooted**       | Indicates if the Android device is rooted (jailbroken).                                                                                                                                                                                                                                                                       |

### Subscription statuses

Generally, Subscriptions can either receive messages (**Subscribed**) or cannot receive messages (**Unsubscribed**). However, there are some exceptions:

**Mobile Subscriptions**

* **Subscribed**: The user has granted permission to receive push notifications.
  * If you have [iOS Provisional push enabled](./ios-provisional-push-notifications), then all iOS mobile Subscriptions are Subscribed until disabled by the user.
* **Unsubscribed**: The Subscription cannot receive push notifications but can receive in-app messages.
  * See [Handling uninstalls, unsubscribes, & invalid push tokens](#handling-uninstalls%2C-unsubscribes%2C-%26-invalid-push-tokens) for more details.
* **Never Subscribed** – User never granted permission (same as unsubscribed).

**Web Subscriptions**

* **Subscribed**: The user has granted permission to receive push notifications.
* **Unsubscribed**: The Subscription cannot receive push notifications.
  * See [Handling unsubscribes & invalid push tokens](#handling-unsubscribes-%26-invalid-push-tokens) below for more details.

**Email Subscriptions**

* **Subscribed**: The user should have provided consent to receive email messages and the email address is valid.
* **Unsubscribed**: The user opted-out of receiving emails but can be [overridden](./email-messaging#send-to-unsubscribed-users) if needed.
  * See [Email Subscriptions](#email-subscriptions) below for more details.

**SMS Subscriptions**

* **Subscribed**: The user should have provided consent to receive SMS messages and the phone number is valid.
* **Unsubscribed**: The user opted-out of receiving SMS messages.
  * See [SMS Subscriptions](#sms-subscriptions) below for more details.

<Info>
  Using our API, `invalid_identifier: true` means unsubscribed. Check `notification_types` for more details.
</Info>

***

### `notification_types`

Indicates the Subscription's ability to receive messages, including reasons for failures. Automatically updated via our frontend SDKs or manually via the API. Viewable via the [View User API](/reference/view-user) or [Export CSV](/reference/csv-export).

<Accordion title="Notification Types definitions." icon="circle-chevron-down">
  `1` or positive number = Subscribed.

* The Subscription can receive messages on this channel.
* Can be used with `enabled` property if you are enabling messages on behalf of the user. For push Subscriptions, a valid `token` must still be set to receive push notifications. See our SDK setup docs for details.

  `0`, `-99` = Never Subscribed.

* The Subscription has not subscribed to the channel yet.

  `-2` = Unsubscribed.

* The Subscription cannot receive messages on this channel.
* Can be used with `enabled` property set to `false` if you are turning off messages on behalf of the user. Recommended value when turning off message permissions.
* Automatically set when the user unsubscribes.

  `-3`, `-5` = Android `Support Library Error`.

  Add or update your app's [Android Support Library](https://developers.google.com/android/).

  `-4`, `-8`, `-11`, `-12` = Android `Google Play Services Library Error`.

* Check the logcat. See [Getting a Debug Log](./capturing-a-debug-log).
* Upgrade your [Google Play Services Library](https://developers.google.com/android/) in your app and check the app's logcat for Google Play Services errors. See [Getting a Debug Log](./capturing-a-debug-log).

  `-6` = Android `Invalid Google Project Number`.

* The FCMv1 Sender ID doesn't match the original in which this `token` belongs. Check the app's logcat. See [Getting a Debug Log](./capturing-a-debug-log).

  `-7`, `-9` = Android `Outdated Google Play Services App`

* Update or enable the Google Play Services app on the device.

  `-10` = Not Subscribed.

* Push Subscription uninstalled app or unsubscribed in device settings.
* Web push blocked notifications, cleared all data and workers.

  `-13` = iOS `missing_push_capability`.

* Review the SDK setup docs to make sure all steps are implemented. See [Channel setup](./channel-setup).

  `-14`, `-16`, `-17` = iOS `APNS Errors`.

* The device is having an issue connecting to APNS. Check the [Troubleshooting iOS](./mobile-troubleshooting) guide and [Getting a Debug Log](./capturing-a-debug-log).

  `-15` = iOS `Simulator Error`.

* iOS Simulator required iOS 16.4+ Use a different simulator or device.

  `-18` = Never Prompted.

* The Subscription was never prompted to subscribe. This only tracks the required permission prompt and does not include in-app messages.

  `-19` = Prompted But Never Answered.

* The Subscription was prompted but didn't provide an answer.

  `-20`, `-21` = temp\_web\_record. Web, `pushSubscriptionchange` permission revoked

  `-22` = Manually Unsubscribed via dashboard.

* Permission was revoked.

  `-23`, `-24` = Web `Service Worker Error`.

* See [Web SDK troubleshooting](./troubleshooting-web-push).

  `-31` = Disabled via REST API.

  `-98` = SMS Subscription awaiting double opt-in.
</Accordion>

***

## Mobile Subscriptions

Mobile Subscriptions represent iOS, Android, Huawei, or Amazon devices and support:

* Push notifications
* In-app messages
* Live Activities

They're automatically created when a user installs and opens your app with the OneSignal SDK.

<Note>
  Each mobile Subscription is tied to the device & push token it was created on. If your app is uninstalled and reinstalled on the same device, a new Subscription will be generated.

  Call [`OneSignal.login`](./mobile-sdk-reference#login-external-id) each time the user opens the app to make sure the [External ID](./users#external-id) is set and the Subscription is linked to the user.
</Note>

### Updating mobile Subscriptions

Mobile Subscription properties are recommended to be updated via the [OneSignal mobile SDK](./mobile-sdk-reference).

* [Prompt for push permissions](./prompt-for-push-permissions) and [observe permission/Subscription changes](./mobile-sdk-reference#addobserver-push-subscription-changes)
* [Login users](./mobile-sdk-reference#login-external-id) to set External ID and Aliases
* Add [Tags](./add-user-data-tags)
* Set [Language](./multi-language-messaging)

You can update tags, language, and some other properties via the [CSV Import](./import) feature.

Mobile Subscriptions can be created and updated via the [Users](/reference/create-user) and [Subscriptions](/reference/create-subscription) APIs as well, but the mobile SDK is recommended for most use cases.

### Handling uninstalls, unsubscribes, & invalid push tokens

Mobile Subscriptions stop receiving push notifications if the user:

* Uninstalls the app
* Disables push in device settings and never reopens the app
* [Push token expires](./fcm-expired-token-faq)

In these cases, the Subscription status will be set to **Unsubscribed** when sending push notifications. See below [When do push Subscription statuses update?](#when-do-push-subscription-statuses-update) for more details.

* If the user re-installs the app on the same device or new device, a new Subscription will be created and they need to re-subscribe to receive messages.
* If the user re-enables push in the device settings, the Subscription status will be set to **Subscribed** and a push token will be updated when they open the app.
* If the push token expires, the Subscription status and new push token will update when the user opens the app on the same device.

Track changes via:

* [Event Streams](./event-streams) - detect unsubscribes when sending push
* [Push reports](./push-notification-message-reports) - detect unsubscribes when sending push
* Use the SDK’s [Subscription change listener](./mobile-sdk-reference#addobserver-push-subscription-changes) - detect unsubscribes when user disables push in device settings then opens the app

***

## Web push Subscriptions

Web push Subscriptions are tied to a specific device, browser, and browser profile. A user who subscribes on Chrome desktop will not receive push on Chrome mobile unless they also subscribe to your website from that mobile device—creating a separate web push Subscription.

New web push Subscriptions are created in these scenarios:

* User subscribes to your website by clicking "Allow" on the browser's system-level [native permission prompt](./permission-requests). This generates a unique push token and Subscription ID.
* User clears browser data (history, cache, cookies, local storage) and revisits your site. This results in a new unique Subscription ID being created.

<Note>
  Web push Subscription IDs will never change. However, new Subscription IDs will be created if the user clears browser data and returns to the site or subscribes on a different browser/browser profile.

  Call [`OneSignal.login`](./web-sdk-reference#login-external-id) each time the user opens the site or within the [Subscription change listener](./web-sdk-reference#addeventlistener-push-subscription-changes) to make sure the [External ID](./users#external-id) is set and the Subscription is linked to the user.
</Note>

### Updating web push Subscriptions

Web push Subscription properties are recommended to be updated via the [OneSignal web SDK](./web-sdk-reference).

* [Prompt for push permissions](./permission-requests) and [observe permission/Subscription changes](./web-sdk-reference#addeventlistener-push-subscription-changes)
* [Login users](./web-sdk-reference#login-external-id) to set External ID and Aliases
* Add [Tags](./add-user-data-tags)
* Set [Language](./multi-language-messaging)

You can update tags, language, and some other properties via the [CSV Import](./import) feature.

Web push Subscriptions can't be created via the REST API but can be updated with [Users](/reference/update-user) and [Subscriptions](/reference/update-subscription) APIs, but the web SDK is recommended for most use cases.

### Handling unsubscribes & invalid push tokens

Web push Subscriptions stop receiving push notifications if the user:

* Clears browser data (history, cache, cookies, local storage)
* Disables push in the browser system settings
* [Push token expires](./fcm-expired-token-faq)

In these cases, the Subscription status will be set to **Unsubscribed** when sending push notifications. See below [When do push Subscription statuses update?](#when-do-push-subscription-statuses-update) for more details.

* If the user returns to the site after clearing browser data, a new Subscription will be created and they will be automatically re-subscribed to receive messages if you have [auto-resubscribe enabled](./web-push-setup#auto-resubscribe).
* If the user re-enables push in the browser settings, the Subscription status will be set to **Subscribed** when they return to the site.
* If the push token expires, the Subscription status and new push token will update when the user returns to the site.

<Warning>
  Chromium put out a [blog post](https://blog.chromium.org/2025/10/automatic-notification-permission.html?m=1) in October 2025, regarding a change that will **automatically revoke push permissions** for users with low site engagement who are being sent a high volume of notifications. The threshold for when a user is considered to have a [low engagement score](https://www.chromium.org/developers/design-documents/site-engagement/), appears to be about 30 days of inactivity. When revoked, the end user should receive a notification from Chrome directly.
</Warning>

Track changes via:

* [Event Streams](./event-streams) - detect unsubscribes when sending push
* [Push reports](./push-notification-message-reports) - detect unsubscribes when sending push
* Use the SDK’s [Subscription change listener](./web-sdk-reference#addeventlistener-push-subscription-changes) - detect unsubscribes when user disables push then returns to the site

***

## Email Subscriptions

Email Subscriptions are based on the email address and used only for email delivery. This is different from setting a [Tag](./add-user-data-tags).

Create Email Subscriptions via:

1. SDK `addEmail` method or [email prompt](./permission-requests) - use these methods after calling `OneSignal.login` to set the External ID and link the Subscription to the user.
2. [Create user API](/reference/create-user) or [Create email API](/reference/email)
3. Dashboard [CSV Importer](./import) or manually add email addresses

<Note>
  Emails are unique per app. Deleting and re-adding the same email creates a new Subscription ID.

  It is recommended to include the `external_id` when creating email Subscriptions to link them to a [User](./users).
</Note>

### Managing email Subscriptions

**Link to a user**

Make sure to set the `external_id` when creating email Subscriptions to link them to a [User](./users).

* Using the SDK, call the `login` method before calling `addEmail` to set the `external_id` and link the email Subscription to the user.
* Using the CSV Importer or REST API, set the `external_id` identifier with the email.

**Subscription statuses**

Newly created email Subscriptions will automatically be set to **Subscribed** unless otherwise specified.

Email Subscriptions can become unsubscribed when:

* Sending emails, the user opts-out via the [Unsubscribe link](./unsubscribe-links-email-subscriptions)
* Setting `enabled` to `false` via the API
* Using the dashboard to unsubscribe the Subscription via the options button
  Email Subscriptions can become resubscribed via:
* Setting `enabled` to `true` via the API
* Using the dashboard to subscribe the Subscription via the options button

If a user unsubscribes from emails, you can keep them as unsubscribed but send them important emails by [sending to unsubscribed emails](./email-messaging#send-to-unsubscribed-users).

***

# SMS Subscriptions

SMS Subscriptions are tied to [E.164 formatted phone numbers](https://en.wikipedia.org/wiki/E.164).

Created via:

1. SDK `addSms` or [SMS prompt](./permission-requests) - use these methods after calling `OneSignal.login` to set the External ID and link the Subscription to the user.
2. [Create user](/reference/create-user) or [Create SMS](/reference/sms) API
3. [CSV Importer](./import)

<Note>
  Phone numbers are unique per app. Re-adding after deletion creates a new Subscription ID.

  It is recommended to include the `external_id` when creating SMS Subscriptions to link them to a [User](./users).
</Note>

### Manage SMS Subscriptions

* User unsubscribes by replying with "STOP" or other [SMS consent keywords](./sms-consent-keyword-management)
  * The user can also resubscribe by replying with "START" or other [SMS consent keywords](./sms-consent-keyword-management)
* Update Subscription via API `enabled` property

***

## Importing or migrating Subscriptions

Import push tokens, email addresses, and phone numbers from another provider using:

* [Create user API](/reference/create-user)
* [Create Subscription API](/reference/create-subscription)

<Note>
  See [Migrating to OneSignal](./migrating-to-onesignal) for details.
</Note>

***

## Delete Subscriptions

Subscriptions can be deleted for:

* Data privacy
* Cleaning up inactive records

See [Delete users](./delete-users) for details.

<Note>
  Subscriptions with no activity for 18+ months are automatically deleted on Free plans.
</Note>

***

## FAQ

### When do push subscription statuses update?

Push subscription statuses update through two mechanisms:

**1. When the user opens your app or site**

The OneSignal SDK checks whether the push token is valid and whether notification permissions are still granted, then updates the subscription status immediately.

For example, if a user disables push notifications in their device settings and then reopens your app, the SDK detects the change and marks the subscription as **Unsubscribed** right away.

You can capture these changes with the SDK's Subscription Observer ([mobile](./mobile-sdk-reference#addobserver-push-subscription-changes) | [web](./web-sdk-reference#addeventlistener-push-subscription-changes)) to sync status to your own database.

**2. When you send push notifications**

If a user uninstalls your app, clears browser data, or disables push **and never returns**, OneSignal cannot detect the change until you send a notification. The push service (FCM, APNs, HMS) reports the token as invalid, and OneSignal marks the subscription as **Unsubscribed**.

This detection typically takes 2 or more messages because the push service does not immediately reject an invalid token:

| Send       | What happens                                                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message 1  | Delivered to device. User then unsubscribes in device settings or uninstalls the app.                                                                       |
| Message 2  | Push service accepts the message but the device does not receive it. OneSignal reports "Delivered" because the push service has not rejected the token yet. |
| Message 3  | Push service rejects the token. OneSignal marks the subscription as **Unsubscribed**.                                                                       |
| Message 4+ | OneSignal does not attempt delivery to this subscription.                                                                                                   |

Use [Event Streams](./event-streams) to detect unsubscribes in real time when sending messages.

<Note>
  If you go long periods without sending to all users, unsubscribes accumulate silently and appear as a large spike when you resume sending. Send to all users at least once or twice a month to detect unsubscribes gradually. See [FCM expired token FAQ](./fcm-expired-token-faq) for more on unsubscribe spikes.
</Note>

<Warning>
  Apple delays unsubscribe reporting by 14+ days. To protect user privacy, Apple does not immediately report uninstalls or permission revocations. If a user opens your app after disabling push, OneSignal detects the change instantly via the SDK. If the user never opens the app again, it may take several weeks for Apple to report the invalid token after you send notifications.

  See [Apple Forum](https://developer.apple.com/forums/thread/670868) and [Technical Note](https://developer.apple.com/library/archive/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG34) for details. Use the dashboard or API to [delete old subscriptions](./delete-users) to keep your audience clean.
</Warning>

### If a user turns off notifications in their device settings and never opens the app again, what happens?

The subscription remains marked as **Subscribed** in OneSignal until you send a notification to that device. After 2 or more send attempts, the push service reports the token as invalid and OneSignal marks the subscription as **Unsubscribed**. See [When do push subscription statuses update?](#when-do-push-subscription-statuses-update) above for the full sequence.

***

Built with [Mintlify](https://mintlify.com).
