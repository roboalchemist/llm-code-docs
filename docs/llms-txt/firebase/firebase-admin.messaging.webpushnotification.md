# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md.txt

# WebpushNotification interface

Represents the WebPush-specific notification options that can be included in [WebpushConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfig_interface). This supports most of the standard options as defined in the Web Notification [specification](https://developer.mozilla.org/en-US/docs/Web/API/notification/Notification).

**Signature:**  

    export interface WebpushNotification 

## Properties

|                                                                             Property                                                                              |                            Type                            |                                                                   Description                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [actions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationactions)                       | Array\<{ action: string; icon?: string; title: string; }\> | An array of notification actions representing the actions available to the user when the notification is presented.                             |
| [badge](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationbadge)                           | string                                                     | URL of the image used to represent the notification when there is not enough space to display the notification itself.                          |
| [body](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationbody)                             | string                                                     | Body text of the notification.                                                                                                                  |
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationdata)                             | any                                                        | Arbitrary data that you want associated with the notification. This can be of any data type.                                                    |
| [dir](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationdir)                               | 'auto' \| 'ltr' \| 'rtl'                                   | The direction in which to display the notification. Must be one of `auto`, `ltr` or `rtl`.                                                      |
| [icon](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationicon)                             | string                                                     | URL to the notification icon.                                                                                                                   |
| [image](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationimage)                           | string                                                     | URL of an image to be displayed in the notification.                                                                                            |
| [lang](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationlang)                             | string                                                     | The notification's language as a BCP 47 language tag.                                                                                           |
| [renotify](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationrenotify)                     | boolean                                                    | A boolean specifying whether the user should be notified after a new notification replaces an old one. Defaults to false.                       |
| [requireInteraction](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationrequireinteraction) | boolean                                                    | Indicates that a notification should remain active until the user clicks or dismisses it, rather than closing automatically. Defaults to false. |
| [silent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationsilent)                         | boolean                                                    | A boolean specifying whether the notification should be silent. Defaults to false.                                                              |
| [tag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationtag)                               | string                                                     | An identifying tag for the notification.                                                                                                        |
| [timestamp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationtimestamp)                   | number                                                     | Timestamp of the notification. Refer to https://developer.mozilla.org/en-US/docs/Web/API/notification/timestamp for details.                    |
| [title](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationtitle)                           | string                                                     | Title text of the notification.                                                                                                                 |
| [vibrate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotificationvibrate)                       | number \| number\[\]                                       | A vibration pattern for the device's vibration hardware to emit when the notification fires.                                                    |

## WebpushNotification.actions

An array of notification actions representing the actions available to the user when the notification is presented.

**Signature:**  

    actions?: Array<{
            action: string;
            icon?: string;
            title: string;
        }>;

## WebpushNotification.badge

URL of the image used to represent the notification when there is not enough space to display the notification itself.

**Signature:**  

    badge?: string;

## WebpushNotification.body

Body text of the notification.

**Signature:**  

    body?: string;

## WebpushNotification.data

Arbitrary data that you want associated with the notification. This can be of any data type.

**Signature:**  

    data?: any;

## WebpushNotification.dir

The direction in which to display the notification. Must be one of `auto`, `ltr` or `rtl`.

**Signature:**  

    dir?: 'auto' | 'ltr' | 'rtl';

## WebpushNotification.icon

URL to the notification icon.

**Signature:**  

    icon?: string;

## WebpushNotification.image

URL of an image to be displayed in the notification.

**Signature:**  

    image?: string;

## WebpushNotification.lang

The notification's language as a BCP 47 language tag.

**Signature:**  

    lang?: string;

## WebpushNotification.renotify

A boolean specifying whether the user should be notified after a new notification replaces an old one. Defaults to false.

**Signature:**  

    renotify?: boolean;

## WebpushNotification.requireInteraction

Indicates that a notification should remain active until the user clicks or dismisses it, rather than closing automatically. Defaults to false.

**Signature:**  

    requireInteraction?: boolean;

## WebpushNotification.silent

A boolean specifying whether the notification should be silent. Defaults to false.

**Signature:**  

    silent?: boolean;

## WebpushNotification.tag

An identifying tag for the notification.

**Signature:**  

    tag?: string;

## WebpushNotification.timestamp

Timestamp of the notification. Refer to https://developer.mozilla.org/en-US/docs/Web/API/notification/timestamp for details.

**Signature:**  

    timestamp?: number;

## WebpushNotification.title

Title text of the notification.

**Signature:**  

    title?: string;

## WebpushNotification.vibrate

A vibration pattern for the device's vibration hardware to emit when the notification fires.

**Signature:**  

    vibrate?: number | number[];