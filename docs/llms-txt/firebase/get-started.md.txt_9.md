# Source: https://firebase.google.com/docs/crashlytics/unity/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started) [Android](https://firebase.google.com/docs/crashlytics/android/get-started) [Android NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started) |

<br />

This guide describes how to get started with Firebase Crashlytics in
your Unity project.

After you've set up the Firebase Crashlytics SDK in your app, you can get
comprehensive crash reports in the Firebase console.

Setting up Crashlytics requires tasks both in the Firebase console and
your IDE (like adding a Firebase configuration file and the Crashlytics
SDK). To finish setup, you'll need to force a test crash to send your first
crash report to Firebase.

## Before you begin

1. If you haven't already, [add Firebase](https://firebase.google.com/docs/unity/setup#set_up_environment)
   to your Unity project. If you don't have a Unity project, you can download a
   [sample app](https://github.com/google/mechahamster).

2. **Recommended** : To automatically get
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#get-breadcrumb-logs)
   to understand user actions leading up to a crash, non-fatal, or ANR event,
   you need to enable Google Analytics in your Firebase project.

   - If your existing Firebase project doesn't have Google Analytics
     enabled, you can enable Google Analytics from the
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/analytics) of your
     \> *Project settings*
     in the Firebase console.

   - If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.

## **Step 1** : Add the Crashlytics SDK to your app

Note that when you registered your Unity project with your Firebase project, you
might have already downloaded the Firebase Unity SDK and added the packages
described in the following steps.

