# Source: https://docs.datadoghq.com/error_tracking/frontend.md

---
title: Frontend Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Error Tracking > Frontend Error Tracking
---

# Frontend Error Tracking

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/error_tracking/rum-et-explorer.e8402f8ddb82d20c4fcd2bc1aedcba63.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

It is critical for your system's health to consistently monitor the errors collected by Datadog. When there are many individual error events, it becomes hard to prioritize errors for troubleshooting.

Error Tracking simplifies debugging by grouping thousands of similar errors into a single issue. Error Tracking enables you to:

- Track, triage, and debug fatal errors
- Group similar errors into issues to identify important errors and reduce noise
- Set monitors on error tracking events, such as high error volume or new issues
- Follow issues over time to know when they first started, if they are still ongoing, and how often they occur
- See a detailed timeline of steps a user took leading up to the error, simplifying the process to reproduce and resolve errors

## Setup{% #setup %}

- [Agentic Onboarding (frontend only)](https://docs.datadoghq.com/agentic_onboarding/setup)
- [Browser](https://docs.datadoghq.com/error_tracking/frontend/browser)
- [Android](https://docs.datadoghq.com/error_tracking/frontend/mobile/android)
- [iOS](https://docs.datadoghq.com/error_tracking/frontend/mobile/ios)
- [Expo](https://docs.datadoghq.com/error_tracking/frontend/mobile/expo)
- [React Native](https://docs.datadoghq.com/error_tracking/frontend/mobile/reactnative)
- [Flutter](https://docs.datadoghq.com/error_tracking/frontend/mobile/flutter)
- [Kotlin Multiplatform](https://docs.datadoghq.com/error_tracking/frontend/mobile/kotlin_multiplatform)
- [Logs](https://docs.datadoghq.com/error_tracking/frontend/logs)

## Further Reading{% #further-reading %}

- [Collect Browser Errors](https://docs.datadoghq.com/error_tracking/standalone_frontend/collecting_browser_errors/)
- [Getting Started with the Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer/)
- [Error Tracking Issue States and Workflows](https://docs.datadoghq.com/error_tracking/issue_states/)
