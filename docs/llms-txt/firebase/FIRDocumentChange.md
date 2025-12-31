# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange.md.txt

# FirebaseFirestore Framework Reference

# FIRDocumentChange


    @interface FIRDocumentChange : NSObject

A `DocumentChange` represents a change to the documents matching a query. It contains the
document affected and the type of change that occurred (added, modified, or removed).
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange#/c:objc(cs)FIRDocumentChange(py)type)

  `
  `  
  The type of change that occurred (added, modified, or removed).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType.html type;

- `
  ``
  ``
  `

  ### [document](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange#/c:objc(cs)FIRDocumentChange(py)document)

  `
  `  
  The document affected by this change.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot.html *_Nonnull document;

- `
  ``
  ``
  `

  ### [oldIndex](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange#/c:objc(cs)FIRDocumentChange(py)oldIndex)

  `
  `  
  The index of the changed document in the result set immediately prior to this `DocumentChange`
  (i.e. supposing that all prior `DocumentChange` objects have been applied). `NSNotFound` for
  `DocumentChangeTypeAdded` events.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSUInteger oldIndex;

- `
  ``
  ``
  `

  ### [newIndex](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange#/c:objc(cs)FIRDocumentChange(py)newIndex)

  `
  `  
  The index of the changed document in the result set immediately after this `DocumentChange`
  (i.e. supposing that all prior `DocumentChange` objects and the current `DocumentChange` object
  have been applied). `NSNotFound` for `DocumentChangeTypeRemoved` events.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSUInteger newIndex;