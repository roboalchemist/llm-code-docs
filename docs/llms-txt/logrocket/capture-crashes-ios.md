# Source: https://docs.logrocket.com/reference/capture-crashes-ios.md

# Capture Crashes (iOS)

LogRocket automatically detects Crashes in your iOS application. After a crash occurs, LogRocket will upload the crash report the next time the app is reopened and LogRocket is initialized.

<Callout icon="🚧">
  Crash reports are not captured when the Xcode debugger is attached to the application. The Xcode debugger "traps" crashes and prevents them from fully occurring, stopping execution on a breakpoint. This prevents the LogRocket SDK from seeing that crash occurred.
</Callout>

Crash reporting can be disabled by setting Configuration option:

```swift
SDK.initialize(configuration: Configuration(
  ...
  unexpectedExceptionCaptureEnabled: false,
  ...
))

```

<br />