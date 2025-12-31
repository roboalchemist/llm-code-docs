# Source: https://firebase.google.com/docs/reference/functions/test/test.firestore.DocumentSnapshotOptions.md.txt

# Interface: DocumentSnapshotOptions

# [test](https://firebase.google.com/docs/reference/functions/test/test).[firestore](https://firebase.google.com/docs/reference/functions/test/test.firestore).DocumentSnapshotOptions

interface static

Interface for defining optional parameters for creating a DocumentSnapshot.

## Properties

### createTime

nullable string

The date the document was created, formatted as a UTC string.

### firebaseApp

nullable firebase.app.App

The Firebase app that the Firestore database belongs to. You do not need to supply this parameter if you supplied Firebase config values when initializing `firebase-functions-test`.

### readTime

nullable string

The last time the document was read, formatted as a UTC string.

### updateTime

nullable string

The last update time for the document, formatted as a UTC string.