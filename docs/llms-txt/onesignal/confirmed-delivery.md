# Source: https://documentation.onesignal.com/docs/en/confirmed-delivery.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Confirmed delivery

> Learn how OneSignal tracks received push notification events across iOS, Android, Huawei, and Web. See requirements, limitations, and troubleshooting steps to interpret confirmed delivery reports.

## Overview

Confirmed Delivery tracks when a device actually **receives** a push notification sent through OneSignal.

In your OneSignal Dashboard, this appears in the [Message Report](./push-notification-message-reports) as **Confirmed** (or **Received**). For a complete overview of all delivery and engagement metrics, see the [Metrics Glossary](./analytics-metrics-glossary).

<Frame caption="Confirmed Deliveries Flow">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/35ba167-analytics-ensure-confirmed-message-delivery_1.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=17ce8f50b8e92e0d368abe42865709c3" alt="Confirmed Deliveries Flow" width="800" height="667" data-path="images/docs/35ba167-analytics-ensure-confirmed-message-delivery_1.png" />
</Frame>

Push notifications are delivered through platform push services:

* **iOS & Safari:** Apple Push Notification Service (APNs)
* **Android & Chrome:** Google Firebase Cloud Messaging (FCM)
* **Huawei devices:** Huawei Messaging Service (HMS)
* **Amazon devices:** Amazon Device Messaging (ADM)
* **Windows devices:** Microsoft Push Notification Service (MPNS)

These services confirm when a notification was **delivered to the service successfully**, failed, or the device token is unsubscribed.

Once the user’s device receives the notification, the **OneSignal SDK sends a Confirmed Delivery event** back to OneSignal. This event includes:

* The notification ID
* The device’s [Subscription ID](./subscriptions)

This allows you to see exactly which Subscriptions received which notifications.

***

## Requirements

* Available only on **paid plans**. [Compare plans](https://onesignal.com/pricing).
* Complete [Mobile SDK Setup](./mobile-sdk-setup), including:
  * iOS Notification Service Extension
  * App Group configuration
* Confirmed Delivery only works if the device has the OneSignal SDK installed.
  * **Not supported** for subscriptions created via API only.

### Platform-specific limitations

#### iOS

* Requires both the **Notification Service Extension** and **App Group** setup.
* APNs keeps only **one message per app** when offline. If multiple pushes are sent while offline, only the latest is delivered.

#### Huawei

* Supported only for the `data` [Huawei message type](/reference/push-notification#body-huawei-msg-type).
* For the `message` type, Huawei provides receipt data only in their own dashboard.

#### Web

* Safari does **not** support Confirmed Delivery.

***

## FAQ

### Why are my Confirmed Delivery numbers low or missing?

Common causes:

1. Many inactive or abandoned devices. See [Handling inactive devices](#handling-inactive-devices).
2. Platform limitations (Huawei, Safari).
3. Setup issues — especially common with iOS. See [Troubleshooting Confirmed Delivery](#troubleshooting-confirmed-delivery).
4. Android devices may **force quit your app**, stopping SDK events. Some device manufacturers treat swiping the app away as a force quit. See [Mobile push not shown guide](./notifications-show-successful-but-are-not-being-shown).

#### Handling inactive devices

Devices that are offline won’t receive push notifications or send Confirmed Delivery events. This is common when users replace or abandon devices.

**Tips to re-engage inactive users:**

* Use **Audience Activity** to resend to users who did not Confirm Delivery.
* Create [Segments](./segmentation) based on **Last Session** (e.g., inactive for 90+ days).
  * Combine with a [Re-engagement Journey](./journeys-examples#re-engagement-campaign) to win them back.
  * Periodically target inactive users to prune unreachable devices.

<Note>
  See [When do push Subscription statuses update?](./subscriptions#when-do-push-subscription-statuses-update%3F) for more details.
</Note>

### Why does it show Confirmed but not appear on my device?

A Confirmed Delivery event means the device received the push. Rarely, the device may not display it.

Check for:

* You may have missed it. Try sending yourself a test push to see if it appears.
* **Focus Mode on iOS:** Pushes are delayed or grouped differently when “Do Not Disturb,” “Sleep,” or other [Focus modes](./ios-focus-modes-and-interruption-levels) are active. Dismissing grouped notifications may cause you to miss it.
* **Custom app code suppressing display:**
  * `event.preventDefault()` in the [foreground lifecycle listener](./mobile-sdk-reference#addforegroundlifecyclelistener-push) or [Notification Service Extension](./service-extensions)
  * Notification APIs that remove messages:
    * [`removeDeliveredNotifications(withIdentifiers:)`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications\(withidentifiers:\))
    * [`removeAllDeliveredNotifications()`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removealldeliverednotifications\(\))
* **Push payload settings:**
  * Make sure `priority` is set to high. See [Push priority](./push#priority).
  * Be careful with [`collapse_id`](./push#collapse_id) — it replaces older pushes with newer ones using the same ID.
* **Wrong device targeted:** Use [Find and set Test Subscriptions](./find-set-test-subscriptions) to confirm.

***

## Troubleshooting Confirmed Delivery

### General

* **Device offline:** Pushes can be delayed up to 3 days (default). Adjust with [Time To Live](./push#ttl).
* **Unstable network:** Notification may be received but the confirmation fails if the app crashes or has no network. This is rare.

### iOS

**Most common issue: misconfigured Notification Service Extension or App Groups.**

Checklist:

1. Add the `OneSignalNotificationServiceExtension` target in Xcode.
2. Double-check steps 3–6 in the [iOS SDK Setup](./ios-sdk-setup#3-add-app-target-to-app-group). Make sure to use the same App Group name for both app and extension:
   * ✅ `group.your-main-app-target-bundle-id.onesignal`
   * ❌ `group.your-bundle-id.OneSignalNotificationServiceExtension.onesignal`
   * If you use your own App Group name, you need to update your `Info.plist` files for both the main app and the Notification Service Extension to tell our SDK which App Group to use.
   * The App Group must be configured for both the main app and the Notification Service Extension. This includes correct `.xcconfig` files (make sure they are not missing).
3. Ensure `mutable-content: 1` is present in the payload (set automatically unless overridden).

See [Troubleshooting the iOS Notification Service Extension](./service-extensions#troubleshooting-the-ios-notification-service-extension) for advanced debugging.

### Android

* If notifications are not displaying: see [Mobile push troubleshooting](./notifications-show-successful-but-are-not-being-shown).
* If notifications show but Confirmed Delivery is missing: a custom Android Service Extension may be blocking it. Check our [Android Service Extension guide](./service-extensions#android-service-extension).

### Web

* Safari is not supported.
* For other browsers, ensure migration to **v16 SDK** is complete:
  * Correct SDK init:

    ```html  theme={null}
    <script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
    ```

  * Correct Service Worker reference:

    ```html  theme={null}
    importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");
    ```

***

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
