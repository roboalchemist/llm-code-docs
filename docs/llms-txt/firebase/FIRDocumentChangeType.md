# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType.md.txt

# FirebaseFirestore Framework Reference

# FIRDocumentChangeType

    enum FIRDocumentChangeType : NSInteger {}

An enumeration of document change types.
- `
  ``
  ``
  `

  ### [FIRDocumentChangeTypeAdded](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeAdded)

  `
  `  
  Indicates a new document was added to the set of documents matching the query.  

  #### Declaration

  Objective-C  

      FIRDocumentChangeTypeAdded

- `
  ``
  ``
  `

  ### [FIRDocumentChangeTypeModified](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeModified)

  `
  `  
  Indicates a document within the query was modified.  

  #### Declaration

  Objective-C  

      FIRDocumentChangeTypeModified

- `
  ``
  ``
  `

  ### [FIRDocumentChangeTypeRemoved](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeRemoved)

  `
  `  
  Indicates a document within the query was removed (either deleted or no longer matches
  the query.  

  #### Declaration

  Objective-C  

      FIRDocumentChangeTypeRemoved