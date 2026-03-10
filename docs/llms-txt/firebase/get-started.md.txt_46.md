# Source: https://firebase.google.com/docs/analytics/cpp/get-started.md.txt

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
the recommended events that make sense for your app and their
prescribed parameters. This also ensures that you benefit from the latest
Google Analytics features as they become available.

## Before you begin

Before you can use
[Google Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics),
you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and
  configured for Firebase.
- Add the [Firebase C++ SDK](https://firebase.google.com/download/cpp) to your C++ project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your C++
> project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open C++ project (for example, you download
Firebase config files from the console, then move them into your C++ project).

## Create and initialize the firebase app

Before you start, you'll need to create and initialize the firebase App:

### iOS+

Create the firebase app:

```c++
app = ::firebase::App::Create(::firebase::AppOptions());
```

Initialize the Analytics library:

```c++
::firebase::analytics::Initialize(app);
```

<br />

### Android

Create the firebase app, passing the jni environment and a `jobject`
reference to the java activity as arguments:

```c++
app = ::firebase::App::Create(::firebase::AppOptions(), jni_env, activity);
```

Initialize the Analytics library:

```c++
::firebase::analytics::Initialize(app);
```

<br />

## Log events

After you have configured the [`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app) instance, you can
begin to log events with the [`LogEvent()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#logevent) method.

The following example updates the user's score:

```c++
analytics::LogEvent(analytics::kEventPostScore, analytics::kParameterScore, 42);
```

> [!NOTE]
> **Note:** Once the property is registered, it can take up to 24 hours for data collected with the property to be included in reports. When the new data is available, the user property can be used as a report filter.

## Next steps

- See your data refresh periodically in the [Firebase console](https://console.firebase.google.com/).
- Explore the guides on [events](https://firebase.google.com/docs/analytics/cpp/events) and [user properties](https://firebase.google.com/docs/analytics/cpp/properties).