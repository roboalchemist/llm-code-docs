# Source: https://docs.logrocket.com/reference/android-capture-exceptions.md

# Capture Exceptions

Capture exceptions to surface in the LogRocket dashboard for Android

## Manually surface exceptions in LogRocket

The LogRocket Android SDK will automatically capture uncaught exceptions which trigger a crash. The SDK does not automatically capture exceptions which are caught in your application. To manually surface these in LogRocket, use the `com.logrocket.core.Logger `utility

```swift
import com.logrocket.core.Logger;

Logger.captureException(Throwable error);
```