---
---
title: Options
description: "Learn more about how the SDK can be configured via options. These are being passed to the init function and therefore set when the SDK is first initialized."
---

## Core Options

Options that can be read from an environment variable (`SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_RELEASE`) are read automatically.

The DSN tells the SDK where to send the events. If this value is not provided, the SDK will try to read it from the `SENTRY_DSN` environment variable. If that variable also does not exist, the SDK will just not send any events.

In runtimes without a process environment (such as the browser) that fallback does not apply.

Learn more about [DSN utilization](/product/sentry-basics/dsn-explainer/#dsn-utilization).

Controls whether the SDK should send events to Sentry. When set to `false`, the SDK will not send any events to Sentry.

Note that setting this to `false` doesn't prevent all overhead from Sentry instrumentation. To disable Sentry completely, you may need to conditionally call `SentrySDK.start` based on your environment.

Turns debug mode on or off. If debug is enabled, SDK will attempt to print out useful debugging information if something goes wrong with sending the event. It's generally not recommended to turn it on in production, though this will not cause any safety concerns.

Enabling `debug` mode makes the SDK generate as much diagnostic data as possible. However, if you'd prefer to lower the verbosity of the Sentry SDK diagnostics logs, configure this option to set the appropriate level:

- `debug`: **default** The most verbose mode
- `info`: Informational messages
- `warning`: Warning that something might not be right
- `error`: Only SDK internal errors are printed
- `fatal`: Only critical errors are printed

Sets the release. Some SDKs will try to automatically configure a release out of the box but it's a better idea to manually set it to guarantee that the release is in sync with your deploy integrations or source map uploads. Release names are strings, but some formats are detected by Sentry and might be rendered differently. Learn more about how to send release data so Sentry can tell you about regressions between releases and identify the potential source in [the releases documentation](/product/releases/) or the sandbox.

Sets the distribution of the application. Distributions are used to disambiguate build or deployment variants of the same release of an application. For example, the dist can be the build number of an Xcode build or the version code of an Android build. The dist has a max length of 64 characters.

Sets the environment. This string is freeform and not set by default. A release can be associated with more than one environment to separate them in the UI (think `staging` vs `prod` or similar).

By default the SDK will try to read this value from the `SENTRY_ENVIRONMENT` environment variable (except for the browser SDK where this is not applicable).

Configures the sample rate for error events, in the range of `0.0` to `1.0`. If set to `0.1`, only 10% of error events will be sent. Events are picked randomly.

This variable controls the total amount of breadcrumbs that should be captured. You can set this to any number. However, you should be aware that Sentry has a [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits) and any events exceeding that payload size will be dropped.

The maximum number of [envelopes](https://develop.sentry.dev/sdk/data-model/envelopes/) to keep in cache. The SDKs use envelopes to send data, such as events, attachments, user feedback, and sessions to sentry.io. An envelope can contain multiple items, such as an event with a session and two attachments. Depending on the usage of the SDK, the size of an envelope can differ. If the number of envelopes in the local cache exceeds `max-cache-items`, the SDK deletes the oldest envelope and migrates the sessions to the next envelope to maintain the integrity of your release health stats.

When enabled, stack traces are automatically attached to all messages logged. Stack traces are always attached to exceptions; however, when this option is set, stack traces are also sent with messages. This option, for instance, means that stack traces appear next to all log messages.

Grouping in Sentry is different for events with stack traces and without. As a result, you will get new groups as you enable or disable this flag for certain events.

_(New in [sentry-cocoa version 8.27.0](https://github.com/getsentry/sentry-cocoa/blob/main/CHANGELOG.md#8270))_

When enabled, the SDK reports SIGTERM signals to Sentry.

It's crucial for developers to understand that the OS sends a SIGTERM to their app as a prelude to a graceful shutdown, before resorting to a SIGKILL. This SIGKILL, which your app can't catch or ignore, is a direct order to terminate your app's process immediately. Developers should be aware that their app can receive a SIGTERM in various scenarios, such as  CPU or disk overuse, watchdog terminations, or when the OS updates your app.

When enabled, the SDK sends crashes to Sentry. If disabled, the SDK will not capture or report crash events.

Note that disabling this option will also disable watchdog termination tracking, as it prevents false positive watchdog termination reporting for every crash.

When enabled, the SDK captures uncaught NSExceptions. As this feature uses swizzling, disabling `enableSwizzling` also disables this feature.

This option registers the `NSApplicationCrashOnExceptions` UserDefault, so your macOS application crashes when an uncaught exception occurs. As the Cocoa Frameworks are generally not exception-safe on macOS, we recommend this approach because the application could otherwise end up in a corrupted state.

**Warning:** Don't use this in combination with `SentryCrashExceptionApplication`. Having both enabled can lead to duplicated reports.

This option is available as of SDK version 8.40.0. Learn more in the capturing uncaught exceptions documentation.

Controls the flush duration when calling `SentrySDK.close()`. This determines how long the SDK will wait for pending events to be sent before shutting down.

If this flag is enabled, certain personally identifiable information (PII) is added by active integrations.

If you are using Sentry in your mobile app, read our [frequently asked questions about mobile data privacy](/security-legal-pii/security/mobile-privacy/) to assist with Apple App Store and Google Play app privacy details.

If you enable this option, be sure to manually remove what you don't want to send using our features for managing [_Sensitive Data_](../../data-management/sensitive-data/).

When set to `true`, the SDK will send session events to Sentry. This is supported in all browser SDKs, emitting one session per pageload and page navigation to Sentry. In mobile SDKs, when the app goes to the background for longer than 30 seconds, sessions are ended.

The interval, measured in milliseconds, to end a session after the app goes to the background. When the app goes to the background and remains there for longer than this interval, the current session is ended.

Learn more about session tracking in the releases documentation.

A list of string prefixes of module names that belong to the app.

Sentry differentiates stack frames that are directly related to your application ("in application") from stack frames that come from other packages such as the standard library, frameworks, or other dependencies. The application package is automatically marked as `inApp`. The difference is visible in [sentry.io](https://sentry.io), where only the "in application" frames are displayed by default.

**Removed in version 9.0.0** - This option had no effect and was removed.

A list of string prefixes of module names that do not belong to the app, but rather to third-party packages. Modules considered not part of the app will be hidden from stack traces by default.

This option can be overridden using .

A block that configures the initial scope when starting the SDK.

```swift
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.initialScope = { scope in
        scope.setTag(value: "my value", key: "my-tag")
        return scope
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.initialScope = ^(SentryScope *scope) {
        [scope setTagValue:@"my value" forKey:@"my-tag"];
        return scope;
    };
}];
```

_(New in [sentry-cocoa version 8.7.0](https://github.com/getsentry/sentry-cocoa/blob/main/CHANGELOG.md#870))_

Takes a screenshot of the application when an error happens and includes it as an attachment.
Learn more about enriching events with screenshots in our Screenshots documentation.

Renders a JSON representation of the entire view hierarchy of the application when an error happens and includes it as an attachment.
Learn more about enriching events with the view hierarchy in our View Hierarchy documentation.

The idle time, measured in ms, to wait until a user interaction transaction will be automatically finished. The transaction will use the end timestamp of the last finished span as the endtime for the transaction.

When enabled, the SDK tracks performance for the UIViewController subclasses.

This feature is not available in `DebugWithoutUIKit` and `ReleaseWithoutUIKit` configurations, even when targeting iOS or tvOS platforms. Learn more in the UIViewController Tracing documentation.

When enabled, the SDK reports non-fully-blocking app hangs. Non-fully-blocking app hangs occur when the app appears stuck to the user but can still render a few frames. Fully-blocking app hangs are when the main thread is stuck completely and the app can't render a single frame.

Learn more in the App Hangs documentation.

Set this boolean to `false` to disable sending of client reports. Client reports are a protocol feature that let clients send status reports about themselves to Sentry. They are currently mainly used to emit outcomes for events that were never sent.

When enabled, the SDK adds breadcrumbs for each network request. This feature uses swizzling, so disabling `enableSwizzling` also disables this feature.

If you want to enable or disable network tracking for performance monitoring, use `enableNetworkTracking` instead.

Once enabled, this feature automatically captures HTTP client errors, like bad response codes, as error events and reports them to Sentry.

This feature is enabled by default starting with SDK version 8.0.0. Learn more in the HTTP Client Errors documentation.

The SDK will only capture HTTP Client errors if the HTTP Response status code is within the defined range.

Learn more in the HTTP Client Errors documentation.

An array of hosts or regexes that determines if HTTP Client errors will be automatically captured. This array can contain instances of `NSString` which should match the URL (using `contains`), and instances of `NSRegularExpression`, which will be used to check the whole URL.

The default value automatically captures HTTP Client errors of all outgoing requests. Learn more in the HTTP Client Errors documentation.

When enabled, the SDK extracts the GraphQL operation name from HTTP requests that have `Content-Type: application/json` and contain a JSON body with an `operationName` field. The operation name is then attached to HTTP breadcrumbs and failed request events.

Learn more in the GraphQL Operation Tracking documentation.

When enabled, the SDK sends logs to Sentry. You must explicitly set this option to `true` to enable log capturing.

Learn more about structured logging in the logs documentation.

When enabled, the SDK tracks watchdog terminations based on heuristics. This feature is available for iOS, tvOS, and Mac Catalyst. It only works if the application was in the foreground, and it doesn't track watchdog terminations for unit tests.

Learn more in the Watchdog Terminations documentation.

## Integration Configuration

For many platform SDKs integrations can be configured alongside it. On some platforms that happen as part of the `init()` call, in some others, different patterns apply.

**Removed in version 9.0.0** - Integrations are now automatically managed by the SDK. Use specific configuration options to control SDK features instead.

In some SDKs, the integrations are configured through this parameter on library initialization. For more information, please see our documentation for a specific integration.

**Removed in version 9.0.0** - Integrations are now automatically managed by the SDK.

This can be used to disable integrations that are added by default. When set to `false`, no default integrations are added.

This can be used to disable integrations that are enabled by default if the SDK detects that the corresponding framework or library is installed. When set to `false`, none of these integrations will be enabled by default, even if the corresponding framework/library is detected.

## Hooks

These options can be used to hook the SDK in various ways to customize the reporting of events.

This function is called with an SDK-specific message or error event object, and can return a modified event object, or `null` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

By the time  is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

This function is called with an SDK-specific breadcrumb object before the breadcrumb is added to the scope. When nothing is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the first argument, which contains the breadcrumb object.
The callback typically gets a second argument (called a "hint") which contains the original object from which the breadcrumb was created to further customize what the breadcrumb should look like.

This function is called with a span object before it is sent to Sentry. You can return a modified span object, or `null`, to skip sending the span. This can be used to filter or modify spans before they are sent.

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.beforeSendSpan = { span in
        // Filter out spans with certain operations
        if span.operation == "db.query" {
            return nil
        }
        return span
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.beforeSendSpan = ^SentrySpan * _Nullable(SentrySpan * _Nonnull span) {
        // Filter out spans with certain operations
        if ([span.operation isEqualToString:@"db.query"]) {
            return nil;
        }
        return span;
    };
}];
```

This function is called with a log object before it is sent to Sentry. You can return a modified log object, or `null` to skip sending the log. This can be used to filter or modify logs before they are sent.

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.enableLogs = true
    options.beforeSendLog = { log in
        // Filter out info level logs
        if log.level == .info {
            return nil
        }
        return log
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.enableLogs = YES;
    options.beforeSendLog = ^SentryLog * _Nullable(SentryLog * _Nonnull log) {
        // Filter out info level logs
        if (log.level == SentryLogLevelInfo) {
            return nil;
        }
        return log;
    };
}];
```

Learn more about log filtering in the logs documentation.

This function is called to decide if the SDK should capture a screenshot. Return `true` to allow screenshot capture, or `false` to prevent it.

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.attachScreenshot = true
    options.beforeCaptureScreenshot = {
        // Prevent screenshots in certain views
        return !isSensitiveView()
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.attachScreenshot = YES;
    options.beforeCaptureScreenshot = ^BOOL {
        // Prevent screenshots in certain views
        return !isSensitiveView();
    };
}];
```

This function is called to decide if the SDK should capture a view hierarchy. Return `true` to allow view hierarchy capture, or `false` to prevent it.

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.attachViewHierarchy = true
    options.beforeCaptureViewHierarchy = {
        // Prevent view hierarchy capture in certain views
        return !isSensitiveView()
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.attachViewHierarchy = YES;
    options.beforeCaptureViewHierarchy = ^BOOL {
        // Prevent view hierarchy capture in certain views
        return !isSensitiveView();
    };
}];
```

A block called after SDK initialization when the last execution terminated with a crash. This callback is invoked synchronously during SDK initialization, so keep any work here minimal.

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.onCrashedLastRun = {
        // Perform actions when a crash was detected on last run
        print("App crashed on last run")
    }
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.onCrashedLastRun = ^{
        // Perform actions when a crash was detected on last run
        NSLog(@"App crashed on last run");
    };
}];
```

## Tracing Options

A number between `0` and `1`, controlling the percentage chance a given transaction will be sent to Sentry. (`0` represents 0% while `1` represents 100%.) Applies equally to all transactions created in the app. Either this or  must be defined to enable tracing.

A function responsible for determining the percentage chance a given transaction will be sent to Sentry. It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent). Can also be used for filtering transactions, by returning 0 for those that are unwanted. Either this or  must be defined to enable tracing.

An optional property that controls which downstream services receive tracing data, in the form of a `sentry-trace` and a `baggage` header attached to any outgoing HTTP requests.

The option may contain a list of strings or regex against which the URLs of outgoing requests are matched.
If one of the entries in the list matches the URL of an outgoing request, trace data will be attached to that request.
String entries do not have to be full matches, meaning the URL of a request is matched when it _contains_ a string provided through the option.

If  is not provided, trace data is attached to every outgoing request from the instrumented client.

This option is available as of [version 9.0.0](https://github.com/getsentry/sentry-cocoa/blob/main/CHANGELOG.md#9000).

If set to `true`, the SDK adds the [W3C `traceparent` header](https://www.w3.org/TR/trace-context/) to outgoing HTTP requests.
This header is attached in addition to the `sentry-trace` and `baggage` headers.
Set this option to `true` if your backend services are instrumented with a W3C Trace Context compatible library such as OpenTelemetry and you want to continue traces from the client.

Use  to control which requests the `traceparent` header is attached to.

This feature is experimental and may have bugs. It's available from [version 8.41.0](https://github.com/getsentry/sentry-cocoa/blob/main/CHANGELOG.md#8410).

When enabled, the SDK finishes the ongoing transaction bound to the scope and links them to the crash event when your app crashes. This allows you to see the performance data leading up to a crash, helping you understand what was happening when the crash occurred.

The SDK skips adding profiles to increase the chance of keeping the transaction.

This feature requires that tracing is enabled via  or .

## Screenshot Options

Screenshot options allow you to configure how screenshots are captured and masked when attached to error events. These options are available under `options.screenshot`.

Learn more about screenshot options in the Screenshots documentation.

When enabled, all text content in screenshots is masked. This helps ensure that no sensitive text data is exposed in screenshots sent to Sentry.

When enabled, all images in screenshots are masked. This helps ensure that no sensitive image data is exposed in screenshots sent to Sentry.

A list of view class names that should be masked in screenshots. Views matching these class names will have their content masked.

A list of view class names that should not be masked in screenshots, even if other masking options are enabled. Views matching these class names will be shown without masking.

When enabled, uses the faster view renderer V2 for capturing screenshots. This renderer reduces the performance impact of screenshot capture.

This option is enabled by default starting with SDK version 8.50.0.

When enabled, uses faster but potentially incomplete view rendering for screenshots. This can improve performance but may result in some views not being fully rendered.

## Session Replay Options

Session Replay options allow you to configure how session replays are recorded and sent to Sentry. These options are available under `options.sessionReplay`.

When enabled, uses faster but potentially incomplete view rendering for session replays. This can improve performance but may result in some views not being fully rendered in the replay.

We discourage using this option as it can result in incomplete or missing views in session replays, which may make debugging more difficult. Only enable this option if you understand the trade-offs and have thoroughly tested your application.

Learn more about session replay performance in the Performance Overhead documentation.

## Profiling Options

Profiling options allow you to configure how profiling data is collected. These options are available under `options.configureProfiling`.

When enabled, the profiler starts as early as possible during the app lifecycle, allowing you to profile app startup performance.

Learn more about profiling in the Profiling documentation.

## Network & Performance Options

A read-only property that indicates whether tracing is enabled. This property is `true` when either  or  is configured.

When enabled, the SDK tracks performance for UIViewController subclasses and HTTP requests automatically. It also measures the app start and slow and frozen frames.

Performance Monitoring must be enabled for this flag to take effect. Learn more about Performance Monitoring.

When enabled, the SDK creates transactions for UI events like button clicks, switch toggles, and other UI elements that use UIControl `sendAction:to:forEvent:`.

This feature is unavailable for SwiftUI. Learn more in the User Interaction Tracing documentation.

Report pre-warmed app starts by dropping the first app start spans if pre-warming paused during these steps. This approach will shorten the app start duration, but it represents the duration a user has to wait after clicking the app icon until the app is responsive.

This option is enabled by default starting with SDK version 9.0.0. Learn more in the Prewarmed App Start Tracing documentation.

When enabled, the SDK tracks performance for HTTP requests if auto performance tracking and `enableSwizzling` are enabled.

Learn more in the Network Tracking documentation.

When enabled, the SDK tracks performance for file I/O reads and writes with NSData if auto performance tracking and `enableSwizzling` are enabled.

Learn more in the File I/O Tracing documentation.

When enabled, the SDK tracks the performance of Core Data operations. It requires enabling performance monitoring.

Learn more in the Core Data Tracing documentation.

When enabled, every UIViewController tracing transaction will wait for a call to `SentrySDK.reportFullyDisplayed()`. Use this in conjunction with `enableUIViewControllerTracing`. If `SentrySDK.reportFullyDisplayed()` is not called, the transaction will finish automatically after 30 seconds and the `Time to full display` span will be finished with a `DeadlineExceeded` status.

Learn more in the Time to Full Display documentation.

Set as the delegate on the URLSession used for network tasks. This allows you to customize the URLSession behavior while still allowing Sentry to track network requests.

Use a custom URLSession with your configuration for sending requests to Sentry. This allows you to use your own URLSession configuration, for example, to configure proxy settings or custom SSL certificates.

## Swizzling Options

Whether the SDK should use swizzling or not. When turned off, the following features are disabled: breadcrumbs for touch events and navigation with UIViewControllers, automatic instrumentation for UIViewControllers, automatic instrumentation for HTTP requests, automatic instrumentation for file I/O with NSData, and automatically added sentry-trace header to HTTP requests for distributed tracing.

Learn more in the Swizzling documentation.

A set of class names to exclude from swizzling. The SDK checks whether the class’s name contains any value in this list. If it does, the class is skipped. For example, if you add `MyUIViewController` to this list, the SDK excludes the following classes from swizzling: `YourApp.MyUIViewController`, `YourApp.MyUIViewControllerA`, `MyApp.MyUIViewController`.

This option is available with SDK version 8.23.0 and above. Learn more in the Swizzling documentation.

When enabled, the SDK tracks performance for file I/O reads and writes with NSData if auto performance tracking and `enableSwizzling` are enabled.

Learn more in the File I/O Tracing documentation.

When enabled, the SDK tracks performance for file I/O operations with NSFileManager if auto performance tracking and `enableSwizzling` are enabled.

This feature is currently experimental and disabled by default. Learn more in the File I/O Tracing documentation.

## App Hang Options

When enabled, the SDK tracks when the application stops responding for a specific amount of time defined by the `appHangTimeoutInterval` option.

On iOS, tvOS and visionOS, the SDK can differentiate between fully-blocking and non-fully-blocking app hangs. A fully-blocking app hang is when the main thread is stuck completely, and the app can't render a single frame. A non-fully-blocking app hang is when the app appears stuck to the user but can still render a few frames.

App Hang tracking is automatically disabled if a debugger is attached. Learn more in the App Hangs documentation.

The minimum amount of time an app should be unresponsive to be classified as an App Hang. The actual amount may be a little longer.

Avoid using values below 100 ms, as this can result in a high volume of app hang events being sent.

Learn more in the App Hangs documentation.

## MetricKit Options

When enabled, the SDK subscribes to MetricKit diagnostic reports and sends MXHangDiagnostic, MXDiskWriteExceptionDiagnostic, and MXCPUExceptionDiagnostic to Sentry.

This feature is available on SDK version 8.14.0 and up. The SDK supports this feature from iOS 15 and up and macOS 12 and up because in these versions, MetricKit delivers diagnostic reports immediately, which allows the Sentry SDK to apply current data from the scope.

Learn more in the MetricKit documentation.

When enabled, the SDK adds the raw MXDiagnosticPayloads as an attachment to the converted SentryEvent. You need to enable `enableMetricKit` for this flag to work.

This feature is available on SDK version 8.29.0 and up.

Learn more in the MetricKit documentation.

## Other Options

When enabled, the SDK adds breadcrumbs for various system events.

The maximum size for each attachment in bytes.

Please also check the maximum attachment size of relay to make sure your attachments don't get discarded there.

If enabled, the view hierarchy attachment will contain view `accessibilityIdentifier`. Set it to `false` if your project uses `accessibilityIdentifier` for PII.

This feature is only available from Xcode 13 and from macOS 12.0, iOS 15.0, tvOS 15.0, watchOS 8.0.

This is an experimental feature and may still have bugs. When enabled, the SDK stitches the call to Swift Async functions in one consecutive stack trace.

Learn more in the Experimental Features documentation.

The path where the SDK stores data (events, transactions, profiles, etc.). By default, the SDK uses `NSCachesDirectory`. You can specify a custom path if needed.

We recommend only changing this when the default can't be accessed, such as in security environments.

## Spotlight

Whether to enable Spotlight for local development. Spotlight is a local development tool that allows you to inspect Sentry events locally.

This option is primarily useful for local development and debugging.

The Spotlight URL for local development.

This option is only used when  is set to `true`.

