# Source: https://documentation.onesignal.com/docs/en/osnotification-payload.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OSNotification payload

> Reference for OneSignal's OSNotification object, including all payload fields, Android and iOS-specific properties, custom data, and click actions.

## `OSNotification` payload reference

This page explains the structure and fields of the OneSignal push notification payload via the `OSNotification` class. Use this reference when receiving or handling notifications in your mobile app.

<Info>
  Push notification payloads are limited to `4096` bytes. To avoid truncation, keep payloads under `3500` bytes. The `additionalData` field is limited to `2048` bytes.
</Info>

***

## Accessing `OSNotification` in your app

All OneSignal SDKs trigger a notification event listener that returns an `OSNotification` object.

* **Android**: `OneSignal.setNotificationWillShowInForegroundHandler(...)`
* **iOS**: `notificationReceivedBlock` or `UNNotificationServiceExtension`

Use this object to access notification title, body, data, and other properties.

The `OSNotification` class provides all notification payload data accessible within SDK notification event listeners. It merges the original `OSNotification` and `OSNotificationPayload` classes into a single, getter-based interface.

### Android fields

| Property                     |           Type          | Description                                                          |
| ---------------------------- | :---------------------: | -------------------------------------------------------------------- |
| `getBody()`                  |         `String`        | Body text of the notification.                                       |
| `getTitle()`                 |         `String`        | Title of the notification.                                           |
| `getLaunchURL()`             |         `String`        | URL opened when the notification is clicked.                         |
| `getNotificationId()`        |         `String`        | OneSignal notification UUID.                                         |
| `getAdditionalData()`        |       `JSONObject`      | Custom key-value data set via dashboard or REST API. Max 2048 bytes. |
| `getTemplateId()`            |         `String`        | Template UUID, if sent using templates.                              |
| `getAndroidNotificationId()` |          `int`          | Android native notification ID.                                      |
| `getLargeIcon()`             |         `String`        | URL or resource name of large icon.                                  |
| `getSmallIcon()`             |         `String`        | Small icon resource name.                                            |
| `getSmallIconAccentColor()`  |         `String`        | Icon accent color in ARGB format.                                    |
| `getSound()`                 |         `String`        | Sound resource name played.                                          |
| `getCollapseId()`            |         `String`        | Collapse key for notification replacement.                           |
| `getPriority()`              |          `int`          | Android priority (-2 to 2).                                          |
| `getLedColor()`              |         `String`        | LED color in ARGB format.                                            |
| `getLockScreenVisibility()`  |          `int`          | Lock screen visibility: `1 = public`, `0 = private`, `-1 = secret`.  |
| `getFromProjectNumber()`     |         `String`        | Sender project number.                                               |
| `getGroupedNotifications()`  |  `List<OSNotification>` | Notifications included in a summary.                                 |
| `getGroupKey()`              |         `String`        | Group key used in summaries.                                         |
| `getGroupMessage()`          |         `String`        | Summary text.                                                        |
| `getBackgroundImageLayout()` | `BackgroundImageLayout` | Object for background image layout and text colors.                  |
| `getActionButtons()`         |   `List<ActionButton>`  | Action buttons with icon, text, and ID.                              |
| `getRawPayload()`            |         `String`        | Full raw JSON string of the payload.                                 |

### iOS fields

| Property           |      Type      | Description                                                                  |
| ------------------ | :------------: | ---------------------------------------------------------------------------- |
| `body`             |   `NSString`   | Body text of the notification.                                               |
| `title`            |   `NSString`   | Title of the notification.                                                   |
| `launchURL`        |   `NSString`   | URL opened when the notification is clicked.                                 |
| `notificationId`   |   `NSString`   | OneSignal notification UUID.                                                 |
| `additionalData`   |  `Dictionary`  | Custom key-value `data` set via dashboard or REST API. Max 2048 bytes.       |
| `templateId`       |   `NSString`   | Template UUID, if sent using templates.                                      |
| `subtitle`         |   `NSString`   | Subtitle text.                                                               |
| `category`         |   `NSString`   | iOS category identifier.                                                     |
| `threadId`         |   `NSString`   | Used to group notifications into threads (iOS 10+).                          |
| `badge`            |   `NSInteger`  | Absolute badge value.                                                        |
| `badgeIncrement`   |   `NSInteger`  | Amount to increment the badge.                                               |
| `contentAvailable` |     `BOOL`     | If `content-available=1`, triggers background fetch.                         |
| `mutableContent`   |     `BOOL`     | If `mutable-content=1`, triggers a Notification Service Extension.           |
| `actionButtons`    |    `NSArray`   | iOS action buttons.                                                          |
| `rawPayload`       | `NSDictionary` | Full raw JSON of the payload.                                                |
| `parseWithApns`    |    *Method*    | Converts raw APNS payload into an OSNotification. Use in service extensions. |

***

## `OSNotificationAction` (click events)

Describes the user's interaction with the notification.

| Property   |   Type   | Description                                           |
| ---------- | :------: | ----------------------------------------------------- |
| `actionId` | `String` | The ID of the clicked action button.                  |
| `type`     |  `enum`  | `Opened` (default tap) or `ActionTaken` (button tap). |

***

## Custom OneSignal payload structure

All OneSignal notifications include a special `"custom"` object in the payload:

```json  theme={null}
{
  "custom": {
    "i": "the-notification-id"
  }
}
```

<Info>
  This key is required for OneSignal SDKs to process the notification. If missing, notifications will not trigger click events or analytics.

  If sending a push from a different service to a device already using OneSignal, avoid duplicating notifications.
</Info>

***

## Optional: move additionalData to APNS root

For iOS apps, you can make `additionalData` available in the root of the APNS payload for easier access in custom handlers.

1. Enable in app settings
   Use the [Update an app API](/reference/update-an-app) and set:

```json  theme={null}
{
  "additional_data_is_root_payload": true
}
```

1. Send push with `data`
   It will be available in the root of the APNS payload. Example:

```json  theme={null}
{
  "aps": {
    "alert": { "title": "Sale", "body": "20% off all items!" }
  },
  "promo_code": "SPRING20"
}
```

Now you can directly access `promo_code` without checking the custom dictionary.

***

## Restored notifications

Notifications will be restored by the Android SDK after a reboot or app restart.

| Property    |    Type   | Description                                                       |
| ----------- | :-------: | ----------------------------------------------------------------- |
| `restoring` | `boolean` | `true` if the notification was restored after device/app restart. |

<Info>
  Restored notifications can be skipped using the `restoring` flag. To avoid restoring old content, set a short or 0 TTL (time-to-live) on your notifications.
</Info>

***

## Related topics

* [Android notification categories](./android-notification-categories)
* [Mobile Service Extensions](./service-extensions)
* [Mobile SDK reference](./mobile-sdk-reference)

***

Built with [Mintlify](https://mintlify.com).
