# Source: https://docs.logrocket.com/reference/capture-error-messages.md

# Capture Error Messages

Capture custom error messages to surface in the LogRocket dashboard for iOS

## Manually surface error messages in LogRocket

Use the `CaptureMessageBuilder` class to manually report a message. This message will be treated as an error within LogRocket.

```swift
let builder = CaptureMessageBuilder("This is a captured message")
  .putTag("subscription", "Pro")
  .putTag("monthly", false)
  .putTag("price", 15.99)
  .putExtra("pageName", "ProfileView")
  .putExtra("age", 42)

SDK.captureMessage(builder)  // Capture the event
```

Add `tag` and `extra` fields to send extra metadata about the message. String, Bool, Int, and Double `tag` and `extra` types are supported. Tags and extra data will appear with the error in the Issues view of the LogRocket dashboard.