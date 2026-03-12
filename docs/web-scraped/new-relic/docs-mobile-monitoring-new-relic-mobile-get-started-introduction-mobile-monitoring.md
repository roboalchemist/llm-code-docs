# Source: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/

Title: Introduction to mobile monitoring

URL Source: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/

Markdown Content:
Introduction to mobile monitoring | New Relic Documentation
===============

Opens in a new window Opens an external website Opens an external website in a new window

We use cookies and other tracking technologies - provided by other companies with whom we share your data - to make our website work, improve your experience, and support our marketing efforts, as explained in our [](https://newrelic.com/termsandconditions/privacy)[Privacy Notice](https://newrelic.com/termsandconditions/privacy). By using our website, you agree to our [](https://newrelic.com/termsandconditions/website-terms)[Website Terms of Use](https://newrelic.com/termsandconditions/website-terms). [Privacy Notice](https://newrelic.com/termsandconditions/privacy)

[](https://newrelic.com/)

[Docs](https://docs.newrelic.com/)[Community](https://support.newrelic.com/)[Learn](https://learn.newrelic.com/)

*   [Docs](https://docs.newrelic.com/)
*   [Community](https://support.newrelic.com/)
*   [Learn](https://learn.newrelic.com/)

*   / 
*   [English](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)[Español](https://docs.newrelic.com/es/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)[Français](https://docs.newrelic.com/fr/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)[日本語](https://docs.newrelic.com/jp/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)[한국어](https://docs.newrelic.com/kr/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)[Português](https://docs.newrelic.com/pt/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)   
*   [Log in](https://one.newrelic.com/)[Start now](https://newrelic.com/signup)

[](https://docs.newrelic.com/)

[](https://docs.newrelic.com/)

START HERE

[Get started with New Relic](https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/)

Tutorials and walkthroughs

Guides and best practices

MONITOR YOUR DATA

New Relic Control

AI monitoring

Application performance monitoring

Browser monitoring

eBPF observability

Infrastructure monitoring

Kubernetes monitoring

Log management

Mobile monitoring

[Introduction to mobile monitoring](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/)

Monitor your mobile app

View data in New Relic

Configure mobile monitoring settings

Mobile SDK

[Best practices](https://docs.newrelic.com/docs/new-relic-solutions/best-practices-guides/full-stack-observability/mobile-monitoring-best-practices-guide/)

[Overview of app launch times](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-app-launch-times/)

[Data privacy and security](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/security-mobile-apps/)

[Mobile agents EOL policy](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/mobile-agents-eol-policy/)

Model performance monitoring

Queues and Streams

Network monitoring

OpenTelemetry

SAP Solutions

Serverless monitoring

Streaming Video & Ads

Synthetic monitoring

Website performance monitoring

DATA INSIGHTS

New Relic AI

Alerts

Change tracking

Charts, dashboards, and querying

Cloud Cost Intelligence

CodeStream

Distributed tracing

Errors inbox

New Relic Lens

NRQL

Service Architecture Intelligence

Service level management

Workflow Automation

SECURITY

Interactive application security testing (IAST)

Security RX (Remediation Explorer)

PRODUCT UPDATES

Release notes

What's new?

[End-of-life announcements](https://docs.newrelic.com/eol/)

ADMIN AND DATA

Account & user management

Data and APIs

[Data dictionary](https://docs.newrelic.com/attribute-dictionary/)

Security and privacy

Licenses

Introduction to mobile monitoring
=================================

New Relic's mobile monitoring capabilities provide deeper visibility into the performance and crash troubleshooting of your Android, iOS, or hybrid mobile applications. You can use mobile monitoring to improve your app's user experience or examine HTTP and network performance to collaborate more effectively with your backend teams.

Once you follow our easy install flow, you'll be able to further configure mobile monitoring to suit your mobile environment.

Create an app and install your agent [](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#install)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Choose your platform to get started:

[Android](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-android/get-started/introduction-new-relic-mobile-android/)[Capacitor](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-ionic-capacitor/get-started/introduction-new-relic-ionic-capacitor/)[Cordova](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-cordova-phonegap/get-started-with-cordova-monitoring/)[Flutter](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-flutter/monitor-your-flutter-application/)[iOS](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-ios/get-started/introduction-new-relic-mobile-ios/)[.NET MAUI](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-maui-dotnet/monitor-your-net-maui-application/)[React Native](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-monitoring-react-native/monitor-your-react-native-application/)[Unity](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-unity/monitor-your-unity-application/)[Unreal Engine](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-unreal-engine/monitor-your-unreal-engine-application/)

After installing your agent, explore uses for mobile monitoring:

Use mobile monitoring as a tool for crash analysis [](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#crash-analysis)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### 1. Receive alert notifications about crashes[](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#alert)

[Set up alerts](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/mobile-monitoring-alert-information/#conditions) to receive alert notifications straight to your mobile device when your users are experiencing app crashes. See an overview of your app's performance on the [Summary](https://docs.newrelic.com/docs/mobile-monitoring/mobile-monitoring-ui/mobile-app-pages/mobile-apps-overview-page/) page, where you can filter for relevant data by a specific app version and [time range](https://docs.newrelic.com/docs/query-your-data/explore-query-data/dashboards/manage-your-dashboard/#dash-time-picker).

[![Image 1: New Relic: Mobile summary](https://docs.newrelic.com/images/mobile_screenshot-full_summary.webp)](https://docs.newrelic.com/images/mobile_screenshot-full_summary.webp)

An example of using the mobile **Summary** page to filter to an Android version with crashes.

##### 2. Use crash analysis to pinpoint errors[](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#crash-analysis)

Click the **Crashes** chart title on the mobile **Summary** page. The [**Crash analysis** page](https://docs.newrelic.com/docs/mobile-monitoring/mobile-monitoring-ui/crashes/crash-analysis-group-filter-your-crashes/) will open with the same time frame and version filters. Observe data about your crashes by looking at crash type to examine the exception, location, and error message. You can also examine the stack trace, interaction trail, and event trail to understand where users were impacted. With this data, you can quickly identify and remedy errors, and restore your app's performance.

[![Image 2: New Relic: Mobile crash analysis](https://docs.newrelic.com/images/mobile_screenshot-full_crash-analysis.webp)](https://docs.newrelic.com/images/mobile_screenshot-full_crash-analysis.webp)

An example of using the **Crash analysis** page to track down the cause for crashes for a new release by examining the exception, location, and error message.

Identify opportunities to speed up app performance [](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#speed-performance)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Create [dashboards](https://docs.newrelic.com/docs/dashboards/new-relic-one-dashboards/get-started/introduction-new-relic-one-dashboards/) to query, visualize, and share performance data.
*   Identify [handled exceptions](https://docs.newrelic.com/docs/mobile-monitoring/mobile-monitoring-ui/crashes/introduction-mobile-handled-exceptions/) to streamline workflows.
*   See trends with sessions, devices, geographical locations, operating systems, carriers, requests and responses, etc. with [crash profiles](https://docs.newrelic.com/docs/mobile-monitoring/mobile-monitoring-ui/crashes/crash-analysis-group-filter-your-crashes/#profiles) and [HTTP profiles](https://docs.newrelic.com/docs/errors-inbox/group-request-errors/#error-profiles).
*   Set up [alert notifications](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/getting-started/alert-information-new-relic-mobile/) for execution time, errors, etc.
*   Define [custom attributes and events](https://docs.newrelic.com/docs/insights/insights-data-sources/custom-events/insert-custom-events-attributes-mobile-data/) to obtain additional, specific details about the mobile data that matters the most to your organization.

Monitor backend issues [](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#backend)
------------------------------------------------------------------------------------------------------------------------------------------------

You can use the [network pages](https://docs.newrelic.com/docs/mobile-monitoring/mobile-monitoring-ui/network-pages/analyze-network-requests-using-mobilerequest-event-data/) in our mobile monitoring UI to identify problems that surface through HTTP requests, errors, and other network issues. You can also [query your data](https://docs.newrelic.com/docs/nrql/nrql-examples/nrql-query-examples-mobile-monitoring/) and create custom dashboards to share with relevant teams like your backend API developers.

#### On this page

*   [Create an app and install your agent](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#install)
*   [Use mobile monitoring as a tool for crash analysis](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#crash-analysis)
*   [Identify opportunities to speed up app performance](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#speed-performance)
*   [Monitor backend issues](https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring/#backend)

Was this doc helpful?

😁

Yes

🙁

No

[Edit this doc](https://github.com/newrelic/docs-website/blob/develop/src/content/docs/mobile-monitoring/new-relic-mobile/get-started/introduction-mobile-monitoring.mdx)

Copyright © 2026 New Relic Inc.

[Careers](https://newrelic.com/about/careers)[Terms of Service](https://newrelic.com/termsandconditions/terms)[DMCA Policy](https://newrelic.com/termsandconditions/dmca)[Patent Notice](https://newrelic.com/termsandconditions/patent-notice)[Privacy Notice](https://newrelic.com/termsandconditions/services-notices)Your Privacy Choices[Cookie Policy](https://newrelic.com/termsandconditions/cookie-policy)[UK Slavery Act](https://newrelic.com/termsandconditions/uk-slavery-act)

This site is protected by reCAPTCHA and the Google[Privacy Policy](https://policies.google.com/privacy) and[Terms of Service](https://policies.google.com/terms) apply.
