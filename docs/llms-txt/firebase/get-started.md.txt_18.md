# Source: https://firebase.google.com/docs/analytics/unity/get-started.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/get-started) [Android](https://firebase.google.com/docs/analytics/android/get-started) [Web](https://firebase.google.com/docs/analytics/web/get-started) [Flutter](https://firebase.google.com/docs/analytics/flutter/get-started) [Unity](https://firebase.google.com/docs/analytics/unity/get-started) [C++](https://firebase.google.com/docs/analytics/cpp/get-started) |

Google Analytics collects usage and behavior data for your app. The SDK
logs two primary types of information:

- **Events:** What is happening in your app, such as user actions, system events, or errors.
- **User properties:** Attributes you define to describe segments of your user base, such as language preference or geographic location.

Analytics automatically logs some
[events](https://support.google.com/analytics/answer/9234069) and
[user properties](https://support.google.com/analytics/answer/9268042);
you don't need to add any code to enable them. If your app needs to collect
additional data, you can set up to 25 different Analytics user properties
and log up to 500 different Analytics event *types* in your app.
There is no limit on the total volume of events your app logs.

To access this data:

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Analytics** from the menu to view the Analytics reporting dashboard.

The **Events** tab shows the event reports that are
automatically created for each distinct type of Analytics event logged by
your app. Read more about the [dashboard](https://support.google.com/analytics/answer/11014767).

To help you get started, the Analytics SDK defines a number of
recommended events that are common among different types of apps, including
retail and ecommerce, travel, and gaming apps. To learn more about these events
and when to use them, see [Recommended events](https://support.google.com/analytics/answer/9267735).
To get the maximum detail in reports, log
the suggested Analytics events that make sense for your app and their
prescribed parameters. This also ensures that you benefit from the latest
Google Analytics features as they become available.

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

You can immediately begin to log events with the
[`LogEvent()`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#logevent) method.

The following example logs events with various types of arguments:

```c#
// Log an event with no parameters.
Firebase.Analytics.FirebaseAnalytics
  .LogEvent(Firebase.Analytics.FirebaseAnalytics.EventLogin);

// Log an event with a float parameter
Firebase.Analytics.FirebaseAnalytics
  .LogEvent("progress", "percent", 0.4f);

// Log an event with an int parameter.
Firebase.Analytics.FirebaseAnalytics
  .LogEvent(
    Firebase.Analytics.FirebaseAnalytics.EventPostScore,
    Firebase.Analytics.FirebaseAnalytics.ParameterScore,
    42
  );

// Log an event with a string parameter.
Firebase.Analytics.FirebaseAnalytics
  .LogEvent(
    Firebase.Analytics.FirebaseAnalytics.EventJoinGroup,
    Firebase.Analytics.FirebaseAnalytics.ParameterGroupId,
    "spoon_welders"
  );

// Log an event with multiple parameters, passed as a struct:
Firebase.Analytics.Parameter[] LevelUpParameters = {
  new Firebase.Analytics.Parameter(
    Firebase.Analytics.FirebaseAnalytics.ParameterLevel, 5),
  new Firebase.Analytics.Parameter(
    Firebase.Analytics.FirebaseAnalytics.ParameterCharacter, "mrspoon"),
  new Firebase.Analytics.Parameter(
    "hit_accuracy", 3.14f)
};
Firebase.Analytics.FirebaseAnalytics.LogEvent(
  Firebase.Analytics.FirebaseAnalytics.EventLevelUp,
  LevelUpParameters);
```

> [!NOTE]
> **Note:** After the property is registered, it can take up to 24 hours for data collected with the property to be included in reports. When the new data is available, the user property can be used as a report filter.

## Next Steps

- See your data refresh periodically in the [Firebase console](https://console.firebase.google.com/).
- Explore the guides on [events](https://firebase.google.com/docs/analytics/unity/events) and [user properties](https://firebase.google.com/docs/analytics/unity/properties).