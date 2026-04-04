---
---
title: Data Collected
description: "See what data is collected by the Sentry SDK."
---

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. Here's a list of data categories the Sentry Unreal Engine SDK collects:

## Users' IP Addresses

By default, the Sentry SDK doesn't send the user's IP address. Once enabled, the Sentry backend services will infer the user ip address based on the incoming request, unless certain integrations you can enable override this behavior.

To enable sending the user's IP address, set `sendDefaultPii=true`.

## Screenshots

The screenshot feature is disabled per default, but when enabled the screenshots may contain PII data.

## Device Information

The Sentry SDK collects information about the device, such as the name, version and build of your operating system or Linux distribution. This information is sent to Sentry by default.

## Thread Stack Information

At the time of a crash, the stack of each thread is collected and sent to Sentry as part of the Minidump snapshot for backends `crashpad` and `breakpad`. This information is sent to Sentry by default, but dropped after processing the event in the backend.

These files are not stored by default, but you can enable Minidump Storage in the Sentry organization or project settings.
