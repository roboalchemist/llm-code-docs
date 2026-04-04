# Source: https://firebase.google.com/docs/perf-mon/troubleshooting.md.txt

<button value="ios" default="">iOS+</button> <button value="android">Android</button> <button value="web">Web</button>

<br />

This page provides troubleshooting tips for getting started with Performance Monitoring or
using Performance Monitoring features and tooling.

## **First checks for troubleshooting**

The following two checks are general best practices recommended for anyone
before further troubleshooting.

#### 1. Check log messages for performance events

Check your log messages to be sure that the Performance Monitoring SDK is capturing
performance events.

<br />

How to view log messages for performance events

<br />

1. Enable debug logging, as follows:

   1. In Xcode (minimum v16.2), select **Product** \> **Scheme** \> **Edit scheme**.
   2. Select **Run** from the left menu, then select the **Arguments** tab.
   3. In the *Arguments Passed on Launch* section, add `-FIRDebugEnabled`.
2. Check your log messages for any error messages.

3. Performance Monitoring tags its log messages with `Firebase/Performance` so that you
   can filter your log messages.

4. Check for the following types of logs which indicate that Performance Monitoring is
   logging performance events:

   - `Logging trace metric: TRACE_NAME, FIREBASE_PERFORMANCE_CONSOLE_URL`
   - `Logging network request trace: URL`
5. Click on the URL to view your data in the Firebase console. It may take a few
   moments for the data to update in the dashboard.

If your app isn't logging performance events, review the [troubleshooting
tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#app-not-logging-events).

<br />

<br />

#### 2. Check the Firebase Status Dashboard

