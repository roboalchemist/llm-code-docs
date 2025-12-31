# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md.txt

# Aps interface

Represents the [aps dictionary](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html) that is part of APNs messages.

**Signature:**  

    export interface Aps 

## Properties

|                                                           Property                                                            |                                                                        Type                                                                        |                                                              Description                                                              |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [alert](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apsalert)                       | string \| [ApsAlert](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apsalert.md#apsalert_interface)                | Alert to be included in the message. This may be a string or an object of type `admin.messaging.ApsAlert`.                            |
| [badge](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apsbadge)                       | number                                                                                                                                             | Badge to be displayed with the message. Set to 0 to remove the badge. When not specified, the badge will remain unchanged.            |
| [category](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apscategory)                 | string                                                                                                                                             | Type of the notification.                                                                                                             |
| [contentAvailable](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apscontentavailable) | boolean                                                                                                                                            | Specifies whether to configure a background update notification.                                                                      |
| [mutableContent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apsmutablecontent)     | boolean                                                                                                                                            | Specifies whether to set the `mutable-content` property on the message so the clients can modify the notification via app extensions. |
| [sound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apssound)                       | string \| [CriticalSound](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.criticalsound.md#criticalsound_interface) | Sound to be played with the message.                                                                                                  |
| [threadId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#apsthreadid)                 | string                                                                                                                                             | An app-specific identifier for grouping notifications.                                                                                |

## Aps.alert

Alert to be included in the message. This may be a string or an object of type `admin.messaging.ApsAlert`.

**Signature:**  

    alert?: string | ApsAlert;

## Aps.badge

Badge to be displayed with the message. Set to 0 to remove the badge. When not specified, the badge will remain unchanged.

**Signature:**  

    badge?: number;

## Aps.category

Type of the notification.

**Signature:**  

    category?: string;

## Aps.contentAvailable

Specifies whether to configure a background update notification.

**Signature:**  

    contentAvailable?: boolean;

## Aps.mutableContent

Specifies whether to set the `mutable-content` property on the message so the clients can modify the notification via app extensions.

**Signature:**  

    mutableContent?: boolean;

## Aps.sound

Sound to be played with the message.

**Signature:**  

    sound?: string | CriticalSound;

## Aps.threadId

An app-specific identifier for grouping notifications.

**Signature:**  

    threadId?: string;