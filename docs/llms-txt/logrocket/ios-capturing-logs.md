# Source: https://docs.logrocket.com/reference/ios-capturing-logs.md

# Capture Application Logs

Surface application logs in LogRocket sessions

Application logs on iOS are automatically captured.

### Disable Log Capture

To disable the automatic log capture, initialize the SDK with the `logCaptureEnabled` set to `false`.

```swift
let configuration = Configuration(appID: "<APP_SLUG>", logCaptureEnabled: false)
SDK.initialize(configuration: configuration)
```

### Manual Log Capture

Our iOS SDK includes a `Logger` interface for capturing logs manually:

```swift
import LogRocket

Logger.debug("Debug level message")
Logger.info("Info level message")
Logger.warning("Warning level message")
Logger.error("Error level message")
```