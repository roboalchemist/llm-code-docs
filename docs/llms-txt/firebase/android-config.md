# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config.md.txt

# FirebaseAdmin.Messaging.AndroidConfig Class Reference

# FirebaseAdmin.Messaging.AndroidConfig

Represents the Android-specific options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

|                                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                                        ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CollapseKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ad3d4dfb8c23427aa6ec78515850c6651)           | `string` Gets or sets a collapse key for the message.                                                                                                                                                                                                               |
| [Data](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a2eedffaa3abe8dea8e752c3425a8f00d)                  | `IReadOnlyDictionary< string, string >` Gets or sets a collection of key-value pairs that will be added to the message as data fields.                                                                                                                              |
| [DirectBootOk](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a698b15e713eeb8e043d9bfa6b2125e35)          | `bool` Gets or sets a boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode.                                                                                                                       |
| [FcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a280d952b828f879abadeed191003680f)            | [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-fcm-options#class_firebase_admin_1_1_messaging_1_1_android_fcm_options) Gets or sets the FCM options to be included in the message.              |
| [Notification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a05ea3f360589e026df4c25b8f07f3b5c)          | [AndroidNotification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification) Gets or sets the Android notification to be included in the message. |
| [Priority](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a9f97e394efd61eaf7cbf1dd15694abe5)              | [Priority](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1a347b410be469983db852f5b5e75fa767) Gets or sets the priority of the message.                                          |
| [RestrictedPackageName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ad38dd9f0bd8ca08e41b758dae9d9ee6b) | `string` Gets or sets the package name of the application where the registration tokens must match in order to receive the message.                                                                                                                                 |
| [TimeToLive](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ae3356b63026aa1ef81937dfdc65caea6)            | `TimeSpan` Gets or sets the time-to-live duration of the message.                                                                                                                                                                                                   |

## Properties

### CollapseKey

```text
string CollapseKey
```  
Gets or sets a collapse key for the message.

Collapse key serves as an identifier for a group of messages that can be collapsed, so that only the last message gets sent when delivery can be resumed. A maximum of 4 different collapse keys may be active at any given time.  

### Data

```text
IReadOnlyDictionary< string, string > Data
```  
Gets or sets a collection of key-value pairs that will be added to the message as data fields.

Keys and the values must not be null. When set, overrides any data fields set on the top-level [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).  

### DirectBootOk

```text
bool DirectBootOk
```  
Gets or sets a boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode.  

### FcmOptions

```text
AndroidFcmOptions FcmOptions
```  
Gets or sets the FCM options to be included in the message.  

### Notification

```text
AndroidNotification Notification
```  
Gets or sets the Android notification to be included in the message.  

### Priority

```text
Priority Priority
```  
Gets or sets the priority of the message.  

### RestrictedPackageName

```text
string RestrictedPackageName
```  
Gets or sets the package name of the application where the registration tokens must match in order to receive the message.  

### TimeToLive

```text
TimeSpan TimeToLive
```  
Gets or sets the time-to-live duration of the message.