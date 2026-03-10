# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification.md.txt

# RemoteMessage.Notification

# RemoteMessage.Notification


```
public class RemoteMessage.Notification
```

<br />

*** ** * ** ***

Remote Firebase notification details.

This class maps to the fields of a notification message.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#body()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#channelId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#clickAction()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#color()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#defaultLightSettings()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#defaultSound()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Long.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#eventTime()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#icon()` |
| `final int[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#lightSettings()` |
| `final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#link()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#localOnly()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#notificationCount()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#notificationPriority()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#sound()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#sticky()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#tag()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#ticker()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#title()` |
| `final long[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#vibrateTimings()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#visibility()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getBody()()` Gets the body of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationArgs()()` Gets the variable string values to be used as format specifiers in the body localization key, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey()()` Gets the string resource name to use to localize the body of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getChannelId()()` Gets the channel id from the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getClickAction()()` Gets the action to be performed on the user opening the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getColor()()` Gets the color of the notification, or null if not set. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getDefaultLightSettings()()` Gets whether or not the notification uses the default notification light settings. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getDefaultSound()()` Gets whether or not the notification uses the default sound. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getDefaultVibrateSettings()()` Gets whether or not the notification uses the default vibrate pattern. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getEventTime()()` Gets the `eventTime` from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getIcon()()` Gets the image resource name of the icon of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getImageUrl()()` Gets the image URL from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html int[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getLightSettings()()` Gets the `lightSettings` from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getLink()()` Gets the deep link from the notification, or null if not set. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getLocalOnly()()` Gets whether or not this notification is only relevant to the current device. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getNotificationCount()()` Gets the `notificationCount` from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getNotificationPriority()()` Gets the `notificationPriority` from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getSound()()` Gets the sound to be played when the notification is shown, or null if not set. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getSticky()()` Gets whether or not the notification is considered sticky. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTag()()` Gets the tag of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTicker()()` Gets the ticker text from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTitle()()` Gets the title of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationArgs()()` Gets the variable string values to be used as format specifiers in the title localization key, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey()()` Gets the string resource name to use to localize the title of the notification, or null if not set. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html long[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getVibrateTimings()()` Gets the `vibrateTimings` from the notification. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getVisibility()()` Gets the `visibility` from the notification. |

## Public fields

### body

```
public final String body
```

### channelId

```
public final String channelId
```

### clickAction

```
public final String clickAction
```

### color

```
public final String color
```

### defaultLightSettings

```
public final boolean defaultLightSettings
```

### defaultSound

```
public final boolean defaultSound
```

### eventTime

```
public final Long eventTime
```

### icon

```
public final String icon
```

### lightSettings

```
public final int[] lightSettings
```

### link

```
public final Uri link
```

### localOnly

```
public final boolean localOnly
```

### notificationCount

```
public final Integer notificationCount
```

### notificationPriority

```
public final Integer notificationPriority
```

### sound

```
public final String sound
```

### sticky

```
public final boolean sticky
```

### tag

```
public final String tag
```

### ticker

```
public final String ticker
```

### title

```
public final String title
```

### vibrateTimings

```
public final long[] vibrateTimings
```

### visibility

```
public final Integer visibility
```

## Public methods

### getBody

```
public @Nullable String getBody()
```

Gets the body of the notification, or null if not set.

### getBodyLocalizationArgs

```
public @Nullable String[] getBodyLocalizationArgs()
```

Gets the variable string values to be used as format specifiers in the body localization key, or null if not set.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getBodyLocalizationKey()` |   |

### getBodyLocalizationKey

```
public @Nullable String getBodyLocalizationKey()
```

Gets the string resource name to use to localize the body of the notification, or null if not set.

### getChannelId

```
public @Nullable String getChannelId()
```

Gets the channel id from the notification, or null if not set.

Note that this method does not perform verification on the existence of a channel, nor does it fallback to the manifest defined default or the default Firebase Cloud Messaging channel.

