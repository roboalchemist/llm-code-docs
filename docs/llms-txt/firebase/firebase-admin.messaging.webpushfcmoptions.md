# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushfcmoptions.md.txt

# WebpushFcmOptions interface

Represents options for features provided by the FCM SDK for Web (which are not part of the Webpush standard).

**Signature:**  

    export interface WebpushFcmOptions 

## Properties

|                                                             Property                                                              |  Type  |                                            Description                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------|
| [link](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.webpushfcmoptions.md#webpushfcmoptionslink) | string | The link to open when the user clicks on the notification. For all URL values, HTTPS is required. |

## WebpushFcmOptions.link

The link to open when the user clicks on the notification. For all URL values, HTTPS is required.

**Signature:**  

    link?: string;