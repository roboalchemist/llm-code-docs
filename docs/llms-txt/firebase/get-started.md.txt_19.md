# Source: https://firebase.google.com/docs/analytics/web/get-started.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/get-started) [Android](https://firebase.google.com/docs/analytics/android/get-started) [Web](https://firebase.google.com/docs/analytics/web/get-started) [Flutter](https://firebase.google.com/docs/analytics/flutter/get-started) [Unity](https://firebase.google.com/docs/analytics/unity/get-started) [C++](https://firebase.google.com/docs/analytics/cpp/get-started) |

This quickstart shows you how to add Google Analytics to your app and begin
logging events.

Google Analytics collects usage and behavior data for your web app. The
SDK logs two primary types of information:

- **Events**: What is happening in your app, such as user actions, system
  events, or errors.

- **User properties**: Attributes you define to describe segments of your user
  base, such as language preference or geographic location.

Analytics automatically logs some
[events](https://support.google.com/analytics/answer/9234069) and
[user properties](https://support.google.com/analytics/answer/9268042);
you don't need to add any code to enable them.

## Before you begin

If you haven't already,
[add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup) and make sure that
Google Analytics is enabled in your Firebase project:

- If you're creating a new Firebase project, enable Google Analytics
  during the project creation workflow.

- If you're using an existing Firebase project that doesn't have
  Google Analytics enabled, go to the
  [*Integrations*](https://console.firebase.google.com/project/_/settings/integrations)
  tab of your \> *Project settings* to enable it.

> [!WARNING]
> **Warning:** Any Firebase project created before July 31, 2019 must be upgraded to the full [Google Analytics 4 experience](https://support.google.com/analytics/answer/10089681) if it hasn't already. (Banners display in the Analytics dashboard if an upgrade is required.) The associated Terms of Service must be [accepted by February 15, 2022](https://support.google.com/analytics/answer/10960488) to ensure data collection continues. See the Support FAQ on the upgrade for help [finding project Owners](https://firebase.google.com/support/faq#analytics-upgrade-tos).

When you enable Google Analytics in your project, your Firebase web apps
are linked to Google Analytics data streams associated with an
[App + Web property](https://developers.google.com/analytics/devguides/collection/app-web/tag-guide).

## Add the Analytics SDK to your app

Depending on how your web application is hosted, your configuration may be
handled automatically or you may need to update your
[Firebase configuration object](https://firebase.google.com/docs/projects/learn-more#config-files-objects).
If your web app already uses Google Analytics, you may need to do additional
setup described in [Use Firebase with existing gtag.js tagging](https://firebase.google.com/docs/analytics/web/get-started#firebase-gtag).

1. Check that your Firebase config object in your code contains
   `measurementId`. This ID is automatically created when you enable
   Analytics in your Firebase project and register a web app, and it's
   required to use Analytics.

   > [!NOTE]
   > **Note:** For apps using the **Firebase JavaScript SDK v7.20.0 and later** , Firebase dynamically fetches the `measurementId` when your app initializes Analytics. Having this ID in your config object is optional, but it does serve as a fallback in the rare case that the dynamic fetch fails.

   - **If your app uses Firebase Hosting *and* uses
     [reserved URLs](https://firebase.google.com/docs/hosting/reserved-urls) for the Firebase SDKs**:

     Firebase automatically handles configuring your application. To complete
     setup, add the scripts from the ***Your apps*** card in your
     [Project settings](https://console.firebase.google.com/project/_/settings/general/)
     to the \<body\> tag of your app, if you haven't already.
   - **If your app does not use reserved URLs** :
     **If you're working with an existing web app** , update the Firebase config
     object in your code to ensure the `measurementId` field is present. The
     config object should look similar to the following example:

         // For Firebase JavaScript SDK v7.20.0 and later, `measurementId` is an optional field
         const firebaseConfig = {
           apiKey: "API_KEY",
           authDomain: "PROJECT_ID.firebaseapp.com",
           databaseURL: "https://PROJECT_ID.firebaseio.com",
           projectId: "PROJECT_ID",
           storageBucket: "`PROJECT_ID.firebasestorage.app`",
           messagingSenderId: "SENDER_ID",
           appId: "APP_ID",
           measurementId: "G-GA_MEASUREMENT_ID"
         };

     1. If you haven't already, [install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize). 2. Add the Analytics JS SDK and initialize Analytics: \* { Web }

     > [!NOTE]
     > [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

     ```
       import { initializeApp } from "firebase/app";
       import { getAnalytics } from "firebase/analytics";

       // TODO: Replace the following with your app's Firebase project configuration
       // See: https://firebase.google.com/docs/web/learn-more#config-object
       const firebaseConfig = {
           // ...
       };

       // Initialize Firebase
       const app = initializeApp(firebaseConfig);

       
       // Initialize Analytics and get a reference to the service
       const analytics = getAnalytics(app);
       
       
     ```
     \* { Web }

     > [!NOTE]
     > [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

     ```
       import firebase from "firebase/compat/app";
       import "firebase/compat/analytics";

       // TODO: Replace the following with your app's Firebase project configuration
       // See: https://firebase.google.com/docs/web/learn-more#config-object
       const firebaseConfig = {
           // ...
       };

       // Initialize Firebase
       firebase.initializeApp(firebaseConfig);

       
       // Initialize Analytics and get a reference to the service
       const analytics = firebase.analytics();
       
     ```

### Use Firebase with existing gtag.js tagging

If you previously had Google Analytics running in your app using the
[gtag.js snippet](https://developers.google.com/analytics/devguides/collection/gtagjs/),
your app may require additional setup if you plan to do one of the following:

- Add Google Analytics calls from Firebase to the page but also plan to continue using `gtag()` calls directly on the same page.
- Want to use the same measurement ID between both direct `gtag()` calls and Google Analytics data sent to Firebase.

To ensure your events are available for use by all Firebase services, complete
the following additional setup steps:

- Remove the line `gtag('config', 'GA_MEASUREMENT_ID');` where the `GA_MEASUREMENT_ID` is the `measurementId` of your Firebase web app. If you have other IDs for other Analytics properties on the page, you don't need to remove their config line.
- Make sure you call `firebase.analytics()` before you send any events with `gtag()`.

Otherwise, events sent to that ID with `gtag()` calls won't be associated
with Firebase and will not be available for targeting in other
Firebase services.

## Start logging events

After you have initialized the
[Analytics service](https://firebase.google.com/docs/reference/js/analytics), you can
begin to log events with the
[`logEvent()`](https://firebase.google.com/docs/reference/js/analytics#logevent)
method.

Certain events are
[recommended for all apps](https://support.google.com/firebase/answer/6317498);
others are recommended for specific business types or verticals. You should send
suggested events along with their prescribed parameters, to ensure maximum
available detail in your reports and to benefit from future features and
integrations as they become available. This section demonstrates logging a
predefined event, for more information on logging events, see
[Log events](https://firebase.google.com/docs/analytics/web/events).

The following example demonstrates how to log a recommended event to indicate a
user has received a notification in your app:

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

const analytics = getAnalytics();
logEvent(analytics, 'notification_received');
```

### Web

```javascript
firebase.analytics().logEvent('notification_received');
```

## Next steps

- Understand [each Analytics report](https://firebase.google.com/docs/analytics/reports).
- Use the [DebugView](https://firebase.google.com/docs/analytics/debugview) to verify your events.
- Explore your data in the [Firebase console](https://console.firebase.google.com/project/_/analytics/).
- Explore the guides on [events](https://firebase.google.com/docs/analytics/web/events) and [user properties.](https://firebase.google.com/docs/analytics/web/user-properties).
- Learn how to export your data to [BigQuery.](https://support.google.com/firebase/answer/7030014)