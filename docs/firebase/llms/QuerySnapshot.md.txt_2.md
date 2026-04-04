# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot.md.txt

# FirebaseFirestore Framework Reference

# QuerySnapshot

    class QuerySnapshot : NSObject, @unchecked Sendable

A `QuerySnapshot` contains zero or more `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html` objects. It can be enumerated
using the `documents` property and its size can be inspected with `isEmpty` and
`count`.
- `


  ### [query](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)query)


  ` The query on which you called `getDocuments` or listened to in order to get this
  `QuerySnapshot`.

  #### Declaration

  Swift

      var query: FIRQuery { get }

- `


  ### [metadata](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)metadata)


  ` Metadata about this snapshot, concerning its source and if it has local modifications.

  #### Declaration

  Swift

      var metadata: FIRSnapshotMetadata { get }

- `


  ### [isEmpty](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)empty)


  ` Indicates whether this `QuerySnapshot` is empty (contains no documents).

  #### Declaration

  Swift

      var isEmpty: Bool { get }

- `


  ### [count](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)count)


  ` The count of documents in this `QuerySnapshot`.

  #### Declaration

  Swift

      var count: Int { get }

- `


  ### [documents](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)documents)


  ` An Array of the `DocumentSnapshots` that make up this document set.

  #### Declaration

  Swift

      var documents: [FIRQueryDocumentSnapshot] { get }

- `


  ### [documentChanges](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)documentChanges)


  ` An array of the documents that changed since the last snapshot. If this is the first snapshot,
  all documents will be in the list as Added changes.

  #### Declaration

  Swift

      var documentChanges: [FIRDocumentChange] { get }

- `


  ### [documentChanges(includeMetadataChanges:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot#/c:objc(cs)FIRQuerySnapshot(im)documentChangesWithIncludeMetadataChanges:)


  ` Returns an array of the documents that changed since the last snapshot. If this is the first
  snapshot, all documents will be in the list as Added changes.

  #### Declaration

  Swift

      func documentChanges(includeMetadataChanges: Bool) -> [FIRDocumentChange]

  #### Parameters

  |---|---|
  | ` includeMetadataChanges ` | Whether metadata-only changes (i.e. only `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html#/c:objc(cs)FIRDocumentSnapshot(py)metadata` changed) should be included. |