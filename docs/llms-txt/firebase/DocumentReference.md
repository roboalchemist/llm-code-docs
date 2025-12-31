# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.md.txt

# FirebaseFirestore Framework Reference

# DocumentReference

    class DocumentReference : NSObject, @unchecked Sendable

A `DocumentReference` refers to a document location in a Firestore database and can be
used to write, read, or listen to the location. The document at the referenced location
may or may not exist. A `DocumentReference` can also be used to create a [CollectionReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html) to
a subcollection.
- `
  ``
  ``
  `

  ### [documentID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(py)documentID)

  `
  `  
  The ID of the document referred to.  

  #### Declaration

  Swift  

      var documentID: String { get }

- `
  ``
  ``
  `

  ### [parent](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(py)parent)

  `
  `  
  A reference to the collection to which this `DocumentReference` belongs.  

  #### Declaration

  Swift  

      var parent: FIRCollectionReference { get }

- `
  ``
  ``
  `

  ### [firestore](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(py)firestore)

  `
  `  
  The [Firestore](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html) for the Firestore database (useful for performing transactions, etc.).  

  #### Declaration

  Swift  

      var firestore: FIRFirestore { get }

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(py)path)

  `
  `  
  A string representing the path of the referenced document (relative to the root of the
  database).  

  #### Declaration

  Swift  

      var path: String { get }

- `
  ``
  ``
  `

  ### [collection(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)collectionWithPath:)

  `
  `  
  Gets a [CollectionReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html) referring to the collection at the specified path, relative to this
  document.  

  #### Declaration

  Swift  

      func collection(_ collectionPath: String) -> FIRCollectionReference

  #### Parameters

  |------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*collectionPath*` ` | The slash-separated relative path of the collection for which to get a [CollectionReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html). |

  #### Return Value

The [CollectionReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html) at the specified *collectionPath*.  
[## Writing Data](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/Writing-Data)

- `
  ``
  ``
  `

  ### [setData(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:)

  `
  `  
  Writes to the document referred to by `DocumentReference`. If the document doesn't yet exist,
  this method creates it and then sets the data. If the document exists, this method overwrites
  the document data with the new values.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any])

  #### Parameters

  |----------------------|----------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` that contains the fields and data to write to the document. |

- `
  ``
  ``
  `

  ### [setData(_:merge:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:merge:)

  `
  `  
  Writes to the document referred to by this `DocumentReference`. If the document does not yet
  exist, it will be created. If you pass `merge:true`, the provided data will be merged into
  any existing document.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any], merge: Bool)

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` that contains the fields and data to write to the document.                                                                                                                            |
  | ` `*merge*` `        | Whether to merge the provided data into any existing document. If enabled, all omitted fields remain untouched. If your input sets any field to an empty dictionary, any nested field is overwritten. |

- `
  ``
  ``
  `

  ### [setData(_:mergeFields:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:mergeFields:)

  `
  `  
  Writes to the document referred to by `document` and only replace the fields
  specified under `mergeFields`. Any field that is not specified in `mergeFields`
  is ignored and remains untouched. If the document doesn't yet exist,
  this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  value in the `data` dictionary.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any], mergeFields: [Any])

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                                                                                                                                                                                                |
  | ` `*mergeFields*` `  | An `Array` that contains a list of `String` or [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html) elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |

- `
  ``
  ``
  `

  ### [setData(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:completion:)

  `
  `  
  Overwrites the document referred to by this `DocumentReference`. If no document exists, it
  is created. If a document already exists, it is overwritten.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any]) async throws

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                  |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [setData(_:merge:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:merge:completion:)

  `
  `  
  Writes to the document referred to by this `DocumentReference`. If the document does not yet
  exist, it will be created. If you pass `merge:true`, the provided data will be merged into
  any existing document.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any], merge: Bool) async throws

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                  |
  | ` `*merge*` `        | Whether to merge the provided data into any existing document. If your input sets any field to an empty dictionary, any nested field is overwritten.                                           |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [setData(_:mergeFields:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:mergeFields:completion:)

  `
  `  
  Writes to the document referred to by `document` and only replace the fields
  specified under `mergeFields`. Any field that is not specified in `mergeFields`
  is ignored and remains untouched. If the document doesn't yet exist,
  this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  value in the `data` dictionary.  

  #### Declaration

  Swift  

      func setData(_ documentData: [String : Any], mergeFields: [Any]) async throws

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                                                                                                                                                                                                |
  | ` `*mergeFields*` `  | An `Array` that contains a list of `String` or [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html) elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately.                                                                                                                                                                               |

- `
  ``
  ``
  `

  ### [updateData(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)updateData:)

  `
  `  
  Updates fields in the document referred to by this `DocumentReference`.
  If the document does not exist, the update fails (specify a completion block to be notified).  

  #### Declaration

  Swift  

      func updateData(_ fields: [AnyHashable : Any])

  #### Parameters

  |----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` ` | A `Dictionary` containing the fields (expressed as an `String` or [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html)) and values with which to update the document. |

- `
  ``
  ``
  `

  ### [updateData(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)updateData:completion:)

  `
  `  
  Updates fields in the document referred to by this `DocumentReference`. If the document
  does not exist, the update fails and the specified completion block receives an error.  

  #### Declaration

  Swift  

      func updateData(_ fields: [AnyHashable : Any]) async throws

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` `     | A `Dictionary` containing the fields (expressed as a `String` or [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html)) and values with which to update the document.                                                                                                                                                                        |
  | ` `*completion*` ` | A block to execute when the update is complete. If the update is successful the error parameter will be nil, otherwise it will give an indication of how the update failed. This block will only execute when the client is online and the commit has completed against the server. The completion handler will not be called when the device is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [delete()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)deleteDocument)

  `
  `  
  Deletes the document referred to by this `DocumentReference`.  

  #### Declaration

  Swift  

      func delete()

