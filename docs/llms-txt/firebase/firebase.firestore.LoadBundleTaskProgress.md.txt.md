# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress.md.txt

# LoadBundleTaskProgress | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- LoadBundleTaskProgress

Represents a progress update or a final state from loading bundles.

## Index

### Properties

- [bytesLoaded](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress#bytesloaded)
- [documentsLoaded](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress#documentsloaded)
- [taskState](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress#taskstate)
- [totalBytes](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress#totalbytes)
- [totalDocuments](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress#totaldocuments)

## Properties

### bytesLoaded

bytesLoaded: number How many bytes have been loaded.

### documentsLoaded

documentsLoaded: number How many documents have been loaded.

### taskState

taskState: [TaskState](https://firebase.google.com/docs/reference/node/firebase.firestore#taskstate) Current task state.

### totalBytes

totalBytes: number How many bytes are in the bundle being loaded.

### totalDocuments

totalDocuments: number How many documents are in the bundle being loaded.