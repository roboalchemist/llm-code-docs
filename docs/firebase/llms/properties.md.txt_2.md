# Source: https://firebase.google.com/docs/analytics/unity/properties.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/user-properties) [Android](https://firebase.google.com/docs/analytics/android/user-properties) [Web](https://firebase.google.com/docs/analytics/web/user-properties) [Flutter](https://firebase.google.com/docs/analytics/flutter/user-properties) [Unity](https://firebase.google.com/docs/analytics/unity/properties) [C++](https://firebase.google.com/docs/analytics/cpp/properties) |

User properties are attributes you define to describe segments of your
user base, such as language preference or geographic location. These can be used
to define [audiences](https://support.google.com/firebase/answer/6317509)
for your app. This guide shows you how to set user properties in your app.

Analytics automatically logs some
[user properties](https://support.google.com/analytics/answer/9268042);
you don't need to add any code to enable them. If you need to collect additional
data, you can set up to 25 different user properties per project. Note that user
property names are case-sensitive and that setting two user properties whose
names differ only in case results in two distinct user properties being logged.

You can't use a small set of user property names reserved by Google:

- **Age**
- **Gender**
- **Interest**

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

## Set user properties

You can set Analytics user properties to describe the users of your app.
You can analyze behaviors of various user segments by applying these
properties as filters to your reports.

Set a user property as follows:

1. [Register](https://support.google.com/analytics/answer/6317519) the property in the **Analytics** tab
   of the [Firebase console](https://console.firebase.google.com/).

2. Add code to set an Analytics user property with the
   [`SetUserProperty()`](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#setuserproperty) method. You can use the name and
   value of your choosing for each property.

The following example shows adding a hypothetical favorite food property, which
assigns the value in the string `mFavoriteFood` to the active user:

```c#
Firebase.Analytics.FirebaseAnalytics.SetUserProperty("favorite_food", "ice cream");
```

> [!NOTE]
> **Note:** After the property is registered, it can take several hours for data collected with the property to be included in reports. When the new data is available, the user property can be used as a report filter.

You can access this data as follows:

1. In the [Firebase console](https://console.firebase.google.com/), open your project.
2. Select **Analytics** from the menu to view the Analytics reporting dashboard.

The **User Properties** tab shows a list of user properties that you have
defined for your app. You can use these properties as a filter on many of the
reports available in Google Analytics. Read more about the
[dashboard](https://support.google.com/analytics/answer/11014767).

> [!NOTE]
> **Note:** Data in the Analytics reporting dashboard refreshes periodically throughout the day.