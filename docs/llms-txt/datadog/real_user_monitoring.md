# Source: https://docs.datadoghq.com/real_user_monitoring.md

---
title: RUM & Session Replay
description: >-
  Visualize, observe, and analyze the performance of your front-end applications
  as seen by your users.
breadcrumbs: Docs > RUM & Session Replay
source_url: https://docs.datadoghq.com/index.html
---

# RUM & Session Replay

{% callout %}
##### Join an enablement webinar session

Discover how to create custom user actions tailored to specific business needs, enabling precise tracking of user behavior.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=RUM)
{% /callout %}

## What is Real User Monitoring?{% #what-is-real-user-monitoring %}

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/performance-summary-browser.ba22e1a210fc9f66622ac32f70f42634.png?auto=format"
   alt="RUM Dashboard" /%}

Datadog's *Real User Monitoring (RUM)* gives you end-to-end visibility into the real-time activity and experience of individual users. RUM solves four types of use cases for monitoring web and mobile applications:

- **Performance**: Track the performance of web pages, mobile application screens, user actions, network requests, and your frontend code.
- **Error Management**: Monitor the ongoing bugs and issues and track them over time and versions.
- **Analytics / Usage**: Understand who is using your application (country, device, OS), monitor individual users journeys, and analyze how users interact with your application (most common page visited, clicks, interactions, and feature usage).
- **Support**: Retrieve all of the information related to one user session to troubleshoot an issue (session duration, pages visited, interactions, resources loaded, and errors).

### Session definition{% #session-definition %}

A user session is a user journey on your web or mobile application. A session includes all related navigation events (RUM Views), user actions (RUM Actions), network requests (RUM Resources), crashes and errors (RUM Errors), and other events and signals that collectively produce a faithful representation of the user experience.

A RUM session can last up to 4 hours, and expires after 15 minutes of inactivity. If the user interacts with the application after either limit, a new session starts automatically.

### Technical limitations{% #technical-limitations %}

| Property                                   | Limitation               |
| ------------------------------------------ | ------------------------ |
| Maximum duration of a session              | 4 hours                  |
| Timeout of a session                       | 15 minutes of inactivity |
| Maximum number of events per session       | 10 million               |
| Maximum number of attributes per event     | 1,000                    |
| Maximum attribute depth per event          | 20                       |
| Maximum event size                         | 1 MB                     |
| Maximum intake payload size                | 5 MB                     |
| Maximum source maps and mapping files size | 500 MB per file          |
| Maximum dSYM files size                    | 2 GB per file            |
| Maximum delay at ingestion                 | 24 hours                 |

If an event goes beyond any of the technical limitations listed above, it is rejected by the Datadog intake.

## What is Session Replay?{% #what-is-session-replay %}

Datadog's *Session Replay* allows you to capture and visually replay the web browsing experience of your users.

Combined with RUM performance data, Session Replay is beneficial for error identification, reproduction, and resolution, and provides insights into your web application's usage patterns and design pitfalls.

## Get started{% #get-started %}

Select an application type to start collecting RUM data:

- [browser](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/)
- [android](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android/setup)
- [ios](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/ios/setup)
- [react native](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/react_native/setup)
- [flutter](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/flutter/setup)
- [android tv](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android/setup)
- [tv OS](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/ios/setup)
- [Roku](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/roku/setup)
- [rum-unity](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/unity/setup)
- [Kotlin Multiplatform](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/kotlin_multiplatform/setup)

### Capabilities and platform support{% #capabilities-and-platform-support %}

**Note**: The Datadog Flutter SDK is not supported for MacOS, Windows, or Linux.

The following table shows which RUM capabilities are supported on each platform:

| Feature                                          | Browser | Android | iOS | Flutter | React Native | Roku | KMP                                       | Unity                                                             | Notes                                                                                                                                         |
| ------------------------------------------------ | ------- | ------- | --- | ------- | ------------ | ---- | ----------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Send logs to Datadog                             | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | yes                                                               |
| Distributed tracing of network requests          | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | yes                                                               | - **Roku** is only able to track some types of HTTP requests.- **Unity** uses a wrapper around `UnityWebRequest` to perform request tracking. |
| Track Views and Actions (RUM)                    | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | yes                                                               | - All actions tracked in **Flutter Web** are recorded as `custom`.- **Roku** and **Unity** support only manual action tracking.               |
| Feature Flags tracking and release tracking      | yes     | yes     | yes | yes     | yes          | yes  | yes                                       |
| Error tracking and source mapping                | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | yes                                                               | Only partially supported for **React Native**.                                                                                                |
| Crash tracking, symbolication, and deobfuscation | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | yes                                                               |
| Stop sessions (Kiosk Monitoring)                 | yes     | yes     | yes | yes     | yes          | yes  | yes                                       |
| Track Events in WebViews                         | yes     | yes     | yes | yes     | yes          |
| Monitor platform-specific vitals                 | yes     | yes     | yes | yes     | yes          | yes  |
| Global context/attribute tracking in Logs        | yes     | yes     | yes | yes     | yes          | yes  | yes                                       |
| Client side tracing                              | yes     | yes     |
| Session Replay                                   | yes     | yes     | yes | yes     | yes          | yes  | **Flutter** Session Replay is in Preview. |
| Frustration signals                              | yes     | yes     | yes | yes     | yes          | yes  | yes                                       | Only partially supported for all **mobile** and **Roku** devices. |

