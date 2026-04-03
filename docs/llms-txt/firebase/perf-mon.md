# Source: https://firebase.google.com/docs/perf-mon.md.txt

# Firebase Performance Monitoring

plat_iosplat_androidplat_webplat_flutter  
Gain insight into your app's performance issues.  
Firebase Performance Monitoringis a service that helps you to gain insight into the performance characteristics of your Apple, Android, and web apps.

<br />

You use thePerformance MonitoringSDK to collect performance data from your app, then review and analyze that data in theFirebaseconsole.Performance Monitoringhelps you to understand in real time where the performance of your app can be improved so that you can use that information to fix performance issues.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/perf-mon/get-started-ios)[Android](https://firebase.google.com/docs/perf-mon/get-started-android)[Web](https://firebase.google.com/docs/perf-mon/get-started-web)[Flutter](https://firebase.google.com/docs/perf-mon/flutter/get-started)

## Key capabilities

|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatically measure app startup time, HTTP network requests, and more | When you integrate thePerformance MonitoringSDK into your app, you don't need to write any code before your app starts automatically monitoring several critical aspects of performance. For native apps, the SDK logs startup time, rendering data by screen, and activity while in the foreground or background. For web apps, the SDK logs aspects like first contentful paint, ability for users to interact with your app, and more. |
| Gain insight into situations where app performance could be improved    | Optimizing the performance of your app can be challenging when you don't know exactly why it is falling short of user expectations. That's whyPerformance Monitoringlets you see performance metrics broken down by[*attributes*](https://firebase.google.com/docs/perf-mon/attributes), like country, device, app version, and OS level.                                                                                                 |
| Customize monitoring for your app                                       | You can instrument[*custom code traces*](https://firebase.google.com/docs/perf-mon/custom-code-traces)to capture your app's performance in specific situations, like when you load a new screen or display a new interactive feature. And, you can create*custom metrics*on these custom code traces to count events that you define (like cache hits) during those traces.                                                               |
| Identify significant changes in app performance                         | Identifying and resolving major app performance issues, like network outages, is vital to the success of your app. Performance Monitoring lets you[set up and customize alerts](https://firebase.google.com/docs/perf-mon/alerts)for the most critical parts of your app so you can see and respond to performance pitfalls -- before they affect your users.                                                                             |

## How does it work?

When you add thePerformance MonitoringSDK, Firebase*automatically*starts collecting data for several common processes in your app, for example:

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | - [App start up time for Apple and Android apps](https://firebase.google.com/docs/perf-mon/app-start-foreground-background-traces) - [Screen rendering for Apple and Android apps](https://firebase.google.com/docs/perf-mon/screen-traces) | - [Page loading for web apps](https://firebase.google.com/docs/perf-mon/page-load-traces) - [Network requests for all types of apps](https://firebase.google.com/docs/perf-mon/network-traces) |

Performance Monitoringuses***traces***to collect data about these processes. A trace is a report that contains data captured between two points in time in your app.

The collected performance data for each trace are called***metrics***and vary depending on the type of trace. For example, when an instance of your app issues a network request, the trace collects metrics that are important for network request monitoring, like response time and payload size.

Each time an instance of your app runs a monitored process, the associated trace also automatically collects***attributes***data for that app instance. For example, if an Android app issues a network request, the trace collects the device, app version, and other attributes for that specific app instance. You can use these attributes to filter your performance data and learn if specific user segments are experiencing issues.

The out-of-the-box traces fromPerformance Monitoringget you started with monitoring your app, but to learn about the performance of specific tasks or flows, try out[instrumenting your own custom traces of code](https://firebase.google.com/docs/perf-mon/custom-code-traces)in your app.

## Implementation path

|---|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Add thePerformance MonitoringSDK to your app                              | You can add thePerformance MonitoringSDK to your app, along with any other Firebase products that you want to use in your app. [Apple platforms](https://firebase.google.com/docs/perf-mon/get-started-ios)\|[Android](https://firebase.google.com/docs/perf-mon/get-started-android)\|[Web](https://firebase.google.com/docs/perf-mon/get-started-web)\|[Flutter](https://firebase.google.com/docs/perf-mon/flutter/get-started) |
|   | *(Optional)* Instrument custom code traces and custom metrics in your app | Using thePerformance MonitoringSDK, you can instrument[custom code traces and custom metrics](https://firebase.google.com/docs/perf-mon/custom-code-traces)to measure specific aspects of your app's performance.                                                                                                                                                                                                                 |
|   | Monitor performance data in the console in real time                      | In the[Firebaseconsole](https://console.firebase.google.com/project/_/performance), you can monitor performance data from your users to learn the specific situations where your app's performance could be improved. You can also break down the performance data by[attributes](https://firebase.google.com/docs/perf-mon/attributes), like app version, country, device, or OS.                                                |

## User data

Performance Monitoringdoes not permanently store any personally identifiable information (such as names, email addresses, or phone numbers). While monitoring HTTP network requests,Performance Monitoringuses URLs (not including URL parameters) to build aggregated and anonymous URL patterns that are eventually persisted and shown in theFirebaseconsole.

For more details, refer to the[Examples of information collected byPerformance Monitoring](https://firebase.google.com/support/privacy#performance-monitoring-collected-info).

## Next steps

- To get started usingPerformance Monitoringin your app, visit:

  - [Get Started withPerformance Monitoringfor Apple platforms](https://firebase.google.com/docs/perf-mon/get-started-ios)
  - [Get Started withPerformance Monitoringfor Android](https://firebase.google.com/docs/perf-mon/get-started-android)
  - [Get Started withPerformance Monitoringfor web](https://firebase.google.com/docs/perf-mon/get-started-web)
  - [Get Started withPerformance Monitoringon Flutter](https://firebase.google.com/docs/perf-mon/flutter/get-started)
- To learn about setting up alerts, see[Set up alerts for performance issues](https://firebase.google.com/docs/perf-mon/alerts).