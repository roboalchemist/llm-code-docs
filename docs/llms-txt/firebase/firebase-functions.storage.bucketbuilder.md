# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.storage.bucketbuilder.md.txt

# storage.BucketBuilder class

The Google Cloud Storage bucket builder interface.

Access via `functions.storage.bucket()`.

**Signature:**  

    export declare class BucketBuilder 

## Methods

|                                                                 Method                                                                  | Modifiers |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------|
| [object()](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.bucketbuilder.md#storagebucketbuilderobject) |           | Event handler which fires every time a Google Cloud Storage change occurs. |

## storage.BucketBuilder.object()

Event handler which fires every time a Google Cloud Storage change occurs.

**Signature:**  

    object(): ObjectBuilder;

**Returns:**

[ObjectBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectbuilder.md#storageobjectbuilder_class)

Storage object builder interface scoped to the specified storage bucket.