# Source: https://firebase.google.com/docs/reference/functions/test/test.firestore.md.txt

# Namespace: firestore

# [test](https://firebase.google.com/docs/reference/functions/test/test).firestore

namespace static

Namespace for testing Cloud Firestore functions using the Cloud Functions for Firebase Test SDK.

## Interface

### [DocumentSnapshotOptions](https://firebase.google.com/docs/reference/functions/test/test.firestore.DocumentSnapshotOptions)

## Methods

### exampleDocumentSnapshot

static

exampleDocumentSnapshot() returns test.firestore.DocumentSnapshot

Fetch an example `Change` object of document snapshots already populated with data. Can be passed into a wrapped Firestore `onCreate` or `onDelete` function.

Returns

:   `non-null test.firestore.DocumentSnapshot`

### exampleDocumentSnapshotChange

static

exampleDocumentSnapshotChange() returns test.firestore.DocumentSnapshot

Fetch an example `Change` object of document snapshots already populated with data. Can be passed into a wrapped Firestore `onUpdate` or `onWrite` function.

Returns

:   `non-null test.firestore.DocumentSnapshot`

### makeDocumentSnapshot

static

makeDocumentSnapshot(data, refPath, options) returns test.firestore.DocumentSnapshot

Create a document snapshot for testing.

|                                                                         #### Parameter                                                                         ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| data    | Object Key-value pairs representing data in the document. Pass in `{}` to mock the snapshot of a document that doesn't exist. Value must not be null. |
| refPath | string Full path of the reference (e.g. 'users/alovelace').                                                                                           |
| options | Object Optional parameters as `DocumentSnapshotOptions`. Value may be null.                                                                           |

Returns

:   `non-null test.firestore.DocumentSnapshot`