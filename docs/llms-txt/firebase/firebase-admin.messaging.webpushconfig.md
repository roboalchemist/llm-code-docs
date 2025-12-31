# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md.txt

# WebpushConfig interface

Represents the WebPush protocol options that can be included in an [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message).

**Signature:**  

    export interface WebpushConfig 

## Properties

|                                                                 Property                                                                  |                                                                            Type                                                                            |                                                                           Description                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfigdata)                 | { \[key: string\]: string; }                                                                                                                               | A collection of data fields.                                                                                                                                     |
| [fcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfigfcmoptions)     | [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushfcmoptions.md#webpushfcmoptions_interface)       | Options for features provided by the FCM SDK for Web.                                                                                                            |
| [headers](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfigheaders)           | { \[key: string\]: string; }                                                                                                                               | A collection of WebPush headers. Header values must be strings.See [WebPush specification](https://tools.ietf.org/html/rfc8030#section-5) for supported headers. |
| [notification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushconfig.md#webpushconfignotification) | [WebpushNotification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushnotification.md#webpushnotification_interface) | A WebPush notification payload to be included in the message.                                                                                                    |

## WebpushConfig.data

A collection of data fields.

**Signature:**  

    data?: {
            [key: string]: string;
        };

## WebpushConfig.fcmOptions

Options for features provided by the FCM SDK for Web.

**Signature:**  

    fcmOptions?: WebpushFcmOptions;

## WebpushConfig.headers

A collection of WebPush headers. Header values must be strings.

See [WebPush specification](https://tools.ietf.org/html/rfc8030#section-5) for supported headers.

**Signature:**  

    headers?: {
            [key: string]: string;
        };

## WebpushConfig.notification

A WebPush notification payload to be included in the message.

**Signature:**  

    notification?: WebpushNotification;