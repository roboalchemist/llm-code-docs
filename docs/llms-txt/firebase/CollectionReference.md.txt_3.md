# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/CollectionReference.md.txt

# FirebaseFirestoreSwift Framework Reference

# CollectionReference

    public extension CollectionReference

- `


  ### [addDocument(data:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/CollectionReference#/s:So22FIRCollectionReferenceC22FirebaseFirestoreSwiftE11addDocument4dataSo011FIRDocumentB0CSDySSypG_tYaKF)


  ` Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.
  Throws
  `Error` if the backend rejected the write.

  #### Declaration

  Swift

      func addDocument(data: [String : Any]) async throws -> DocumentReference

  #### Parameters

  |---|---|
  | ` data ` | A `Dictionary` containing the data for the new document. |

  #### Return Value

  A `DocumentReference` pointing to the newly created document.
- `


  ### [addDocument(from:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/CollectionReference#/s:So22FIRCollectionReferenceC22FirebaseFirestoreSwiftE11addDocument4from7encoder10completionSo011FIRDocumentB0Cx_So12FIRFirestoreCACE7EncoderVys5Error_pSgcSgtKSERzlF)


  ` Encodes an instance of `Encodable` and adds a new document to this collection
  with the encoded data, assigning it a document ID automatically.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      func addDocument<T: Encodable>(from value: T,
                                     encoder: Firestore.Encoder = Firestore.Encoder(),
                                     completion: ((Error?) -> Void)? = nil) throws
        -> DocumentReference

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` encoder ` | An encoder instance to use to run the encoding. |
  | ` completion ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

  #### Return Value

  A `DocumentReference` pointing to the newly created document.