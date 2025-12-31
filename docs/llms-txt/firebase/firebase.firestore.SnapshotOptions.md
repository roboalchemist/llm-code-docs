# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions.md.txt

# SnapshotOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- SnapshotOptions

Options that configure how data is retrieved from a `DocumentSnapshot`
(e.g. the desired behavior for server timestamps that have not yet been set
to their final value).

## Index

### Properties

- [serverTimestamps](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions#servertimestamps)

## Properties

### Optional serverTimestamps

serverTimestamps: "estimate" \| "previous" \| "none"  
If set, controls the return value for server timestamps that have not yet
been set to their final value.

By specifying 'estimate', pending server timestamps return an estimate
based on the local clock. This estimate will differ from the final value
and cause these values to change once the server result becomes available.

By specifying 'previous', pending timestamps will be ignored and return
their previous value instead.

If omitted or set to 'none', `null` will be returned by default until the
server value becomes available.