# Source: https://firebase.google.com/docs/crashlytics/android/get-started.md.txt

<br />

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/get-started) [Android](https://firebase.google.com/docs/crashlytics/android/get-started) [Android NDK](https://firebase.google.com/docs/crashlytics/android/get-started-ndk) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/get-started) [Unity](https://firebase.google.com/docs/crashlytics/unity/get-started) |

<br />

This guide describes how to get started with Firebase Crashlytics in
your Android app.

After you've set up the Firebase Crashlytics SDK in your app, you can get
comprehensive crash reports in the Firebase console. With Crashlytics for
Android, you get reports for crashes, non-fatal errors, and
"Application Not Responding" (ANR) errors.

Setting up Crashlytics requires tasks both in the Firebase console and
your IDE (like adding a Firebase configuration file and the Crashlytics
SDK). To finish setup, you'll need to force a test crash to send your first
crash report to Firebase.

## Before you begin

1. If you haven't already, [add Firebase](https://firebase.google.com/docs/android/setup) to your Android
   project. If you don't have an Android app, you can download
   a [sample app](https://firebase.google.com/docs/samples).

2. **Recommended** : To automatically get
   [breadcrumb logs](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#get-breadcrumb-logs)
   to understand user actions leading up to a crash, non-fatal, or ANR event,
   you need to enable Google Analytics in your Firebase project.

   - If your existing Firebase project doesn't have Google Analytics
     enabled, you can enable Google Analytics from the
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations/analytics) of your
     \> *Project settings*
     in the Firebase console.

   - If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.

3. Make sure your app has the following ***minimum*** required versions:

   - Gradle 8.0
   - Android Gradle plugin 8.1.0
   - Google services Gradle plugin 4.4.1

## **Step 1** : Add the Crashlytics SDK to your app

> [!NOTE]
> **Does your app use NDK?** Go to the [NDK crash reporting documentation](https://firebase.google.com/docs/crashlytics/ndk-reports) to learn how to configure Crashlytics to report crashes that occur in your app's underlying NDK libraries.

In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Crashlytics library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

<br />

To take advantage of [breadcrumb logs](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#get-breadcrumb-logs),
also add the Firebase SDK for Google Analytics to your app. Make sure that
[Google Analytics is enabled](https://support.google.com/firebase/answer/9289399#linkga)
in your Firebase project.

```
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

    // Add the dependencies for the Crashlytics and Analytics libraries
    // When using the BoM, you don't specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-crashlytics")
    implementation("com.google.firebase:firebase-analytics")
}
```

By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
your app will always use compatible versions of Firebase Android libraries.
*(Alternative)*
Add Firebase library dependencies *without* using the BoM

If you choose not to use the Firebase BoM, you must specify each Firebase library version
in its dependency line.

**Note that if you use *multiple* Firebase libraries in your app, we strongly
recommend using the BoM to manage library versions, which ensures that all versions are
compatible.**

```groovy
dependencies {
    // Add the dependencies for the Crashlytics and Analytics libraries
    // When NOT using the BoM, you must specify versions in Firebase library dependencies
    implementation("com.google.firebase:firebase-crashlytics:20.0.4")
    implementation("com.google.firebase:firebase-analytics:23.0.0")
}
```

<br />

## **Step 2** : Add the Crashlytics Gradle plugin to your app

1. In your **root-level (project-level)** Gradle file
   (`<project>/build.gradle.kts` or `<project>/build.gradle`), add the
   Crashlytics Gradle plugin to the `plugins` block:

   ### Kotlin

   > [!NOTE]
   > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

   ```kotlin
   plugins {
       // Make sure that you have the AGP plugin 8.1+ dependency
       id("com.android.application") version "8.1.4" apply false
       // ...

       // Make sure that you have the Google services Gradle plugin 4.4.1+ dependency
       id("com.google.gms.google-services") version "4.4.4" apply false

       // Add the dependency for the Crashlytics Gradle plugin
       id("com.google.firebase.crashlytics") version "3.0.6" apply false
   }
   ```

   ### Groovy

   > [!NOTE]
   > Are you still using the `buildscript` syntax? Learn how to [add Firebase plugins](https://firebase.google.com/docs/android/troubleshooting-faq#add-plugins-using-buildscript-syntax) using that syntax.

   ```groovy
   plugins {
       // Make sure that you have the AGP plugin 8.1+ dependency
       id 'com.android.application' version '8.1.4' apply false
       // ...

       // Make sure that you have the Google services Gradle plugin 4.4.1+ dependency
       id 'com.google.gms.google-services' version '4.4.4' apply false

       // Add the dependency for the Crashlytics Gradle plugin
       id 'com.google.firebase.crashlytics' version '3.0.6' apply false
   }
   ```

   > [!NOTE]
   > Is your app using a lower version of Gradle? Consider [upgrading](https://firebase.google.com/docs/crashlytics/troubleshooting#android-upgrade-to-gradle-plugin-v3); otherwise, you should use v2.9.9 of the Crashlytics Gradle plugin.

2. In your **module (app-level)** Gradle file
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the Crashlytics Gradle plugin:

   ### Kotlin

   ```kotlin
   plugins {
     id("com.android.application")
     // ...

     // Make sure that you have the Google services Gradle plugin
     id("com.google.gms.google-services")

     // Add the Crashlytics Gradle plugin
     id("com.google.firebase.crashlytics")
   }
   ```

   ### Groovy

   ```groovy
   plugins {
     id 'com.android.application'
     // ...

     // Make sure that you have the Google services Gradle plugin
     id 'com.google.gms.google-services'

     // Add the Crashlytics Gradle plugin
     id 'com.google.firebase.crashlytics'
   }
   ```

## **Step 3**: Force a test crash to finish setup

To finish setting up Crashlytics and see initial data in the
Crashlytics dashboard of the Firebase console, you need to force a test
crash.

1. Add code to your app that you can use to force a test crash.

   You can use the following code in your app's `MainActivity` to add a button
   to your app that, when pressed, causes a crash. The button is labeled
   "Test Crash".

   ### Kotlin

   ```kotlin
   val crashButton = Button(this)
   crashButton.text = "Test Crash"
   crashButton.setOnClickListener {
      throw RuntimeException("Test Crash") // Force a crash
   }

   addContentView(crashButton, ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT))
   ```

   ### Java

   ```java
   Button crashButton = new Button(this);
   crashButton.setText("Test Crash");
   crashButton.setOnClickListener(new View.OnClickListener() {
      public void onClick(View view) {
          throw new RuntimeException("Test Crash"); // Force a crash
      }
   });

   addContentView(crashButton, new ViewGroup.LayoutParams(
          ViewGroup.LayoutParams.MATCH_PARENT,
          ViewGroup.LayoutParams.WRAP_CONTENT));
   ```
2. Build and run your app.

3. Force the test crash in order to send your app's first crash report:

   1. Open your app from your test device or emulator.

   2. In your app, press the "Test Crash" button that you added using the code
      above.

   3. After your app crashes, restart it so that your app can send the crash
      report to Firebase.

4. Go to the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
   Firebase console to see your test crash.

   If you've refreshed the console and you're still not seeing the test crash
   after five minutes,
   [enable debug logging](https://firebase.google.com/docs/crashlytics/android/test-implementation#enable-debug-logging)
   to see if your app is sending crash reports.

<br />

And that's it! Crashlytics is now monitoring your app for crashes, non-fatal
errors, and ANRs.
Visit the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics) to view and investigate
all your reports and statistics.

## Next steps

-
  [Customize your crash report setup](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports)
  by adding opt-in reporting, logs, keys, and tracking of non-fatal errors.

-
  [Integrate with Google Play](https://firebase.google.com/docs/crashlytics/integrate-with-google-play) so that
  you can filter your Android app's crash reports by Google Play track directly in the
  Crashlytics dashboard. This allows you to better focus your dashboard on specific builds.

-
  In Android Studio, view and filter Crashlytics data.

  - Use the *App Quality Insights* (AQI) window in Android Studio to view Crashlytics data alongside your code --- no need to jump back and forth between the Crashlytics dashboard and the IDE to start debugging top issues.
  - Learn [how to use the AQI window](https://developer.android.com/studio/debug/app-quality-insights) in the Android Studio documentation.
  - We'd love to hear from you! Send us feedback about the AQI window by [filing a bug report](https://issuetracker.google.com/issues/new?title=%5BAQI%5D+%3CTitle%3E&cc=adarshf@google.com,makuchaku@google.com,+jbakermalone@google.com&format=PLAIN&component=192708&type=BUG&priority=P1&severity=S2&hotlistIds=4012235&assignee=vkryachko@google.com&template=840533).

  <br />

-
  [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud)
  for advanced analysis and features, like
  querying your data, building custom dashboards, and setting up custom alerts.