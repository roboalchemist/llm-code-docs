# Source: https://docs.logrocket.com/reference/ios-capture-exceptions.md

# Capture Exceptions and Errors

Add exceptions into the LogRocket dashboard for iOS

## Manually surface exceptions and errors

Use `Logger.captureException()` to manually report an exception in your application. 3 different exception and error types can be captured.

1. NSExceptions - The captured exception will include the stack frames included with the NSException object.

```Text objective-c
[LROLogger captureExceptionWithException:exception];
```

2. NSError - The captured exception will include the stack frames of where `captureException` was called and not where the error occurred, as NSError objects do not include stack frames.

```Text objective-c
[LROLogger captureExceptionWithError:error];
```

3. Error - The captured exception will include the stack frames of where `captureException` was called and not where the error occurred, as Error objects do not include stack frames.

```Text Swift
Logger.captureException(error: error)  

// For Example:
enum TestError: Error {
  case runtimeError(String)
}

do {
  throw TestError.runtimeError("My exception")
} catch {
  Logger.captureException(error: error)
}
```