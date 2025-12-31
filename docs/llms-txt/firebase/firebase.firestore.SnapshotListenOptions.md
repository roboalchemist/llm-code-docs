# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotListenOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions.md.txt

# SnapshotListenOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- SnapshotListenOptions

An options object that can be passed to `DocumentReference.onSnapshot()`,
`Query.onSnapshot()` and `QuerySnapshot.docChanges()` to control which
types of changes to include in the result set.

## Index

### Properties

- [includeMetadataChanges](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions#includemetadatachanges)

## Properties

### Optional includeMetadataChanges

includeMetadataChanges: boolean  
Include a change even if only the metadata of the query or of a document
changed. Default is false.