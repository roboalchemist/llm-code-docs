# Source: https://docs.logrocket.com/reference/flutter-exceptions.md

# Capture Exceptions

Capture Flutter Exceptions and Errors in LogRocket

Manual exception capture can be used to capture any exception which is caught by your application

## Capture Exceptions

Use `LogRocket.captureException(Exception exception, [StackTrace? stackTrace])` to manually capture exceptions.

```dart Flutter
try {
  throw FormatException('Stop! Invalid format!');
} on Exception catch (exception, stackTrace) {
  LogRocket.captureException(exception, stackTrace);
}
```

## Capture Errors

Use `LogRocket.captureError(Error error)` to manually capture runtime errors.

```dart Flutter
try {
  dynamic foo = true;
  print(foo++); // Runtime error
} on Error catch (error) {
  LogRocket.captureError(error);
}
```