## Supported endpoints for SDK domains{% #supported-endpoints-for-sdk-domains %}

All Datadog SDKs traffic is transmitted over SSL (default 443) to the following domains:

| Site    | Site URL                                   |
| ------- | ------------------------------------------ |
| US1     | `https://browser-intake-datadoghq.com`     |
| US3     | `https://browser-intake-us3-datadoghq.com` |
| US5     | `https://browser-intake-us5-datadoghq.com` |
| EU1     | `https://browser-intake-datadoghq.eu`      |
| US1-FED | `https://browser-intake-ddog-gov.com`      |
| AP1     | `https://browser-intake-ap1-datadoghq.com` |
| AP2     | `https://browser-intake-ap2-datadoghq.com` |

## Explore Datadog RUM{% #explore-datadog-rum %}

Access RUM by navigating to [**Digital Experience > Performance Summary**](https://app.datadoghq.com/rum/performance-monitoring).

Select an application from the top navigation, or follow the setup instructions for [browser](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/setup/) or [mobile](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/) to add your first application.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/rum-performance-application-selector.c4338a455c1dd29329e37c255ef59b73.png?auto=format"
   alt="Select a RUM application" /%}

**Tip**: To open RUM from Datadog's global search, press `Cmd`/`Ctrl` + `K` and search for `real user monitoring`.

## Performance monitoring summary{% #performance-monitoring-summary %}

| Browser Performance Summary                                                                                                                                                                                                                     | Mobile Performance Summary                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {% image
     source="https://datadog-docs.imgix.net/images/real_user_monitoring/performance-summary-browser.ba22e1a210fc9f66622ac32f70f42634.png?auto=format"
     alt="RUM Performance Monitoring summary page for a browser application" /%} | {% image
     source="https://datadog-docs.imgix.net/images/real_user_monitoring/performance-summary-mobile-2.753130f48e10dd97d00bbef53c8e51b1.png?auto=format"
     alt="RUM Performance Monitoring summary page for a mobile application" /%} |

