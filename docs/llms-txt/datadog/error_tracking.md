# Source: https://docs.datadoghq.com/tracing/error_tracking.md

# Source: https://docs.datadoghq.com/error_tracking.md

---
title: Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Error Tracking
source_url: https://docs.datadoghq.com/index.html
---

# Error Tracking

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-tracking-overview-2.aa2160eb75631cb79d8401f9448cc71f.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

It is critical for your system's health to consistently monitor the errors collected by Datadog. When there are many individual error events, it becomes hard to prioritize errors for troubleshooting.

Error Tracking simplifies debugging by grouping thousands of similar errors into a single issue. An issue is an aggregation of error data that provides insights such as

- How many users have been impacted
- When the error first occurred
- Which commit probably caused the error

Error Tracking enables you to:

- Track, triage, and debug fatal errors
- Group similar errors into issues, so that you can more easily identify important errors and reduce noise
- Set monitors on error tracking events, such as high error volume or new issues
- Follow issues over time to know when they first started, if they are still ongoing, and how often they occur

Additional features are available depending on the source of the error. See supported error sources.

## Getting started{% #getting-started %}

- Take a tour of key Error Tracking features in the [Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer) documentation.
- Use the product-specific links in the next section to set up Error Tracking for a particular error source.

## Setup{% #setup %}

- [Agentic Onboarding](https://docs.datadoghq.com/agentic_onboarding/setup)
- [Browser](https://docs.datadoghq.com/error_tracking/frontend/browser)
- [Android](https://docs.datadoghq.com/error_tracking/frontend/mobile/android)
- [iOS](https://docs.datadoghq.com/error_tracking/frontend/mobile/ios)
- [Expo](https://docs.datadoghq.com/error_tracking/frontend/mobile/expo)
- [React Native](https://docs.datadoghq.com/error_tracking/frontend/mobile/reactnative)
- [Flutter](https://docs.datadoghq.com/error_tracking/frontend/mobile/flutter)
- [Kotlin Multiplatform](https://docs.datadoghq.com/error_tracking/frontend/mobile/kotlin_multiplatform)
- [Logs](https://docs.datadoghq.com/error_tracking/frontend/logs)

## Supported error sources{% #supported-error-sources %}

Error Tracking captures and processes errors across your web, mobile, and backend applications. You can instrument your applications and services using the [Browser SDK](https://docs.datadoghq.com/error_tracking/frontend/browser), [Mobile SDK](https://docs.datadoghq.com/error_tracking/frontend/mobile), or ingest errors from your Logs, Traces, and Real User Monitoring events.

Additional features are available depending on the source of the error. For example, in errors originating from an APM trace, the [Exception Replay](https://docs.datadoghq.com/error_tracking/backend/exception_replay) feature automatically captures production variable values.

For details, see the product-specific Error Tracking documentation:

- [APM](https://docs.datadoghq.com/tracing/error_tracking#setup)
- [Log Management](https://docs.datadoghq.com/logs/error_tracking#setup)
- [Real User Monitoring](https://docs.datadoghq.com/real_user_monitoring/error_tracking#setup)

## Further reading{% #further-reading %}

- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
- [Troubleshoot root causes with GitHub commit and ownership data in Error Tracking](https://www.datadoghq.com/blog/error-tracking-and-github/)
- [A practical guide to error handling in Go](https://www.datadoghq.com/blog/go-error-handling/)
