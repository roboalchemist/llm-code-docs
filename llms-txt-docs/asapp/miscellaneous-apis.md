# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/messaging-platform/integrations/android-sdk/miscellaneous-apis.md

# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/miscellaneous-apis.md

# Miscellaneous APIs

## Conversation Status

Call `ASAPP.getChatStatus(success:failure:)` to get the current conversation status. The first parameter of the success handler provides a count of unread messages, while the second indicates whether the chat is live. If `isLive` is true, it means the customer is currently connected to a live customer support agent, even if the user isn't currently on the chat screen or the application is in the background.
**Example:**

```json  theme={null}
ASAPP.getChatStatus(success: { unread, isLive in
    DispatchQueue.main.async { [weak self] in
        self?.updateBadge(count: unread, isLive: isLive)
    }
}, failure: { error in
    print("Could not get chat status: \(error)")
})
```

## Debug Logs

To allow the SDK to print more debugging information to the console, set `ASAPP.debugLogLevel` to.debug. Please see [`ASAPPLogLevel`](https://docs-sdk.asapp.com/api/chatsdk/ios/latest/Enums/ASAPPLogLevel.html) for more options and make sure to set the level to `.errors` or `.none` in release builds.
Example:

```json  theme={null}
#if DEBUG
ASAPP.debugLogLevel = .debug
#else
ASAPP.debugLogLevel = .none
#endif
```

## Clear the Persisted Session

To clear the session persisted on disk, call `ASAPP.clearSavedSession()`. This will also disable push notifications to the customer.

## Set an Intent

To open chat with an initial intent, call one of the two functions below, passing in a dictionary specifying the intent in a format provided by ASAPP. Please ask your Implementation Manager for details.

### Create a Chat View Controller with an Initial Intent

```json  theme={null}
let chat = ASAPP.createChatViewControllerForPushing(withIntent: [“Code”: 
“EXAMPLE_INTENT”])
or
let chat = ASAPP.createChatViewControllerForPresenting(withIntent: 
[“Code”: “EXAMPLE_INTENT”])
```

To set the intent while chat is already open, call `ASAPP.setIntent(_:)`, passing in a dictionary as described above. This should only be called if a chat view controller already exists.

## Handle Chat Events

Certain agreed-upon events may occur during chat. To react to these events, implement the `ASAPPDelegate` protocol, including the `chatViewControllerDidReceiveChatEvent(name:data:)` method. Please ask your Implementation Manager if you have questions regarding chat event names and data.

## Send

This API is primarily used to send information that is used to show a proactive chat prompt when a specific criteria or set of criteria are met. To use and trigger this API, create data structure like below and call ASAPP.updateCustomerDataInfo() method.

```json  theme={null}
let customerInfo: [String: Any] = [
    "CustomerInfo": [
        "key1": "value1"
        "OrangeKey": "A Key",
        "FirstName": "A name",
        "key4": "value4"
    ]
]
ASAPP.updateCustomerDataInfo(customerParams: customerInfo)
```

This API is primarily used to send information that is used to show a proactive chat prompt.
\##Custom Chat Events
To track the 'end of a chat', or add custom codes on 'new issue' and 'agent assigned', implement the following custom events.

```json  theme={null}
 func chatViewControllerDidReceiveEndChatEvent(eventData: [String: Any]?) {
  if let eventDetails = eventData {
        let issueId = eventDetails["issueId"] as? Int64
        let customerId = eventDetails["customerId"] as? Int64
        let eventTime = eventDetails["eventTime"] as? Double
        let eventId = eventDetails["eventId"] as? String
        let eventName = eventDetails["eventName"] as? String
        if eventName == "issue:end" {
            //This code block will be triggered when a chat conversation is ended
        } else if eventName == "issue:new" {
            //This code block will be triggered when a user taps “New Question” or new issue is created
        } else if eventName == "agent:assigned" {
            //This code block will be triggered when a new agent has been assigned
        }
    }
}
```
