# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message.md.txt

# Firebase.Messaging.FirebaseMessage Class Reference

# Firebase.Messaging.FirebaseMessage

Data structure used to send messages to, and receive messages from, cloud messaging.

## Summary

|                                                                                                                                                                                                    ### Properties                                                                                                                                                                                                    ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CollapseKey](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a1813fdabff5132597f19637bc8a287ce)        | `string` Gets the collapse key used for collapsible messages.                                                                                                                                                 |
| [Data](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a33c57d728bd270b0552040e27f5f15f5)               | `System.Collections.Generic.IDictionary< string, string >` Gets or sets the metadata, including all original key/value pairs.                                                                                 |
| [Error](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1aca9e7419f1bac15e83a48ecddefe5e9a)              | `string` Gets the error code.                                                                                                                                                                                 |
| [ErrorDescription](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a04e2ea03761de860cf9841c8ebef1754)   | `string` Gets the human readable details about the error.                                                                                                                                                     |
| [From](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a2c2d9c9b194eed3ed2e0738c7c0d6df8)               | `string` Gets the authenticated ID of the sender. This is a project number in most cases.                                                                                                                     |
| [Link](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1afbfd085d9b4e82bad2d53c19152ea479)               | `System.Uri` The link into the app from the message.                                                                                                                                                          |
| [MessageId](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a996cb34715974be19152a1e532d221b3)          | `string` Gets or sets the message ID.                                                                                                                                                                         |
| [MessageType](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1ab507d2fc6d94bae37158bd24ed1d5bf7)        | `string` Gets the message type, equivalent with a content-type.                                                                                                                                               |
| [Notification](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1aa10fa82f455d7186e3ed5b06872c4a3f)       | [FirebaseNotification](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification) Optional notification to show. |
| [NotificationOpened](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a0ed7d611a65bfbcafe254c0456bf6524) | `bool` Gets a flag indicating whether this message was opened by tapping a notification in the OS system tray.                                                                                                |
| [Priority](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1aa3324ea881382e7053cf315bcc25f6ae)           | `string` Gets the priority level.                                                                                                                                                                             |
| [RawData](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a8d84ca587ee5a89103f5e7180228733b)            | `byte[]` Gets the binary payload.                                                                                                                                                                             |
| [TimeToLive](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a9b5f82155558871f6293fc841765ac2e)         | `System.TimeSpan` The Time To Live (TTL) for the message.                                                                                                                                                     |
| [To](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-message#class_firebase_1_1_messaging_1_1_firebase_message_1a5e435662062e96c344d9ad302810c71c)                 | `string` Gets or sets recipient of a message.                                                                                                                                                                 |

## Properties

### CollapseKey

```c#
string CollapseKey
```  
Gets the collapse key used for collapsible messages.  

### Data

```c#
System.Collections.Generic.IDictionary< string, string > Data
```  
Gets or sets the metadata, including all original key/value pairs.

Includes some of the HTTP headers used when sending the message. `gcm`, `google` and `goog` prefixes are reserved for internal use.  

### Error

```c#
string Error
```  
Gets the error code.

Used in "nack" messages for CCS, and in responses from the server. See the CCS specification for the externally-supported list.  

### ErrorDescription

```c#
string ErrorDescription
```  
Gets the human readable details about the error.  

### From

```c#
string From
```  
Gets the authenticated ID of the sender. This is a project number in most cases.  

### Link

```c#
System.Uri Link
```  
The link into the app from the message.  

### MessageId

```c#
string MessageId
```  
Gets or sets the message ID.

This can be specified by sender. Internally a hash of the message ID and other elements will be used for storage. The ID must be unique for each topic subscription - using the same ID may result in overriding the original message or duplicate delivery.  

### MessageType

```c#
string MessageType
```  
Gets the message type, equivalent with a content-type.

CCS uses "ack", "nack" for flow control and error handling. "control" is used by CCS for connection control.  

### Notification

```c#
FirebaseNotification Notification
```  
Optional notification to show.

This only set if a notification was received with this message, otherwise it is null.  

### NotificationOpened

```c#
bool NotificationOpened
```  
Gets a flag indicating whether this message was opened by tapping a notification in the OS system tray.

If the message was received this way this flag is set to true.  

### Priority

```c#
string Priority
```  
Gets the priority level.

Defined values are "normal" and "high". By default messages are sent with normal priority.  

### RawData

```c#
byte[] RawData
```  
Gets the binary payload.

For webpush and non-json messages, this is the body of the request entity.  

### TimeToLive

```c#
System.TimeSpan TimeToLive
```  
The Time To Live (TTL) for the message.  

### To

```c#
string To
```  
Gets or sets recipient of a message.

For example it can be a registration token, a topic name, a IID or project ID.