# Source: https://firebase.google.com/docs/cloud-messaging/android/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
Android client apps so that you can reliably send messages.

FCM clients require devices running Android 6.0 or
higher that also have the Google Play Store app installed, or an emulator
running Android 6.0 with Google APIs.
Note that you are not limited to deploying your Android apps through
Google Play Store.

## Setup the SDK

If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

For an optimal experience with FCM, we strongly recommend
[enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga) in your
project. Google Analytics is a requirement for FCM's
[message delivery reporting](https://firebase.google.com/docs/cloud-messaging/understand-delivery).

## Edit your app manifest

Add the following to your app's manifest:

- A service that extends `FirebaseMessagingService`. This is required if you want to do any message handling beyond receiving notifications on apps in the background. To receive notifications in foreground apps, to receive data payload, and more, you must extend this service.

```
<service
    android:name=".java.MyFirebaseMessagingService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>https://github.com/firebase/quickstart-android/blob/519fa2686c3eb45309c18a11db27981ce55f6535/messaging/app/src/main/AndroidManifest.xml#L50-L56
```
- (Optional) Within the application component, metadata elements to set a default notification icon and color. Android uses these values whenever incoming messages don't explicitly set icon or color.

```
<!-- Set custom default icon. This is used when no icon is set for incoming notification messages.
     See README(https://goo.gl/l4GJaQ) for more. -->
<meta-data
    android:name="com.google.firebase.messaging.default_notification_icon"
    android:resource="@drawable/ic_stat_ic_notification" />
<!-- Set color used with incoming notification messages. This is used when no color is set for the incoming
     notification message. See README(https://goo.gl/6BKBk7) for more. -->
<meta-data
    android:name="com.google.firebase.messaging.default_notification_color"
    android:resource="@color/colorAccent" />
```
- (Optional) From Android 8.0 (API level 26) and higher, [notification channels](https://developer.android.com/guide/topics/ui/notifiers/notifications.html#ManageChannels) are supported and recommended. FCM provides a default notification channel with basic settings. If you prefer to [create](https://developer.android.com/guide/topics/ui/notifiers/notifications.html#CreateChannel) and use your own default channel, set `default_notification_channel_id` to the ID of your notification channel object as shown; FCM will use this value whenever incoming messages don't explicitly set a notification channel. To learn more, see [Manage notification channels](https://developer.android.com/guide/topics/ui/notifiers/notifications.html#ManageChannels).

```
<meta-data
    android:name="com.google.firebase.messaging.default_notification_channel_id"
    android:value="@string/default_notification_channel_id" />
```

## Request runtime notification permission on Android 13+

Android 13 introduces a new runtime permission for showing notifications. This
affects all apps running on Android 13 or higher that use FCM
notifications.

By default, the FCM SDK (version 23.0.6 or higher) includes the
[`POST_NOTIFICATIONS`](https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS)
permission defined in the manifest.
However, your app will also need to request the runtime version of this
permission using the constant, `android.permission.POST_NOTIFICATIONS`.
Your app won't be allowed to show notifications until
the user has granted this permission.

To request the new runtime permission:

### Kotlin

```kotlin
// Declare the launcher at the top of your Activity/Fragment:
private val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission(),
) { isGranted: Boolean ->
    if (isGranted) {
        // FCM SDK (and your app) can post notifications.
    } else {
        // TODO: Inform user that that your app will not show notifications.
    }
}

private fun askNotificationPermission() {
    // This is only necessary for API level >= 33 (TIRAMISU)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) ==
            PackageManager.PERMISSION_GRANTED
        ) {
            // FCM SDK (and your app) can post notifications.
        } else if (shouldShowRequestPermissionRationale(Manifest.permission.POST_NOTIFICATIONS)) {
            // TODO: display an educational UI explaining to the user the features that will be enabled
            //       by them granting the POST_NOTIFICATION permission. This UI should provide the user
            //       "OK" and "No thanks" buttons. If the user selects "OK," directly request the permission.
            //       If the user selects "No thanks," allow the user to continue without notifications.
        } else {
            // Directly ask for the permission
            requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
        }
    }
}
```

### Java

```java
// Declare the launcher at the top of your Activity/Fragment:
private final ActivityResultLauncher<String> requestPermissionLauncher =
        registerForActivityResult(new ActivityResultContracts.RequestPermission(), isGranted -> {
            if (isGranted) {
                // FCM SDK (and your app) can post notifications.
            } else {
                // TODO: Inform user that that your app will not show notifications.
            }
        });

private void askNotificationPermission() {
    // This is only necessary for API level >= 33 (TIRAMISU)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) ==
                PackageManager.PERMISSION_GRANTED) {
            // FCM SDK (and your app) can post notifications.
        } else if (shouldShowRequestPermissionRationale(Manifest.permission.POST_NOTIFICATIONS)) {
            // TODO: display an educational UI explaining to the user the features that will be enabled
            //       by them granting the POST_NOTIFICATION permission. This UI should provide the user
            //       "OK" and "No thanks" buttons. If the user selects "OK," directly request the permission.
            //       If the user selects "No thanks," allow the user to continue without notifications.
        } else {
            // Directly ask for the permission
            requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS);
        }
    }
}
```

Generally, you should display a UI explaining to the user the
features that will be enabled if they grant permissions for the
app to post notifications. This UI should provide the user options to
agree or deny, such as **OK** and **No thanks**
buttons. If the user selects **OK** , directly request the permission.
If the user selects **No thanks**, allow
the user to continue without notifications.

See [Notification runtime permission](https://developer.android.com/about/versions/13/changes/notification-permission#new-apps)
for more best practices on when your app should request the
`POST_NOTIFICATIONS` permission from the user.

### Notification permissions for apps targeting Android 12L (API level 32) or lower

Android automatically asks the user for permission the first time your app
creates a notification channel, as long as the app is in the foreground.
However, there are important caveats regarding the timing of channel creation
and permission requests:

- If your app creates its first notification channel when it is running in the background, which the FCM SDK does when receiving an FCM notification, Android won't allow the notification to be displayed and won't prompt the user for the notification permission until the next time your app is opened. This means that any notifications received before your app is opened and the user accepts the permission will be lost.
- We strongly recommend that you update your app to target Android 13+ to take advantage of the platform's APIs to request permission. If that isn't possible, your app should create notification channels before you send any notifications to the app in order to trigger the notification permission dialog and make sure no notifications are lost. See [notification permission best practices](https://developer.android.com/about/versions/13/changes/notification-permission#wait-to-show-prompt) for more information.

#### Optional: remove `POST_NOTIFICATIONS` permission

By default, the FCM SDK includes the `POST_NOTIFICATIONS` permission.
If your app does not use notification messages (whether through FCM
notifications, through another SDK, or directly posted by your app) and you
don't want your app to include the permission, you can remove it using the
[manifest merger's](https://developer.android.com/studio/build/manage-manifests)
`remove` marker. Keep in mind that removing this permission prevents the display
of all notifications, not just FCM notifications. Add the following to
your app's manifest file:

    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" tools:node="remove"/>

## Access the FCM registration token

> [!TIP]
> **Tip:** See [Best practices for FCM registration token
> management](https://firebase.google.com/docs/cloud-messaging/manage-tokens) for tips on managing tokens.


On initial startup of your app, the FCM SDK generates a registration
token for the client app instance. If you want to target single app instances or
create device groups, you'll need to access this token by extending
[`FirebaseMessagingService`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService) and overriding `onNewToken`. Because the
token could be rotated after initial
startup, you are strongly recommended to retrieve the latest updated registration
token.

The registration token may change when:

- The app is restored on a new device
- The user uninstalls/reinstall the app
- The user clears app data.

<br />

> [!CAUTION]
> Apps still using deprecated Instance ID APIs for token management should update all token logic to use the FCM APIs described here.

### Retrieve the current registration token

When you need to retrieve the current token, call
[`FirebaseMessaging.getInstance().getToken()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()):

### Kotlin

```kotlin
FirebaseMessaging.getInstance().token.addOnCompleteListener(OnCompleteListener { task ->
    if (!task.isSuccessful) {
        Log.w(TAG, "Fetching FCM registration token failed", task.exception)
        return@OnCompleteListener
    }

    // Get new FCM registration token
    val token = task.result

    // Log and toast
    val msg = getString(R.string.msg_token_fmt, token)
    Log.d(TAG, msg)
    Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
})
```

### Java

```java
FirebaseMessaging.getInstance().getToken()
    .addOnCompleteListener(new OnCompleteListener<String>() {
        @Override
        public void onComplete(@NonNull Task<String> task) {
          if (!task.isSuccessful()) {
            Log.w(TAG, "Fetching FCM registration token failed", task.getException());
            return;
          }

          // Get new FCM registration token
          String token = task.getResult();

          // Log and toast
          String msg = getString(R.string.msg_token_fmt, token);
          Log.d(TAG, msg);
          Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
        }
    });
```

### Monitor token generation

The `onNewToken` callback fires whenever a new token is generated.

### Kotlin

```kotlin
/**
 * Called if the FCM registration token is updated. This may occur if the security of
 * the previous token had been compromised. Note that this is called when the
 * FCM registration token is initially generated so this is where you would retrieve the token.
 */
override fun onNewToken(token: String) {
    Log.d(TAG, "Refreshed token: $token")

    // If you want to send messages to this application instance or
    // manage this apps subscriptions on the server side, send the
    // FCM registration token to your app server.
    sendRegistrationToServer(token)
}
```

### Java

```java
/**
 * There are two scenarios when onNewToken is called:
 * 1) When a new token is generated on initial app startup
 * 2) Whenever an existing token is changed
 * Under #2, there are three scenarios when the existing token is changed:
 * A) App is restored to a new device
 * B) User uninstalls/reinstalls the app
 * C) User clears app data
 */
@Override
public void onNewToken(@NonNull String token) {
    Log.d(TAG, "Refreshed token: " + token);

    // If you want to send messages to this application instance or
    // manage this apps subscriptions on the server side, send the
    // FCM registration token to your app server.
    sendRegistrationToServer(token);
}
```

After you've obtained the token, you can send it to your app server and store
it using your preferred method.

## Check for Google Play services

Apps that rely on the Play Services SDK should always check the device for a
compatible Google Play services APK before accessing Google Play services
features. To learn more, see[set up Google Play
services](https://developers.google.com/android/guides/setup). It is recommended to do
this in two places: in the main activity's `onCreate()` method, and in its
`onResume()` method. The check in `onCreate()` makes sure that the app can't be
used without a successful check. The check in `onResume()` makes sure that if
the user returns to the running app through some other means, such as through
the back button, the check is still performed.

If the device doesn't have a compatible version of Google Play services, your
app can call
[`GoogleApiAvailability.makeGooglePlayServicesAvailable()`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability.html#public-methods)
to allow users to download Google Play services from the Play Store.

## Prevent auto initialization

When an FCM registration token is generated, the library uploads the
identifier and configuration data to Firebase. If you prefer to prevent token
auto generation, disable Analytics collection and FCM auto initialization (you
must disable both) by adding these metadata values to your
`AndroidManifest.xml`:

```
<meta-data
    android:name="firebase_messaging_auto_init_enabled"
    android:value="false" />
<meta-data
    android:name="firebase_analytics_collection_enabled"
    android:value="false" />https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/messaging/app/src/main/AndroidManifest.xml#L12-L17
```

To re-enable FCM auto-init, make a runtime call:

### Kotlin

```kotlin
Firebase.messaging.isAutoInitEnabled = truehttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/messaging/app/src/main/java/com/google/firebase/example/messaging/kotlin/MainActivity.kt#L42-L42
```

### Java

```java
FirebaseMessaging.getInstance().setAutoInitEnabled(true);
```

To re-enable Analytics collection, call the
[`setAnalyticsCollectionEnabled()`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean))
method of the `FirebaseAnalytics` class. For example:

    setAnalyticsCollectionEnabled(true);

These values persist across app restarts once set.

## Send a notification message

To make sure that your Android client is setup correctly, you can send a test
notification message using the following instructions:

1. Install and run the app on the target device.
2. Make sure the app is in the background on the device.
3. In the Firebase console, open the [**Messaging**](https://console.firebase.google.com/project/_/notification) page.
4. If this is your first message, select **Create your first campaign** , **Firebase Notification messages** and then **Create**.
5. Otherwise, on the **Campaigns** tab, select **New campaign** and then **Notifications**.
6. Enter the message text. All other fields are optional.
7. Select **Send test message** from the right pane.
8. In the field labeled **Add an FCM registration token**, enter the registration token you obtained in a previous section of this guide.
9. Select **Test**.

The targeted client device, with the app in the background, should receive the
notification.

For more information into message delivery to your app, see the [FCM
reporting
dashboard](https://console.firebase.google.com/project/_/notification/reporting),
which records the number of messages sent and opened on Apple and Android
devices, along with data for **impressions** (notifications seen by users) for
Android apps.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for Android:

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in an Android app](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=android)
- [Send messages to topics](https://firebase.google.com/docs/cloud-messaging/topic-messaging)