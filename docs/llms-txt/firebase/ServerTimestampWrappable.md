# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/ServerTimestampWrappable.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable.md.txt

# FirebaseFirestore Framework Reference

# ServerTimestampWrappable

    public protocol ServerTimestampWrappable

A type that can initialize itself from a Firestore Timestamp, which makes
it suitable for use with the [@ServerTimestamp](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp.html) property wrapper.

Firestore includes extensions that make `Timestamp` and `Date` conform to
`ServerTimestampWrappable`.
- `
  ``
  ``
  `

  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable#/s:17FirebaseFirestore24ServerTimestampWrappableP4wrapyxSo12FIRTimestampCKFZ)

  `
  `  
  Creates a new instance by converting from the given `Timestamp`.  

  #### Declaration

  Swift  

      static func wrap(_ timestamp: Timestamp) throws -> Self

  #### Parameters

  |-------------------|--------------------------------------|
  | ` `*timestamp*` ` | The timestamp from which to convert. |

- `
  ``
  ``
  `

  ### [unwrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable#/s:17FirebaseFirestore24ServerTimestampWrappableP6unwrapySo12FIRTimestampCxKFZ)

  `
  `  
  Converts this value into a Firestore `Timestamp`.  

  #### Declaration

  Swift  

      static func unwrap(_ value: Self) throws -> Timestamp

  #### Return Value

  A `Timestamp` representation of this value.