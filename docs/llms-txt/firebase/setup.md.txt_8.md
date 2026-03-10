# Source: https://firebase.google.com/docs/unity/setup.md.txt

Power up your [Unity](https://unity3d.com) games with our Firebase Unity SDKs.
[Video](https://www.youtube.com/watch?v=A6du3DUTIPI)

To show how easy it is to plug Firebase into your Unity project, we made a
sample game, MechaHamster. If you want to try out adding Firebase to a game, use
the starter version that's on **GitHub** . If you want a completed version, check
out the versions in the **App Store** or the **Google Play Store**.

[MechaHamster (GitHub)](https://github.com/firebase/level-up-with-firebase)

[MechaHamster (App Store)](https://itunes.apple.com/us/app/mechahamster/id1286046770?mt=8&ign-mpt=uo%3D4)

[MechaHamster (Play Store)](https://play.google.com/store/apps/details?id=com.google.fpl.mechahamster)

<br />

**Find out more information about powering up your games with Firebase at our
[Firebase games page](https://firebase.google.com/games).**

> [!CAUTION]
> Learn which [Firebase products](https://firebase.google.com/docs/unity/setup#available-libraries) the Firebase Unity SDK supports.

Already added Firebase to your Unity project? Make sure that you're using the
latest version of the [Firebase Unity SDK](https://firebase.google.com/download/unity).

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

- Set up a physical device or use an emulator to run your app.

  - **For Apple platforms** --- Set up a physical device or use an iOS or tvOS
    simulator.

    <br />

    Do you want to use Cloud Messaging?

    <br />

    <br />

    > For Cloud Messaging on iOS or tvOS, here are the prerequisites:
    > - Set up a *physical device*.
    > - Obtain an Apple Push Notification Authentication Key for your [Apple Developer account](https://developer.apple.com/account).
    > - Enable Push Notifications in XCode under **App \> Capabilities**.

    <br />

    <br />

  - **For Android** ---
    [Emulators](https://developer.android.com/studio/run/managing-avds) must use an
    emulator image with Google Play.

<!-- -->

- [Sign into Firebase](https://console.firebase.google.com/) using your Google account.

If you don't already have a Unity project and just want to try out a Firebase
product, you can download one of our [quickstart samples](https://github.com/firebase/quickstart-unity).

## **Step 1**: Create a Firebase project

Before you can add Firebase to your Unity project, you need to create a Firebase
project to connect to your Unity project. Visit
[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more) to learn more about
Firebase projects.
**View instructions to create a Firebase project**

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

## **Step 2**: Register your app with Firebase

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

## **Step 3**: Add Firebase configuration files

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

## **Step 4**: Add Firebase Unity SDKs

> [!NOTE]
> **Note:** The following setup workflow is recommended for first time users of the Unity SDK. For particular use cases, Firebase offers [alternative setup flows](https://firebase.google.com/docs/unity/setup-alternative).

1. In the Firebase console, click **Download Firebase Unity SDK**, then unzip
   the SDK somewhere convenient.

   - You can download the [Firebase Unity SDK](https://firebase.google.com/download/unity) again at any time.

   - The Firebase Unity SDK is not platform-specific.

2. In your open Unity project, navigate to
   **Assets** \> **Import Package** \> **Custom Package**.

3. From the unzipped SDK, select the [supported Firebase
   products](https://firebase.google.com/docs/unity/setup#available-libraries) that you want to use in
   your app.


   ### Analytics enabled


   - Add the Firebase package for Google Analytics: `FirebaseAnalytics.unitypackage`
   - Add the packages for any other Firebase products you want to use in your app. For example, to use Firebase Authentication and Firebase Realtime Database:  
     `FirebaseAuth.unitypackage` and `FirebaseDatabase.unitypackage`

   <br />

   ### Analytics not enabled


   Add the packages for the Firebase products you want to use in your app.
   For example, to use Firebase Authentication and Firebase Realtime Database:  

   `FirebaseAuth.unitypackage` and
   `FirebaseDatabase.unitypackage`
4. In the *Import Unity Package* window, click **Import**.

5. Back in the Firebase console, in the setup workflow, click **Next**.

> [!IMPORTANT]
> **Important:** With the Firebase Unity SDK for iOS, **do not disable method
> swizzling** . Swizzling is required by the SDK; without it, key Firebase features (such as FCM token handling) do not function properly.

## **Step 5**: Confirm Google Play services version requirements

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

You're all set! Your Unity project is registered and configured to use Firebase.

If you're having trouble getting set up, though, visit the
[Unity troubleshooting \& FAQ](https://firebase.google.com/docs/unity/troubleshooting-faq).

## Set up a desktop workflow (**beta**)

> [!CAUTION]
> **Caution:** Firebase Unity SDK desktop support is a **beta** feature. This feature is intended only for workflows during the development of your game, not for publicly shipping code.

When you're creating a game, it's often much easier to test your game in the
Unity editor and on desktop platforms first, then deploy and test on mobile
devices later in development. To support this workflow, we provide a
[subset of the Firebase Unity SDKs](https://firebase.google.com/docs/unity/setup#available-libraries-desktop) which can run
on Windows, macOS, Linux, and from within the Unity editor.

1. Set up a desktop-platform Unity project by following the same instructions as
   for a mobile platform (start with the
   [Register your app with Firebase](https://firebase.google.com/docs/unity/setup#register-app) step above).

2. Run your Unity project in the Unity IDE or select to build your Unity
   project for **desktop**.

   > [!NOTE]
   > **Note:** Firebase locates your *mobile* Firebase config file (either `GoogleService-Info.plist` or `google-services.json`) that you added to your Unity project. Then, from the mobile config file, Firebase automatically generates a *desktop* Firebase config file (`google-services-desktop.json`). This desktop config file contains the Unity project ID that you entered in the Firebase console setup workflow. This file associates your app with your Firebase project.   
   >
   > If the editor cannot locate the *desktop* config file, [check that the `StreamingAssets` directory exists](https://firebase.google.com/docs/unity/build-debug-guide#ensure_your_project_contains_and_is_using_valid_configuration_files) and that the *desktop* config file is inside of it.

3. *(Optional)* Run your Unity project in Edit Mode.

   The Firebase Unity SDK can also be run in Unity's edit mode, allowing its use
   in editor plugins.
   1. When you create a `FirebaseApp` used by the editor, don't use the
      default instance.

   2. Instead, provide a unique name to the `FirebaseApp.Create()` call.

      This is important to avoid a conflict in options between the instance used
      by the Unity IDE and the instance used by your Unity project.

## Supported Firebase products

Learn more about the Unity Firebase libraries in the
[reference documentation](https://firebase.google.com/docs/reference/unity).

### Available Firebase libraries for mobile

The Firebase Unity SDK supports the following Firebase products on
*Apple* and *Android*:

> [!NOTE]
> **Note:** For Apple platforms, each Firebase library may only support a selection of Apple OS platforms (iOS, tvOS, etc.). Check which platforms are supported by each library in [Learn more about Unity and Firebase](https://firebase.google.com/docs/unity/learn-more#library-support-by-platform).

| Firebase product | Unity package |
|---|---|
| [AdMob](https://developers.google.com/admob/unity/start) | Distributed separately in the AdMob Unity Plugin |
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) | `FirebaseAI.unitypackage` |
| [Analytics](https://firebase.google.com/docs/analytics/unity/start) | `FirebaseAnalytics.unitypackage` |
| [App Check](https://firebase.google.com/docs/app-check) | `FirebaseAppCheck.unitypackage` |
| [Authentication](https://firebase.google.com/docs/auth/unity/start) | `FirebaseAuth.unitypackage` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `FirebaseFirestore.unitypackage` |
| [Cloud Functions](https://firebase.google.com/docs/functions/get-started) | `FirebaseFunctions.unitypackage` |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/unity/client) | `FirebaseMessaging.unitypackage` *(recommended)* `FirebaseAnalytics.unitypackage` |
| [Cloud Storage](https://firebase.google.com/docs/storage/unity/start) | `FirebaseStorage.unitypackage` |
| [Crashlytics](https://firebase.google.com/docs/crashlytics/unity/get-started) | `FirebaseCrashlytics.unitypackage` *(recommended)* `FirebaseAnalytics.unitypackage` |
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links/unity/create) | `FirebaseDynamicLinks.unitypackage` *(recommended)* `FirebaseAnalytics.unitypackage` |
| [Realtime Database](https://firebase.google.com/docs/database/unity/start) | `FirebaseDatabase.unitypackage` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=unity) | `FirebaseRemoteConfig.unitypackage` *(recommended)* `FirebaseAnalytics.unitypackage` |

### Available Firebase libraries for desktop

The Firebase Unity SDK includes [desktop workflow support](https://firebase.google.com/docs/unity/setup#desktop-workflow)
for a subset of products, enabling certain parts of Firebase to be used in the
Unity editor and in standalone desktop builds on Windows, macOS, and Linux.

> [!CAUTION]
> **Caution:** Firebase Unity SDK desktop support is a **beta** feature. This feature is intended only for workflows during the development of your game, not for publicly shipping code.

| Firebase product (desktop) | Unity package |
|---|---|
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) | `FirebaseAI.unitypackage` |
| [App Check](https://firebase.google.com/docs/app-check) | `FirebaseAppCheck.unitypackage` |
| [Authentication](https://firebase.google.com/docs/auth/unity/start) | `FirebaseAuth.unitypackage` |
| [Cloud Functions](https://firebase.google.com/docs/functions/get-started) | `FirebaseFunctions.unitypackage` |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `FirebaseFirestore.unitypackage` |
| [Cloud Storage](https://firebase.google.com/docs/storage/unity/start) | `FirebaseStorage.unitypackage` |
| [Realtime Database](https://firebase.google.com/docs/database/unity/start) | `FirebaseDatabase.unitypackage` |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=unity) | `FirebaseRemoteConfig.unitypackage` |

Firebase provides the remaining desktop libraries as stub (non-functional)
implementations for convenience when building for Windows, macOS, and Linux.
Therefore, you don't need to conditionally compile code to target the desktop.

## Next steps

- Explore [sample Firebase apps](https://firebase.google.com/docs/samples).

- Prepare to launch your app:

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
- Having trouble with Firebase and your Unity project?
  Visit the [Unity troubleshooting \& FAQ](https://firebase.google.com/docs/unity/troubleshooting-faq).