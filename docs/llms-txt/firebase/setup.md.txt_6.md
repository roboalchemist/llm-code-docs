# Source: https://firebase.google.com/docs/flutter/setup.md.txt

# Add Firebase to your Flutter app

<button value="ios" default="">iOS+</button> <button value="android">Android</button> <button value="web">Web</button>

<br />

[Video](https://www.youtube.com/watch?v=FkFvQ0SaT1I)

## Prerequisites

- Install your preferred [editor or IDE](https://docs.flutter.dev/get-started/editor/).

- [Install Flutter](https://docs.flutter.dev/get-started/install/) for your specific
  operating system, including the following:

  - Flutter SDK
  - Supporting libraries
  - Platform-specific software and SDKs
- [Sign into Firebase](https://console.firebase.google.com/) using your Google
  account.

If you don't already have a Flutter app, you can complete the [Get
Started: Test Drive](https://docs.flutter.dev/get-started/test-drive?tab=vscode) to
create a new Flutter app using your preferred editor or IDE.

## **Step 1**: Install the required command line tools

1. If you haven't already,
   [install the Firebase CLI](https://firebase.google.com/docs/cli#setup_update_cli).

2. Log into Firebase using your Google account by running the following
   command:

       firebase login

3. Install the FlutterFire CLI by running the following command from any
   directory:

       dart pub global activate flutterfire_cli

## **Step 2**: Configure your apps to use Firebase

Use the FlutterFire CLI to configure your Flutter apps to connect to Firebase.

From your Flutter project directory, run the following command to start the
app configuration workflow:

    flutterfire configure

<br />

What does this `flutterfire configure`
workflow do?

<br />

> The `flutterfire configure` workflow does the following:
>
> - Asks you to select the platforms (iOS, Android, Web) supported in your
>   Flutter app. For each selected platform, the FlutterFire CLI creates a new
>   Firebase app in your Firebase project.
>
>   You can select either to use an existing Firebase project or to create a
>   new Firebase project. If you already have apps registered in an existing
>   Firebase project, the FlutterFire CLI will attempt to match them based on
>   your current Flutter project configuration.
>
>   > [!NOTE]
>   > **Note:** Here are some tips about setting up and managing your Firebase project:
>   > - Check out our [best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices) for adding apps to a Firebase project, including how to handle multiple variants.
>   > - [Enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga) in your project, which enables you to have an optimal experience using many Firebase products, like Crashlytics and Remote Config.
>
> - Creates a Firebase configuration file (`firebase_options.dart`) and adds it
>   to your `lib/` directory.
>
>   > [!NOTE]
>   > **Note:** This Firebase config file contains unique, but non-secret identifiers for each platform you selected.   
>   > Visit [Understand
>   > Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects) to learn more about this config file.
>
> - *(for Crashlytics or Performance Monitoring on Android)* Adds the required
>   product-specific Gradle plugins to your Flutter app.
>
>   > [!NOTE]
>   > **Note:** For the FlutterFire CLI to add the appropriate Gradle plugin, the product's Flutter plugin must already be imported into your Flutter app.
>
<br />

<br />

<br />

> [!CAUTION]
> After this initial running of `flutterfire configure`, you need to re-run the command any time that you:
>
> - Start supporting a new platform in your Flutter app.
> - Start using a new Firebase service or product in your Flutter app, especially if you start using sign-in with Google, Crashlytics, Performance Monitoring, or Realtime Database.
>
> Re-running the command ensures that your Flutter app's Firebase
> configuration is up-to-date and (for Android) automatically adds any
> required Gradle plugins to your app.

## **Step 3**: Initialize Firebase in your app

1. From your Flutter project directory, run the following command to install
   the core plugin:

       flutter pub add firebase_core

2. From your Flutter project directory, run the following command to ensure
   that your Flutter app's Firebase configuration is up-to-date:

       flutterfire configure

3. In your `lib/main.dart` file, import the Firebase core plugin and the
   configuration file you generated earlier:

       import 'package:firebase_core/firebase_core.dart';
       import 'firebase_options.dart';

4. Also in your `lib/main.dart` file, initialize Firebase using the
   `DefaultFirebaseOptions` object exported by the configuration file:

       WidgetsFlutterBinding.ensureInitialized();
       await Firebase.initializeApp(
         options: DefaultFirebaseOptions.currentPlatform,
       );
       runApp(const MyApp());

5. Rebuild your Flutter application:

       flutter run

If you would rather use a demo project, you can start the [Firebase Emulator](https://firebase.google.com/docs/emulator-suite) and
in your `lib/main.dart` file initialize Firebase using `demoProjectId` (it should start with `demo-`):

      await Firebase.initializeApp(
        demoProjectId: "demo-project-id",
      );

## **Step 4**: Add Firebase plugins

You access Firebase in your Flutter app through the various
[Firebase Flutter plugins](https://firebase.google.com/docs/flutter/setup#available-plugins), one for each Firebase product
(for example: Cloud Firestore, Authentication, Analytics, etc.).

Since Flutter is a multi-platform framework, each Firebase plugin is applicable
for Apple, Android, and web platforms. So, if you add any Firebase plugin to
your Flutter app, it will be used by the Apple, Android, and web versions of
your app.

Here's how to add a Firebase Flutter plugin:

1. From your Flutter project directory, run the following command:

   ```
   flutter pub add PLUGIN_NAME
   ```
2. From your Flutter project directory, run the following command:

       flutterfire configure

   Running this command ensures that your Flutter app's Firebase configuration
   is up-to-date and, for Crashlytics and Performance Monitoring on Android, adds the
   required Gradle plugins to your app.
3. Once complete, rebuild your Flutter project:

       flutter run

You're all set! Your Flutter apps are registered and configured to use Firebase.

### Available plugins

| Product | Plugin name | iOS | Android | Web | Other Apple (macOS, etc.) | Windows |
|---|---|---|---|---|---|---|
| [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started) ^1^ | `firebase_ai` |   |   |   | beta |   |
| [Analytics](https://firebase.google.com/docs/analytics/get-started?platform=flutter) | `firebase_analytics` |   |   |   | beta |   |
| [App Check](https://firebase.google.com/docs/app-check/flutter/default-providers) | `firebase_app_check` |   |   |   | beta |   |
| [Authentication](https://firebase.google.com/docs/auth/flutter/start) | `firebase_auth` |   |   |   | beta | beta |
| [Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) | `cloud_firestore` |   |   |   | beta | beta |
| [Cloud Functions](https://firebase.google.com/docs/functions/get-started) | `cloud_functions` |   |   |   | beta |   |
| [Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/flutter/client) | `firebase_messaging` |   |   |   | beta |   |
| [Cloud Storage](https://firebase.google.com/docs/storage/flutter/start) | `firebase_storage` |   |   |   | beta | beta |
| [Crashlytics](https://firebase.google.com/docs/crashlytics/flutter/get-started) | `firebase_crashlytics` |   |   |   | beta |   |
| [Data Connect](https://firebase.google.com/docs/data-connect/flutter-sdk) | `firebase_data_connect` |   |   |   |   |   |
| [Dynamic Links](https://firebase.google.com/docs/dynamic-links/flutter/create) | `firebase_dynamic_links` |   |   |   |   |   |
| [In-App Messaging](https://firebase.google.com/docs/in-app-messaging/get-started?platform=flutter) | `firebase_in_app_messaging` |   |   |   |   |   |
| [Firebase installations](https://firebase.google.com/docs/projects/manage-installations) | `firebase_app_installations` |   |   |   | beta |   |
| [ML Model Downloader](https://firebase.google.com/docs/ml/flutter/use-custom-models) | `firebase_ml_model_downloader` |   |   |   | beta |   |
| [Performance Monitoring](https://firebase.google.com/docs/perf-mon/flutter/get-started) | `firebase_performance` |   |   |   |   |   |
| [Realtime Database](https://firebase.google.com/docs/database/flutter/start) | `firebase_database` |   |   |   | beta |   |
| [Remote Config](https://firebase.google.com/docs/remote-config/get-started?platform=flutter) | `firebase_remote_config` |   |   |   | beta |   |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase" with the plugin
`firebase_vertexai`.*^

> [!CAUTION]
> **Caution:** Firebase on Windows is not intended for production use cases, only local development workflows.

## Try out an example app with Analytics

Like all packages, the `firebase_analytics` plugin comes with an
[example program](https://github.com/firebase/flutterfire/tree/main/packages/firebase_analytics/firebase_analytics/example).

1. Open a Flutter app that you've already configured to use Firebase (see
   instructions on this page).

2. Access the `lib` directory of the app, then delete the existing `main.dart`
   file.

3. From the Google Analytics
   [example program repository](https://github.com/firebase/flutterfire/tree/main/packages/firebase_analytics/firebase_analytics/example/lib),
   copy-paste the following two files into your app's `lib` directory:

   - `main.dart`
   - `tabs_page.dart`
4. Run your Flutter app.

5. Go to your app's Firebase project in the [Firebase console](https://console.firebase.google.com/), then click
   **Analytics** in the left-nav.

   1. Click
      [**Dashboard**](https://support.google.com/firebase/answer/6317517).
      If Analytics is working properly, the dashboard shows an active user
      in the "Users active in the last 30 minutes" panel (this might take
      time to populate this panel).

   2. Click [**DebugView**](https://firebase.google.com/docs/analytics/debugview). Enable the feature to
      see all the events generated by the example program.

For more information about setting up Analytics, visit the getting started
guides for [iOS+](https://firebase.google.com/docs/analytics/get-started?platform=ios),
[Android](https://firebase.google.com/docs/analytics/get-started?platform=android), and
[web](https://firebase.google.com/docs/analytics/get-started?platform=web).

## Next steps

- Get hands-on experience with the
  [Firebase Flutter Codelab](https://firebase.google.com/codelabs/firebase-get-to-know-flutter).

- Prepare to launch your app:

  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).