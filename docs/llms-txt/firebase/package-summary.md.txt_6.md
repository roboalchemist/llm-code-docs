# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/package-summary.md.txt

# com.google.firebase.messaging

### Interfaces

|---|---|
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | Response from an operation that sends FCM messages to multiple recipients. |

### Classes

|---|---|
| [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) | Represents the Android-specific options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) |   |
| [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) | Represents the Android-specific FCM options that can be included in an `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig`. |
| [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder) |   |
| [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) | Represents the Android-specific notification options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) |   |
| [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) | Represents the APNS-specific options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) |   |
| [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) | Represents the APNS-specific FCM options that can be included in an `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig`. |
| [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) |   |
| [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps) | Represents the [aps dictionary](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html) that is part of every APNS message. |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) |   |
| [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) | Represents the [alert property](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html#//apple_ref/doc/uid/TP40008194-CH17-SW5) that can be included in the aps dictionary of an APNS payload. |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) |   |
| [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) | The sound configuration for APNs critical alerts. |
| [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder) |   |
| [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) | Represents the platform-independent FCM options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder) |   |
| [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging) | This class is the entry point for all server-side Firebase Cloud Messaging actions. |
| [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings) | A class representing light settings in an Android Notification. |
| [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder) |   |
| [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) | A class representing color in LightSettings. |
| [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) | Represents a message that can be sent via Firebase Cloud Messaging (FCM). |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) |   |
| [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) | Represents a message that can be sent to multiple devices via Firebase Cloud Messaging (FCM). |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) |   |
| [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) | Represents the notification parameters that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) |   |
| [SendResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse) | The result of an individual send operation that was executed as part of a batch. |
| [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse) | The response produced by FCM topic management operations. |
| [TopicManagementResponse.Error](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error) | A topic management error. |
| [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) | Represents the Webpush protocol options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) |   |
| [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) | Represents options for features provided by the FCM SDK for Web. |
| [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder) |   |
| [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) | Represents the Webpush-specific notification options that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message`. |
| [WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action) | Represents an action available to users when the notification is presented. |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) |   |

### Enums

|---|---|
| [AndroidConfig.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Priority) | Priority levels that can be set on an `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig`. |
| [AndroidNotification.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Priority) |   |
| [AndroidNotification.Proxy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Proxy) |   |
| [AndroidNotification.Visibility](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Visibility) |   |
| [MessagingErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MessagingErrorCode) | Error codes that can be raised by the Cloud Messaging APIs. |
| [WebpushNotification.Direction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Direction) | Different directions a notification can be displayed in. |

### Exceptions

|---|---|
| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) |   |