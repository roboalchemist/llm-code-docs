# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification.md.txt

# FirebaseAdmin.Messaging.AndroidNotification Class Reference

# FirebaseAdmin.Messaging.AndroidNotification

Represents the Android-specific notification options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message).

## Summary

|                                                                                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                                                                                           ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Body](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ad117c67f61dffffacf8cc5f2c65ded9b)                  | `string` Gets or sets the title of the Android notification.                                                                                                                                                                                                                                                                                                  |
| [BodyLocArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a9fd6782e761824f616ad1c01e923a7be)           | `IEnumerable< string >` Gets or sets the collection of resource key strings that will be used in place of the format specifiers in [BodyLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ad122079a98c3dd362380b71c46ec5e1b).  |
| [BodyLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ad122079a98c3dd362380b71c46ec5e1b)            | `string` Gets or sets the key of the body string in the app's string resources to use to localize the body text.                                                                                                                                                                                                                                              |
| [ChannelId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a63af0cd93a1eacbcb9db3ef9af91bdf9)             | `string` Gets or sets the Android notification channel ID (new in Android O).                                                                                                                                                                                                                                                                                 |
| [ClickAction](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1addccf8b18bebb3759b01f692ec795c15)           | `string` Gets or sets the action associated with a user click on the notification.                                                                                                                                                                                                                                                                            |
| [Color](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a022a1091c288753f8330a12e43bde198)                 | `string` Gets or sets the notification icon color.                                                                                                                                                                                                                                                                                                            |
| [DefaultLightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a74a2eaa6fbcae4095bc9238e07edf6f3)  | `bool` Gets or sets a value indicating whether or not to use the default light settings.                                                                                                                                                                                                                                                                      |
| [DefaultSound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a066f2480fd4a781026b6aa10747081de)          | `bool` Gets or sets a value indicating whether or not to use the default sound.                                                                                                                                                                                                                                                                               |
| [DefaultVibrateTimings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aeb369cb611ddebbd5e2a35362c4fa6a1) | `bool` Gets or sets a value indicating whether or not to use the default vibration timings.                                                                                                                                                                                                                                                                   |
| [EventTimestamp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a2ec32630df1b86bc432ce11a32b3c0b1)        | `DateTime` Gets or sets the time that the event in the notification occurred for notifications that inform users about events with an absolute time reference.                                                                                                                                                                                                |
| [Icon](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a59892ba64df1db5b87ff94d44897c49e)                  | `string` Gets or sets the icon of the Android notification.                                                                                                                                                                                                                                                                                                   |
| [ImageUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ab79c2ebd0fb8e9e192f71f8975a049e2)              | `string` Gets or sets the URL of the image to be displayed in the notification.                                                                                                                                                                                                                                                                               |
| [LightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a35f39915be654715d9aca8094266876c)         | [LightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/light-settings#class_firebase_admin_1_1_messaging_1_1_light_settings) Gets or sets the settings to control the notification's LED blinking rate and color if LED is available on the device.                                                           |
| [LocalOnly](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a19beeb33e052500a355ffc51e8b5ed34)             | `bool` Gets or sets a value indicating whether or not this notification is relevant only to the current device.                                                                                                                                                                                                                                               |
| [NotificationCount](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a674b054c95afa4d416f008682125fddd)     | `int` Gets or sets the number of items this notification represents.                                                                                                                                                                                                                                                                                          |
| [Priority](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a1fc1ded03d9cbac13df504c695235234)              | [NotificationPriority](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1a324ca90a4b2d796e0b2cb4eb7f94e426) Gets or sets the relative priority for this notification.                                                                                                        |
| [Proxy](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a7c471bed860a34beb21dfabb459c5a70)                 | [NotificationProxy](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1abd239c55bdb884c80e1a15e7d7127bb3) Gets or sets the proxy behavior of this notification.                                                                                                               |
| [Sound](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ad147c6a5b7a93b6b777c092db4f85e62)                 | `string` Gets or sets the sound to be played when the device receives the notification.                                                                                                                                                                                                                                                                       |
| [Sticky](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a6a2d4854478ff4e5a43afd483f4c5897)                | `bool` Gets or sets a value indicating whether the notification is automatically dismissed or persists when the user clicks it in the panel.                                                                                                                                                                                                                  |
| [Tag](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1afc1b80d9e74f28bd58c6c12e7feee30d)                   | `string` Gets or sets the notification tag.                                                                                                                                                                                                                                                                                                                   |
| [Ticker](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a7030557da63423d23b2729a194ce6cb1)                | `string` Gets or sets the "ticker" text which is sent to accessibility services.                                                                                                                                                                                                                                                                              |
| [Title](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a70d020191c6520766c1c527744027e6b)                 | `string` Gets or sets the title of the Android notification.                                                                                                                                                                                                                                                                                                  |
| [TitleLocArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a1a3fcf1db46edc36b835978f6ed61270)          | `IEnumerable< string >` Gets or sets the collection of resource key strings that will be used in place of the format specifiers in [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a093d853073bcc07acb797e17280a4af8). |
| [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a093d853073bcc07acb797e17280a4af8)           | `string` Gets or sets the key of the title string in the app's string resources to use to localize the title text.                                                                                                                                                                                                                                            |
| [VibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aaf2c0e9f0e8e43735a2f83fefbe9c458)  | `long[]` Gets or sets a list of vibration timings in milliseconds in the array to use.                                                                                                                                                                                                                                                                        |
| [Visibility](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1af2616658a68d126b1650185effbe94fb)            | [NotificationVisibility](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging_1aa70ebfc59ec0ced84091801552c75447) Gets or sets the visibility of this notification.                                                                                                              |

## Properties

### Body

```text
string Body
```  
Gets or sets the title of the Android notification.

When provided, overrides the title set via [Notification.Body](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification#class_firebase_admin_1_1_messaging_1_1_notification_1ac2487f71a7b455553aed14f4276b1cd9).  

### BodyLocArgs

```text
IEnumerable< string > BodyLocArgs
```  
Gets or sets the collection of resource key strings that will be used in place of the format specifiers in [BodyLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1ad122079a98c3dd362380b71c46ec5e1b).  

### BodyLocKey

```text
string BodyLocKey
```  
Gets or sets the key of the body string in the app's string resources to use to localize the body text.  

### ChannelId

```text
string ChannelId
```  
Gets or sets the Android notification channel ID (new in Android O).

The app must create a channel with this channel ID before any notification with this channel ID is received. If you don't send this channel ID in the request, or if the channel ID provided has not yet been created by the app, FCM uses the channel ID specified in the app manifest.  

### ClickAction

```text
string ClickAction
```  
Gets or sets the action associated with a user click on the notification.

If specified, an activity with a matching Intent Filter is launched when a user clicks on the notification.  

### Color

```text
string Color
```  
Gets or sets the notification icon color.

Must be of the form `#RRGGBB`.  

### DefaultLightSettings

```text
bool DefaultLightSettings
```  
Gets or sets a value indicating whether or not to use the default light settings.

If set to true, use the Android framework's default LED light settings for the notification. Default values are specified in config.xml. If [DefaultLightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a74a2eaa6fbcae4095bc9238e07edf6f3) is set to true and [LightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/light-settings#class_firebase_admin_1_1_messaging_1_1_light_settings) is also set, the user-specified [LightSettings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/light-settings#class_firebase_admin_1_1_messaging_1_1_light_settings) is used instead of the default value.  

### DefaultSound

```text
bool DefaultSound
```  
Gets or sets a value indicating whether or not to use the default sound.

If set to true, use the Android framework's default sound for the notification. Default values are specified in config.xml.  

### DefaultVibrateTimings

```text
bool DefaultVibrateTimings
```  
Gets or sets a value indicating whether or not to use the default vibration timings.

If set to true, use the Android Sets the whether to use the default vibration timings. If set to true, use the Android in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If [DefaultVibrateTimings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aeb369cb611ddebbd5e2a35362c4fa6a1) is set to true and [VibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aaf2c0e9f0e8e43735a2f83fefbe9c458) is also set, the default value is used instead of the user-specified [VibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aaf2c0e9f0e8e43735a2f83fefbe9c458).  

### EventTimestamp

```text
DateTime EventTimestamp
```  
Gets or sets the time that the event in the notification occurred for notifications that inform users about events with an absolute time reference.

Notifications in the panel are sorted by this time.  

### Icon

```text
string Icon
```  
Gets or sets the icon of the Android notification.  

### ImageUrl

```text
string ImageUrl
```  
Gets or sets the URL of the image to be displayed in the notification.  

### LightSettings

```text
LightSettings LightSettings
```  
Gets or sets the settings to control the notification's LED blinking rate and color if LED is available on the device.

The total blinking time is controlled by the OS.  

### LocalOnly

```text
bool LocalOnly
```  
Gets or sets a value indicating whether or not this notification is relevant only to the current device.

Some notifications can be bridged to other devices for remote display, such as a Wear OS watch. This hint can be set to recommend this notification not be bridged. See [Wear OS guides](https://developer.android.com/training/wearables/notifications/bridger#existing-method-of-preventing-bridging).  

### NotificationCount

```text
int NotificationCount
```  
Gets or sets the number of items this notification represents.

May be displayed as a badge count for launchers that support badging. If not invoked then notification count is left unchanged. For example, this might be useful if you're using just one notification to represent multiple new messages but you want the count here to represent the number of total new messages.If zero or unspecified, systems that support badging use the default, which is to increment a number displayed on the long-press menu each time a new notification arrives.  

### Priority

```text
NotificationPriority Priority
```  
Gets or sets the relative priority for this notification.

Priority is an indication of how much of the user's attention should be consumed by this notification. Low-priority notifications may be hidden from the user in certain situations, while the user might be interrupted for a higher-priority notification.  

### Proxy

```text
NotificationProxy Proxy
```  
Gets or sets the proxy behavior of this notification.  

### Sound

```text
string Sound
```  
Gets or sets the sound to be played when the device receives the notification.  

### Sticky

```text
bool Sticky
```  
Gets or sets a value indicating whether the notification is automatically dismissed or persists when the user clicks it in the panel.

When set to false, the notification is automatically dismissed. When set to true, the notification persists.  

### Tag

```text
string Tag
```  
Gets or sets the notification tag.

This is an identifier used to replace existing notifications in the notification drawer. If not specified, each request creates a new notification.  

### Ticker

```text
string Ticker
```  
Gets or sets the "ticker" text which is sent to accessibility services.

Prior to API level 21 (Lollipop), gets or sets the text that is displayed in the status bar when the notification first arrives.  

### Title

```text
string Title
```  
Gets or sets the title of the Android notification.

When provided, overrides the title set via [Notification.Title](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification#class_firebase_admin_1_1_messaging_1_1_notification_1a47986b4044134363ad8daa6e7234871d).  

### TitleLocArgs

```text
IEnumerable< string > TitleLocArgs
```  
Gets or sets the collection of resource key strings that will be used in place of the format specifiers in [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1a093d853073bcc07acb797e17280a4af8).  

### TitleLocKey

```text
string TitleLocKey
```  
Gets or sets the key of the title string in the app's string resources to use to localize the title text.  

### VibrateTimingsMillis

```text
long[] VibrateTimingsMillis
```  
Gets or sets a list of vibration timings in milliseconds in the array to use.

The first value in the array indicates the duration to wait before turning the vibrator on. The next value indicates the duration to keep the vibrator on. Subsequent values alternate between duration to turn the vibrator off and to turn the vibrator on. If [VibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aaf2c0e9f0e8e43735a2f83fefbe9c458) is set and [DefaultVibrateTimings](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aeb369cb611ddebbd5e2a35362c4fa6a1) is set to true, the default value is used instead of the user-specified [VibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/android-notification#class_firebase_admin_1_1_messaging_1_1_android_notification_1aaf2c0e9f0e8e43735a2f83fefbe9c458). A duration in seconds with up to nine fractional digits, terminated by 's'.Example: "3.5s".  

### Visibility

```text
NotificationVisibility Visibility
```  
Gets or sets the visibility of this notification.