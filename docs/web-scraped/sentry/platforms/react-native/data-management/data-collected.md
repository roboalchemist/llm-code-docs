---
---
title: Data Collected
description: "See what data is collected by the Sentry SDK."
---

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. This page lists data categories that the Sentry React Native SDK collects.

Many of the categories listed here require you to set `sendDefaultPii: true` in your `Sentry.init({})` config.

## HTTP Headers

By default, failed Fetch and XHR requests error events from `Sentry.httpClientIntegration` don't contain headers.

To start sending headers, set `sendDefaultPii: true` in your `Sentry.init({})` config.

## User-Agent

By default, the Sentry SDK attaches the HTTP request User-agent to the event. To disable this behavior, remove the `Sentry.httpContextIntegration` from the integrations array.

## Cookies

By default, the Sentry SDK doesn't send cookies. Sentry tries to remove any cookies that contain sensitive information, such as the Session ID and CSRF Token cookies.

To start sending cookies, set `sendDefaultPii: true` in your `Sentry.init({})` config.

## Information About Logged-in User

By default, the Sentry SDK doesn't send any information about the logged-in user, such as email address, user ID, or username. Even if enabled, the type of logged-in user information you'll be able to send depends on the integrations you enable in Sentry's SDK. Most integrations won't send any user information. Some will only set the user ID, but there are a few that will set the user ID, username, and email address.

To start sending logged-in user information, set `sendDefaultPii: true` in your `Sentry.init({})` config.

## Users' IP Addresses

By default, the user's IP address is inferred by the Sentry backend services based on the incoming request.

To disable sending the user's IP address, override the default value by a custom String value, for example by calling `Sentry.setUser({ip_address: '0.0.0.0'})`.

## Request URL

The full request URL and Referer of outgoing HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data.

## Request Query String

The full request query string of outgoing HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data.

## Device Information

By default the Sentry SDK does not send the name of the device on Android.

If you want to send the device name, set `sendDefaultPii: true` in your `Sentry.init({})` config.

## Console Logs

By default, the Sentry SDK sends JS console logs to Sentry which may contain PII data.

To disable sending console logs, set `console: false` in your `Sentry.breadcrumbsIntegration` config, see the Breadcrumbs documentation.

## Screenshots

The screenshot feature is disabled per default, but when enabled the screenshots may contain PII data.

## View Hierarchy

The view hierarchy feature is disabled per default, but when enabled the view hierarchy may contain PII data when using the `accessibilityIdentifier` property with personal information.

## Session Replay

By default, our Session Replay SDK masks all text content, images, webviews, and user input. This helps ensure that no sensitive data is exposed. You can find more details in the Session Replay documentation.

## Source Context

By default, the Sentry React Native SDK build tooling will upload only the applications' JS bundles and source maps to Sentry. To disable sources upload set `SENTRY_DISABLE_AUTO_UPLOAD=true` in your environment variables, see the Source Maps documentation.

To opt into native source code upload enable the feature as described in the Debug Symbols documentation.
