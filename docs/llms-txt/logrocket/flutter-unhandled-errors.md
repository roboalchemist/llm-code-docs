# Source: https://docs.logrocket.com/reference/flutter-unhandled-errors.md

# Unhandled Errors and Exceptions

Capture Flutter Unhandled Errors and Exceptions in LogRocket 

Unhandled errors or exceptions thrown by a Flutter application are automatically captured by LogRocket when the application has been [wrapped by LogRocket](https://docs.logrocket.com/reference/initialize-flutter#initializing-the-sdk).

### Disable Error Capture

To disable automatically capturing unhandled errors, set LogRocket SDK wrap option `errorCaptureEnabled` to `false`.

```dart Flutter
LogRocketWrapConfiguration(
  errorCaptureEnabled: false,
)
```