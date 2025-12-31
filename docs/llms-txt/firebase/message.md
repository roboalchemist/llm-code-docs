# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message.md.txt

# firebase::messaging::Message Struct Reference

# firebase::messaging::Message


`#include <messaging.h>`

Data structure used to receive messages from cloud messaging.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a14fb59167b60b3eff52f1e656e06fc8d)`()` Initialize the message. ||
| [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a9833168dfd13435832a6ff096d48170a)`(const `[Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)` & other)` Copy constructor. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message). ||
| [~Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1aa16266e60e2583b47a4ba8a276d051a2)`()` Destructor. ||

|                                                                                                                                                                                    ### Public attributes                                                                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [collapse_key](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a1ad89997ef39d1ec5c4fde0b055b9f72)        | `std::string` This parameter identifies a group of messages (e.g., with collapse_key: "Updates Available") that can be collapsed, so that only the last message gets sent when delivery can be resumed. |
| [data](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1ab07ea6b606eb0c507beea7841cc33400)                | `std::map< std::string, std::string >` The metadata, including all original key/value pairs.                                                                                                            |
| [error](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a77813a88e383a2095991b919994c9e5e)               | `std::string` Error code.                                                                                                                                                                               |
| [error_description](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a35ee65569a8315b1833e4d0657663031)   | `std::string` Human readable details about the error.                                                                                                                                                   |
| [from](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1afdb0f76d509b241f8e75c6438908bb35)                | `std::string` Authenticated ID of the sender.                                                                                                                                                           |
| [link](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a1ee3b958683c8fc861a7c0162e310ddb)                | `std::string` The link into the app from the message.                                                                                                                                                   |
| [message_id](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1ae4326ab26e85dbf2590e4f5efa1f8c9c)          | `std::string` [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message) ID.                                                   |
| [message_type](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1aa384b95b8a9a8f33e4e37d76f268361c)        | `std::string` Equivalent with a content-type.                                                                                                                                                           |
| [notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1afc3866c370d13c23741d441302b10c27)        | [Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification)` *` Optional notification to show.                   |
| [notification_opened](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a7fb524a737b0299bc280fc712c928b82) | `bool` A flag indicating whether this message was opened by tapping a notification in the OS system tray.                                                                                               |
| [priority](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a830def80777c766936de1281224d6b23)            | `std::string` Sets the priority of the message.                                                                                                                                                         |
| [raw_data](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1ad7867e7bc94e148c31a52b08cf5456f7)            | `std::vector< unsigned char >` Binary payload.                                                                                                                                                          |
| [time_to_live](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1aaef43beaa2a7293a3d72e7fdc3eb8c5b)        | `int32_t` This parameter specifies how long (in seconds) the message should be kept in FCM storage if the device is offline.                                                                            |
| [to](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1acb76d0cfae7959fed1f703075d43c611)                  | `std::string` This parameter specifies the recipient of a message.                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                                                                        ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator=](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message_1a2acc3c3ce54a520a78607c838c286717)`(const `[Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)` & other)` | [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message)` &` Copy assignment operator. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message). |

## Public attributes

### collapse_key

```c++
std::string firebase::messaging::Message::collapse_key
```  
This parameter identifies a group of messages (e.g., with collapse_key: "Updates Available") that can be collapsed, so that only the last message gets sent when delivery can be resumed.

This is intended to avoid sending too many of the same messages when the device comes back online or becomes active.

Note that there is no guarantee of the order in which messages get sent.

Note: A maximum of 4 different collapse keys is allowed at any given time. This means a FCM connection server can simultaneously store 4 different send-to-sync messages per client app. If you exceed this number, there is no guarantee which 4 collapse keys the FCM connection server will keep.  

### data

```c++
std::map< std::string, std::string > firebase::messaging::Message::data
```  
The metadata, including all original key/value pairs.

Includes some of the HTTP headers used when sending the message. `gcm`, `google` and `goog` prefixes are reserved for internal use.  

