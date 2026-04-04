# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps.md.txt

# FirebaseAdmin.Messaging.Aps Class Reference

# FirebaseAdmin.Messaging.Aps

Represents the [aps dictionary](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html) that is part of every APNs message.

## Summary

|                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Alert](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a38f3f8bb7aba2acd0e6a851291ffed35)            | [ApsAlert](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert) Gets or sets an advanced alert configuration to be included in the message.         |
| [AlertString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf34aec27e8b3d26a6a5e35c48392f60)      | `string` Gets or sets the alert text to be included in the message.                                                                                                                                                                               |
| [Badge](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a17b5dd427b793f6ccd6d49e9ea57f84a)            | `int` Gets or sets the badge to be displayed with the message.                                                                                                                                                                                    |
| [Category](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a255d0babff997239a4c6db38096b8e62)         | `string` Gets or sets the type of the notification.                                                                                                                                                                                               |
| [ContentAvailable](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1ad8bfba3091e2ca4b2cf9e69a31c31bf8) | `bool` Gets or sets a value indicating whether to configure a background update notification.                                                                                                                                                     |
| [CriticalSound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1aa14e87b958864c964df08e3185f71a79)    | [CriticalSound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound) Gets or sets the critical alert sound to be played with the message. |
| [CustomData](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a59098a4d657d5fc5d596bcb9e2c2a774)       | `IDictionary< string, object >` Gets or sets a collection of arbitrary key-value data to be included in the `aps` dictionary.                                                                                                                     |
| [MutableContent](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a825e6a6648761ce814e9e8fa72895ae7)   | `bool` Gets or sets a value indicating whether to include the `mutable-content` property in the message.                                                                                                                                          |
| [Sound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf62013b8f49cbe6494e1c1a162d427d)            | `string` Gets or sets the name of a sound file in your app's main bundle or in the `Library/Sounds` folder of your app's container directory.                                                                                                     |
| [ThreadId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a058f750de0d7b47a1fc243e1211c67f5)         | `string` Gets or sets the app-specific identifier for grouping notifications.                                                                                                                                                                     |

## Properties

### Alert

```text
ApsAlert Alert
```  
Gets or sets an advanced alert configuration to be included in the message.

It is an error to set both [Alert](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a38f3f8bb7aba2acd0e6a851291ffed35) and [AlertString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf34aec27e8b3d26a6a5e35c48392f60) properties together.  

### AlertString

```text
string AlertString
```  
Gets or sets the alert text to be included in the message.

To specify a more advanced alert configuration, use the [Alert](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a38f3f8bb7aba2acd0e6a851291ffed35) property instead. It is an error to set both [Alert](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1a38f3f8bb7aba2acd0e6a851291ffed35) and [AlertString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf34aec27e8b3d26a6a5e35c48392f60) properties together.  

### Badge

```text
int Badge
```  
Gets or sets the badge to be displayed with the message.

Set to 0 to remove the badge. When not specified, the badge will remain unchanged.  

### Category

```text
string Category
```  
Gets or sets the type of the notification.  

### ContentAvailable

```text
bool ContentAvailable
```  
Gets or sets a value indicating whether to configure a background update notification.  

### CriticalSound

```text
CriticalSound CriticalSound
```  
Gets or sets the critical alert sound to be played with the message.

It is an error to set both [Sound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf62013b8f49cbe6494e1c1a162d427d) and [CriticalSound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound) properties together.  

### CustomData

```text
IDictionary< string, object > CustomData
```  
Gets or sets a collection of arbitrary key-value data to be included in the `aps` dictionary.

This is exposed as an IDictionary{TKey, TValue} to support correct deserialization of custom properties.  

### MutableContent

```text
bool MutableContent
```  
Gets or sets a value indicating whether to include the `mutable-content` property in the message.

When set, this property allows clients to modify the notification via app extensions.  

### Sound

```text
string Sound
```  
Gets or sets the name of a sound file in your app's main bundle or in the `Library/Sounds` folder of your app's container directory.

Specify the string `default` to play the system sound. It is an error to set both [Sound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps_1abf62013b8f49cbe6494e1c1a162d427d) and [CriticalSound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound) properties together.  

### ThreadId

```text
string ThreadId
```  
Gets or sets the app-specific identifier for grouping notifications.