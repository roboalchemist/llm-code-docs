---
---
title: Data Collected
description: "See what data is collected by the Sentry SDK."
---

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. This page lists data categories that the Apple SDK collects.

  The types and amount of information collected depends on the platform on which the Apple SDK is used. Refer to the respective platform guide to see information specific to the platform you're interested in.

## HTTP Headers

The HTTP Client Errors, which are enabled by default, send the HTTP headers of the failed request and response to Sentry. The SDK uses a [denylist](https://github.com/getsentry/sentry-cocoa/blob/main/Sources/Swift/Tools/HTTPHeaderSanitizer.swift) to filter out any headers that contain sensitive data.

## Users' IP Addresses

By default, the Sentry SDK doesn't send the user's IP address. Once enabled, the Sentry backend services will infer the user ip address based on the incoming request, unless certain integrations you can enable override this behavior.

To enable sending the user's IP address, set `sendDefaultPii=true`.

## Request URL

When the Apple SDK sends URLs to Sentry it always sends a sanitized URL which means it removes the query string and the fragment of the URL. Although the Apple SDK sanitizes the URL by removing the query string and the fragment of the URL, depending on your application, this could contain PII data.

Network breadcrumbs and HTTP Client Errors, both enabled by default, send a sanitized URL for outgoing HTTP requests. You can disable network breadcrumbs by setting the option `enableNetworkBreadcrumbs` to `false` and you can disable HTTP Client Errors by setting the option `enableCaptureFailedRequests` to `false`.

When you enable tracing, which is disabled per default,  network tracing sends a sanitized URL for outgoing HTTP requests.

## Source Context

You can upload your source code to Sentry, which can then used to show the lines of code where an error happened in the Issue Details page, via the sentry-cli or the Sentry Fastlane plugin.

To opt into sending this source context to Sentry, you have to enable the feature as described in the Source Context documentation.

## File I/O

When you enable tracing, which is disabled per default, the Apple SDK instruments file I/O operations and sends the file names and paths to Sentry.

## Core Data Queries

When you enable tracing, which is disabled per default, the Apple SDK instruments Core Data queries and sends the Core Data queries to Sentry. Neither the full SQL query (`SELECT 'User' WHERE name == 'username'`), nor the values of its parameters will ever be sent. A parameterized version of the query (`SELECT 'User' WHERE name == %@`) is sent instead.

## Screenshots

The screenshot feature is disabled per default, but when enabled the screenshots may contain PII data.

## View Hierarchy

The view hierarchy feature is disabled per default, but when enabled the view hierarchy may contain PII data when using the `accessibilityIdentifier` property with personal information.

## Session Replay

By default, our Session Replay SDK masks all text content, images, webviews, and user input. This helps ensure that no sensitive data is exposed. You can find more details in the Session Replay documentation.

