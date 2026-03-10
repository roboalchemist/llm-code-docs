# Source: https://firebase.google.com/docs/perf-mon/flutter/get-started.md.txt

This quickstart describes how to set up Firebase Performance Monitoring to help
you to gain insight into the performance characteristics of your Flutter apps.

## Before you begin

If you haven't already,
[configure and initialize Firebase](https://firebase.google.com/docs/flutter/setup) in your Flutter
project.

## **Step 1**: Add Performance Monitoring to your app

1. From the root directory of your Flutter project, run the following
   command to install the Performance Monitoring Flutter plugin:

       flutter pub add firebase_performance

2. From the root directory of your Flutter project, run the following command:

       flutterfire configure

   Running this command ensures that your Flutter app's Firebase configuration
   is up-to-date and, for Android, adds the required Performance Monitoring
   Gradle plugin to your app.
3. Once complete, rebuild your Flutter project:

       flutter run

After you've added the Performance Monitoring SDK, Firebase automatically starts collecting
data related to your app's lifecycle (like
[app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces)), and
data for [HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces).

On Flutter, automatic screen rendering performance monitoring is not possible
for individual Flutter screens. A single view controller encapsulates your
entire Flutter application natively so the underlying native Firebase SDK is
not aware of screen transitions.

> [!NOTE]
> **Note:** When you add Performance Monitoring to your app, the Remote Config SDK is included as a dependency. If you already use Remote Config, you won't see any difference. However, if you're new to Remote Config, explore the [Remote Config documentation](https://firebase.google.com/docs/remote-config) to learn more about the various features you'll be able to access in your app.

## **Step 2**: Generate performance events for initial data display

Firebase starts processing the events when you successfully add the SDK to your
app. If you're still developing locally, interact with your app to generate
events for initial data collection and processing.

> [!NOTE]
> **Note:** The Performance Monitoring SDK batches events locally then sends them to Firebase periodically (every 30 seconds) or when the app comes back to foreground. So, there's a delay between an app interaction and when Firebase receives the event information from your app.

1. Continue to develop your app using a simulator or test device.

2. Generate events by switching your app between background and foreground
   several times, interacting with your app by navigating across screens,
   and/or triggering network requests.

3. Go to the [*Performance* dashboard](https://console.firebase.google.com/project/_/performance)
   of the Firebase console. You should see your initial data display within
   a few minutes.

   If you don't see a display of your initial data, review the [troubleshooting
   tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#sdk-detected-no-data).

## **Step 3** : *(Optional)* View log messages for performance events

1. Check your log messages for any error messages.

   Performance Monitoring tags its log messages with the following tags so that
   you can filter your log messages:
   - iOS+: `Firebase/Performance`
   - Android: `FirebasePerformance`
2. Check for the following types of logs which indicate that Performance Monitoring is
   logging performance events:

   - `Logging trace metric: TRACE_NAME, FIREBASE_PERFORMANCE_CONSOLE_URL`
   - `Logging network request trace: URL`
3. Click on the URL to view your data in the Firebase console. It may take a few
   moments for the data to update in the dashboard.

## **Step 4** : *(Optional)* Add custom monitoring for specific code

To monitor performance data associated with specific code in your app, you can
instrument [**custom code traces**](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=flutter).

With a custom code trace, you can measure how long it takes your app to complete
a specific task or set of tasks, such as loading a set of images or querying
your database. The default metric for a custom code trace is its duration, but
you can also add custom metrics, such as cache hits and memory warnings.

In your code, you define the beginning and the end of a custom code trace (and
add any desired custom metrics) using the API provided by the Performance Monitoring SDK.

Visit [Add monitoring for specific code](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=flutter)
to learn more about these features and how to add them to your app.

## **Step 5**: Deploy your app then review results

After you've validated Performance Monitoring using the an emulator and one or more
test devices, you can deploy the updated version of your app to your users.

You can monitor performance data in the
[*Performance* dashboard](https://console.firebase.google.com/project/_/performance)
of the Firebase console.

## Next steps

- Learn more about data automatically collected by Performance Monitoring:

  - Data related to your app's lifecycle, like [app start time](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces)
  - Data for [HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces) issued by your app
- [View, track, and filter](https://firebase.google.com/docs/perf-mon/console) your
  performance data in the Firebase console.

- Add monitoring for specific tasks or workflows in your app by
  [instrumenting custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=flutter).

- [Use attributes to filter performance data](https://firebase.google.com/docs/perf-mon/attributes).