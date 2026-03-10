# Source: https://firebase.google.com/docs/cloud-messaging/unity/receive-messages.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/receive-messages) [Android](https://firebase.google.com/docs/cloud-messaging/android/receive-messages) [Web](https://firebase.google.com/docs/cloud-messaging/web/receive-messages) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/receive-messages) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/receive-messages) |

<br />

To receive messages, your app must assign a callback to the
[`Firebase.Messaging.FirebaseMessaging.MessageReceived`](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#messagereceived)
event handler.

### `MessageReceived` Event

By overriding assigning a callback to [`Firebase.Messaging.FirebaseMessaging.MessageReceived`](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#messagereceived)
you can perform actions based on the received message and get the message
data:

    public void OnMessageReceived(object sender, Firebase.Messaging.MessageReceivedEventArgs e) {
      UnityEngine.Debug.Log("From: " + e.Message.From);
      UnityEngine.Debug.Log("Message ID: " + e.Message.MessageId);
    }

Messages can represent different kinds of incoming data. Most commonly,
messages are sent to the app after being initiated by the developer. Messages
are also sent to your app to represent message sent events, message send error
events, and messages deleted events. These special events can be
differentiated by checking the `Message::message_type` field.

### Messages Deleted

Sent to your app when the FCM server deletes pending messages.
`Message::message_type` will be `"deleted_messages"`. Messages may be deleted
due to:

1. Too many messages stored on the FCM server.

   This can occur when an app's servers send a bunch of [non-collapsible messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types)
   to FCM servers while the device is offline.
2. The device hasn't connected in a long time and the app server has
   recently (within the last 4 weeks) sent a message to the app on that
   device.

   It is recommended that the app do a full sync with the app
   server after receiving this call.

### Send Event

Called when an upstream message has been successfully sent to FCM.
`MessageType` will be `"send_event"`.

### Send Error

Called when there was an error sending an upstream message.
`MessageType` will be `"send_error"`.