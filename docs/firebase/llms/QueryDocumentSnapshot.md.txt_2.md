# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QueryDocumentSnapshot.md.txt

# FirebaseFirestore Framework Reference

# QueryDocumentSnapshot

    class QueryDocumentSnapshot : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html

A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as
part of a query. The document is guaranteed to exist and its data can be extracted with the
`data` property or by using subscript syntax to access a specific field.

A `QueryDocumentSnapshot` offers the same API surface as a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html`. As
deleted documents are not returned from queries, its `exists` property will always be true and
`data()` will never return `nil`.
- `


  ### [data()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QueryDocumentSnapshot#/c:objc(cs)FIRQueryDocumentSnapshot(im)data)


  ` Retrieves all fields in the document as a `Dictionary`.

  Server-provided timestamps that have not yet been set to their final value will be returned as
  `NSNull`. You can use the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QueryDocumentSnapshot.html#/c:objc(cs)FIRQueryDocumentSnapshot(im)dataWithServerTimestampBehavior:` method to configure this behavior.

  #### Declaration

  Swift

      func data() -> [String : Any]

  #### Return Value

  A `Dictionary` containing all fields in the document.
- `


  ### [data(with:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QueryDocumentSnapshot#/c:objc(cs)FIRQueryDocumentSnapshot(im)dataWithServerTimestampBehavior:)


  ` Retrieves all fields in the document as a `Dictionary`.

  #### Declaration

  Swift

      func data(with serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html) -> [String : Any]

  #### Parameters

  |---|---|
  | ` serverTimestampBehavior ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  A `Dictionary` containing all fields in the document.