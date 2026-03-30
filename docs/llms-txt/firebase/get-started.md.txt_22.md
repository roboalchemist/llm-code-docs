# Source: https://firebase.google.com/docs/crashlytics/flutter/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started) [Android](https://firebase.google.com/docs/crashlytics/android/get-started) [Android NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started) |

<br />

This guide describes how to get started with Firebase Crashlytics in
your Flutter app.

After you've set up the Crashlytics Flutter plugin in your app, you can get
comprehensive crash reports in the Firebase console.

Setting up Crashlytics involves using both a command-line tool and your IDE.
To finish setup, you'll need to force a test exception to be thrown to send your
first crash report to Firebase.

## Before you begin

1. If you haven't already,
   [configure and initialize Firebase](https://firebase.google.com/docs/flutter/setup) in your Flutter
   project.

2. **Recommended** : To automatically get
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#get-breadcrumb-logs)
   to understand user actions leading up to a crash, non-fatal, or ANR event,
   you need to enable Google Analytics in your Firebase project.

   - If your existing Firebase project doesn't have Google Analytics
     enabled, you can enable Google Analytics from the
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/analytics) of your
     \> *Project settings*
     in the Firebase console.

   - If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.

   Note that breadcrumb logs are available for all Android and Apple platforms
   supported by Crashlytics (except watchOS).

## **Step 1** : Add Crashlytics to your Flutter project

1. From the root of your Flutter project, run the following command to install
   the Flutter plugin for Crashlytics.

   To take advantage of
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports#get-breadcrumb-logs),
   also add the Flutter plugin for Google Analytics to your app.
   Make sure that
   [Google Analytics is enabled](https://support.google.com/firebase/answer/9289399#linkga)
   in your Firebase project.

       flutter pub add firebase_crashlytics && flutter pub add firebase_analytics

2. From the root directory of your Flutter project, run the following command:

       flutterfire configure

   Running this command ensures that your Flutter app's Firebase configuration
   is up-to-date and, for Android, adds the required Crashlytics Gradle
   plugin to your app.
3. Once complete, rebuild your Flutter project:

       flutter run

4. *(Optional)* If your Flutter project uses the `--split-debug-info` flag
   (and, optionally, also the `--obfuscate` flag), additional steps are
   required to show readable stack traces for your apps.

   - **Apple platforms:** Make sure that your project is using the recommended
     version configuration (Flutter 3.12.0+ and
     Crashlytics Flutter plugin 3.3.4+) so that your project can
     automatically generate and upload Flutter symbols (dSYM files) to
     Crashlytics.

   - **Android:** Use the [Firebase CLI](https://firebase.google.com/docs/cli) (v.11.9.0+) to upload
     Flutter debug symbols. You need to upload the debug symbols *before*
     reporting a crash from an obfuscated code build.

     From the root directory of your Flutter project, run the following
     command:

     ```
     firebase crashlytics:symbols:upload --app=FIREBASE_APP_ID PATH/TO/symbols
     ```
     - <var translate="no">FIREBASE_APP_ID</var>: Your Firebase Android App ID (not your
       package name)  

       Example Firebase Android App ID: `1:567383003300:android:17104a2ced0c9b9b`

       <br />

       Need to find your Firebase App ID?

       <br />

       > Here are two ways to find your Firebase App ID:
       > - In your `google-services.json` file, your App ID is the
       >   `mobilesdk_app_id` value; or
       >
       > - In the Firebase console, go to your
       >   [*Project settings*](https://console.firebase.google.com/project/_/settings/general/).
       >   Go to the *Your apps* card, then click the intended Firebase App
       >   to find its App ID.

       <br />

       <br />

     - `PATH/TO/symbols`: The same directory that you
       pass to the `--split-debug-info` flag when building the application

## **Step 2**: Configure crash handlers

You can automatically catch all errors that are thrown within the Flutter
framework by overriding `FlutterError.onError` with
`FirebaseCrashlytics.instance.recordFlutterFatalError`:

    void main() async {
      WidgetsFlutterBinding.ensureInitialized();

      await Firebase.initializeApp();

      // Pass all uncaught "fatal" errors from the framework to Crashlytics
      FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterFatalError;

      runApp(MyApp());
    }

To catch asynchronous errors that aren't handled by the Flutter framework, use
`PlatformDispatcher.instance.onError`:

    Future<void> main() async {
        WidgetsFlutterBinding.ensureInitialized();
        await Firebase.initializeApp();
        FlutterError.onError = (errorDetails) {
          FirebaseCrashlytics.instance.recordFlutterFatalError(errorDetails);
        };
        // Pass all uncaught asynchronous errors that aren't handled by the Flutter framework to Crashlytics
        PlatformDispatcher.instance.onError = (error, stack) {
          FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
          return true;
        };
        runApp(MyApp());

    }

For examples of how to handle other types of errors, see
[Customize crash reports](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports).

## **Step 3**: Force a test crash to finish setup

To finish setting up Crashlytics and see initial data in the Crashlytics
dashboard of the Firebase console, you need to force a test exception to be
thrown.

1. Add code to your app that you can use to force a test exception to be
   thrown.

   If you've added an error handler that calls
   `FirebaseCrashlytics.instance.recordError(error, stack, fatal: true)` to the
   top-level `Zone`, you can use the following code to add a button to your app
   that, when pressed, throws a test exception:

       TextButton(
           onPressed: () => throw Exception(),
           child: const Text("Throw Test Exception"),
       ),

2. Build and run your app.

3. Force the test exception to be thrown in order to send your app's first
   report:

   1. Open your app from your test device or emulator.

   2. In your app, press the test exception button that you added using the
      code above.

4. Go to the
   [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics)
   of the Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes,
   [enable debug logging](https://firebase.google.com/docs/crashlytics/flutter/test-implementation#enable-debug-logging)
   to see if your app is sending crash reports.

<br />

And that's it! Crashlytics is now monitoring your app for crashes and, on
Android, non-fatal errors and ANRs. Visit the
[Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics)
to view and investigate all your reports and statistics.

## Next steps

- [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports)
  by adding opt-in reporting, logs, keys, and tracking of additional non-fatal
  errors.

- [Integrate with Google Play](https://firebase.google.com/docs/crashlytics/integrate-with-google-play)
  so that you can filter your Android app's crash reports by Google Play track
  directly in the Crashlytics dashboard. This lets you better focus
  your dashboard on specific builds.

- [View stack traces and crash statistics alongside your code](https://developer.android.com/studio/preview/features#aqi)
  with the *App Quality Insights* window in Android Studio (available starting
  with Electric Eel 2022.1.1).

- [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud)
  for advanced analysis and features, like
  querying your data, building custom dashboards, and setting up custom alerts.