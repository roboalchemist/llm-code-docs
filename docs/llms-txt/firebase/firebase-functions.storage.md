# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.storage.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md.txt

# storage namespace

## Functions

|                                                                                  Function                                                                                  |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [onObjectArchived(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectarchived)                       | Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.                                                                                                                             |
| [onObjectArchived(bucket, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectarchived)               | Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.                                                                                                                             |
| [onObjectArchived(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectarchived)                 | Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.                                                                                                                             |
| [onObjectDeleted(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectdeleted)                         | Event handler which fires every time a Google Cloud Storage deletion occurs.Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method. |
| [onObjectDeleted(bucket, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectdeleted)                 | Event handler which fires every time a Google Cloud Storage deletion occurs.Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method. |
| [onObjectDeleted(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectdeleted)                   | Event handler which fires every time a Google Cloud Storage deletion occurs.Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method. |
| [onObjectFinalized(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectfinalized)                     | Event handler which fires every time a Google Cloud Storage object creation occurs.Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.                                                                                                   |
| [onObjectFinalized(bucket, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectfinalized)             | Event handler which fires every time a Google Cloud Storage object creation occurs.Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.                                                                                                   |
| [onObjectFinalized(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectfinalized)               | Event handler which fires every time a Google Cloud Storage object creation occurs.Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.                                                                                                   |
| [onObjectMetadataUpdated(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectmetadataupdated)         | Event handler which fires every time the metadata of an existing object changes.                                                                                                                                                                                                                                                                                                                   |
| [onObjectMetadataUpdated(bucket, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectmetadataupdated) | Event handler which fires every time the metadata of an existing object changes.                                                                                                                                                                                                                                                                                                                   |
| [onObjectMetadataUpdated(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.md#storageonobjectmetadataupdated)   | Event handler which fires every time the metadata of an existing object changes.                                                                                                                                                                                                                                                                                                                   |

## Interfaces

|                                                                                  Interface                                                                                   |                                                                     Description                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomerEncryption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.customerencryption.md#storagecustomerencryption_interface) | Metadata of customer-supplied encryption key, if the object is encrypted by such a key.                                                             |
| [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)                   | A CloudEvent that contains StorageObjectData                                                                                                        |
| [StorageObjectData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageobjectdata.md#storagestorageobjectdata_interface)    | An object within Google Cloud Storage. Ref: https://github.com/googleapis/google-cloudevents-nodejs/blob/main/cloud/storage/v1/StorageObjectData.ts |
| [StorageOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageoptions.md#storagestorageoptions_interface)             | StorageOptions extend EventHandlerOptions with a bucket name                                                                                        |

## storage.onObjectArchived()

Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.

**Signature:**  

    export declare function onObjectArchived(handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                  Description                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage archival occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectArchived()

Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.

**Signature:**  

    export declare function onObjectArchived(bucket: string | Expression<string>, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                  Description                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| bucket    | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>                            | The name of the bucket containing this object.                                |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage archival occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectArchived()

Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.

**Signature:**  

    export declare function onObjectArchived(opts: StorageOptions, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                  Description                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| opts      | [StorageOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageoptions.md#storagestorageoptions_interface)                              | Options that can be set on an individual event-handling function.             |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage archival occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectDeleted()

Event handler which fires every time a Google Cloud Storage deletion occurs.

Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method.

**Signature:**  

    export declare function onObjectDeleted(handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectDeleted()

Event handler which fires every time a Google Cloud Storage deletion occurs.

Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method.

**Signature:**  

    export declare function onObjectDeleted(bucket: string | Expression<string>, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| bucket    | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>                            | The name of the bucket containing this object.                                       |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectDeleted()

Event handler which fires every time a Google Cloud Storage deletion occurs.

Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method.

**Signature:**  

    export declare function onObjectDeleted(opts: StorageOptions, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| opts      | [StorageOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageoptions.md#storagestorageoptions_interface)                              | Options that can be set on an individual event-handling function.                    |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectFinalized()

Event handler which fires every time a Google Cloud Storage object creation occurs.

Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.

**Signature:**  

    export declare function onObjectFinalized(handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object creation occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectFinalized()

Event handler which fires every time a Google Cloud Storage object creation occurs.

Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.

**Signature:**  

    export declare function onObjectFinalized(bucket: string | Expression<string>, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| bucket    | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>                            | The name of the bucket containing this object.                                       |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object creation occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectFinalized()

Event handler which fires every time a Google Cloud Storage object creation occurs.

Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.

**Signature:**  

    export declare function onObjectFinalized(opts: StorageOptions, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                     Description                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| opts      | [StorageOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageoptions.md#storagestorageoptions_interface)                              | Options that can be set on an individual event-handling function.                    |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object creation occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectMetadataUpdated()

Event handler which fires every time the metadata of an existing object changes.

**Signature:**  

    export declare function onObjectMetadataUpdated(handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                         Description                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object metadata update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectMetadataUpdated()

Event handler which fires every time the metadata of an existing object changes.

**Signature:**  

    export declare function onObjectMetadataUpdated(bucket: string | Expression<string>, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                         Description                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| bucket    | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>                            | The name of the bucket containing this object.                                              |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object metadata update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>

## storage.onObjectMetadataUpdated()

Event handler which fires every time the metadata of an existing object changes.

**Signature:**  

    export declare function onObjectMetadataUpdated(opts: StorageOptions, handler: (event: StorageEvent) => any | Promise<any>): CloudFunction<StorageEvent>;

### Parameters

| Parameter |                                                                                             Type                                                                                              |                                         Description                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| opts      | [StorageOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageoptions.md#storagestorageoptions_interface)                              | Options that can be set on an individual event-handling function.                           |
| handler   | (event: [StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)) =\> any \| Promise\<any\> | Event handler which is run every time a Google Cloud Storage object metadata update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[StorageEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.storage.storageevent.md#storagestorageevent_interface)\>