### getClickAction

```
public @Nullable String getClickAction()
```

Gets the action to be performed on the user opening the notification, or null if not set.

The action is to open an [Activity](https://developer.android.com/reference/android/app/Activity) with matching intent filter.

### getColor

```
public @Nullable String getColor()
```

Gets the color of the notification, or null if not set.

Color is expressed in #rrggbb format.

### getDefaultLightSettings

```
public boolean getDefaultLightSettings()
```

Gets whether or not the notification uses the default notification light settings.

See details about `defaultLightSettings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `boolean` | `true` if it is set to `true`; Otherwise `false`. |

### getDefaultSound

```
public boolean getDefaultSound()
```

Gets whether or not the notification uses the default sound.

See details about `defaultSound` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `boolean` | `true` if it is set to `true`; Otherwise `false`. |

### getDefaultVibrateSettings

```
public boolean getDefaultVibrateSettings()
```

Gets whether or not the notification uses the default vibrate pattern.

See details about `defaultVibrateTimings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `boolean` | `true` if it is set to `true`; Otherwise `false`. |

### getEventTime

```
public @Nullable Long getEventTime()
```

Gets the `eventTime` from the notification.

See details about `eventTime` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

### getIcon

```
public @Nullable String getIcon()
```

Gets the image resource name of the icon of the notification, or null if not set.

### getImageUrl

```
public @Nullable Uri getImageUrl()
```

Gets the image URL from the notification.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | The image URL if it was set, null otherwise. |

### getLightSettings

```
public @Nullable int[] getLightSettings()
```

Gets the `lightSettings` from the notification. `lightSettings` is an primitive integer array of size three that includes `color`, `lightOnDuration` and `
lightOffDuration` respectively.

See details about `lightSettings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

### getLink

```
public @Nullable Uri getLink()
```

Gets the deep link from the notification, or null if not set.

### getLocalOnly

```
public boolean getLocalOnly()
```

Gets whether or not this notification is only relevant to the current device.

See details about `localOnly` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `boolean` | `true` if it is set to `true`; Otherwise `false`. |

### getNotificationCount

```
public @Nullable Integer getNotificationCount()
```

Gets the `notificationCount` from the notification.

See details about `notificationCount` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

### getNotificationPriority

```
public @Nullable Integer getNotificationPriority()
```

Gets the `notificationPriority` from the notification.

See details about `notificationPriority` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

### getSound

```
public @Nullable String getSound()
```

Gets the sound to be played when the notification is shown, or null if not set.

This will be either a raw resource name, or "default" for the user's default notification sound.

### getSticky

```
public boolean getSticky()
```

Gets whether or not the notification is considered sticky.

See details about `sticky` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

| Returns |
|---|---|
| `boolean` | `true` if it is set to `true`; Otherwise `false`. |

### getTag

```
public @Nullable String getTag()
```

Gets the tag of the notification, or null if not set.

### getTicker

```
public @Nullable String getTicker()
```

Gets the ticker text from the notification.

### getTitle

```
public @Nullable String getTitle()
```

Gets the title of the notification, or null if not set.

### getTitleLocalizationArgs

```
public @Nullable String[] getTitleLocalizationArgs()
```

Gets the variable string values to be used as format specifiers in the title localization key, or null if not set.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification#getTitleLocalizationKey()` |   |

### getTitleLocalizationKey

```
public @Nullable String getTitleLocalizationKey()
```

Gets the string resource name to use to localize the title of the notification, or null if not set.

### getVibrateTimings

```
public @Nullable long[] getVibrateTimings()
```

Gets the `vibrateTimings` from the notification.

See details about `vibrateTimings` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).

### getVisibility

```
public @Nullable Integer getVisibility()
```

Gets the `visibility` from the notification.

See details about `visibility` in [Firebase Cloud Messaging Reference: HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification).