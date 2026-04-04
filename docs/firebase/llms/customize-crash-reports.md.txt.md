# Source: https://firebase.google.com/docs/crashlytics/android/customize-crash-reports.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports) [Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports) [Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports) |

<br />

In the Crashlytics dashboard, you can click into an issue and get a detailed
event report. You can customize those reports to help you better understand
what's happening in your app and the circumstances around events reported to
Crashlytics.

- Instrument your app to log [custom keys](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys),
  [custom log messages](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-logs), and [user identifiers](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#set-user-ids).

- Report [exceptions](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#log-excepts) to Crashlytics.

- Automatically get [breadcrumb logs](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#get-breadcrumb-logs) if your app uses the
  Firebase SDK for Google Analytics. These logs give you visibility into
  user actions leading up to a Crashlytics-collected event in your app.

- Turn off automatic crash reporting and
  [enable opt-in reporting](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#enable-reporting) for your users. Note that, by
  default, Crashlytics automatically collects crash reports for all your
  app's users.

## Add custom keys

Custom keys help you get the specific state of your app leading up to a crash.
You can associate arbitrary key-value pairs with your crash reports, then use
the custom keys to search and filter crash reports in the Firebase console.

- In the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics), you can search for issues
  that match a custom key.

- When you're reviewing a specific issue in the console, you can view the
  associated custom keys for each event (*Keys* subtab) and even filter the
  events by custom keys (*Filter* menu at the top of the page).

> [!NOTE]
> **Note:** Crashlytics supports a maximum of 64 key-value pairs. After you reach this threshold, additional values are not saved. Each key-value pair can be up to 1 kB in size.

Use the `setCustomKey` instance method to set key-value pairs. Note that
`setCustomKey` is overloaded for the `value` parameter to accept any primitive
or `String` argument. Here are some examples:

### Kotlin

```kotlin
val crashlytics = Firebase.crashlytics
crashlytics.setCustomKeys {
    key("my_string_key", "foo") // String value
    key("my_bool_key", true) // boolean value
    key("my_double_key", 1.0) // double value
    key("my_float_key", 1.0f) // float value
    key("my_int_key", 1) // int value
}
```

### Java

```java
FirebaseCrashlytics crashlytics = FirebaseCrashlytics.getInstance();

crashlytics.setCustomKey("my_string_key", "foo" /* string value */);

crashlytics.setCustomKey("my_bool_key", true /* boolean value */);

crashlytics.setCustomKey("my_double_key", 1.0 /* double value */);

crashlytics.setCustomKey("my_float_key", 1.0f /* float value */);

crashlytics.setCustomKey("my_int_key", 1 /* int value */);
```

You can also modify the value of an existing key by calling the key and setting
it to a different value. For example:

### Kotlin

```kotlin
val crashlytics = Firebase.crashlytics
crashlytics.setCustomKeys {
    key("current_level", 3)
    key("last_UI_action", "logged_in")
}
```

### Java

```java
FirebaseCrashlytics crashlytics = FirebaseCrashlytics.getInstance();

crashlytics.setCustomKey("current_level", 3);
crashlytics.setCustomKey("last_UI_action", "logged_in");
```

Add key-value pairs in bulk by passing an instance of `CustomKeysAndValues` to
the `setCustomKeys` instance method:

### Kotlin

For Kotlin, the existing functionality is simpler than using the
`CustomKeysAndValues` builder.

```kotlin
crashlytics.setCustomKeys {
  key("str_key", "hello")
  key("bool_key", true)
  key("int_key", 1)
  key("long_key", 1L)
  key("float_key", 1.0f)
  key("double_key", 1.0)
}
```

### Java

```java
CustomKeysAndValues keysAndValues = new CustomKeysAndValues.Builder()
.putString("string key", "string value")
.putString("string key 2", "string  value 2")
.putBoolean("boolean key", True)
.putBoolean("boolean key 2", False)
.putFloat("float key", 1.01)
.putFloat("float key 2", 2.02)
.build();

FirebaseCrashlytics.getInstance().setCustomKeys(keysAndValues);
```

## Add custom log messages

To give yourself more context for the events leading up to a crash, you can add
custom Crashlytics logs to your app. Crashlytics associates the logs
with your crash data and displays them in the Crashlytics page of the
[Firebase console](https://console.firebase.google.com/project/_/crashlytics), under the **Logs** tab.

> [!NOTE]
> **Note:** To avoid slowing down your app, Crashlytics limits logs to 64kB and deletes older log entries when a session's logs go over that limit.

Use `log` to help pinpoint issues. For example:

### Kotlin

```kotlin
Firebase.crashlytics.log("message")
```

### Java

```java
FirebaseCrashlytics.getInstance().log("message");
```

## Set user identifiers

To diagnose an issue, it's often helpful to know which of your users experienced
a given crash. Crashlytics includes a way to anonymously identify users in
your crash reports.

To add user IDs to your reports, assign each user a unique identifier in the
form of an ID number, token, or hashed value:

### Kotlin

```kotlin
Firebase.crashlytics.setUserId("user123456789")
```

### Java

```java
FirebaseCrashlytics.getInstance().setUserId("user123456789");
```

If you ever need to clear a user identifier after you set it, reset the value to
a blank string. Clearing a user identifier does not remove existing
Crashlytics records. If you need to delete records associated with a user
ID, [contact Firebase support](https://firebase.google.com/support/troubleshooter/contact).

## *(Android NDK only)* Add metadata to NDK crash reports

You can optionally include the `crashlytics.h` header in your C++ code to add
metadata to NDK crash reports, such as [custom keys](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-keys),
[custom logs](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#add-logs),
[user identifiers](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports#set-user-ids). All these options are described on
this page above.

`crashlytics.h` is available as a header-only C++ library in the
[Firebase Android SDK GitHub Repository](https://github.com/firebase/firebase-android-sdk/blob/master/firebase-crashlytics-ndk/src/main/jni/libcrashlytics/include/crashlytics/external/crashlytics.h).

Read the comments in the header file for instructions on using the NDK C++ APIs.

### Include GWP-ASan reports to debug memory corruption issues

Crashlytics can help you debug crashes caused by native memory errors by
collecting GWP-ASan reports. These memory-related errors can be associated with
memory corruption within your app, which is the leading cause of app security
vulnerabilities.

- You can view this data in a new "Memory stack traces" tab when you click
  into an issue's details in the
  [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics).

- You can also use the new "GWP-ASan report" signal and filter to quickly view
  all issues with this data.

You can get GWP-ASan memory reports if you
[explicitly enable GWP-ASan](https://developer.android.com/ndk/guides/gwp-asan#opt-in)
in your app and use the Crashlytics SDK for NDK v18.3.6+ (Firebase BoM
v31.3.0+). You can test your GWP-ASan setup using the
[example native code in the Android documentation](https://developer.android.com/ndk/guides/gwp-asan#example).

## Report non-fatal exceptions

In addition to automatically reporting your app's crashes, Crashlytics lets
you record non-fatal exceptions and sends them to you the next time your app
launches.

> [!NOTE]
> **Note:** Crashlytics only stores the most recent eight recorded exceptions. If your app throws more than eight exceptions, older exceptions are lost.

Use the `recordException` method to record non-fatal exceptions in your app's
`catch` blocks. For example:

### Kotlin

```kotlin
try {
    methodThatThrows()
} catch (e: Exception) {
    Firebase.crashlytics.recordException(e)
    // handle your exception here
}
```

### Java

```java
try {
    methodThatThrows();
} catch (Exception e) {
    FirebaseCrashlytics.getInstance().recordException(e);
    // handle your exception here
}
```

Additionally, you can also attach custom keys to the specific non-fatal
exception. For example:

### Kotlin

```kotlin
try {
    methodThatThrows()
} catch (e: Exception) {
    Firebase.crashlytics.recordException(e) {
        key("string key", "string value")
        key("boolean key", true)
        key("float key", Float.MAX_VALUE)
    }
    // handle your exception here
}
```

### Java

```java
try {
    methodThatThrows();
} catch (Exception e) {
    CustomKeysAndValues keysAndValues = new CustomKeysAndValues.Builder()
            .putString("string key", "string value")
            .putBoolean("boolean key", true)
            .putFloat("float key", Float.MAX_VALUE)
            .build();
    FirebaseCrashlytics.getInstance().recordException(e, keysAndValues);
    // handle your exception here
}
```

> [!WARNING]
> **Warning:** Avoid including a unique value (for example, a user ID or a timestamp) in your exception message; use a custom key instead. Adding values directly can result in several issues and may cause Crashlytics to limit reporting errors in your app.

All recorded exceptions appear as non-fatal issues in the Firebase console.
The issue summary contains all the state information you normally get from
crashes, along with breakdowns by Android version and hardware device.

Crashlytics processes exceptions on a dedicated background thread to
minimize the performance impact to your app. To reduce your users' network
traffic, Crashlytics batches logged exceptions together and sends them the
next time the app launches.

## Get breadcrumb logs

Breadcrumb logs give you a better understanding of the interactions that a user
had with your app leading up to a crash, non-fatal, or ANR event. These logs can
be helpful when trying to reproduce and debug an issue.

Breadcrumb logs are powered by Google Analytics, so to get breadcrumb logs, you
need to
[enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
for your Firebase project and
[add the Firebase SDK for Google Analytics](https://firebase.google.com/docs/analytics/get-started#add-sdk)
to your app. Once these requirements are met, breadcrumb logs are automatically
included with an event's data within the **Logs** tab when you view the details
of an issue.

The Analytics SDK
[automatically logs the `screen_view` event](https://firebase.google.com/docs/analytics/screenviews)
which enables the breadcrumb logs to show a list of screens viewed before the
crash, non-fatal, or ANR event. A `screen_view` breadcrumb log contains a
`firebase_screen_class` parameter.

Breadcrumb logs are also populated with any
[custom events](https://firebase.google.com/docs/analytics/events) that you manually log within the user's
session, including the event's parameter data. This data can help show a series
of user actions leading up to a crash, non-fatal, or ANR event.

Note that you can
[control the collection and use of Google Analytics data](https://firebase.google.com/docs/analytics/configure-data-collection),
which includes the data that populates breadcrumb logs.

## Enable opt-in reporting

> [!CAUTION]
> If you enable opt-in reporting by disabling automatic reporting, you will reduce the accuracy of your app's event count and crash-free metrics, which makes them less reflective of the overall stability of your app. [Learn more.](https://firebase.google.com/docs/crashlytics/crash-free-metrics#impact-of-data-collection-settings)

By default, Crashlytics automatically collects crash reports for all your
app's users. To give users more control over the data they send, you can enable
opt-in reporting by disabling automatic reporting and only sending data to
Crashlytics when you choose to in your code.

1. In the `application` block of your `AndroidManifest.xml` file, add
   a `meta-data` tag to turn off automatic collection:

       <meta-data
           android:name="firebase_crashlytics_collection_enabled"
           android:value="false" />

2. Enable collection for select users by calling the Crashlytics data
   collection override at runtime. The override value persists across all
   subsequent launches of your app so Crashlytics can automatically collect
   reports for that user.

   ### Kotlin

   ```kotlin
   Firebase.crashlytics.setCrashlyticsCollectionEnabled(true)
   ```

   ### Java

   ```java
   FirebaseCrashlytics.getInstance().setCrashlyticsCollectionEnabled(true);
   ```

   If the user later opts-out of data collection, you can pass `false` as the
   override value, which will apply the next time the user launches the app and
   will persist across all subsequent launches for that user.

> [!NOTE]
> **Note:** When data collection is disabled for a user, Crashlytics will store crash information locally on the device. If data collection is subsequently enabled, any crash information stored on the device will be sent to Crashlytics for processing.

## Manage Crash Insights data

Crash Insights helps you resolve issues by comparing your anonymized stack
traces to traces from other Firebase apps and letting you know if your issue is
part of a larger trend. For many issues, Crash Insights even provides resources
to help you debug the crash.

Crash Insights uses aggregated crash data to identify common stability trends.
If you'd prefer not to share your app's data, you can opt-out of Crash Insights
from the **Crash Insights** menu at the top of your Crashlytics issue list
in the [Firebase console](https://console.firebase.google.com/project/_/crashlytics).

> [!NOTE]
> **Note:** Disabling data sharing also removes insights on your issues. Changes may take up to 24 hours to take effect.

## Next steps

- [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud) for advanced analysis and features, like querying your data, building custom dashboards, and setting up custom alerts.