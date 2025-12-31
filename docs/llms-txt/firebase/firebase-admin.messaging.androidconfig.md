# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md.txt

# AndroidConfig interface

Represents the Android-specific options that can be included in an [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message).

**Signature:**  

    export interface AndroidConfig 

## Properties

|                                                                          Property                                                                           |                                                                            Type                                                                            |                                                                                                                            Description                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [collapseKey](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigcollapsekey)                     | string                                                                                                                                                     | Collapse key for the message. Collapse key serves as an identifier for a group of messages that can be collapsed, so that only the last message gets sent when delivery can be resumed. A maximum of four different collapse keys may be active at any given time. |
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigdata)                                   | { \[key: string\]: string; }                                                                                                                               | A collection of data fields to be included in the message. All values must be strings. When provided, overrides any data fields set on the top-level [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message).         |
| [directBootOk](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigdirectbootok)                   | boolean                                                                                                                                                    | A boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode.                                                                                                                                          |
| [fcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigfcmoptions)                       | [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidfcmoptions.md#androidfcmoptions_interface)       | Options for features provided by the FCM SDK for Android.                                                                                                                                                                                                          |
| [notification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfignotification)                   | [AndroidNotification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotification_interface) | Android notification to be included in the message.                                                                                                                                                                                                                |
| [priority](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigpriority)                           | ('high' \| 'normal')                                                                                                                                       | Priority of the message. Must be either `normal` or `high`.                                                                                                                                                                                                        |
| [restrictedPackageName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigrestrictedpackagename) | string                                                                                                                                                     | Package name of the application where the registration tokens must match in order to receive the message.                                                                                                                                                          |
| [ttl](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidconfig.md#androidconfigttl)                                     | number                                                                                                                                                     | Time-to-live duration of the message in milliseconds.                                                                                                                                                                                                              |

## AndroidConfig.collapseKey

Collapse key for the message. Collapse key serves as an identifier for a group of messages that can be collapsed, so that only the last message gets sent when delivery can be resumed. A maximum of four different collapse keys may be active at any given time.

**Signature:**  

    collapseKey?: string;

## AndroidConfig.data

A collection of data fields to be included in the message. All values must be strings. When provided, overrides any data fields set on the top-level [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message).

**Signature:**  

    data?: {
            [key: string]: string;
        };

## AndroidConfig.directBootOk

A boolean indicating whether messages will be allowed to be delivered to the app while the device is in direct boot mode.

**Signature:**  

    directBootOk?: boolean;

## AndroidConfig.fcmOptions

Options for features provided by the FCM SDK for Android.

**Signature:**  

    fcmOptions?: AndroidFcmOptions;

## AndroidConfig.notification

Android notification to be included in the message.

**Signature:**  

    notification?: AndroidNotification;

## AndroidConfig.priority

Priority of the message. Must be either `normal` or `high`.

**Signature:**  

    priority?: ('high' | 'normal');

## AndroidConfig.restrictedPackageName

Package name of the application where the registration tokens must match in order to receive the message.

**Signature:**  

    restrictedPackageName?: string;

## AndroidConfig.ttl

Time-to-live duration of the message in milliseconds.

**Signature:**  

    ttl?: number;