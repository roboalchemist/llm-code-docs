# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md.txt

# AndroidNotification interface

Represents the Android-specific notification options that can be included in [AndroidConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfig_interface).

**Signature:**  

    export interface AndroidNotification 

## Properties

|                                                                                Property                                                                                 |                                                                   Type                                                                   |                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [body](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationbody)                                   | string                                                                                                                                   | Body of the Android notification. When provided, overrides the body set via `admin.messaging.Notification`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [bodyLocArgs](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationbodylocargs)                     | string\[\]                                                                                                                               | An array of resource keys that will be used in place of the format specifiers in `bodyLocKey`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bodyLocKey](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationbodylockey)                       | string                                                                                                                                   | Key of the body string in the app's string resource to use to localize the body text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [channelId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationchannelid)                         | string                                                                                                                                   | The Android notification channel ID (new in Android O). The app must create a channel with this channel ID before any notification with this channel ID can be received. If you don't send this channel ID in the request, or if the channel ID provided has not yet been created by the app, FCM uses the channel ID specified in the app manifest.                                                                                                                                                                                                                               |
| [clickAction](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationclickaction)                     | string                                                                                                                                   | Action associated with a user click on the notification. If specified, an activity with a matching Intent Filter is launched when a user clicks on the notification.                                                                                                                                                                                                                                                                                                                                                                                                               |
| [color](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationcolor)                                 | string                                                                                                                                   | Notification icon color in `#rrggbb` format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [defaultLightSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationdefaultlightsettings)   | boolean                                                                                                                                  | If set to `true`, use the Android framework's default LED light settings for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If `default_light_settings` is set to `true` and `light_settings` is also set, the user-specified `light_settings` is used instead of the default value.                                                                                                                                                                           |
| [defaultSound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationdefaultsound)                   | boolean                                                                                                                                  | If set to `true`, use the Android framework's default sound for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml).                                                                                                                                                                                                                                                                                                                                                 |
| [defaultVibrateTimings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationdefaultvibratetimings) | boolean                                                                                                                                  | If set to `true`, use the Android framework's default vibrate pattern for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If `defaultVibrateTimings` is set to `true` and `vibrateTimingsMillis` is also set, the default value is used instead of the user-specified `vibrateTimingsMillis`.                                                                                                                                                                   |
| [eventTimestamp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationeventtimestamp)               | Date                                                                                                                                     | For notifications that inform users about events with an absolute time reference, sets the time that the event in the notification occurred. Notifications in the panel are sorted by this time.                                                                                                                                                                                                                                                                                                                                                                                   |
| [icon](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationicon)                                   | string                                                                                                                                   | Icon resource for the Android notification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [imageUrl](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationimageurl)                           | string                                                                                                                                   | URL of an image to be displayed in the notification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [lightSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationlightsettings)                 | [LightSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.lightsettings.md#lightsettings_interface) | Settings to control the notification's LED blinking rate and color if LED is available on the device. The total blinking time is controlled by the OS.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [localOnly](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationlocalonly)                         | boolean                                                                                                                                  | Sets whether or not this notification is relevant only to the current device. Some notifications can be bridged to other devices for remote display, such as a Wear OS watch. This hint can be set to recommend this notification not be bridged. See [Wear OS guides](https://developer.android.com/training/wearables/notifications/bridger#existing-method-of-preventing-bridging).                                                                                                                                                                                             |
| [notificationCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationnotificationcount)         | number                                                                                                                                   | Sets the number of items this notification represents. May be displayed as a badge count for Launchers that support badging. See [NotificationBadge](https://developer.android.com/training/notify-user/badges). For example, this might be useful if you're using just one notification to represent multiple new messages but you want the count here to represent the number of total new messages. If zero or unspecified, systems that support badging use the default, which is to increment a number displayed on the long-press menu each time a new notification arrives. |
| [priority](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationpriority)                           | ('min' \| 'low' \| 'default' \| 'high' \| 'max')                                                                                         | Sets the relative priority for this notification. Low-priority notifications may be hidden from the user in certain situations. Note this priority differs from `AndroidMessagePriority`. This priority is processed by the client after the message has been delivered. Whereas `AndroidMessagePriority` is an FCM concept that controls when the message is delivered.                                                                                                                                                                                                           |
| [proxy](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationproxy)                                 | ('allow' \| 'deny' \| 'if_priority_lowered')                                                                                             | Sets if this notification should attempt to be proxied. Must be either `allow`, `deny` or `if_priority_lowered`. If unspecified, it remains undefined in the Admin SDK, and defers to the FCM backend's default mapping.                                                                                                                                                                                                                                                                                                                                                           |
| [sound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationsound)                                 | string                                                                                                                                   | File name of the sound to be played when the device receives the notification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [sticky](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationsticky)                               | boolean                                                                                                                                  | When set to `false` or unset, the notification is automatically dismissed when the user clicks it in the panel. When set to `true`, the notification persists even when the user clicks it.                                                                                                                                                                                                                                                                                                                                                                                        |
| [tag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationtag)                                     | string                                                                                                                                   | Notification tag. This is an identifier used to replace existing notifications in the notification drawer. If not specified, each request creates a new notification.                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ticker](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationticker)                               | string                                                                                                                                   | Sets the "ticker" text, which is sent to accessibility services. Prior to API level 21 (Lollipop), sets the text that is displayed in the status bar when the notification first arrives.                                                                                                                                                                                                                                                                                                                                                                                          |
| [title](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationtitle)                                 | string                                                                                                                                   | Title of the Android notification. When provided, overrides the title set via `admin.messaging.Notification`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [titleLocArgs](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationtitlelocargs)                   | string\[\]                                                                                                                               | An array of resource keys that will be used in place of the format specifiers in `titleLocKey`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [titleLocKey](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationtitlelockey)                     | string                                                                                                                                   | Key of the title string in the app's string resource to use to localize the title text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [vibrateTimingsMillis](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationvibratetimingsmillis)   | number\[\]                                                                                                                               | Sets the vibration pattern to use. Pass in an array of milliseconds to turn the vibrator on or off. The first value indicates the duration to wait before turning the vibrator on. The next value indicates the duration to keep the vibrator on. Subsequent values alternate between duration to turn the vibrator off and to turn the vibrator on. If `vibrateTimingsMillis` is set and `defaultVibrateTimings` is set to `true`, the default value is used instead of the user-specified `vibrateTimingsMillis`.                                                                |
| [visibility](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotificationvisibility)                       | ('private' \| 'public' \| 'secret')                                                                                                      | Sets the visibility of the notification. Must be either `private`, `public`, or `secret`. If unspecified, it remains undefined in the Admin SDK, and defers to the FCM backend's default mapping.                                                                                                                                                                                                                                                                                                                                                                                  |

## AndroidNotification.body

Body of the Android notification. When provided, overrides the body set via `admin.messaging.Notification`.

**Signature:**  

    body?: string;

## AndroidNotification.bodyLocArgs

An array of resource keys that will be used in place of the format specifiers in `bodyLocKey`.

**Signature:**  

    bodyLocArgs?: string[];

## AndroidNotification.bodyLocKey

Key of the body string in the app's string resource to use to localize the body text.

**Signature:**  

    bodyLocKey?: string;

## AndroidNotification.channelId

The Android notification channel ID (new in Android O). The app must create a channel with this channel ID before any notification with this channel ID can be received. If you don't send this channel ID in the request, or if the channel ID provided has not yet been created by the app, FCM uses the channel ID specified in the app manifest.

**Signature:**  

    channelId?: string;

## AndroidNotification.clickAction

Action associated with a user click on the notification. If specified, an activity with a matching Intent Filter is launched when a user clicks on the notification.

**Signature:**  

    clickAction?: string;

## AndroidNotification.color

Notification icon color in `#rrggbb` format.

**Signature:**  

    color?: string;

## AndroidNotification.defaultLightSettings

If set to `true`, use the Android framework's default LED light settings for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If `default_light_settings` is set to `true` and `light_settings` is also set, the user-specified `light_settings` is used instead of the default value.

**Signature:**  

    defaultLightSettings?: boolean;

## AndroidNotification.defaultSound

If set to `true`, use the Android framework's default sound for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml).

**Signature:**  

    defaultSound?: boolean;

## AndroidNotification.defaultVibrateTimings

If set to `true`, use the Android framework's default vibrate pattern for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If `defaultVibrateTimings` is set to `true` and `vibrateTimingsMillis` is also set, the default value is used instead of the user-specified `vibrateTimingsMillis`.

**Signature:**  

    defaultVibrateTimings?: boolean;

## AndroidNotification.eventTimestamp

For notifications that inform users about events with an absolute time reference, sets the time that the event in the notification occurred. Notifications in the panel are sorted by this time.

**Signature:**  

    eventTimestamp?: Date;

## AndroidNotification.icon

Icon resource for the Android notification.

**Signature:**  

    icon?: string;

## AndroidNotification.imageUrl

URL of an image to be displayed in the notification.

**Signature:**  

    imageUrl?: string;

## AndroidNotification.lightSettings

Settings to control the notification's LED blinking rate and color if LED is available on the device. The total blinking time is controlled by the OS.

**Signature:**  

    lightSettings?: LightSettings;

## AndroidNotification.localOnly

Sets whether or not this notification is relevant only to the current device. Some notifications can be bridged to other devices for remote display, such as a Wear OS watch. This hint can be set to recommend this notification not be bridged. See [Wear OS guides](https://developer.android.com/training/wearables/notifications/bridger#existing-method-of-preventing-bridging).

**Signature:**  

    localOnly?: boolean;

## AndroidNotification.notificationCount

Sets the number of items this notification represents. May be displayed as a badge count for Launchers that support badging. See [NotificationBadge](https://developer.android.com/training/notify-user/badges). For example, this might be useful if you're using just one notification to represent multiple new messages but you want the count here to represent the number of total new messages. If zero or unspecified, systems that support badging use the default, which is to increment a number displayed on the long-press menu each time a new notification arrives.

**Signature:**  

    notificationCount?: number;

## AndroidNotification.priority

Sets the relative priority for this notification. Low-priority notifications may be hidden from the user in certain situations. Note this priority differs from `AndroidMessagePriority`. This priority is processed by the client after the message has been delivered. Whereas `AndroidMessagePriority` is an FCM concept that controls when the message is delivered.

**Signature:**  

    priority?: ('min' | 'low' | 'default' | 'high' | 'max');

## AndroidNotification.proxy

Sets if this notification should attempt to be proxied. Must be either `allow`, `deny` or `if_priority_lowered`. If unspecified, it remains undefined in the Admin SDK, and defers to the FCM backend's default mapping.

**Signature:**  

    proxy?: ('allow' | 'deny' | 'if_priority_lowered');

## AndroidNotification.sound

File name of the sound to be played when the device receives the notification.

**Signature:**  

    sound?: string;

## AndroidNotification.sticky

When set to `false` or unset, the notification is automatically dismissed when the user clicks it in the panel. When set to `true`, the notification persists even when the user clicks it.

**Signature:**  

    sticky?: boolean;

## AndroidNotification.tag

Notification tag. This is an identifier used to replace existing notifications in the notification drawer. If not specified, each request creates a new notification.

**Signature:**  

    tag?: string;

## AndroidNotification.ticker

Sets the "ticker" text, which is sent to accessibility services. Prior to API level 21 (Lollipop), sets the text that is displayed in the status bar when the notification first arrives.

**Signature:**  

    ticker?: string;

## AndroidNotification.title

Title of the Android notification. When provided, overrides the title set via `admin.messaging.Notification`.

**Signature:**  

    title?: string;

## AndroidNotification.titleLocArgs

An array of resource keys that will be used in place of the format specifiers in `titleLocKey`.

**Signature:**  

    titleLocArgs?: string[];

## AndroidNotification.titleLocKey

Key of the title string in the app's string resource to use to localize the title text.

**Signature:**  

    titleLocKey?: string;

## AndroidNotification.vibrateTimingsMillis

Sets the vibration pattern to use. Pass in an array of milliseconds to turn the vibrator on or off. The first value indicates the duration to wait before turning the vibrator on. The next value indicates the duration to keep the vibrator on. Subsequent values alternate between duration to turn the vibrator off and to turn the vibrator on. If `vibrateTimingsMillis` is set and `defaultVibrateTimings` is set to `true`, the default value is used instead of the user-specified `vibrateTimingsMillis`.

**Signature:**  

    vibrateTimingsMillis?: number[];

## AndroidNotification.visibility

Sets the visibility of the notification. Must be either `private`, `public`, or `secret`. If unspecified, it remains undefined in the Admin SDK, and defers to the FCM backend's default mapping.

**Signature:**  

    visibility?: ('private' | 'public' | 'secret');