# Source: https://documentation.onesignal.com/docs/en/notifications-show-successful-but-are-not-being-shown.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile push: Notifications not shown or delayed

> Troubleshoot mobile push notifications that show as Delivered in OneSignal but don't appear or are delayed on Android and iOS devices.

This page covers the most common reasons a push notification shows as Delivered in OneSignal but does not appear on the device — or appears significantly delayed.

In your OneSignal dashboard [Push message reports](./push-notification-message-reports):

* **Delivered** means OneSignal successfully handed the notification off to the push service (FCM, APNs, or HMS) and received a success response.
* **Confirmed** means the OneSignal SDK on the device received the notification.

If your notification is Delivered but not Confirmed, and it did not appear on the device, start below.

***

## Before you begin

Gather the following to help troubleshoot. You will need these to identify the correct Subscription and check delivery status.

* Your [OneSignal App ID](./keys-and-ids)
* The [Message ID](./push-notification-message-reports) of the notification that didn't show
* The affected user's [Subscription ID](./find-set-test-subscriptions)

<Note>
  If you only have the External ID, find the Subscription in **Audience > Subscriptions** by filtering on Device Type, Last Session, or IP Address.
</Note>

***

## Device settings

This section applies to all platforms. Check these first before investigating platform-specific or code-level causes.

### Permission and subscription status

On the device:

1. Navigate to **Settings > Notifications** and open the app's notification settings.
2. Confirm that notification permission is enabled.
3. Then open the app. If our SDK initializes, it will sync the subscription status back to OneSignal.

In your OneSignal dashboard:

