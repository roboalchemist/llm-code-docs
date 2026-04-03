# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.md.txt

# FirebaseFirestore Framework Reference

# FIRQuerySnapshot


    @interface FIRQuerySnapshot : NSObject

A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects. It can be enumerated
using the `documents` property and its size can be inspected with `isEmpty` and
`count`.
- `
  ``
  ``
  `

  ### [query](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)query)

  `
  `  
  The query on which you called `getDocuments` or listened to in order to get this
  `QuerySnapshot`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *_Nonnull query;

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)metadata)

  `
  `  
  Metadata about this snapshot, concerning its source and if it has local modifications.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotMetadata.html *_Nonnull metadata;

- `
  ``
  ``
  `

  ### [empty](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)empty)

  `
  `  
  Indicates whether this `QuerySnapshot` is empty (contains no documents).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, getter=isEmpty) BOOL empty;

- `
  ``
  ``
  `

  ### [count](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)count)

  `
  `  
  The count of documents in this `QuerySnapshot`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger count;

- `
  ``
  ``
  `

  ### [documents](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)documents)

  `
  `  
  An Array of the `DocumentSnapshots` that make up this document set.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot.html *> *_Nonnull documents;

- `
  ``
  ``
  `

  ### [documentChanges](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(py)documentChanges)

  `
  `  
  An array of the documents that changed since the last snapshot. If this is the first snapshot,
  all documents will be in the list as Added changes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange.html *> *_Nonnull documentChanges;

- `
  ``
  ``
  `

  ### [-documentChangesWithIncludeMetadataChanges:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot#/c:objc(cs)FIRQuerySnapshot(im)documentChangesWithIncludeMetadataChanges:)

  `
  `  
  Returns an array of the documents that changed since the last snapshot. If this is the first
  snapshot, all documents will be in the list as Added changes.  

  #### Declaration

  Objective-C  

      - (nonnull NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange.html *> *)
          documentChangesWithIncludeMetadataChanges:(BOOL)includeMetadataChanges;

  #### Parameters

  |--------------------------------|---------------------------------------------------------------------------------------------------|
  | ` `*includeMetadataChanges*` ` | Whether metadata-only changes (i.e. only `DocumentSnapshot.metadata` changed) should be included. |