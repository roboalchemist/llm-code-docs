# Source: https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/

Title: How to use browser monitoring to improve your website's performance

URL Source: https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/

Markdown Content:
How to use browser monitoring to improve your website's performance | New Relic Documentation
===============

Opens in a new window Opens an external website Opens an external website in a new window

We use cookies and other tracking technologies - provided by other companies with whom we share your data - to make our website work, improve your experience, and support our marketing efforts, as explained in our [](https://newrelic.com/termsandconditions/privacy)[Privacy Notice](https://newrelic.com/termsandconditions/privacy). By using our website, you agree to our [](https://newrelic.com/termsandconditions/website-terms)[Website Terms of Use](https://newrelic.com/termsandconditions/website-terms). [Privacy Notice](https://newrelic.com/termsandconditions/privacy)

[](https://newrelic.com/)

[Docs](https://docs.newrelic.com/)[Community](https://support.newrelic.com/)[Learn](https://learn.newrelic.com/)

*   [Docs](https://docs.newrelic.com/)
*   [Community](https://support.newrelic.com/)
*   [Learn](https://learn.newrelic.com/)

*   / 
*   [English](https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)[Español](https://docs.newrelic.com/es/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)[Français](https://docs.newrelic.com/fr/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)[日本語](https://docs.newrelic.com/jp/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)[한국어](https://docs.newrelic.com/kr/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)[Português](https://docs.newrelic.com/pt/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)   
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

[Get started with browser monitoring](https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/)

[Improve your website's performance Tutorial](https://docs.newrelic.com/docs/tutorial-improve-site-performance/improve-website-performance/)

Guides

Installation

Configuration

View browser data

Monitor single page applications (SPA)

Page load timing resources

Browser APIs

Troubleshooting

Release notes

[Data privacy and security](https://docs.newrelic.com/docs/browser/new-relic-browser/performance-quality/security-browser-monitoring/)

[New Relic's impact on your app's performance](https://docs.newrelic.com/docs/browser/new-relic-browser/performance-quality/browser-monitoring-performance-impact/)

Browser integrations

Lab: Troubleshoot your site
Lab

eBPF observability

Infrastructure monitoring

Kubernetes monitoring

Log management

Mobile monitoring

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

How to use browser monitoring to improve your website's performance
===================================================================

Our browser monitoring provides a real user monitoring (RUM) solution. It measures speed and performance as your end users navigate to your site through different web browsers, devices, operating systems, and networks. But browser monitoring goes far beyond providing information about the initial page load. Use it to measure full page life cycle data and start getting the info you need to help ensure customer satisfaction.

New Relic lets you monitor the data from browser activity and optimize performance across your entire stack. Use browser monitoring to help ensure successful deployments and quickly troubleshoot customer-visible problems. Monitor your stack at a glance and make sure all your entities are operating as they should. Visualize application speed and performance, JavaScript errors, AJAX requests, logs and more. Spend less time trying to chase down issues and more time delivering a perfect digital experience to customers.

[Sign up](https://newrelic.com/signup)

[Deploy browser monitoring](https://onenr.io/0BQ127zqMwx)

[Deployment options](https://docs.newrelic.com/docs/browser/browser-monitoring/installation/install-browser-monitoring-agent/#options)

[![Image 1: A screenshot of data visualization using browser monitoring](https://docs.newrelic.com/images/browser_screenshot-crop_data-visualize.webp)](https://docs.newrelic.com/images/browser_screenshot-crop_data-visualize.webp)

[![Image 2: An image showing the distributed tracing feature](https://docs.newrelic.com/images/browser_screenshot-crop_distributed-tracing.webp)](https://docs.newrelic.com/images/browser_screenshot-crop_distributed-tracing.webp)

Track web vitals[](https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/#track-web-vitals)
-----------------------------------------------------------------------------------------------------------------------------------------------

Google's core web vitals are three metrics to gauge how users experience your browser app - and New Relic can help you track them! There are two places to see core web vitals in New Relic:

*   [Monitor Google's core web vitals to ensure your app's performance](https://docs.newrelic.com/docs/browser/new-relic-browser/guides/guide-to-core-web-vitals/#monitor)

*   [Use our additional web vitals to examine other aspects of your app's performance](https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/browser-summary-page/)

Identify end-user issues[](https://docs.newrelic.com/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring/#identify-end-user-issues)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Instrument any type of data you need, such as metrics, events, logs, and traces, to help optimize your end users' page load experience and keep them happy.

*   [Compare real user browser interactions and synthetic monitoring trends](https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/administration/compare-page-load-performance-browser-synthetic-monitoring/)

*   [Focus on specific geographical locations or specific types of end-user activity](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/filterable-geography-webpage-metrics-location/)

*   [Determine whether problems are related to specific types of browsers, browser versions, or device-types](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/browsers-problem-patterns-type-or-platform/)

[#### Use Javascript analytics to see how users trigger errors](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/javascript-errors-page-detect-analyze-errors/)[#### Monitor activity during browser interactions for apps with single-page application (SPA) architecture](https://docs.newrelic.com/docs/browser/single-page-app-monitoring/get-started/introduction-single-page-app-monitoring/)[#### Determine if specific browsers or devices cause problems](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/browsers-problem-patterns-type-or-platform/)[#### Use distributed tracing to isolate latency across a full transaction](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/browser-data-distributed-tracing/)

Was this doc helpful?

😁

Yes

🙁

No

[Edit this doc](https://github.com/newrelic/docs-website/blob/develop/src/content/docs/browser/browser-monitoring/getting-started/introduction-browser-monitoring.mdx)

Copyright © 2026 New Relic Inc.

[Careers](https://newrelic.com/about/careers)[Terms of Service](https://newrelic.com/termsandconditions/terms)[DMCA Policy](https://newrelic.com/termsandconditions/dmca)[Patent Notice](https://newrelic.com/termsandconditions/patent-notice)[Privacy Notice](https://newrelic.com/termsandconditions/services-notices)Your Privacy Choices[Cookie Policy](https://newrelic.com/termsandconditions/cookie-policy)[UK Slavery Act](https://newrelic.com/termsandconditions/uk-slavery-act)

This site is protected by reCAPTCHA and the Google[Privacy Policy](https://policies.google.com/privacy) and[Terms of Service](https://policies.google.com/terms) apply.

How likely are you to recommend our docs to a friend or colleague?
==================================================================

0 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