Check the
[Firebase Status Dashboard](https://status.firebase.google.com/) in case
there is a known outage for Firebase or for Performance Monitoring.

## **Getting started with Performance Monitoring**

If you're getting started with Performance Monitoring
([iOS+](https://firebase.google.com/docs/perf-mon/get-started-ios) \|
[Android](https://firebase.google.com/docs/perf-mon/get-started-android) \|
[Web](https://firebase.google.com/docs/perf-mon/get-started-web)), the following troubleshooting
tips can help with issues that involve Firebase detecting the SDK or displaying
your first performance data in the Firebase console.

<br />

### Added the SDK to app, but console
still says to add SDK

<br />

Firebase can detect if you've successfully added the Performance Monitoring SDK to your app
when it receives event information (like app interactions) from your app.
Usually within 10 minutes of starting your app, the [*Performance*
dashboard](https://console.firebase.google.com/project/_/performance)
of the Firebase console displays an "SDK detected" message. Then, within 30
minutes, the dashboard displays the initial processed data.

If it's been more than 10 minutes since you added the latest version of SDK to
your app, and you're still not seeing any change, [check your log
messages](https://firebase.google.com/docs/perf-mon/troubleshooting#check-logs-for-events) to make sure that Performance Monitoring is logging
events. Try the appropriate troubleshooting steps as described below to
troubleshoot a delayed SDK detection message.

<br />

**App is logging events: troubleshooting
steps**

<br />

> [!NOTE]
> **Note:** The Performance Monitoring SDK batches events locally then sends them to Firebase periodically or when the app comes back to foreground. So, there's a delay between an app interaction and when Firebase receives the event information from your app.

1. If you're still developing locally, try generating more events for data
   collection:

   1. Continue to develop your app using a simulator or test device.

   2. Generate events by switching your app between background and foreground
      several times, interacting with your app by navigating across screens,
      and/or triggering network requests.

2. Make sure that your [Firebase configuration
   file](https://firebase.google.com/docs/ios/setup#add-config-file) (`Google-Service-Info.plist`) is
   correctly added to your app and that you haven't modified the file.
   Specifically, check the following:

   - The config file name isn't appended with additional characters, like
     `(2)`.

   - The config file is in the root of your XCode project and added to the
     correct targets.

   - The Firebase Apple App ID (`GOOGLE_APP_ID`) listed in the config file is
     correct for your app. Find your Firebase App ID in the *Your apps* card
     of your [**Project
     settings**](https://console.firebase.google.com/project/_/settings/general/).

   If anything seems wrong with the config file in your app, try the following:
   1. Delete the config file that you currently have in your app.

   2. Follow [these instructions](https://firebase.google.com/docs/ios/setup#add-config-file) to download
      a new config file and add it to your Apple app.

3. If the SDK is logging events and everything seems to be set up correctly,
   but you're still not seeing the SDK detection message or processed data
   (after 2 hours), [contact Firebase Support](https://firebase.google.com/docs/perf-mon/troubleshooting#contact-support).

<br />

<br />

<br />

**App is *not* logging events:
troubleshooting steps**

<br />

1. Make sure that the [Performance Monitoring SDK is ***not***
   disabled](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=ios#disable-during-build)
   through either of the following flags in your `Info.plist` file:

   - `firebase_performance_collection_enabled`
   - `firebase_performance_collection_deactivated`
2. Make sure that Performance Monitoring is ***not*** disabled at runtime
   ([Swift](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Performance#isdatacollectionenabled)
   \|
   [Obj-C](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#datacollectionenabled)).

3. If you can't find anything that's disabled in your app,
   [contact Firebase Support](https://firebase.google.com/docs/perf-mon/troubleshooting#contact-support).

<br />

<br />

<br />

<br />

<br />

### Console says the SDK is
detected, but no data is displayed

<br />

Performance Monitoring processes performance event data before displaying it in the
[*Performance* dashboard](https://console.firebase.google.com/project/_/performance).

If it's been **more than 24 hours since the "SDK detected" message appeared** ,
and you're still not seeing data, then check the
[Firebase Status Dashboard](https://status.firebase.google.com/) in case there is a
known outage. If there is no outage,
[contact Firebase Support](https://firebase.google.com/docs/perf-mon/troubleshooting#contact-support).

<br />

<br />

## **General troubleshooting**

If you've successfully added the SDK and are using Performance Monitoring in your app, the
following troubleshooting tips can help with general issues that involve
Performance Monitoring features and tooling.

<br />

### App is not logging
performance events

<br />

If you're not seeing [log messages for performance
events](https://firebase.google.com/docs/perf-mon/troubleshooting#check-logs-for-events), try the following troubleshooting steps:

1. Make sure that the [Performance Monitoring SDK is ***not***
   disabled](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=ios#disable-during-build)
   through either of the following flags in your `Info.plist` file:

   - `firebase_performance_collection_enabled`
   - `firebase_performance_collection_deactivated`
2. Make sure that Performance Monitoring is ***not*** disabled at runtime
   ([Swift](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Performance#isdatacollectionenabled)
   \|
   [Obj-C](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#datacollectionenabled)).

3. If you can't find anything that's disabled in your app,
   [contact Firebase Support](https://firebase.google.com/docs/perf-mon/troubleshooting#contact-support).

<br />

<br />

<br />

### Performance dashboard is
missing screen trace data

<br />

If you're missing data for screen rendering traces, try the following
troubleshooting steps:

<br />

<br />

<br />

### Performance dashboard is
missing custom trace data

<br />

Are you seeing performance data for automatically collected traces *but not for
custom code traces*? Try the following troubleshooting steps:

1. Check the setup of custom code traces instrumented via the
   [Trace API](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=ios#add-custom-traces),
   especially the following:


   - Names for custom code traces and custom metrics must meet the following requirements: no leading or trailing whitespace, no leading underscore (`_`) character, and max length is 32 characters.
   - All traces must be started and stopped. Any trace that is not started, not stopped, or stopped before started will not be logged.

   <br />

2. [Check your log messages](https://firebase.google.com/docs/perf-mon/troubleshooting#check-logs-for-events) to make sure that
   Performance Monitoring is logging expected custom code traces.

3. If Performance Monitoring is logging events, but no data displays after 24 hours,
   [contact Firebase Support](https://firebase.google.com/docs/perf-mon/troubleshooting#contact-support).

<br />

<br />

<br />

### Performance dashboard
is missing network request data

<br />

If you're missing network request data, try the following troubleshooting steps:

1. Check for network library incompatibility. Performance Monitoring [automatically
   collects metrics for network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=ios)
   that use the following networking libraries:

   - For Swift: URLSession and URLConnection
   - For Objective-C: NSURLSession and NSURLConnection

   Note that you can [add custom monitoring for network
   requests](https://firebase.google.com/docs/perf-mon/custom-network-traces?platform=ios).
2. Be aware of the following:

   - Depending on the behavior of your code and networking libraries used by
     your code, Performance Monitoring might only report on network requests that are
     completed. This means that HTTP/S connections that are left open might not
     be reported.

   - Performance Monitoring does not report on network requests with invalid
     `Content-Type` headers. However, network requests without the
     `Content-Type` headers will still be accepted.

<br />

<br />

<br />

### Network request data are not aggregating as expected

<br />

Learn more about [how Performance Monitoring aggregates network request
data](https://firebase.google.com/docs/perf-mon/network-traces#url-patterns) under URL patterns.

You can also try out [custom URL
patterns](https://firebase.google.com/docs/perf-mon/custom-url-patterns)!

<br />

<br />

## **FAQ**

<button value="ios" default="">iOS+</button> <button value="android">Android</button> <button value="web">Web</button>

<br />

#### What happened to Top Issues in the Performance card on Project home?

<br />

We replaced **Top Issues** with **Recent Alerts** as a follow-up to our
recent introduction of alerts, which automatically notify you when the
thresholds you set are crossed. [Issues are now deprecated](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#faq-issues-tab)
and replaced by alerts.

The apps selector at the top of the Performance card filters the alert
entries under **Recent Alerts**. Only the three most recent alerts for the
app(s) selected are displayed.

To learn more about alerts, see
[Set up alerts for performance issues](https://firebase.google.com/docs/perf-mon/alerts).

<br />

<br />

<br />

#### What happened to the ability to set thresholds for issues in the console?

<br />

Performance Monitoring supports [alerts](https://firebase.google.com/docs/perf-mon/alerts) for metrics that exceed
defined thresholds. To avoid confusion with these configurable thresholds for
performance metrics, we removed the ability to configure thresholds for
[issues](https://firebase.google.com/docs/perf-mon/issue-management).

<br />

<br />

<br />

#### What happened to the Details and Metrics information in the Firebase console?

<br />

We replaced the Details and Metrics pages with a newly redesigned, centralized
user interface (UI) to improve how you troubleshoot issues. This new
troubleshooting UI offers the same core functionality that Details and
Metrics offered. To learn more about troubleshooting, see
[View more data for a specific trace](https://firebase.google.com/docs/perf-mon/console#view_more_data_for_a_specific_trace).

<br />

<br />

<br />

#### Why is the number of samples not what I expect?

<br />

Performance Monitoring collects performance data from your app's user devices. If your
application has many users or if the app generates a large amount of performance
activity, Performance Monitoring might limit data collection to a subset of devices to
reduce the number of processed events. These limits are high enough so that,
even with fewer events, the metric values are still representative of
your user's app experience.

To manage the volume of data that we collect, Performance Monitoring uses the following
sampling options:

- **On-device rate limiting**: To prevent a device from sending sudden bursts of
  traces, we limit the number of code and network request traces sent from a
  device to 300 events every 10 mins. This approach protects the device from
  looped instrumentations that can send large amounts of performance data, and
  it prevents a single device from skewing the performance measurements.

- **Dynamic sampling** : Performance Monitoring collects a limited number of code traces and
  network request traces per app daily across all app users. A dynamic sampling
  rate is fetched on devices (using Firebase Remote Config) to determine
  whether a random device should capture and send traces. A device that is not
  selected for sampling does not send any events. The dynamic sampling rate is
  app-specific and adjusts to ensure that the overall volume of collected data
  remains below the limit.

  Projects that enabled BigQuery integration receive a higher limit for the
  number of network request traces.

  User sessions send additional, detailed data from a user's device, requiring
  more resources to capture and send the data. To minimize the impact of user
  sessions, Performance Monitoring might also restrict the number of sessions.
- **Server-side rate limiting** : To ensure that apps don't exceed the sampling
  limit, Performance Monitoring might use server-side sampling to drop some events
  received from devices. Although this type of limiting doesn't change the
  effectiveness of our metrics, it may cause minor pattern shifts, including the
  following:

  - The number of traces can differ from the number of times that a piece of code was executed.
  - Traces that are closely coupled in code may each have a different number of samples.

> [!NOTE]
> **Note:** Specific sampling limits and their application might change as Performance Monitoring evolves.

<br />

<br />

<br />

#### What happened to the *Issues* tab in the console?

<br />

We replaced the Issues tab with the introduction of Alerts, which
automatically notifies you when the thresholds you set are exceeded. You no
longer need to manually check the Firebase console to determine the status of
a threshold. To learn about Alerts, see [Set up alerts for performance issues](https://firebase.google.com/docs/perf-mon/alerts).

<br />

<br />

<br />

#### What happened to the *On Device* and *Network* tabs in the console?
How do I view the traces that were on those pages?

<br />

We've redesigned the Performance Monitoring section of the Firebase console so that the
*Dashboard* tab displays your key metrics and all your traces in one space. As
part of the redesign, we removed the *On device* and *Network* pages.

The traces table at the bottom of the *Dashboard* tab has all the same
information that the *On device* and *Network* tabs displayed, but with some
added features, including the ability to sort your traces by the percentage
change for a specific metric. To view *all* the metrics and data for a specific
trace, click the trace name in the traces table.

View your traces in the following subtabs of the traces table:

- Network request traces (both out-of-the-box and custom) --- *Network requests* subtab
- Custom code traces --- *Custom traces* subtab
- App start, app-in-foreground, app-in-background traces --- *Custom traces* subtab
- Screen rendering traces --- *Screen rendering* subtab
- Page load traces --- *Page load* subtab

For details about the traces table and viewing metrics and data, visit the
console overview page
([iOS+](https://firebase.google.com/docs/perf-mon/console?platform=ios#view-traces-and-data) \|
[Android](https://firebase.google.com/docs/perf-mon/console?platform=android#view-traces-and-data) \|
[Web](https://firebase.google.com/docs/perf-mon/console?platform=web#view-traces-and-data)).

<br />

<br />

<br />

#### Why is the number of slow and frozen frames not what I expected?

<br />

Slow rendering frames and frozen frames are calculated with an assumed device
refresh rate of 60Hz. If a device refresh rate is lower than 60Hz, each frame
will have a slower rendering time because fewer frames are rendered per second.
Slower rendering times can cause more slow or frozen frames to be reported
because more frames will be rendered slower or will freeze. However, if a device
refresh rate is higher than 60Hz, each frame will have a faster rendering time.
This can cause fewer slow or frozen frames to be reported. This is a current
limitation in the Performance Monitoring SDK.

<br />

<br />

<br />

#### My Performance Monitoring data is taking longer than expected to be exported to
BigQuery. Is it not real time?

<br />

If you have enabled the BigQuery integration for Firebase Performance Monitoring, your data
will be exported to BigQuery 12 to 24 hours after the end of the day (Pacific
Time).

For example, the data for April 19th will be available in BigQuery on April 20th
between 12:00pm and midnight (all dates and times are Pacific Time).

<br />

<br />

### Near real-time data processing and display

<br />

#### What does "near real-time" performance data mean?

<br />

Firebase Performance Monitoring processes collected performance data as it comes in, which
results in near real-time data display in the Firebase console. Processed
data displays in the console within a few minutes of its collection, hence the
term "near real-time".

To take advantage of near real-time data processing, make sure your app uses a
[real-time compatible SDK
version](https://firebase.google.com/docs/perf-mon/troubleshooting#faq-real-time-compatible-sdk-versions).

<br />

<br />

<br />

#### How do I get near real-time performance data for my app?

<br />

To take advantage of near real-time data processing, you only need to make sure
that your app uses a Performance Monitoring SDK version that's compatible with real-time
data processing.

These are the real-time compatible SDK versions:

- **iOS** --- v7.3.0 or later
- **tvOS** --- v8.9.0 or later
- **Android** --- v19.0.10 or later (or Firebase Android BoM v26.1.0 or later)
- **Web** --- v7.14.0 or later

Note that we always recommend using the latest version of SDK, but any
version listed above will enable Performance Monitoring to process your data in near real
time.

<br />

<br />

<br />

<br />

#### Which versions of the Performance Monitoring SDK are considered real-time compatible?

<br />

These are the SDK versions compatible with real-time data processing:

- **iOS** --- v7.3.0 or later
- **tvOS** --- v8.9.0 or later
- **Android** --- v19.0.10 or later (or Firebase Android BoM v26.1.0 or later)
- **Web** --- v7.14.0 or later

Note that we always recommend using the latest version of SDK, but any
version listed above will enable Performance Monitoring to process your data in near real
time.

<br />

<br />

<br />

<br />

#### What if I don't update my app to use a real-time compatible SDK version?

<br />

If your app doesn't use a real-time compatible SDK version, you will still see
all your app's performance data in the Firebase console. However, the display
of performance data will be delayed by roughly 36 hours from the time of its
collection.

<br />

<br />

<br />

#### I've updated to a real-time compatible SDK version, but some of my users are
still on old versions of my app. Do I continue to see their performance
data in the Firebase console?

<br />

Yes! Regardless of which SDK version an app instance uses, you'll see
performance data from all your users.

However, if you're looking at *recent* data (less than roughly 36 hours old),
then the displayed data is from users of app instances using a real-time
compatible SDK version. The *non-recent* data, though, includes performance data
from all versions of your app.

<br />

<br />

## **Contacting Firebase Support**

If you
[reach out to Firebase Support](https://firebase.google.com/support/troubleshooter/contact),
always include your Firebase App ID. Find your Firebase App ID in the
*Your apps* card of your
[**Project
settings**](https://console.firebase.google.com/project/_/settings/general/).