# Source: https://docs.datadoghq.com/error_tracking/frontend/mobile/roku.md

---
title: Roku Crash Reporting and Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Error Tracking > Frontend Error Tracking > Mobile Crash Reporting >
  Roku Crash Reporting and Error Tracking
---

# Roku Crash Reporting and Error Tracking

## Overview{% #overview %}

Error Tracking processes errors collected from the Roku SDK.

Enable Roku Crash Reporting and Error Tracking to get comprehensive crash reports and error trends with Real User Monitoring. With this feature, you can access:

- Aggregated Roku crash dashboards and attributes
- Trend analysis with Roku error tracking

Your crash reports appear in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

## Setup{% #setup %}

If you have not set up the Roku SDK yet, follow the [in-app setup instructions](https://app.datadoghq.com/rum/application/create) or see the [Roku setup documentation](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/roku/setup/).

1. Add the latest version of the [Roku SDK](https://github.com/DataDog/dd-sdk-roku) to your ROPM dependencies (or download the zip archive).
1. Configure your application's `env` when [initializing the SDK](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android/advanced_configuration/?tabs=kotlin#initialization-parameters).

For any given error, you can access the file path, line number, and a code snippet for each frame of the related stack trace.

## Limitations{% #limitations %}

The SDK supports stack trace in crash reporting on Roku OS 13+, while on Roku OS <13, the stack trace is empty.

## Test your implementation{% #test-your-implementation %}

To verify your Roku Crash Reporting and Error Tracking configuration, you need to trigger a crash in your application and confirm that the error appears in Datadog.

To test your implementation:

1. Run your application on an Roku device.

1. Execute some code containing a crash. For example:

   ```
   sub explodingMethod()
       x = 1
       print x.foo
   ```

1. After the crash happens, restart your application and wait for the Roku SDK to upload the crash report in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

### Forward errors to Datadog{% #forward-errors-to-datadog %}

Whenever you perform an operation that might throw an exception, you can forward the error to Datadog by adding the following code snippet:

```
    try
        doSomethingThatMightThrowAnException()
    catch error
        m.global.datadogRumAgent.callfunc("addError", error)
    end try
```

## Further Reading{% #further-reading %}

- [Get started with Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking/)
- [Visualize Error Tracking data in the Explorer](https://docs.datadoghq.com/real_user_monitoring/error_tracking/explorer)
