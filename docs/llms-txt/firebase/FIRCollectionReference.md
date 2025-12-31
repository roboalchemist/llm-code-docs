# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference.md.txt

# FirebaseFirestore Framework Reference

# FIRCollectionReference


    @interface FIRCollectionReference : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html

A `CollectionReference` object can be used for adding documents, getting document references,
and querying for documents (using the methods inherited from `Query`).
- `
  ``
  ``
  `

  ### [collectionID](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(py)collectionID)

  `
  `  
  ID of the referenced collection.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSString *_Nonnull collectionID;

- `
  ``
  ``
  `

  ### [parent](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(py)parent)

  `
  `  
  For subcollections, `parent` returns the containing `DocumentReference`. For root collections,
  `nil` is returned.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *parent;

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(py)path)

  `
  `  
  A string containing the slash-separated path to this this `CollectionReference` (relative to the
  root of the database).  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSString *_Nonnull path;

- `
  ``
  ``
  `

  ### [-documentWithAutoID](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(im)documentWithAutoID)

  `
  `  
  Returns a `DocumentReference` pointing to a new document with an auto-generated ID.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)documentWithAutoID;

  #### Return Value

  A `DocumentReference` pointing to a new document with an auto-generated ID.
- `
  ``
  ``
  `

  ### [-documentWithPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(im)documentWithPath:)

  `
  `  
  Gets a `DocumentReference` referring to the document at the specified path, relative to this
  collection's own path.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)documentWithPath:
          (nonnull NSString *)documentPath;

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------|
  | ` `*documentPath*` ` | The slash-separated relative path of the document for which to get a `DocumentReference`. |

  #### Return Value

  The `DocumentReference` for the specified document path.
- `
  ``
  ``
  `

  ### [-addDocumentWithData:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(im)addDocumentWithData:)

  `
  `  
  Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)addDocumentWithData:
          (nonnull NSDictionary<NSString *, id> *)data;

  #### Parameters

  |--------------|----------------------------------------------------------|
  | ` `*data*` ` | A `Dictionary` containing the data for the new document. |

  #### Return Value

  A `DocumentReference` pointing to the newly created document.
- `
  ``
  ``
  `

  ### [-addDocumentWithData:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference#/c:objc(cs)FIRCollectionReference(im)addDocumentWithData:completion:)

  `
  `  
  Adds a new document to this collection with the specified data, assigning it a document ID
  automatically.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)
          addDocumentWithData:(nonnull NSDictionary<NSString *, id> *)data
                   completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `       | A `Dictionary` containing the data for the new document.                                                                                                                                       |
  | ` `*completion*` ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

  #### Return Value

  A `DocumentReference` pointing to the newly created document.