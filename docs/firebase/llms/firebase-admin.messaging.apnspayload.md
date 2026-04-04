# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnspayload.md.txt

# ApnsPayload interface

Represents the payload of an APNs message. Mainly consists of the `aps` dictionary. But may also contain other arbitrary custom keys.

**Signature:**  

    export interface ApnsPayload 

## Properties

|                                                      Property                                                       |                                                    Type                                                    |                     Description                     |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [aps](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.apnspayload.md#apnspayloadaps) | [Aps](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.aps.md#aps_interface) | The `aps` dictionary to be included in the message. |

## ApnsPayload.aps

The `aps` dictionary to be included in the message.

**Signature:**  

    aps: Aps;