# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.md.txt

# FirebaseFirestore Framework Reference

# FIRDocumentReference


    @interface FIRDocumentReference : NSObject

A `DocumentReference` refers to a document location in a Firestore database and can be
used to write, read, or listen to the location. The document at the referenced location
may or may not exist. A `DocumentReference` can also be used to create a `CollectionReference` to
a subcollection.
- `
  ``
  ``
  `

  ### [documentID](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(py)documentID)

  `
  `  
  The ID of the document referred to.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSString *_Nonnull documentID;

- `
  ``
  ``
  `

  ### [parent](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(py)parent)

  `
  `  
  A reference to the collection to which this `DocumentReference` belongs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference.html *_Nonnull parent;

- `
  ``
  ``
  `

  ### [firestore](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(py)firestore)

  `
  `  
  The `Firestore` for the Firestore database (useful for performing transactions, etc.).  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore.html *_Nonnull firestore;

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(py)path)

  `
  `  
  A string representing the path of the referenced document (relative to the root of the
  database).  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSString *_Nonnull path;

- `
  ``
  ``
  `

  ### [-collectionWithPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)collectionWithPath:)

  `
  `  
  Gets a `CollectionReference` referring to the collection at the specified path, relative to this
  document.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference.html *)collectionWithPath:
          (nonnull NSString *)collectionPath;

  #### Parameters

  |------------------------|-----------------------------------------------------------------------------------------------|
  | ` `*collectionPath*` ` | The slash-separated relative path of the collection for which to get a `CollectionReference`. |

  #### Return Value

The `CollectionReference` at the specified *collectionPath*.  
[## Writing Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/Writing-Data)

- `
  ``
  ``
  `

  ### [-setData:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:)

  `
  `  
  Writes to the document referred to by `DocumentReference`. If the document doesn't yet exist,
  this method creates it and then sets the data. If the document exists, this method overwrites
  the document data with the new values.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData;

  #### Parameters

  |----------------------|----------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` that contains the fields and data to write to the document. |

- `
  ``
  ``
  `

  ### [-setData:merge:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:merge:)

  `
  `  
  Writes to the document referred to by this `DocumentReference`. If the document does not yet
  exist, it will be created. If you pass `merge:true`, the provided data will be merged into
  any existing document.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData
                merge:(BOOL)merge;

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` that contains the fields and data to write to the document.                                                                                                                            |
  | ` `*merge*` `        | Whether to merge the provided data into any existing document. If enabled, all omitted fields remain untouched. If your input sets any field to an empty dictionary, any nested field is overwritten. |

- `
  ``
  ``
  `

  ### [-setData:mergeFields:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:mergeFields:)

  `
  `  
  Writes to the document referred to by `document` and only replace the fields
  specified under `mergeFields`. Any field that is not specified in `mergeFields`
  is ignored and remains untouched. If the document doesn't yet exist,
  this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  value in the `data` dictionary.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData
          mergeFields:(nonnull NSArray<id> *)mergeFields;

  #### Parameters

  |----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                                                                                       |
  | ` `*mergeFields*` `  | An `Array` that contains a list of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |

- `
  ``
  ``
  `

  ### [-setData:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:completion:)

  `
  `  
  Overwrites the document referred to by this `DocumentReference`. If no document exists, it
  is created. If a document already exists, it is overwritten.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData
           completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                  |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [-setData:merge:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:merge:completion:)

  `
  `  
  Writes to the document referred to by this `DocumentReference`. If the document does not yet
  exist, it will be created. If you pass `merge:true`, the provided data will be merged into
  any existing document.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData
                merge:(BOOL)merge
           completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                  |
  | ` `*merge*` `        | Whether to merge the provided data into any existing document. If your input sets any field to an empty dictionary, any nested field is overwritten.                                           |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [-setData:mergeFields:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)setData:mergeFields:completion:)

  `
  `  
  Writes to the document referred to by `document` and only replace the fields
  specified under `mergeFields`. Any field that is not specified in `mergeFields`
  is ignored and remains untouched. If the document doesn't yet exist,
  this method creates it and then sets the data.

  It is an error to include a field in `mergeFields` that does not have a corresponding
  value in the `data` dictionary.  

  #### Declaration

  Objective-C  

      - (void)setData:(nonnull NSDictionary<NSString *, id> *)documentData
          mergeFields:(nonnull NSArray<id> *)mergeFields
           completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*documentData*` ` | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                                                                                       |
  | ` `*mergeFields*` `  | An `Array` that contains a list of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |
  | ` `*completion*` `   | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately.                                                                      |

