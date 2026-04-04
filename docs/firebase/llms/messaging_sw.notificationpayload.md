# Source: https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md.txt

# NotificationPayload interface

Display notification details. Details are sent through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).

**Signature:**  

    export interface NotificationPayload 

## Properties

|                                                      Property                                                       |  Type  |                                                                      Description                                                                      |
|---------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [body](https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md#notificationpayloadbody)   | string | The notification's body text.                                                                                                                         |
| [icon](https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md#notificationpayloadicon)   | string | The URL to use for the notification's icon. If you don't send this key in the request, FCM displays the launcher icon specified in your app manifest. |
| [image](https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md#notificationpayloadimage) | string | The URL of an image that is downloaded on the device and displayed in the notification.                                                               |
| [title](https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md#notificationpayloadtitle) | string | The notification's title.                                                                                                                             |

## NotificationPayload.body

The notification's body text.

**Signature:**  

    body?: string;

## NotificationPayload.icon

The URL to use for the notification's icon. If you don't send this key in the request, FCM displays the launcher icon specified in your app manifest.

**Signature:**  

    icon?: string;

## NotificationPayload.image

The URL of an image that is downloaded on the device and displayed in the notification.

**Signature:**  

    image?: string;

## NotificationPayload.title

The notification's title.

**Signature:**  

    title?: string;