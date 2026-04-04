# Source: https://firebase.google.com/docs/cloud-messaging/cpp/receive-messages.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/receive-messages) [Android](https://firebase.google.com/docs/cloud-messaging/android/receive-messages) [Web](https://firebase.google.com/docs/cloud-messaging/web/receive-messages) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/receive-messages) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/receive-messages) |

<br />

To receive downstream messages, each client app needs to implement the methods
on the
[`firebase::messaging::Listener`](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener)
API.

## Initialize FCM

Before you can use FCM to get access to your registration token or
receive messages it must be initialized.

To initialize FCM, call
[`::firebase::messaging::Initialize`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#initialize)
and supply it with your [`::firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app)
object as well as an implementation of the
[`::firebase::messaging::Listener`](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener)
class.

    MyListener my_listener_implementation;
    ::firebase::messaging::Initialize(app, &my_listener_implementation);

## Access the registration token

On initial startup of your app, the FCM SDK generates a registration
token for the client app instance. If you want to target single devices, or
create device groups for FCM, you'll need to access this token.

You can access the token's value through the
[`::firebase::messaging::Listener::OnTokenReceived`](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#ontokenreceived)
virtual function.

    void OnTokenReceived(const char* token) {
      LogMessage("The registration token is `%s`", token);

      // TODO: If necessary send token to application server.
    }

## Receive and handle messages

To receive messages, your Listener class must implement the
[`OnMessage`](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#onmessage)
virtual function.

#### Override `OnMessage`

By overriding the method [`::firebase::messaging::Listener::OnMessage`](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#onmessage),
you can perform actions based on the received message and get the message
data:

    void OnMessage(const ::firebase::messaging::Message& message) {
      LogMessage(TAG, "From: %s", message.from.c_str());
      LogMessage(TAG, "Message ID: %s", message.message_id.c_str());
    }

Messages can represent different kinds of incoming data. Most commonly,
messages are sent to the app after being initiated by the developer. Messages
are also sent to your app to represent message sent events, message send error
events, and messages deleted events. These special events can be
differentiated by checking the `Message::message_type` field.

#### Messages Deleted

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