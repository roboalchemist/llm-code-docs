# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference.md.txt

# FirebaseFirestoreSwift Framework Reference

# DocumentReference

    extension DocumentReference: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable.html

- `


  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:22FirebaseFirestoreSwift19DocumentIDWrappableP4wrapyxSo20FIRDocumentReferenceCKFZ)


  `

  #### Declaration

  Swift

      public static func wrap(_ documentReference: DocumentReference) throws -> Self

- `


  ### [getDocument(as:with:decoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:So20FIRDocumentReferenceC22FirebaseFirestoreSwiftE11getDocument2as4with7decoder10completionyxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderVys6ResultOyxs5Error_pGctSeRzlF)


  ` Fetches and decodes the document referenced by this `DocumentReference`.

  This allows users to retrieve a Firestore document and have it decoded to
  an instance of caller-specified type as follows:

      ref.getDocument(as: Book.self) { result in
        do {
          let book = try result.get()
        } catch {
          // Handle error
        }
      }

  This method attempts to provide up-to-date data when possible by waiting
  for data from the server, but it may return cached data or fail if you are
  offline and the server cannot be reached. If `T` denotes an optional
  type, the method returns a successful status with a value of `nil` for
  non-existing documents.

  #### Declaration

  Swift

      func getDocument<T: Decodable>(as type: T.Type,
                                     with serverTimestampBehavior: ServerTimestampBehavior =
                                       .none,
                                     decoder: Firestore.Decoder = .init(),
                                     completion: @escaping (Result<T, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` as ` | A `Decodable` type to convert the document fields to. |
  | ` serverTimestampBehavior ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |
  | ` decoder ` | The decoder to use to convert the document. Defaults to use the default decoder. |
  | ` completion ` | The closure to call when the document snapshot has been fetched and decoded. |

- `


  ### [getDocument(as:with:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:So20FIRDocumentReferenceC22FirebaseFirestoreSwiftE11getDocument2as4with7decoderxxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderVtYaKSeRzlF)


  ` Fetches and decodes the document referenced by this `DocumentReference`.

  This allows users to retrieve a Firestore document and have it decoded
  to an instance of caller-specified type as follows:

      do {
        let book = try await ref.getDocument(as: Book.self)
      } catch {
        // Handle error
      }

  This method attempts to provide up-to-date data when possible by waiting
  for data from the server, but it may return cached data or fail if you
  are offline and the server cannot be reached. If `T` denotes
  an optional type, the method returns a successful status with a value
  of `nil` for non-existing documents.

  #### Declaration

  Swift

      @available(iOS 15, tvOS 15, macOS 12, watchOS 8, *)
      func getDocument<T: Decodable>(as type: T.Type,
                                     with serverTimestampBehavior: ServerTimestampBehavior =
                                       .none,
                                     decoder: Firestore.Decoder = .init()) async throws -> T

  #### Parameters

  |---|---|
  | ` as ` | A `Decodable` type to convert the document fields to. |
  | ` serverTimestampBehavior ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |
  | ` decoder ` | The decoder to use to convert the document. Defaults to use the default decoder. |

  #### Return Value

  This instance of the supplied `Decodable` type `T`.
- `


  ### [setData(from:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:So20FIRDocumentReferenceC22FirebaseFirestoreSwiftE7setData4from7encoder10completionyx_So12FIRFirestoreCACE7EncoderVys5Error_pSgcSgtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by this `DocumentReference`. If no document exists,
  it is created. If a document already exists, it is overwritten.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      func setData<T: Encodable>(from value: T,
                                 encoder: Firestore.Encoder = Firestore.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` encoder ` | An encoder instance to use to run the encoding. |
  | ` completion ` | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately. |

- `


  ### [setData(from:merge:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:So20FIRDocumentReferenceC22FirebaseFirestoreSwiftE7setData4from5merge7encoder10completionyx_SbSo12FIRFirestoreCACE7EncoderVys5Error_pSgcSgtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by this `DocumentReference`. If no document exists,
  it is created. If a document already exists, it is overwritten. If you pass
  merge:true, the provided `Encodable` will be merged into any existing document.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      func setData<T: Encodable>(from value: T,
                                 merge: Bool,
                                 encoder: Firestore.Encoder = Firestore.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` merge ` | Whether to merge the provided `Encodable` into any existing document. |
  | ` encoder ` | An encoder instance to use to run the encoding. |
  | ` completion ` | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately. |

- `


  ### [setData(from:mergeFields:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference#/s:So20FIRDocumentReferenceC22FirebaseFirestoreSwiftE7setData4from11mergeFields7encoder10completionyx_SayypGSo12FIRFirestoreCACE7EncoderVys5Error_pSgcSgtKSERzlF)


  ` Encodes an instance of `Encodable` and writes the encoded data to the document referred
  by this `DocumentReference` by only replacing the fields specified under `mergeFields`.
  Any field that is not specified in mergeFields is ignored and remains untouched. If the
  document doesn't yet exist, this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  field in the `Encodable`.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html` for more details about the encoding process.

  #### Declaration

  Swift

      func setData<T: Encodable>(from value: T,
                                 mergeFields: [Any],
                                 encoder: Firestore.Encoder = Firestore.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` mergeFields ` | Array of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. |
  | ` encoder ` | An encoder instance to use to run the encoding. |
  | ` completion ` | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately. |