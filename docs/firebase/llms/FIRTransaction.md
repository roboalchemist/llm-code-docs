# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction.md.txt

# FirebaseFirestore Framework Reference

# FIRTransaction


    @interface FIRTransaction : NSObject

`Transaction` provides methods to read and write data within a transaction.  
See
`Firestore.runTransaction(_:)`
- `
  ``
  ``
  `

  ### [-setData:forDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)setData:forDocument:)

  `
  `  
  Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If the document exists, this method overwrites
  the document data with the new values.  

  #### Declaration

  Objective-C  

      - (nonnull FIRTransaction *)setData:(nonnull NSDictionary<NSString *, id> *)data
                              forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|----------------------------------------------------------------------------|
  | ` `*data*` `     | A `Dictionary` that contains the fields and data to write to the document. |
  | ` `*document*` ` | A reference to the document whose data should be overwritten.              |

  #### Return Value

  This `Transaction` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-setData:forDocument:merge:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)setData:forDocument:merge:)

  `
  `  
  Writes to the document referred to by `document`. If the document doesn't yet exist,
  this method creates it and then sets the data. If you pass `merge:true`, the provided data will
  be merged into any existing document.  

  #### Declaration

  Objective-C  

      - (nonnull FIRTransaction *)setData:(nonnull NSDictionary<NSString *, id> *)data
                              forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document
                                    merge:(BOOL)merge;

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `     | A `Dictionary` that contains the fields and data to write to the document.                                                                                                                            |
  | ` `*document*` ` | A reference to the document whose data should be overwritten.                                                                                                                                         |
  | ` `*merge*` `    | Whether to merge the provided data into any existing document. If enabled, all omitted fields remain untouched. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `Transaction` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-setData:forDocument:mergeFields:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)setData:forDocument:mergeFields:)

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

      - (nonnull FIRTransaction *)setData:(nonnull NSDictionary<NSString *, id> *)data
                              forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document
                              mergeFields:(nonnull NSArray<id> *)mergeFields;

  #### Parameters

  |---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*data*` `        | A `Dictionary` containing the fields that make up the document to be written.                                                                                                                                                                                       |
  | ` `*document*` `    | A reference to the document whose data should be overwritten.                                                                                                                                                                                                       |
  | ` `*mergeFields*` ` | An `Array` that contains a list of `String` or `FieldPath` elements specifying which fields to merge. Fields can contain dots to reference nested fields within the document. If your input sets any field to an empty dictionary, any nested field is overwritten. |

  #### Return Value

  This `Transaction` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-updateData:forDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)updateData:forDocument:)

  `
  `  
  Updates fields in the document referred to by `document`.
  If the document does not exist, the transaction will fail.  

  #### Declaration

  Objective-C  

      - (nonnull FIRTransaction *)updateData:(nonnull NSDictionary<id, id> *)fields
                                 forDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------|
  | ` `*fields*` `   | A `Dictionary` containing the fields (expressed as an `String` or `FieldPath`) and values with which to update the document. |
  | ` `*document*` ` | A reference to the document whose data should be updated.                                                                    |

  #### Return Value

  This `Transaction` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-deleteDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)deleteDocument:)

  `
  `  
  Deletes the document referred to by `document`.  

  #### Declaration

  Objective-C  

      - (nonnull FIRTransaction *)deleteDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document;

  #### Parameters

  |------------------|-----------------------------------------------------|
  | ` `*document*` ` | A reference to the document that should be deleted. |

  #### Return Value

  This `Transaction` instance. Used for chaining method calls.
- `
  ``
  ``
  `

  ### [-getDocument:error:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction#/c:objc(cs)FIRTransaction(im)getDocument:error:)

  `
  `  
  Reads the document referenced by `document`.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *_Nullable)
          getDocument:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)document
                error:(NSError *_Nullable *_Nullable)error;

  #### Parameters

  |------------------|--------------------------------------------------------|
  | ` `*document*` ` | A reference to the document to be read.                |
  | ` `*error*` `    | An out parameter to capture an error, if one occurred. |