- `
  ``
  ``
  `

  ### [delete()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)deleteDocumentWithCompletion:)

  `
  `  
  Deletes the document referred to by this `DocumentReference`.  

  #### Declaration

  Swift  

      func delete() async throws

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

[## Retrieving Data](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/Retrieving-Data)

- `
  ``
  ``
  `

  ### [getDocument()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)getDocumentWithCompletion:)

  `
  `  
  Reads the document referenced by this `DocumentReference`.

  This method attempts to provide up-to-date data when possible by waiting for
  data from the server, but it may return cached data or fail if you are
  offline and the server cannot be reached. See the
  `getDocument(source:completion:)` method to change this behavior.  

  #### Declaration

  Swift  

      func getDocument() async throws -> FIRDocumentSnapshot

  #### Parameters

  |--------------------|------------------------------------------------------------------|
  | ` `*completion*` ` | a block to execute once the document has been successfully read. |

- `
  ``
  ``
  `

  ### [getDocument(source:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)getDocumentWithSource:completion:)

  `
  `  
  Reads the document referenced by this `DocumentReference`.  

  #### Declaration

  Swift  

      func getDocument(source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource.html) async throws -> FIRDocumentSnapshot

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*source*` `     | indicates whether the results should be fetched from the cache only (`Source.cache`), the server only (`Source.server`), or to attempt the server and fall back to the cache (`Source.default`). |
  | ` `*completion*` ` | a block to execute once the document has been successfully read.                                                                                                                                 |

- `
  ``
  ``
  `

  ### [addSnapshotListener(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListener:)

  `
  `  
  Attaches a listener for [DocumentSnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html) events.  

  #### Declaration

  Swift  

      func addSnapshotListener(_ listener: @escaping (FIRDocumentSnapshot?, (any Error)?) -> Void) -> any https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html

  #### Parameters

  |------------------|-------------------------|
  | ` `*listener*` ` | The listener to attach. |

  #### Return Value

  A [ListenerRegistration](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html) that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [addSnapshotListener(includeMetadataChanges:listener:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListenerWithIncludeMetadataChanges:listener:)

  `
  `  
  Attaches a listener for [DocumentSnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html) events.  

  #### Declaration

  Swift  

      func addSnapshotListener(includeMetadataChanges: Bool, listener: @escaping (FIRDocumentSnapshot?, (any Error)?) -> Void) -> any https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html

  #### Parameters

  |--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*includeMetadataChanges*` ` | Whether metadata-only changes (i.e. only [DocumentSnapshot.metadata](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html#/c:objc(cs)FIRDocumentSnapshot(py)metadata) changed) should trigger snapshot events. |
  | ` `*listener*` `               | The listener to attach.                                                                                                                                                                                                                                                  |

  #### Return Value

  A [ListenerRegistration](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html) that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [addSnapshotListener(options:listener:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListenerWithOptions:listener:)

  `
  `  
  Attaches a listener for [DocumentSnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot.html) events.  

  #### Declaration

  Swift  

      func addSnapshotListener(options: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions.html, listener: @escaping (FIRDocumentSnapshot?, (any Error)?) -> Void) -> any https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html

  #### Parameters

  |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*options*` `  | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
  | ` `*listener*` ` | The listener to attach.                                                                                                                                                                                              |

  #### Return Value

  A [ListenerRegistration](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ListenerRegistration.html) that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:17FirebaseFirestore19DocumentIDWrappableP4wrapyxSo20FIRDocumentReferenceCKFZ)

  `
  `  

  #### Declaration

  Swift  

      public static func wrap(_ documentReference: DocumentReference) throws -> Self

- `
  ``
  ``
  `

  ### [getDocument(as:with:decoder:source:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:So20FIRDocumentReferenceC17FirebaseFirestoreE11getDocument2as4with7decoder6source10completionyxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderCSo0O6SourceVys6ResultOyxs5Error_pGctSeRzlF)

  `
  `  
  Fetches and decodes the document referenced by this `DocumentReference`.

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
                                     with serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html =
                                       .none,
                                     decoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Decoder = .init(),
                                     source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource.html = .default,
                                     completion: @escaping (Result<T, Error>) -> Void)

  #### Parameters

  |---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*as*` `                      | A `Decodable` type to convert the document fields to.                                                                                                                                            |
  | ` `*serverTimestampBehavior*` ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot.                                                                                 |
  | ` `*decoder*` `                 | The decoder to use to convert the document. Defaults to use the default decoder.                                                                                                                 |
  | ` `*source*` `                  | Indicates whether the results should be fetched from the cache only (`Source.cache`), the server only (`Source.server`), or to attempt the server and fall back to the cache (`Source.default`). |
  | ` `*completion*` `              | The closure to call when the document snapshot has been fetched and decoded.                                                                                                                     |

- `
  ``
  ``
  `

  ### [getDocument(as:with:decoder:source:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:So20FIRDocumentReferenceC17FirebaseFirestoreE11getDocument2as4with7decoder6sourcexxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderCSo0N6SourceVtYaKSeRzlF)

  `
  `  
  Fetches and decodes the document referenced by this `DocumentReference`.

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

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      func getDocument<T: Decodable>(as type: T.Type,
                                     with serverTimestampBehavior: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.html =
                                       .none,
                                     decoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Decoder = .init(),
                                     source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource.html = .default) async throws -> T

  #### Parameters

  |---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*as*` `                      | A `Decodable` type to convert the document fields to.                                                                                                                                            |
  | ` `*serverTimestampBehavior*` ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot.                                                                                 |
  | ` `*decoder*` `                 | The decoder to use to convert the document. Defaults to use the default decoder.                                                                                                                 |
  | ` `*source*` `                  | Indicates whether the results should be fetched from the cache only (`Source.cache`), the server only (`Source.server`), or to attempt the server and fall back to the cache (`Source.default`). |

  #### Return Value

  This instance of the supplied `Decodable` type `T`.
- `
  ``
  ``
  `

  ### [setData(from:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:So20FIRDocumentReferenceC17FirebaseFirestoreE7setData4from7encoder10completionyx_So12FIRFirestoreCACE7EncoderCys5Error_pSgcSgtKSERzlF)

  `
  `  
  Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by this `DocumentReference`. If no document exists,
  it is created. If a document already exists, it is overwritten.

  See [Firestore.Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html) for more details about the encoding process.  

  #### Declaration

  Swift  

      func setData<T: Encodable>(from value: T,
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `      | An instance of `Encodable` to be encoded to a document.                                                                                                                                            |
  | ` `*encoder*` `    | An encoder instance to use to run the encoding.                                                                                                                                                    |
  | ` `*completion*` ` | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [setData(from:merge:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:So20FIRDocumentReferenceC17FirebaseFirestoreE7setData4from5merge7encoder10completionyx_SbSo12FIRFirestoreCACE7EncoderCys5Error_pSgcSgtKSERzlF)

  `
  `  
  Encodes an instance of `Encodable` and overwrites the encoded data
  to the document referred by this `DocumentReference`. If no document exists,
  it is created. If a document already exists, it is overwritten. If you pass
  merge:true, the provided `Encodable` will be merged into any existing document.

  See [Firestore.Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html) for more details about the encoding process.  

  #### Declaration

  Swift  

      func setData<T: Encodable>(from value: T,
                                 merge: Bool,
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `      | An instance of `Encodable` to be encoded to a document.                                                                                                                                            |
  | ` `*merge*` `      | Whether to merge the provided `Encodable` into any existing document.                                                                                                                              |
  | ` `*encoder*` `    | An encoder instance to use to run the encoding.                                                                                                                                                    |
  | ` `*completion*` ` | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [setData(from:mergeFields:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/s:So20FIRDocumentReferenceC17FirebaseFirestoreE7setData4from11mergeFields7encoder10completionyx_SayypGSo12FIRFirestoreCACE7EncoderCys5Error_pSgcSgtKSERzlF)

  `
  `  
  Encodes an instance of `Encodable` and writes the encoded data to the document referred
  by this `DocumentReference` by only replacing the fields specified under `mergeFields`.
  Any field that is not specified in mergeFields is ignored and remains untouched. If the
  document doesn't yet exist, this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  field in the `Encodable`.

  See [Firestore.Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html) for more details about the encoding process.  

  #### Declaration

  Swift  

      func setData<T: Encodable>(from value: T,
                                 mergeFields: [Any],
                                 encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder(),
                                 completion: ((Error?) -> Void)? = nil) throws

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `       | An instance of `Encodable` to be encoded to a document.                                                                                                                                                                                                      |
  | ` `*mergeFields*` ` | Array of `String` or [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html) elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. |
  | ` `*encoder*` `     | An encoder instance to use to run the encoding.                                                                                                                                                                                                              |
  | ` `*completion*` `  | A closure to execute once the document has been successfully written to the server. This closure will not be called while the client is offline, though local changes will be visible immediately.                                                           |