# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/agent-desk/integrations/ios-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/miscellaneous-apis.md

# Miscellaneous APIs

## Conversation Status

To get the current `ASAPPConversationStatus`, implement the `conversationStatusHandler` callback:

```kotlin  theme={null}
ASAPP.instance.conversationStatusHandler = { conversationStatus ->
    // Handle conversationStatus.isLiveChat and conversationStatus.unreadMessages
}
```

* If `isLiveChat` is `true`, the customer is currently connected to a live support agent or in a queue.
* The `unreadMessages` integer indicates the number of new messages received since last entering Chat.

### Trigger the Conversation Status Handler

You can trigger this handler in two ways:

1. Manually trigger it with:

```kotlin  theme={null}
ASAPP.instance.fetchConversationStatus()
```

The Chat SDK will fetch the status asynchronously and callback to `conversationStatusHandler` once it is available.

2. The handler may be triggered when a push notification is received if the application is in the foreground. If your application handles Firebase push notifications, use:

```kotlin  theme={null}
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        val wasFromAsapp = ASAPP.instance.onFirebaseMessageReceived(message)
        // Additional handling...
    }
}
```

<Note>
  The Chat SDK only looks for conversation status data in the payload and doesn't cache or persist analytics. If the push notification was sent from ASAPP, the SDK returns true and triggers the `conversationStatusHandler` callback.
</Note>

## Debug Logs

By default, the SDK only prints error logs to the console output. To allow the SDK to log warnings and debug information, use `setDebugLoggingEnabled`.

```kotlin  theme={null}
ASAPP.instance.setDebugLoggingEnabled(BuildConfig.DEBUG)
```

<Note>
  Disable debug logs for production use.
</Note>

## Clear the Persisted Session

To clear the ASAPP session persisted on disk:

```kotlin  theme={null}
ASAPP.instance.clearSession()
```

<Note>
  Only use this when an identified user signs out. Don't use for anonymous users, as it will cause chat history loss.
</Note>

## Setting an Intent

### Open Chat with an Initial Intent

```kotlin  theme={null}
ASAPP.instance.openChat(context, asappIntent = mapOf("Code" to "EXAMPLE_INTENT"))
```

To set the intent while chat is open, use `ASAPP.instance.setASAPPIntent()`. Only call this if chat is already open. Use `ASAPP.instance.doesASAPPActivityExist` to verify if the user is in chat.

## Handling Chat Events

Implement the `ASAPPChatEventHandler` interface to react to specific chat events:

```kotlin  theme={null}
ASAPP.instance.chatEventHandler = object : ASAPPChatEventHandler {
    override fun handle(name: String, data: Map<String, Any>?) {
        // Handle chat event
    }
}
```

<Note>
  These events relate to user flows inside chat, not user behavior like button clicks.
</Note>

### Implement Chat end, New Issue, and Agent Assigned

To track the `end of a chat`, or add custom codes on `new issue` and `agent assigned` implement the following custom events

<Tip>
  In this example, the event messages are shown as Toasts. But you add any custom code here.
</Tip>

```kotlin  theme={null}
chatEventHandler = object : ASAPPChatEventHandler {
                override fun handle(name: String, data: Map<String, Any>?) {
                    if (name == CustomEvent.CHAT_CLOSED.name) {
                        Toast.makeText(applicationContext,
                            "Chat is closed",
                            Toast.LENGTH_LONG).show()
                    } else if (name == CustomEvent.NEW_ISSUE.name) {
                        Toast.makeText(applicationContext,
                            "New Issue event received",
                            Toast.LENGTH_LONG).show()
                    } else if (name == CustomEvent.AGENT_ASSIGNED.name) {
                        Toast.makeText(applicationContext,
                            "Agent is assigned",
                            Toast.LENGTH_LONG).show()
                    }
                }
            }
```

<Note>
  Chat end implementation is available for the SDK version 10.3.1 and above.
</Note>
