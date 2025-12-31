# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config.md.txt

# FirebaseAdmin.Messaging.ApnsConfig Class Reference

# FirebaseAdmin.Messaging.ApnsConfig

Represents the APNS-specific options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

Refer to [APNs documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) for various headers and payload fields supported by APNS.

|                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                        ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Aps](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config_1a390632ca8806867363ffabaeb5cdbcfe)               | [Aps](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps#class_firebase_admin_1_1_messaging_1_1_aps) Gets or sets the `aps` dictionary to be included in the APNs payload.                            |
| [CustomData](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config_1aec57fafcb439cd673aedbfa88d77dbd1)        | `IDictionary< string, object >` Gets or sets a collection of arbitrary key-value data that will be included in the APNs payload.                                                                                                              |
| [FcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config_1aec11ccf19057724e851c6e8e98aa1114)        | [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-fcm-options#class_firebase_admin_1_1_messaging_1_1_apns_fcm_options) Gets or sets the FCM options to be included in the message. |
| [Headers](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config_1a7a9858f0b30ef7c437205ca01d6e62f6)           | `IReadOnlyDictionary< string, string >` Gets or sets the APNs headers.                                                                                                                                                                        |
| [LiveActivityToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/apns-config#class_firebase_admin_1_1_messaging_1_1_apns_config_1a73a5c8096de53e5830be10adf9112f14) | `string` Gets or sets the APNs token used for live activities on iOS.                                                                                                                                                                         |

## Properties

### Aps

```text
Aps Aps
```  
Gets or sets the `aps` dictionary to be included in the APNs payload.  

### CustomData

```text
IDictionary< string, object > CustomData
```  
Gets or sets a collection of arbitrary key-value data that will be included in the APNs payload.  

### FcmOptions

```text
ApnsFcmOptions FcmOptions
```  
Gets or sets the FCM options to be included in the message.  

### Headers

```text
IReadOnlyDictionary< string, string > Headers
```  
Gets or sets the APNs headers.  

### LiveActivityToken

```text
string LiveActivityToken
```  
Gets or sets the APNs token used for live activities on iOS.

Refer to [Firebase live activity documentation](https://firebase.google.com/docs/cloud-messaging/ios/live-activity) for more information.