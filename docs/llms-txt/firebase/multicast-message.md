# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message.md.txt

# FirebaseAdmin.Messaging.MulticastMessage Class Reference

# FirebaseAdmin.Messaging.MulticastMessage

Represents a message that can be sent to multiple devices via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging) (FCM).

## Summary

Contains payload information as well as the list of device registration tokens to which the message should be sent. A single [MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message) may contain up to 500 registration tokens.

|                                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Android](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1a5c5ab088f7b6e77543a125bfed786775)      | [AndroidConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config) Gets or sets the Android-specific information to be included in the message. |
| [Apns](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1a6f18ccb7bd2de15c077e897eb22b3c95)         | [ApnsConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config) Gets or sets the APNs-specific information to be included in the message.             |
| [Data](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1a120b1e286d6d36be92010b08912601e0)         | `IReadOnlyDictionary< string, string >` Gets or sets a collection of key-value pairs that will be added to the message as data fields.                                                                                                                    |
| [Notification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1ae20b5b816db4827a289c949e4f1da641) | [Notification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification#class_firebase_admin_1_1_messaging_1_1_notification) Gets or sets the notification information to be included in the message.          |
| [Tokens](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1a5b53d9b698d653658023b58c82bb20b1)       | `IReadOnlyList< string >` Gets or sets the registration tokens for the devices to which the message should be distributed.                                                                                                                                |
| [Webpush](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message_1aec7e1ec9958d3c2a732dec56277be1aa)      | [WebpushConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config#class_firebase_admin_1_1_messaging_1_1_webpush_config) Gets or sets the Webpush-specific information to be included in the message. |

## Properties

### Android

```text
AndroidConfig Android
```  
Gets or sets the Android-specific information to be included in the message.  

### Apns

```text
ApnsConfig Apns
```  
Gets or sets the APNs-specific information to be included in the message.  

### Data

```text
IReadOnlyDictionary< string, string > Data
```  
Gets or sets a collection of key-value pairs that will be added to the message as data fields.

Keys and the values must not be null.  

### Notification

```text
Notification Notification
```  
Gets or sets the notification information to be included in the message.  

### Tokens

```text
IReadOnlyList< string > Tokens
```  
Gets or sets the registration tokens for the devices to which the message should be distributed.  

### Webpush

```text
WebpushConfig Webpush
```  
Gets or sets the Webpush-specific information to be included in the message.