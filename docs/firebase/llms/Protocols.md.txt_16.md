# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols.md.txt

# FirebaseFirestoreSwift Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [DocumentIDWrappable](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable)


  ` A type that can initialize itself from a Firestore `DocumentReference`,
  which makes it suitable for use with the `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID` property wrapper.

  Firestore includes extensions that make `String` and `DocumentReference`
  conform to `DocumentIDWrappable`.

  Note that Firestore ignores fields annotated with `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID` when writing
  so there is no requirement to convert from the wrapped type back to a
  `DocumentReference`.

  #### Declaration

  Swift

      public protocol DocumentIDWrappable

- `


  ### [ServerTimestampWrappable](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/ServerTimestampWrappable)


  ` A type that can initialize itself from a Firestore Timestamp, which makes
  it suitable for use with the `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ServerTimestamp` property wrapper.

  Firestore includes extensions that make `Timestamp` and `Date` conform to
  `ServerTimestampWrappable`.

  #### Declaration

  Swift

      public protocol ServerTimestampWrappable