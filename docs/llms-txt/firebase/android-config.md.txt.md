# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config.md.txt

# FirebaseAdmin.Messaging.AndroidConfig Class Reference

# FirebaseAdmin.Messaging.AndroidConfig

Represents the Android-specific options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ad3d4dfb8c23427aa6ec78515850c6651` | `string` Gets or sets a collapse key for the message. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a2eedffaa3abe8dea8e752c3425a8f00d` | `IReadOnlyDictionary< string, string >` Gets or sets a collection of key-value pairs that will be added to the message as data fields. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a698b15e713eeb8e043d9bfa6b2125e35` | `bool` Gets or sets a boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a280d952b828f879abadeed191003680f` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-fcm-options#class_firebase_admin_1_1_messaging_1_1_android_fcm_options` Gets or sets the FCM options to be included in the message. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a05ea3f360589e026df4c25b8f07f3b5c` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification` Gets or sets the Android notification to be included in the message. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1a9f97e394efd61eaf7cbf1dd15694abe5` | `https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1a347b410be469983db852f5b5e75fa767` Gets or sets the priority of the message. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ad38dd9f0bd8ca08e41b758dae9d9ee6b` | `string` Gets or sets the package name of the application where the registration tokens must match in order to receive the message. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-config#class_firebase_admin_1_1_messaging_1_1_android_config_1ae3356b63026aa1ef81937dfdc65caea6` | `TimeSpan` Gets or sets the time-to-live duration of the message. |

## Properties

### CollapseKey

```
string CollapseKey
```
Gets or sets a collapse key for the message.

Collapse key serves as an identifier for a group of messages that can be collapsed, so that only the last message gets sent when delivery can be resumed. A maximum of 4 different collapse keys may be active at any given time.

### Data

```
IReadOnlyDictionary< string, string > Data
```
Gets or sets a collection of key-value pairs that will be added to the message as data fields.

Keys and the values must not be null. When set, overrides any data fields set on the top-level [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

### DirectBootOk

```
bool DirectBootOk
```
Gets or sets a boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode.

### FcmOptions

```
AndroidFcmOptions FcmOptions
```
Gets or sets the FCM options to be included in the message.

### Notification

```
AndroidNotification Notification
```
Gets or sets the Android notification to be included in the message.

### Priority

```
Priority Priority
```
Gets or sets the priority of the message.

### RestrictedPackageName

```
string RestrictedPackageName
```
Gets or sets the package name of the application where the registration tokens must match in order to receive the message.

### TimeToLive

```
TimeSpan TimeToLive
```
Gets or sets the time-to-live duration of the message.