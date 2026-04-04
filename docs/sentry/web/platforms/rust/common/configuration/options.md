---
---
title: Options
description: "Learn more about how the SDK can be configured via options. These are being passed to the init function and therefore set when the SDK is first initialized."
---

## Available Options

## Core Options

Options that can be read from an environment variable (`SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_RELEASE`) are read automatically.

The DSN tells the SDK where to send the events. If this value is not provided, the SDK will try to read it from the `SENTRY_DSN` environment variable. If that variable also does not exist, the SDK will just not send any events.

Learn more about [DSN utilization](/product/sentry-basics/dsn-explainer/#dsn-utilization).

Turns debug mode on or off. If debug is enabled, the SDK will attempt to print out useful debugging information if something goes wrong while sending the event. While it's generally not recommended to turn debug mode on in production, it won't create any security concerns.

Sets the release. This string is freeform and not set by default. Some formats are detected by Sentry and might be rendered differently. Learn more about how to send release data so Sentry can tell you about regressions between releases and identify the potential source in [the releases documentation](/product/releases/) or the sandbox.

Sets the environment. This string is freeform and not set by default. A release can be associated with more than one environment to separate them in the UI (think `staging` vs `prod` or similar).

By default the SDK will try to read this value from the `SENTRY_ENVIRONMENT` environment variable. If that is not present, this value will be set to `development` if debug assertions are enabled, otherwise to `production`.

This variable controls the total amount of breadcrumbs that should be captured. This defaults to `100`, but you can set this to any number. However, you should be aware that Sentry has a [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits) and any events exceeding that payload size will be dropped.

When enabled, stack traces are automatically attached to all messages logged. Stack traces are always attached to exceptions; however, when this option is set, stack traces are also sent with messages. This option, for instance, means that stack traces appear next to all log messages.

This option is turned off by default.

Grouping in Sentry is different for events with stack traces and without. As a result, you will get new groups as you enable or disable this flag for certain events.

If this flag is enabled, certain personally identifiable information (PII) is added by active integrations. By default, no such data is sent.

If you enable this option, be sure to manually remove what you don't want to send using our features for managing [_Sensitive Data_](../../data-management/sensitive-data/).

">

A list of string prefixes of module names that belong to the app. This option takes precedence over `in_app_exclude`.

Sentry differentiates stack frames that are directly related to your application ("in application") from stack frames that come from other packages such as the standard library, frameworks, or other dependencies. The application package is automatically marked as `inApp`. The difference is visible in [sentry.io](https://sentry.io), where only the "in application" frames are displayed by default.

">

A list of string prefixes of module names that do not belong to the app, but rather to third-party packages. Modules considered not part of the app will be hidden from stack traces by default.

This option can be overridden using `in_app_include`.

The server name to be reported. When not set, the server name is not sent with events.

">

The user agent that should be reported when sending events to Sentry.

This function is called with a breadcrumb struct before the breadcrumb is added to the scope. When `None` is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the breadcrumb itself.

This option controls the maximum size of request bodies that are sent to Sentry by HTTP server integrations.
The default value of `MaxRequestBodySize::Medium` will capture request bodies up to 10kB in size.

  The timeout on client drop for draining events on shutdown. This controls how long the SDK will wait for pending events to be sent when shutting down.

>">

  A list of integrations to enable. This allows you to manually pick and choose the integrations to enable.
  By default, only the default integrations are enabled.

  Whether to add default integrations. When set to `false`, no default integrations will be added automatically.
  The list of default integrations depends on the feature flags of the `sentry` crate that are active.

## Error Monitoring Options

  Configures the sample rate for error events, in the range of `0.0` to `1.0`. The default is `1.0`, which means that 100% of error events will be sent. If set to `0.1`, only 10% of error events will be sent. Events are picked randomly.

This function is called with the event payload, and can return a modified event struct, or `None` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

  By the time `before_send` is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

## Tracing Options

A number between `0.0` and `1.0`, controlling the percentage chance a given transaction will be sent to Sentry (`0.0` represents 0% while `1.0` represents 100%.) Applies equally to all transactions created in the app.

If given, called with a `SamplingContext` for each transaction to determine the sampling rate. Return a sample rate between `0.0` and `1.0` for the transaction in question. Takes priority over the `traces_sample_rate`.

## Transport Options

  When set, a proxy can be configured that should be used for outbound requests. This is also used for HTTPS requests unless a separate `https_proxy` is configured. However, not all SDKs support a separate HTTPS proxy. SDKs will attempt to default to the system-wide configured proxy, if possible. For instance, on Unix systems, the `HTTP_PROXY` environment variable will be picked up.

  Configures a separate proxy for outgoing HTTPS requests. If this option is not provided but `http_proxy` is, then `http_proxy` is used for HTTPS requests too.

Setting this to `true` disables SSL certificate validation when sending outbound requests to Sentry. This should never be enabled when using the SDK in your real codebase or otherwise handling any kind of sensitive or personally identifiable information, as it could be exposed to potential attackers.

'>

  The transport to use to send envelopes to Sentry.
  This is typically either a boxed function taking the client options by reference and returning a `Transport`, a boxed `Arc` or alternatively the `DefaultTransportFactory`.
  By default, the SDK uses a transport based on the `reqwest` crate running on a background thread.

## Logging Options

The following features and options are only available when the `logs` feature of the `sentry` crate is enabled. This is not a default feature.

Determines whether captured structured logs should be sent to Sentry.

  Callback that is executed for each Log being captured. When `None` is returned from the function, the log record is dropped. To pass the log record through, return the log record itself.

## Session Tracking Options

The following features and options are only available when the `release-health` feature of the `sentry` crate is enabled. This is a default feature.

Enable Release Health Session tracking. When automatic session tracking is enabled, a new "user-mode" session is started at the time of `sentry::init`, and will persist for the application lifetime.

Determine how Sessions are being tracked. Controls the mode for session tracking when `auto_session_tracking` is enabled.

