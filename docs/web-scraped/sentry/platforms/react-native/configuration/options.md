---
---
title: Options
description: "Learn more about how the SDK can be configured via options. These are being passed to the init function and therefore set when the SDK is first initialized."
---

## Available Options

Options that can be read from an environment variable (`SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_RELEASE`) are read automatically.

## Core Options

The DSN tells the SDK where to send the events. If this value is not provided, the SDK will try to read it from the `SENTRY_DSN` environment variable. If that variable also does not exist, the SDK will just not send any events.

In runtimes without a process environment (such as the browser) that fallback does not apply.

Learn more about [DSN utilization](/product/sentry-basics/dsn-explainer/#dsn-utilization).

Turns debug mode on or off. If debug is enabled SDK will attempt to print out useful debugging information if something goes wrong with sending the event. The default is always `false`. It's generally not recommended to turn it on in production, though turning `debug` mode on will not cause any safety concerns.

Sets the distribution of the application. Distributions are used to disambiguate build or deployment variants of the same release of an application. For example, the dist can be the build number of an Xcode build or the version code of an Android build. The dist has a max length of 64 characters.

Sets the release. Some SDKs will try to automatically configure a release out of the box but it's a better idea to manually set it to guarantee that the release is in sync with your deploy integrations or source map uploads. Release names are strings, but some formats are detected by Sentry and might be rendered differently. Learn more about how to send release data so Sentry can tell you about regressions between releases and identify the potential source in [the releases documentation](/product/releases/) or the sandbox.

By default the SDK will try to read this value from the `SENTRY_RELEASE` environment variable (in the browser SDK, this will be read off of the `window.SENTRY_RELEASE.id` if available).

Sets the environment. This string is freeform and not set by default. A release can be associated with more than one environment to separate them in the UI (think `staging` vs `prod` or similar).

By default the SDK will try to read this value from the `SENTRY_ENVIRONMENT` environment variable (except for the browser SDK where this is not applicable).

Configures the sample rate for error events, in the range of `0.0` to `1.0`. The default is `1.0`, which means that 100% of error events will be sent. If set to `0.1`, only 10% of error events will be sent. Events are picked randomly.

This variable controls the total amount of breadcrumbs that should be captured. This defaults to `100`, but you can set this to any number. However, you should be aware that Sentry has a [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits) and any events exceeding that payload size will be dropped.

The maximum number of [envelopes](https://develop.sentry.dev/sdk/data-model/envelopes/) to keep in cache. The SDKs use envelopes to send data, such as events, attachments, user feedback, and sessions to sentry.io. An envelope can contain multiple items, such as an event with a session and two attachments. Depending on the usage of the SDK, the size of an envelope can differ. If the number of envelopes in the local cache exceeds `maxCacheItems`, the SDK deletes the oldest envelope and migrates the sessions to the next envelope to maintain the integrity of your release health stats. The default is `30`.

When enabled, stack traces are automatically attached to all messages logged. Stack traces are always attached to exceptions; however, when this option is set, stack traces are also sent with messages. This option, for instance, means that stack traces appear next to all log messages.

This option is turned on by default.

Grouping in Sentry is different for events with stack traces and without. As a result, you will get new groups as you enable or disable this flag for certain events.

If this flag is enabled, certain personally identifiable information (PII) is added by active integrations. By default, no such data is sent.

If you are using Sentry in your mobile app, read our [frequently asked questions about mobile data privacy](/security-legal-pii/security/mobile-privacy/) to assist with Apple App Store and Google Play app privacy details.

This option is turned off by default.

If you enable this option, be sure to manually remove what you don't want to send using our features for managing [_Sensitive Data_](../../data-management/sensitive-data/).

When set to `true`, the SDK will send session events to Sentry. This is supported in all browser SDKs, emitting one session per pageload and page navigation to Sentry. In mobile SDKs, when the app goes to the background for longer than 30 seconds, sessions are ended.

Maximum number of characters a single value can have before it will be truncated (defaults to `250`).

Sentry SDKs normalize any contextual data to a given depth. Any data beyond this depth will be trimmed and marked using its type instead (`[Object]` or `[Array]`), without walking the tree any further. By default, walking is performed three levels deep.

This is the maximum number of properties or entries that will be included in any given object or array when the SDK is normalizing contextual data. Any data beyond this depth will be dropped. (defaults to 1000)

Takes a screenshot of the application when an error happens and includes it as an attachment.
Learn more about enriching events with screenshots in our Screenshots documentation.

_(New in version 4.11.0)_

Renders a JSON representation of the entire view hierarchy of the application when an error happens and includes it as an attachment.
Learn more about enriching events with the view hierarchy in our View Hierarchy documentation.

Specifies whether this SDK should send events to Sentry. Defaults to `true`. Setting this to `enabled: false` doesn't prevent all overhead from Sentry instrumentation. To disable Sentry completely, depending on environment, call `Sentry.init` conditionally.

Once enabled, this feature automatically captures HTTP client errors, like bad response codes, as error events and reports them to Sentry.

_(New in version 5.3.0)_

## Logs Options

Set this option to `true` to enable log capturing in Sentry. The logger APIs will only send logs to Sentry when this is turned on.

This function is called with a log object, and can return a modified log object, or `null` to skip sending this log to Sentry. This can be used, for instance, for manual PII stripping before sending, or to add custom attributes to all logs.

 

Allows the choice of which logs are captured: `native` for logs from native code only, `js` for logs from the JavaScript layer only, or `all` for both layers.
- It will only Take effect when `enableLogs` is `true`.

(New in version 7.7.0)

## Integration Configuration

For many platform SDKs integrations can be configured alongside it. On some platforms that happen as part of the `init()` call, in some others, different patterns apply.

In some SDKs, the integrations are configured through this parameter on library initialization. For more information, please see our documentation for a specific integration.

This can be used to disable integrations that are added by default. When set to `false`, no default integrations are added.

This can be used to disable integrations that are enabled by default if the SDK detects that the corresponding framework or library is installed. When set to `false`, none of these integrations will be enabled by default, even if the corresponding framework/library is detected.

## Hooks

These options can be used to hook the SDK in various ways to customize the reporting of events.

This function is called with an SDK-specific message or error event object, and can return a modified event object, or `null` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

By the time  is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

This function is called with an SDK-specific transaction event object, and can return a modified transaction event object, or `null` to skip reporting the event. One way this might be used is for manual PII stripping before sending.

This function is called with an SDK-specific breadcrumb object before the breadcrumb is added to the scope. When nothing is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the first argument, which contains the breadcrumb object.
The callback typically gets a second argument (called a "hint") which contains the original object from which the breadcrumb was created to further customize what the breadcrumb should look like.

## Transport Options

Transports are used to send events to Sentry. Transports can be customized to some degree to better support highly specific deployments.

Switches out the transport used to send events. How this works depends on the SDK. It can, for instance, be used to capture events for unit-testing or to send it through some more complex setup that requires proxy authentication.

Options used to configure the transport. This is an object with the following possible optional keys:

- `headers`: An object containing headers to be sent with every request. Used by the SDK's fetch and XHR transports.
- `fetchOptions`: An object containing options to be passed to the `fetch` call. Used by the SDK's fetch transport.

Controls how many seconds to wait before shutting down. Sentry SDKs send events from a background queue. This queue is given a certain amount to drain pending events. The default is SDK specific but typically around two seconds. Setting this value too low may cause problems for sending events from command line applications. Setting the value too high will cause the application to block for a long time for users experiencing network connectivity problems.

## Tracing Options

A number between `0` and `1`, controlling the percentage chance a given transaction will be sent to Sentry. (`0` represents 0% while `1` represents 100%.) Applies equally to all transactions created in the app. Either this or  must be defined to enable tracing.

A function responsible for determining the percentage chance a given transaction will be sent to Sentry. It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent). Can also be used for filtering transactions, by returning 0 for those that are unwanted. Either this or  must be defined to enable tracing.

An optional property that controls which downstream services receive tracing data, in the form of a `sentry-trace` and a `baggage` header attached to any outgoing HTTP requests.

The option may contain a list of strings or regex against which the URLs of outgoing requests are matched.
If one of the entries in the list matches the URL of an outgoing request, trace data will be attached to that request.
String entries do not have to be full matches, meaning the URL of a request is matched when it _contains_ a string provided through the option.

If  is not provided, trace data is attached to every outgoing request from the application (mobile, desktop, tv). When running on web trace data is only attached to outgoing requests that contain `localhost` in their URL or requests whose URL starts with a `'/'` (for example `GET /api/v1/users`).

Controls whether the SDK should propagate the W3C `traceparent` HTTP header alongside the `sentry-trace` and `baggage` headers for outgoing HTTP requests.

## Experimental Features

An optional property that configures which features are in experimental mode. This property is either an `Object Type` with properties or a key/value `TypedDict`, depending the language. Experimental features are still in-progress and may have bugs. We recognize the irony.

## Hybrid SDK Options

Set this boolean to `false` to disable the native SDK. This will disable all native crash and error handling and, instead, the SDK will only capture errors on the upper layer.

Set this boolean to `false` to disable the auto initialization of the native layer SDK. Doing so means you will need to initialize the native SDK manually. Do not use this to disable the native layer.

To disable the native layer, use [enableNative](#enableNative).

You should follow the [guide to native initialization](/platforms/react-native/manual-setup/native-init/) if you chose to use this option.

Set this boolean to `false` to disable hard crash handling from the native layer. Doing so means that the SDK won't capture events for hard crashes on Android and iOS if the error was caused by native code.

Set this boolean to `false` to disable the native nagger alert being shown.

Set this boolean to `false` to disable the [release health](/product/releases/health/) feature.

Set this to change the default interval to end a session (release health) if the app goes to the background. Default is 30,000.

Set this boolean to `false` to disable the scope sync from Java to NDK on Android.

Set this boolean to `true` to automatically attach all threads to all logged events on Android.

Set this boolean to `false` to disable auto [performance monitoring](/product/insights/) tracking.

Set this boolean to `false` to disable [out of memory](/platforms/apple/guides/ios/configuration/out-of-memory/) tracking on iOS.

Set this callback, which is called after the Sentry React Native SDK initializes its Native SDKs (Android and iOS).

