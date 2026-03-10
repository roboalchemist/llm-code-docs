# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch.md.txt

# FirebaseFirestore Framework Reference

# WriteBatch

    class WriteBatch : NSObject

A write batch is used to perform multiple writes as a single atomic unit.

A WriteBatch object can be acquired by calling `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html#/c:objc(cs)FIRFirestore(im)batch`. It provides methods for
adding writes to the write batch. None of the writes will be committed (or visible locally)
until `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch.html#/c:objc(cs)FIRWriteBatch(im)commit` is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you
don't need to condition your writes on read data.
- `


  ### [setData(_:forDocument:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:)


  ` Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If the document exists, this method overwrites
  the document data with the new values.

  #### Declaration

  Swift

      func setData(_ data: [String : Any], forDocument document: FIRDocumentReference) -> WriteBatch

  #### Parameters

  |---|---|
  | ` data ` | A `Dictionary` that contains the fields and data to write to the document. |
  | ` document ` | A reference to the document whose data should be overwritten. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `


  ### [setData(_:forDocument:merge:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:merge:)


  ` Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If you pass `merge:true`, the provided data will
  be merged into any existing document.

  #### Declaration

  Swift

      func setData(_ data: [String : Any], forDocument document: FIRDocumentReference, merge: Bool) -> WriteBatch

  #### Parameters

  |---|---|
  | ` data ` | A `Dictionary` that contains the fields and data to write to the document. |
  | ` document ` | A reference to the document whose data should be overwritten. |
  | ` merge ` | Whether to merge the provided data into any existing document. If enabled, all omitted fields remain untouched. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `


  ### [setData(_:forDocument:mergeFields:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:mergeFields:)


  ` Writes to the document referred to by `document` and only replace the fields
  specified under `mergeFields`. Any field that is not specified in `mergeFields`
  is ignored and remains untouched. If the document doesn't yet exist,
  this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  value in the `data` dictionary.

  #### Declaration

  Swift

      func setData(_ data: [String : Any], forDocument document: FIRDocumentReference, mergeFields: [Any]) -> WriteBatch

  #### Parameters

  |---|---|
  | ` data ` | A `Dictionary` that contains the fields and data to write to the document. |
  | ` document ` | A reference to the document whose data should be overwritten. |
  | ` mergeFields ` | An `Array` that contains a list of `String` or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `


  ### [updateData(_:forDocument:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)updateData:forDocument:)


  ` Updates fields in the document referred to by `document`.
  If document does not exist, the write batch will fail.

  #### Declaration

  Swift

      func updateData(_ fields: [AnyHashable : Any], forDocument document: FIRDocumentReference) -> WriteBatch

  #### Parameters

  |---|---|
  | ` fields ` | A `Dictionary` containing the fields (expressed as an `String` or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html`) and values with which to update the document. |
  | ` document ` | A reference to the document whose data should be updated. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `


  ### [deleteDocument(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)deleteDocument:)


  ` Deletes the document referred to by `document`.

  #### Declaration

  Swift

      func deleteDocument(_ document: FIRDocumentReference) -> WriteBatch

  #### Parameters

  |---|---|
  | ` document ` | A reference to the document that should be deleted. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `


  ### [commit()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)commit)


  ` Commits all of the writes in this write batch as a single atomic unit.

  #### Declaration

  Swift

      func commit()

- `


  ### [commit()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)commitWithCompletion:)


  ` Commits all of the writes in this write batch as a single atomic unit.

  #### Declaration

  Swift

      func commit() async throws

  #### Parameters

  |---|---|
  | ` completion ` | A block to be called once all of the writes in the batch have been successfully written to the backend as an atomic unit. This block will only execute when the client is online and the commit has completed against the server. The completion handler will not be called when the device is offline, though local changes will be visible immediately. |

- `


  ### [setData(from:forDocument:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/s:So13FIRWriteBatchC17FirebaseFirestoreE7setData4from11forDocument7encoderABx_So20FIRDocumentReferenceCSo12FIRFirestoreCACE7EncoderCtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by `doc`. If no document exists,
  it is created. If a document already exists, it is overwritten.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html,
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html
                                   .Encoder()) throws -> WriteBatch

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` encoder ` | The encoder instance to use to run the encoding. |
  | ` doc ` | The document to create/overwrite the encoded data to. |

  #### Return Value

  This instance of `WriteBatch`. Used for chaining method calls.
- `


  ### [setData(from:forDocument:merge:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/s:So13FIRWriteBatchC17FirebaseFirestoreE7setData4from11forDocument5merge7encoderABx_So20FIRDocumentReferenceCSbSo12FIRFirestoreCACE7EncoderCtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by `doc`. If no document exists,
  it is created. If a document already exists, it is overwritten. If you pass
  merge:true, the provided `Encodable` will be merged into any existing document.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html,
                                 merge: Bool,
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html
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


  ### [setData(from:forDocument:mergeFields:encoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/s:So13FIRWriteBatchC17FirebaseFirestoreE7setData4from11forDocument11mergeFields7encoderABx_So20FIRDocumentReferenceCSayypGSo12FIRFirestoreCACE7EncoderCtKSERzlF)


  ` Encodes an instance of `Encodable` and writes the encoded data to the document referred
  by `doc` by only replacing the fields specified under `mergeFields`.
  Any field that is not specified in mergeFields is ignored and remains untouched. If the
  document doesn't yet exist, this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  field in the `Encodable`.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      @discardableResult
      func setData<T: Encodable>(from value: T,
                                 forDocument doc: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html,
                                 mergeFields: [Any],
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html
                                   .Encoder()) throws -> WriteBatch

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` doc ` | The document to create/overwrite the encoded data to. |
  | ` mergeFields ` | Array of `String` or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. |
  | ` encoder ` | The encoder instance to use to run the encoding. |

  #### Return Value

  This instance of `WriteBatch`. Used for chaining method calls.