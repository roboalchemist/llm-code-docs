# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/in-app-replies/in-app-chat-event-handlers.md

# In-App Chat Event Handlers

## New Received Message

This block is executed each time a new message is received in the SDK. Use it to show your own UI when a new message is received (for example when default chat notifications are disabled).

{% code title="JavaScript" %}

```javascript
Replies.setOnNewReplyReceivedHandler(function () {
    // Create custom alert
});
```

{% endcode %}

{% hint style="info" %}
You can set custom data (such as a user attribute) at any time, including inside event handlers. Logging user events from event handlers is possible as well.
{% endhint %}
