# Source: https://docs.luciq.ai/references/sdk-event-handlers/set-on-new-message-handler.md

# Set Received-Reply Handler

Use this handler to run specific code each time a new message is received by the SDK.

This block is executed each time a new message is received. This can be used to show your own UI when a new message is received when default chat notifications are disabled, for example.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Replies.didReceiveReplyHandler = {
    // Notify users about new message.
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQReplies.didReceiveReplyHandler = ^{
    // Notify users about new message.
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.setOnNewReplyReceivedCallback(new Runnable() {
	//Your code goes here.
});
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setOnNewReplyReceivedCallback(new Runnable() {
  @Override
  public void run() {
    //Show an alert to notify users about a new message.
  }
});
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.setOnNewReplyReceivedHandler(function () {
    //Create custom alert
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Replies.setOnNewReplyReceivedCallback(Function function);
```

{% endtab %}
{% endtabs %}
