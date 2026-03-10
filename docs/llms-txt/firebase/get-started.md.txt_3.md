# Source: https://firebase.google.com/docs/cloud-messaging/flutter/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
Flutter client apps so that you can reliably send messages.

Depending on the platform you're targeting, there are some additional required
setup steps that you'll need to take.

## iOS+

<br />

### Enable app capabilities in XCode

<br />

Before your application can start to receive messages, you must enable push
notifications and background modes in your Xcode project.

1. Open your Xcode project workspace (\`ios/Runner.xcworkspace\`).
2. [Enable push
   notifications](https://help.apple.com/xcode/mac/current/#/devdfd3d04a1).
3. Enable the **Background fetch** and the **Remote notifications** [background
   execution modes](https://developer.apple.com/documentation/xcode/configuring-background-execution-modes).

<br />

<br />

<br />

### Upload your APNs
authentication key

<br />

Before you use FCM, upload your APNs authentication key to Firebase console. If you don't
already have an APNs authentication key, create one in the [Apple Developer
Member Center](https://developer.apple.com/membercenter/index.action).

1. Inside your project in the Firebase console, select the gear icon, select **Project Settings** , and then select the **Cloud Messaging** tab.
2. Select the **Upload** button to upload your development authentication key, or production authetication key, or both. At least one is required.
3. For each authentication key, select the .p8 file, and provide the key ID and your Apple team ID. Select **Save**.

<br />

<br />

#### Method swizzling

To use the FCM Flutter plugin on Apple devices, method swizzling is
required. Without it, key Firebase features such as FCM token handling
won't function properly.

## Android

### Google Play services

FCM clients require devices running Android 4.4 or higher that also
have Google
Play services installed, or an emulator running Android 4.4 with Google APIs.
Note that you are not limited to deploying your Android apps through Google Play
Store.

Apps that rely on the Play Services SDK should always check the device for a
compatible Google Play services APK before accessing Google Play services
features. It is recommended to do this in two places: in the main activity's
`onCreate()` method, and in its `onResume()` method. The check in `onCreate()`
makes sure that the app can't be used without a successful check. The check in
`onResume()` makes sure that if the user returns to the running app through some
other means, such as through the back button, the check is still performed.

If the device doesn't have a compatible version of Google Play services, your
app can call
[`GoogleApiAvailability.makeGooglePlayServicesAvailable()`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability.html#public-methods)
to allow users to download Google Play services from the Play Store.

## Web

### Configure Web Credentials with FCM

The FCM Web interface uses Web credentials called Voluntary
Application Server Identification, or "VAPID" keys, to authorize send requests
to supported web push services. To subscribe your app to push notifications, you
need to associate a pair of keys with your Firebase project. You can either
generate a new key pair or import your existing key pair through the
Firebase console.

<br />

### Generate a new key pair

<br />

1. Open the [Cloud
   Messaging](https://console.firebase.google.com/project/_/settings/cloudmessaging/) tab of the Firebase console **Settings** pane and go to the **Web configuration** section.
2. In the **Web Push certificates** tab, click **Generate Key Pair**. The console displays a notice that the key pair was generated, and displays the public key string and date added.

<br />

<br />

<br />

### Import an existing key pair

<br />

If you have an existing key pair you are already using with your web app, you
can import it to FCM so that you can reach your existing web app
instances through FCM APIs. To import keys, you must have
owner-level access to the Firebase project. Import your existing public and
private key in base64 URL safe encoded form:

1. Open the [Cloud
   Messaging](https://console.firebase.google.com/project/_/settings/cloudmessaging/) tab of the Firebase console **Settings** pane and go to the **Web configuration** section.
2. In the **Web Push certificates** tab, select **import
   an existing key pair**.
3. In the **Import a key pair** dialog, provide your public and private keys in the corresponding fields and click **Import**. The console displays the public key string and date added.

For more information about the format of the keys and how to generate them,
see [Application server keys](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol#application_server_keys).

<br />

<br />

## Install the FCM plugin

1. [Install and initialize the Firebase plugins for Flutter](https://firebase.google.com/docs/flutter/setup)
   if you haven't already done so.

2. From the root of your Flutter project, run the following command to install
   the plugin:

       flutter pub add firebase_messaging

3. Once complete, rebuild your Flutter application:

       flutter run

## Access the registration token

To send a message to a specific device, you need to know the device
registration token. To retrieve the registration token for an app instance, call
`getToken()`. If notification permission has not been granted, this method will
ask the user for notification permissions. Otherwise, it returns a token or
rejects the future due to an error.

> [!WARNING]
> **Warning:** In iOS SDK 10.4.0 and higher, it is required that the APNs token is available before making API requests. The APNs token is not guaranteed to have been received before making FCM plugin API requests.

    // You may set the permission requests to "provisional" which allows the user to choose what type
    // of notifications they would like to receive once the user receives a notification.
    final notificationSettings = await FirebaseMessaging.instance.requestPermission(provisional: true);

    // For apple platforms, make sure the APNS token is available before making any FCM plugin API calls
    final apnsToken = await FirebaseMessaging.instance.getAPNSToken();
    if (apnsToken != null) {
     // APNS token is available, make FCM plugin API requests...
    }

On web platforms, pass your VAPID public key to `getToken()`:

    final fcmToken = await FirebaseMessaging.instance.getToken(vapidKey: "BKagOny0KF_2pCJQ3m....moL0ewzQ8rZu");

To be notified whenever the token is updated, subscribe to the `onTokenRefresh`
stream:

    FirebaseMessaging.instance.onTokenRefresh
        .listen((fcmToken) {
          // TODO: If necessary send token to application server.

          // Note: This callback is fired at each app startup and whenever a new
          // token is generated.
        })
        .onError((err) {
          // Error getting token.
        });

## Prevent auto initialization

When an FCM registration token is generated, the library uploads
the identifier and configuration data to Firebase. If you prefer to prevent
token auto generation, disable auto-initialization at build time.

### iOS

On iOS, add a metadata value to your `Info.plist`:

    FirebaseMessagingAutoInitEnabled = NO

### Android

On Android, disable Analytics collection and FCM auto initialization (you must
disable both) by adding these metadata values to your `AndroidManifest.xml`:

    <meta-data
        android:name="firebase_messaging_auto_init_enabled"
        android:value="false" />
    <meta-data
        android:name="firebase_analytics_collection_enabled"
        android:value="false" />

### Re-enable FCM auto-init at runtime

To enable auto-init for a specific app instance, call `setAutoInitEnabled()`:

    await FirebaseMessaging.instance.setAutoInitEnabled(true);

This value persists across app restarts once set.

## Send a test notification message

1. Install and run the app on the target device. On Apple devices, you'll need to accept the request for permission to receive remote notifications.
2. Make sure the app is in the background on the device.
3. In the Firebase console, open the Messaging page.
4. If this is your first message, select **Create your first campaign** .
   1. Select **Firebase Notification messages** and select **Create**.
5. Otherwise, on the **Campaigns** tab, select **New campaign** and then **Notifications**.
6. Enter the message text.
7. Select **Send test message** from the right pane.
8. In the field labeled **Add an FCM registration token**, enter your registration token.
9. Select **Test**.

After you select **Test**, the targeted client device, with the app in the
background, should receive the notification.

For insight into message delivery to your app, see the FCM reporting
dashboard, which records the number of messages sent and opened on Apple and
Android devices, along with impression data for Android apps.

## Handling interaction

When users tap a notification, the default behavior on both Android and iOS is
to open the application. If the application is terminated, it will be started,
and if it is in the background, it will be brought to the foreground.

Depending on the content of a notification, you may want to handle the user's
interaction when the application opens. For example, if a new chat message is
sent using a notification and the user selects it, you may want to open the
specific conversation when the application opens.

The `firebase-messaging` package provides two ways to handle this interaction:

1. `getInitialMessage():` If the application is opened from a terminated state, this method returns a `Future` containing a `RemoteMessage`. Once consumed, the `RemoteMessage` will be removed.
2. `onMessageOpenedApp`: A`Stream` which posts a `RemoteMessage` when the application is opened from a background state.

To make sure your users have a smooth experience, you should handle both
scenarios. The following code example outlines how this can be achieved:

```
class Application extends StatefulWidget {
  @override
  State createState() => _Application();
}

class _Application extends State {
  // In this example, suppose that all messages contain a data field with the key 'type'.
  Future setupInteractedMessage() async {
    // Get any messages which caused the application to open from
    // a terminated state.
    RemoteMessage? initialMessage =
        await FirebaseMessaging.instance.getInitialMessage();

    // If the message also contains a data property with a "type" of "chat",
    // navigate to a chat screen
    if (initialMessage != null) {
      _handleMessage(initialMessage);
    }

    // Also handle any interaction when the app is in the background using a
    // Stream listener
    FirebaseMessaging.onMessageOpenedApp.listen(_handleMessage);
  }

  void _handleMessage(RemoteMessage message) {
    if (message.data['type'] == 'chat') {
      Navigator.pushNamed(context, '/chat',
        arguments: ChatArguments(message),
      );
    }
  }

  @override
  void initState() {
    super.initState();

    // Run code required to handle interacted messages in an async function
    // as initState() must not be async
    setupInteractedMessage();
  }

  @override
  Widget build(BuildContext context) {
    return Text("...");
  }
}
```

How you handle interaction depends on your setup. The previously shown example
is a basic example of using a `StatefulWidget`.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for Flutter:

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in a Flutter app](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=flutter)
- [Send messages to topics](https://firebase.google.com/docs/cloud-messaging/topic-messaging)