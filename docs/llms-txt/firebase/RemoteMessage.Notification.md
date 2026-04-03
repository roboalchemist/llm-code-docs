# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification.md.txt

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

|                                                                          ### Public functions                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>?` | [getBodyLocalizationArgs](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationArgs())`()` Gets the variable string values to be used as format specifiers in the body localization key, or null if not set.    |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                    | [getBodyLocalizationKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey())`()` Gets the string resource name to use to localize the body of the notification, or null if not set.                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                     | [getDefaultVibrateSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getDefaultVibrateSettings())`()` Gets whether or not the notification uses the default vibrate pattern.                                           |
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                                                                                          | [getImageUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getImageUrl())`()` Gets the image URL from the notification.                                                                                                    |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>?` | [getTitleLocalizationArgs](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationArgs())`()` Gets the variable string values to be used as format specifiers in the title localization key, or null if not set. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                    | [getTitleLocalizationKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey())`()` Gets the string resource name to use to localize the title of the notification, or null if not set.                  |

|                                                                           ### Public properties                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [body](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#body())                                 |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [channelId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#channelId())                       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [clickAction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#clickAction())                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [color](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#color())                               |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [defaultLightSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#defaultLightSettings()) |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [defaultSound](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#defaultSound())                 |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`!`                                                                                            | [eventTime](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#eventTime())                       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [icon](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#icon())                                 |
| [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)`<`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`>!`     | [lightSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#lightSettings())               |
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`!`                                                                                              | [link](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#link())                                 |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [localOnly](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#localOnly())                       |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`!`                                                                                              | [notificationCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#notificationCount())       |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`!`                                                                                              | [notificationPriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#notificationPriority()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [sound](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#sound())                               |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [sticky](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#sticky())                             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [tag](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#tag())                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [ticker](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#ticker())                             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [title](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#title())                               |
| [LongArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long-array/index.html)`<`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`>!` | [vibrateTimings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#vibrateTimings())             |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`!`                                                                                              | [visibility](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#visibility())                     |

## Public functions

### getBodyLocalizationArgs

```
funÂ getBodyLocalizationArgs():Â Array<String!>?
```

Gets the variable string values to be used as format specifiers in the body localization key, or null if not set.  

|                                                                           See also                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [getBodyLocalizationKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey()) |   |

### getBodyLocalizationKey

```
funÂ getBodyLocalizationKey():Â String?
```

Gets the string resource name to use to localize the body of the notification, or null if not set.  

### getDefaultVibrateSettings

```
funÂ getDefaultVibrateSettings():Â Boolean
```

Gets whether or not the notification uses the default vibrate pattern.

See details about `defaultVibrateTimings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `true` if it is set to `true`; Otherwise `false`. |

### getImageUrl

```
funÂ getImageUrl():Â Uri?
```

Gets the image URL from the notification.  

|                                    Returns                                    |
|-------------------------------------------------------------------------------|----------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?` | The image URL if it was set, null otherwise. |

### getTitleLocalizationArgs

```
funÂ getTitleLocalizationArgs():Â Array<String!>?
```

Gets the variable string values to be used as format specifiers in the title localization key, or null if not set.  

|                                                                            See also                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [getTitleLocalizationKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey()) |   |

### getTitleLocalizationKey

```
funÂ getTitleLocalizationKey():Â String?
```

Gets the string resource name to use to localize the title of the notification, or null if not set.  

## Public properties

### body

```
valÂ body:Â String!
```  

### channelId

```
valÂ channelId:Â String!
```  

### clickAction

```
valÂ clickAction:Â String!
```  

### color

```
valÂ color:Â String!
```  

### defaultLightSettings

```
valÂ defaultLightSettings:Â Boolean
```  

### defaultSound

```
valÂ defaultSound:Â Boolean
```  

### eventTime

```
valÂ eventTime:Â Long!
```  

### icon

```
valÂ icon:Â String!
```  

### lightSettings

```
valÂ lightSettings:Â IntArray<Int>!
```  

### link

```
valÂ link:Â Uri!
```  

### localOnly

```
valÂ localOnly:Â Boolean
```  

### notificationCount

```
valÂ notificationCount:Â Int!
```  

### notificationPriority

```
valÂ notificationPriority:Â Int!
```  

### sound

```
valÂ sound:Â String!
```  

### sticky

```
valÂ sticky:Â Boolean
```  

### tag

```
valÂ tag:Â String!
```  

### ticker

```
valÂ ticker:Â String!
```  

### title

```
valÂ title:Â String!
```  

### vibrateTimings

```
valÂ vibrateTimings:Â LongArray<Long>!
```  

### visibility

```
valÂ visibility:Â Int!
```