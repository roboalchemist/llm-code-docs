# Source: https://firebase.google.com/docs/analytics/android/get-started.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/get-started) [Android](https://firebase.google.com/docs/analytics/android/get-started) [Web](https://firebase.google.com/docs/analytics/web/get-started) [Flutter](https://firebase.google.com/docs/analytics/flutter/get-started) [Unity](https://firebase.google.com/docs/analytics/unity/get-started) [C++](https://firebase.google.com/docs/analytics/cpp/get-started) |

This quickstart shows you how to add Google Analytics to your app and begin
logging events.

Google Analytics collects usage and behavior data for your app. The SDK
logs two primary types of information:

- **Events:** What is happening in your app, such as user actions, system events, or errors.
- **User properties:** Attributes you define to describe segments of your user base, such as language preference or geographic location.

Analytics automatically logs some
[events](https://support.google.com/firebase/answer/6317485) and
[user properties](https://support.google.com/firebase/answer/6317486);
you don't need to add any code to enable them.

## Before you begin

If you haven't already, [add Firebase to your Android
project](https://firebase.google.com/docs/android/setup) and make sure that Google Analytics is
enabled in your Firebase project:

- If you're creating a new Firebase project, enable Google Analytics
  during the project creation workflow.

- If you're using an existing Firebase project that doesn't have
  Google Analytics enabled, go to the
  [*Integrations*](https://console.firebase.google.com/project/_/settings/integrations)
  tab of your \> *Project settings* to enable it.

When you enable Google Analytics in your project, your Firebase apps are
linked to Google Analytics data streams.

## Add the Analytics SDK to your app

1.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Analytics library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Analytics library
       // When using the BoM, you don't specify versions in Firebase library dependencies
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
       // Add the dependency for the Analytics library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-analytics:23.0.0")
   }
   ```

   <br />

2. Declare the `com.google.firebase.analytics.FirebaseAnalytics` object at the
   top of your activity:

   ### Kotlin

   ```kotlin
   private lateinit var firebaseAnalytics: FirebaseAnalyticshttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L23-L23
   ```

   ### Java

   ```java
   private FirebaseAnalytics mFirebaseAnalytics;
   ```
3. Initialize it in the `onCreate()` method:

   ### Kotlin

   ```kotlin
   // Obtain the FirebaseAnalytics instance.
   firebaseAnalytics = Firebase.analyticshttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L31-L32
   ```

   ### Java

   ```java
   // Obtain the FirebaseAnalytics instance.
   mFirebaseAnalytics = FirebaseAnalytics.getInstance(this);
   ```

## Start logging events

After you have created a `FirebaseAnalytics` instance, you can begin to log
events with the [`logEvent()`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(java.lang.String,%20android.os.Bundle)) method.

Certain events are
[recommended for all apps](https://support.google.com/firebase/answer/6317498);
others are recommended for specific business types or verticals. You should send
suggested events along with their prescribed parameters, to ensure maximum
available detail in your reports and to benefit from future features and
integrations as they become available. This section demonstrates logging a
predefined event, for more information on logging events, see
[Log events](https://firebase.google.com/docs/analytics/android/events).

The following code logs a [`SELECT_CONTENT`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_CONTENT) event when
a user clicks on a specific element in your app.

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_ITEM) {
    param(FirebaseAnalytics.Param.ITEM_ID, id)
    param(FirebaseAnalytics.Param.ITEM_NAME, name)
    param(FirebaseAnalytics.Param.CONTENT_TYPE, "image")
}
```

### Java

```java
Bundle bundle = new Bundle();
bundle.putString(FirebaseAnalytics.Param.ITEM_ID, id);
bundle.putString(FirebaseAnalytics.Param.ITEM_NAME, name);
bundle.putString(FirebaseAnalytics.Param.CONTENT_TYPE, "image");
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_CONTENT, bundle);
```

You can enable verbose logging to monitor logging of events by the SDK to help
verify that events are being logged properly. This includes both automatically
and manually logged events.

You can enable verbose logging with a series of `adb` commands:

    adb shell setprop log.tag.FA VERBOSE
    adb shell setprop log.tag.FA-SVC VERBOSE
    adb logcat -v time -s FA FA-SVC

This command displays your events in the Android Studio logcat, helping you
immediately verify that events are being sent.

## Next steps

- Understand [each Analytics report](https://firebase.google.com/docs/analytics/reports).
- Use the [DebugView](https://firebase.google.com/docs/analytics/debugview) to verify your events.
- Explore your data in the [Firebase console.](https://console.firebase.google.com/project/_/analytics/)
- Explore the guides on [events](https://firebase.google.com/docs/analytics/android/events) and [user properties.](https://firebase.google.com/docs/analytics/android/user-properties)
- Learn how to export your data to [BigQuery.](https://support.google.com/firebase/answer/7030014)