The [RUM Performance Monitoring summary](https://app.datadoghq.com/rum/performance-monitoring) page provides relevant and actionable insights for both web and mobile applications. You have a tailored experience for each platform that helps you:

- **Focus on key datapoints** by platform, such as the UI latency for web or mobile crashes
- **Monitor application health** through familiar KPIs, such as Core Web Vitals for web apps or hang rate for iOS, to assess app reliability
- **Dive into investigations directly** from interactive widgets without leaving the page

For **web apps**, use the search bar to filter data, identify slow pages, and follow the UI to the [RUM Optimization Inspect](https://app.datadoghq.com/rum/optimization/inspect) page.

For **mobile apps**, review recent crashes at the bottom of the page and use the [Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking/) side panel for troubleshooting.

### Out-of-the-box dashboards{% #out-of-the-box-dashboards %}

Analyze information about your user sessions, performance, mobile applications, frustration signals, network resources, and errors collected automatically with [out-of-the-box RUM dashboards](https://docs.datadoghq.com/real_user_monitoring/platform/dashboards/).

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/rum-out-of-the-box-dashboard.0e6c161abcc5f3b87cf472e785740a17.png?auto=format"
   alt="RUM dashboard" /%}

### RUM Explorer and visualizations{% #rum-explorer-and-visualizations %}

View user sessions in segments, such as checking when latency impacts your premium customers, with [visualizations](https://docs.datadoghq.com/real_user_monitoring/explorer/visualize/). Explore data, save views, and create [monitors](https://docs.datadoghq.com/monitors/types/real_user_monitoring/) on your customized searches.

{% video
   url="https://datadog-docs.imgix.net/images/real_user_monitoring/explorer/analytics/rum_analytics.mp4" /%}

### Integration with logs, APM, and profiler{% #integration-with-logs-apm-and-profiler %}

View your [backend traces, logs, and infrastructure metrics](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/) down to the exact line of code impacting your application performance, corresponding to user experiences and reported issues.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/connect_rum_and_traces/rum_apm_logs-2.37d045abf254c97fe68ea022b0693385.png?auto=format"
   alt="RUM and APM" /%}

### Error tracking and crash reporting{% #error-tracking-and-crash-reporting %}

Get automated alerts on outliers and groups of errors, timeouts, and crashes to significantly reduce your MTTR with [Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking/).

{% video
   url="https://datadog-docs.imgix.net/images/real_user_monitoring/error_tracking/errors_rum.mp4" /%}

### Web and mobile vitals{% #web-and-mobile-vitals %}

View performance scores and telemetry for [browser applications](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/monitoring_page_performance/#event-timings-and-core-web-vitals) such as Core Web Vitals and Mobile Vitals for [iOS and tvOS](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/ios/mobile_vitals/) or [Android and Android TV applications](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android/mobile_vitals/).

### Web view tracking{% #web-view-tracking %}

Collect information from your native web applications and explore hybrid views with Web View Tracking for [iOS and tvOS](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/ios/web_view_tracking/) or [Android and Android TV](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android/web_view_tracking/).

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/webview_tracking/webview_tracking_light.9f5964c2c9aa95f9bccb790a1fd51bf3.png?auto=format"
   alt="Web Views captured in a user session in the RUM Explorer" /%}

## Explore Datadog Session Replay{% #explore-datadog-session-replay %}

### Session replays{% #session-replays %}

Watch [browser recordings](https://docs.datadoghq.com/session_replay/browser/) of real users interacting with your website and set [privacy controls](https://docs.datadoghq.com/session_replay/browser/privacy_options/) for your organization.

### Developer tools{% #developer-tools %}

Access triggered logs, errors, and performance information when troubleshooting application issues using [Browser Dev Tools](https://docs.datadoghq.com/session_replay/browser/developer_tools/).

## Permissions{% #permissions %}

By default, all users can change an application's RUM configuration.

Use granular access controls to limit the [roles](https://docs.datadoghq.com/account_management/rbac/) that may edit a particular application's RUM configuration:

1. While viewing an application's RUM configuration, click on the **Edit application** button at the top of the screen. A dropdown appears.
1. Select **Manage App Permissions**.
1. Click **Restrict Access**.
1. The dialog box updates to show that members of your organization have **Viewer** access by default.
1. Use the dropdown to select one or more roles, teams, or users that may edit the notebook.
1. Click **Add**.
1. The dialog box updates to show that the role you selected has the **Editor** permission.
1. Click **Save**.

**Note:** To maintain your edit access to the application, the system requires you to include at least one role that you are a member of before saving.

You must have edit access to restore general access to a restricted application. Complete the following steps:

1. While viewing an application's RUM configuration, click on the **Edit application** button at the top of the screen. A dropdown appears.
1. Select **Manage App Permissions**.
1. Click **Restore Full Access**.
1. Click **Save**.

## Further reading{% #further-reading %}

- [From performance to impact: Bridging frontend teams through shared context](https://www.datadoghq.com/blog/rum-product-analytics-bridging-teams)
- [Check out the latest Datadog RUM releases! (App login required)](https://app.datadoghq.com/release-notes?category=Real%20User%20Monitoring)
- [Join an interactive session to gain insights through Real User Monitoring](https://dtdg.co/fe)
- [Introducing Datadog Real User Monitoring](https://www.datadoghq.com/blog/real-user-monitoring-with-datadog/)
- [Improve mobile user experience with Datadog Mobile Real User Monitoring](https://www.datadoghq.com/blog/datadog-mobile-rum/)
- [Best practices for monitoring mobile app performance](https://www.datadoghq.com/blog/mobile-monitoring-best-practices/)
- [Make sense of application issues with Datadog Error Tracking](https://www.datadoghq.com/blog/error-tracking/)
- [Unify APM and RUM data for full-stack visibility](https://www.datadoghq.com/blog/unify-apm-rum-datadog/)
- [Use geomaps to visualize your app data by location](https://www.datadoghq.com/blog/datadog-geomaps/)
- [Get better RUM data with our custom React components](https://www.datadoghq.com/blog/datadog-rum-react-components/#tune-up-your-react-data-collection)
- [Monitor your hybrid mobile applications with Datadog](https://www.datadoghq.com/blog/hybrid-app-monitoring/)
- [How Datadog's Technical Solutions team uses RUM, Session Replay, and Error Tracking to resolve customer issues](https://www.datadoghq.com/blog/how-datadogs-tech-solutions-team-rum-session-replay/)
- [Best practices for monitoring static web applications](https://www.datadoghq.com/blog/static-web-application-monitoring-best-practices/)
- [RUM Browser Data Collected](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/data_collected/)
- [Best practices for monitoring progressive web applications](https://www.datadoghq.com/blog/progressive-web-application-monitoring/)
