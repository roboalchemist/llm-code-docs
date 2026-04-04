# Source: https://documentation.onesignal.com/docs/en/mobile-troubleshooting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile SDK troubleshooting

> Resolve common OneSignal Mobile SDK issues including push delivery failures, APNS errors, and in-app messaging problems across iOS, Android, and cross-platform frameworks.

<Note>
  If you are having issues with your website, see the [Web Push Troubleshooting guide](./troubleshooting-web-push).
</Note>

## Troubleshooting steps

### Review setup instructions and update the SDK

We frequently [release updates](https://github.com/OneSignal/sdks) with bug fixes, improvements, and support for the latest operating system changes. Ensure you are using the latest SDK version and have followed the setup instructions.

<Card title="Mobile SDK setup" icon="wrench" href="./mobile-sdk-setup">
  Setup instructions designed to help prevent common issues and test the integration.
</Card>

### Check common troubleshooting guides

<Columns cols={2}>
  <Card title="Notifications not shown or delayed" icon="bell-slash" href="./notifications-show-successful-but-are-not-being-shown">
    Push notifications are not appearing on the device or are delayed.
  </Card>

  <Card title="Notification images not showing" icon="image" href="./notification-images-not-showing">
    Images are not appearing in the expanded notification view.
  </Card>

  <Card title="Notification CTR" icon="arrow-pointer" href="./notification-ctr">
    Low or no clicks on notifications.
  </Card>

  <Card title="Duplicated notifications" icon="copy" href="./duplicated-notifications">
    Notifications are appearing multiple times on the device.
  </Card>

  <Card title="In-app message troubleshooting" icon="message" href="./in-app-message-troubleshooting">
    In-app messages are not displaying or behaving as expected.
  </Card>
</Columns>

### Check your app for common issues

#### OneSignal methods that block push from showing

Check your app for `optOut()` like `OneSignal.User.pushSubscription.optOut()` or if you set `enabled: false` via our REST APIs. This sets the push subscription status to `unsubscribed`. See [Mobile SDK reference](./mobile-sdk-reference#optout-%2C-optin-%2C-optedin) for more details.

If you have the app open while the push is being sent, you may be preventing the push from showing via the `preventDefault()` method. This is usually set in the [Foreground Event Listener](./mobile-sdk-reference#addforegroundlifecyclelistener-push) or [Android Notification Service Extension](./service-extensions).

#### Firebase Messaging or other SDK conflicts

If your app also includes the Firebase Messaging SDK or other push notification SDKs, verify it is not intercepting messages before OneSignal can process them.

This issue commonly occurs when:

* Notifications show as **Delivered** in OneSignal but never appear on the device.
* The app includes both OneSignal and `firebase_messaging` (or a custom `FirebaseMessagingService`).
* Push works when Firebase Messaging is removed, but fails when both SDKs are present.

1. Check your `AndroidManifest.xml` for legacy Firebase receivers such as `com.google.firebase.iid.FirebaseInstanceIdReceiver` and remove/conditionally exclude them if OneSignal is responsible for push delivery.

2. Check for custom `FirebaseMessagingService` implementations (or libraries such as `firebase_messaging` in Flutter) that override `onMessageReceived`. If another service fully processes or suppresses messages, it may consume the FCM payload before OneSignal can display the notification.

3. Avoid calling Firebase token management APIs such as: `FirebaseMessaging.getToken()` or `FirebaseMessaging.deleteToken()`.

If OneSignal is responsible for push delivery, it should be the only SDK managing the push token lifecycle. Fetching or managing the FCM token directly can lead to token ownership conflicts and inconsistent delivery behavior.

If you need the device push token for other systems, read it from OneSignal (for example, `User.pushSubscription.token`) and listen for subscription/token changes using the [SDK's observer APIs](./mobile-sdk-reference#addobserver-push-subscription-changes).

### Test an example project your SDK

Check if the issue is reproducible using the example project maintained by our engineering team for each SDK.

* [iOS example project](https://github.com/OneSignal/OneSignal-iOS-SDK/tree/main/OneSignalSwiftUIExample)
* [Android example project](https://github.com/OneSignal/OneSignal-Android-SDK/tree/main/examples)
* [Cordova variants example project](https://github.com/OneSignal/OneSignal-Cordova-SDK/tree/main/examples)
* [React Native example project](https://github.com/OneSignal/react-native-onesignal/tree/main/examples)
* [Flutter example project](https://github.com/OneSignal/OneSignal-Flutter-SDK/tree/main/examples)
* [Unity example project](https://github.com/OneSignal/OneSignal-Unity-SDK/tree/main/examples)
* [.NET MAUI example project](https://github.com/OneSignal/OneSignal-DotNet-SDK/tree/main/examples)

### Check the error logs

Gather log data before diagnosing further:

* Follow the guide on [capturing a debug log](./capturing-a-debug-log).
* Look for errors, warnings, or deprecation notices that could explain the behavior.

<Card title="Capturing a debug log" icon="bug" href="./capturing-a-debug-log">
  How to enable verbose logging and capture SDK output for troubleshooting.
</Card>

### Contact support

If you are still experiencing the issue, contact `support@onesignal.com` with:

* Your OneSignal App ID
* Your External ID and/or Subscription ID of the affected device
* The notification ID or a link to the notification in the dashboard (if applicable)
* A [debug log from the device](./capturing-a-debug-log) reproducing the issue

***

## Common errors

### APNS Delegate never fired

Errors like "APNS Delegate Never Fired" and "APNS 3000" are timeout messages from Apple indicating that the device could not connect to Apple's APNS servers. This is most common when:

* Testing on APNS development environments
* Using multiple push notification dependencies or native iOS push APIs alongside OneSignal
* A temporary connectivity issue — this often self-resolves the next time the user starts a new session (app in background for 30+ seconds, then reopened)

**Steps to resolve:**

1. Remove any other push notification dependencies or native iOS push APIs and use only OneSignal. Once the error resolves, you can re-add the other code. Contact `support@onesignal.com` for best practices on coexistence.
2. Check the [debug log from the device](./capturing-a-debug-log) for more details.
3. If the error persists, [contact support](#troubleshooting-steps).

If you are using Capacitor, add this configuration to let OneSignal handle push notifications. This configuration will resolve the issue.

<CodeGroup>
  ```json json theme={null}
  {
    "ios": {
      "handleApplicationNotifications": false
    }
  }
  ```

  ```typescript capacitor.config.ts theme={null}
  const config: CapacitorConfig = {
    // ... additional configuration

    ios: {
      // ... additional configuration
      handleApplicationNotifications: false
    }
  };
  ```

</CodeGroup>

### App not opening when force-closed and clicking a notification

Make sure you are not testing on a `Debug` build. For example, on Flutter Apps, you can either:

* Use a release build via Flutter e.g. `flutter run --release` (requires a physical device)
* Update the Xcode scheme to be `Release` not `Debug`

***

## Related pages

<Columns cols={2}>
  <Card title="Mobile SDK setup" icon="wrench" href="./mobile-sdk-setup">
    Setup instructions for all supported mobile and cross-platform SDKs.
  </Card>

  <Card title="Capturing a debug log" icon="bug" href="./capturing-a-debug-log">
    How to capture SDK logs for troubleshooting.
  </Card>

  <Card title="Web Push troubleshooting" icon="globe" href="./troubleshooting-web-push">
    Troubleshoot web push notification issues.
  </Card>

  <Card title="Mobile SDK reference" icon="book" href="./mobile-sdk-reference">
    Full API reference for the OneSignal Mobile SDKs.
  </Card>
</Columns>

***

## FAQ

### What happens if I change my OneSignal App ID in my app?

Changing the OneSignal App ID in your app's initialization code will create a brand new user and push subscription under the new App ID when the user updates and opens the app to the latest version.

If your iOS bundle ID and/or Android package ID are the same, then the device will continue with the same push subscription status. The user data will be brand new i.e. you will need to add back your aliases, tags, email address, phone number on the new record.

If the iOS bundle ID or Android package ID are different, then this is a brand new app and should have different push certs/keys.

### Can OneSignal send push notifications in an on-premise closed network?

This can work as long as the computers on your closed network have access to the push gateway servers that you want to support:

* [https://support.apple.com/en-us/HT203609](https://support.apple.com/en-us/HT203609)
* [https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall](https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall)

If the network is completely disconnected from the Internet, push notifications cannot be delivered via the standard OS/browser services, which is what we support.

***

Built with [Mintlify](https://mintlify.com).
