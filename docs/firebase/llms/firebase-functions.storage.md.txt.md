# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.storage.md.txt

# storage namespace

## Functions

| Function | Description |
|---|---|
| [bucket(bucket)](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.md#storagebucket) | Registers a Cloud Function scoped to a specific storage bucket. |
| [object()](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.md#storageobject) | Registers a Cloud Function scoped to the default storage bucket for the project. |

## Classes

| Class | Description |
|---|---|
| [BucketBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.bucketbuilder.md#storagebucketbuilder_class) | The Google Cloud Storage bucket builder interface.Access via `functions.storage.bucket()`. |
| [ObjectBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilder_class) | The Google Cloud Storage object builder interface.Access via `functions.storage.object()`. |

## Interfaces

| Interface | Description |
|---|---|
| [ObjectMetadata](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata.md#storageobjectmetadata_interface) | Interface representing a Google Google Cloud Storage object metadata object. |

## storage.bucket()

Registers a Cloud Function scoped to a specific storage bucket.

**Signature:**

    export declare function bucket(bucket?: string): BucketBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| bucket | string | Name of the bucket to which this Cloud Function is scoped. |

**Returns:**

[BucketBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.bucketbuilder.md#storagebucketbuilder_class)

Storage bucket builder interface.

## storage.object()

Registers a Cloud Function scoped to the default storage bucket for the project.

**Signature:**

    export declare function object(): ObjectBuilder;

**Returns:**

[ObjectBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilder_class)

Storage object builder interface.