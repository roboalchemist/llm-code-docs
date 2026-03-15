# Source: https://posthog.com/docs/session-replay/console-log-recording.md

# Console logs recording - Docs

PostHog can capture console logs, info, warnings, and errors from your application. This is useful for debugging and providing extra context on what is happening in your user's browser or mobile device environment.

## Web

As console logs can contain sensitive information, we do not capture these logs automatically. You can enable this feature globally *either* from your [project settings](https://us.posthog.com/settings/project-replay#replay) **or** client-side by setting `enable_recording_console_log: true` in our [JavaScript Web SDK config](/docs/libraries/js/config.md).

Web

PostHog AI

```javascript
posthog.init('<ph_project_token>', {
  api_host: 'https://us.i.posthog.com',
  defaults: '2026-01-30',
    enable_recording_console_log: true,
    // ... other options
})
```

> **Important:** Individual console logs are truncated at 2000 characters. The rest of the log is not sent to PostHog. When truncating a log message we add `...[Truncated]` to the message.

## Android

You can enable this feature from your client-side by setting `captureLogcat = true` in our [Android SDK config](/docs/session-replay/installation/android.md#step-two-configure-replay-settings).

Android

PostHog AI

```kotlin
val config = PostHogAndroidConfig(apiKey = "<ph_project_token>").apply {
    // Enable session recording. Requires enabling in your project settings as well.
    // Default is false.
    sessionReplay = true
    // Capture logs automatically. Default is true.
    // Remote configuration via project settings requires SDK version 3.32.0 or higher.
    sessionReplayConfig.captureLogcat = true
    ...
}
```

## React Native

You can enable this feature from your client-side by setting `captureLog: true` in our [React Native SDK config](/docs/session-replay/installation/react-native.md#step-two-configure-replay-settings).

> **Note:** Console log recording is only available for Android.

TypeScript

PostHog AI

```typescript
export const posthog = new PostHog(
  '<ph_project_token>',
  {
    // Enable session recording. Requires enabling in your project settings as well.
    // Default is false.
    enableSessionReplay: true,
    sessionReplayConfig: {
      // Capture logs automatically. Default is true.
      // Android only (Native Logcat only)
      // Remote configuration via project settings requires SDK version 4.35.0 or higher.
      captureLog: true,
      ...
    },
  },
);
```

## iOS

As console logs can contain sensitive information, we do not capture these logs automatically. You can enable this feature from your client-side by setting `captureLogs = true` in our [iOS SDK config](/docs/session-replay/installation/ios.md#step-two-enable-session-recordings-in-your-project-settings).

iOS

PostHog AI

```swift
let config = PostHogConfig(apiKey: "<ph_project_token>", host: "https://us.i.posthog.com")
config.sessionReplay = true
// Remote configuration via project settings requires SDK version 3.41.1 or higher.
config.sessionReplayConfig.captureLogs = true
PostHogSDK.shared.setup(config)
```

> **Important:** Individual console logs are truncated at 2000 characters. The rest of the log is not sent to PostHog. When truncating a log message we add ...\[Truncated\] to the message.

### Sanitizing or skipping logs

PostHog iOS SDK allows you to customize how log messages are processed and categorized by providing a custom `logSanitizer` handler.

This handler is called for each new line printed to the console. It receives the line's content and can return either a processed log entry with its severity level, or `nil` to skip the log entirely:

iOS

PostHog AI

```swift
let config = PostHogConfig(apiKey: "<ph_project_token>", host: "https://us.i.posthog.com")
// Custom log processing and sanitization
config.sessionReplayConfig.captureLogsConfig.logSanitizer = { output in
    // Skip trace-level logs
    guard !output.contains("TRACE") else {
        return nil
    }
    // Determine log level based on message content
    let level: PostHogLogLevel = {
        if output.contains("CRITICAL") { return .error }
        if output.contains("WARN") { return .warn }
        return .info
    }()
    // Remove sensitive information (e.g., auth tokens)
    let sanitizedMessage = output.replacingOccurrences(
        of: #"Bearer\s+[A-Za-z0-9-._~+/]+=*"#,
        with: "Bearer [TOKEN REDACTED]",
        options: .regularExpression
    )
    return PostHogLogEntry(level: level, message: sanitizedMessage)
}
PostHogSDK.shared.setup(config)
```

### Configuring minimum log level

By default, the SDK only captures error-level logs to minimize noise in session replays. You can adjust this using the `minLogLevel` setting:

iOS

PostHog AI

```swift
// Capture errors only (default)
config.sessionReplayConfig.captureLogsConfig.minLogLevel = .error
// Capture warnings and errors
config.sessionReplayConfig.captureLogsConfig.minLogLevel = .warn
// Capture all logs (most verbose)
config.sessionReplayConfig.captureLogsConfig.minLogLevel = .info
```

Only logs with a level greater than or equal to the `minLogLevel` will be captured. For example, if set to `.warn`, both **warning** and **error** logs will be captured, but **info** logs will be filtered out.

### Default behavior

#### Log level

The SDK captures raw console output directly, independent of any specific logging framework or implementation. Since the raw output doesn't inherently carry log level information, the SDK deduces severity levels by analyzing the log content. By default, the SDK automatically classifies log messages into three severity levels:

-   **Error** (highest severity)

    -   Messages containing: "error", "exception", "fail", "failed"
    -   OSLog entries with type "Error" or "Fault"
-   **Warning** (medium severity)

    -   Messages containing: "warning", "warn", "caution", "deprecated"
    -   OSLog entries with type "Warning"
-   **Info** (lowest severity)

    -   All other messages that don't match error or warning patterns

#### Filtering and processing

-   Log filtering based on `minLogLevel` (default: `.error`). Only logs with equal or higher severity are captured.
-   Multi-line logs are automatically split into separate entries
-   OSLog metadata (e.g., subsystem, category) is automatically removed for cleaner output

The SDK captures logs from:

-   Standard output (stdout)
-   Standard error (stderr)
-   OSLog messages
-   NSLog messages

## Viewing and searching console logs

Once enabled, you can then view captured console logs by clicking the "Inspector" button and choosing the console tab.

![Logs in session replay](https://res.cloudinary.com/dmukukwp6/image/upload/v1715340828/posthog.com/contents/images/docs/session-replay/log-light.png)![Logs in session replay](https://res.cloudinary.com/dmukukwp6/image/upload/v1715340827/posthog.com/contents/images/docs/session-replay/log-dark.png)

In that tab, you can search for specific logs with the following patterns:

| Token | Match Type | Description |
| --- | --- | --- |
| jscript | fuzzy-match | Items that fuzzy match jscript |
| =scheme | exact-match | Items that are scheme |
| 'python | include-match | Items that include python |
| !ruby | inverse-exact-match | Items that do not include ruby |
| ^java | prefix-exact-match | Items that start with java |
| !^earlang | inverse-prefix-exact-match | Items that do not start with earlang |
| .js$ | suffix-exact-match | Items that end with .js |
| !.go$ | inverse-suffix-exact-match | Items that do not end with .go |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better