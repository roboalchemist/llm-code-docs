# Source: https://firebase.google.com/docs/analytics/flutter/get-started.md.txt

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

1. [Install `firebase_core`](https://firebase.google.com/docs/flutter/setup) and add the initialization code to your app if you haven't already.
2. Add your app to your Firebase project in the [Firebase console](https://console.firebase.google.com).

## Add the Analytics SDK to your app

1. From the root of your Flutter project, run the following command to install
   the plugin:

       flutter pub add firebase_analytics

2. Once complete, rebuild your Flutter application:

       flutter run

3. Once installed, you can access the `firebase_analytics`
   plugin by importing it in your Dart code:

       import 'package:firebase_analytics/firebase_analytics.dart';

4. Create a new Firebase Analytics instance by accessing the
   `instance` property on
   `FirebaseAnalytics`:

       FirebaseAnalytics analytics = FirebaseAnalytics.instance;

## Start logging events

After you have created a `FirebaseAnalytics` instance, you can begin to log
events with the library's `log`- methods.

Certain events are
[recommended for all apps](https://support.google.com/analytics/answer/9267735);
others are recommended for specific business types or verticals. You should send
recommended events along with their prescribed parameters, to ensure maximum
available detail in your reports and to benefit from future features and
integrations as they become available. This section demonstrates logging a
predefined event, for more information on logging events, see
[Log events](https://firebase.google.com/docs/analytics/flutter/events).

The following code logs a checkout event:

    await FirebaseAnalytics.instance
      .logBeginCheckout(
        value: 10.0,
        currency: 'USD',
        items: [
          AnalyticsEventItem(
            itemName: 'Socks',
            itemId: 'xjw73ndnw',
            price: '10.0'
          ),
        ],
        coupon: '10PERCENTOFF'
      );

## Next steps

- Use the [DebugView](https://firebase.google.com/docs/analytics/debugview) to verify your events.
- Explore your data in the [Firebase console](https://console.firebase.google.com/project/_/analytics/).
- Explore the guides on [events](https://firebase.google.com/docs/analytics/flutter/events) and [user properties](https://firebase.google.com/docs/analytics/flutter/user-properties).
- Learn how to export your data to [BigQuery](https://support.google.com/firebase/answer/7030014).