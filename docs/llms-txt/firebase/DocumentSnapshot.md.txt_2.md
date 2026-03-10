# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.md.txt

# FirebaseFirestore Framework Reference

# DocumentSnapshot

    class DocumentSnapshot : NSObject, @unchecked Sendable

A `DocumentSnapshot` contains data read from a document in your Firestore database. The data
can be extracted with the `data` property or by using subscript syntax to access a specific
field.

For a `DocumentSnapshot` that points to a non-existing document, any data access will return
`nil`. You can use the `exists` property to explicitly verify a documents existence.
- `


  ### [exists](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)exists)


  ` True if the document exists.

  #### Declaration

  Swift

      var exists: Bool { get }

- `


  ### [reference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)reference)


  ` A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html` to the document location.

  #### Declaration

  Swift

      var reference: FIRDocumentReference { get }

- `


  ### [documentID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)documentID)


  ` The ID of the document for which this `DocumentSnapshot` contains data.

  #### Declaration

  Swift

      var documentID: String { get }

- `


  ### [metadata](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)metadata)


  ` Metadata about this snapshot concerning its source and if it has local modifications.

  #### Declaration

  Swift

      var metadata: FIRSnapshotMetadata { get }

- `


  ### [data()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)data)


  ` Retrieves all fields in the document as a `Dictionary`. Returns `nil` if the document doesn't
  exist.

  Server-provided timestamps that have not yet been set to their final value will be returned as
  `NSNull`. You can use the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html#/c:objc(cs)FIRDocumentSnapshot(im)dataWithServerTimestampBehavior:` method to configure this behavior.

  #### Declaration

  Swift

      func data() -> [String : Any]?

  #### Return Value

  A `Dictionary` containing all fields in the document or `nil` if the document doesn't
  exist.
- `


  ### [data(with:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)dataWithServerTimestampBehavior:)


  ` Retrieves all fields in the document as a `Dictionary`. Returns `nil` if the document doesn't
  exist.

  #### Declaration

  Swift

      func data(with serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html) -> [String : Any]?

  #### Parameters

  |---|---|
  | ` serverTimestampBehavior ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  A `Dictionary` containing all fields in the document or `nil` if the document doesn't
  exist.
- `


  ### [get(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)valueForField:)


  ` Retrieves a specific field from the document. Returns `nil` if the document or the field doesn't
  exist.

  The timestamps that have not yet been set to their final value will be returned as `NSNull`. You
  can use `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html#/c:objc(cs)FIRDocumentSnapshot(im)valueForField:serverTimestampBehavior:` to configure this behavior.

  #### Declaration

  Swift

      func get(_ field: Any) -> Any?

  #### Parameters

  |---|---|
  | ` field ` | The field to retrieve. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.
- `


  ### [get(_:serverTimestampBehavior:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)valueForField:serverTimestampBehavior:)


  ` Retrieves a specific field from the document. Returns `nil` if the document or the field doesn't
  exist.

  The timestamps that have not yet been set to their final value will be returned as `NSNull`. You
  can use `get(_:serverTimestampBehavior:)` to configure this behavior.

  #### Declaration

  Swift

      func get(_ field: Any, serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html) -> Any?

  #### Parameters

  |---|---|
  | ` field ` | The field to retrieve. |
  | ` serverTimestampBehavior ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.
- `


  ### [subscript(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)objectForKeyedSubscript:)


  ` Retrieves a specific field from the document.

  #### Declaration

  Swift

      subscript(key: Any) -> Any? { get }

  #### Parameters

  |---|---|
  | ` key ` | The field to retrieve. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.
- `


  ### [data(as:with:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot#/s:So19FIRDocumentSnapshotC17FirebaseFirestoreE4data2as4with7decoderxxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderCtKSeRzlF)


  ` Retrieves all fields in a document and converts them to an instance of
  caller-specified type.

  By default, server-provided timestamps that have not yet been set to their
  final value will be returned as `NSNull`. Pass `serverTimestampBehavior`
  to configure this behavior.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder.html` for more details about the decoding process.

  #### Declaration

  Swift

      func data<T: Decodable>(as type: T.Type,
                              with serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html = .none,
                              decoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Decoder = .init()) throws -> T