### error

```c++
std::string firebase::messaging::Message::error
```  
Error code.

Used in "nack" messages for CCS, and in responses from the server. See the CCS specification for the externally-supported list.  

### error_description

```c++
std::string firebase::messaging::Message::error_description
```  
Human readable details about the error.  

### from

```c++
std::string firebase::messaging::Message::from
```  
Authenticated ID of the sender.

This is a project number in most cases.

Any value starting with google.com, goog. or gcm. are reserved.  

### link

```c++
std::string firebase::messaging::Message::link
```  
The link into the app from the message.  

### message_id

```c++
std::string firebase::messaging::Message::message_id
```  
[Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message) ID.

This can be specified by sender. Internally a hash of the message ID and other elements will be used for storage. The ID must be unique for each topic subscription - using the same ID may result in overriding the original message or duplicate delivery.  

### message_type

```c++
std::string firebase::messaging::Message::message_type
```  
Equivalent with a content-type.

Defined values:

- "deleted_messages" - indicates the server had too many messages and dropped some, and the client should sync with his own server. Current limit is 100 messages stored.
- "send_event" - indicates an upstream message has been pushed to the FCM server. It does not guarantee the upstream destination received it. Parameters: "message_id"
- "send_error" - indicates an upstream message expired, without being sent to the FCM server. Parameters: "message_id" and "error"

<br />

If this field is missing, the message is a regular message.  

### notification

```c++
Notification * firebase::messaging::Message::notification
```  
Optional notification to show.

This only set if a notification was received with this message, otherwise it is null.

The notification is only guaranteed to be valid during the call to [Listener::OnMessage()](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener_1a074808bae034dd30ba1e7756ca196281). If you need to keep it around longer you will need to make a copy of either the [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message) or [Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification). Copying the [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message) object implicitly makes a deep copy of the notification (allocated with new) which is owned by the [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message).  

### notification_opened

```c++
bool firebase::messaging::Message::notification_opened
```  
A flag indicating whether this message was opened by tapping a notification in the OS system tray.

If the message was received this way this flag is set to true.  

### priority

```c++
std::string firebase::messaging::Message::priority
```  
Sets the priority of the message.

Valid values are "normal" and "high." On iOS and tvOS, these correspond to APNs priority 5 and 10.

By default, messages are sent with normal priority. Normal priority optimizes the client app's battery consumption, and should be used unless immediate delivery is required. For messages with normal priority, the app may receive the message with unspecified delay.

When a message is sent with high priority, it is sent immediately, and the app can wake a sleeping device and open a network connection to your server.

For more information, see [Setting the priority of a message](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message).  

### raw_data

```c++
std::vector< unsigned char > firebase::messaging::Message::raw_data
```  
Binary payload.  

### time_to_live

```c++
int32_t firebase::messaging::Message::time_to_live
```  
This parameter specifies how long (in seconds) the message should be kept in FCM storage if the device is offline.

The maximum time to live supported is 4 weeks, and the default value is 4 weeks. For more information, see [Setting the lifespan of a message](https://firebase.google.com/docs/cloud-messaging/concept-options#ttl).  

### to

```c++
std::string firebase::messaging::Message::to
```  
This parameter specifies the recipient of a message.

For example it can be a registration token, a topic name, an Instance ID or project ID.

[PROJECT_ID@gcm.googleapis.com](mailto:PROJECT_ID@gcm.googleapis.com) or Instance ID are accepted.

## Public functions

### Message

```c++
 firebase::messaging::Message::Message()
```  
Initialize the message.  

### Message

```c++
 firebase::messaging::Message::Message(
  const Message & other
)
```  
Copy constructor. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message).  

### operator=

```c++
Message & firebase::messaging::Message::operator=(
  const Message & other
)
```  
Copy assignment operator. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message).  

### \~Message

```c++
 firebase::messaging::Message::~Message()
```  
Destructor.