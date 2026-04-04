# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-in-app-replies/in-app-replies-callbacks.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-in-app-replies/in-app-replies-callbacks.md

# In-App Replies Callbacks

### New Received Message

This block is executed each time a new message is received in the SDK. This can be used to show your own UI when a new message is received when default chat notifications are disabled.

{% code title="Dart" %}

```dart
Replies.setOnNewReplyReceivedCallback(Function function);
```

{% endcode %}
