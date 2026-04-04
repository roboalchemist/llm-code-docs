---
---
title: Troubleshooting
description: "Learn how to troubleshoot your profiling setup."
---

## I see elevated number of crashes in the Android Runtime when profiling is activated

Profiling uses the Android runtime's `tracer` under the hood to sample threads. There are known issues that this `tracer` can cause crashes in certain circumstances. Read on for more information, and subscribe to this GitHub issue for updates.

As of October 2024, two of these crashes (see 1, 2) have been acknowledged and fixed by Google. The fixes are being rolled out to affected devices by Google, but the crashing behavior might still be present on devices that didn't receive the fix yet.

There is one other issue, where the likely root cause is incorrect native thread handling by app code or third party code. This means that it can also not be fixed in the Sentry SDK. If you experience this, please comment on the GitHub issue.

## I don't see any profiling data in [sentry.io](https://sentry.io)

If you don't see any profiling data in [sentry.io](https://sentry.io), you can try the following:

- Ensure that Tracing is enabled.
- Ensure that the automatic instrumentation is sending performance data to Sentry by going to the **Performance** page in [sentry.io](https://sentry.io).
- If the automatic instrumentation is not sending performance data, try using custom instrumentation.
- Enable debug mode in the SDK and check the logs.
