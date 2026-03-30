# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotMetadata.md.txt

# FirebaseFirestore Framework Reference

# SnapshotMetadata

    class SnapshotMetadata : NSObject, @unchecked Sendable

Metadata about a snapshot, describing the state of the snapshot.
- `


  ### [hasPendingWrites](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotMetadata#/c:objc(cs)FIRSnapshotMetadata(py)pendingWrites)


  ` Returns `true` if the snapshot contains the result of local writes (e.g. set() or update() calls)
  that have not yet been committed to the backend. If your listener has opted into metadata updates
  (via `includeMetadataChanges:true`) you will receive another snapshot with `hasPendingWrites`
  equal to `false` once the writes have been committed to the backend.

  #### Declaration

  Swift

      var hasPendingWrites: Bool { get }

- `


  ### [isFromCache](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotMetadata#/c:objc(cs)FIRSnapshotMetadata(py)fromCache)


  ` Returns `true` if the snapshot was created from cached data rather than guaranteed up-to-date
  server data. If your listener has opted into metadata updates (via `includeMetadataChanges:true`)
  you will receive another snapshot with `isFromCache` equal to `false` once the client has
  received up-to-date data from the backend.

  #### Declaration

  Swift

      var isFromCache: Bool { get }