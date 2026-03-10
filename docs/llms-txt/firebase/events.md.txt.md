# Source: https://firebase.google.com/docs/analytics/unity/events.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/events) [Android](https://firebase.google.com/docs/analytics/android/events) [Web](https://firebase.google.com/docs/analytics/web/events) [Flutter](https://firebase.google.com/docs/analytics/flutter/events) [Unity](https://firebase.google.com/docs/analytics/unity/events) [C++](https://firebase.google.com/docs/analytics/cpp/events) |

Events provide insight on what is happening in your app, such as user
actions, system events, or errors.

Google Analytics automatically logs some
[events](https://support.google.com/analytics/answer/9234069) for
you; you don't need to add any code to receive them. If your app needs to
collect additional data, you can log up to 500 different Analytics event
types in your app. There is no limit on the total volume of events your app
logs. Note that event names are case-sensitive and that logging two events
whose names differ only in case results in two distinct events.

## Before you begin

Before you can use
[Google Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseAnalytics.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Log events

After you have initialized the `Firebase.Analytics.FirebaseAnalytics` module,
you can use it to log events with the [`LogEvent()`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#logevent) method.

To help you get started, the Analytics SDK defines a number of
recommended events that are common among different types of apps, including
retail and ecommerce, travel, and gaming apps. To learn more about these events
and when to use them, see [Recommended events](https://support.google.com/analytics/answer/9267735)
articles in the Google Analytics Help Center.

> [!NOTE]
> **Note:** To get the maximum detail in reports, log the suggested Analytics Events that make sense for your app and their prescribed parameters. This also ensures that you benefit from the latest Google Analytics features as they become available.

You can find implementation details for recommended events in the following
locations:

- Suggested events: see the list of [`Event`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#eventaddpaymentinfo) constants.
- Prescribed parameters: see the list of [`Parameters`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter) constants.

The following example demonstrates how to log a suggested
[`SELECT_CONTENT`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#eventselectcontent) Event:

```c#
    // Log an event with multiple parameters, passed as an array:

Firebase.Analytics.FirebaseAnalytics.LogEvent(
  Firebase.Analytics.FirebaseAnalytics.EventSelectContent,
  new Firebase.Analytics.Parameter(
    Firebase.Analytics.FirebaseAnalytics.ParameterItemId, id),
  new Firebase.Analytics.Parameter(
    Firebase.Analytics.FirebaseAnalytics.ParameterItemName, "name"),
  new Firebase.Analytics.Parameter(
    Firebase.Analytics.FirebaseAnalytics.UserPropertySignUpMethod, "Google"),
  new Firebase.Analytics.Parameter(
    "favorite_food", mFavoriteFood),
  new Firebase.Analytics.Parameter(
    "user_id", mUserId)
);
```

In addition to the prescribed parameters, you can add the following parameters
to any event:

- Custom parameters: Custom parameters are not represented directly in your
  Analytics reports, but they can be used as filters in
  [Audience](https://support.google.com/firebase/answer/6317509) definitions that can be applied to every report. Custom
  parameters are also included in data [exported to BigQuery](https://support.google.com/firebase/answer/6318765) if
  your app is linked to a BigQuery project.

- `VALUE` Parameter: `VALUE` is a general purpose [parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter)
  that is useful for accumulating a key metric that pertains to an
  Analytics Event. Examples include revenue, distance, time and points.

If your application has specific needs not covered by a suggested
Analytics Event type, you can log your own custom Analytics Events
as shown in this example:

```c#
Firebase.Analytics.FirebaseAnalytics.LogEvent("custom_progress_event", "percent", 0.4f);
```

## View events in the log output

### iOS+

Events are logged to the console, and can be viewed while running the app
through XCode.

### Android

You can enable verbose logging in the Android Studio Debug Log, to help
verify that events are being logged properly by the SDK.
This includes both automatically and manually logged events.

You can enable verbose logging with a series of adb commands:

<br />

```
adb shell setprop log.tag.FA VERBOSE
```

```
adb shell setprop log.tag.FA-SVC VERBOSE
```

```
adb logcat -v time -s FA FA-SVC
```

<br />

This command displays your events in the Android Studio logcat, helping
you immediately verify that events are being sent.

## View analytics events in the dashboard

You can view aggregated statistics about your Analytics Events in the
Firebase console dashboards. These dashboards update periodically
throughout the day. For immediate testing, use the logcat output as described in
the previous section.

To access this data in the Firebase console:

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Analytics** from the menu to view the Analytics reporting dashboard.

The **Events** tab shows the event reports that are
automatically created for each distinct type of Analytics event logged by
your app. Read more about the [dashboard](https://support.google.com/analytics/answer/11014767).