# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/CollectionReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.md.txt

# FirebaseFirestore Framework Reference

# CollectionReference

    class CollectionReference : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html, @unchecked Sendable

A `CollectionReference` object can be used for adding documents, getting document references,
and querying for documents (using the methods inherited from [Query](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html)).
- `
  ``
  ``
  `

  ### [collectionID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(py)collectionID)

  `
  `  
  ID of the referenced collection.  

  #### Declaration

  Swift  

      var collectionID: String { get }

- `
  ``
  ``
  `

  ### [parent](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(py)parent)

  `
  `  
  For subcollections, `parent` returns the containing [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html). For root collections,
  `nil` is returned.  

  #### Declaration

  Swift  

      var parent: FIRDocumentReference? { get }

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(py)path)

  `
  `  
  A string containing the slash-separated path to this this `CollectionReference` (relative to the
  root of the database).  

  #### Declaration

  Swift  

      var path: String { get }

- `
  ``
  ``
  `

  ### [document()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(im)documentWithAutoID)

  `
  `  
  Returns a [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to a new document with an auto-generated ID.  

  #### Declaration

  Swift  

      func document() -> FIRDocumentReference

  #### Return Value

  A [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to a new document with an auto-generated ID.
- `
  ``
  ``
  `

  ### [document(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(im)documentWithPath:)

  `
  `  
  Gets a [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) referring to the document at the specified path, relative to this
  collection's own path.  

  #### Declaration

  Swift  

      func document(_ documentPath: String) -> FIRDocumentReference

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentPath*` ` | The slash-separated relative path of the document for which to get a [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html). |

  #### Return Value

  The [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) for the specified document path.
- `
  ``
  ``
  `

  ### [addDocument(data:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(im)addDocumentWithData:)

  `
  `  
  Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.  

  #### Declaration

  Swift  

      func addDocument(data: [String : Any]) -> FIRDocumentReference

  #### Parameters

  |--------------|----------------------------------------------------------|
  | ` `*data*` ` | A `Dictionary` containing the data for the new document. |

  #### Return Value

  A [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to the newly created document.
- `
  ``
  ``
  `

  ### [addDocument(data:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/c:objc(cs)FIRCollectionReference(im)addDocumentWithData:completion:)

  `
  `  
  Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.  

  #### Declaration

  Swift  

      func addDocument(data: [String : Any], completion: (((any Error)?) -> Void)? = nil) -> FIRDocumentReference

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `       | A `Dictionary` containing the data for the new document.                                                                                                                                       |
  | ` `*completion*` ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

  #### Return Value

  A [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to the newly created document.
- `
  ``
  ``
  `

  ### [addDocument(data:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/s:So22FIRCollectionReferenceC17FirebaseFirestoreE11addDocument4dataSo011FIRDocumentB0CSDySSypG_tYaKF)

  `
  `  
  Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.  
  Throws
  `Error` if the backend rejected the write.  

  #### Declaration

  Swift  

      @discardableResult
      func addDocument(data: [String : Any]) async throws -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html

  #### Parameters

  |--------------|----------------------------------------------------------|
  | ` `*data*` ` | A `Dictionary` containing the data for the new document. |

  #### Return Value

  A [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to the newly created document.
- `
  ``
  ``
  `

  ### [addDocument(from:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference#/s:So22FIRCollectionReferenceC17FirebaseFirestoreE11addDocument4from7encoder10completionSo011FIRDocumentB0Cx_So12FIRFirestoreCACE7EncoderCys5Error_pSgcSgtKSERzlF)

  `
  `  
  Encodes an instance of `Encodable` and adds a new document to this collection
  with the encoded data, assigning it a document ID automatically.

  See [Firestore.Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html) for more details about the encoding process.  

  #### Declaration

  Swift  

      @discardableResult
      func addDocument<T: Encodable>(from value: T,
                                     encoder: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder = https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html.Encoder(),
                                     completion: ((Error?) -> Void)? = nil) throws
        -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `      | An instance of `Encodable` to be encoded to a document.                                                                                                                                        |
  | ` `*encoder*` `    | An encoder instance to use to run the encoding.                                                                                                                                                |
  | ` `*completion*` ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

  #### Return Value

  A [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) pointing to the newly created document.