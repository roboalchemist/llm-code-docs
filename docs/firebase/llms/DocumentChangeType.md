# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType.md.txt

# FirebaseFirestore Framework Reference

# DocumentChangeType

    @frozen enum DocumentChangeType : Int, @unchecked Sendable

An enumeration of document change types.
- `
  ``
  ``
  `

  ### [added](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeAdded)

  `
  `  
  Indicates a new document was added to the set of documents matching the query.  

  #### Declaration

  Swift  

      case added = 0

- `
  ``
  ``
  `

  ### [modified](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeModified)

  `
  `  
  Indicates a document within the query was modified.  

  #### Declaration

  Swift  

      case modified = 1

- `
  ``
  ``
  `

  ### [removed](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType#/c:@E@FIRDocumentChangeType@FIRDocumentChangeTypeRemoved)

  `
  `  
  Indicates a document within the query was removed (either deleted or no longer matches
  the query.  

  #### Declaration

  Swift  

      case removed = 2