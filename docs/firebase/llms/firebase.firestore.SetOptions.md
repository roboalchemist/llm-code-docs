# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.SetOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions.md.txt

# SetOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- SetOptions

An options object that configures the behavior of `set()` calls in
[DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#set), [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#set) and [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#set). These calls can be
configured to perform granular merges instead of overwriting the target
documents in their entirety by providing a `SetOptions` with `merge: true`.

## Index

### Properties

- [merge](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions#merge)
- [mergeFields](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions#mergefields)

## Properties

### Optional merge

merge: boolean  
Changes the behavior of a set() call to only replace the values specified
in its data argument. Fields omitted from the set() call remain
untouched.

### Optional mergeFields

mergeFields: (string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath))\[\]  
Changes the behavior of set() calls to only replace the specified field
paths. Any field path that is not specified is ignored and remains
untouched.