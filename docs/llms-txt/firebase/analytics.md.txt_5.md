# Source: https://firebase.google.com/docs/analytics.md.txt

# Google Analytics

Google Analytics is an app measurement
solution, available at no charge, that provides insight on app usage and user engagement.
[Video](https://www.youtube.com/watch?v=8iZpH7O6zXo) At the heart of Firebase is Google Analytics, an unlimited analytics solution available at no charge. Analytics integrates across Firebase features and provides you with unlimited reporting for up to 500 distinct events that you can define using the Firebase SDK. Analytics reports help you understand clearly how your users behave, which enables you to make informed decisions regarding app marketing and performance optimizations.

<br />

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/analytics/ios/get-started)
[Android](https://firebase.google.com/docs/analytics/android/get-started)
[Web](https://firebase.google.com/docs/analytics/web/get-started)
[Flutter](https://firebase.google.com/docs/analytics/flutter/get-started)

[Unity](https://firebase.google.com/docs/analytics/unity/get-started)
[C++](https://firebase.google.com/docs/analytics/cpp/get-started)

## Key capabilities

|---|---|
| Unlimited Reporting | Analytics provides unlimited reporting on up to 500 distinct events. |
| Audience Segmentation | Custom audiences can be defined in the Firebase console based on device data, custom events, or user properties. These audiences can be used with other Firebase features when targeting new features or notification messages. |

## How does it work?

Google Analytics helps you understand how people use your web, Apple, or
Android app. The SDK automatically captures a number of events and user
properties and also allows you to define your own custom events to measure the
things that uniquely matter to your business. Once the data is captured, it's
available in a dashboard through the Firebase console. This dashboard
provides detailed insights about your data --- from summary data such as
active users and demographics, to more detailed data such as identifying your
most purchased items.

Analytics also integrates with a number of other Firebase
features. For example, it automatically logs events that correspond to
notification messages sent via the Notifications composer and provides reporting on the
impact of each campaign.

Analytics helps you understand how your users behave, so you can
make informed decisions about how to market your app. See the performance of
your campaigns across organic and paid channels to understand which methods are
most effective at driving high-value users. If you need to perform custom
analysis or join your data with other sources you can link your
Analytics data to BigQuery, which allows for more complex analysis like
querying large data sets and joining multiple data sources.

## Integrations with other services

|---|---|
| BigQuery | [Link your Firebase app to BigQuery](https://support.google.com/firebase/answer/6318765) where you can perform custom analysis on your entire Analytics dataset and import other data sources. |
| Crashlytics | Analytics logs events for each crash so you can get a sense of the rate of crashes for different versions or regions, allowing you to gain insight into which users are impacted. You can also create audiences for users who have experienced multiple crashes and respond with notification messages directed at that audience. |
| FCM | Analytics automatically logs events that correspond to notification messages sent via the Notifications composer and supports reporting on the impact of each campaign. |
| Firebase Remote Config | Use Analytics audience definitions to change the behavior and appearance of your app for different audiences without distributing multiple versions of your app. |
| Google Tag Manager | Integrating [Google Tag Manager](https://developers.google.com/tag-manager/) alongside Google Analytics enables you to manage your Analytics implementation remotely from a web interface after your app has been distributed. |

## Implementation path

|---|---|---|
|   | Connect your app to Firebase | Getting started with Analytics is easy. Just add the Firebase SDK to your new or existing app, and data collection begins automatically. You can view analytics data in the Firebase console within hours. |
|   | Log custom data | You can use Analytics to log custom events that make sense for your app, like E-Commerce purchases or achievements. |
|   | Create audiences | You can define the audiences that matter to you in the Firebase console. |
|   | Target audiences | Use your custom audiences to target messages, promotions, or new app features using other Firebase features, such as FCM, and Remote Config. |

## Next steps

- Add Google Analytics to your [web](https://firebase.google.com/docs/analytics/web/get-started), [Apple](https://firebase.google.com/docs/analytics/ios/get-started), [Android](https://firebase.google.com/docs/analytics/android/get-started), or [Flutter](https://firebase.google.com/docs/analytics/flutter/get-started) app.
- Download [sample code](https://firebase.google.com/docs/samples).