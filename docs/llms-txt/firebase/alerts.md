# Source: https://firebase.google.com/docs/perf-mon/alerts.md.txt

<br />

UsePerformance Monitoringalerts to notify project members if code changes or network requests are degrading the performance of your app.

You can set up and customize alerts for your app, which notify you when the performance of an event crosses a set threshold.

## What triggers an alert?

An alert is triggered when a metric for your app crosses a threshold that you define for a specified percentile (if applicable) in theFirebaseconsole. Alerts are triggered only if your app uses a[real-time compatible SDK version](https://firebase.google.com/docs/perf-mon/troubleshooting#faq-real-time-data).  

### app start time

When you configure an alert for app start time, the alert is triggered if all of the following conditions are true:

- Firebase recorded at least100 samplesof the`_app_start`trace for the latest version of your app in the last hour.
- The duration of the`_app_start`trace exceeded the app's defined threshold during the last hour and for the configured percentile.
- There was no alert previously raised for the same threshold in the latest version of your app.

| **Note:** By default, every app is opted in for the app start time alert, and the default threshold is5 secondsat the 90th percentile.

### custom code traces

When you configure an alert for a custom code trace metric, the alert is triggered if all of the following conditions are true:

- Firebase recorded at least100 samplesof the custom code trace for the latest version of your app in the last hour.
- The duration of the trace exceeded the app's defined threshold during the last hour and for the configured percentile.
- (For iOS+ and Android only) There was no alert previously raised for the same threshold in the latest version of your app.
- (For web only) There was no alert previously raised for the same threshold in the past3 days.

### network requests

When you configure an alert for a network request metric, the alert is triggered if all of the following conditions are true:

- Firebase recorded at least100 samplesthat matched to the URL pattern across all versions of your app in the last hour.
- The metric's aggregated value crossed the defined threshold during the last hour:
  - *response time*: the aggregated value exceeded the set threshold for the configured percentile
  - *success rate*: (for iOS+/Android only) the aggregated value went below the set threshold across all users
- There was no alert previously raised for the same threshold in the past3 days.

### screen rendering

When you configure an alert for a screen rendering metric, the alert is triggered if all of the following conditions are true:

- Firebase recorded at least100 samplessamples of screen rendering for the latest version of your app in the last hour.
- The metric's aggregated value crossed the defined threshold during the last hour:
  - *frozen frames*: the aggregated value exceeded the set threshold
  - *slow frames*: the aggregated value exceeded the set threshold
- There was no alert previously raised for the same threshold in the latest version of your app.

### page loads

When you configure an alert for a page load metric, the alert is triggered if all of the following conditions are true:

- Firebase recorded at least100 samplesof the page loading for your app in the last hour.
- The metric's aggregated value crossed the defined threshold during the last hour and for the configured percentile:
  - *first input delay*: the aggregated value exceeded the set threshold and the configured percentile
  - *first contentful paint*: the aggregated value exceeded the set threshold and the configured percentile
  - *first paint*: the aggregated value exceeded the set threshold and the configured percentile
- There was no alert previously raised for the same threshold in the past3 days.

Learn more about[configuring alerts](https://firebase.google.com/docs/perf-mon/alerts#configure),[default percentiles](https://firebase.google.com/docs/perf-mon/console#track-key-metrics), and[best practices](https://firebase.google.com/docs/perf-mon/alerts#best-practices)for setting up alerts for specific types of traces and metrics.

Alerts for other performance metrics or for Firebase-console configured integrations with Slack, Jira, or PagerDuty are not available forPerformance Monitoringalerts.

## Receive alerts

### Get default alerts

By default, Firebase can sendPerformance Monitoringalerts via email.

To receivePerformance Monitoringalerts via this default mechanism, you must have the`firebaseperformance.config.update`permission. The following roles include this required permission by default:

- [Firebase Performance Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#performance)
- [Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles)
- [Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products)
- Project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic)

Alerts and their settings are project-wide. This means that, by default, every project member will get an email when a performance alert is triggered. Alerts are only sent to project members with the[required permissions to receive alerts](https://support.google.com/firebase/answer/7276542#required-permissions-roles)and to individual email addresses (not to groupings of accounts like Google groups or Google Workspace accounts).

#### Turn on/off alerts for your own account

For your own account, you can turn on/offPerformance Monitoringalerts without affecting other project members. Note that you still need the required permissions to receive alerts.

To turnPerformance Monitoringalerts on or off, follow these steps:

1. In theFirebaseconsole, in the top right-corner, go tonotifications*Firebase alerts*.
2. Then, go tosettings*Settings*and set your account preference forPerformance Monitoringalerts.

### Set up advanced alerting to third-party services

You can also sendPerformance Monitoringalerts to your team's preferred notification channel, usingCloud Functions for Firebase. For example, you can write a function that captures an alert event for slow app start time and posts the alert information to a third-party service, like Discord, Slack, or Jira.
| **Note:** To use advanced alerting capabilities, your Firebase project needs to use the[Blaze pricing plan](https://firebase.google.com/pricing).

To set up advanced alerting capabilities usingCloud Functions for Firebase, follow these steps:

1. [Set up Cloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started), which includes the following tasks:

   1. Set up a development environment for Node.js or Python.
   2. Install and sign into theFirebaseCLI.
   3. InitializeCloud Functions for Firebaseusing theFirebaseCLI.
2. [Write and deploy a function](https://firebase.google.com/docs/functions/alert-events)that captures an alert event fromPerformance Monitoringand handles the event payload (for example, posts the alert information in a message on Discord).

To learn about all the performance alert events that you can capture, go to the reference documentation for[Performance Monitoring alerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance).

## Automatic removal of invalid alerts

Performance Monitoringvalidates alerts to ensure that data is valid and that alerts are in active use. Alerts are considered valid if one of the following is true:

- The alert is created for a Resource ID for whichPerformance Monitoringreceived data in the last 90 days.
- The alert was created recently for a custom URL pattern. After you create a custom URL pattern and set up an alert, you have 90 days to send data for that pattern. If no data is sent within the 90-day time period,Performance Monitoringremoves that alert. For more information about custom URL patterns, see[Aggregate data under customer URL patterns](https://firebase.google.com/docs/perf-mon/custom-url-patterns#custom-url-patterns).

If either of these conditions is not met,Performance Monitoringremoves the alert.

## Configure an alert

To configurePerformance Monitoringalerts, you must have the`firebaseperformance.config.update`permission. The following roles include this required permission by default:[Firebase Performance Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-product#performance),[Firebase Quality Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-category#quality_roles),[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products), and project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

If you haven't already done so, add the latestPerformance MonitoringSDK to your app. For more information, see get started guides for the[web](https://firebase.google.com/docs/perf-mon/get-started-web),[Android](https://firebase.google.com/docs/perf-mon/get-started-android),[Apple](https://firebase.google.com/docs/perf-mon/get-started-ios), and[Flutter](https://firebase.google.com/docs/perf-mon/flutter/get-started)platforms.
| **Important:** Alerts and their configurations are project-wide, which means that any change affects the alert configuration for*all* project members who receivePerformance Monitoringalerts.

In each of your registered apps, use the[Traces table](https://firebase.google.com/docs/perf-mon/alerts#configure-traces-table)or the[Dashboard report card](https://firebase.google.com/docs/perf-mon/alerts#configure-dashboard-report-card)to configure an alert for each metric that you want to monitor. Each app can have a different set of alerts, each with a different threshold (or have no alerts at all).

### Configure an alert in the Traces table

1. Go to thePerformance Monitoring[*Dashboard*tab](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, and then select the app for which you want to configure an alert.

2. Scroll down to the Traces table at the bottom of the screen.

3. Select the tab of the trace type for which you want to set an alert, and then find the applicable row.

   | **Note:** The`_app_start`trace is located in the Custom traces tab.
4. At the far right of the row, open the Overflow Menu (more_vert) and select**Alert settings**.

5. Follow the on-screen instructions to set the alert threshold and the percentile (if applicable) for the app, or to turn on/off the alert. The default percentiles are 90th for Android and iOS, and 75th for Web. To learn more about default percentiles, see[Track key metrics in your dashboard](https://firebase.google.com/docs/perf-mon/console#track-key-metrics).

   | **Note:** Percentile configuration is not applicable to success rate, frozen frames, or slow frames because those metrics are percentages.

### Configure an alert in the Dashboard report card

1. Go to thePerformance Monitoring[*Dashboard*tab](https://console.firebase.google.com/project/_/performance)in theFirebaseconsole, and then select the app for which you want to configure an alert.

2. In the Report card tab, locate the metric card for which you want to configure an alert.

3. In the desired metric card, open the Overflow Menu (more_vert) and select**Alert settings**.

4. Follow the on-screen instructions to set the alert threshold and the percentile (if applicable) for the app, or to turn on/off the alert. The default percentiles are 90th for Android and iOS, and 75th for Web. To learn more about default percentiles, see[Track key metrics in your dashboard](https://firebase.google.com/docs/perf-mon/console#track-key-metrics).

   | **Note:** Percentile configuration is not applicable to success rate, frozen frames, and slow frames because those metrics are percentages.

## Best practices for setting a performance alert

### Network requests

Firebase aggregates the data from similar network requests under URL patterns, which can be either of the following:

- User-defined patterns, which are called[custom URL patterns](https://firebase.google.com/docs/perf-mon/network-traces#custom-url-patterns).

- Firebase-derived patterns, which are called[automatic URL patterns](https://firebase.google.com/docs/perf-mon/network-traces#automatic-url-patterns).  
  These patterns may change over time based on your app's latest usage behavior.

#### Set up alerts for your custom URL patterns

We recommend setting up alerts for any custom URL patterns that you've configured. Since Firebase attempts to match a request to a custom URL pattern first, similar requests are more consistently mapped to the same URL pattern. This makes alerts for a custom URL pattern more meaningful and effective for your team, because you've already identified that specific pattern of requests as important to your app.

#### Set up alerts for automatic URL patterns

When setting up an alert for an automatic URL pattern, ensure that the automatic URL pattern has stabilized for a few days. Keep in mind that automatic URL patterns may change over time, and alert configurations do not carry over to new URL patterns. This could result in incorrect or missing alerts for the patterns you care about. You can also consider creating a custom URL pattern to ensure that this pattern is stable.

### Web page loads

To learn recommended thresholds for measuring web metrics, see the[Core Web Vitals](https://web.dev/articles/vitals/#core-web-vitals)documentation.

### Screen renderings

To ensure an optimal app experience, user sessions should be free of slow and frozen frames.Performance Monitoringrecommends that you set up alerts for frozen frames greater than 1% and that you set up alerts for slow frames exceeding 5%. You will find that these values are present as the default settings during performance alert configuration. To learn more about excessive slow or frozen frames and other app performance best practices, see the[Google Play guidance](https://support.google.com/googleplay/android-developer/answer/9844486#slow_frames&zippy=%2Cexcessive-slow-frames%2Cexcessive-frozen-frames).