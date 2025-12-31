# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch.md.txt

# FirebaseFirestore Framework Reference

# FIRWriteBatch


    @interface FIRWriteBatch : NSObject

A write batch is used to perform multiple writes as a single atomic unit.

A WriteBatch object can be acquired by calling `Firestore.batch()`. It provides methods for
adding writes to the write batch. None of the writes will be committed (or visible locally)
until `WriteBatch.commit()` is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you
don't need to condition your writes on read data.
- `
  ``
  ``
  `

  ### [-setData:forDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:)

  `
  `  
  Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If the document exists, this method overwrites
  the document data with the new values.  

  #### Declaration

  Objective-C  

      - (nonnull FIRWriteBatch *)setData:(nonnull NSDictionary<NSString *, id> *)data
                             forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|----------------------------------------------------------------------------|
  | ` `*data*` `     | A `Dictionary` that contains the fields and data to write to the document. |
  | ` `*document*` ` | A reference to the document whose data should be overwritten.              |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-setData:forDocument:merge:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:merge:)

  `
  `  
  Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If you pass `merge:true`, the provided data will
  be merged into any existing document.  

  #### Declaration

  Objective-C  

      - (nonnull FIRWriteBatch *)setData:(nonnull NSDictionary<NSString *, id> *)data
                             forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document
                                   merge:(BOOL)merge;

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `     | A `Dictionary` that contains the fields and data to write to the document.                                                                                                                            |
  | ` `*document*` ` | A reference to the document whose data should be overwritten.                                                                                                                                         |
  | ` `*merge*` `    | Whether to merge the provided data into any existing document. If enabled, all omitted fields remain untouched. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-setData:forDocument:mergeFields:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)setData:forDocument:mergeFields:)

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

      - (nonnull FIRWriteBatch *)setData:(nonnull NSDictionary<NSString *, id> *)data
                             forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document
                             mergeFields:(nonnull NSArray<id> *)mergeFields;

  #### Parameters

  |---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `        | A `Dictionary` that contains the fields and data to write to the document.                                                                                                                                                                                          |
  | ` `*document*` `    | A reference to the document whose data should be overwritten.                                                                                                                                                                                                       |
  | ` `*mergeFields*` ` | An `Array` that contains a list of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-updateData:forDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)updateData:forDocument:)

  `
  `  
  Updates fields in the document referred to by `document`.
  If document does not exist, the write batch will fail.  

  #### Declaration

  Objective-C  

      - (nonnull FIRWriteBatch *)updateData:(nonnull NSDictionary<id, id> *)fields
                                forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` `   | A `Dictionary` containing the fields (expressed as an `String` or `FieldPath`) and values with which to update the document. |
  | ` `*document*` ` | A reference to the document whose data should be updated.                                                                    |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-deleteDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)deleteDocument:)

  `
  `  
  Deletes the document referred to by `document`.  

  #### Declaration

  Objective-C  

      - (nonnull FIRWriteBatch *)deleteDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|-----------------------------------------------------|
  | ` `*document*` ` | A reference to the document that should be deleted. |

  #### Return Value

  This `WriteBatch` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-commit](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)commit)

  `
  `  
  Commits all of the writes in this write batch as a single atomic unit.  

  #### Declaration

  Objective-C  

      - (void)commit;

- `
  ``
  ``
  `

  ### [-commitWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch#/c:objc(cs)FIRWriteBatch(im)commitWithCompletion:)

  `
  `  
  Commits all of the writes in this write batch as a single atomic unit.  

  #### Declaration

  Objective-C  

      - (void)commitWithCompletion:(nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to be called once all of the writes in the batch have been successfully written to the backend as an atomic unit. This block will only execute when the client is online and the commit has completed against the server. The completion handler will not be called when the device is offline, though local changes will be visible immediately. |