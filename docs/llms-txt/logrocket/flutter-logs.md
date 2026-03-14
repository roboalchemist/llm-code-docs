# Source: https://docs.logrocket.com/reference/flutter-logs.md

# Application Logs

Capture Flutter application logs

## Print Logs

Flutter application print statements are automatically captured by LogRocket when the application has been [wrapped by LogRocket](https://docs.logrocket.com/reference/initialize-flutter#initializing-the-sdk).

### Disable Print Capture

To disable the automatic print capture, set LogRocket SDK wrap option `logCaptureEnabled`  to false.

```dart Flutter
LogRocketWrapConfiguration(
  logCaptureEnabled: false,
)
```

## Manual Log Capture

Our iOS SDK includes a functions to manually capture logs. This can be useful to capture logs in LogRocket without printing them on the device. It can also be used to explicitly capture specific logs when automatic log capture is disabled.

```dart Flutter
// Option 1: Use the `log` method and provide a log level.
LogRocket.log(LogRocketLogLevel.INFO, 'log information');

// Option 2: Use speicifc log level methods.
LogRocket.error('Error level message');
LogRocket.warn('Warning level message');
LogRocket.info('Info level message');
LogRocket.debug('Debug level message');
```