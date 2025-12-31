# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable.md.txt

# FirebaseFirestore Framework Reference

# DocumentIDWrappable

    public protocol DocumentIDWrappable

A type that can initialize itself from a Firestore [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html),
which makes it suitable for use with the [@DocumentID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID.html) property wrapper.

Firestore includes extensions that make `String` and [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html)
conform to `DocumentIDWrappable`.

Note that Firestore ignores fields annotated with [@DocumentID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID.html) when writing
so there is no requirement to convert from the wrapped type back to a
[DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html).
- `
  ``
  ``
  `

  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable#/s:17FirebaseFirestore19DocumentIDWrappableP4wrapyxSo20FIRDocumentReferenceCKFZ)

  `
  `  
  Creates a new instance by converting from the given [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html).  

  #### Declaration

  Swift  

      static func wrap(_ documentReference: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html) throws -> Self