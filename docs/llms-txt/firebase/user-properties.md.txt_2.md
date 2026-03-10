# Source: https://firebase.google.com/docs/analytics/flutter/user-properties.md.txt

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

Make sure that you've set up your project and can access Analytics as
described in
[Get Started with Analytics](https://firebase.google.com/docs/analytics/flutter/get-started).

## Set user properties

You can set Analytics user properties to describe the users of your app.
You can make use of user properties by creating custom definitions, then using
them to apply comparisons in your reports or as audience evaluation criteria.

To set a user property, follow these steps:

1. Create a custom definition for the user property in the [**Custom Definitions** page](https://console.firebase.google.com/project/_/analytics/userproperty) of *Analytics* in the Firebase console. For more information, see [Custom dimensions and metrics](https://support.google.com/analytics/answer/10075209).
2. Set a user property in your app with the `setUserProperty()` method.

The following example adds a hypothetical favorite food property, which
assigns the value in `favoriteFood` to the active user:

    await FirebaseAnalytics.instance
      .setUserProperty({
        name: 'favorite_food',
        value: favoriteFood,
      });