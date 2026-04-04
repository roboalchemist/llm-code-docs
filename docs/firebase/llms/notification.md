# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification.md.txt

# firebase::messaging::Notification Struct Reference

# firebase::messaging::Notification


`#include <messaging.h>`

Used for messages that display a notification.

## Summary

On android, this requires that the app is using the Play Services client library.

| ### Constructors and Destructors ||
|---|---|
| [Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a9b9c73a75bd95ad5fccddf43a48193f5)`()` ||
| [Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a2e95e3161938ad9d49d02c9d4c17d752)`(const `[Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification)` & other)` Copy constructor. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message). ||
| [~Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1add7635184af20f76f1faee7a88e9a019)`()` Destructor. ||

|                                                                                                                                                                                                                ### Public attributes                                                                                                                                                                                                                 ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [android](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1afacd3abd26f39c23608faed9ea290953)        | [AndroidNotificationParams](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/android-notification-params#structfirebase_1_1messaging_1_1_android_notification_params)` *` Parameters that are unique to the Android implementation. |
| [badge](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a17e80042a025853792011237fa91dd7e)          | `std::string` Indicates the badge on the client app home icon. iOS and tvOS only.                                                                                                                                                                           |
| [body](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a556535bdb4c355eedacea95660f44947)           | `std::string` Indicates notification body text.                                                                                                                                                                                                             |
| [body_loc_args](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a8125da230f7cc9c5ca2b1e8168799ae3)  | `std::vector< std::string >` Indicates the string value to replace format specifiers in body string for localization.                                                                                                                                       |
| [body_loc_key](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1aa7c44942a0cf37089a4c911f61b79b30)   | `std::string` Indicates the key to the body string for localization.                                                                                                                                                                                        |
| [click_action](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a43f6afde3fa3a8d5ca9b7bffc45573bf)   | `std::string` The action associated with a user click on the notification.                                                                                                                                                                                  |
| [color](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a2fd13df5792abac17952a5c6de93df7b)          | `std::string` Indicates color of the icon, expressed in #rrggbb format. Android only.                                                                                                                                                                       |
| [icon](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a1eb21456354623b78f28d335431632d0)           | `std::string` Indicates notification icon.                                                                                                                                                                                                                  |
| [sound](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a67e9173a8ea609ca5e0176d76a984177)          | `std::string` Indicates a sound to play when the device receives the notification.                                                                                                                                                                          |
| [tag](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a05304d0658b4ad75cb2838b798b71748)            | `std::string` Indicates whether each notification results in a new entry in the notification drawer on Android.                                                                                                                                             |
| [title](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a835f4027e27a0083e5a351ce0e67ead5)          | `std::string` Indicates notification title.                                                                                                                                                                                                                 |
| [title_loc_args](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a0cf79549025d86c9f9763ceb0348aec7) | `std::vector< std::string >` Indicates the string value to replace format specifiers in title string for localization.                                                                                                                                      |
| [title_loc_key](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a443ea90dd2d00de9219f0157db3f56f8)  | `std::string` Indicates the key to the title string for localization.                                                                                                                                                                                       |

|                                                                                                                                                                                                                                                                                                                                           ### Public functions                                                                                                                                                                                                                                                                                                                                            ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator=](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification_1a00db80fad1e6922df867b164fd4de285)`(const `[Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification)` & other)` | [Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification#structfirebase_1_1messaging_1_1_notification)` &` Copy assignment operator. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message). |

## Public attributes

### android

```c++
AndroidNotificationParams * firebase::messaging::Notification::android
```  
Parameters that are unique to the Android implementation.  

### badge

```c++
std::string firebase::messaging::Notification::badge
```  
Indicates the badge on the client app home icon. iOS and tvOS only.  

### body

```c++
std::string firebase::messaging::Notification::body
```  
Indicates notification body text.  

### body_loc_args

```c++
std::vector< std::string > firebase::messaging::Notification::body_loc_args
```  
Indicates the string value to replace format specifiers in body string for localization.

On iOS and tvOS, this corresponds to "loc-args" in APNS payload.

On Android, these are the format arguments for the string resource. For more information, see [Formatting strings](https://developer.android.com/guide/topics/resources/string-resource.html#FormattingAndStyling).  

### body_loc_key

```c++
std::string firebase::messaging::Notification::body_loc_key
```  
Indicates the key to the body string for localization.

On iOS and tvOS, this corresponds to "loc-key" in APNS payload.

On Android, use the key in the app's string resources when populating this value.  

### click_action

```c++
std::string firebase::messaging::Notification::click_action
```  
The action associated with a user click on the notification.

On Android, if this is set, an activity with a matching intent filter is launched when user clicks the notification.

If set on iOS or tvOS, corresponds to category in APNS payload.  

### color

```c++
std::string firebase::messaging::Notification::color
```  
Indicates color of the icon, expressed in #rrggbb format. Android only.  

### icon

```c++
std::string firebase::messaging::Notification::icon
```  
Indicates notification icon.

Sets value to myicon for drawable resource myicon.  

### sound

```c++
std::string firebase::messaging::Notification::sound
```  
Indicates a sound to play when the device receives the notification.

Supports default, or the filename of a sound resource bundled in the app.

Android sound files must reside in /res/raw/, while iOS and tvOS sound files can be in the main bundle of the client app or in the Library/Sounds folder of the app's data container.  

### tag

```c++
std::string firebase::messaging::Notification::tag
```  
Indicates whether each notification results in a new entry in the notification drawer on Android.

If not set, each request creates a new notification. If set, and a notification with the same tag is already being shown, the new notification replaces the existing one in the notification drawer.  

### title

```c++
std::string firebase::messaging::Notification::title
```  
Indicates notification title.

This field is not visible on tvOS, iOS phones and tablets.  

### title_loc_args

```c++
std::vector< std::string > firebase::messaging::Notification::title_loc_args
```  
Indicates the string value to replace format specifiers in title string for localization.

On iOS and tvOS, this corresponds to "title-loc-args" in APNS payload.

On Android, these are the format arguments for the string resource. For more information, see [Formatting strings](https://developer.android.com/guide/topics/resources/string-resource.html#FormattingAndStyling).  

### title_loc_key

```c++
std::string firebase::messaging::Notification::title_loc_key
```  
Indicates the key to the title string for localization.

On iOS and tvOS, this corresponds to "title-loc-key" in APNS payload.

On Android, use the key in the app's string resources when populating this value.

## Public functions

### Notification

```c++
 firebase::messaging::Notification::Notification()
```  

### Notification

```c++
 firebase::messaging::Notification::Notification(
  const Notification & other
)
```  
Copy constructor. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message).  

### operator=

```c++
Notification & firebase::messaging::Notification::operator=(
  const Notification & other
)
```  
Copy assignment operator. Makes a deep copy of this [Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message).  

### \~Notification

```c++
 firebase::messaging::Notification::~Notification()
```  
Destructor.