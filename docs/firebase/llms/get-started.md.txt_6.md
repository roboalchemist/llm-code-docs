# Source: https://firebase.google.com/docs/cloud-messaging/unity/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
Unity client apps so that you can reliably send messages.

To write your cross-platform Firebase Cloud Messaging client app with Unity, use
the [Firebase Cloud Messaging](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging) API. The Unity SDK works for
both Android and Apple, with some additional setup required for each platform.

## Before you begin

## Prerequisites

- Install Unity 2021 LTS or later. Earlier versions may also be compatible but
  won't be actively supported.

- *(Apple platforms only)* Install the following:

  - Xcode 16.2 or higher
  - CocoaPods 1.12.0 or higher
- Make sure that your Unity project meets these requirements:

  - **For iOS** --- targets iOS 15 or higher
  - **For tvOS** - targets tvOS 15 or higher
  - **For Android** --- targets API level 23 (Marshmallow) or higher

<!-- -->

- Set up a device or use an emulator to run your Unity project.

  - **For iOS or tvOS** --- Set up a *physical device* to run your
    app, and complete these tasks:

    - Obtain an Apple Push Notification Authentication Key for your [Apple Developer account](https://developer.apple.com/account).
    - Enable Push Notifications in XCode under **App** \> **Capabilities**.
  - **For Android** ---
    [Emulators](https://developer.android.com/studio/run/managing-avds) must use an
    emulator image with Google Play.

<!-- -->

- [Sign into Firebase](https://console.firebase.google.com/) using your Google account.

If you don't already have a Unity project and just want to try out a Firebase
product, you can download one of our [quickstart samples](https://github.com/firebase/quickstart-unity).

### Step 1: Create a Firebase project

Before you can add Firebase to your Unity project, you need to create a Firebase
project to connect to your Unity project. Visit [Understand Firebase
Projects](https://firebase.google.com/docs/projects/learn-more) to learn more about Firebase projects.
**Create a Firebase project**

### New to Firebase or Cloud


Follow these steps if you're new to Firebase or Google Cloud.  

You can also follow these steps if you want to create a wholly new
Firebase project (and its underlying Google Cloud project).

1. Sign into the [Firebase console](https://console.firebase.google.com/).
2. Click the button to create a new Firebase project.
3. In the text field, enter a **project name**.

   If you're part of a Google Cloud org, you can optionally select which
   folder you create your project in.

   > [!CAUTION]
   > Your project name is used as a display name in Firebase interfaces, and Firebase auto-creates a unique project ID based on this project name. Note that you can optionally click the **Edit** icon now to set your preferred project ID, but you cannot change this ID after project creation. Learn about [how Firebase uses the
   > project ID](https://firebase.google.com/docs/projects/learn-more#project-id).

4. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
5. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
6. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

7. Click **Create project**.

Firebase creates your project, provisions some initial resources, and
enables important APIs. When the process completes, you'll be taken to the
overview page for your Firebase project in the Firebase console.

### Existing Cloud project


Follow these steps if you want to start using Firebase with an existing
Google Cloud project. Learn more about and troubleshoot
["adding
Firebase" to an existing Google Cloud project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project).

1. Sign into the [Firebase console](https://console.firebase.google.com/) with the account that gives you access to the existing Google Cloud project.
2. Click the button to create a new Firebase project.
3. At the bottom of the page, click **Add Firebase to Google Cloud project**.
4. In the text field, start entering the **project name** of the existing project, and then select the project from the displayed list.
5. Click **Open project**.
6. If prompted, review and accept the [Firebase terms](https://firebase.google.com/terms), then click **Continue**.
7. *(Optional)* Enable AI assistance in the Firebase console (called "Gemini in Firebase"), which can help you get started and streamline your development process.
8. *(Optional)* Set up Google Analytics for your project,
   which enables an optimal experience using these Firebase products:
   [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),
   [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),
   [Crashlytics](https://firebase.google.com/docs/crashlytics),
   [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and
   [Remote Config](https://firebase.google.com/docs/remote-config)
   (including
   [Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing
   [Google Analytics account](https://support.google.com/analytics/answer/1009618)
   or create a new account. If you create a new account, select your
   [Analytics reporting location](https://firebase.google.com/docs/projects/locations),
   then accept the data sharing settings and Google Analytics terms
   for your project.

   > [!NOTE]
   > You can always set up Google Analytics later in the [*Integrations* tab](https://console.firebase.google.com/project/_/settings/integrations) of your *Project settings*.

9. Click **Add Firebase**.

Firebase
[adds
Firebase to your existing project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).
When the process completes, you'll be taken to the overview page for your
Firebase project in the Firebase console.

### Step 2: Register your app with Firebase

You can register one or more apps or games to connect with your Firebase
project.

> [!CAUTION]
> If you're releasing your game on both iOS and Android, register both build targets of your Unity project *with the same Firebase project* . If you have *multiple build variants* with different iOS bundle IDs or Android app IDs defined, you must register each variant with the same Firebase project.

1. Go to the [Firebase console](https://console.firebase.google.com/).

2. In the center of the project overview page, click the **Unity** icon
   ()
   to launch the setup workflow.

   If you've already added an app to your Firebase project, click **Add app**
   to display the platform options.
3. Select which build target of your Unity project that you'd like to register,
   or you can even select to register both targets now at the same time.

   > [!NOTE]
   > **Note:** If you only register one build target of your Unity project now, you can always return to the setup workflow later to register the other build target.

4. Enter your Unity project's platform-specific ID(s).

   - **For iOS** --- Enter your Unity project's iOS ID in the
     [**iOS bundle
     ID**](https://cocoacasts.com/what-are-app-ids-and-bundle-identifiers/)
     field.

   - **For Android** --- Enter your Unity project's Android ID in the
     [**Android package
     name**](https://developer.android.com/studio/build/application-id) field.  

     The terms *package name* and *application ID* are often used
     interchangeably.

   <br />

   Where do you find your Unity project's ID?

   <br />

   > Open your Unity project in your Unity IDE, then navigate to the settings
   > section for each platform:
   > - **For iOS** --- Navigate to **Build Settings \> iOS**.
   >
   > - **For Android** --- Navigate to **Android \> Player Settings \>
   >   Other Settings**.
   >
   > Your Unity project's ID is the **Bundle Identifier** value
   > (example ID: `com.yourcompany.yourproject`).

   <br />

   <br />

   > [!CAUTION]
   > Make sure that you enter the ID that your project is actually using. The ID value is case-sensitive, and it cannot be changed for these Firebase apps after they're registered with your Firebase project.

5. *(Optional)* Enter your Unity project's platform-specific nickname(s).  

   These nicknames are internal, convenience identifiers and are only visible
   to you in the Firebase console.

6. Click **Register app**.

### Step 3: Add Firebase configuration files

1. Obtain your platform-specific Firebase configuration file(s) in the
   Firebase console setup workflow.

   > [!CAUTION]
   > If you're registering both an iOS and an Android build target of your Unity project, you'll need to download and add the config files for both platforms.

   - **For iOS** --- Click **Download GoogleService-Info.plist**.

   - **For Android** --- Click **Download google-services.json**.

   <br />

   What do you need to know about this config file?

   <br />

   > - The Firebase config file contains unique, but non-secret identifiers for
   >   your project and app. To learn more about this config file, visit
   >   [Understand Firebase
   >   Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects).
   >
   > - You can download your [Firebase config
   >   file](https://support.google.com/firebase/answer/7015592)
   >   again at any time.
   >
   > - Make sure the config file name is not appended with additional characters,
   >   like `(2)`.

   <br />

   <br />

2. Open the **Project** window of your Unity project, then move your config
   file(s) into the `Assets` folder.

3. Back in the Firebase console, in the setup workflow, click **Next**.

### Step 4: Add Firebase Unity SDKs

1. In the Firebase console, click **Download Firebase Unity SDK**, then unzip
   the SDK somewhere convenient.

   - You can download the [Firebase Unity SDK](https://firebase.google.com/download/unity) again at any time.

   - The Firebase Unity SDK is not platform-specific.

2. In your open Unity project, navigate to
   **Assets** \> **Import Package** \> **Custom Package**.

3. From the unzipped SDK, select the [supported Firebase
   products](https://firebase.google.com/docs/unity/setup#available-libraries) that you want to use in
   your app.


   For an optimal experience with Firebase Cloud Messaging, we recommend
   [enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
   in your project. Also, as part of setting up Analytics, you need to add
   the Firebase package for Analytics to your app.


   ### Analytics enabled


   - Add the Firebase package for Google Analytics: `FirebaseAnalytics.unitypackage`
   - Add the package for Firebase Cloud Messaging: `FirebaseMessaging.unitypackage`

   <br />

   <br />

   ### Analytics not enabled


   Add the package for Firebase Cloud Messaging:
   `FirebaseMessaging.unitypackage`

   <br />

4. In the *Import Unity Package* window, click **Import**.

5. Back in the Firebase console, in the setup workflow, click **Next**.

> [!IMPORTANT]
> **Important:** With the Firebase Unity SDK for iOS, **do not disable method
> swizzling** . Swizzling is required by the SDK; without it, key Firebase features (such as FCM token handling) do not function properly.

### Step 5: Confirm Google Play services version requirements

Some products in the Firebase Unity SDK for Android require
[Google Play services](https://developers.google.com/android/guides/overview).
Learn
[which products have this dependency](https://firebase.google.com/docs/android/android-play-services#google-play-services-required-recommended).
Google Play services must be up-to-date before those products can be used.

Add the following `using` statement and initialization code at the start of your
application. You can check for and optionally update Google Play services to the
required version before calling any other methods in the SDK.

    using Firebase.Extensions;

    Firebase.FirebaseApp.CheckAndFixDependenciesAsync().ContinueWithOnMainThread(task => {
      var dependencyStatus = task.Result;
      if (dependencyStatus == Firebase.DependencyStatus.Available) {
        // Create and hold a reference to your FirebaseApp,
        // where app is a Firebase.FirebaseApp property of your application class.
           app = Firebase.FirebaseApp.DefaultInstance;

        // Set a flag here to indicate whether Firebase is ready to use by your app.
      } else {
        UnityEngine.Debug.LogError(System.String.Format(
          "Could not resolve all Firebase dependencies: {0}", dependencyStatus));
        // Firebase Unity SDK is not safe to use here.
      }
    });

Your Unity project is registered and configured to use Firebase.

> [!NOTE]
> Visit [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup) to:
>
> - Learn which [Firebase products](https://firebase.google.com/docs/unity/setup#available-libraries) the Firebase Unity SDK supports.
> - Set up a [desktop
>   workflow](https://firebase.google.com/docs/unity/setup#desktop-workflow) for your Unity project.
> - Troubleshoot [known
>   issues](https://firebase.google.com/docs/unity/setup#known-issues).

## Get setup with Apple platforms

Use the following instructions to set up FCM with Unity and Apple
platforms.

### Upload your APNs authentication key


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

### Enable push notifications on Apple platforms

1. Click your project in Xcode, then select the **General** tab from the **Editor area**.
2. Scroll to **Linked Frameworks and Libraries** , then click the **+** button to add a framework.
3. In the window that appears, scroll to **UserNotifications.framework** , click that entry, then click **Add**.
4. Click your project in Xcode, then select the **Capabilities** tab from the **Editor area**.
5. Switch **Push Notifications** to **On**.
6. Scroll to **Background Modes** , then switch it to **On**.
7. Select the **Remote notifications** checkbox under **Background Modes**.

## Initialize Firebase Cloud Messaging

The Firebase Cloud Message library will be initialized when adding handlers
for either the `TokenReceived` or `MessageReceived` events.

Upon initialization, a registration token is requested for the client app
instance. The app will receive the token with the `OnTokenReceived` event,
which should be cached for later use. You'll need this
token if you want to target this specific device for messages.

In addition, you will need to register for the `OnMessageReceived` event if
you want to be able to receive incoming messages.

The setup will look like this:

```c#
public void Start() {
  Firebase.Messaging.FirebaseMessaging.TokenReceived += OnTokenReceived;
  Firebase.Messaging.FirebaseMessaging.MessageReceived += OnMessageReceived;
}

public void OnTokenReceived(object sender, Firebase.Messaging.TokenReceivedEventArgs token) {
  UnityEngine.Debug.Log("Received Registration Token: " + token.Token);
}

public void OnMessageReceived(object sender, Firebase.Messaging.MessageReceivedEventArgs e) {
  UnityEngine.Debug.Log("Received a new message from: " + e.Message.From);
}
```

## Get setup with Android platforms

Use the following instructions to setup FCM with Unity and Android
platforms.

### Configure an Android entry point Activity

Firebase Cloud Messaging comes bundled with a custom entry point
activity that replaces the default `UnityPlayerActivity`. If you are not using
a custom entry point, this replacement happens automatically and you shouldn't
have to take any additional action.

The Firebase Cloud Messaging Unity Plugin on Android comes bundled with two
additional files:

- `Assets/Plugins/Android/libmessaging_unity_player_activity.jar` contains an activity called `MessagingUnityPlayerActivity` that replaces the standard `UnityPlayerActivity`.
- `Assets/Plugins/Android/AndroidManifest.xml` instructs the app to use `MessagingUnityPlayerActivity` as the entry point to the app.

These files are provided because the default `UnityPlayerActivity` does not
handle `onStop`, `onRestart` activity lifecycle transitions or implement the
`onNewIntent` which is necessary for Firebase Cloud Messaging to correctly
handle incoming messages.

### Configure a custom entry point Activity

If your app does not use the default `UnityPlayerActivity` you will need to
remove the supplied `AndroidManifest.xml` and make sure that your custom
activity properly handles all transitions of the [Android Activity
Lifecycle](https://developer.android.com/reference/android/app/Activity.html#ActivityLifecycle)
(an example of how to do this is shown below). If your custom activity extends
`UnityPlayerActivity` you can instead extend
`com.google.firebase.MessagingUnityPlayerActivity` which implements all
necessary methods.

If you are using a custom Activity and not extending
`com.google.firebase.MessagingUnityPlayerActivity`, you should include the
following snippets in your Activity.

```c#
/**
 * Workaround for when a message is sent containing both a Data and Notification payload.
 *
 * When the app is in the background, if a message with both a data and notification payload is
 * received the data payload is stored on the Intent passed to onNewIntent. By default, that
 * intent does not get set as the Intent that started the app, so when the app comes back online
 * it doesn't see a new FCM message to respond to. As a workaround, we override onNewIntent so
 * that it sends the intent to the MessageForwardingService which forwards the message to the
 * FirebaseMessagingService which in turn sends the message to the application.
 */
@Override
protected void onNewIntent(Intent intent) {
  Intent message = new Intent(this, MessageForwardingService.class);
  message.setAction(MessageForwardingService.ACTION_REMOTE_INTENT);
  message.putExtras(intent);
  message.setData(intent.getData());
  // For earlier versions of Firebase C++ SDK (< 7.1.0), use `startService`.
  // startService(message);
  MessageForwardingService.enqueueWork(this, message);
}

/**
 * Dispose of the mUnityPlayer when restarting the app.
 *
 * This makes sure that when the app starts up again it does not start with stale data.
 */
@Override
protected void onCreate(Bundle savedInstanceState) {
  if (mUnityPlayer != null) {
    mUnityPlayer.quit();
    mUnityPlayer = null;
  }
  super.onCreate(savedInstanceState);
}
```

New versions of Firebase C++ SDK (7.1.0 onwards) use `JobIntentService` which
requires additional modifications in `AndroidManifest.xml` file.

```c#
<service android:name="com.google.firebase.messaging.MessageForwardingService"
     android:permission="android.permission.BIND_JOB_SERVICE"
     android:exported="false" >
</service>
```

### Message delivery on Android

When the app is not running at all and a user taps on a notification,
the message is not, by default, routed through FCM's built in
callbacks. In this case, message payloads are received through an `Intent`
used to start the application.

Messages received while the app is in the background have the content of their
notification field used to populate the system tray notification, but that
notification content won't be communicated to FCM. This means that
`FirebaseMessage.Notification` will be a null.

In summary:

| App state | Notification | Data | Both |
|---|---|---|---|
| Foreground | `Firebase.Messaging.FirebaseMessaging.MessageReceived` | `Firebase.Messaging.FirebaseMessaging.MessageReceived` | `Firebase.Messaging.FirebaseMessaging.MessageReceived` |
| Background | System tray | `Firebase.Messaging.FirebaseMessaging.MessageReceived` | Notification: system tray Data: in extras of the intent. |

### Handling messages with deep links on Android

FCM allows messages to be sent containing a deep link into your app.
To receive messages that contain a deep link, you must add a new intent filter
to the activity that handles deep links for your app. The intent filter should
catch deep links of your domain. In AndroidManifest.xml:

```c#
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

```c#
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

## Prevent auto initialization

FCM generates a registration token for device targeting.
When a token is generated, the library uploads the
identifier and configuration data to Firebase. If you want to get an explicit
opt-in before using the token, you can prevent generation at configure time by
disabling FCM (and on Android, Analytics). You can add a metadata value to
your `Info.plist` (not your `GoogleService-Info.plist`) on Apple, or your
`AndroidManifest.xml` on Android:

#### Android

```c#
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

```c#
Firebase.Messaging.FirebaseMessaging.TokenRegistrationOnInitEnabled = true;
```

This value persists across app restarts once set.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for Unity:

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in a Unity Client](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=unity)
- [Send topic messages](https://firebase.google.com/docs/cloud-messaging/unity/topic-messaging)