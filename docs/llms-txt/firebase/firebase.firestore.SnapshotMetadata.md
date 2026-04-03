# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata.md.txt

# SnapshotMetadata | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- SnapshotMetadata

Metadata about a snapshot, describing the state of the snapshot.

## Index

### Properties

- [fromCache](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata#fromcache)
- [hasPendingWrites](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata#haspendingwrites)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata#isequal)

## Properties

### fromCache

fromCache: boolean  
True if the snapshot was created from cached data rather than guaranteed
up-to-date server data. If your listener has opted into metadata updates
(via `SnapshotListenOptions`)
you will receive another snapshot with `fromCache` set to false once
the client has received up-to-date data from the backend.

### hasPendingWrites

hasPendingWrites: boolean  
True if the snapshot contains the result of local writes (e.g. set() or
update() calls) that have not yet been committed to the backend.
If your listener has opted into metadata updates (via
`SnapshotListenOptions`) you will receive another
snapshot with `hasPendingWrites` equal to false once the writes have been
committed to the backend.

## Methods

### isEqual

- isEqual ( other : [SnapshotMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata) ) : boolean
- Returns true if this `SnapshotMetadata` is equal to the provided one.

  #### Parameters

  -

    ##### other: [SnapshotMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata)

    The `SnapshotMetadata` to compare against.

  #### Returns boolean

true if this `SnapshotMetadata` is equal to the provided one.