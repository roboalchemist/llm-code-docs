# Source: https://firebase.google.com/docs/cloud-messaging/customize-messages/android-direct-boot.md.txt

If you want to send FCM messages to apps before the device is
unlocked, you can enable direct boot mode. For example, if you want your users
of your app to receive alarm notifications even on a locked device.

When building out this use case, observe the general [best practices and
restrictions](https://developer.android.com/training/articles/direct-boot) for
direct boot mode. It's important to consider the *visibility* of direct
boot-enabled messages. Any user with access to the device can view these
messages without entering user credentials.

## Prerequisites

- The device must be set up for direct boot mode.
- The device must have a recent version of Google Play services installed (19.0.54 or later).
- The app must be using the FCM SDK (`com.google.firebase:firebase-messaging`) to receive FCM messages.

## Enable direct boot mode message handling in your app

1. In the app-level Gradle file, add a dependency on the FCM direct
   boot support library:

       implementation 'com.google.firebase:firebase-messaging-directboot:20.2.0'

2. Make the app's `FirebaseMessagingService` direct boot aware by adding the
   `android:directBootAware="true"` attribute in the app manifest:

       <service
           android:name=".java.MyFirebaseMessagingService"
           android:exported="false"
           android:directBootAware="true">
           <intent-filter>
               <action android:name="com.google.firebase.MESSAGING_EVENT" />
           </intent-filter>
       </service>

It is important to ensure that this `FirebaseMessagingService` can run in direct
boot mode. You can check using the following requirements:

- The service shouldn't access credential protected storage while running in direct boot mode.
- The service shouldn't attempt to use components, such as `Activities`, `BroadcastReceivers`, or other `Services` that are not marked as direct boot aware while running in direct boot mode.
- Any libraries that the service uses must also not access credential protected storage nor call non-directBootAware components while running in direct boot mode. This means that any libraries the app uses that are called from the service either will need to be direct boot aware, or the app will need to check if it's running in direct boot mode and not call them in that mode. For example, Firebase SDKs work with direct boot (they can be included in an app without crashing it in direct boot mode), but many Firebase APIs don't support being called in direct boot mode.
- If the app is using a custom `Application`, the `Application` will also need to be direct boot aware (no access to credential protected storage in direct boot mode).

## Send direct boot-enabled messages

You can send messages to devices in direct boot mode using the
[HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send).

> [!CAUTION]
> **Caution:** It's important to consider the *visibility* of direct boot- enabled messages; any user with access to the device can view these messages without entering user credentials.

The message request must include the key `"direct_boot_ok": true` in the
`AndroidConfig` options of the request body. For example:

    https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send
    Content-Type:application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA

    {
      "message":{
        "token" : "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
        "data": {
          "score": "5x1",
          "time": "15:10"
        },
        "android": {
          "direct_boot_ok": true,
        },
    }