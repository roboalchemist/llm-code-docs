---
---
title: Troubleshooting
description: "Troubleshooting steps for PHP"
---

## General

A good first step to debug SDK issues is using the `logger` option. For your convenience, the SDK ships with two implementations, `DebugFileLogger` and `DebugStdOutLogger`.

```php
\Sentry\init([
    'logger' => new \Sentry\Logger\DebugFileLogger('/path/to/your/logfile.log'),
]);

// or

\Sentry\init([
    'logger' => new \Sentry\Logger\DebugStdOutLogger(),
]);
```

The produced output will look something like this:

```
sentry/sentry: [debug] The "Sentry\Integration\ExceptionListenerIntegration, Sentry\Integration\ErrorListenerIntegration, Sentry\Integration\FatalErrorListenerIntegration, Sentry\Integration\RequestIntegration, Sentry\Integration\TransactionIntegration, Sentry\Integration\FrameContextifierIntegration, Sentry\Integration\EnvironmentIntegration, Sentry\Integration\ModulesIntegration" integration(s) have been installed.
sentry/sentry: [info] Transaction [e2919a7b0f954478b6994c7282b060de] was started and sampled, decided by config:traces_sample_rate.
sentry/sentry: [info] Transaction [e2919a7b0f954478b6994c7282b060de] started profiling because it was sampled.
sentry/sentry: [info] Sending transaction [59390dc9dd934c0290d8cdc7a589da82] to o1.ingest.sentry.io [project:1].
sentry/sentry: [warning] The profile does not contain enough samples, the profile will be discarded.
sentry/sentry: [info] Sent transaction [59390dc9dd934c0290d8cdc7a589da82] to o1.ingest.sentry.io [project:1]. Result: "success" (status: 200).

```

This is caused by the PHP configuration. PHP 7.4 introduced a new .ini setting, `zend.exception_ignore_args`, that will ignore stack trace arguments. Check your .ini file to ensure this setting is set to `Off` or `0`.

  Currently, every tag has a maximum character limit of 200 characters. Tags over the 200 character limit will become truncated, losing potentially important information. To retain this data, you can split data over several tags instead.

  For example, a 200+ character tagged request:

  `https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=161803398874989484820458683436563811772030917980576`

  The 200+ character request above will become truncated to:

  `https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=1618033988749894848`

  

## Profiling

If you don't see any profiling data in [sentry.io](https://sentry.io), you can try the following:

  - Ensure that Tracing is enabled.
  - Ensure that the automatic instrumentation is sending performance data to Sentry by going to the **Performance** page in [sentry.io](https://sentry.io).
  - Ensure that the custom instrumentation is sending performance data to Sentry by going to the **Performance** page in [sentry.io](https://sentry.io).
  - Ensure the `Sentry\Integration\EnvironmentIntegration` is enabled.
  - Enable the logger to see what the SDK is doing under the hood.

## Crons

  You may not have linked errors to your monitor.

  You may not have set up alerts for your monitor.

  Our current data retention policy is 90 days.

  Currently, we only support crontab expressions with five fields.

  You can either consider running your jobs in the background OR use the `checkInMargin` option to make the window larger.

