# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md.txt

# BaseMessage interface

**Signature:**  

    export interface BaseMessage 

## Properties

|                                                               Property                                                                |                                                                   Type                                                                   | Description |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [android](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessageandroid)           | [AndroidConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfig_interface) |             |
| [apns](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessageapns)                 | [ApnsConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md#apnsconfig_interface)          |             |
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessagedata)                 | { \[key: string\]: string; }                                                                                                             |             |
| [fcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessagefcmoptions)     | [FcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.fcmoptions.md#fcmoptions_interface)          |             |
| [notification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessagenotification) | [Notification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notification.md#notification_interface)    |             |
| [webpush](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessagewebpush)           | [WebpushConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfig_interface) |             |

## BaseMessage.android

**Signature:**  

    android?: AndroidConfig;

## BaseMessage.apns

**Signature:**  

    apns?: ApnsConfig;

## BaseMessage.data

**Signature:**  

    data?: {
            [key: string]: string;
        };

## BaseMessage.fcmOptions

**Signature:**  

    fcmOptions?: FcmOptions;

## BaseMessage.notification

**Signature:**  

    notification?: Notification;

## BaseMessage.webpush

**Signature:**  

    webpush?: WebpushConfig;