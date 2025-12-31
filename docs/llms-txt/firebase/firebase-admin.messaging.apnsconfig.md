# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md.txt

# ApnsConfig interface

Represents the APNs-specific options that can be included in an [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message). Refer to [Apple documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for various headers and payload fields supported by APNs.

**Signature:**  

    export interface ApnsConfig 

## Properties

|                                                                   Property                                                                    |                                                                    Type                                                                     |                                Description                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [fcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md#apnsconfigfcmoptions)               | [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsfcmoptions.md#apnsfcmoptions_interface) | Options for features provided by the FCM SDK for iOS.                     |
| [headers](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md#apnsconfigheaders)                     | { \[key: string\]: string; }                                                                                                                | A collection of APNs headers. Header values must be strings.              |
| [liveActivityToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md#apnsconfigliveactivitytoken) | string                                                                                                                                      | APN `pushToStartToken` or `pushToken` to start or update live activities. |
| [payload](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnsconfig.md#apnsconfigpayload)                     | [ApnsPayload](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnspayload.md#apnspayload_interface)          | An APNs payload to be included in the message.                            |

## ApnsConfig.fcmOptions

Options for features provided by the FCM SDK for iOS.

**Signature:**  

    fcmOptions?: ApnsFcmOptions;

## ApnsConfig.headers

A collection of APNs headers. Header values must be strings.

**Signature:**  

    headers?: {
            [key: string]: string;
        };

## ApnsConfig.liveActivityToken

APN `pushToStartToken` or `pushToken` to start or update live activities.

**Signature:**  

    liveActivityToken?: string;

## ApnsConfig.payload

An APNs payload to be included in the message.

**Signature:**  

    payload?: ApnsPayload;