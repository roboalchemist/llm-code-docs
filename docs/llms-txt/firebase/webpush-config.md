# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config.md.txt

# FirebaseAdmin.Messaging.WebpushConfig Class Reference

# FirebaseAdmin.Messaging.WebpushConfig

Represents the Webpush protocol options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

|                                                                                                                                                                                                                                ### Properties                                                                                                                                                                                                                                 ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Data](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config#class_firebase_admin_1_1_messaging_1_1_webpush_config_1a594375d33c47bb998f21fd93fc5a7067)         | `IReadOnlyDictionary< string, string >` Gets or sets the Webpush data fields.                                                                                                                                                                                 |
| [FcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config#class_firebase_admin_1_1_messaging_1_1_webpush_config_1a9fcdc1d618c70f9c52660dce96d99bcb)   | [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-fcm-options#class_firebase_admin_1_1_messaging_1_1_webpush_fcm_options) Gets or sets the Webpush options included in the message.          |
| [Headers](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config#class_firebase_admin_1_1_messaging_1_1_webpush_config_1a7c35176dc1638bfc37c87d20d9c329aa)      | `IReadOnlyDictionary< string, string >` Gets or sets the Webpush HTTP headers.                                                                                                                                                                                |
| [Notification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-config#class_firebase_admin_1_1_messaging_1_1_webpush_config_1a50d992cf26edb488d664f6d029f365ce) | [WebpushNotification](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification) Gets or sets the Webpush notification included in the message. |

## Properties

### Data

```text
IReadOnlyDictionary< string, string > Data
```  
Gets or sets the Webpush data fields.

When set, overrides any data fields set via [Message.Data](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message_1a60de8969556aba3ad8bef3726ba474b4).  

### FcmOptions

```text
WebpushFcmOptions FcmOptions
```  
Gets or sets the Webpush options included in the message.  

### Headers

```text
IReadOnlyDictionary< string, string > Headers
```  
Gets or sets the Webpush HTTP headers.

Refer [Webpush specification](https://tools.ietf.org/html/rfc8030#section-5) for supported headers.  

### Notification

```text
WebpushNotification Notification
```  
Gets or sets the Webpush notification included in the message.