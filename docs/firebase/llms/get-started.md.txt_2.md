# Source: https://firebase.google.com/docs/cloud-messaging/cpp/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
C++ client apps so that you can reliably send messages.

To write your cross-platform Firebase Cloud Messaging client app with C++, use the
[Firebase Cloud Messaging](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging) API.
The C++ SDK works for both Android and Apple platforms, with some additional
setup required for each platform. To learn more about how the C++ SDK for iOS and
Android works with FCM, see [Understand Firebase for
C++](https://firebase.google.com/docs/cpp/learn-more).

## Set up Firebase and the FCM SDK

### Android

1. If you haven't already,
   [add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup?platform=android).

   - In the linked setup instructions, review the device and app
     requirements for using the Firebase C++ SDK, including the
     recommendation to use CMake to build your app.

   - In your project-level `build.gradle` file, make sure to include
     Google's Maven repository in both your `buildscript` and
     `allprojects` sections.

   > [!IMPORTANT]
   > **Important:** Make sure to add the **`firebase_messaging`** library to your `CMakeLists.txt` file.

2. Create a Firebase App object, passing in the JNI environment and
   Activity:

   ```c++
   app = ::firebase::App::Create(::firebase::AppOptions(), jni_env, activity);
   ```

   <br />

3. Define a class that implements the `firebase::messaging::Listener`
   interface.

4. Initialize FCM, passing in the App and a constructed Listener:

   ```c++
   ::firebase::messaging::Initialize(app, listener);
   ```

   <br />

5. Apps that rely on the Google Play services SDK should check the device
   for a compatible Google Play services APK before accessing the features.
   To learn more, refer to
   [Check for Google Play services APK](https://firebase.google.com/docs/cloud-messaging/android/client#sample-play).

### iOS+

1. If you haven't already, [add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup?platform=ios). Then, to set up your project for FCM:
   1. In your project's Podfile, add the FCM dependency:

      ```c++
      pod 'FirebaseMessaging'
      ```
   2. Drag the `firebase.framework` and `firebase_messaging.framework` frameworks into your Xcode project from the [Firebase C++ SDK](https://firebase.google.com/download/cpp).
2.
   Upload your APNs authentication key to Firebase.
   If you don't already have an APNs authentication key, make sure to create one in the
   [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action).

   1.
      Inside your project in the Firebase console, select the
      gear icon, select
      **Project Settings** , and then select the
      **Cloud Messaging** tab.

   2.
      In **APNs authentication key** under **iOS app configuration** ,
      click the **Upload** button to upload your development authentication key, or
      production authentication key, or both. At least one is required.

   3.
      Browse to the location where you saved your key, select it, and click
      **Open** . Add the key ID for the key (available in the
      [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action)) and click
      **Upload**.

3. Configure your Xcode project to enable Push Notifications:

   1. Select the project from the **Navigator area**.
   2. Select the project target from the **Editor area**.
   3. Select the **General** tab from the **Editor area**.

      1. Scroll to **Linked Frameworks and Libraries** , then click the **+** button to add frameworks.
      2. In the window that appears, scroll to
         **UserNotifications.framework** , click the entry, then click
         **Add**.

         This framework only appears in Xcode v8 and later and is
         required by this library.
   4. Select the **Capabilities** tab from the **Editor area**.

      1. Switch **Push Notifications** to **On**.
      2. Scroll to **Background Modes** , then switch it to **On**.
      3. Select **Remote notifications** under **Background Modes**.
4. Create a Firebase App object:

   ```c++
   app = ::firebase::App::Create(::firebase::AppOptions());
   ```

   <br />

5. Define a class that implements the `firebase::messaging::Listener`
   interface.

6. Initialize Firebase Cloud Messaging, passing in the App and a constructed
   Listener:

   ```c++
   ::firebase::messaging::Initialize(app, listener);
   ```

   <br />

## Access the FCM registration token

Upon initializing the Firebase Cloud Messaging library, a registration token is
requested for the client app instance. The app will receive the token with the
`OnTokenReceived` callback, which should be defined in the class that implements
`firebase::messaging::Listener`.

If you want to target that specific app instance, you'll need access to this token.

## Note about message delivery on Android

When the app is not running at all and a user taps on a notification,
the message is not, by default, routed through FCM's built in
callbacks. In this case, message payloads are received through an `Intent`
used to start the application. To have FCM forward these incoming
messages to the C++ library callback, you need to override the method
`onNewIntent` in your Activity and pass the `Intent` to the
`MessageForwardingService`.

```c++
import com.google.firebase.messaging.MessageForwardingService;

class MyActivity extends Activity {
  private static final String TAG = "MyActvity";

  @Override
  protected void onNewIntent(Intent intent) {
    Log.d(TAG, "A message was sent to this app while it was in the background.");
    Intent message = new Intent(this, MessageForwardingService.class);
    message.setAction(MessageForwardingService.ACTION_REMOTE_INTENT);
    message.putExtras(intent);
    message.setData(intent.getData());
    // For older versions of Firebase C++ SDK (< 7.1.0), use `startService`.
    // startService(message);
    MessageForwardingService.enqueueWork(this, message);
  }
}
```

Messages received while the app is in the background have the content of
their notification field used to populate the system tray notification, but
that notification content won't be communicated to FCM. That is,
`Message::notification` will be a null.

In summary:

| App state | Notification | Data | Both |
|---|---|---|---|
| Foreground | `OnMessageReceived` | `OnMessageReceived` | `OnMessageReceived` |
| Background | System tray | `OnMessageReceived` | Notification: system tray Data: in extras of the intent. |

## Custom message handling on Android

By default, notifications sent to the app are passed to
`::firebase::messaging::Listener::OnMessageReceived`, but in some cases you may
want to override the default behavior. To do this on Android you will need to
write custom classes that extend
`com.google.firebase.messaging.cpp.ListenerService` as well as update your
project's `AndroidManifest.xml`.

### Override `ListenerService` methods

The `ListenerService` is the Java class that intercepts incoming messages sent to
the app and routes them to the C++ library. When the app is in the foreground
(or when the app is the background and it receives a data-only payload),
messages will pass through one of the callbacks provided on this class. To add
custom behavior to the message handling, you will need to extend FCM's
default `ListenerService`:

```c++
import com.google.firebase.messaging.cpp.ListenerService;

class MyListenerService extends ListenerService {
```

By overriding the method `ListenerService.onMessageReceived`, you can
perform actions based on the received
[RemoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage)
object and get the message data:

```c++
@Override
public void onMessageReceived(RemoteMessage message) {
  Log.d(TAG, "A message has been received.");
  // Do additional logic...
  super.onMessageReceived(message);
}
```

`ListenerService` also has a few other methods that are used less frequently.
These can be overridden as well, for more information see the
[FirebaseMessagingService](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService)
reference.

```c++
@Override
public void onDeletedMessages() {
  Log.d(TAG, "Messages have been deleted on the server.");
  // Do additional logic...
  super.onDeletedMessages();
}

@Override
public void onMessageSent(String messageId) {
  Log.d(TAG, "An outgoing message has been sent.");
  // Do additional logic...
  super.onMessageSent(messageId);
}

@Override
public void onSendError(String messageId, Exception exception) {
  Log.d(TAG, "An outgoing message encountered an error.");
  // Do additional logic...
  super.onSendError(messageId, exception);
}
```

### Update `AndroidManifest.xml`

Once your custom classes have been written, they must be included in the
`AndroidManifest.xml` to take effect. Make sure that the manifest includes the
merge tools by declaring the appropriate attribute inside the `<manifest>` tag,
like so:

```c++
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.google.firebase.messaging.cpp.samples"
    xmlns:tools="http://schemas.android.com/tools">
```

In the `firebase_messaging_cpp.aar` archive there is an `AndroidManifest.xml`
file which declares FCM's default `ListenerService`. This manifest
is normally merged with the project specific manifest which is how the
`ListenerService` is able to run. This `ListenerService` needs to replaced with
the custom listener service. That is accomplished by removing the default
`ListenerService` and adding the custom Service, which can be done with the
following lines your projects `AndroidManifest.xml` file:

```c++
<service android:name="com.google.firebase.messaging.cpp.ListenerService"
         tools:node="remove" />
```

```c++
<service android:name="com.google.firebase.messaging.cpp.samples.MyListenerService"
         android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT"/>
  </intent-filter>
</service>
```

New versions of Firebase C++ SDK (7.1.0 onwards) use `JobIntentService` which requires
additional modifications in `AndroidManifest.xml` file.

```c++
<service android:name="com.google.firebase.messaging.MessageForwardingService"
     android:permission="android.permission.BIND_JOB_SERVICE"
     android:exported="false" >
</service>
```

## Prevent auto initialization

FCM generates a registration token for app instance targeting.
When a token is generated, the library uploads the
identifier and configuration data to Firebase. If you want to get an explicit
opt-in before using the token, you can prevent generation at configure time by
disabling FCM (and on Android, Analytics). To do this, add a metadata value to
your `Info.plist` (not your `GoogleService-Info.plist`) on Apple platforms,
or your `AndroidManifest.xml` on Android:

#### Android

```c++
<?xml version="1.0" encoding="utf-8"?>
<application>
  <meta-data android:name="firebase_messaging_auto_init_enabled"
             android:value="false" />
  <meta-data android:name="firebase_analytics_collection_enabled"
             android:value="false" />
</application>
```

#### Swift

```swift
FirebaseMessagingAutoInitEnabled = NO
```

To re-enable FCM, you can make a runtime call:

```c++
::firebase::messaging::SetTokenRegistrationOnInitEnabled(true);
```

This value persists across app restarts once set.

## Messages with deep links on Android

FCM allows messages to be sent containing a deep link into your app.
To receive messages that contain a deep link, you must add a new intent filter
to the activity that handles deep links for your app. The intent filter should
catch deep links of your domain. If your messages don't contain a deep link,
this configuration is not necessary. In AndroidManifest.xml:

```c++
<intent-filter>
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:host="CHANGE_THIS_DOMAIN.example.com" android:scheme="http"/>
  <data android:host="CHANGE_THIS_DOMAIN.example.com" android:scheme="https"/>
</intent-filter>
```

It is also possible to specify a wildcard to make the intent filter more
flexible. For example:

```c++
<intent-filter>
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:host="*.example.com" android:scheme="http"/>
  <data android:host="*.example.com" android:scheme="https"/>
</intent-filter>
```

When users tap a notification containing a link to the scheme and host you
specify, your app will start the activity with this intent filter to handle the
link.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for C++:

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in a C++ app](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=cpp)
- [Send messages to topics](https://firebase.google.com/docs/cloud-messaging/topic-messaging)