1. Navigate to **Audience > Subscriptions**.
2. Search for the Subscription ID or External ID or sort by Device Type, Last Session, or IP Address.
3. Confirm the push status shows **Subscribed**. If it shows unsubscribed or does not appear, the device will not receive notifications regardless of what you send. If the status is unexpected, see [Troubleshooting](#troubleshooting) below.

### Do not disturb and focus modes

Do Not Disturb and Focus modes on both Android and iOS can suppress notifications entirely or group them in ways that make them appear invisible until the mode is cleared.

Disable these modes before testing:

* **iOS:** Settings > Focus > Do Not Disturb > turn off
* **Android:** Settings > Notifications > Do Not Disturb > turn off

Send a test notification after disabling. If the notification appears, the mode was the cause.

<Note>
  On iOS, if a notification arrives during Focus mode and the user swipes away the grouped notification summary, those notifications will not reappear individually later.
</Note>

### Low power mode and battery optimization

**iOS**: Disable Low Power Mode in Settings > Battery before testing.

**Android devices**: In Battery Settings, set the app to "Unrestricted" or "Not Optimized". If you don't see that option, search for **Battery Optimization**, **Power Saving Mode**, **Energy Saving**, **Background usage limits**, or **Adaptive Battery Settings** and disable for the app.

### Network and connectivity

Devices must be online to receive push notifications. If the device is turned off, in airplane mode, has unstable or no internet connection, the push will not show until a proper connection is made. You can set the timeframe FCM and APNs will wait for a connection with the Time To Live (TTL) Parameter (the default is 3 days).

If the device is on a WiFi network with a firewall or VPN, that network may be blocking the connection to Apple or Google servers. Test by switching to cellular data.

If you are managing network traffic through a firewall, configure it to allow the following:

* **FCM (Android):** outbound TCP ports 5228, 5229, and 5230. See [FCM documentation](https://firebase.google.com/docs/cloud-messaging/concept-options) for full requirements.
* **APNs (iOS):** outbound TCP port 5223 and TCP port 443 or 2197. See [Apple's documentation](https://support.apple.com/en-us/HT203609) for full requirements.

### Notification grouping behavior

Different versions of Android and iOS have their own notification grouping behavior. Notification grouping is when several notifications for the same app or multiple apps are grouped together in the notification center. It's common for grouped notifications to be dismissed together, causing users to miss individual notifications.

***

## Android issues

This section applies only to Android devices. If you are troubleshooting iOS, skip to [iOS issues](#ios-issues).

### Android Force Stop

When an Android app is Force Stopped, the operating system prevents it from receiving push notifications until the user manually reopens it. This is one of the most common causes of missed notifications on Android.

Some manufacturers — including Samsung, Xiaomi, and Huawei — aggressively Force Stop apps when the user swipes them away from the recent apps list, while exempting large apps like Gmail and WhatsApp. See [dontkillmyapp.com](https://dontkillmyapp.com/) for device-specific behavior.

To reduce Force Stop behavior on the affected device, try the following steps in order:

1. **Allow background activity**: Settings > Apps > Your App > Battery > Allow background activity.
2. **Disable sleeping apps**: Settings > Battery and Device Care > Battery > Background Usage Limits > Sleeping Apps > remove your app from this list.
3. **Lock the app in Recent Apps**: Open your app, tap the Recent Apps button, then tap and hold on the app window and select **Lock this app** (available on some Samsung models).
4. **Enable auto-start** (some devices): Settings > Apps > Your App > Permissions > Auto-Start > Enable.
5. **Disable adaptive battery optimization**: Settings > Battery and Device Care > Battery > More Battery Settings > Adaptive Battery > toggle off (or exclude your app).

To check whether your app has been Force Stopped, run the following command. Replace `com.company.appname` with your package name:

```bash  theme={null}
adb shell dumpsys package com.company.appname | grep stopped
```

`stopped=false` means the app is not Force Stopped. `stopped=true` means it is.

You can also send a few notifications and check logcat for this entry:

```text  theme={null}
W/GCM-DMM: broadcast intent callback: result=CANCELLED forIntent {
   act=com.google.android.c2dm.intent.RECEIVE pkg=com.onesignal.example (has extras)
}
```

If you see this cancelled intent, the app could not be started to process the notification.

<Note>
  FCM provides an API to check the last time a device connected to FCM servers. This can confirm whether the device is reachable at all. See [Google's documentation on app instance info](https://developers.google.com/instance-id/reference/server#get_information_about_app_instances) for details.

  To help users fix this themselves, use an in-app message to target known Android devices users with instructions to enable background activity. See [Example: Target certain Android manufacturers and devices](./example-target-certain-android-manufacturers-and-devices).
</Note>

### Android notification categories disabled

Android notification categories (also called channels) allow users to disable specific types of notifications from your app. If a category is disabled, notifications sent with that category will not appear on the device — even if the app has notification permission.

Check the category state on the device: **Settings > Notifications > Your App**. Confirm that "Show notifications" is enabled and that all categories are toggled on.

<Frame caption="Android app notification settings showing the Abandoned Cart - Urgent category toggled off, which prevents notifications from that category from appearing on the device.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5a83479-Screen_Shot_2021-07-29_at_7.47.11_AM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=7f6d3cc24cda04f807e1c9840895c22b" alt="Android app notification settings showing the Abandoned Cart - Urgent category toggled off, which prevents notifications from that category from appearing on the device." width="800" height="650" data-path="images/docs/5a83479-Screen_Shot_2021-07-29_at_7.47.11_AM.png" />
</Frame>

If no category is set on the notification, OneSignal uses a default Miscellaneous category. Verify this category is enabled if you are not using custom categories. See [Android Notification Categories](./android-notification-categories) for setup details.

<Warning>
  Samsung One UI 6.1 automatically disables notification categories for many apps. If your users are on Samsung devices and recently stopped receiving certain notifications, this is a likely cause. See coverage from [Android Police](https://www.androidpolice.com/one-ui-61-disables-notification-channels/) for details.
</Warning>

<Note>
  You can use in-app messages to target Samsung users with instructions to re-enable categories. See [Example: Target certain Android manufacturers and devices](./example-target-certain-android-manufacturers-and-devices).
</Note>

### Android Doze mode, priority, and deprioritized messages

Android's [Doze mode](https://developer.android.com/training/monitoring-device-state/doze-standby) and [App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby#understand_app_standby) features delay background processes — including push delivery — when the device is unplugged and stationary. These modes activate automatically and are not visible to the user.

Sending [high priority](./push#priority) messages will wake the device and bypass Doze mode. However, if you send too many high priority messages that do not result in visible notifications, FCM may automatically downgrade your messages to normal priority. From [FCM documentation](https://firebase.google.com/docs/cloud-messaging/android/message-priority):

> High priority messages on Android are meant for time sensitive, user visible content. If FCM detects a pattern in which messages do not result in user-facing notifications, your messages may be deprioritized to normal priority.

If you suspect deprioritization, reduce high priority usage to time-sensitive messages only.

### Android emulator setup

Push notifications on Android emulators require Google Play Services. If you are testing on an emulator and not receiving notifications, verify the following:

1. The emulator image includes the Google Play Store
2. The emulator is configured to use a Cold Boot

To set Cold Boot: open Android Studio Device Manager > select your device > Edit > Additional Settings > set Boot option to Cold Boot > save and restart.

***

## iOS issues

This section applies only to iOS devices. If you are troubleshooting Android, see [Android issues](#android-issues).

### APNs notification coalescing

If multiple notifications were sent while an iOS device was offline or unreachable, only the most recent one may appear when the device reconnects. APNs stores one notification per app while the device is offline and discards earlier ones. This is expected [APNs behavior](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns) and cannot be changed by OneSignal or your app.

### iOS foreground blocking

If you set up the [iOS UNUserNotificationCenterDelegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate), you may have code blocking the notification from showing while the app is in the foreground.

Remove this custom code and use our SDK's [Foreground Event Listener](./mobile-sdk-reference#addforegroundlifecyclelistener-push) instead.

### iOS badge clearing

When an app clears its badge count, iOS removes all of that app's notifications from the Notification Center. The OneSignal SDK clears badges automatically when the app opens, which means previously delivered notifications may disappear when the user next opens the app.

If this is causing confusion during testing, see [Badges](./badges) for how to control this behavior.

***

## Message configuration

This section covers issues caused by how the notification was configured in OneSignal, not by the device.

### Subscription not in the target audience

Check the message audience to verify that your mobile Subscription is included:

* **[Segments](./segmentation)**: Verify your Subscription meets all audience filter conditions.
* **Direct send**: Confirm the ID you are targeting is correct:
  * The Subscription is still subscribed to push.
  * It has a recent last session date — you may be sending to an old or inactive Subscription.

### Collapse ID replacing notifications

If you are setting a Collapse ID on your messages, a new notification with the same Collapse ID will silently replace any unread notification with that ID. If the user has not opened the earlier notification, they will only see the newest one. See [Remove notifications and TTL](./push) for details on how Collapse ID works.

***

## Code-level causes

This section requires access to the app's source code. If you do not have code access, share these checks with your development team.

### OneSignal foreground notification prevention

The OneSignal SDK's [Foreground Event Listener](./mobile-sdk-reference#addforegroundlifecyclelistener-push) includes an `event.preventDefault()` method that suppresses a notification while the app is in the foreground. If this method is called unconditionally in your code, all foreground notifications will be silently blocked.

While testing, keep the app in the background or fully closed to rule out foreground suppression as the cause.

### Android Notification Service Extension

If you have implemented the [Android Notification Service Extension](./service-extensions), this is the first entry point for an incoming notification in your app. If `event.preventDefault()` is called inside this extension, the notification will be blocked regardless of app state. Review the extension code and confirm this method is only called intentionally.

### Firebase Messaging SDK conflict

If your app also includes the Firebase Messaging SDK, verify it is not intercepting FCM messages before OneSignal can process them.

This issue commonly occurs when:

* Notifications show as **Delivered** in OneSignal but never appear on the device.
* The app includes both OneSignal and `firebase_messaging` (or a custom `FirebaseMessagingService`).
* Push works when Firebase Messaging is removed, but fails when both SDKs are present.

1. Check your `AndroidManifest.xml` for legacy Firebase receivers such as `com.google.firebase.iid.FirebaseInstanceIdReceiver` and remove/conditionally exclude them if OneSignal is responsible for push delivery.

2. Check for custom `FirebaseMessagingService` implementations (or libraries such as `firebase_messaging` in Flutter) that override `onMessageReceived`. If another service fully processes or suppresses messages, it may consume the FCM payload before OneSignal can display the notification.

3. Avoid calling Firebase token management APIs such as: `FirebaseMessaging.getToken()` or `FirebaseMessaging.deleteToken()`.

If OneSignal is responsible for push delivery, it should be the only SDK managing the push token lifecycle. Fetching or managing the FCM token directly can lead to token ownership conflicts and inconsistent delivery behavior.

If you need the device push token for other systems, read it from OneSignal (for example, `User.pushSubscription.token`) and listen for subscription/token changes using the [SDK's observer APIs](./mobile-sdk-reference#addobserver-push-subscription-changes).

***

## Troubleshooting

If you have worked through the sections above and the issue is not resolved, capture a debug log. This is the fastest way to identify exactly where delivery is failing.

Follow [Getting a Debug Log](./capturing-a-debug-log) to enable verbose logging in your app. Then:

1. Put the app in the background
2. Send a test notification to the affected device
3. Check the log for any errors. Make sure you see OneSignal initialized and the `subscription-id` in the log is subscribed to push and the same as the one you are sending the message to.

***

<Info>
  Need help?

  Contact our Support team at `support@onesignal.com`

  Please include:

* Your OneSignal App ID
* The Subscription ID or External ID
* The URL to the message you tested in the OneSignal Dashboard
* The full debug log from [Getting a Debug Log](./capturing-a-debug-log)

  We're happy to help!
</Info>

Built with [Mintlify](https://mintlify.com).
