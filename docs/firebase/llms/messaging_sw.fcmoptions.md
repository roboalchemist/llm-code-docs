# Source: https://firebase.google.com/docs/reference/js/messaging_sw.fcmoptions.md.txt

# FcmOptions interface

Options for features provided by the FCM SDK for Web. See [WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).

**Signature:**  

    export interface FcmOptions 

## Properties

|                                                      Property                                                       |  Type  |                        Description                         |
|---------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------|
| [analyticsLabel](https://firebase.google.com/docs/reference/js/messaging_sw.fcmoptions.md#fcmoptionsanalyticslabel) | string | The label associated with the message's analytics data.    |
| [link](https://firebase.google.com/docs/reference/js/messaging_sw.fcmoptions.md#fcmoptionslink)                     | string | The link to open when the user clicks on the notification. |

## FcmOptions.analyticsLabel

The label associated with the message's analytics data.

**Signature:**  

    analyticsLabel?: string;

## FcmOptions.link

The link to open when the user clicks on the notification.

**Signature:**  

    link?: string;