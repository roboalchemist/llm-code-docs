# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification.md.txt

# Firebase.Messaging.FirebaseNotification Class Reference

# Firebase.Messaging.FirebaseNotification

Used for messages that display a notification.

## Summary

On android, this requires that the app is using the Play Services client library.

|                                                                                                                                                                                                                   ### Properties                                                                                                                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Android](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a4f06b79abeff95eab2caa2733c4e5883)               | [AndroidNotificationParams](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/android-notification-params#class_firebase_1_1_messaging_1_1_android_notification_params) Android-specific data to show. |
| [Badge](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1aa57adba311ccd53221036a233bf9bbef)                 | `string` Indicates the badge on the client app home icon. iOS and tvOS only.                                                                                                                                                   |
| [Body](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a6de35365883803c7f64bd8e84efeddb6)                  | `string` Indicates notification body text.                                                                                                                                                                                     |
| [BodyLocalizationArgs](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1aa1952f88e1ca900fda4f1157fdd6260e)  | `System.Collections.Generic.IEnumerable< string >` Indicates the string value to replace format specifiers in body string for localization.                                                                                    |
| [BodyLocalizationKey](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a304ed66037b87305df18746ce7f20023)   | `string` Indicates the key to the body string for localization.                                                                                                                                                                |
| [ClickAction](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a8ac4fdc6fd70a17606181301db3c6ea0)           | `string` The action associated with a user click on the notification.                                                                                                                                                          |
| [Color](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a24240f747e6f457b27ab4a4d789c0504)                 | `string` Indicates color of the icon, expressed in #rrggbb format. Android only.                                                                                                                                               |
| [Icon](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a474ec0a5e71ecedebb23f7439b2c2f70)                  | `string` Indicates notification icon.                                                                                                                                                                                          |
| [Sound](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1ab1d8db02efc1eac3270ed3e7cde03a7c)                 | `string` Indicates a sound to play when the device receives the notification.                                                                                                                                                  |
| [Tag](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a358ea766a6160e93ed250206dbf1d937)                   | `string` Indicates whether each notification results in a new entry in the notification drawer on Android.                                                                                                                     |
| [Title](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a1197858304170aa9c3eb734fc5491386)                 | `string` Indicates notification title.                                                                                                                                                                                         |
| [TitleLocalizationArgs](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1a2a751f559df75001afc270f3f1199e3f) | `System.Collections.Generic.IEnumerable< string >` Indicates the string value to replace format specifiers in title string for localization.                                                                                   |
| [TitleLocalizationKey](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-notification#class_firebase_1_1_messaging_1_1_firebase_notification_1aaeb787fd9fbe978fea99f3048cd3d359)  | `string` Indicates the key to the title string for localization.                                                                                                                                                               |

## Properties

### Android

```c#
AndroidNotificationParams Android
```  
Android-specific data to show.  

### Badge

```c#
string Badge
```  
Indicates the badge on the client app home icon. iOS and tvOS only.  

### Body

```c#
string Body
```  
Indicates notification body text.  

### BodyLocalizationArgs

```c#
System.Collections.Generic.IEnumerable< string > BodyLocalizationArgs
```  
Indicates the string value to replace format specifiers in body string for localization.

On iOS and tvOS, this corresponds to "loc-args" in APNS payload.

On Android, these are the format arguments for the string resource. For more information, see [Formatting strings](https://developer.android.com/guide/topics/resources/string-resource.html#FormattingAndStyling).  

### BodyLocalizationKey

```c#
string BodyLocalizationKey
```  
Indicates the key to the body string for localization.

On iOS and tvOS, this corresponds to "loc-key" in APNS payload.

On Android, use the key in the app's string resources when populating this value.  

### ClickAction

```c#
string ClickAction
```  
The action associated with a user click on the notification.

On Android, if this is set, an activity with a matching intent filter is launched when user clicks the notification.

If set on iOS or tvOS, corresponds to category in APNS payload.  

### Color

```c#
string Color
```  
Indicates color of the icon, expressed in #rrggbb format. Android only.  

### Icon

```c#
string Icon
```  
Indicates notification icon.

Sets value to myicon for drawable resource myicon.  

### Sound

```c#
string Sound
```  
Indicates a sound to play when the device receives the notification.

Supports default, or the filename of a sound resource bundled in the app.

Android sound files must reside in /res/raw/, while tvOS and iOS sound files can be in the main bundle of the client app or in the Library/Sounds folder of the app's data container.  

### Tag

```c#
string Tag
```  
Indicates whether each notification results in a new entry in the notification drawer on Android.

If not set, each request creates a new notification. If set, and a notification with the same tag is already being shown, the new notification replaces the existing one in the notification drawer.  

### Title

```c#
string Title
```  
Indicates notification title.

This field is not visible on tvOS, iOS phones and tablets.  

### TitleLocalizationArgs

```c#
System.Collections.Generic.IEnumerable< string > TitleLocalizationArgs
```  
Indicates the string value to replace format specifiers in title string for localization.

On iOS and tvOS, this corresponds to "title-loc-args" in APNS payload.

On Android, these are the format arguments for the string resource. For more information, see [Formatting strings](https://developer.android.com/guide/topics/resources/string-resource.html#FormattingAndStyling).  

### TitleLocalizationKey

```c#
string TitleLocalizationKey
```  
Indicates the key to the title string for localization.

On iOS and tvOS, this corresponds to "title-loc-key" in APNS payload.

On Android, use the key in the app's string resources when populating this value.