- `
  ``
  ``
  `

  ### [-updateData:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)updateData:)

  `
  `  
  Updates fields in the document referred to by this `DocumentReference`.
  If the document does not exist, the update fails (specify a completion block to be notified).  

  #### Declaration

  Objective-C  

      - (void)updateData:(nonnull NSDictionary<id, id> *)fields;

  #### Parameters

  |----------------|------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` ` | A `Dictionary` containing the fields (expressed as an `String` or `FieldPath`) and values with which to update the document. |

- `
  ``
  ``
  `

  ### [-updateData:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)updateData:completion:)

  `
  `  
  Updates fields in the document referred to by this `DocumentReference`. If the document
  does not exist, the update fails and the specified completion block receives an error.  

  #### Declaration

  Objective-C  

      - (void)updateData:(nonnull NSDictionary<id, id> *)fields
              completion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` `     | A `Dictionary` containing the fields (expressed as a `String` or `FieldPath`) and values with which to update the document.                                                                                                                                                                                                                                                                                 |
  | ` `*completion*` ` | A block to execute when the update is complete. If the update is successful the error parameter will be nil, otherwise it will give an indication of how the update failed. This block will only execute when the client is online and the commit has completed against the server. The completion handler will not be called when the device is offline, though local changes will be visible immediately. |

- `
  ``
  ``
  `

  ### [-deleteDocument](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)deleteDocument)

  `
  `  
  Deletes the document referred to by this `DocumentReference`.  

  #### Declaration

  Objective-C  

      - (void)deleteDocument;

- `
  ``
  ``
  `

  ### [-deleteDocumentWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)deleteDocumentWithCompletion:)

  `
  `  
  Deletes the document referred to by this `DocumentReference`.  

  #### Declaration

  Objective-C  

      - (void)deleteDocumentWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to execute once the document has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |

[## Retrieving Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/Retrieving-Data)

- `
  ``
  ``
  `

  ### [-getDocumentWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)getDocumentWithCompletion:)

  `
  `  
  Reads the document referenced by this `DocumentReference`.

  This method attempts to provide up-to-date data when possible by waiting for
  data from the server, but it may return cached data or fail if you are
  offline and the server cannot be reached. See the
  `getDocument(source:completion:)` method to change this behavior.  

  #### Declaration

  Objective-C  

      - (void)getDocumentWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable,
                            NSError *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------|
  | ` `*completion*` ` | a block to execute once the document has been successfully read. |

- `
  ``
  ``
  `

  ### [-getDocumentWithSource:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)getDocumentWithSource:completion:)

  `
  `  
  Reads the document referenced by this `DocumentReference`.  

  #### Declaration

  Objective-C  

      - (void)getDocumentWithSource:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource.html)source
                         completion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable,
                                                      NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*source*` `     | indicates whether the results should be fetched from the cache only (`Source.cache`), the server only (`Source.server`), or to attempt the server and fall back to the cache (`Source.default`). |
  | ` `*completion*` ` | a block to execute once the document has been successfully read.                                                                                                                                 |

- `
  ``
  ``
  `

  ### [-addSnapshotListener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListener:)

  `
  `  
  Attaches a listener for `DocumentSnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)addSnapshotListener:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable,
                            NSError *_Nullable))listener;

  #### Parameters

  |------------------|-------------------------|
  | ` `*listener*` ` | The listener to attach. |

  #### Return Value

  A `ListenerRegistration` that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [-addSnapshotListenerWithIncludeMetadataChanges:listener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListenerWithIncludeMetadataChanges:listener:)

  `
  `  
  Attaches a listener for `DocumentSnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
          addSnapshotListenerWithIncludeMetadataChanges:(BOOL)includeMetadataChanges
                                               listener:
                                                   (nonnull void (^)(
                                                       https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable,
                                                       NSError *_Nullable))listener;

  #### Parameters

  |--------------------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*includeMetadataChanges*` ` | Whether metadata-only changes (i.e. only `DocumentSnapshot.metadata` changed) should trigger snapshot events. |
  | ` `*listener*` `               | The listener to attach.                                                                                       |

  #### Return Value

  A `ListenerRegistration` that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [-addSnapshotListenerWithOptions:listener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference#/c:objc(cs)FIRDocumentReference(im)addSnapshotListenerWithOptions:listener:)

  `
  `  
  Attaches a listener for `DocumentSnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
          addSnapshotListenerWithOptions:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions.html *)options
                                listener:
                                    (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable,
                                                      NSError *_Nullable))listener;

  #### Parameters

  |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*options*` `  | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
  | ` `*listener*` ` | The listener to attach.                                                                                                                                                                                              |

  #### Return Value

  A `ListenerRegistration` that can be used to remove this listener.