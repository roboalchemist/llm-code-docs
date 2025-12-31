# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder.md.txt

# AndroidNotification.Builder

public static class **AndroidNotification.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [addAllBodyLocalizationArgs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#addAllBodyLocalizationArgs(java.util.List<java.lang.String>))(List\<String\> args) Adds a list of resource keys that will be used in place of the format specifiers in `bodyLocKey`.                                                                                                                            |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [addAllTitleLocalizationArgs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#addAllTitleLocalizationArgs(java.util.List<java.lang.String>))(List\<String\> args) Adds a list of resource keys that will be used in place of the format specifiers in `titleLocKey`.                                                                                                                         |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [addBodyLocalizationArg](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#addBodyLocalizationArg(java.lang.String))(String arg) Adds a resource key string that will be used in place of the format specifiers in `bodyLocKey`.                                                                                                                                                               |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [addTitleLocalizationArg](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#addTitleLocalizationArg(java.lang.String))(String arg) Adds a resource key string that will be used in place of the format specifiers in `titleLocKey`.                                                                                                                                                            |
| [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#build())() Creates a new [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) instance from the parameters set on this builder.                                                                                                                  |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setBody](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setBody(java.lang.String))(String body) Sets the body of the Android notification.                                                                                                                                                                                                                                                 |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setBodyLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setBodyLocalizationKey(java.lang.String))(String bodyLocKey) Sets the key of the body string in the app's string resources to use to localize the body text.                                                                                                                                                        |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setChannelId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setChannelId(java.lang.String))(String channelId) Sets the Android notification channel ID (new in Android O).                                                                                                                                                                                                                |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setClickAction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setClickAction(java.lang.String))(String clickAction) Sets the action associated with a user click on the notification.                                                                                                                                                                                                     |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setColor(java.lang.String))(String color) Sets the notification icon color.                                                                                                                                                                                                                                                       |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setDefaultLightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setDefaultLightSettings(boolean))(boolean defaultLightSettings) Sets the whether to use the default light settings.                                                                                                                                                                                                |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setDefaultSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setDefaultSound(boolean))(boolean defaultSound) Sets the whether to use the default sound.                                                                                                                                                                                                                                 |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setDefaultVibrateTimings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setDefaultVibrateTimings(boolean))(boolean defaultVibrateTimings) Sets the whether to use the default vibration timings.                                                                                                                                                                                          |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setEventTimeInMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setEventTimeInMillis(long))(long eventTimeInMillis) For notifications that inform users about events with an absolute time reference, sets the time that the event in the notification occurred in milliseconds.                                                                                                      |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setIcon](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setIcon(java.lang.String))(String icon) Sets the icon of the Android notification.                                                                                                                                                                                                                                                 |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setImage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setImage(java.lang.String))(String imageUrl) Sets the URL of the image that is going to be displayed in the notification.                                                                                                                                                                                                         |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setLightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setLightSettings(com.google.firebase.messaging.LightSettings))([LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings) lightSettings) Sets the settings to control the notification's LED blinking rate and color if LED is available on the device. |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setLocalOnly](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setLocalOnly(boolean))(boolean localOnly) Sets whether or not this notification is relevant only to the current device.                                                                                                                                                                                                       |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setNotificationCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setNotificationCount(int))(int notificationCount) Sets the number of items this notification represents.                                                                                                                                                                                                              |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setPriority(com.google.firebase.messaging.AndroidNotification.Priority))([AndroidNotification.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Priority) priority) Sets the relative priority for this notification.                                |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setProxy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setProxy(com.google.firebase.messaging.AndroidNotification.Proxy))([AndroidNotification.Proxy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Proxy) proxy) Sets the proxy of this notification.                                                               |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setSound(java.lang.String))(String sound) Sets the sound to be played when the device receives the notification.                                                                                                                                                                                                                  |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setSticky](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setSticky(boolean))(boolean sticky) Sets the sticky flag.                                                                                                                                                                                                                                                                        |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setTag](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setTag(java.lang.String))(String tag) Sets the notification tag.                                                                                                                                                                                                                                                                    |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setTicker](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setTicker(java.lang.String))(String ticker) Sets the "ticker" text, which is sent to accessibility services.                                                                                                                                                                                                                     |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setTitle](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setTitle(java.lang.String))(String title) Sets the title of the Android notification.                                                                                                                                                                                                                                             |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setTitleLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setTitleLocalizationKey(java.lang.String))(String titleLocKey) Sets the key of the title string in the app's string resources to use to localize the title text.                                                                                                                                                   |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setVibrateTimingsInMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setVibrateTimingsInMillis(long[]))(long\[\] vibrateTimingsInMillis) Sets a list of vibration timings in milliseconds in the array to use.                                                                                                                                                                        |
| [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [setVisibility](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder#setVisibility(com.google.firebase.messaging.AndroidNotification.Visibility))([AndroidNotification.Visibility](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Visibility) visibility) Sets the visibility of this notification.                            |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**addAllBodyLocalizationArgs**
(List\<String\> args)

Adds a list of resource keys that will be used in place of the format specifiers in
`bodyLocKey`.  

##### Parameters

| args | List of resource key strings. |
|------|-------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**addAllTitleLocalizationArgs**
(List\<String\> args)

Adds a list of resource keys that will be used in place of the format specifiers in
`titleLocKey`.  

##### Parameters

| args | List of resource key strings. |
|------|-------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**addBodyLocalizationArg**
(String arg)

Adds a resource key string that will be used in place of the format specifiers in
`bodyLocKey`.  

##### Parameters

| arg | Resource key string. |
|-----|----------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**addTitleLocalizationArg**
(String arg)

Adds a resource key string that will be used in place of the format specifiers in
`titleLocKey`.  

##### Parameters

| arg | Resource key string. |
|-----|----------------------|

##### Returns

- This builder.  

#### public [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification)
**build**
()

Creates a new [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) instance from the parameters set on this builder.  

##### Returns

- A new [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setBody**
(String body)

Sets the body of the Android notification. When provided, overrides the body set
via [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| body | Body of the notification. |
|------|---------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setBodyLocalizationKey**
(String bodyLocKey)

Sets the key of the body string in the app's string resources to use to localize the body
text.  

##### Parameters

| bodyLocKey | Resource key string. |
|------------|----------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setChannelId**
(String channelId)

Sets the Android notification channel ID (new in Android O). The app must create a channel
with this channel ID before any notification with this channel ID is received. If you
don't send this channel ID in the request, or if the channel ID provided has not yet been
created by the app, FCM uses the channel ID specified in the app manifest.  

##### Parameters

| channelId | The notification's channel ID. |
|-----------|--------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setClickAction**
(String clickAction)

Sets the action associated with a user click on the notification. If specified, an activity
with a matching Intent Filter is launched when a user clicks on the notification.  

##### Parameters

| clickAction | Click action name. |
|-------------|--------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setColor**
(String color)

Sets the notification icon color.  

##### Parameters

| color | Color specified in the `#rrggbb` format. |
|-------|------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setDefaultLightSettings**
(boolean defaultLightSettings)

Sets the whether to use the default light settings. If set to true, use the Android
framework's default LED light settings for the notification. Default values are
specified in config.xml. If `default_light_settings` is set to true and
`light_settings` is also set, the user-specified `light_settings` is used
instead of the default value.  

##### Parameters

| defaultLightSettings | The flag indicating whether to use the default light settings |
|----------------------|---------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setDefaultSound**
(boolean defaultSound)

Sets the whether to use the default sound. If set to true, use the Android framework's
default sound for the notification. Default values are specified in config.xml.  

##### Parameters

| defaultSound | The flag indicating whether to use the default sound |
|--------------|------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setDefaultVibrateTimings**
(boolean defaultVibrateTimings)

Sets the whether to use the default vibration timings. If set to true, use the Android
framework's default vibrate pattern for the notification. Default values are specified
in `config.xml`. If `default_vibrate_timings` is set to true and
`vibrate_timings` is also set, the default value is used instead of the
user-specified `vibrate_timings`.  

##### Parameters

| defaultVibrateTimings | The flag indicating whether to use the default vibration timings |
|-----------------------|------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setEventTimeInMillis**
(long eventTimeInMillis)

For notifications that inform users about events with an absolute time reference, sets
the time that the event in the notification occurred in milliseconds. Notifications
in the panel are sorted by this time. The time is formatted in RFC3339 UTC "Zulu"
format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". Note that
since the time is in milliseconds, the last section of the time representation always
has 6 leading zeros.  

##### Parameters

| eventTimeInMillis | The event time in milliseconds |
|-------------------|--------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setIcon**
(String icon)

Sets the icon of the Android notification.  

##### Parameters

| icon | Icon resource for the notification. |
|------|-------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setImage**
(String imageUrl)

Sets the URL of the image that is going to be displayed in the notification. When provided,
overrides the imageUrl set via [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| imageUrl | URL of the image that is going to be displayed in the notification. |
|----------|---------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setLightSettings**
([LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings) lightSettings)

Sets the settings to control the notification's LED blinking rate and color if LED is
available on the device. The total blinking time is controlled by the OS.  

##### Parameters

| lightSettings | The light settings to use |
|---------------|---------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setLocalOnly**
(boolean localOnly)

Sets whether or not this notification is relevant only to the current device. Some
notifications can be bridged to other devices for remote display, such as a Wear
OS watch. This hint can be set to recommend this notification not be bridged.  

##### Parameters

| localOnly | The "local only" flag |
|-----------|-----------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setNotificationCount**
(int notificationCount)

Sets the number of items this notification represents. May be displayed as a badge
count for launchers that support badging.
If not invoked then notification count is left unchanged.
For example, this might be useful if you're using just one notification to represent
multiple new messages but you want the count here to represent the number of total
new messages. If zero or unspecified, systems that support badging use the default,
which is to increment a number displayed on
the long-press menu each time a new notification arrives.  

##### Parameters

| notificationCount | Zero or positive value. Zero indicates leave unchanged. |
|-------------------|---------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setPriority**
([AndroidNotification.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Priority) priority)

Sets the relative priority for this notification. Priority is an indication of how much of
the user's attention should be consumed by this notification. Low-priority notifications
may be hidden from the user in certain situations, while the user might be interrupted
for a higher-priority notification.  

##### Parameters

| priority | The priority value, one of the values in {MIN, LOW, DEFAULT, HIGH, MAX} |
|----------|-------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setProxy**
([AndroidNotification.Proxy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Proxy) proxy)

Sets the proxy of this notification.  

##### Parameters

| proxy | The proxy value, one of the values in {ALLOW, DENY, IF_PRIORITY_LOWERED} |
|-------|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setSound**
(String sound)

Sets the sound to be played when the device receives the notification.  

##### Parameters

| sound | File name of the sound resource or "default". |
|-------|-----------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setSticky**
(boolean sticky)

Sets the sticky flag. When set to false or unset, the notification is automatically
dismissed when the user clicks it in the panel. When set to true, the notification
persists even when the user clicks it.  

##### Parameters

| sticky | The sticky flag |
|--------|-----------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setTag**
(String tag)

Sets the notification tag. This is an identifier used to replace existing notifications in
the notification drawer. If not specified, each request creates a new notification.  

##### Parameters

| tag | Notification tag. |
|-----|-------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setTicker**
(String ticker)

Sets the "ticker" text, which is sent to accessibility services. Prior to API level 21
(Lollipop), sets the text that is displayed in the status bar when the notification
first arrives.  

##### Parameters

| ticker | Ticker name. |
|--------|--------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setTitle**
(String title)

Sets the title of the Android notification. When provided, overrides the title set
via [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| title | Title of the notification. |
|-------|----------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setTitleLocalizationKey**
(String titleLocKey)

Sets the key of the title string in the app's string resources to use to localize the title
text.  

##### Parameters

| titleLocKey | Resource key string. |
|-------------|----------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setVibrateTimingsInMillis**
(long\[\] vibrateTimingsInMillis)

Sets a list of vibration timings in milliseconds in the array to use. The first value in the
array indicates the duration to wait before turning the vibrator on. The next value
indicates the duration to keep the vibrator on. Subsequent values alternate between
duration to turn the vibrator off and to turn the vibrator on. If `vibrate_timings`
is set and `default_vibrate_timings` is set to true, the default value is used instead
of the user-specified `vibrate_timings`.
A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".  

##### Parameters

| vibrateTimingsInMillis | List of vibration time in milliseconds |
|------------------------|----------------------------------------|

##### Returns

- This builder.  

#### public [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**setVisibility**
([AndroidNotification.Visibility](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Visibility) visibility)

Sets the visibility of this notification.  

##### Parameters

| visibility | The visibility value. one of the values in {PRIVATE, PUBLIC, SECRET} |
|------------|----------------------------------------------------------------------|

##### Returns

- This builder.