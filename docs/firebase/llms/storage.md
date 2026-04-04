# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage.md.txt

# Source: https://firebase.google.com/docs/storage.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/storage.md.txt

# Source: https://firebase.google.com/docs/reference/security/storage.md.txt

# Source: https://firebase.google.com/docs/reference/js/storage.md.txt

# Source: https://firebase.google.com/docs/storage.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/storage.md.txt

# Source: https://firebase.google.com/docs/reference/security/storage.md.txt

# Source: https://firebase.google.com/docs/reference/js/storage.md.txt

# storage package

Cloud Storage for Firebase

## Functions

|                                                                    Function                                                                     |                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [getStorage(app, bucketUrl)](https://firebase.google.com/docs/reference/js/storage.md#getstorage_25f3a57)                                       | Gets a [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance for the given Firebase app.                                                                                                                                                                                                                                                                                                                                                                                                         |
| **function(storage, ...)**                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [connectStorageEmulator(storage, host, port, options)](https://firebase.google.com/docs/reference/js/storage.md#connectstorageemulator_e9039de) | Modify this [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance to communicate with the Cloud Storage emulator.                                                                                                                                                                                                                                                                                                                                                                                |
| [ref(storage, url)](https://firebase.google.com/docs/reference/js/storage.md#ref_5672fc1)                                                       | Returns a [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) for the given url.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **function(ref, ...)**                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [deleteObject(ref)](https://firebase.google.com/docs/reference/js/storage.md#deleteobject_30df0b2)                                              | Deletes the object at this location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [getBlob(ref, maxDownloadSizeBytes)](https://firebase.google.com/docs/reference/js/storage.md#getblob_1c7a935)                                  | Downloads the data at the object's location. Returns an error if the object is not found.To use this functionality, you have to whitelist your app's origin in your Cloud Storage bucket. See also https://cloud.google.com/storage/docs/configuring-corsThis API is not available in Node.                                                                                                                                                                                                                                                                               |
| [getBytes(ref, maxDownloadSizeBytes)](https://firebase.google.com/docs/reference/js/storage.md#getbytes_1c7a935)                                | Downloads the data at the object's location. Returns an error if the object is not found.To use this functionality, you have to whitelist your app's origin in your Cloud Storage bucket. See also https://cloud.google.com/storage/docs/configuring-cors                                                                                                                                                                                                                                                                                                                 |
| [getDownloadURL(ref)](https://firebase.google.com/docs/reference/js/storage.md#getdownloadurl_30df0b2)                                          | Returns the download URL for the given [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface).                                                                                                                                                                                                                                                                                                                                                                                                          |
| [getMetadata(ref)](https://firebase.google.com/docs/reference/js/storage.md#getmetadata_30df0b2)                                                | A `Promise` that resolves with the metadata for this object. If this object doesn't exist or metadata cannot be retrieved, the promise is rejected.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [getStream(ref, maxDownloadSizeBytes)](https://firebase.google.com/docs/reference/js/storage.md#getstream_1c7a935)                              | Downloads the data at the object's location. Raises an error event if the object is not found.This API is only available in Node.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [list(ref, options)](https://firebase.google.com/docs/reference/js/storage.md#list_36af757)                                                     | List items (files) and prefixes (folders) under this storage reference.List API is only available for Firebase Rules Version 2.GCS is a key-blob store. Firebase Storage imposes the semantic of '/' delimited folder structure. Refer to GCS's List API if you want to learn more.To adhere to Firebase Rules's Semantics, Firebase Storage does not support objects whose paths end with "/" or contain two consecutive "/"s. Firebase Storage List API will filter these unsupported objects. list() may fail if there are too many unsupported objects in the bucket. |
| [listAll(ref)](https://firebase.google.com/docs/reference/js/storage.md#listall_30df0b2)                                                        | List all items (files) and prefixes (folders) under this storage reference.This is a helper method for calling list() repeatedly until there are no more results. The default pagination size is 1000.Note: The results may not be consistent if objects are changed while this operation is running.Warning: `listAll` may potentially consume too many resources if there are too many results.                                                                                                                                                                         |
| [updateMetadata(ref, metadata)](https://firebase.google.com/docs/reference/js/storage.md#updatemetadata_a634608)                                | Updates the metadata for this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [uploadBytes(ref, data, metadata)](https://firebase.google.com/docs/reference/js/storage.md#uploadbytes_02686b1)                                | Uploads data to this object's location. The upload is not resumable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [uploadBytesResumable(ref, data, metadata)](https://firebase.google.com/docs/reference/js/storage.md#uploadbytesresumable_02686b1)              | Uploads data to this object's location. The upload can be paused and resumed, and exposes progress updates.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [uploadString(ref, value, format, metadata)](https://firebase.google.com/docs/reference/js/storage.md#uploadstring_277829d)                     | Uploads a string to this object's location. The upload is not resumable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **function(storageOrRef, ...)**                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [ref(storageOrRef, path)](https://firebase.google.com/docs/reference/js/storage.md#ref_41be95d)                                                 | Returns a [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) for the given path in the default bucket.                                                                                                                                                                                                                                                                                                                                                                                              |

## Classes

|                                                  Class                                                   |                  Description                   |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [StorageError](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerror_class) | An error returned by the Firebase Storage SDK. |

## Enumerations

|                                          Enumeration                                          |                         Description                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [StorageErrorCode](https://firebase.google.com/docs/reference/js/storage.md#storageerrorcode) | Error codes that can be attached to `StorageError` objects. |

## Interfaces

|                                                           Interface                                                            |                                                                    Description                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface)          | A Firebase Storage instance.                                                                                                                      |
| [FullMetadata](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadata_interface)                   | The full set of object metadata, including read-only properties.                                                                                  |
| [ListOptions](https://firebase.google.com/docs/reference/js/storage.listoptions.md#listoptions_interface)                      | The options `list()` accepts.                                                                                                                     |
| [ListResult](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresult_interface)                         | Result returned by list().                                                                                                                        |
| [SettableMetadata](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadata_interface)       | Object metadata that can be set at any time.                                                                                                      |
| [StorageObserver](https://firebase.google.com/docs/reference/js/storage.storageobserver.md#storageobserver_interface)          | A stream observer for Firebase Storage.                                                                                                           |
| [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)       | Represents a reference to a Google Cloud Storage object. Developers can upload, download, and delete objects, as well as get/set object metadata. |
| [UploadMetadata](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadata_interface)             | Object metadata that can be set at upload.                                                                                                        |
| [UploadResult](https://firebase.google.com/docs/reference/js/storage.uploadresult.md#uploadresult_interface)                   | Result returned from a non-resumable upload.                                                                                                      |
| [UploadTask](https://firebase.google.com/docs/reference/js/storage.uploadtask.md#uploadtask_interface)                         | Represents the process of uploading an object. Allows you to monitor and manage the upload.                                                       |
| [UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshot_interface) | Holds data about the current state of the upload task.                                                                                            |

## Variables

|                                       Variable                                        |                        Description                        |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [StringFormat](https://firebase.google.com/docs/reference/js/storage.md#stringformat) | An enumeration of the possible string formats for upload. |

## Type Aliases

|                                      Type Alias                                       |                        Description                        |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [StringFormat](https://firebase.google.com/docs/reference/js/storage.md#stringformat) | An enumeration of the possible string formats for upload. |
| [TaskEvent](https://firebase.google.com/docs/reference/js/storage.md#taskevent)       | An event that is triggered on a task.                     |
| [TaskState](https://firebase.google.com/docs/reference/js/storage.md#taskstate)       | Represents the current state of a running upload.         |

## function(app, ...)

### getStorage(app, bucketUrl)

Gets a [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance for the given Firebase app.

**Signature:**  

    export declare function getStorage(app?: FirebaseApp, bucketUrl?: string): FirebaseStorage;

#### Parameters

| Parameter |                                                 Type                                                  |                                                                       Description                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | Firebase app to get [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance for. |
| bucketUrl | string                                                                                                | The gs:// url to your Firebase Storage Bucket. If not passed, uses the app's default Storage Bucket.                                                    |

**Returns:**

[FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface)

A [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance.

## function(storage, ...)

### connectStorageEmulator(storage, host, port, options)

Modify this [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance to communicate with the Cloud Storage emulator.

**Signature:**  

    export declare function connectStorageEmulator(storage: FirebaseStorage, host: string, port: number, options?: {
        mockUserToken?: EmulatorMockTokenOptions | string;
    }): void;

#### Parameters

| Parameter |                                                                   Type                                                                    |                                                            Description                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| storage   | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface)                     | The [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance |
| host      | string                                                                                                                                    | The emulator host (ex: localhost)                                                                                                  |
| port      | number                                                                                                                                    | The emulator port (ex: 5001)                                                                                                       |
| options   | { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/util.md#emulatormocktokenoptions) \| string; } | Emulator options. `options.mockUserToken` is the mock auth token to use for unit testing Security Rules.                           |

**Returns:**

void

### ref(storage, url)

Returns a [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) for the given url.

**Signature:**  

    export declare function ref(storage: FirebaseStorage, url?: string): StorageReference;

#### Parameters

| Parameter |                                                         Type                                                          |                                                           Description                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| storage   | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) instance. |
| url       | string                                                                                                                | URL. If empty, returns root reference.                                                                                          |

**Returns:**

[StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)

## function(ref, ...)

### deleteObject(ref)

Deletes the object at this location.

**Signature:**  

    export declare function deleteObject(ref: StorageReference): Promise<void>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                  Description                                                                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) for object to delete. |

**Returns:**

Promise\<void\>

A `Promise` that resolves if the deletion succeeds.

### getBlob(ref, maxDownloadSizeBytes)

Downloads the data at the object's location. Returns an error if the object is not found.

To use this functionality, you have to whitelist your app's origin in your Cloud Storage bucket. See also https://cloud.google.com/storage/docs/configuring-cors

This API is not available in Node.

**Signature:**  

    export declare function getBlob(ref: StorageReference, maxDownloadSizeBytes?: number): Promise<Blob>;

#### Parameters

|      Parameter       |                                                           Type                                                           |                      Description                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| ref                  | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | StorageReference where data should be downloaded.      |
| maxDownloadSizeBytes | number                                                                                                                   | If set, the maximum allowed size in bytes to retrieve. |

**Returns:**

Promise\<Blob\>

A Promise that resolves with a Blob containing the object's bytes

### getBytes(ref, maxDownloadSizeBytes)

Downloads the data at the object's location. Returns an error if the object is not found.

To use this functionality, you have to whitelist your app's origin in your Cloud Storage bucket. See also https://cloud.google.com/storage/docs/configuring-cors

**Signature:**  

    export declare function getBytes(ref: StorageReference, maxDownloadSizeBytes?: number): Promise<ArrayBuffer>;

#### Parameters

|      Parameter       |                                                           Type                                                           |                      Description                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| ref                  | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | StorageReference where data should be downloaded.      |
| maxDownloadSizeBytes | number                                                                                                                   | If set, the maximum allowed size in bytes to retrieve. |

**Returns:**

Promise\<ArrayBuffer\>

A Promise containing the object's bytes

### getDownloadURL(ref)

Returns the download URL for the given [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface).

**Signature:**  

    export declare function getDownloadURL(ref: StorageReference): Promise<string>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                      Description                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) to get the download URL for. |

**Returns:**

Promise\<string\>

A `Promise` that resolves with the download URL for this object.

### getMetadata(ref)

A `Promise` that resolves with the metadata for this object. If this object doesn't exist or metadata cannot be retrieved, the promise is rejected.

**Signature:**  

    export declare function getMetadata(ref: StorageReference): Promise<FullMetadata>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                  Description                                                                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) to get metadata from. |

**Returns:**

Promise\<[FullMetadata](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadata_interface)\>

### getStream(ref, maxDownloadSizeBytes)

Downloads the data at the object's location. Raises an error event if the object is not found.

This API is only available in Node.

**Signature:**  

    export declare function getStream(ref: StorageReference, maxDownloadSizeBytes?: number): ReadableStream;

#### Parameters

|      Parameter       |                                                           Type                                                           |                      Description                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| ref                  | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | StorageReference where data should be downloaded.      |
| maxDownloadSizeBytes | number                                                                                                                   | If set, the maximum allowed size in bytes to retrieve. |

**Returns:**

ReadableStream

A stream with the object's data as bytes

### list(ref, options)

List items (files) and prefixes (folders) under this storage reference.

List API is only available for Firebase Rules Version 2.

GCS is a key-blob store. Firebase Storage imposes the semantic of '/' delimited folder structure. Refer to GCS's List API if you want to learn more.

To adhere to Firebase Rules's Semantics, Firebase Storage does not support objects whose paths end with "/" or contain two consecutive "/"s. Firebase Storage List API will filter these unsupported objects. list() may fail if there are too many unsupported objects in the bucket.

**Signature:**  

    export declare function list(ref: StorageReference, options?: ListOptions): Promise<ListResult>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                Description                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) to get list from. |
| options   | [ListOptions](https://firebase.google.com/docs/reference/js/storage.listoptions.md#listoptions_interface)                | See [ListOptions](https://firebase.google.com/docs/reference/js/storage.listoptions.md#listoptions_interface) for details.                 |

**Returns:**

Promise\<[ListResult](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresult_interface)\>

A `Promise` that resolves with the items and prefixes. `prefixes` contains references to sub-folders and `items` contains references to objects in this folder. `nextPageToken` can be used to get the rest of the results.

### listAll(ref)

List all items (files) and prefixes (folders) under this storage reference.

This is a helper method for calling list() repeatedly until there are no more results. The default pagination size is 1000.
| **Note:** The results may not be consistent if objects are changed while this operation is running.
| **Warning:** `listAll` may potentially consume too many resources if there are too many results.

**Signature:**  

    export declare function listAll(ref: StorageReference): Promise<ListResult>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                Description                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) to get list from. |

**Returns:**

Promise\<[ListResult](https://firebase.google.com/docs/reference/js/storage.listresult.md#listresult_interface)\>

A `Promise` that resolves with all the items and prefixes under the current storage reference. `prefixes` contains references to sub-directories and `items` contains references to objects in this folder. `nextPageToken` is never returned.

### updateMetadata(ref, metadata)

Updates the metadata for this object.

**Signature:**  

    export declare function updateMetadata(ref: StorageReference, metadata: SettableMetadata): Promise<FullMetadata>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                       Description                                                                        |
|-----------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) to update metadata for.         |
| metadata  | [SettableMetadata](https://firebase.google.com/docs/reference/js/storage.settablemetadata.md#settablemetadata_interface) | The new metadata for the object. Only values that have been explicitly set will be changed. Explicitly setting a value to null will remove the metadata. |

**Returns:**

Promise\<[FullMetadata](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadata_interface)\>

A `Promise` that resolves with the new metadata for this object.

### uploadBytes(ref, data, metadata)

Uploads data to this object's location. The upload is not resumable.

**Signature:**  

    export declare function uploadBytes(ref: StorageReference, data: Blob | Uint8Array | ArrayBuffer, metadata?: UploadMetadata): Promise<UploadResult>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                       Description                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) where data should be uploaded. |
| data      | Blob \| Uint8Array \| ArrayBuffer                                                                                        | The data to upload.                                                                                                                                     |
| metadata  | [UploadMetadata](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadata_interface)       | Metadata for the data to upload.                                                                                                                        |

**Returns:**

Promise\<[UploadResult](https://firebase.google.com/docs/reference/js/storage.uploadresult.md#uploadresult_interface)\>

A Promise containing an UploadResult

### uploadBytesResumable(ref, data, metadata)

Uploads data to this object's location. The upload can be paused and resumed, and exposes progress updates.

**Signature:**  

    export declare function uploadBytesResumable(ref: StorageReference, data: Blob | Uint8Array | ArrayBuffer, metadata?: UploadMetadata): UploadTask;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                       Description                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) where data should be uploaded. |
| data      | Blob \| Uint8Array \| ArrayBuffer                                                                                        | The data to upload.                                                                                                                                     |
| metadata  | [UploadMetadata](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadata_interface)       | Metadata for the data to upload.                                                                                                                        |

**Returns:**

[UploadTask](https://firebase.google.com/docs/reference/js/storage.uploadtask.md#uploadtask_interface)

An UploadTask

### uploadString(ref, value, format, metadata)

Uploads a string to this object's location. The upload is not resumable.

**Signature:**  

    export declare function uploadString(ref: StorageReference, value: string, format?: StringFormat, metadata?: UploadMetadata): Promise<UploadResult>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                        Description                                                                        |
|-----------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ref       | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) where string should be uploaded. |
| value     | string                                                                                                                   | The string to upload.                                                                                                                                     |
| format    | [StringFormat](https://firebase.google.com/docs/reference/js/storage.md#stringformat)                                    | The format of the string to upload.                                                                                                                       |
| metadata  | [UploadMetadata](https://firebase.google.com/docs/reference/js/storage.uploadmetadata.md#uploadmetadata_interface)       | Metadata for the string to upload.                                                                                                                        |

**Returns:**

Promise\<[UploadResult](https://firebase.google.com/docs/reference/js/storage.uploadresult.md#uploadresult_interface)\>

A Promise containing an UploadResult

## function(storageOrRef, ...)

### ref(storageOrRef, path)

Returns a [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) for the given path in the default bucket.

**Signature:**  

    export declare function ref(storageOrRef: FirebaseStorage | StorageReference, path?: string): StorageReference;

#### Parameters

|  Parameter   |                                                                                                                       Type                                                                                                                        |                                                                                                                    Description                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| storageOrRef | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) \| [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | [FirebaseStorage](https://firebase.google.com/docs/reference/js/storage.firebasestorage.md#firebasestorage_interface) or [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface). |
| path         | string                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                    |

**Returns:**

[StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface)

## StringFormat

An enumeration of the possible string formats for upload.

**Signature:**  

    StringFormat: {
        readonly RAW: "raw";
        readonly BASE64: "base64";
        readonly BASE64URL: "base64url";
        readonly DATA_URL: "data_url";
    }

## StringFormat

An enumeration of the possible string formats for upload.

**Signature:**  

    export type StringFormat = (typeof StringFormat)[keyof typeof StringFormat];

## TaskEvent

An event that is triggered on a task.

**Signature:**  

    export type TaskEvent = 'state_changed';

## TaskState

Represents the current state of a running upload.

**Signature:**  

    export type TaskState = 'running' | 'paused' | 'success' | 'canceled' | 'error';

## StorageErrorCode

Error codes that can be attached to `StorageError` objects.

**Signature:**  

    export declare enum StorageErrorCode 

## Enumeration Members

|         Member          |            Value            | Description |
|-------------------------|-----------------------------|-------------|
| APP_DELETED             | `"app-deleted"`             |             |
| BUCKET_NOT_FOUND        | `"bucket-not-found"`        |             |
| CANCELED                | `"canceled"`                |             |
| CANNOT_SLICE_BLOB       | `"cannot-slice-blob"`       |             |
| INTERNAL_ERROR          | `"internal-error"`          |             |
| INVALID_ARGUMENT        | `"invalid-argument"`        |             |
| INVALID_ARGUMENT_COUNT  | `"invalid-argument-count"`  |             |
| INVALID_CHECKSUM        | `"invalid-checksum"`        |             |
| INVALID_DEFAULT_BUCKET  | `"invalid-default-bucket"`  |             |
| INVALID_EVENT_NAME      | `"invalid-event-name"`      |             |
| INVALID_FORMAT          | `"invalid-format"`          |             |
| INVALID_ROOT_OPERATION  | `"invalid-root-operation"`  |             |
| INVALID_URL             | `"invalid-url"`             |             |
| NO_DEFAULT_BUCKET       | `"no-default-bucket"`       |             |
| NO_DOWNLOAD_URL         | `"no-download-url"`         |             |
| OBJECT_NOT_FOUND        | `"object-not-found"`        |             |
| PROJECT_NOT_FOUND       | `"project-not-found"`       |             |
| QUOTA_EXCEEDED          | `"quota-exceeded"`          |             |
| RETRY_LIMIT_EXCEEDED    | `"retry-limit-exceeded"`    |             |
| SERVER_FILE_WRONG_SIZE  | `"server-file-wrong-size"`  |             |
| UNAUTHENTICATED         | `"unauthenticated"`         |             |
| UNAUTHORIZED            | `"unauthorized"`            |             |
| UNAUTHORIZED_APP        | `"unauthorized-app"`        |             |
| UNKNOWN                 | `"unknown"`                 |             |
| UNSUPPORTED_ENVIRONMENT | `"unsupported-environment"` |             |