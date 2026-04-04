# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.criticalsound.md.txt

# CriticalSound interface

Represents a critical sound configuration that can be included in the `aps` dictionary of an APNs payload.

**Signature:**  

    export interface CriticalSound 

## Properties

|                                                             Property                                                              |  Type   |                                                                                 Description                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [critical](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.criticalsound.md#criticalsoundcritical) | boolean | The critical alert flag. Set to `true` to enable the critical alert.                                                                                                         |
| [name](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.criticalsound.md#criticalsoundname)         | string  | The name of a sound file in the app's main bundle or in the `Library/Sounds` folder of the app's container directory. Specify the string "default" to play the system sound. |
| [volume](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.criticalsound.md#criticalsoundvolume)     | number  | The volume for the critical alert's sound. Must be a value between 0.0 (silent) and 1.0 (full volume).                                                                       |

## CriticalSound.critical

The critical alert flag. Set to `true` to enable the critical alert.

**Signature:**  

    critical?: boolean;

## CriticalSound.name

The name of a sound file in the app's main bundle or in the `Library/Sounds` folder of the app's container directory. Specify the string "default" to play the system sound.

**Signature:**  

    name: string;

## CriticalSound.volume

The volume for the critical alert's sound. Must be a value between 0.0 (silent) and 1.0 (full volume).

**Signature:**  

    volume?: number;