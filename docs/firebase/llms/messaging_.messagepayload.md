# Source: https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md.txt

Message payload that contains the notification payload that is represented with [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_.notificationpayload.md#notificationpayload_interface) and the data payload that contains an arbitrary number of key-value pairs sent by developers through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).

**Signature:**  

    export interface MessagePayload 

## Properties

|                                                       Property                                                        |                                                                 Type                                                                 |                                                                                        Description                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [collapseKey](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloadcollapsekey)   | string                                                                                                                               | The collapse key of the message. See [Non-collapsible and collapsible messages](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages) |
| [data](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloaddata)                 | { \[key: string\]: string; }                                                                                                         | Arbitrary key/value payload.                                                                                                                                                               |
| [fcmOptions](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloadfcmoptions)     | [FcmOptions](https://firebase.google.com/docs/reference/js/messaging_.fcmoptions.md#fcmoptions_interface)                            | Options for features provided by the FCM SDK for Web. See [WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).                 |
| [from](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloadfrom)                 | string                                                                                                                               | The sender of this message.                                                                                                                                                                |
| [messageId](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloadmessageid)       | string                                                                                                                               | The message ID of a message.                                                                                                                                                               |
| [notification](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayloadnotification) | [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_.notificationpayload.md#notificationpayload_interface) | Display notification details. Details are sent through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).                              |

## MessagePayload.collapseKey

The collapse key of the message. See [Non-collapsible and collapsible messages](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages)

**Signature:**  

    collapseKey: string;

## MessagePayload.data

Arbitrary key/value payload.

**Signature:**  

    data?: {
            [key: string]: string;
        };

## MessagePayload.fcmOptions

Options for features provided by the FCM SDK for Web. See [WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).

**Signature:**  

    fcmOptions?: FcmOptions;

## MessagePayload.from

The sender of this message.

**Signature:**  

    from: string;

## MessagePayload.messageId

The message ID of a message.

**Signature:**  

    messageId: string;

## MessagePayload.notification

Display notification details. Details are sent through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).

**Signature:**  

    notification?: NotificationPayload;