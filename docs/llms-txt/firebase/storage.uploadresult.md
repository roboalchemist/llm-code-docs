# Source: https://firebase.google.com/docs/reference/js/storage.uploadresult.md.txt

# UploadResult interface

Result returned from a non-resumable upload.

**Signature:**  

    export interface UploadResult 

## Properties

|                                                Property                                                |                                                           Type                                                           |                   Description                    |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [metadata](https://firebase.google.com/docs/reference/js/storage.uploadresult.md#uploadresultmetadata) | [FullMetadata](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadata_interface)             | Contains the metadata sent back from the server. |
| [ref](https://firebase.google.com/docs/reference/js/storage.uploadresult.md#uploadresultref)           | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | The reference that spawned this upload.          |

## UploadResult.metadata

Contains the metadata sent back from the server.

**Signature:**  

    readonly metadata: FullMetadata;

## UploadResult.ref

The reference that spawned this upload.

**Signature:**  

    readonly ref: StorageReference;