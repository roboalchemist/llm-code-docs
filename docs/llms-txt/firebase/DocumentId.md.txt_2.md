# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID.md.txt

# FirebaseFirestoreSwift Framework Reference

# DocumentID

    @propertyWrapper
    public struct DocumentID<Value: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable.html & Codable>:
      DocumentIDProtocol, Codable

    extension DocumentID: Equatable where Value: Equatable

    extension DocumentID: Hashable where Value: Hashable

A value that is populated in Codable objects with the `DocumentReference`
of the current document by the Firestore.Decoder when a document is read.

If the field name used for this type conflicts with a read document field,
an error is thrown. For example, if a custom object has a field `firstName`
annotated with `@DocumentID`, and there is a property from the document
named `firstName` as well, an error is thrown when you try to read the
document.

When writing a Codable object containing an `@DocumentID` annotated field,
its value is ignored. This allows you to read a document from one path and
write it into another without adjusting the value here.

NOTE: Trying to encode/decode this type using encoders/decoders other than
Firestore.Encoder leads to an error.
- `


  ### [init(wrappedValue:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/s:22FirebaseFirestoreSwift10DocumentIDV12wrappedValueACyxGxSg_tcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID.html#/s:22FirebaseFirestoreSwift10DocumentIDV12wrappedValuexSgvp value: Value?)

- `


  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/s:22FirebaseFirestoreSwift10DocumentIDV12wrappedValuexSgvp)


  ` Undocumented

  #### Declaration

  Swift

      public var wrappedValue: Value? { get set }

[## \`DocumentIDProtocol\` conformance](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/%60DocumentIDProtocol%60-conformance)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/s:22FirebaseFirestoreSwift18DocumentIDProtocolP4fromxSo20FIRDocumentReferenceCSg_tKcfc)


  `

  #### Declaration

  Swift

      public init(from documentReference: DocumentReference?) throws

[## \`Codable\` implementation.](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/%60Codable%60-implementation.)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws

- `


  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID#/s:SE6encode2toys7Encoder_p_tKF)


  `

  #### Declaration

  Swift

      public func encode(to encoder: Encoder) throws