1. Download the [Firebase Unity SDK](https://firebase.google.com/download/unity), then unzip the SDK somewhere convenient.
   The Firebase Unity SDK is not platform-specific.

2. In your open Unity project, navigate to
   **Assets** \> **Import Package** \> **Custom Package**.

3. From the unzipped SDK, select to import the Crashlytics SDK
   (`FirebaseCrashlytics.unitypackage`).

   To take advantage of
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#get-breadcrumb-logs)
   also add the Firebase SDK for Google Analytics to your app
   (`FirebaseAnalytics.unitypackage`). Make sure that
   [Google Analytics is enabled](https://support.google.com/firebase/answer/9289399#linkga)
   in your Firebase project.

   > [!NOTE]
   > **Unity 2017.x and later** allow the use of the .NET 4.x
   > framework. If your Unity project uses .NET 4.x, import
   > `dotnet4/FirebaseCrashlytics.unitypackage`.

4. In the *Import Unity Package* window, click **Import**.

> [!IMPORTANT]
> **Important:** With the Firebase Unity SDK for Apple platforms, **do not disable
> method swizzling** . Swizzling is required by the SDK; without it, key Firebase features (such as FCM token handling) do not function properly.

## **Step 2** : Initialize Crashlytics

1. Create a new C# script, then add it to a `GameObject` in the scene.

   1. Open your first scene, then create an empty `GameObject` named
      `CrashlyticsInitializer`.

   2. Click **Add Component** in the **Inspector** for the new object.

   3. Select your `CrashlyticsInit` script to add it to the
      `CrashlyticsInitializer` object.

2. Initialize Crashlytics in the script's `Start` method:

   ```c#
   using System.Collections;
   using System.Collections.Generic;
   using UnityEngine;

   // Import Firebase and Crashlytics
   using Firebase;
   using Firebase.Crashlytics;

   public class CrashlyticsInit : MonoBehaviour {
       // Use this for initialization
       void Start () {
           // Initialize Firebase
           Firebase.FirebaseApp.CheckAndFixDependenciesAsync().ContinueWith(task => {
               var dependencyStatus = task.Result;
               if (dependencyStatus == Firebase.DependencyStatus.Available)
               {
                   // Create and hold a reference to your FirebaseApp,
                   // where app is a Firebase.FirebaseApp property of your application class.
                   // Crashlytics will use the DefaultInstance, as well;
                   // this ensures that Crashlytics is initialized.
                   Firebase.FirebaseApp app = Firebase.FirebaseApp.DefaultInstance;

                   // When this property is set to true, Crashlytics will report all
                   // uncaught exceptions as fatal events. This is the recommended behavior.
                   Crashlytics.ReportUncaughtExceptionsAsFatal = true;

                   // Set a flag here for indicating that your project is ready to use Firebase.
               }
               else
               {
                   UnityEngine.Debug.LogError(System.String.Format(
                     "Could not resolve all Firebase dependencies: {0}",dependencyStatus));
                   // Firebase Unity SDK is not safe to use here.
               }
           });
       }

     // Update is called once per frame
     void Update()
       // ...
   }
   ```

## **Step 3** : *(Android only)* Get set up for symbol uploading

***This step is only required for Android apps that use IL2CPP.***

- For Android apps that use Unity's Mono scripting backend, these steps aren't
  needed.

- For Apple platform apps, these steps aren't needed because the Firebase Unity
  Editor plugin automatically configures your Xcode project to upload symbols.

Crashlytics's Unity SDK 8.6.1+ automatically includes NDK crash reporting,
which allows Crashlytics to automatically report Unity
[IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html)
crashes on Android. However, to see symbolicated stack traces for native library
crashes in the Crashlytics dashboard, you must upload symbol information at
build time using the Firebase CLI.

To get set up for symbol uploading, follow the instructions to
[install the Firebase CLI](https://firebase.google.com/docs/cli).

If you've already installed the CLI, make sure to
[update to its latest version](https://firebase.google.com/docs/cli#update-cli).

> [!NOTE]
> **Note:** You can also run Firebase CLI commands in Cloud Shell. [Cloud Shell](https://firebase.google.com/docs/cloud-shell) is a browser-based, pre-authenticated command-line environment, accessible from the Firebase console, and comes with the Firebase CLI pre-installed. This makes it a convenient option for getting started quickly, provided you add your project files to the Cloud Shell environment.

## **Step 4**: Build your project and upload symbols

> [!NOTE]
> **Note:** Complete the steps in this section to get started with Crashlytics. Then, in the future, complete these steps each time that you create a release build or any build for which you want to see symbolicated stack traces in the Firebase console.

#### **iOS+** (Apple platform)

1. From the *Build Settings* dialog, export your project to an Xcode workspace.

2. Build your app.

   For Apple platforms, the Firebase Unity Editor plugin automatically
   configures your Xcode project to generate and upload a
   Crashlytics-compatible symbol file to Firebase servers for each build.

#### **Android**

1. From the *Build Settings* dialog, do one of the following:

   - Export to an Android Studio project to build your project; or

   - Build your APK directly from the Unity Editor.  

     Before building, make sure the checkbox for **Create symbols.zip** is
     checked in the *Build Settings* dialog.

2. Once your build has finished, generate a Crashlytics-compatible symbol
   file and upload it to Firebase servers by running the following
   Firebase CLI command:

   ```
   firebase crashlytics:symbols:upload --app=FIREBASE_APP_ID PATH/TO/SYMBOLS
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
     >   Scroll down to the *Your apps* card, then click on the desired Firebase
     >   App to find its App ID.

     <br />

     <br />

   - <var translate="no">PATH/TO/SYMBOLS</var>: The path to the symbol file generated by the
     CLI

     - Exported to an Android Studio project ---
       <var translate="no">PATH/TO/SYMBOLS</var> is the `unityLibrary/symbols` directory,
       which is created in the exported project root after you build the app
       via Gradle or Android Studio.

     - Built the APK directly from within Unity ---
       <var translate="no">PATH/TO/SYMBOLS</var> is the path of the zipped symbol file
       generated in the project root directory when your build finished
       (for example:
       `myproject/myapp-1.0-v100.symbols.zip`).

   View advanced options for using the
   Firebase CLI command for symbol file generation and upload

   | **Flag** | **Description** |
   |---|---|
   | `--generator=csym` | Uses the legacy cSYM symbol file generator instead of the default Breakpad generator Not recommended for use. We recommend using the default Breakpad symbol file generator. |
   | `--generator=breakpad` | Uses the Breakpad symbol file generator Note that the default for symbol file generation is Breakpad. Only use this flag if you've added `symbolGenerator { csym() }` in your build configuration and you want to override it to use Breakpad instead. |
   | `--dry-run` | Generates the symbol files but does not upload them This flag is useful if you want to inspect the content of the files that are sent. |
   | `--debug` | Provides additional debugging information |

## **Step 5**: Force a test crash to finish setup

To finish setting up Crashlytics and see initial data in the
Crashlytics dashboard of the Firebase console, you need to force a test
crash.

1. Find an existing `GameObject`, then add to it the following script. This
   script will cause a test crash a few seconds after you run your app.

   ```c#
   using System;
   using UnityEngine;

   public class CrashlyticsTester : MonoBehaviour {

       int updatesBeforeException;

       // Use this for initialization
       void Start () {
         updatesBeforeException = 0;
       }

       // Update is called once per frame
       void Update()
       {
           // Call the exception-throwing method here so that it's run
           // every frame update
           throwExceptionEvery60Updates();
       }

       // A method that tests your Crashlytics implementation by throwing an
       // exception every 60 frame updates. You should see reports in the
       // Firebase console a few minutes after running your app with this method.
       void throwExceptionEvery60Updates()
       {
           if (updatesBeforeException > 0)
           {
               updatesBeforeException--;
           }
           else
           {
               // Set the counter to 60 updates
               updatesBeforeException = 60;

               // Throw an exception to test your Crashlytics implementation
               throw new System.Exception("test exception please ignore");
           }
       }
   }
   ```
2. Build your app and upload symbol information after your build finishes.

   - **iOS+**: The Firebase Unity Editor plugin automatically configures your
     Xcode project to upload your symbol file.

   - **Android** : For your Android apps that use IL2CPP, run the
     Firebase CLI `crashlytics:symbols:upload` command to upload your
     symbol file.

3. Run your app. Once your app is running, watch the device log and wait for
   the exception to trigger from the `CrashlyticsTester`.

   - **iOS+**: View logs in the bottom pane of Xcode.

   - **Android** : View logs by running the following command in the terminal:
     `adb logcat`.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes,
   [enable debug logging](https://firebase.google.com/docs/crashlytics/unity/test-implementation#enable-debug-logging)
   to see if your app is sending crash reports.

<br />

And that's it! Crashlytics is now monitoring your app for crashes.
Visit the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) to view and investigate
all your reports and statistics.

## Next steps

-
  ***(Recommended)*** For Android apps that use IL2CPP,
  get help debugging crashes caused by native memory errors by
  [collecting
  GWP-ASan reports](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#gwp-asan-unity).
  These memory-related errors can be associated with memory corruption within
  your app, which is the leading cause of app security vulnerabilities.
  To take advantage of this debugging feature, make sure your app
  uses the latest Crashlytics SDK for Unity (v10.7.0+) and has
  [GWP-ASan explicitly enabled](https://developer.android.com/ndk/guides/gwp-asan#opt-in)
  (requires you to
  [modify your Android App Manifest](https://docs.unity3d.com/Manual/android-manifest.html)).

-
  [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports)
  by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.

-
  [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud)
  for advanced analysis and features, like
  querying your data, building custom dashboards, and setting up custom alerts.