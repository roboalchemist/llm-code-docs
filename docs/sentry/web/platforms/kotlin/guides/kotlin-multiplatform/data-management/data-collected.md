---
---
title: Data Collected
description: "See what data is collected by the Sentry SDK."
---

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. By default the Kotlin Multiplatform SDK will collect data as specified by the used native SDKs.

Many of the categories listed require you to set `sendDefaultPii: true` in your `Sentry.init` config.

The `sendDefaultPii` option is available since KMP SDK version `0.13.0`.

Read the documentation of the native SDKs for more details.
- [Apple](/platforms/apple/data-management/data-collected/)
- [Android](/platforms/android/data-management/data-collected/)
- [Java](/platforms/java/data-management/data-collected/)
