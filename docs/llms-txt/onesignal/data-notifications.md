# Source: https://documentation.onesignal.com/docs/en/data-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data & background notifications

> Learn how to configure and send silent background and VoIP notifications with OneSignal across iOS, Android, and supported derivatives. Includes payload setup, SDK requirements, and platform-specific limitations.

## Overview

Silent notifications let you wake your app and perform background tasks—such as syncing or refreshing data—without showing a visible message or playing a sound.

On iOS, these are called **Background Notifications**, and on Android, they’re known as **Data Notifications**. Together, they’re often referred to as silent pushes and behave differently from normal, visible notifications.

This guide explains how to configure and send silent notifications with OneSignal across supported platforms.

### Limitations

Silent notifications behave differently from normal push messages and have several platform-specific limitations.

* **Apps cannot receive silent pushes if**:
  * **iOS**: The app has been closed by the user like when swiped away from the app switcher. (See [Apple support](https://support.apple.com/en-us/HT201330)).
  * **Android**: The app has been force-quit via device settings or automatically by some manufacturers when swiped away. ([More details here](./notifications-show-successful-but-are-not-being-shown#android-app-is-force-stopped)).
* **Delivery is not guaranteed**:
  * Both Apple and Google treat silent notifications as *best-effort*. iOS may delay or drop delivery under Low Power Mode, Background App Refresh off, or if the app was closed by the user. Android may throttle or batch delivery under Doze or OEM power-saving rules.
  * Because of this, **silent notifications should never be used for critical updates**.
* **Subscribed users only**: The OneSignal SDK only sends data notifications to subscribed [Subscriptions](./subscriptions). To reach unsubscribed users, follow [this workaround](https://github.com/OneSignal/OneSignal-iOS-SDK/issues/302).
* **Limited support for cross-platform SDKs**:
  * Silent notifications must be handled in native code (Java/Kotlin for Android, Swift/Obj-C for iOS).
  * iOS requires implementation of [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application).
  * Android requires implementation of a [Notification Service Extension](./service-extensions).

***

## Sending silent notifications from OneSignal

Follow these steps to send a silent notification from OneSignal:

<Steps>
  <Step title="Omit visible content">
    Remove any visible text or titles from the message. This includes:

    * **API**: `contents`, `headings`, `subtitle` in your [Create notification](/reference/create-message) API request.
    * **Dashboard**: Message, Title, Subtitle
  </Step>

  <Step title="Set content_available">
    * **API**: Set `content_available` to `true`.
    * **Dashboard**: Check **Content available** under "Send to Apple iOS". This is applicable for all platforms and just tells our system that no message is being sent.
  </Step>

  <Step title="Add data to the notification">
    * **API**: Use the `data` parameter.
    * **Dashboard**: Use the **Additional Data** fields.
  </Step>
</Steps>

***

## Platform-specific setup

### iOS background notification setup

To handle background notifications, your iOS app must have the **Background Modes > Remote Notifications** capability enabled in Xcode. This is typically added if you followed our [Mobile SDK Setup](./mobile-sdk-setup).

Apple documentation:

* [Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc)
* [Generating a Remote Notification](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification)
* To process the notification, use the `AppDelegate` method [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application).

<Warning>
  If the user has closed the app (swiped it away from the app switcher), iOS will not deliver the notification.

  In such cases, include a visible `contents` message and process data in the [`UNNotificationServiceExtension.didReceive`](./service-extensions#ios-notification-service-extension).
</Warning>

***

### Android data notification setup

Handle data notifications on Android using the [Notification Service Extension](./service-extensions).

This lets you:

* Process notifications as long as the app hasn't been force closed
* Customize how notifications are displayed or suppressed

***

## Sending VoIP notifications

VoIP notifications are supported but require additional configuration outside the standard OneSignal SDKs. OneSignal does not register VoIP tokens automatically.

For setup instructions, see the [VoIP Notifications Setup Guide](./voip-notifications).

***

## FAQ

### Can silent notifications be used to detect uninstalls or unsubscribes?

Technically yes, but it’s unreliable. As explained in the [Limitations](#limitations) section above, silent notifications are not guaranteed to be delivered.

Instead:

* Send visible notifications (with content) to all your users at least once a month.
* Optionally send silent notifications as a supplemental check.

For more details on handling subscription status changes, see our [Subscriptions](./subscriptions) guide.

### Do confirmed deliveries work with silent notifications?

Confirmed deliveries do not work with silent notifications.

***

Built with [Mintlify](https://mintlify.com).
