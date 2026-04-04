# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert.md.txt

# FirebaseAdmin.Messaging.ApsAlert Class Reference

# FirebaseAdmin.Messaging.ApsAlert

Represents the [alert property](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html#//apple_ref/doc/uid/TP40008194-CH17-SW5) that can be included in the `aps` dictionary of an APNs payload.

## Summary

|                                                                                                                                                                                                                                                            ### Properties                                                                                                                                                                                                                                                             ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a01287c4e434db3dfae5c7192fae67fe9)    | `string` Gets or sets the key of the text in the app's string resources to use to localize the action button text.                                                                                                                                                                                                           |
| [Body](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a84a0a79a1ca7d93c29f5b1c5330c6856)            | `string` Gets or sets the body of the alert.                                                                                                                                                                                                                                                                                 |
| [LaunchImage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a56251f2f5cc2d94e6396ae8cdd939068)     | `string` Gets or sets the launch image for the notification action.                                                                                                                                                                                                                                                          |
| [LocArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1ae9a258605a9efebe46fa019e2055074e)         | `IEnumerable< string >` Gets or sets the resource key strings that will be used in place of the format specifiers in [LocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a35cde56173dc2ee3386348bd1dc549cd).         |
| [LocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a35cde56173dc2ee3386348bd1dc549cd)          | `string` Gets or sets the key of the body string in the app's string resources to use to localize the body text.                                                                                                                                                                                                             |
| [Subtitle](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1ad3ed241c89718e707b022ebaad3766cc)        | `string` Gets or sets the subtitle of the alert.                                                                                                                                                                                                                                                                             |
| [SubtitleLocArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1adc20bc1d10c7cff72ea5c03a811d1bd2) | `IEnumerable< string >` Gets or sets the resource key strings that will be used in place of the format specifiers in [SubtitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1aab7773c01aad4789cc3dff4823d87bdd). |
| [SubtitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1aab7773c01aad4789cc3dff4823d87bdd)  | `string` Gets or sets the key of the subtitle string in the app's string resources to use to localize the subtitle text.                                                                                                                                                                                                     |
| [Title](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1abe833758da6cae369b76249822744ccf)           | `string` Gets or sets the title of the alert.                                                                                                                                                                                                                                                                                |
| [TitleLocArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a03d8d2e33a383882857092e834bb72fe)    | `IEnumerable< string >` Gets or sets the resource key strings that will be used in place of the format specifiers in [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a3ec931edeab19cbba9eef0f1eed7e8ba).    |
| [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a3ec931edeab19cbba9eef0f1eed7e8ba)     | `string` Gets or sets the key of the title string in the app's string resources to use to localize the title text.                                                                                                                                                                                                           |

## Properties

### ActionLocKey

```text
string ActionLocKey
```  
Gets or sets the key of the text in the app's string resources to use to localize the action button text.  

### Body

```text
string Body
```  
Gets or sets the body of the alert.

When provided, overrides the body set via [Notification.Body](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification#class_firebase_admin_1_1_messaging_1_1_notification_1ac2487f71a7b455553aed14f4276b1cd9).  

### LaunchImage

```text
string LaunchImage
```  
Gets or sets the launch image for the notification action.  

### LocArgs

```text
IEnumerable< string > LocArgs
```  
Gets or sets the resource key strings that will be used in place of the format specifiers in [LocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a35cde56173dc2ee3386348bd1dc549cd).  

### LocKey

```text
string LocKey
```  
Gets or sets the key of the body string in the app's string resources to use to localize the body text.  

### Subtitle

```text
string Subtitle
```  
Gets or sets the subtitle of the alert.  

### SubtitleLocArgs

```text
IEnumerable< string > SubtitleLocArgs
```  
Gets or sets the resource key strings that will be used in place of the format specifiers in [SubtitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1aab7773c01aad4789cc3dff4823d87bdd).  

### SubtitleLocKey

```text
string SubtitleLocKey
```  
Gets or sets the key of the subtitle string in the app's string resources to use to localize the subtitle text.  

### Title

```text
string Title
```  
Gets or sets the title of the alert.

When provided, overrides the title set via [Notification.Title](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/notification#class_firebase_admin_1_1_messaging_1_1_notification_1a47986b4044134363ad8daa6e7234871d).  

### TitleLocArgs

```text
IEnumerable< string > TitleLocArgs
```  
Gets or sets the resource key strings that will be used in place of the format specifiers in [TitleLocKey](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/aps-alert#class_firebase_admin_1_1_messaging_1_1_aps_alert_1a3ec931edeab19cbba9eef0f1eed7e8ba).  

### TitleLocKey

```text
string TitleLocKey
```  
Gets or sets the key of the title string in the app's string resources to use to localize the title text.