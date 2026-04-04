# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/message-received-event-args.md.txt

# Firebase.Messaging.MessageReceivedEventArgs Class Reference

# Firebase.Messaging.MessageReceivedEventArgs

Event argument for the MessageReceived event containing the message data.

## Summary

### Inheritance

Inherits from: EventArgs

| ### Constructors and Destructors ||
|---|---|
| [MessageReceivedEventArgs](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/message-received-event-args#class_firebase_1_1_messaging_1_1_message_received_event_args_1aa925ba9a3331f87bd0ff5ef060f2b821)`(`[FirebaseMessage](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message)` msg)` ||

|                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Message](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/message-received-event-args#class_firebase_1_1_messaging_1_1_message_received_event_args_1aee91da2b83bff983ad662b3fff6c9f03) | [FirebaseMessage](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message) Message data passed to the MessageReceived event handler. |

## Properties

### Message

```c#
FirebaseMessage Message
```  
Message data passed to the MessageReceived event handler.

## Public functions

### MessageReceivedEventArgs

```c#
 MessageReceivedEventArgs(
  FirebaseMessage msg
)
```