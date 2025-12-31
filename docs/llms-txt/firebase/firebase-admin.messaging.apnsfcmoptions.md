# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsfcmoptions.md.txt

# ApnsFcmOptions interface

Represents options for features provided by the FCM SDK for iOS.

**Signature:**  

    export interface ApnsFcmOptions 

## Properties

|                                                                    Property                                                                     |  Type  |                       Description                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------|
| [analyticsLabel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsfcmoptions.md#apnsfcmoptionsanalyticslabel) | string | The label associated with the message's analytics data. |
| [imageUrl](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsfcmoptions.md#apnsfcmoptionsimageurl)             | string | URL of an image to be displayed in the notification.    |

## ApnsFcmOptions.analyticsLabel

The label associated with the message's analytics data.

**Signature:**  

    analyticsLabel?: string;

## ApnsFcmOptions.imageUrl

URL of an image to be displayed in the notification.

**Signature:**  

    imageUrl?: string;