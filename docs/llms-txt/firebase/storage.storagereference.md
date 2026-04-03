# Source: https://firebase.google.com/docs/reference/js/storage.storagereference.md.txt

# StorageReference interface

Represents a reference to a Google Cloud Storage object. Developers can upload, download, and delete objects, as well as get/set object metadata.

**Signature:**  

    export interface StorageReference 

## Properties

|                                                    Property                                                    |                                                               Type                                                               |                                                                            Description                                                                             |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bucket](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferencebucket)     | string                                                                                                                           | The name of the bucket containing this reference's object.                                                                                                         |
| [fullPath](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferencefullpath) | string                                                                                                                           | The full path of this object.                                                                                                                                      |
| [name](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferencename)         | string                                                                                                                           | The short name of this object, which is the last component of the full path. For example, if fullPath is 'full/path/image.png', name is 'image.png'.               |
| [parent](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferenceparent)     | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) \| null | A reference pointing to the parent location of this reference, or null if this reference is the root.                                                              |
| [root](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferenceroot)         | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)         | A reference to the root of this object's bucket.                                                                                                                   |
| [storage](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferencestorage)   | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface)            | The [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance associated with this reference. |

## Methods

|                                                      Method                                                      |                                     Description                                      |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [toString()](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereferencetostring) | Returns a gs:// URL for this object in the form `gs://<bucket>/<path>/<to>/<object>` |

## StorageReference.bucket

The name of the bucket containing this reference's object.

**Signature:**  

    bucket: string;

## StorageReference.fullPath

The full path of this object.

**Signature:**  

    fullPath: string;

## StorageReference.name

The short name of this object, which is the last component of the full path. For example, if fullPath is 'full/path/image.png', name is 'image.png'.

**Signature:**  

    name: string;

## StorageReference.parent

A reference pointing to the parent location of this reference, or null if this reference is the root.

**Signature:**  

    parent: StorageReference | null;

## StorageReference.root

A reference to the root of this object's bucket.

**Signature:**  

    root: StorageReference;

## StorageReference.storage

The [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance associated with this reference.

**Signature:**  

    storage: FirebaseStorage;

## StorageReference.toString()

Returns a gs:// URL for this object in the form `gs://<bucket>/<path>/<to>/<object>`

**Signature:**  

    toString(): string;

**Returns:**

string

The gs:// URL.