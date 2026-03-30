# Source: https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports) [Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports) [Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports) |

<br />

In the Crashlytics dashboard, you can click into an issue and get a detailed
event report. You can customize those reports to help you better understand
what's happening in your app and the circumstances around events reported to
Crashlytics.

- Report [caught exceptions](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#report-caught-exceptions) and
  [uncaught exceptions](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#report-uncaught-exceptions) to Crashlytics.

- Include [GWP-ASan reports](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#gwp-asan-unity) to debug memory corruption issues.

- Instrument your app to log [custom keys](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-keys),
  [custom log messages](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#add-logs), and [user identifiers](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#set-user-ids).

- Automatically get [breadcrumb logs](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#get-breadcrumb-logs) if your app uses the
  Firebase SDK for Google Analytics. These logs give you visibility into
  user actions leading up to a Crashlytics-collected event in your app.

- Turn off automatic crash reporting and
  [enable opt-in reporting](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports#enable-reporting) for your users. Note that, by
  default, Crashlytics automatically collects crash reports for all your
  app's users.

## Report exceptions

### Report caught exceptions

If you have exceptions that are expected, you can have the Crashlytics SDK
report them as ***non-fatal events***. These events are logged on device and
then sent along with the next fatal event report or when the end-user restarts
the game.

You can log exceptions in C# using the following method:

```c#
Crashlytics.LogException(Exception ex);
```

You can log expected exceptions in your game's try/catch blocks:

```c#
try {
    myMethodThatThrows();
} catch (Exception e) {
   Crashlytics.LogException(e);
   // handle your exception here!
}
```

### Report uncaught exceptions

For ***uncaught exceptions*** that don't crash your game (for example, uncaught
C# exceptions in game logic), you can have the Crashlytics SDK report them
as ***fatal events*** by setting the
`Crashlytics.ReportUncaughtExceptionsAsFatal` property to `true` where you
[initialize Crashlytics in your Unity project](https://firebase.google.com/docs/crashlytics/unity/get-started#initialize-crashlytics)
.
These events are reported to Crashlytics in real-time without the need for
the end-user to restart the game.

Reporting these uncaught exceptions as fatal events means that they'll count in
your crash-free user statistics and towards velocity alerts.

> [!NOTE]
> **Note:** This feature to report uncaught exceptions as fatal events is only available when using the Firebase Crashlytics Unity SDK v10.4.0 and later.

Note that ***native crashes*** are always reported as ***fatal events***. These
events are logged on device and then sent along when the end-user restarts the
game.

```c#
void Start() {
    // Since there is no try-block surrounding this call, if an exception is thrown,
    // it is considered unexpected.
    // Setting `Crashlytics.ReportUncaughtExceptionsAsFatal = true`
    // will ensure that such cases are reported as fatals.
    thirdPartyMethodThatMayThrow();
}
```

## Include GWP-ASan reports to debug memory corruption issues

For Android apps that use IL2CPP, Crashlytics can help you debug crashes
caused by native memory errors by collecting GWP-ASan reports. These
memory-related errors can be associated with memory corruption within your app,
which is the leading cause of app security vulnerabilities.

- You can view this data in a new "Memory stack traces" tab when you click
  into an issue's details in the
  [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics).

- You can also use the new "GWP-ASan report" signal and filter to quickly view
  all issues with this data.

You can get GWP-ASan memory reports if your app
uses the latest Crashlytics SDK for Unity (v10.7.0+) and has
[GWP-ASan explicitly enabled](https://developer.android.com/ndk/guides/gwp-asan#opt-in)
(requires you to
[modify your Android App Manifest](https://docs.unity3d.com/Manual/android-manifest.html)).
If you have any C++ code in your app, you can test your GWP-ASan setup using the
[example native code in the Android documentation](https://developer.android.com/ndk/guides/gwp-asan#example).

## Add custom keys

Custom keys help you get the specific state of your app leading up to a crash.
You can associate arbitrary key-value pairs with your crash reports, then use
the custom keys to search and filter crash reports in the Firebase console.

- In the [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics), you can search for issues that match a custom key.
- When you're reviewing a specific issue in the console, you can view the associated custom keys for each event (*Keys* subtab) and even filter the events by custom keys (*Filter* menu at the top of the page).

> [!NOTE]
> **Note:** Crashlytics supports a maximum of 64 key-value pairs. After you reach this threshold, additional values are not saved. Each key-value pair can be up to 1 kB in size.

When called multiple times, new values for existing keys will update the value,
and only the most current value is captured when a crash is recorded.

```c#
Crashlytics.SetCustomKey(string key, string value);
```

## Add custom log messages

Logged messages are associated with your crash data and are visible in the
Firebase Crashlytics dashboard when viewing a specific crash.

```c#
Crashlytics.Log(string message);
```

## Set user identifiers

You can use an ID number, token, or hashed value to uniquely identify the
end-user of your application without disclosing or transmitting any of their
personal information. You can also clear the value by setting it to a blank
string. This value is displayed in the Firebase Crashlytics dashboard when
viewing a specific crash.

```c#
Crashlytics.SetUserId(string identifier);
```

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
app's users. You can give users more control over the data they send by letting
them opt-in to reporting crashes.

To disable automatic collection only for selected users, call the
Crashlytics data collection override at runtime. The override value persists
across all subsequent launches of your app so Crashlytics can automatically
collect reports for that user.

```c#
Crashlytics.IsCrashlyticsCollectionEnabled = true
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