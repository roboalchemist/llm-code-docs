# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/WriteBatch.md.txt

# FirebaseFirestoreSwift Framework Reference

# WriteBatch

    public extension WriteBatch

- `


  ### [setData(from:forDocument:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/WriteBatch#/s:So13FIRWriteBatchC22FirebaseFirestoreSwiftE7setData4from11forDocument7encoderABx_So20FIRDocumentReferenceCSo12FIRFirestoreCACE7EncoderVtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by `doc`. If no document exists,
  it is created. If a document already exists, it is overwritten.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: DocumentReference,
                                 encoder: Firestore.Encoder = Firestore
                                   .Encoder()) throws -> WriteBatch

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` encoder ` | The encoder instance to use to run the encoding. |
  | ` doc ` | The document to create/overwrite the encoded data to. |

  #### Return Value

  This instance of `WriteBatch`. Used for chaining method calls.
- `


  ### [setData(from:forDocument:merge:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/WriteBatch#/s:So13FIRWriteBatchC22FirebaseFirestoreSwiftE7setData4from11forDocument5merge7encoderABx_So20FIRDocumentReferenceCSbSo12FIRFirestoreCACE7EncoderVtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by `doc`. If no document exists,
  it is created. If a document already exists, it is overwritten. If you pass
  merge:true, the provided `Encodable` will be merged into any existing document.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: DocumentReference,
                                 merge: Bool,
                                 encoder: Firestore.Encoder = Firestore
                                   .Encoder()) throws -> WriteBatch

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` doc ` | The document to create/overwrite the encoded data to. |
  | ` merge ` | Whether to merge the provided `Encodable` into any existing document. |
  | ` encoder ` | The encoder instance to use to run the encoding. |

  #### Return Value

  This instance of `WriteBatch`. Used for chaining method calls.
- `


  ### [setData(from:forDocument:mergeFields:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/WriteBatch#/s:So13FIRWriteBatchC22FirebaseFirestoreSwiftE7setData4from11forDocument11mergeFields7encoderABx_So20FIRDocumentReferenceCSayypGSo12FIRFirestoreCACE7EncoderVtKSERzlF)


  ` Encodes an instance of `Encodable` and writes the encoded data to the document referred
  by `doc` by only replacing the fields specified under `mergeFields`.
  Any field that is not specified in mergeFields is ignored and remains untouched. If the
  document doesn't yet exist, this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  field in the `Encodable`.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: DocumentReference,
                                 mergeFields: [Any],
                                 encoder: Firestore.Encoder = Firestore
                                   .Encoder()) throws -> WriteBatch

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` doc ` | The document to create/overwrite the encoded data to. |
  | ` mergeFields ` | Array of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. |
  | ` encoder ` | The encoder instance to use to run the encoding. |

  #### Return Value

  This instance of `WriteBatch`. Used for chaining method calls.