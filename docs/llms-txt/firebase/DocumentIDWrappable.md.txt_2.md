# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable.md.txt

# FirebaseFirestoreSwift Framework Reference

# DocumentIDWrappable

    public protocol DocumentIDWrappable

A type that can initialize itself from a Firestore `DocumentReference`,
which makes it suitable for use with the `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID.html` property wrapper.

Firestore includes extensions that make `String` and `DocumentReference`
conform to `DocumentIDWrappable`.

Note that Firestore ignores fields annotated with `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID.html` when writing
so there is no requirement to convert from the wrapped type back to a
`DocumentReference`.
- `


  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable#/s:22FirebaseFirestoreSwift19DocumentIDWrappableP4wrapyxSo20FIRDocumentReferenceCKFZ)


  ` Creates a new instance by converting from the given `DocumentReference`.

  #### Declaration

  Swift

      static func wrap(_ documentReference: DocumentReference) throws -> Self