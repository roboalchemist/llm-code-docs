# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification.md.txt

# FirebaseAdmin.Messaging.WebpushNotification Class Reference

# FirebaseAdmin.Messaging.WebpushNotification

Represents the Webpush-specific notification options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

Supports most standard options defined in the [Web Notification specification](https://developer.mozilla.org/en-US/docs/Web/API/notification/Notification).

|                                                                                                                                                                                                                                    ### Properties                                                                                                                                                                                                                                    ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Actions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a348079b311cdc47c2987680b0adfbdcd)            | `IEnumerable< `[Action](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/action#class_firebase_admin_1_1_messaging_1_1_action)` >` Gets or sets a collection of Webpush notification actions.                |
| [Badge](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a682e99d8f8b90c90a286a96acd7d53a8)              | `string` Gets or sets the URL of the image used to represent the notification when there is not enough space to display the notification itself.                                                                                                   |
| [Body](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a5c0151723285e683ee58edbb6693469f)               | `string` Gets or sets the body text of the notification.                                                                                                                                                                                           |
| [CustomData](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a76c7844b488dd7925ee362f1b7a2813f)         | `IDictionary< string, object >` Gets or sets the custom key-value pairs that will be included in the notification.                                                                                                                                 |
| [Data](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a9b075ff57ba13a142157846845baa86e)               | `object` Gets or sets some arbitrary data that will be included in the notification.                                                                                                                                                               |
| [Direction](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a2de83f6c4296fb36a44db02aa0a215d4)          | [Direction](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1ae98b9a366d634a1a4bd33068005c79c7) Gets or sets the direction in which to display the notification. |
| [Icon](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a5be781d5ec5298fd28c0810aa60f32f3)               | `string` Gets or sets the URL to the icon of the notification.                                                                                                                                                                                     |
| [Image](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1ad088d0121adb1e2a3ca27c7932c34059)              | `string` Gets or sets the URL of an image to be displayed in the notification.                                                                                                                                                                     |
| [Language](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1afe91072cc3cdc78e330f07f5d2fc9803)           | `string` Gets or sets the language of the notification.                                                                                                                                                                                            |
| [Renotify](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a40bdd0162c8f5dc0a85b4fc08f1af5a7)           | `bool` Gets or sets whether the user should be notified after a new notification replaces an old one.                                                                                                                                              |
| [RequireInteraction](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a6bb6f48caed5dfaeff53dfe67a198593) | `bool` Gets or sets whether the notification should remain active until the user clicks or dismisses it, rather than closing it automatically.                                                                                                     |
| [Silent](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a5b8bb3fe1fd1d7f5e497a2dc587f9929)             | `bool` Gets or sets whether the notification should be silent.                                                                                                                                                                                     |
| [Tag](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a766f81870b4626ba29c8e718dc4b35d9)                | `string` Gets or sets an identifying tag for the notification.                                                                                                                                                                                     |
| [TimestampMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a05e8fc781b0088333d9ec71f338b94f8)    | `long` Gets or sets the notification's timestamp value in milliseconds.                                                                                                                                                                            |
| [Title](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1a04b2c381c37ea9826781b2920cbee1a2)              | `string` Gets or sets the title text of the notification.                                                                                                                                                                                          |
| [Vibrate](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/webpush-notification#class_firebase_admin_1_1_messaging_1_1_webpush_notification_1abde827e47bb54dd665c3cec9b616acf3)            | `int[]` Gets or sets a vibration pattern for the receiving device's vibration hardware.                                                                                                                                                            |

## Properties

### Actions

```text
IEnumerable< Action > Actions
```  
Gets or sets a collection of Webpush notification actions.  

### Badge

```text
string Badge
```  
Gets or sets the URL of the image used to represent the notification when there is not enough space to display the notification itself.  

### Body

```text
string Body
```  
Gets or sets the body text of the notification.  

### CustomData

```text
IDictionary< string, object > CustomData
```  
Gets or sets the custom key-value pairs that will be included in the notification.

This is exposed as an IDictionary{TKey, TValue} to support correct deserialization of custom properties.  

### Data

```text
object Data
```  
Gets or sets some arbitrary data that will be included in the notification.  

### Direction

```text
Direction Direction
```  
Gets or sets the direction in which to display the notification.  

### Icon

```text
string Icon
```  
Gets or sets the URL to the icon of the notification.  

### Image

```text
string Image
```  
Gets or sets the URL of an image to be displayed in the notification.  

### Language

```text
string Language
```  
Gets or sets the language of the notification.  

### Renotify

```text
bool Renotify
```  
Gets or sets whether the user should be notified after a new notification replaces an old one.  

### RequireInteraction

```text
bool RequireInteraction
```  
Gets or sets whether the notification should remain active until the user clicks or dismisses it, rather than closing it automatically.  

### Silent

```text
bool Silent
```  
Gets or sets whether the notification should be silent.  

### Tag

```text
string Tag
```  
Gets or sets an identifying tag for the notification.  

### TimestampMillis

```text
long TimestampMillis
```  
Gets or sets the notification's timestamp value in milliseconds.  

### Title

```text
string Title
```  
Gets or sets the title text of the notification.  

### Vibrate

```text
int[] Vibrate
```  
Gets or sets a vibration pattern for the receiving device's vibration hardware.