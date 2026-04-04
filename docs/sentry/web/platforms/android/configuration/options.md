---
---
title: Options
description: "Learn more about how the SDK can be configured via options. These are being passed to the init function and therefore set when the SDK is first initialized."
---

## Core Options

The DSN tells the SDK where to send the events. If this value is not provided, the SDK will just not send any events.

Learn more about [DSN utilization](/product/sentry-basics/dsn-explainer/#dsn-utilization).

Turns debug mode on or off. If debug is enabled SDK will attempt to print out useful debugging information if something goes wrong with sending the event. It's generally not recommended to turn it on in production, though turning `debug` mode on will not cause any safety concerns.

Enabling `debug` mode makes the SDK generate as much diagnostic data as possible. However, if you'd prefer to lower the verbosity of the Sentry SDK diagnostics logs, configure this option to set the appropriate level:

- `debug`: **default** The most verbose mode
- `info`: Informational messages
- `warning`: Warning that something might not be right
- `error`: Only SDK internal errors are printed
- `fatal`: Only critical errors are printed

Sets the distribution of the application. Distributions are used to disambiguate build or deployment variants of the same release of an application. For example, the dist can be the build number of an Xcode build or the version code of an Android build. The dist has a max length of 64 characters.

Sets the release. Some SDKs will try to automatically configure a release out of the box but it's a better idea to manually set it to guarantee that the release is in sync with your deploy integrations or source map uploads. Release names are strings, but some formats are detected by Sentry and might be rendered differently. Learn more about how to send release data so Sentry can tell you about regressions between releases and identify the potential source in [the releases documentation](/product/releases/) or the sandbox.

Sets the environment. This string is freeform and can be used to associate a release with more than one environment to separate them in the UI (think `staging` vs `prod` or similar).

Configures the sample rate for error events, in the range of `0.0` to `1.0`. (`1.0` means 100% of error events will be sent, `0.1` means only 10% will be sent.) Events are picked randomly.

This variable controls the total amount of breadcrumbs that should be captured. You can set this to any number. However, you should be aware that Sentry has a [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits) and any events exceeding that payload size will be dropped.

The maximum number of [envelopes](https://develop.sentry.dev/sdk/data-model/envelopes/) to keep in cache. The SDKs use envelopes to send data, such as events, attachments, user feedback, and sessions to sentry.io. An envelope can contain multiple items, such as an event with a session and two attachments. Depending on the usage of the SDK, the size of an envelope can differ. If the number of envelopes in the local cache exceeds `max-cache-items`, the SDK deletes the oldest envelope and migrates the sessions to the next envelope to maintain the integrity of your release health stats.

When enabled, stack traces are automatically attached to all messages logged. Stack traces are always attached to exceptions; however, when this option is set, stack traces are also sent with messages. This option, for instance, means that stack traces appear next to all log messages.

Grouping in Sentry is different for events with stack traces and without. As a result, you will get new groups as you enable or disable this flag for certain events.

When enabled, information about all threads is attached to events, not just the crashing thread. This provides a more complete picture of the application state at the time of an error, including stack traces from all running threads.

Note that enabling this option may increase the payload size of events sent to Sentry.

Controls whether the SDK collects additional device context (such as battery level, memory usage, storage state, and connectivity) to enrich events. Disabling this can reduce file I/O and help avoid Android StrictMode violations or ANR triggers on some devices at the cost of losing that context on events.

AndroidManifest.xml key: `io.sentry.additional-context`.

If this flag is enabled, certain personally identifiable information (PII) is added by active integrations.

If you are using Sentry in your mobile app, read our [frequently asked questions about mobile data privacy](/security-legal-pii/security/mobile-privacy/) to assist with Apple App Store and Google Play app privacy details.

If you enable this option, be sure to manually remove what you don't want to send using our features for managing [_Sensitive Data_](../../data-management/sensitive-data/).

When set to `true`, the SDK will send session events to Sentry. This is supported in all browser SDKs, emitting one session per pageload and page navigation to Sentry. In mobile SDKs, when the app goes to the background for longer than 30 seconds, sessions are ended.

A list of string prefixes of module names that belong to the app. This option takes precedence over `in-app-excludes`.

Sentry differentiates stack frames that are directly related to your application ("in application") from stack frames that come from other packages such as the standard library, frameworks, or other dependencies. The application package is automatically marked as `inApp`. The difference is visible in [sentry.io](https://sentry.io), where only the "in application" frames are displayed by default.

A list of string prefixes of module names that do not belong to the app, but rather to third-party packages. Modules considered not part of the app will be hidden from stack traces by default.

This option can be overridden using .

A list of exception types that will be filtered out before sending to Sentry.

This parameter controls whether integrations should capture HTTP request bodies. It can be set to one of the following values:

- `none`: **default** Request bodies are never sent.
- `small`: Only small request bodies will be captured. The cutoff for small depends on the SDK (typically 4KB).
- `medium`: Medium and small requests will be captured (typically 10KB).
- `always`: The SDK will always capture the request body as long as Sentry can make sense of it.

Takes a screenshot of the application when an error happens and includes it as an attachment.
Learn more about enriching events with screenshots in our Screenshots documentation.

_(New in version 6.0.0)_

Renders a JSON representation of the entire view hierarchy of the application when an error happens and includes it as an attachment.
Learn more about enriching events with the view hierarchy in our View Hierarchy documentation.

The idle time, measured in ms, to wait until a transaction will be automatically finished. The transaction will use the end timestamp of the last finished span as the endtime for the transaction.

_(New in version 6.0.0)_

This only affects [user interaction transactions](/platforms/android/tracing/instrumentation/automatic-instrumentation/#user-interaction-instrumentation).

The deadline time, measured in ms, to wait until a transaction will be automatically forcefully finished, even if a child span is currently running.

_(New in version 8.18.0)_

This only affects [automatic transactions](/platforms/android/tracing/instrumentation/automatic-instrumentation/).

Specifies whether this SDK should send events to Sentry. Setting this to `enabled: false` doesn't prevent all overhead from Sentry instrumentation. To disable Sentry completely call `SentryAndroid.init` conditionally.

Set this boolean to `false` to disable sending of client reports. Client reports are a protocol feature that let clients send status reports about themselves to Sentry. They are currently mainly used to emit outcomes for events that were never sent.

_(New in version 6.0.0)_

Set this boolean to `true` to force a call to `SentryAndroid.init` to re-initialize the SDK, even if the SDK has already been initialized with high priority.

_(New in version 8.0.0)_

## Integration Configuration

For many platform SDKs integrations can be configured alongside it. On some platforms that happen as part of the `init()` call, in some others, different patterns apply.

In some SDKs, the integrations are configured through this parameter on library initialization. For more information, please see our documentation for a specific integration.

This can be used to disable integrations that are added by default. When set to `false`, no default integrations are added.

This can be used to disable integrations that are enabled by default if the SDK detects that the corresponding framework or library is installed. When set to `false`, none of these integrations will be enabled by default, even if the corresponding framework/library is detected.

## Hooks

These options can be used to hook the SDK in various ways to customize the reporting of events or to monitor the type and amount of discarded data.

This function is called with an SDK-specific message or error event object, and can return a modified event object, or `null` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

By the time  is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

This function is called with an SDK-specific transaction event object, and can return a modified transaction event object, or `null` to skip reporting the event. One way this might be used is for manual PII stripping before sending.

This function is called with an SDK-specific breadcrumb object before the breadcrumb is added to the scope. When nothing is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the first argument, which contains the breadcrumb object.

The callback typically gets a second argument (called a "hint") which contains the original object from which the breadcrumb was created to further customize what the breadcrumb should look like.

This function is called when data is discarded, for reasons including sampling, network errors, or queue overflows. The function arguments give the user insight into the reason for discarding, the type of data discarded, and the number of items discarded.

## Transport Options

Transports are used to send events to Sentry. Transports can be customized to some degree to better support highly specific deployments.

Switches out the transport used to send events. How this works depends on the SDK. It can, for instance, be used to capture events for unit-testing or to send it through some more complex setup that requires proxy authentication.

When set, a proxy can be configured that should be used for outbound requests. This is also used for HTTPS requests.

Specifies a local directory used for caching payloads. When this option is enabled (that is, when the directory is set), the Sentry SDK will persist envelopes locally before sending to Sentry. This configuration option is particularly useful if you expect your application to run in environments where internet connectivity is limited.

Controls how many seconds to wait before shutting down. Sentry SDKs send events from a background queue. This queue is given a certain amount to drain pending events. Setting this value too low may cause problems for sending events from the application. Setting the value too high will cause the application to block for a long time for users experiencing network connectivity problems.

## Tracing Options

A number between `0` and `1`, controlling the percentage chance a given transaction will be sent to Sentry. (`0` represents 0% while `1` represents 100%.) Applies equally to all transactions created in the app. Either this or  must be defined to enable tracing.

A function responsible for determining the percentage chance a given transaction will be sent to Sentry. It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent). Can also be used for filtering transactions, by returning 0 for those that are unwanted. Either this or  must be defined to enable tracing.

An optional property that controls which downstream services receive tracing data, in the form of a `sentry-trace` and a `baggage` header attached to any outgoing HTTP requests.

The option may contain a list of strings or regex against which the URLs of outgoing requests are matched.
If one of the entries in the list matches the URL of an outgoing request, trace data will be attached to that request.
String entries do not have to be full matches, meaning the URL of a request is matched when it _contains_ a string provided through the option.

If  is not provided, trace data is attached to every outgoing request from the instrumented client.

Controls whether the SDK should propagate the W3C `traceparent` HTTP header alongside the `sentry-trace` and `baggage` headers for outgoing HTTP requests.

Set this boolean to `false` to disable tracing for `OPTIONS` requests. This option's default value will likely be changed in the next major version, meaning you will have to set it to `true` if you want to keep tracing `OPTIONS` requests.

## UI Profiling Options

UI Profiling requires SDK versions `8.7.0` or higher. Lower versions can use the transaction-based profiling.

A number between `0` and `1`, controlling the percentage chance that the session will be profiled. (`0` represents 0%, `1` represents 100%.) The default is null (disabled).

Whether the UI profiling lifecycle is controlled manually or based on the trace lifecycle. Possible values are:

- `manual`: **default** Profiler must be started and stopped through `Sentry.startProfiler()` and `Sentry.stopProfiler()` APIs
- `trace`: Profiler is started and stopped automatically whenever a sampled trace starts or finishes

A boolean value that determines whether the app start process will be profiled. When true, the startup process, including ContentProviders, Application, and first Activity creation, will be profiled. Note that  must be defined.

- If profileLifecycle is set to `manual`: profiling is started automatically on startup and stopProfiler must be called manually whenever the app startup is deemed to be completed
- If profileLifecycle is set to `trace`: profiling is started automatically on startup, and will automatically be stopped when the root span that is associated with app startup ends

## Transaction-Based Profiling Options

This mode will eventually be deprecated, and it's recommended to upgrade to UI Profiling. The same behaviour, without the 30 seconds limitation, can be achieved with the `trace` profile lifecycle option. In order to upgrade to UI Profiling, you also need to remove the transaction-based options from your configuration.

A number between `0` and `1`, controlling the percentage chance that a given profile will be sent to Sentry. (`0` represents 0% while `1` represents 100%.) Applies only to sampled transactions created in the app. Setting this option will enable the legacy profiler.

A function responsible for determining the percentage chance that a given profile will be sent to Sentry. It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent). Can also be used for filtering profiles, by returning 0 for those that are unwanted. Either this or  must be defined to enable transaction profiling. Setting this option will enable the legacy profiler.

A boolean value that determines whether the app start process will be profiled. When true, the startup process, including ContentProviders, Application, and first Activity creation, will be profiled.

