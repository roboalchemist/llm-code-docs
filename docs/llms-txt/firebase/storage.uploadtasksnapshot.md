# Source: https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md.txt

# UploadTaskSnapshot interface

Holds data about the current state of the upload task.

**Signature:**  

    export interface UploadTaskSnapshot 

## Properties

|                                                              Property                                                              |                                                           Type                                                           |                                                                     Description                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [bytesTransferred](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshotbytestransferred) | number                                                                                                                   | The number of bytes that have been successfully uploaded so far.                                                                                    |
| [metadata](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshotmetadata)                 | [FullMetadata](https://firebase.google.com/docs/reference/js/storage.fullmetadata.md#fullmetadata_interface)             | Before the upload completes, contains the metadata sent to the server. After the upload completes, contains the metadata sent back from the server. |
| [ref](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshotref)                           | [StorageReference](https://firebase.google.com/docs/reference/js/storage.storagereference.md#storagereference_interface) | The reference that spawned this snapshot's upload task.                                                                                             |
| [state](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshotstate)                       | [TaskState](https://firebase.google.com/docs/reference/js/storage.md#taskstate)                                          | The current state of the task.                                                                                                                      |
| [task](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshottask)                         | [UploadTask](https://firebase.google.com/docs/reference/js/storage.uploadtask.md#uploadtask_interface)                   | The task of which this is a snapshot.                                                                                                               |
| [totalBytes](https://firebase.google.com/docs/reference/js/storage.uploadtasksnapshot.md#uploadtasksnapshottotalbytes)             | number                                                                                                                   | The total number of bytes to be uploaded.                                                                                                           |

## UploadTaskSnapshot.bytesTransferred

The number of bytes that have been successfully uploaded so far.

**Signature:**  

    bytesTransferred: number;

## UploadTaskSnapshot.metadata

Before the upload completes, contains the metadata sent to the server. After the upload completes, contains the metadata sent back from the server.

**Signature:**  

    metadata: FullMetadata;

## UploadTaskSnapshot.ref

The reference that spawned this snapshot's upload task.

**Signature:**  

    ref: StorageReference;

## UploadTaskSnapshot.state

The current state of the task.

**Signature:**  

    state: TaskState;

## UploadTaskSnapshot.task

The task of which this is a snapshot.

**Signature:**  

    task: UploadTask;

## UploadTaskSnapshot.totalBytes

The total number of bytes to be uploaded.

**Signature:**  

    totalBytes: number;