# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notification.md.txt

# Notification interface

A notification that can be included in [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message).

**Signature:**  

    export interface Notification 

## Properties

|                                                            Property                                                             |  Type  |                     Description                      |
|---------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------|
| [body](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notification.md#notificationbody)         | string | The notification body                                |
| [imageUrl](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notification.md#notificationimageurl) | string | URL of an image to be displayed in the notification. |
| [title](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notification.md#notificationtitle)       | string | The title of the notification.                       |

## Notification.body

The notification body

**Signature:**  

    body?: string;

## Notification.imageUrl

URL of an image to be displayed in the notification.

**Signature:**  

    imageUrl?: string;

## Notification.title

The title of the notification.

**Signature:**  

    title?: string;