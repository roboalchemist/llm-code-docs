# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md.txt

# storage.ObjectBuilder class

The Google Cloud Storage object builder interface.

Access via `functions.storage.object()`.

**Signature:**  

    export declare class ObjectBuilder 

## Methods

|                                                                               Method                                                                               | Modifiers |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [onArchive(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilderonarchive)               |           | Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.                                                                                                                             |
| [onDelete(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilderondelete)                 |           | Event handler which fires every time a Google Cloud Storage deletion occurs.Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method. |
| [onFinalize(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilderonfinalize)             |           | Event handler which fires every time a Google Cloud Storage object creation occurs.Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.                                                                                                   |
| [onMetadataUpdate(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilderonmetadataupdate) |           | Event handler which fires every time the metadata of an existing object changes.                                                                                                                                                                                                                                                                                                                   |

## storage.ObjectBuilder.onArchive()

Event handler sent only when a bucket has enabled object versioning. This event indicates that the live version of an object has become an archived version, either because it was archived or because it was overwritten by the upload of an object of the same name.

**Signature:**  

    onArchive(handler: (object: ObjectMetadata, context: EventContext) => PromiseLike<any> | any): CloudFunction<ObjectMetadata>;

### Parameters

| Parameter |                                                                                                                                                                 Type                                                                                                                                                                 |                                  Description                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| handler   | (object: [ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler which is run every time a Google Cloud Storage archival occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface)\>

A function which you can export and deploy.

## storage.ObjectBuilder.onDelete()

Event handler which fires every time a Google Cloud Storage deletion occurs.

Sent when an object has been permanently deleted. This includes objects that are overwritten or are deleted as part of the bucket's lifecycle configuration. For buckets with object versioning enabled, this is not sent when an object is archived, even if archival occurs via the `storage.objects.delete` method.

**Signature:**  

    onDelete(handler: (object: ObjectMetadata, context: EventContext) => PromiseLike<any> | any): CloudFunction<ObjectMetadata>;

### Parameters

| Parameter |                                                                                                                                                                 Type                                                                                                                                                                 |                                  Description                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| handler   | (object: [ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler which is run every time a Google Cloud Storage deletion occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface)\>

A function which you can export and deploy.

## storage.ObjectBuilder.onFinalize()

Event handler which fires every time a Google Cloud Storage object creation occurs.

Sent when a new object (or a new generation of an existing object) is successfully created in the bucket. This includes copying or rewriting an existing object. A failed upload does not trigger this event.

**Signature:**  

    onFinalize(handler: (object: ObjectMetadata, context: EventContext) => PromiseLike<any> | any): CloudFunction<ObjectMetadata>;

### Parameters

| Parameter |                                                                                                                                                                 Type                                                                                                                                                                 |                                     Description                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (object: [ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler which is run every time a Google Cloud Storage object creation occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface)\>

A function which you can export and deploy.

## storage.ObjectBuilder.onMetadataUpdate()

Event handler which fires every time the metadata of an existing object changes.

**Signature:**  

    onMetadataUpdate(handler: (object: ObjectMetadata, context: EventContext) => PromiseLike<any> | any): CloudFunction<ObjectMetadata>;

### Parameters

| Parameter |                                                                                                                                                                 Type                                                                                                                                                                 |                                     Description                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (object: [ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler which is run every time a Google Cloud Storage metadata update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface)\>

A function which you can export and deploy.