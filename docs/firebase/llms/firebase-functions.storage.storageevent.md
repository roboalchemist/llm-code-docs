# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md.txt

# storage.StorageEvent interface

A CloudEvent that contains StorageObjectData

**Signature:**  

    export interface StorageEvent extends CloudEvent<StorageObjectData> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[StorageObjectData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdata_interface)\>

## Properties

|                                                                     Property                                                                     |  Type  |                  Description                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------|
| [bucket](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageeventbucket) | string | The name of the bucket containing this object. |

## storage.StorageEvent.bucket

The name of the bucket containing this object.

**Signature:**  

    bucket: string;