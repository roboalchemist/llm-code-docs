# Source: https://firebase.google.com/docs/reference/node/firebase.storage.UploadTaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.UploadTaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot.md.txt

# UploadTaskSnapshot | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- UploadTaskSnapshot

Holds data about the current state of the upload task.

## Index

### Properties

- [bytesTransferred](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#bytestransferred)
- [metadata](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#metadata)
- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#ref)
- [state](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#state)
- [task](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#task)
- [totalBytes](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot#totalbytes)

## Properties

### bytesTransferred

bytesTransferred: number  
The number of bytes that have been successfully uploaded so far.

### metadata

metadata: [FullMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FullMetadata)  
Before the upload completes, contains the metadata sent to the server.
After the upload completes, contains the metadata sent back from the server.

### ref

ref: [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)  
The reference that spawned this snapshot's upload task.

### state

state: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)  
The current state of the task.

### task

task: [UploadTask](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTask)  
The task of which this is a snapshot.

### totalBytes

totalBytes: number  
The total number of bytes to be uploaded.