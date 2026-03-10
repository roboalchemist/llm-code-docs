# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification.md.txt

# RemoteMessage.Notification

# RemoteMessage.Notification


```
class RemoteMessage.Notification
```

<br />

*** ** * ** ***

Remote Firebase notification details.

This class maps to the fields of a notification message.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationArgs()()` Gets the variable string values to be used as format specifiers in the body localization key, or null if not set. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey()()` Gets the string resource name to use to localize the body of the notification, or null if not set. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getDefaultVibrateSettings()()` Gets whether or not the notification uses the default vibrate pattern. |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getImageUrl()()` Gets the image URL from the notification. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationArgs()()` Gets the variable string values to be used as format specifiers in the title localization key, or null if not set. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey()()` Gets the string resource name to use to localize the title of the notification, or null if not set. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#body()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#channelId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#clickAction()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#color()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#defaultLightSettings()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#defaultSound()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#eventTime()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#icon()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#lightSettings()` |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#link()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#localOnly()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#notificationCount()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#notificationPriority()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#sound()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#sticky()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#tag()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#ticker()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#title()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#vibrateTimings()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#visibility()` |

## Public functions

### getBodyLocalizationArgs

```
fun getBodyLocalizationArgs(): Array<String!>?
```

Gets the variable string values to be used as format specifiers in the body localization key, or null if not set.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey()` |   |

### getBodyLocalizationKey

```
fun getBodyLocalizationKey(): String?
```

Gets the string resource name to use to localize the body of the notification, or null if not set.

### getDefaultVibrateSettings

```
fun getDefaultVibrateSettings(): Boolean
```

Gets whether or not the notification uses the default vibrate pattern.

See details about `defaultVibrateTimings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if it is set to `true`; Otherwise `false`. |

### getImageUrl

```
fun getImageUrl(): Uri?
```

Gets the image URL from the notification.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | The image URL if it was set, null otherwise. |

### getTitleLocalizationArgs

```
fun getTitleLocalizationArgs(): Array<String!>?
```

Gets the variable string values to be used as format specifiers in the title localization key, or null if not set.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey()` |   |

### getTitleLocalizationKey

```
fun getTitleLocalizationKey(): String?
```

Gets the string resource name to use to localize the title of the notification, or null if not set.

## Public properties

### body

```
val body: String!
```

### channelId

```
val channelId: String!
```

### clickAction

```
val clickAction: String!
```

### color

```
val color: String!
```

### defaultLightSettings

```
val defaultLightSettings: Boolean
```

### defaultSound

```
val defaultSound: Boolean
```

### eventTime

```
val eventTime: Long!
```

### icon

```
val icon: String!
```

### lightSettings

```
val lightSettings: IntArray<Int>!
```

### link

```
val link: Uri!
```

### localOnly

```
val localOnly: Boolean
```

### notificationCount

```
val notificationCount: Int!
```

### notificationPriority

```
val notificationPriority: Int!
```

### sound

```
val sound: String!
```

### sticky

```
val sticky: Boolean
```

### tag

```
val tag: String!
```

### ticker

```
val ticker: String!
```

### title

```
val title: String!
```

### vibrateTimings

```
val vibrateTimings: LongArray<Long>!
```

### visibility

```
val visibility: Int!
```