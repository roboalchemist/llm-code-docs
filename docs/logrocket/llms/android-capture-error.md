# Source: https://docs.logrocket.com/reference/android-capture-error.md

# Capture Error Messages

Capture custom error messages to surface in the LogRocket dashboard

## Manually surface error messages in LogRocket

Use the `CaptureMessageBuilder` class to manually report a message. This message will be treated as an error within LogRocket.

```java
CaptureMessageBuilder builder = new CaptureMessageBuilder("This is a captured message");
builder.putTag("subscription", "Pro");
builder.putTag("monthly", false);
builder.putTag("price", 15.99);
builder.putExtra("pageName", "ProfileView");
builder.putExtra("age", 42);

SDK.captureMessage(builder);  // Capture the event
```

Add `tag` and `extra` fields to send extra metadata about the message. String, boolean, int, and double `tag` and `extra` types are supported. Tags and extra data will appear with the error in the Issues view of the LogRocket dashboard.