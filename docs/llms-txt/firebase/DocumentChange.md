# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange.md.txt

# FirebaseFirestore Framework Reference

# DocumentChange

    class DocumentChange : NSObject, @unchecked Sendable

A `DocumentChange` represents a change to the documents matching a query. It contains the
document affected and the type of change that occurred (added, modified, or removed).
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange#/c:objc(cs)FIRDocumentChange(py)type)

  `
  `  
  The type of change that occurred (added, modified, or removed).  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType.html { get }

- `
  ``
  ``
  `

  ### [document](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange#/c:objc(cs)FIRDocumentChange(py)document)

  `
  `  
  The document affected by this change.  

  #### Declaration

  Swift  

      var document: FIRQueryDocumentSnapshot { get }

- `
  ``
  ``
  `

  ### [oldIndex](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange#/c:objc(cs)FIRDocumentChange(py)oldIndex)

  `
  `  
  The index of the changed document in the result set immediately prior to this `DocumentChange`
  (i.e. supposing that all prior `DocumentChange` objects have been applied). `NSNotFound` for
  `DocumentChangeTypeAdded` events.  

  #### Declaration

  Swift  

      var oldIndex: UInt { get }

- `
  ``
  ``
  `

  ### [newIndex](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange#/c:objc(cs)FIRDocumentChange(py)newIndex)

  `
  `  
  The index of the changed document in the result set immediately after this `DocumentChange`
  (i.e. supposing that all prior `DocumentChange` objects and the current `DocumentChange` object
  have been applied). `NSNotFound` for `DocumentChangeTypeRemoved` events.  

  #### Declaration

  Swift  

      var newIndex: UInt { get }